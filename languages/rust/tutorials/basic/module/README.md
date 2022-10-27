# 模块

- Crates ：一个模块的树形结构，它形成了库或二进制项目。

    crate 是 Rust 在编译时最小的代码单位。如果你用 rustc 而不是 cargo 来编译一个文件，编译器还是会将那个文件认作一个 crate。 crate 可以包含模块，模块可以定义在其他文件，然后和 crate 一起编译。

    crate 有两种形式：二进制项和库。

    - 二进制：可以被编译为可执行程序，比如一个命令行程序或者一个服务器。它们必须有一个 main 函数来定义当程序被执行的时候所需要做的事情。
    - 库：没有 main 函数，它们也不会编译为可执行程序，它们提供一些诸如函数之类的东西，使其他项目也能使用这些东西。

- 包（Packages）：Cargo 的一个功能，它允许你构建、测试和分享 crate。

    提供一系列功能的一个或者多个 crate。一个包会包含一个 Cargo.toml 文件，阐述如何去构建这些 crate。

    包中可以包含至多一个库 crate(library crate)。包中可以包含任意多个二进制 crate(binary crate)，但是必须至少包含一个 crate（无论是库的还是二进制的）。

    Cargo 遵循的一个约定：src/main.rs 就是一个与包同名的二进制 crate 的 crate 根。同样的，Cargo 知道如果包目录中包含 src/lib.rs，则包带有与其同名的库 crate，且 src/lib.rs 是 crate 根。crate 根文件将由 Cargo 传递给 rustc 来实际构建库或者二进制项目。通过将文件放在 src/bin 目录下，一个包可以拥有多个二进制 crate：每个 src/bin 下的文件都会被编译成一个独立的二进制 crate。

- 模块（Modules）和 use： 允许你控制作用域和路径的私有性。

## 声明模块

在 crate 根文件中，你可以声明一个新模块；比如，你用 `mod garden` 声明了一个叫做 `garden` 的模块。编译器会在下列路径中寻找模块代码：

- 内联，在大括号中，当 `mod garden` 后方不是一个分号而是一个大括号
- 在文件 src/garden.rs
- 在文件 src/garden/mod.rs

ps：`src/main.rs` 和 `src/lib.rs` 叫做 crate 根。之所以这样叫它们是因为这两个文件的内容都分别在 crate 模块结构的根组成了一个名为 crate 的模块，该结构被称为模块树（module tree）。

## 子模块

在除了 crate 根节点以外的其他文件中，你可以定义子模块。比如，你可能在 `src/garden.rs` 中定义了 `mod vegetables`;。编译器会在以父模块命名的目录中寻找子模块代码：

- 内联, 在大括号中，当 `mod vegetables` 后方不是一个分号而是一个大括号
- 在文件 src/garden/vegetables.rs
- 在文件 src/garden/vegetables/mod.rs

## 私有 vs 公用

一个模块里的代码默认对其父模块私有。为了使一个模块公用，应当在声明时使用 `pub mod` 替代 `mod`。为了使一个公用模块内部的成员公用，应当在声明前使用 `pub`。

## 引用路径

- 绝对路径：`crate::...`
- 相对路径：

    - 当前模块：`...`
    - seft：`seft::`
    - super：`super::`

## use 关键字

使用 use 关键字可以将子模块的公共项引入作用域，然后调用该模块中的项，就如同它们是本地项一样。

```shell
backyard
├── Cargo.lock
├── Cargo.toml
└── src
    ├── garden
    │   └── vegetables.rs
    ├── garden.rs
    └── main.rs
```

- src/main.rs

    ```rust
    use crate::garden::vegetables::Asparagus;

    pub mod garden;

    fn main() {
        let plant = Asparagus {};
        println!("I'm growing {:?}!", plant);
    }
    ```

- src/garden.rs

    ```rust
    pub mod vegetables;
    ```

- src/garden/vegetables.rs


    ```rust
    #[derive(Debug)]
    pub struct Asparagus {}
    ```

### use 约定

- 函数、常量等：要想使用 use 将函数的父模块引入作用域，我们必须在调用函数时指定父模块，这样可以清晰地表明函数不是在本地定义的，同时使完整路径的重复度最小化。

    ```rust
    mod front_of_house {
        pub mod hosting {
            pub fn add_to_waitlist() {}
        }
    }

    use self::front_of_house::hosting;
    // use self::front_of_house::hosting::add_to_waitlist; // 不推荐

    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
        hosting::add_to_waitlist();
        hosting::add_to_waitlist();
    }
    ```

- 结构体、枚举等：指定它们的完整路径

    ```rust
    use std::collections::HashMap;

    fn main() {
        let mut map = HashMap::new();
        map.insert(1, 2);
    }
    ```

    ps：如果有冲突时，可以使用父模块区分。

### as 关键字

    ```rust
    use std::fmt::Result;
    use std::io::Result as IoResult;

    fn function1() -> Result {
        // --snip--
    }

    fn function2() -> IoResult<()> {
        // --snip--
    }
    ```

### 重新导出

使用 use 关键字，将某个名称导入当前作用域后，这个名称在此作用域中就可以使用了，但它对此作用域之外还是私有的。如果想让其他人调用我们的代码时，也能够正常使用这个名称，就好像它本来就在当前作用域一样，那我们可以将 pub 和 use 合起来使用。这种技术被称为 “重导出（re-exporting）”：我们不仅将一个名称导入了当前作用域，还允许别人把它导入他们自己的作用域。

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting; // 外部代码现在可以通过新路径 <crate>::hosting::add_to_waitlist

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}
```

### 使用外部包

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

### 嵌套路径

```rust
// 繁琐
use std::cmp::Ordering;
use std::io;

// 简洁
use std::{cmp::Ordering, io};
```

### Glob

```rust
use std::collections::*;
```
