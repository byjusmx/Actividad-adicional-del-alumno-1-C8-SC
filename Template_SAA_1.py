import turtle

wn = turtle.Screen()

wn.bgcolor()#Escribe light green - verde claro, como el color

turtle.color()#Escribe blue - azul, como el color

def sqrfunc():#Pasa el valor de size y speed
    for i in range(4):
        (size, speed) = (size + 5, speed + 5)
        (turtle.speed())#Utiliza la variable speed
        turtle.fd()#Utiliza la variable name
        turtle.left(90)

sqrfunc(6, 2)
sqrfunc(26, 5)
sqrfunc(46, 7)
sqrfunc(66, 10)
sqrfunc(86, 15)
sqrfunc(106, 20)
sqrfunc()#Rellena con los valores 116,30
sqrfunc()#Rellena con los valores 136,40
