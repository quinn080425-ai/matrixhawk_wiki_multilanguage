# -*- coding: utf-8 -*-
#
# ArduPilot documentation build configuration file
#

import os
import sys

# -----------------------------------------------------------------------------
# 1. 基础路径配置 (保持不变)
# -----------------------------------------------------------------------------
# Import common configuration information as "common_conf"
# Ensure repository root is added to sys.path reliably
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)  # noqa: E402
import common_conf  # noqa: E402


# -----------------------------------------------------------------------------
# 2. 核心 Sphinx 配置
# -----------------------------------------------------------------------------
extensions = common_conf.extensions

# Add any paths that contain templates here, relative to this directory.
templates_path = [os.path.join(os.path.dirname(__file__), '_templates')]

source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'


# -----------------------------------------------------------------------------
# 3. 主题配置 (关键修改点)
# -----------------------------------------------------------------------------
# 既然我们已经修复了 setup.py 并注册了 entry_points
# Sphinx 会自动从 Python 环境中找到这个主题，无需指定 html_theme_path
html_theme = 'matrixhawk_sphinx_rtd_theme'

try:
    # 尝试导入我们安装好的包
    import matrixhawk_sphinx_rtd_theme
    
    # 获取包的物理路径 (就是你刚才列表里显示的那个路径)
    theme_path = os.path.dirname(os.path.dirname(matrixhawk_sphinx_rtd_theme.__file__))
    
    # 告诉 Sphinx: "别去注册表里查了，主题就在这个文件夹里！"
    html_theme_path = [theme_path]
    
    print(f"✅ 主题路径锁定: {theme_path}")

except ImportError:
    print("❌ 致命错误: Python 找不到 matrixhawk_sphinx_rtd_theme 包")
    print("请运行: pip install -e ./submodules/matrixhawk_sphinx_rtd_theme")


# -----------------------------------------------------------------------------
# 4. 项目信息
# -----------------------------------------------------------------------------
project = u'matrixhawk user manual'
copyright = u'2024, ArduPilot Dev Team. Modifications and New Content © 2025, BZUAV Devteam'
author = u'BZUAV Dev Team'

version = u'0.1'
release = u'0.0.1'
language = 'en'

exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True


# -----------------------------------------------------------------------------
# 5. HTML 输出选项
# -----------------------------------------------------------------------------
html_short_title = 'ardupilot'
html_favicon = '../../images/favicon_default.ico'
html_static_path = ['_static']

html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
htmlhelp_basename = 'ArduPilotdoc'


# -----------------------------------------------------------------------------
# 6. 上下文补丁 (必须保留！)
# -----------------------------------------------------------------------------
html_context = common_conf.html_context

# 【重要补丁】
# 解决主题模板报错 "UndefinedError: 'navigation_depth' is undefined"
# 这是一个全局注入，确保侧边栏能正确渲染
if html_context is None:
    html_context = {}
html_context['navigation_depth'] = 4


# -----------------------------------------------------------------------------
# 7. 其他格式输出 (LaTeX / Epub 等)
# -----------------------------------------------------------------------------
latex_elements = {
    # 'papersize': 'letterpaper',
    # 'pointsize': '10pt',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'ArduPilot.tex', u'ArduPilot Documentation',
     u'ArduPilot Dev Team', 'manual'),
]

man_pages = [
    (master_doc, 'ardupilot', u'ArduPilot Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'ArduPilot', u'ArduPilot Documentation',
     author, 'ArduPilot', 'One line description of project.',
     'Miscellaneous'),
]

# Epub settings
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']

# External JS (Analytics etc)
html_js_files = [
    ('https://plausible.ardupilot.org/js/script.outbound-links.js', {"data-domain": "ardupilot.org", "defer": "defer"}),
]

# Intersphinx mapping config (done globally)
intersphinx_mapping = common_conf.intersphinx_mapping

def setup(app):
    common_conf.setup(app)