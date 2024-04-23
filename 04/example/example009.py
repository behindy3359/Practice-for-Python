#use turtle
import turtle

def func():
    a=turtle.Pen()
    a.pencolor('red')
    a.shape('turtle')
    a.pensize(2)
    
    x=a.xcor()
    y=a.ycor()
    a.pendown()
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(70)
    a.forward(40)
    a.right(100)
    a.forward(100)
    a.pendown()
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(70)
    a.forward(40)
    a.right(100)
    a.forward(100)
    
    a.circle(50, 360)
    a.up()
    a.forward(100)
    a.pendown()
    
    a.write('문자그리기', True,'left',font=("돋움",24,"normal"))
    turtle.done()

    #메인 모듈일 때, 함수를 호출한다.
if __name__ == '__main__':
    func()