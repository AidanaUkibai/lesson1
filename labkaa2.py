#Четные числа
#Task1
print("Task1")
a=int(input())
b=int(input())
for i in range(a,b,2):
    c=i%2+i
    print(c,end=" ")
print('\n')
#2.Минимальный делитель
print("Task2")
n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
    print(n)
#3. Делители числа
print('Task3')
n = int(input())
for i in range(1, n+1):
    if (n % i == 0):
        print(i, end = " ")
#4.Сумма чисел
n=int(input())
s=0
for i in range(1,n+1):
  o=int(input())
  s=o+s
print(f'Summa = {s}')
#5. Перевод числа
#1=zhol
a = int(input(),2)
print(a)
#6.Степень
def power(a,b):
    return a**b
n=int(input())
n1=int(input())
print(power(n,n1))
#7.Golosovanie
def Election(x,y,z):
    if x==y and x==z and y==z:
        return 1
    else:
        return 0
n=int(input())
n1=int(input())
n2=int(input())
print(Election(n,n1,n2))
#8.
#A
def addToBankAccount(a):
    p=0
    print(0+a)

def substractFromBankAccount(o,p):
    o=o-p
    return o

def moneyConversion(t,o1, o2):
    match o1,o2:
        case "USD","KZT":
            return t*470
        case "KZT","USD":
            return t/470

money=120

print(moneyConversion(120,"USD","KZT"))
