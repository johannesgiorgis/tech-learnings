# Chapter 2: Basic Control Flow

## for

Rust's `for` loop is a powerful upgrade. It iterates over values from any expression that evaluates into an iterator.

- `..` operator creates an iterator that generates numbers from a start number up to but not including an end number
- `..=` operator creates an iterator that generates numbers from a startup number up to and including an end number

## match

`match` is used for matching all possible conditions of a value and executing a code path if hte match is true.

Matching combined with destructuring is by far one of the most common patterns you will see in all of Rust.

## Returning Values from Block Expressions

`if`, `match`, functions, and scope blocks all have a unique way of returning values in Rust. If the last statement is an expression without a `;`, Rust will return it as a value from the block. This is a great way to createa concise logic that returns a value that can be put into a new variable.
