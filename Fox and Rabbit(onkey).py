import turtle,random,time
wn=turtle.Screen()
wn.setup(900,700)
wn.bgpic('forest_edge.gif')
wn.tracer(20)
rabbit=[]
N=5
Xpos=[]
angle=[]
L=[]
wn.addshape('Rabbit1.gif')
for i in range(N):
    rabbit.append(turtle.Turtle())
    Xpos.append(0)
    rabbit[i].up()
    rabbit[i].shape('Rabbit1.gif')
    rabbit[i].setposition(-550,random.randint(-200,0))
    Xpos[i]=rabbit[i].xcor()
    angle.append(0)
    L.append(0)
    angle[i]=random.randint(20,70)
rabbit[0].hideturtle()
fox=turtle.Turtle()
wn.addshape('fox1.gif')
wn.addshape('fox2.gif')
wn.addshape('fox3.gif')
wn.addshape('fox4.gif')
fox.shape('fox1.gif')
fox.up()
fox.goto(300,-50)
turtle.tracer(2)
j=-1
start = time.time()
n=0
while True:
    for i in range(N):
        time.sleep(0.1)
        rabbit[i].setheading(angle[i])
        for q in range(50):
            rabbit[i].fd(1)
        time.sleep(0.2)
        rabbit[i].setheading(-angle[i])
        for q in range(50):
            rabbit[i].fd(1)
        Xpos[i]=rabbit[i].xcor()
        if Xpos[i]>450:
            rabbit[i].setx(-450)
    time.sleep(0.1)
    for z in range(1,N):
        L[z]=abs(rabbit[z].position()-fox.position())
        if L[z]<35:
            rabbit[z].hideturtle()
            rabbit[z].goto(500,500)
            n=n+1
            print('number=',n)
           
            if n>N-2:
                print('n=',n)
                finish = time.time()
                time_finish=finish-start
                text=turtle.Turtle()
                text.up()
                text.hideturtle()
                text.goto(-100,200)
                text.color('white')
                text.write('GAME OVER',font=('Aril',20,'bold'))
                text.goto(-100,100)
                text.write('Time(seconds)=',font=('Aril',20,'bold'))
                text.goto(150,100)
                text.write(round(time_finish),font=('Aril',20,'bold'))
                
        def move_up():
            global j
            j=j+1
            j1=j%2
            fox.setheading(90)
            if j1==0:
                fox.shape('fox1.gif')
            if j1==1:
                fox.shape('fox2.gif')
            fox.fd(5)
        def move_down():
            global j
            j=j+1
            j1=j%2
            fox.setheading(-90)
            if j1==0:
                fox.shape('fox1.gif')
            if j1==1:
                fox.shape('fox2.gif')
            fox.fd(5)
        def move_right():
            global j
            j=j+1
            j1=j%2
            fox.setheading(0)
            if j1==0:
                fox.shape('fox3.gif')
            if j1==1:
                fox.shape('fox4.gif')
            fox.fd(10)
        def move_left():
            global j
            j=j+1
            j1=j%2
            fox.setheading(180)
            if j1==0:
                fox.shape('fox1.gif')
            if j1==1:
                fox.shape('fox2.gif')
            fox.fd(5)
    wn.onkey(move_up,'Up')
    wn.onkey(move_down,'Down')
    wn.onkey(move_right,'Right')
    wn.onkey(move_left,'Left')
    wn.listen()

