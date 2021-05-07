// for loop
// .. operator: creates an iterator that generates numbers from a start number up to but not including an end number
// ..= operator: creates an iterator that generates numbers from a start number up to and including an end number

fn main() {
    for x in 0..5 {
        println!("{}", x);
    }

    for x in 0..=5 {
        println!("{}", x);
    }
}
