use crate::basic::variables::*;
// use basic::variables::*;

mod basic;

fn main() {
    // let mut v = vec![100, 32, 57];
    // let first = &mut v[0];
    // *first = 2;
    // for i in &mut v {
    //     *i += 50;
    //     println!("{}", i);
    // }
    let mut a = 1;
    print!("\n1. a: {a} - {:p}", &a);
    let b = &mut a;
    *b = 2;
    print!("\n2. b: {b} - {:p}", &b);
    print!("\n3. a: {a} - {:p}", &a);
}

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {
            // eat_at_restaurant()
        }
    }
}

pub fn eat_at_restaurant() {
    // 绝对路径
    // crate::front_of_house::hosting::add_to_waitlist();

    // // 相对路径
    // front_of_house::hosting::add_to_waitlist();
    variables_temp();
    basic::basic_print();
}
