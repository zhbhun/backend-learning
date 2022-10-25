# 数据类型

## 整型

| 长度 | 有符号 | 无符号 |
| --- | --- | --- |
| 8-bit | i8 | u8 |
| 16-bit | i16 | u16 |
| 32-bit | i32 | u32 |
| 64-bit | i64 | u64 |
| 128-bit | i128 | u128 |
| arch | isize | usize |

ps：默认类型为 `i32`，可以使用类型后缀来制定类型，例如：`57u8`，同时也允许使用 _ 做为分隔符以方便读数，例如1_000，它的值与你指定的 1000 相同。

| 数字字面值 | 例子 |
| --- | --- |
| Decimal (十进制) | 98_222 |
| Hex (十六进制) |0xff |
| Octal (八进制) | 0o77 |
| Binary (二进制) | 0b1111_0000 |
| Byte (单字节字符)(仅限于u8) | b'A' |

## 浮点型

- `f32`：默认类型
- `f64`

## 布尔值

```rust
bool
```

## 字符

- `char`
- `String`
- `&str`

## 复合类型

### 元组类型

元组是一个将多个其他类型的值组合进一个复合类型的主要方式。元组长度固定：一旦声明，其长度不会增大或缩小。我们使用包含在圆括号中的逗号分隔的值列表来创建一个元组。元组中的每一个位置都有一个类型，而且这些不同值的类型也不必是相同的。

```rust
// 创建元组
let tup: (i32, f64, u8) = (500, 6.4, 1);
// 解构使用
let (x, y, z) = tup;
// 索引访问
let five_hundred = x.0;
let six_point_four = x.1;
let one = x.2;
```

### 数组类型

数组中的每个元素的类型必须相同，且数组长度是固定的。

```rust
// 创建数组
let a = [1, 2, 3, 4, 5];
let a: [i32; 5] = [1, 2, 3, 4, 5];
let a = [3; 5];
// 访问数组元素
let first = a[0];
let outOfBounds = a[5]; // 报错
```

## 结构体

### 定义结构体

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

### 结构体实例

```rust
fn main() {
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
}
```

### 访问设置

注意整个实例必须是可变的；Rust 并不允许只将某个字段标记为可变。

```rust
fn main() {
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

### 结构体更新语法

```rust
fn main() {
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    let user2 = User {
        email: String::from("another@example.com"),
        ..user1 // 必须放在最后，以指定其余的字段应从 user1 的相应字段中获取其值
    };
    // user1 的字符串等搜有权转移了，不能再使用 user1
}
```

### 元组结构体

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    let black = origin;
    // black 和 origin 值的类型不同，不能相互赋值
}
```

### 类单元结构体

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

### 打印结构体

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1); // error[E0277]: `Rectangle` doesn't implement `std::fmt::Display`
}
```

ps：println! 宏能处理很多类型的格式，不过，{} 默认告诉 println! 使用被称为 Display 的格式：意在提供给直接终端用户查看的输出。目前为止见过的基本类型都默认实现了 Display，因为它就是向用户展示 1 或其他任何基本类型的唯一方式。不过对于结构体，println! 应该用来输出的格式是不明确的，因为这有更多显示的可能性：是否需要逗号？需要打印出大括号吗？所有字段都应该显示吗？由于这种不确定性，Rust 不会尝试猜测我们的意图，所以结构体并没有提供一个 Display 实现来使用 println! 与 {} 占位符。

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1); // 在 {} 中加入 :? 指示符告诉 println! 我们想要使用叫做 Debug 的输出格式。
    // rect1 is Rectangle { width: 30, height: 50 }

    println!("rect1 is {:#?}", rect1); // 格式化显示
}
```

ps：Debug 是一个 trait，它允许我们以一种对开发者有帮助的方式打印结构体，以便当我们调试代码时能看到它的值。

### 结构体方法

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

### 关联函数

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let sq = Rectangle::square(3);
}
```
