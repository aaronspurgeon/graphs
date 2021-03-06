# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#     "cat": "bob",
#     "dog": 23,
#     19: 18,
#     90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
hash_table = {"cat": 'bob', 'foo': 'bar', 19: 18, 90: 'fish', 'jim': 23}


def hash_sum(obj):
    result = 0
    obj_list = obj.values()
    for i in obj_list:
        if type(i) == int:
            result = result + i
    return result


print(hash_sum(hash_table))
