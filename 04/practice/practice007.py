import time
print('직원 자료를 키보드로 입력받아 조건에 맞게 가공한 후 출력하시오. 이때 while문과 break 문을 사용하여 구현하시오.')

str_input = ''
str_check = 'y'
str_check_input = ''
str_list=[]
now=time.localtime()
today=int(now.tm_year)

while str_check== 'y' :
    str_input = input('사번,이름,기본급,입사년도 입력')
    str_list.append(str_input)
    str_check=input('계속 입력하시겠습니까?[y/n]')

print('목록 :',str_list)

num_order = 0
str_list_index=[]
str_nth_index=''
num_seniority = 0
str_id=''
str_name=''
num_pay=0
num_seniority_pay=0
num_ded=0
num_real_pay=0
print('사번 이름   기본급  근무년수  근속수당  공제액  수령액')
while num_order < (len(str_list)) :
    str_list_index = str(str_list[num_order]).split(',')
    num_seniority = today-int(str_list_index[3])
    str_id=str_list_index[0]
    str_name=str_list_index[1]
    num_pay=int(str_list_index[2])
    num_ded=0
    num_real_pay=0
    
    if num_seniority<4:
        num_seniority_pay=50
    elif num_seniority<8:
        num_seniority_pay=100
    else :
        num_seniority_pay=150
        
    if (num_pay +num_seniority_pay) > 500:
        num_ded = 0.03
    elif (num_pay+num_seniority_pay)>400:
        num_ded = 0.02
    else :
        num_ded = 0.01
    num_real_pay = (num_pay + num_seniority_pay)*(1-num_ded)
    print('%s    %s%d    %d          %d          %d          %d' %(str_id, str_name, num_pay, num_seniority, num_seniority_pay, (num_pay+num_seniority_pay)*num_ded, num_real_pay))
    num_order= num_order+1