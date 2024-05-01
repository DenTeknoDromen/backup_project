class Children:
    def __init__(self, c_name, surname):
        print(f"Child: {c_name} {surname}")

class Parent(Children):
    def __init__(self, p_name, surname):
        print(f"Parent {p_name} {surname}")
        super().__init__("Tobias", surname)

p = Parent("Leif", "Jansson")

with open("BLABLABLA", "rw") as f:
    f.write("BAJSBAJSBJAS")