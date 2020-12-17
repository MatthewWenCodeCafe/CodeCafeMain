import threading


class Student:

    def __init__(self, name):
        self.name = name
        self.last_name = ""

    @staticmethod
    def load_with_no_name():
        s = Student("John")
        return s

    var = 10

    @staticmethod
    def same_for_everybody(v):
        Student.var = v
        return "Same for Everybody"

    def set_lastname(self, last_name):
        self.last_name = last_name

    def print_name(self):
        print(self.name + " " + self.last_name)
        return None


# s1 = Student("Caleb")
# s2 = Student("Jessica")
# s1.set_lastname("Darr")
# s2.set_lastname("Wong")
#
# print(s1.same_for_everybody(4))
# print(s2.same_for_everybody(5))
# print(s1.var)
# print(s2.var)
#
# s1.print_name()
# s2.print_name()
#
# s3 = Student.load_with_no_name()
# s3.print_name()


def print_cube(num): # 50 minutes to run
    print(f"Cube: {num * num * num}")
    print("Cube: {}".format(num * num * num))


def print_square(num): # 50 minutes to run
    print(f"Square: {num * num}")
    print("Square: {}".format(num ** 2))  # num ^ 2


t1 = threading.Thread(target=print_cube, args=(10,))
"""
when t1.start() -> run this code with num = 10
print(f"Cube: {num * num * num}")
print("Cube: {}".format(num * num * num))
"""

t2 = threading.Thread(target=print_square, args=(5,))
"""
when t2.start() -> run this code with num = 5 
print(f"Cube: {5 * 5 * 5}")
print("Cube: {}".format(5 * 5 * 5))
"""


# t2.start()
t1.start()

t1.join()
# t2.join()
print("Done")


print_cube(10) # 50 min
print_square(5) # 60 min
# 110 min

t1.start() # 50 min
t2.start() # 60 min
# 60 minutes
t1.join()
t2.join()
