n = int(input("Qual número você quer verificar? "))
t1 = 0
t2 = 1
calc = True
if n == t1 or n == t2:
    print("O número informado pertence a sequência de Fibonacci.")
    calc = False
while calc:
    t3 = t1 + t2
    if n == t3:
        print("O número informado pertence a sequência de Fibonacci.")
        break
    if t3 > n:
        print("O número informado não pertence a sequência de Fibonacci.")
        break
    t1 = t2
    t2 = t3
