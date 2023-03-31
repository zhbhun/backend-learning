from typing import List

# 在 Python 3.5 版本以后，可以用类型注解功能来直接注明变量类型。
def remove_invalid1(items: List[int]): ➊
    """剔除 items 里面无效的元素"""
    ... ...

# Python 官方推荐的 Sphinx 格式文档
def remove_invalid2(items):
    """剔除 items 里面无效的元素

    :param items: 待剔除对象
    :type items: 包含整数的列表，[int, ...]
    """

