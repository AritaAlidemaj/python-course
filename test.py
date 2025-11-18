# Find the length of a string
def string_length(s: str) -> int:
    return len(s)

# str_len = string_length("Hello world!")
# print(str_len)


# Change a string to lowercase
def to_lower(s: str) -> str:
    return s.lower()

str_lower = to_lower("HeLLO WorLD")
# print(str_lower)



# Change a string to uppercase
def to_upper(s: str) -> str:
    return s.upper()

str_upper = to_upper("HeLLO WorLD")
# print(str_upper)



# Count how many times a word appears
def count_word(s: str) -> int:
    return s.count("apple")

word_count = count_word("apple strawberry apple")
# print(word_count)



# Replace a word in a sentence
def replace_word(s: str) -> str:
    return s.replace("dog", "cat")

replace = replace_word("I have a dog")
print(replace)



# Join a list of words into one string
def join_words(words: list[str]) -> str:
    return " ".join(words)

# Split a sentence into words
def split_sentence(s: str) -> list[str]:
    return s.split()

# Get the smallest number from a list
def smallest(nums: list[int]) -> int:
    return min(nums)

# Get the largest number from a list
def largest(nums: list[int]) -> int:
    return max(nums)

# Sum all numbers in a list
def total(nums: list[int]) -> int:
    return sum(nums)

# Sort numbers
def sort_numbers(nums: list[int]) -> list[int]:
    return sorted(nums)

# Remove duplicates from a list
def remove_duplicates(items: list) -> list:
    return list(set(items))

# Check if a value exists in a list
def contains_value(items: list, value) -> bool:
    return value in items

# Get both the smallest and largest number
def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)

# Combine two lists
def combine_lists(a: list, b: list) -> list:
    return a + b

# Find common elements between two sets
def common_elements(a: set, b: set) -> set:
    return a.intersection(b)

# Find elements only in the first set
def only_in_first(a: set, b: set) -> set:
    return a.difference(b)

# Check if one set is a subset of another
def is_subset(a: set, b: set) -> bool:
    return a.issubset(b)

# Combine two sets
def combine_sets(a: set, b: set) -> set:
    return a.union(b)

# Create a dictionary with a single key-value pair
def make_dict() -> dict:
    return {"name": "Alice"}

# Get a value from a dictionary
def get_age(person: dict) -> int:
    return person.get("age")

# Update a dictionary
def update_city(person: dict) -> dict:
    person.update({"city": "Paris"})
    return person

# Create a tuple with three items
def make_tuple() -> tuple[int, int, int]:
    return (1, 2, 3)

# Get the first and last item from a tuple
def ends(t: tuple) -> tuple:
    return (t[0], t[-1])