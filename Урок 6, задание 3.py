a=int(input('Введите чило а '))
b=int(input("Введите число b "))

if a<=b:

 for i in range(a, b+1):

  if i%2==0:
    print(i, end=" ")
else:
  print("Число а должно быть меньше или равно b")