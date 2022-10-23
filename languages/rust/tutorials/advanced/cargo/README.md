## 初始化项目

```shell
cargo init # 当前目录
cargo new # 新建目录
```

## 安装依赖

- 全局

    ```shell
    npm install [dep]
    ```

- 本地

    ```shell
    cargo install cargo-edit # 首次安装
    cargo add dep # 添加依赖
    cargo rm dep # 删除依赖
    cargo upgrade dep # 升级依赖
    ```

## 运行测试

```shell
cargo test
```

## 构建运行

```shell
cargo build # 构建
cargo run # 构建 + 运行
cargo bench # 基准测试
cargo clean # 清除构建
cargo doc # 生成文档
```

ps：不支持类似 npm 的自定义脚本，可以使用 [just](https://github.com/casey/just)、cargo-make 和 cargo-cmd 代替。

## 工作区间

默认支持，可以使用 [cargo-workspaces](https://github.com/pksunkara/cargo-workspaces) 来协助。

```shell
cargo workspaces init # 初始化
cargo workspaces create # 创建新 crate
cargo workspaces list # 列出所有的 crate
cargo workspaces exec # 执行任务
cargo workspaces version # 升级任务
```


## 参考文献

- [From npm to cargo](https://github.com/wasmflow/node-to-rust/blob/master/book/chapters/chapter-2-cargo.adoc)
