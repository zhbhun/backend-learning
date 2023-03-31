## 数值

- int：整数
- float：浮点数
- complex：复数

```python
# 定义一个整型
score = 100
# 定义一个浮点型
temp = 37.2
# 定义一个复数
com = 1+2j
```

## 布尔

- True
- False

## 字符

- 拼接

    ```python
    # += 
    words_str += f'Value: {i + 1}'


    # 列表操作
    words = ['Numbers(1-10):']
    for i in range(10):
        words.append(f'Value: {i + 1}')
    print('\n'.join(words))
    ```

- 切片

    ```python
    s[::-1] # 反转字符串
    ```

- 遍历

    ```python
    s = 'Hello, world!'
    for c in s:
        print(c)
    ```

- 格式化

    ```python
    username, score = 'piglei', 100
    # 1. C 语言风格格式化
    print('Welcome %s, your score is %d' % (username, score))
    # 2. str.format
    print('Welcome {}, your score is {:d}'.format(username, score))
    # 3. f-string，最短最直观
    print(f'Welcome {username}, your score is {score:d}')
    # 输出：
    # Welcome piglei, your score is 100
    ```

- 工具函数

    - isdigit：判断是否是数字字符串
    - join
    - split
    - startswith
    - partition
    - translate

## 容器

### 列表

列表是一种有序的可变容器类型

- 构造

    ```python
    # 字面量
    numbers = [1, 2, 3, 4]

    # 构造
    list('foo') # ['f', 'o', 'o']
    ```

- 添加：`numbers.append(1)`
- 访问：`numbers[2]`
- 切片：`numbers[1:]`
- 删除：`del numbers[1:]`
- 遍历

    ```python
    names = ['foo', 'bar']
    for index, s in enumerate(names):
        print(index, s)

    for index, s in enumerate(names, start=10):
        print(index, s)
    ```

- 列表推导式

    ```python
    # 用一个表达式完成4件事情
    #
    # 1. 遍历旧列表：for n in numbers
    # 2. 对成员进行条件过滤：if n % 2 == 0
    # 3. 修改成员： n * 100
    # 4. 组装新的结果列表
    #
    results = [n * 100 for n in numbers if n % 2 == 0]

    # 等价于下面的逻辑
    def remove_odd_mul_100(numbers):
        """剔除奇数并乘以100"""
        results = []
        for number in numbers:
            if number % 2 == 1:
                continue
            results.append(number * 100)
        return results
    ```

### 元组

元组是一种有序的不可变容器类型。

- 构造：

    - `t = (0, 1, 2)`
    - `t = 0, 1, 2`
    - `tuple('012')`：`('0', '1', '2')`

- 访问：`t[0]`
- 元组推导式：

    ```python
    results = tuple((n * 100 for n in range(10) if n % 2 == 0)) # (0, 200, 400, 600, 800)
    ```

- 具名元组

    ```python
    from collections import namedtuple

    Rectangle = namedtuple('Rectangle', 'width,height')

    rect = Rectangle(100, 20) ➊
    rect = Rectangle(width=100, height=20) ➋
    print(rect[0]) # 100
    print(rect.width) # 100
    rect.width += 1 # AttributeError: can't set attribute

    # 在 Python 3.6 版本以后，除了使用 namedtuple() 函数以外，你还可以用 typing.NamedTuple 和类型注解语法来定义具名元组类型
    class Rectangle(NamedTuple):
        width: int
        height: int

    rect = Rectangle(100, 20)
    ```

### 字典

跟列表和元组比起来，字典是一种更为复杂的容器结构。它所存储的内容不再是单一维度的线性序列，而是多维度的 key: value 键值对。

- 构造

    ```python
    movie = {'name': 'Burning', 'type': 'movie', 'year': 2018}
    ```

