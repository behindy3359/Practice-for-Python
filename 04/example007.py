def area_tri(a,b):
    c=a*b/2
    print('순서 2')
    area_print(c)
    print('순서 4')
def area_print(c):
    print('순서 3')
    print('삼각형의 면적은',c)
    
print('순서 1')
area_tri(20,50)
print('순서 5')