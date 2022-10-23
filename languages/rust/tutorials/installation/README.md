一般推荐使用 [rustup](https://github.com/rust-lang/rustup/) 安装 rust 和 cargo，安装完成后通过下面的命令来检查。

- `rustup --version`

    rustup 用来管理安装 rust 和 cargo

- `rustc --version`

    rustc 是 rust 编译期

- `cargo --version`

    cargo 是 rust 构建工具和包管理器

- `rustfmt --version`

    自动格式化工具

## 检查更新

```shell
rustup check
rustup update
```
## Hello Rust

```shell
cd ./example
# fn main() {println!("Hello, world!");}
rustc ./hello.rs
./hello # Hello, world!
```

## Hello Cargo

```shell
cargo new hello_cargo # 创建基于 cargo 的项目
cd hello_cargo
cargo build # 构建项目
./target/debug/hello_cargo # 运行构建产物
cargo run # 构建 + 运行
cargo check # 在不生成二进制文件的情况下构建项目来检查错误
cargo build --release # 发布构建
```

## 编辑器设置

1. `ext install matklad.rust-analyzer`
2. Additional linting

    ```json
    {
      "rust-analyzer.checkOnSave.command": "clippy"
    }
    ```

3. Inlay hints can be disabled

    ```json
    {
      "rust-analyzer.inlayHints.enable": false,
      "rust-analyzer.inlayHints.chainingHints": false,
      "rust-analyzer.inlayHints.parameterHints": false
    }
    ```

4. Additional extensions

    - [vscode-lldb](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) - debug 工具
    - [better-toml](https://marketplace.visualstudio.com/items?itemName=bungcip.better-toml) - TOML 语法支持
    - [crates](https://marketplace.visualstudio.com/items?itemName=serayuzgur.crates) - 依赖更新提示
    - [search-crates-io](https://marketplace.visualstudio.com/items?itemName=belfz.search-crates-io) - 依赖自动完成

Refs:

- [Setting up Visual Studio Code](https://github.com/wasmflow/node-to-rust/blob/master/book/chapters/chapter-3-vscode.adoc)
