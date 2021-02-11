value = input("Вводите число n: ")
count = 0
end = 3
n = ""
summa = 0
stroka = ""
text = ""
while count < end:
    count = count + 1
    n = value + n
    summa = summa + int(n)
    stroka = stroka + "n"
    text = text + " + " + stroka
print(f"Сумма {text[3:]} = ", summa)
