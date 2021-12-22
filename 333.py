class check():
    def __init__(self):
        self.n = []

    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def dis(self):
        return (self.n)


obj = check()

choice = 1
while choice != 0:
    print("0. Выход")
    print("1. Добавить")
    print("2. Удалить")
    print("3. Вывести на экран")
    choice = int(input("Выберите одно из этих значений: "))
    if choice == 1:
        n = int(input("Введите число для добавления в список: "))
        obj.add(n)
        print("Список: ", obj.dis())

    elif choice == 2:
        n = int(input("Введите число, которое хотите удалить: "))
        obj.remove(n)
        print("Список: ", obj.dis())

    elif choice == 3:
        print("Список: ", obj.dis())
    elif choice == 0:
        print("Выходим!")
    else:
        print("Неверный выбор!!")

print()