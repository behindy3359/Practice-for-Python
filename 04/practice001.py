num_order = 1
num_object = 0
num_sum = 0

while num_order * 3 < 100:
    num_object = num_order * 3
    num_sum = num_sum + num_object
    print('num_order:%d num_object:%d num_sum:%d' %( num_order, num_object, num_sum))
    num_order = num_order + 1

print( '1~100까지의 3의 배수의 총 합은 %d입니다.' %(num_sum))
    