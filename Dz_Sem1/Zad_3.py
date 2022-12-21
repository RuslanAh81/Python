# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#

# def F(x, y, z):
#     return not(x or y or z) == (not x) and (not y) and (not z)
#
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             if F(x, y, z):
#                 print(x, y, z)


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not(x or y or z) == (not x) and (not y) and (not z):
                print("True")
            else:
                print("False")

