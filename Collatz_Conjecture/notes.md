# Collatz Conjecture - Notes

## Approach
used flow of control (while loops, if else statements) to modify data

## Challenges
this one wasnt too challenging, tested concepts I was already familiar with

## Testing
used test cases provided by exercism

## Potential Improvements
I improved this function after looking at community solutions to the same exercise. I thought that the parameter was passed by reference so I wanted to make a local variable with this value, but I learned that int are passed by value in python (you get a pointer to the value in memory, and then every time you modify the value, your pointer points to that new object (ints are immutable))

## Reflection
see above
