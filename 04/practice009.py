print('for 문을 사용하여 구구단 2단부터 9단까지 출력하는 프로그램을 구현하시오.')

for i in range(8):
    for j in range(9):
        print(f'{i+2}X{j+1}={(i+2)*(j+1)}')