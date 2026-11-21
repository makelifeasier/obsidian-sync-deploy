# Google OAuth 正式发布

先检查现有项目、Drive API、OAuth 客户端类型、插件回调和实际账号。沿用能正常工作的项目。GSync 1.0.4 使用 Web application 类型和插件公开回调，必须精确匹配完整 URI。只有需要迁移回调时才同时调整控制台与设备。完整 Drive scope 的授权范围是整个 Drive，插件的同步目录配置只限制插件运行时的操作。向用户说明所请求的实际范围。

- Testing 下包含 Drive 访问的离线授权有固定七天限制。已有成功登录与长期可用是两件事。查看控制台 Audience 的实际状态。若 Publish app 禁用，按 Branding 的表单反馈补齐可公开访问的主页、隐私政策及所需域名，按实际需要补充使用条款。
- 可使用用户控制的免费静态托管。页面说明数据访问范围、用途、设备与 Drive 存储、回调、保留和撤销、Gemini 检索的数据流以及联系途径。仅部署经过审查的公开文件，检查 HTTPS 页面、链接和实发内容。不要把笔记、邮箱、OAuth 配置或令牌打包进站点。
- 将应用切换为 In production 后，区分发布状态和 Google 品牌或权限审核。个人自用是否适用验证例外，以 Google 当前官方说明及项目界面为准。让本人处理安全提示和账号登录。保留仍有效的旧配置直到新授权完成，避免提前退出或全局撤销影响其他设备。
- 各端执行一次 Sign in again，确认真正收到新授权，不能只凭原本的 Signed in。可在本地比较更新前后令牌是否变化，只输出布尔值。再验证各端令牌刷新成功且有权限访问预期 Drive 文件夹。iOS 若程序点击未打开浏览器，优先用本人触屏点击。记录仍可能因为其他原因要求重新授权。
- 控制台界面、政策有变时核对当前资料。优先使用 [Audience 说明](https://support.google.com/cloud/answer/15549945) 和 [Google 验证要求](https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification)。
