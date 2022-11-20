#Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
print("Task1")
a = int(input())
b = int(input())
print((a*a + b*b)**0.5)
#Число десятков
print("Task2")
n = int(input("chislo="))
k = n // 10 % 10
print(k)
#3. Следующее четное
print("Task3")
n=int(input("Chislo="))
print(n+2-(n%2))
#4.Конец уроков
print("Task4")
n = int(input())
n = n*45 + (n//2)*5 + ((n+1)//2-1)*15
print(n//60 + 9, n%60)
#5. Какое из чисел больше?
print("Task5")
n=int(input())
k=int(input())
if n>k:
    print(n)
else:
    print(k)
#6.Максимум из трех
print("Task6")
n=int(input())
m=int(input())
k=int(input())
max = n
if m > max:
    max = m
if k > max:
    max = k
print(max)
#7.Ладья
print("Task7")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
#8.Существует ли треугольник?
print("Task8")
a =int(input())
b =int(input())
c =int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
#9.Количество равных из
print("Task9")
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
   print(3)
elif a == b or b == c or a == c:
   print(2)
else:
   print(0)
#10.Упорядочить три числа
print("Tas10")
a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


