# Write a Python program to calculate the length of a string.
length = len("text")
print(length)

def str_len(input: str):
    counter = 0
    for i in input:
        counter += 1 # counter = counter + 1 
    return counter

counter = str_len("text test test")
print("counter: ", counter)

# Write a Python program to sum all the items in a list.
# [1, 2, 3]
# 1 + 2 + 3 = 6
def sum_list(lista: list):
    sum_nums = 0
    for num in lista:
        sum_nums += num
    return sum_nums

sum_nums = sum_list([1, 2, 3])
print(sum_nums)


# [1, 2, 3]
# Write a Python program to get the largest number from a list
def max_num(lista: list):
    max = lista[0] 
    for item in lista:
        if item > max:
            max = item
    return max

max_num_val = max_num([1, 2, 3])
print(max_num_val)


# Write a Python function that takes two lists and returns True if they have at least one common member.
# [1, 2, 3]
# [3, 4, 5]
def common_nums(list1: list, list2: list):
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                return True
    return False
common_nums_value = common_nums([1, 2, 8], [3, 4, 5])
print(common_nums_value)


# Write a Python program to iterate over dictionaries using for loops.
def iterate_dict(input: dict):
    for key, item in input.items():
        print("key: ", key, "item: ", item)

iterate_dict({"name": "Team", "city": "Peje"})



# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Write a Python program to count the occurrences of each word in a given sentence.
# Write a Python program that:
    # Randomly chooses a secret number between 1 and 50.
    # Asks the user to guess the number.
    # Uses a while loop to keep asking until the guess is correct.
    # After each wrong guess, the program should tell the user whether they are getting warmer or colder compared to their previous guess.
    # On the first wrong guess, it only tells them “Wrong, try again!” (because there is no previous guess to compare to).
    # When the user finds the number, print “Correct! You found it!” and stop the loop.