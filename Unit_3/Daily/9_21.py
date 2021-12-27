# this file has split and join, kind of insane


winter = ["snow", "christmas"]
print(winter)
winter.append("cocoa")

# extinding is just appending the elements of a new list, without making it a nested list
winter.extend(["ski", "sledding"])

# another example
more_winter = ["frost", "fun"]
winter.extend(more_winter)
print(winter)

# += basically the same as extend
winter += ["holiday", "snowboard"]
print(winter)

winter.pop(2)
print(winter)

# create a string for a list of strings
# join()
sledding_list = ["s", "l", "e", "d", "d", "i", "n", "g"]
print(sledding_list)
sledding_string = "".join(sledding_list)
print(sledding_string)

sledding_list2 = list(sledding_string)
print(sledding_list2)

# i have a new keybind, shift+p twice to run file
# lets make this comma seperated list into a regular normal list
comma_separated_string_of_values = "a,b,c,d"
values_list = comma_separated_string_of_values.split(",")
# split is gonna be insanely useful
print(comma_separated_string_of_values)
print(values_list)


# list aliasing
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1  # this is just a way to have list1 be called something else
print(list1, list2, list3)
list3[2] = 20
print(list1, list2, list3)


def add_one_to_each_element(some_list):
    for i in range(len(some_list)):
        some_list[i] += 1  # modifies the list


add_one_to_each_element(list1)  # notice how this also changes list3
print(list1, list2, list3)

word = "winter"
print(word[1], word[-1], word[0:3])
# strings are immutable (they cannt be changed)
# word[0] = "W" # THIS WONT WORK

# string concatination
word += "Test "
print(word)
word = "winds of " + word
print(word)
word *= 5
print(word)

# string comparison
# this used < <= >= > == != on the first char of each string
print("clash of kings" < word)  # because lowercase c is less than lowercase w
# a is 97
# A is 65
print("Winds of winter" < word)  # because upercase is before lowercase
