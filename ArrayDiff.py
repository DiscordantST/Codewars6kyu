def array_diff(a, b):
        return [x for x in a if x not in b]



# #another answer
# def array_diff(a, b):
#     for item in b:
#         while item in a:
#             a.remove(item)
#         print(a)



