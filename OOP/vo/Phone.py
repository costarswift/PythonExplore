
class Phone:
    __current_voltage = None
    name = None

    def __init__(self, name):
        self.name = name

    def __keep_single_core(self):
        print("单核模式启动")

phone = Phone("iPhone 15 Pro MAX")
print(phone.name)
