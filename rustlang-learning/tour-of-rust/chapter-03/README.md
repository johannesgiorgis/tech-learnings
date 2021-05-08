# Chapter 3: Basic Data Structure Types

## Structures

`struct`: collection of fields

A _field_ is simply a data value associated with a data structure. Its value can be of a primitive type or a data structure.

Its definition is like a blueprint for a compiler on how to layout the fields in memory nearby each other.

## Calling Methods

Methods are functions associated with a specific data type

- **static methods**: methods that belong to a type itself are called using the `::` operator
- **instance methods**: methods that belong to an instance of a type are called using the `.` operator

## Memory

Rust programs have 3 memory regions where data is stored:

- **data memory**: Data that is fixed in size and **static** - always available through the life of a program. Compilers make lots of optimizations with this kind of data, and they are generally considered very fast to use since locations and known and fixed.
- **stack memory**: Data that is declared as variables within a function. The location of this memory never changes for the duration of a function call; because of this compilers can optimize code so stack data is very fast to access
- **heap memory**: Data that is created while the application is running. Data in this region may be added, moved, removed, resized, ...etc. Because of its dynamic nature it's generaly considered slower to use, but it allows for much more creative usages of memory. When data is added to the region we call it an **allocation**. When data is removed from this section we call it a **deallocation**.

## Enumerations

Enumerations allow you to create a new type that can have a value of several tagged elements using the `enum` keyword.

`match` helps ensure exhaustive handling of all possible enum values making it a powerful tool in ensuring quality code.

## Enumerations with Data

`enum` elements can also have one or more data types allowing them to behave like _union_ from C.

When an `enum` is pattern matched using `match`, you can bind a variable name to each data value.

Memory details of `enum`:

- An enum data value will have a memory size equal to its largest element. This allows for all potential values to fit in the same space of memory
- In addition to element data types (if any), each element also has a numeric value that represents which tag it is

Other details:

- Rust's `enum` is something also known as a _tagged union_.
- The combining of types to make a new type is what people mean when they say Rust has _algebraic types_.
