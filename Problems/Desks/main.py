# put your python code here

desks_class1 = int(input())
desks_class2 = int(input())
desks_class3 = int(input())

if desks_class1 % 2 == 0:
    class1 = desks_class1 / 2
else:
    class1 = desks_class1 // 2 + 1

if desks_class2 % 2 == 0:
    class2 = desks_class2 / 2
else:
    class2 = desks_class2 // 2 + 1

if desks_class3 % 2 == 0:
    class3 = desks_class3 / 2
else:
    class3 = desks_class3 // 2 + 1

print(int(class1 + class2 + class3))
