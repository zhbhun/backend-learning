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
