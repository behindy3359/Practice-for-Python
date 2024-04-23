print('경로 지정 방법1 -> import 패키지명.모듈명')

import pack.mymod1
print(dir(pack. mymod1))

print('\mymod1의 함수 호출----')
list1 =[1,3]
list2 =[2,4]
pack.mymod1.listhap(list1,list2)
print('다른 모듈의 전역 변수 읽기 tot:', pack.mymod1.tot)

print('경로 지정 방법2 -> from 패키지명 import 모듈명')
from pack import mymod1
mymod1.kbs()
print('다른 모듈의 전역 변수 읽기 tot:', mymod1.tot)

print('\경로지정 방법 3 -> from 패키지명.모듈명 import 함수명,...변수,....')
from pack.mymod1 import mbc
mbc()