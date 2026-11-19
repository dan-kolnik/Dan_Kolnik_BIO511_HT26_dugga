# Q2

my_names = ["alice", "bob", "charlie"]

# Task A

# long_names = []

# for item in my_names:
#     print(len(item))
#     if len(item) > 4:
#         long_names.append(item)

# print(long_names)


# # Task B

# def get_long_names(my_list):
#     long_names = []
#     for item in my_list:
#         print(len(item))
#         if len(item) > 4:
#             long_names.append(item)
#     return long_names

# my_long_names = get_long_names(my_names)
# print(my_long_names)


# Task C

New_list = ["doggy", 5, "elsa"]

for Item in New_list:
    my_names.append(Item)

print(my_names)

# def get_long_names(my_list):
#     long_names = []
#     for item in my_list:
#         # print(len(item))
#         try:
#             if type(item) == str:
#                 continue
#         except ValueError:
#             print(f"'{item}' is not of type string and was skipped.")
#         if len(item) > 4:
#             long_names.append(item)
#     return long_names

# my_long_names = get_long_names(my_names)
# print(my_long_names)

def get_long_names(my_list):
    long_names = []
    for item in my_list:
        try:
            print(len(item))
        except ValueError:
            print(f"'{item}' is not of type string and was skipped.")
        if len(item) > 4:
            long_names.append(item)
    return long_names

my_long_names = get_long_names(my_names)
print(my_long_names)