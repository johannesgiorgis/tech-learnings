# Chapter 1: The Basics

## Variables

Variables are declared using the `let` keyword.

When assigning a value, Rust will be able to infer the type of your variable 99% of the time.

Variable names are always in `snake_case`.

## Changing Variables

Rust cares a great deal about what variables are modifiable. Values fall into two types:

- **mutable**: the compiler will allow the variable to be written to and read from
- **immutable**: the compiler will only allow the variable to be read from

Mutable values are denoted with a `mut` keyword.

## Basic Type Conversion

Rust requires explicitness when it comes to numeric types.

Rust makes numeric type conversions very easy with the `as` keyword

## Constants

Constants allow us to specify a common value that's used throughout our code many times efficiently. Instead of copying values like variables where they are used, constants directly replace the text identifier where they are used with their value at compile time.

Unlike variables, constants must always have explicit types.

Constant names are always in `SCREAMING_SNAKE_CASE`.

## Arrays

An _array_ is a **fixed length collection** of data elements all of the same type.

The data type for an array is `[T;N]` where T is the elements' type, and N is the fixed length known at compile time.

## Functions

A function has zero or more parameters. Function names are always in `snake_case`.
