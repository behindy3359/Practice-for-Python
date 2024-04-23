print('-1,3,-5,7,-9,11~99 까지의 합을 출력하시오. 이때 while 문을 사용하여 구현하시오')

num_order = 1
num_state =0
num_sum = 0
while ((num_order*2) -1) < 100:
    num_state =((num_order*2)-1)
    if (num_order % 2) == 0 :
        num_sum = num_sum +num_state
        print('num_order :%d num_state :%d num_sum :%d' %( num_order, num_state, num_sum))
        num_order = num_order + 1
    else :
        num_state = num_state*(-1)
        num_sum = num_sum +num_state
        print('num_order :%d num_state :%d num_sum :%d' %( num_order, num_state, num_sum))
        num_order = num_order + 1
print('-1, 3 , -5, 7, -9, 11 ~99 까지의 합', num_sum)