## 声明

```python
# 定义函数
def add(x, y):
    return x + y

# 调用函数
add(3, 4)
```

```python
# 使用 lambda 关键字来定义一个匿名函数，效果与 add 函数一样
add = lambda x, y: x + y
```

## 参数

### 参数默认值

Python 函数的参数默认值只会在函数定义阶段被创建一次，之后不论再调用多少次，函数内拿到的默认值都是同一个对象。

```python
def append_value(value, items=[]):
    """向 items 列表中追加内容，并返回列表"""
    items.append(value)
    return items
append_value('foo') # ['foo']
append_value('bar') # ['foo', 'bar']
```

### 定义仅限关键字参数

```python
def query_users(limit, offset, min_followers_count, include_profile):
    """查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    """
query_users(limit = 20, offset = 0, min_followers_count = 100, include_profile = True)
# 关键字参数可以不严格按照函数定义参数的顺序来传递
query_users(min_followers_count = 100, include_profile = True, limit = 20, offset = 0)
```

ps：通过在参数列表中插入 * 符号，该符号后的所有参数都变成了“仅限关键字参数”（keyword-only argument）。如果调用方仍然想用位置参数来提供这些参数值，程序就会抛出错误。


### 仅限位置参数

“仅限位置参数”的使用方式是在参数列表中插入/符号。比如 `def query_users(limit, offset, /, min_followers_count, include_profile)` 表示，limit 和 offset 参数都只能通过位置参数来提供。

## 返回值

- None 也是不带任何 return 语句的函数的默认返回值

## functools

- functools.partial()
- functools.lru_cache()
