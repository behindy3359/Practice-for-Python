def divideFunc(a,b):
    return a/b

print('뭔가를 하다가...')
c = divideFunc(5,2)
print(c)

try:
    c = divideFunc(5,2)
    print(c)
    
    aa=[1,2]
    print(aa[0])
    
    f=open('c:/abc.txt')
except ZeroDivisionError:
    print('두번째 숫자로 0 은 안돼!')
except IndexError as e:
    print('참조범위 오류:', e)
except Exception as e:
    print('에러발생:', e)
finally:
    print('에러 여부에 관계없이 수행')
print('정상종료')    