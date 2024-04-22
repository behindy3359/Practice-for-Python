print('중첩 while문을 사용하여 구구단 중에서 2단, 3단을 출력하시오.')

num_order = 1
num_dan = 2

while num_dan < 4 :
    
    while num_order < 10 :
        print('%d X %d = %d' %(num_dan, num_order, num_order*num_dan))
        num_order = num_order + 1
    num_order = 1
    num_dan = num_dan + 1