# 集合

## Vector

vector 允许我们在一个单独的数据结构中储存多于一个的值，它在内存中彼此相邻地排列所有的值。

```rust
// 新建
let v: Vec<i32> = Vec::new(); // 主动声明
let v = vec![1, 2, 3]; // 自动推断

// 更新
let v: Vec<i32> = Vec::new(); // 主动声明
v.push(5); // 增加值

// 读取
let v: Vec<i32> = Vec::new(); // 主动声明
let third: &i32 = &v[2]; // 索引语法
let thrid: &i32 = v.get(2); // get 方法

// 遍历
let v = vec![100, 32, 57];
for i in &v {
    println!("{}", i);
}
let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

### HashMap

```rust
// 新建
use std::collections::HashMap;
let mut scores = HashMap::new();

// 在 vector 上使用迭代器（iterator）和 collect 方法
let teams = vec![String::from("Blue"), String::from("Yellow")];
let initial_scores = vec![10, 50];
let mut scores: HashMap<_, _> = teams.into_iter().zip(initial_scores.into_iter()).collect();

// 添加
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

// 所有权
let field_name = String::from("Favorite color");
let field_value = String::from("Blue");
let mut map = HashMap::new();
map.insert(field_name, field_value);
// 这里 field_name 和 field_value 不再有效，

// 访问哈希 map 中的值
 let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
let team_name = String::from("Blue");
let score = scores.get(&team_name); // Option<i32>

// 遍历
use std::collections::HashMap;
let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
for (key, value) in &scores {
    println!("{}: {}", key, value);
}

// 更新哈希 map
let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);
println!("{:?}", scores);

// 只在键没有对应值时插入
let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);
println!("{:?}", scores);

// 根据旧值更新一个值
let text = "hello world wonderful world";
let mut map = HashMap::new();
for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}
println!("{:?}", map);
```
