# Inventory Management - Notes

## Approach
Used dictionaries to keep track of inventory (add and remove entries)

## Challenges
This was the first time learning dictionaries, so I had to refer to my notes a lot to pick out which methods to use.

## Testing
Tested with test cases provided by exercism

## Potential Improvements
I noticed that I was using the pop method to pop and entry from the dictionary and that this returns a value, but I never used the return value, 
I wonder if there is best practice

## Reflection
read up about best practices and it appears using pop() is correct where I did because I dont want an error to be raised, if it is not found,
pop will just return a value and not modify the dict which is what I want. I tried del dict[item], but this raised an error which is not what I wanted.
Enjoyed working with dicts, and reading algorithms book helped a lot to understand conceptually what is happening and why on average speed of O(1)
