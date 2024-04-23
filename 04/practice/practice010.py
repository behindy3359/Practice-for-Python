#선언부
import random

#함수 정의
def checkfunction(a, b):
    f = any(c==b for c in a)
    return f 

#문제
print('임의의 정수를 가진 리스트에서 특정 숫자를 찾는 함수를 작성한 후, 특정 숫자의 포함 여부를 확인하는 코드를 작성하시오.')

#변수 선언
numRandomList=[]

#무작위 정수 리스트 생성
while len(numRandomList) < 5:
    b=random.randint(1,20)
    numRandomList.append(b)

#정수 리스트 확인
print(numRandomList)
t =[]
#포함 여부 확인

while True:
    c=int(input('포함 여부를 확인 할 숫자를 입력해주세요 : '))
    k = checkfunction(numRandomList, c)
    if k ==True:
        print(c, ': 존재합니다.')
        print('확인한 숫자들 : ',t)
        break
    else :
        print(c, ': 존재하지 않습니다.')
        t.append(c)