# 错误处理

Rust 将错误分为两大类：可恢复的（recoverable）和 不可恢复的（unrecoverable）错误。

## 不可恢复的错误

Rust 程序执行出错时会自动调用 `panic!` 宏，执行后程序会打印出一个错误信息，并展开清理栈数据，然后退出。

- 主动调用

    ```rust
    fn main() {
        panic!("crash and burn");
    }
    ```

- 程序 bug

    ```rust
    fn main() {
        let v = vec![1, 2, 3];

        v[99];
    }
    ```

### backtrace

启动命令设置 `RUST_BACKTRACE=1` 可以开启 backtrace，这样在程序出错时会显示详细的错误日志。

```shell
$ RUST_BACKTRACE=1 cargo run
```

### 展开 vs 终止

- 展开（unwinding）：当出现 panic 时，程序默认会开始 展开（unwinding），这意味着 Rust 会回溯栈并清理它遇到的每一个函数的数据，不过这个回溯并清理的过程有很多工作。
- 终止（abort）：不清理数据就退出程序，那么程序所使用的内存需要由操作系统来清理。

ps：如果你需要项目的最终二进制文件越小越好，panic 时通过在 Cargo.toml 的 `[profile]` 部分增加 `panic = 'abort'`，可以由展开切换为终止。

```toml
# 只在 release 模式使用终止模式
[profile.release]
panic = 'abort'
```

## 可恢复错误

大部分错误并没有严重到需要程序完全停止执行，Rust 可以用 Result 处理可恢复的错误。

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

### 处理错误

可通过查询 [Rust 标准库 API 文档](https://doc.rust-lang.org/std/index.html) 来确认哪些 API 会返回 Result。

- [`std::fs::File::open()`](https://doc.rust-lang.org/std/fs/struct.File.html#method.open)：打开文件

```rust
use std::fs::File;
use std::io::Error;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error)
            }
        },
    };
}
```

### 闭包方式

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
}
```

### unwrap 和 expect

unwrap 和 expect 会返回 Ok 中的值，如果 Result 是成员 Err，unwrap 和 expect 会为我们调用 panic!。

unwrap

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").unwrap();
}
```

expect

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
}
```

### 传播错误

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}
```

### 传播错误的简写：? 运算符

```rust
use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}
```
