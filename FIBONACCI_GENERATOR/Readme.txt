The Infinite Fibonacci Generator is a Python program that generates Fibonacci numbers continuously 
using a generator function with the yield keyword. Unlike traditional approaches that store all values in memory, 
this implementation produces numbers one at a time, making it memory-efficient and suitable for large or continuous sequences.

The Fibonacci sequence is defined as:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Each number is the sum of the two preceding numbers.

The generator starts with two initial values: 0 and 1.

It produces the next Fibonacci number using:

next_number = previous + current

The yield keyword pauses the function and returns the value.

The function resumes from the same state when called again.

The sequence continues indefinitely unless stopped manually.