"""Compare stable local vault copies without printing note contents or hashes."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath


def relative_path(value):
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or ":" in path.as_posix() or ".." in path.parts or not path.parts:
        raise ValueError(f"Invalid relative vault path: {value!r}")
    return path.as_posix()


def visible_files(root, excluded_files, excluded_folders):
    result = {}
    for folder, directories, files in os.walk(root, onerror=raise_walk_error):
        base = Path(folder)
        directories[:] = [
            name for name in directories
            if not name.startswith(".")
            and (base / name).relative_to(root).as_posix() not in excluded_folders
            and not (base / name).is_symlink()
            and not getattr(base / name, "is_junction", lambda: False)()
        ]
        for name in files:
            item = base / name
            relative = item.relative_to(root).as_posix()
            if name.startswith(".") or relative in excluded_files or item.is_symlink():
                continue
            if item.is_file():
                result[relative] = item
    return result


def raise_walk_error(error):
    raise error


def digest(path):
    before = path.stat()
    with path.open("rb") as stream:
        checksum = hashlib.file_digest(stream, "sha256").digest()
    after = path.stat()
    if (before.st_size, before.st_mtime_ns, before.st_ino) != (
        after.st_size, after.st_mtime_ns, after.st_ino
    ):
        raise OSError("A file changed during hashing. Retry with stable vault copies.")
    return checksum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--exclude", action="append", default=[], help="Exact file or folder ending in /")
    parser.add_argument("--approved-manifest", type=Path, help="JSON array of approved relative paths")
    parser.add_argument("--list-paths", action="store_true", help="Include paths for differences")
    args = parser.parse_args()

    try:
        source = args.source.resolve(strict=True)
        target = args.target.resolve(strict=True)
        if not source.is_dir() or not target.is_dir() or source == target:
            raise ValueError("Use two distinct vault directories.")
        excluded_files = {relative_path(p) for p in args.exclude if not p.endswith(("/", "\\"))}
        excluded_folders = {relative_path(p) for p in args.exclude if p.endswith(("/", "\\"))}
        left = visible_files(source, excluded_files, excluded_folders)
        right = visible_files(target, excluded_files, excluded_folders)
        expected = set(left)
        if args.approved_manifest:
            entries = json.loads(args.approved_manifest.read_text(encoding="utf-8-sig"))
            if not isinstance(entries, list) or not all(isinstance(p, str) for p in entries):
                raise ValueError("The manifest must be a JSON array of relative paths.")
            expected = {relative_path(p) for p in entries}
        differences = {
            "missing_from_source": sorted(expected - left.keys()),
            "missing_from_target": sorted(expected - right.keys()),
            "extra_in_target": sorted(right.keys() - expected),
            "content_mismatch": sorted(
                p for p in expected & left.keys() & right.keys()
                if digest(left[p]) != digest(right[p])
            ),
        }
    except (OSError, ValueError) as error:
        parser.exit(2, f"Comparison failed ({type(error).__name__}). Check inputs and access.\n")

    match = not any(differences.values())
    report = {"match": match, "expected": len(expected), "target_files": len(right)}
    report.update({name: len(paths) for name, paths in differences.items()})
    if args.list_paths:
        report["paths"] = differences
    print(json.dumps(report, ensure_ascii=True))
    return 0 if match else 1


if __name__ == "__main__":
    raise SystemExit(main())
