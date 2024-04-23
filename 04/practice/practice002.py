num_order = 1
num_state = 0
num_sum = 0
num_list = []

print('1~100 사이의 정수 중에서 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 구하여 출력하시오, 이때 while 문을 사용하여 구현하시오')
while num_order *3 < 100 :
    num_state = num_order * 3
    if (num_state % 2) == 0 :
        num_order = num_order + 1
    else :
        num_list.append(num_state)
        num_sum = num_sum + num_state
        num_order = num_order + 1

print ('1~100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수 :' , num_list)
print ('1~100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수들의 합 :', num_sum)