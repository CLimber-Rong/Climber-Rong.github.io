'''
Name: 
Copyright: 
Author: 
Date: 12/07/24 14:53
Description: 
'''
import markdown
import os

paths = os.walk('./')

for path, tmp2, file_list in paths:
    for i in file_list:
        if i.endswith('.md'):
            html_path = 'stamon_'+i[0:-3] + '.html'
            fin = open(os.path.join(path, i), 'r', encoding='utf8')
            fout = open(os.path.join(path, html_path), 'w', encoding='utf8')
            fout.write('''<!DOCTYPE html>
    <html>
    <meta charset="utf-8" />
    <title></title>

    <!-- 新 Bootstrap4 核心 CSS 文件 -->
    <link
        rel="stylesheet"
        href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css"
    />
    <!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

    <!-- bootstrap.bundle.min.js 用于弹窗、提示、下拉菜单，包含了 popper.min.js -->
    <script src="https://cdn.bootcdn.net/ajax/libs/popper.js/1.15.0/umd/popper.min.js"></script>

    <!-- 最新的 Bootstrap4 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </head>

    <body>
    <nav class="navbar navbar-expand-sm bg-light justify-content-center">
        <a class="navbar-brand" href="#">
        <img src="https://CLimber-Rong.github.io/image/icon.png" alt="logo" style="width: 40px" />
        </a>
        <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" href="https://CLimber-Rong.github.io/index.html">首页</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://CLimber-Rong.github.io/about.html">关于</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://CLimber-Rong.github.io/doc.html">文档</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://CLimber-Rong.github.io/project.html">项目</a>
        </li>
        </ul>
    </nav>
    <br><div style=\"margin: auto;\">'''
                    +markdown.markdown(fin.read())
                    +''' </div> </body>
    </html>'''
            )