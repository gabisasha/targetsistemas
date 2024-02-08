'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

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
