# def sum_int(a, b):
#    return a+b #함수의 종료

# num1 = 10
# num2 = 20

# result = sum_int(num1, num2)
# print(f'{num1} + {num2} = {result}')

# def  mul_int(a, b):
#    return a*b

# result2 = mul_int(num1, num2)
# print(f'{num1} x {num2} = {result2}')
#i = 0
#r = 0
#def sumfunc(a) :
#    while i == a:
#        i = i+1
#        r = 1 + (a+1)
#    return r
#num = int(input("1이상의 정수를 입력 하시오:"))
#if num > 0 : 
#    result = sumfunc(num)
#    print(f'{num} {result}')
#else :
#    print("1이상의 정수가 아닙니다.")
def sumfunc(num):
    sum = 0
    for j in range(1,num+1):
        sum = sum + j
    return sum

num = int(input("1이상의 정수를 입력하시오 :"))
if num > 0 :
    sum = sumfunc(num)
    
else :
    print("정수가 아닙니다.")
print(f"1~{num}까지 정수의 합은 {sum} 입니다.")
