# 所有权

- Rust 中的每一个值都有一个所有者（owner）；
- 值在任一时刻有且只有一个所有者；
- 当所有者（变量）离开作用域，这个值将被丢弃。

## 变量作用域

作用域是一个项（item）在程序中有效的范围

## 所有权转移

变量的所有权总是遵循相同的模式：将值赋给另一个变量时移动它。当持有堆中数据值的变量离开作用域时，其值将通过 drop 被清理掉，除非数据被移动为另一个变量所有。

```rust
let x = 5;
let y = x; // x 仍然有效
let s1 = String::from("hello");
let s2 = s1; // s1 无效了
```

如果一个类型实现了 Copy trait，那么一个旧的变量在将其赋值给其他变量后仍然可用。

Rust 不允许自身或其任何部分实现了 Drop trait 的类型使用 Copy trait。如果我们对其值离开作用域时需要特殊处理的类型使用 Copy 注解，将会出现一个编译时错误。要学习如何为你的类型添加 Copy 注解以实现该 trait，请阅读附录 C 中的 “可派生的 trait”。

实现了 Copy trait 的一些类型：

- 所有整数类型，比如 u32；
- 所有浮点数类型，比如 f64；
- 布尔类型，bool，它的值是 true 和 false
- 字符类型，char；
- 元组，当且仅当其包含的类型也都实现 Copy 的时候。

## 所有权与函数

将值传递给函数与给变量赋值的原理相似。向函数传递值可能会移动或者复制，就像赋值语句一样。

```rust
fn takes_ownership(some_string: String) { // some_string 进入作用域
    println!("{}", some_string);
} // 这里，some_string 移出作用域并调用 `drop` 方法。

fn main() {
    let s = String::from("hello"); // s 进入作用域
    takes_ownership(s); // s 的值移动到函数里 ...
    // ... 所以 s 到这里不再有效
}
```

## 引用和借用

- 引用（reference）：像一个指针，因为它是一个地址，我们可以由此访问储存于该地址的属于其他变量的数据。 

    创建一个引用的行为称为借用（borrowing）。

    ```rust
    fn main() {
        let s1 = String::from("hello");

        let len = calculate_length(&s1);

        println!("The length of '{}' is {}.", s1, len);
    }

    fn calculate_length(s: &String) -> usize {
        s.len()
    }
    ```

    ps：rust 禁止创建悬垂引用（Dangling References），例如：一个函数不能返回内部创建的数据引用，必须把所有权转移出去。

- 可变引用（（mutable reference））：值在任一时刻有且只有一个所有者，所以不能同时创建两个可变引用，也不能在拥有不可变引用的同时拥有可变引用。

    ```rust
    fn main() {
        let mut s = String::from("hello");
        change(&mut s);
    }

    fn change(some_string: &mut String) {
        some_string.push_str(", world");
    }
    ```

- slice 引用：允许你引用集合中一段连续的元素序列，而不用引用整个集合。slice 是一类引用，所以它没有所有权。
