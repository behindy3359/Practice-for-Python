print('중첩 while 문을 사용하여 다음과 같이 별 문자를 출력하시오.')
print('*')
print('**')
print('***')
print('****')
print('*****')
print('____________________________')

num_order = 1
num_state = 1
str_print = ''

while num_order <= 5:
    num_state = num_order
    while num_state != 0:
        str_print = str_print + '*'
        num_state = num_state-1
    print(str_print)
    str_print = ''
    num_order = num_order + 1