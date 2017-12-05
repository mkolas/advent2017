# part 1

values = []

with open("input1.txt") as file:
    for row in file:
        largest = 0
        smallest = 9999
        numbers = [int(x) for x in row.split()]
        for number in numbers:
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number
        values.append(largest - smallest)

print(sum(values))

# part 2

values = []

with open("input1.txt") as file:
    for row in file:
        numbers = [int(x) for x in row.split()]
        for number in numbers:
            divisors = [int(x) for x in row.split()]
            for divisor in divisors:
                if number != divisor and number%divisor == 0:
                    values.append(number/divisor)
                    break

print(sum(values))