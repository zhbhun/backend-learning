# 异常

- LBYL(Look before you leap)：就是在执行一个可能会出错的操作时，先做一些关键的条件判断，仅当条件满足时才进行操作。
- EAFP(easier to ask for forgiveness than permission)：EAFP 指不做任何事前检查，直接执行操作，但在外层用try来捕获可能发生的异常。如果还用下雨举例，这种做法类似于“出门前不看天气预报，如果淋雨了，就回家后洗澡吃感冒药”。

ps：还有一类没有异常处理机制的语言，例如：go，JavaScript 的异步调用错误等，它们采用返回多个值的方式来输出错误信息。但是，这种处理方式在有多层调用的场景，处理起来比较麻烦。

## 异常处理

```python
# 把更精确的 except 语句放在前面
def safe_int(value):
    """尝试把输入转换为整数"""
    try:
        return int(value)
    except TypeError:
        # 当某类异常被抛出时，将会执行对应 except 下的语句
        print(f'type error: {type(value)} is invalid')
    except ValueError:
        # 你可以在一个 try 语句块下写多个 except
        print(f'value error: {value} is invalid')
    finally:
        # finally 里的语句，无论如何都会被执行，哪怕已经执行了return
        print('function completed')
```

### 使用 else 分支

异常捕获语句里的 else 表示：仅当 try 语句块里没抛出任何异常时，才执行 else 分支下的内容，效果就像在 try 最后增加一个标记变量一样。

```python
try:
    sync_profile(user.profile, to_external=True)
except Exception as e:
    print("Error while syncing user profile")
else:
    send_notification(user, 'profile sync succeeded')
```

### 使用空 raise 语句

当一个空 raise 语句出现在 except 块里时，它会原封不动地重新抛出当前异常。

```python
def incr_by_key(d, key):
    try:
        d[key] += 1
    except KeyError:
        print(f'key {key} does not exists, re-raise the exception')
        raise
```

## 上下文管理器

```python
class DummyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__会在进入管理器时被调用，同时可以返回结果
        # 这个结果可以通过 as 关键字被调用方获取
        #
        # 此处返回一个增加了随机后缀的name
        return f'{self.name}-{random.random()}'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__会在退出管理器时被调用
        # exc_type：异常的类型
        # exc_value：异常对象
        # traceback：错误的堆栈对象
        # 在代码执行时，假如 with 管辖的上下文内没有抛出任何异常，那么当解释器触发 __exit__ 方法时，上面的三个参数值都是 None；但如果有异常抛出，这三个参数就会变成该异常的具体内容。此时，程序的行为取决于 __exit__ 方法的返回值。如果 __exit__ 返回了 True，那么这个异常就会被当前的 with 语句压制住，不再继续抛出，达到“忽略异常”的效果；如果 __exit__ 返回了False，那这个异常就会被正常抛出，交由调用方处理。
        print('Exiting DummyContext')
        return False

with DummyContext('foo') as name:
    print(f'Name: {name}')
```

### 使用 contextmanager 装饰器

@contextmanager 位于内置模块 contextlib 下，它可以把任何一个生成器函数直接转换为一个上下文管理器。

```python
from contextlib import contextmanager
@contextmanager
def create_conn_obj(host, port, timeout=None):
    """创建连接对象，并在退出上下文时自动关闭"""
    conn = create_conn(host, port, timeout=timeout)
    try:
        yield conn # 以 yield 关键字为界，yield 前的逻辑会在进入管理器时执行（类似于__enter__），yield 后的逻辑会在退出管理器时执行（类似于__exit__）
    finally: 
        conn.close() # 如果要在上下文管理器内处理异常，必须用 try 语句块包裹 yield 语句
```
