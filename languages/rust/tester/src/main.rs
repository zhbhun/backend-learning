fn main() {
    let mut a = 1;
    println!("{:p}", &a);
    a = 2;
    println!("{:p}", &a);
    let a = 3;
    println!("{:p}", &a);
}
