class Nice:
    name=''
    def __init__(a, k):
        a.name=k
        print('생성자 메소드에 의해 '+k+'객체가 생성됨')
    def __del__(b):
        del b.name

obj = Nice('tom')
