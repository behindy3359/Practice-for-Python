import random
print('while문과 break 문을 사용하여 컴퓨터가 기억하고 있는 1~10사이의 정수를 맞추는 프로그램을 구현하시오. 이때 사용자는 키보드로 예상하는 숫자를 입력한다.')

num_random = random.randint(1, 10)
num_input = 0
while  True :    
    num_input =int(input('숫자를 입력해주세요. :'))
    if num_input == num_random :
        print('correct, 정답입니다.')
        break
    else :
        if num_random < num_input :
            print('down, 틀렸습니다.')
        else :
            print('up, 틀렸습니다.')