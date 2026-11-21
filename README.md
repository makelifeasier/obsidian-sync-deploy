# Obsidian 三端部署手册

用 GSync 和 Google Drive 同步 Windows、Android 与 iPhone/iPad 上的 Obsidian 笔记库。手册也覆盖 Google OAuth 正式发布，以及用 Gemini Helper 在多端查询同一份笔记索引。

从 [SKILL.md](SKILL.md) 按当前任务选读。全新部署先看[同步与设备](references/sync.md)。如果手机看不到文件，直接看[验收与排错](references/acceptance.md)。

仓库附有一个 Python 3.11+ 校验脚本，用于比较两份本地库副本：

```bash
python scripts/compare_vaults.py source-vault target-vault
```

默认只显示文件计数和差异数量。可以用 `--approved-manifest` 指定允许同步的路径，用 `--list-paths` 查看差异详情。对比时请使用稳定的副本，并按手册明确排除私人资料。
