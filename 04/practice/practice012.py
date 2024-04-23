print('재귀 함수를 이용하여 다음과 같이 구구단 3단을 출력하시오.')
def showGugudan(n):
    if n != 10:
        print(3,'X',n,'=',(3*n))
        showGugudan(n+1)
showGugudan(1)