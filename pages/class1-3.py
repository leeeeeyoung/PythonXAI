print(1 == 1)  # True
print(1 != 1)  # False
print(2 > 1)  # True
print(2 < 1)  # False
print(2 >= 2)  # True
print(2 <= 1)  # False

print(not True)  # False
print(not False)  # True

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

password = input("請輸入密碼: ")

if password == "1234":
    print("歡迎 John!")

if password == "1234":
    print("歡迎 John!")
else:
    print("密碼錯誤!")

if password == "1234":
    print("歡迎 John!")
elif password == "5678":
    print("歡迎 Mary!")
else:
    print("密碼錯誤!")
