import random

# list practice problems

# generate a list of random numbers between 1 and 20


def make_rand_list(amount):
    numbers = []
    for i in range(1, 21):
        numbers.append(random.randrange(1, 11))
    return numbers


def pretty_print(numbers):
    for i in numbers:
        print(numbers[i], end=" ")
    print()


numbers = make_rand_list(20)
pretty_print(numbers)

print(min(numbers))
print(max(numbers))

count = 0
for num in numbers:
    if num == 5:
        count += 1

print("There have been", count, "fives")
