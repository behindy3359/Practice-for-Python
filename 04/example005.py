#built_in_function
print(sum([3,5,7]))

print(int(1.7))
print(float(3))

print(str(5)+': 숫자 오')

a = 10

print('eval 결과 :', eval('a+5'))
print('round(1.7)+round(1.3) :' , round(1.7),round(1.3))

b_list=[True, 1, False]
print(all(b_list))
print(any(b_list))

b_list2 = [1,3,5,7,9]
print('모든 숫자가 10 미만인가? :', all(a<10 for a in b_list2))
print('숫자들 중 5 미만인 수가 있는가? :', any(a<5 for a in b_list2))

x=[10, 20, 30]
y=['a', 'b']

for i in zip(x,y):
    print(i)