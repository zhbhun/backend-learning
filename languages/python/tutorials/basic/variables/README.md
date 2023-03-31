## 常见用法

- 声明：`author = 'piglei'`
- 多变量赋值：`author, reader = 'piglei', 'raymond'`
- 变量交换：`author, reader = reader, author`
- 变量解包：

    ```python
    # 注意：左侧变量的个数必须和待展开的列表长度相等，否则会报错
    usernames = ['piglei', 'raymond']
    author, reader = usernames

    # 多层嵌套
    attrs = [1, ['piglei', 100]]
    user_id, (username, score) = attrs

    # 动态解包
    data = ['piglei', 'apple', 'orange', 'banana', 100]
    username, *fruits, score = data
    # 切片赋值
    username, fruits, score = data[0], data[1:-1], data[-1]
    # 两种变量赋值方式完全等价
    ```

## 类型注释

```python
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
```

ps：类型注解配合 mypy 等静态类型检查工具，能提升代码正确性