- 访问：`movie['year']`

    ps：当用不存在的键访问字典内容时，程序会抛出 KeyError 异常

    ```python
    # 条件判断
    if 'rating' in movie:
        rating = movie['rating']
    else:
        rating = 0
    
    # 捕获 KeyError
    try:
        rating = movie['rating']
    except KeyError:
        rating = 0

    # get
    movie.get('rating', 0)
    ```

- 修改：`movie['rating'] = 10`

    ps：当用不存在的键访问字典内容时，程序会抛出 KeyError 异常

    ```python
    d = {'title': 'foobar'}

    # 捕获 KeyError
    try:
        d['items'].append(value)
    except KeyError:
        d['items'] = [value]

    # dict.setdefault(key, default)
    d.setdefault('items', []).append('foo')
    ```
- 删除

    ```python
    # 捕获 KeyError
    try:
        del d[key]
    except KeyError:
        # 忽略 key 不存在的情况
        pass

    # pop
    d.pop(key, None)
    ```

- 遍历：

    ```python
    # 遍历获取字典所有的key
    for key in movie:
        print(key, movie[key])

    # 一次获取字典的所有 key: value 键值对
    for key, value in movie.items():
        print(key, value)
    ```

- 字典推导式

    ```python
    d1 = {'foo': 3, 'bar': 4}
    {key: value * 10 for key, value in d1.items() if key == 'foo'} # {'foo': 30}
    ```

## 集合

集合是一种无序的可变容器类型，它最大的特点就是成员不能重复。

- 构造：

    ```python
    # 字面量
    fruits = {'apple', 'orange', 'apple', 'pineapple'}

    # set
    empty_set = set()
    ```

- 添加：`fruits.add('...')`
- 运算

    ```python
    fruits_1 = {'apple', 'orange', 'pineapple'}
    fruits_2 = {'tomato', 'orange', 'grapes', 'mango'}

    # intersection
    fruits_1 & fruits_2 # {'orange'}
    fruits_1.intersection(fruits_2) # {'orange'}

    # union
    fruits_1 | fruits_2 # {'mango', 'orange', 'grapes', 'pineapple', 'apple', 'tomato'}
    fruits_1.union(fruits_2)

    # difference
    fruits_1 - fruits_2 # {'apple', 'pineapple'}
    fruits_1.difference(fruits_2)
...
    ```

- 不可变集合：`empty_fruits = frozenset(['apple', 'orange', 'apple', 'pineapple'])`
- 集合推导式

    ```python
    nums = [1, 2, 2, 4, 1]
    {n for n in nums if n < 3} # {1, 2}
    ```

- 可哈希对象：集合里只能存放“可哈希”（hashable）的对象。假如把不可哈希的对象（比如上面的列表）放入集合，程序就会抛出 TypeError 异常。

    ps：不可变的内置类型都是可哈希的，而可变的内置类型都无法正常计算哈希值，例如：列表、集合和字典等都是可变的内置类型。

    1. 所有的不可变内置类型，都是可哈希的，比如str、int、tuple、frozenset等；
    2. 所有的可变内置类型，都是不可哈希的，比如dict、list等；
    3. 对于不可变容器类型(tuple, frozenset)，仅当它的所有成员都不可变时，它自身才是可哈希的；
    4. 用户定义的类型默认都是可哈希的。

## 转换

### 隐式类型转换

- 布尔 =》数值：True == 1，False == 0

### 强制类型转换

- `int()`
- `float()`

## 拷贝

- 浅拷贝

    ```python
    import copy

    nums = [1, 2, 30, 4]
    nums_copy = copy.copy(nums)
    nums[2] = 30 # 修改不再相互影响
    nums, nums_copy # ([1, 2, 30, 4], [1, 2, 3, 4])

    # 用推导式也可以产生一个浅拷贝对象
    d = {'foo': 1}
    d2 = {key: value for key, value in d.items()}
    d['foo'] = 2
    d, d2 # ({'foo': 2}, {'foo': 1})
    ```

- 深拷贝：`copy.deepcopy(items)`
