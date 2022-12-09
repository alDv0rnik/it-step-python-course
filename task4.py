# def revrse_list(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, *kwargs)
#         rev = list(reversed(a))
#         return rev
#     return wrapper


# @revrse_list
# def transform(list1, list2):
#     result = []
#     for i in list1:
#         for j in list2:
#             result.append(f"{i} + {j}")
#     return result


l1 = [6, 3, 1]
l2 = [9, 5, 2]
print(transform(l1, l2))