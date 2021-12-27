# write python code that rompts the user for a letter then count how many times it appears in
sentance = "the quick brown fox jumps over the lazy dog"

input = input("What letter would you like to count?")
amount = 0

for letter in sentance:
    if letter == input:
        amount += 1
print("The letter",input,"appeared",amount,"times!")