use self::temp::temp_print;
use variables::variables_temp;

pub mod temp;

pub mod variables;

pub fn basic_print() {
    temp_print();
    temp::temp_print();
    variables_temp();
    variables::variables_temp();
}
