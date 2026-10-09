# GitHub 上传指南（新手版）

## 方法一：使用 GitHub Desktop（推荐）

1. 注册或登录 https://github.com/ 。
2. 安装 GitHub Desktop：https://desktop.github.com/ ，然后登录 GitHub 账号。
3. 将项目 ZIP 解压到一个容易找到的位置，例如桌面上的 `image-processing-lab` 文件夹。
4. 在 GitHub Desktop 中选择 **File → Add Local Repository…**。
5. 选择刚才解压出来的 `image-processing-lab` 文件夹。
   - 如果提示这不是 Git 仓库，选择 **create a repository** 或按提示在该文件夹中初始化仓库。
   - 如果需要创建仓库，名称填写 `image-processing-lab`，本地路径选择项目文件夹。
6. 在左下角的 Summary（摘要）填写 `Initial release`，点击 **Commit to main**。
7. 点击顶部的 **Publish repository**。
8. 仓库名称填写 `image-processing-lab`。如果希望所有人都能看到并使用，取消 **Keep this code private**，然后点击 **Publish repository**。
9. 发布完成后，点击 **View on GitHub**，就能看到项目网页。

## 发布前检查

- 不要上传密码、API 密钥、个人隐私文件或虚拟环境文件夹。
- 确认 `.gitignore` 文件在项目根目录中。
- README 中的示例克隆地址 `https://github.com/你的用户名/image-processing-lab.git` 只是占位符；发布后可以把“你的用户名”替换为自己的 GitHub 用户名。
- `assets/` 目前只有说明文件。如果之后有应用截图，可以放进这个文件夹，再提交一次更新。

## 更新项目

以后修改了代码，在 GitHub Desktop 左侧填写修改说明，点击 **Commit to main**，再点击 **Push origin**，更新就会同步到 GitHub。

## 让别人在线体验（可选）

代码发布到 GitHub 后，可以再使用 Streamlit Community Cloud 部署。部署时选择这个仓库和 `app.py` 作为主文件。依赖会从根目录的 `requirements.txt` 自动安装。
