print("Oddiy kalkulyator")

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

print("Qo'shish:", a + b)
print("Ayirish:", a - b)
print("Ko'paytirish:", a * b)

if b != 0:
    print("Bo'lish:", a / b)
else:
    print("Nolga bo'lish mumkin emas!")
    