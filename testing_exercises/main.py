# def reverse_string(string):
#     reversed_list = []
#     num = -1
#     length = len(string)
#     for x in range(length):
#         reversed_list.append(string[num])
#         num -= 1
#     reversed_word = ''.join(reversed_list)
#     return reversed_word


# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str


# Reversing a string in python

# def reverse(s):
#     return s[::-1]

#######################################################################################################################


# print(all(isinstance(x, list) for x in list_check))


# def list_check(list_checklist):
#     for item in list_checklist:
#         if type(item) != list:
#             return False
#     return True
#
#
# print(list_check([[], [1], [2, 3]]))

###############################################################

# def sum_pairs(lista, num):
#     list_len = len(lista)
#     num_index = 0
#     num_slice = 1
#     for y in range(list_len):
#         for x in lista[num_slice:]:
#             if lista[num_index] + x == num:
#                 return [lista[num_index], x]
#             return []
#         num_index += 1
#         num_slice += 1

# ANOTHER solution doesn't work with repeated numbers
# def sum_pairs(lst1, int1):
#     for x in lst1:
#         for y in lst1:
#             if x + y == int1 and x is not y:
#                 return [x, y]
#     return []

# Colt's solution
# def sum_pairs(ints, s):
#     already_visited = set()
#     for i in ints:
#         difference = s - i
#         if difference in already_visited:
#             return [difference, i]
#         already_visited.add(i)
#     return []
#
# print(sum_pairs([4, 4, 10, 5, 1], 8))
################################################################################################################
# CAPITALIZE first letter

# def titleize(string):
#     s = list(string)
#     for ind, x in enumerate(s):
#         if x == " ":
#             s[ind + 1] = s[ind + 1].upper()
#             s[0] = s[0].upper()
#     return "".join(s)
#
# print(titleize("oNLy cAPITALIZe fIRSt"))


#########################################################################################
#How to update a dictionary inside a loop

# string1 = "Elie"
# string = string1.lower()
# vowels = ["a", "e", "i", "o", "u"]
# dictionary = {key: string.count(key) for key in vowels if key in string}
# print(dictionary)

# dictio = {}
# for key in vowels:
#     if key in string:
#         dict = {key: string.count(key)}
#         dictio.update(dict)

