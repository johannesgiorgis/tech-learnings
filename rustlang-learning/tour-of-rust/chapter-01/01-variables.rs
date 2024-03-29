// Variables

fn main() {
    // rust infers the type of x
    let x = 13;
    println!("{}", x);

    // rust can also be explicit about the type
    let x: f64 = 3.14159;
    println!("{}", x);

    // rust can also declare and initialize later, but this is rarely done
    let x;
    x = 0;
    println!("{}", x);

    changing_variables()
}

fn changing_variables() {
    println!("changing variables...");
    let mut x = 42;
    println!("{}", x);
    x = 13;
    println!("{}", x);
}
