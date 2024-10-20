
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("一个学生对象被创建了")

    def __str__(self):
        return f"[name:{self.name}, age:{self.age}, address:{self.address}]"

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.address == other.address

stu = Student("张三", 23, "上海黄浦区")
stu2 = Student("李四", 25, "上海徐汇区")
print(stu.name)
print(stu)

print(stu < stu2)
print(stu == stu2)