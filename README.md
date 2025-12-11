# matrixhawk User Manual Documentation

这是 matrixhawk 无人机的用户手册文档项目。本项目基于 Sphinx 构建，并使用自定义的 `matrixhawk_sphinx_rtd_theme` 主题。

## 📋 目录结构说明

- **source/**: 文档源代码 (.rst 文件)
- **submodules/**: 包含外部依赖（如自定义主题）的 Git 子模块
- **build/**: 编译生成的 HTML 文件输出目录

## 🚀 快速开始 (Getting Started)

### 1. 克隆项目

由于本项目包含子模块（主题），请务必使用 `--recursive` 参数来克隆，否则主题文件夹会是空的。

```bash
# 克隆主项目及其所有子模块
git clone --recursive [https://github.com/YourUsername/matrixhawk_wiki.git](https://github.com/YourUsername/matrixhawk_wiki.git)

# 进入项目目录
cd matrixhawk_wiki

注意：如果你已经克隆了项目但忘记加 --recursive，请运行以下命令修复：

Bash

git submodule update --init --recursive

2. 环境配置
建议使用 Python 虚拟环境，以避免污染全局环境。

Bash

# 创建虚拟环境 (Windows)
python -m venv .venv
.venv\Scripts\activate

# 创建虚拟环境 (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

3. 安装依赖 (一键安装)
我们使用 requirements.txt 管理所有依赖，包括本地的自定义主题。这将自动以“可编辑模式”安装子项目。

Bash

pip install -r requirements.txt
4. 编译文档
安装完成后，即可构建 HTML 文档：

Bash

# macOS / Linux
make html

# Windows
make.bat html
编译完成后，打开 build/html/index.html 即可预览。

🛠 维护与更新
更新子模块 (主题)
如果 matrixhawk_sphinx_rtd_theme 主题仓库有更新，使用以下命令同步最新代码：

Bash

git submodule update --remote
清理缓存
如果遇到奇怪的编译报错（如 UndefinedError），请先尝试清理构建缓存：

Bash

make clean
make html
📝 贡献指南
Fork 本仓库

创建你的特性分支 (git checkout -b feature/AmazingFeature)

提交更改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

提交 Pull Request