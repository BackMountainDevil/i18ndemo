# i18n
## 干啥
python 借助 xgettext 国际化和本地化开发案例 demo。

详细的 [wiki](https://backmountaindevil.github.io/#/code/python/i18n)

## 三秒运行

```bash
find . -iname "*.py" | xargs xgettext
mkdir -p locale/zh_CN/LC_MESSAGES
cp messages.po locale/zh_CN/LC_MESSAGES/zh_CN.po
# 翻译 po
msgfmt -o locale/zh_CN/LC_MESSAGES/zh_CN.mo locale/zh_CN/LC_MESSAGES/zh_CN.po
```

## 文件结构

```bash
.
├── fun.py
├── LICENSE
├── locale
│   └── zh_CN
│       └── LC_MESSAGES
│           ├── zh_CN.mo
│           └── zh_CN.po
├── main.py
├── messages.po
├── model
│   ├── __init__.py
│   └── nice.py
└── README.md
```

# 非包的外部模块引用
## 同级目录

```bash
.
├── fun.py
├── main.py
└── README.md
```

```python
# File: fun.py
def fun():
  print("Have a funny day")
```
运行上面的代码没有输出

```python
# File: main.py
import fun

fun.fun()
```
运行上面的代码会输出 “Have a funny day”.

上面的 main 代码也可以这样写
```python
from fun import *
fun()
```

## 跨级

```bash
├── main.py
├── model
│   ├── __init__.py
│   ├── nice.py
```
`__init__.py` 是为了让编译器认为这是一个模块，啥也不写。

```python
# File: model/nice.py
def nice():
  print("Have a nice day")
```
运行上面的代码没有输出

```python
# File: main.py
from model.nice import *

nice()
```
运行上面的代码会输出 “Have a nice day”

## 