use crate::basic::variables::*;
// use basic::variables::*;

mod basic;

fn main() {
    print();
    basic::basic_print();
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
