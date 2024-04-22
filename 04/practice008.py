print('판매과와 인사과 대리, 과장, 부장에 대한 수당을 순서대로 리스트에 저장하였다. 두개의 리스트 요솟값에 대한 차이를 각각 출력하시오. 단위는 만원이며, for 문을 사용하여 구현하시오')

panmaeSudang=[55, 67, 100]
insaSudang=[50, 60, 100]
className=['대리', '과장', '부장']

for i in range(len(panmaeSudang)):
    difference = (panmaeSudang[i]-insaSudang[i])
    print("%s 직급 수당 차이 : %d만원" %(className[i] ,difference))
