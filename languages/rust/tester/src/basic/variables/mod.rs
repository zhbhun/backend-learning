// use crate::basic::temp;
// use super::temp::*;

#[derive(Debug)]
pub struct Square {
    width: i32,
    height: i32,
}

impl Square {
    fn area(&self) -> i32 {
        self.width * self.height
    }
}

pub fn print() {
    let square = Square {
        width: 100,
        height: 100,
    };
    print!("{}", square.area());
}

pub fn variables_temp() {
    // temp_print();
    // temp::temp_print();
    super::temp::temp_print();
    print!("variables");
}
