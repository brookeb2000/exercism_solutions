def steps(number):
    """
    takes a positive integer and returns the number if steps it takes to reach 1 according to the rules of the Collatz Conjecture
    param number: int, positive integer greater than 0
    return: int, number of steps takes to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        if number % 2 == 0: #if the number is even
            number = number/2
        else:
            number = number * 3 + 1
        steps += 1
    return steps
