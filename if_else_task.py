a = int(input("ввести а "))
b = int(input("ввести b "))
c = int(input("ввести c "))

if a > c:
    print("Свершилось!")
elif c > a:
    print("Да ну!")
elif a == c:
    print("А если так?!")
    if a + b == c - b:
        print("А вдруг!!!")
