'''
Write a Python program that asks the user to enter 10 integers, and outputs the largest odd number among
them. If no odd numbers were entered, your program should output a message saying: "No odd numbers
were entered".
'''

print "Enter 10 integers"

lst = []

for i in range (10) :
    num = int(raw_input())
    if (num % 2) != 0 :
      lst.append(num)

if not lst:
  print "No odd numbers were entered"
elif lst != 0:
  print max(lst)