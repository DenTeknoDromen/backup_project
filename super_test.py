# class Children:
#     def __init__(self, c_name, surname):
#         print(f"Child: {c_name} {surname}")

# class Parent(Children):
#     def __init__(self, p_name, surname):
#         print(f"Parent {p_name} {surname}")
#         super().__init__("Tobias", surname)

# p = Parent("Leif", "Jansson")

# with open("BLABLABLA", "rw") as f:
#     f.write("BAJSBAJSBJAS")

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list1 = list1 + list2

for x in list1:
    print(x)