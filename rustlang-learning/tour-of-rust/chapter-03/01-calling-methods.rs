// calling methods

fn main() {
    // Using a static method to create an instance of String
    let s = String::from("Hello world!");
    // Using a method of the instance
    println!("{} is {} characters long.", s, s.len());
}