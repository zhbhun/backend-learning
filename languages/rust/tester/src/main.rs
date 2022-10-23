// use crate::basic::variables::print;

// pub mod basic;

fn greet(target: String) {
    println!("Hello, {}", target);
}

fn main() {
    let v = 1;
    println!("&v:{:p}",&v);
    let mut v = 2;

    let message = String::from("Word!");
    greet(message);
}
