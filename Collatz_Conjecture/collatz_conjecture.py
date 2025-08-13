def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    num = number
    steps = 0
    while num != 1:
        if num % 2 == 0: #if the number is even
            num = num/2
        else:
            num = num * 3 + 1
        steps += 1
    return steps
