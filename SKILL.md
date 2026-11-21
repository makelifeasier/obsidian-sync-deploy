---
name: obsidian-sync-deploy
description: Deploy, migrate, recover, or verify Obsidian vault sync across Windows, Android, and iPhone/iPad using GSync and Google Drive, including Google OAuth production and Gemini Helper shared note retrieval. Use for the whole stack or for a new device, missing mobile files, sign-in failures, or stale note citations. Not for general Obsidian note writing or unrelated deployments.
---

# Obsidian 三端同步与笔记检索

先识别任务是全新部署、接入新设备、迁移还是修复。确认现有库、设备、预算、同步目录和 检索范围。优先读取本机配置和已有验收记录，能从证据确认的事项直接推进。把文件同步、OAuth 授权和 Gemini 索引视为三个独立状态，分别验证。

- 全新部署或迁移读 [同步与设备](references/sync.md)，涉及 Google 登录或每七天过期时读 [OAuth](references/oauth.md)。
- 配置 Gemini、索引或问答时读 [笔记检索](references/retrieval.md)。
- 接入新设备、检查空文件列表、收尾交付时读 [验收与排错](references/acceptance.md)。

全量部署先做独立快照并验证可恢复性，排查同一库的其他同步工具，再用隔离测试库验证同步行为。正式库先确认允许同步的文件范围和排除规则，再接入各设备。用同一 Google 账号连同一云端目录，各设备独立授权。默认沿用用户已确定的免费方案、前台同步和本地敏感资料边界。只有实际任务需要且已有授权时，才发布公共说明页、切换 OAuth 或发送经审核的笔记到 Gemini。启用检索前展示拟上传范围，保留已批准的数据边界。

凭据从设备本地设置或密钥存储读取和写入，仅在所需的官方流程中使用。报告、截图、终端输出和安装包须避开密钥、令牌、授权码和笔记正文。新设备各自登录。正式库及原有设备够用时，优先修复现有配置。

用接口结果验证云端，用真实设备区分本地文件存在与 UI 可见。记录通过、失败及未验证项目，区分模拟测试、历史验收与本轮实机结果。以需求选用验证步骤，无须为单项修复重新部署全套。
