- `&str`：不可变字符串
- `String`：可变字符串

## 类型转换

- &str to a String

    ```rust
    // to_string
    let new_string = "Hello World!".to_string();
    // to_owned
    let new_string = "Hello World!".to_owned();
    // String::from
    let new_string = String::from("Hello World!");
    // String::push_str()
    let mut new_string = String::new(); 
    new_string.push_str("Hello");
    new_string.push_str(" World!");
    ```

- String to a &str

    ```rust
    let world_var= "world";
    let new_string = format!("Hello {}!", world_var);
    ```

## 参考文献

- [Strings - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/std/str.html)
- [Why Are There Two Types of Strings In Rust?](https://www.justanotherdot.com/posts/why-are-there-two-types-of-strings-in-rust)
- [How do I convert a &str to a String in Rust?](https://blog.mgattozzi.dev/how-do-i-str-string/)
- [Rust: str vs String](https://www.ameyalokare.com/rust/2017/10/12/rust-str-vs-String.html)
- [String vs &str in Rust](https://blog.thoughtram.io/string-vs-str-in-rust/)
