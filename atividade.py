def calculadora(num1,num2,operacao):
    if(operacao == 1): return num1+num2
    elif(operacao == 2): return num1-num2
    elif(operacao == 3): return num1/num2
    elif(operacao == 4): return num1*num2
    else: return False
num1= float(input("Digite o primeiro numero da operação :"))
operacao= int(input('digite a operação sabendo que 1= soma; 2= subtração; 3= Divisão; 4= multiplicação :'))
num2= float(input("digite o segundo numero da operação :"))
resultado= calculadora(num1, num2, operacao)
print("o resultado da soma foi :",resultado)