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

## 对象

## 转换

### 隐式类型转换

- 布尔 =》数值：True == 1，False == 0

### 强制类型转换

- `int()`
- `float()`
