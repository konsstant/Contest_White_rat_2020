import math
import pygame
import sys
import random
import pygame.font

scene_x=800
scene_y=800

border=10

v=[]

x=[]
y=[]
z=[]

vt=[]

vn=[]

f=[]

triangel=[]

vertexs_x=[]
vertexs_y=[]
vertexs_z=[]

scale_x=1
scale_y=1
scale_z=1
scale_all=1

file_name="rat2020_03.obj"

v_count=0
f_count=0

StopShow=True

def load_data (file_name):

    file=open(file_name,"rt")

    for line in file:
        #print(line)
        if line[0]=="v" and line[1]==" ":
            v.append(line)
        if line[0]=="v" and line[1]=="t":
            vt.append(line)
        if line[0]=="v" and line[1]=="n":
            vn.append(line)
        if line[0]=="f" and line[1]==" ":
            f.append(line)
    file.close()

    for i in range(0, len(v)):
        _,x_cash,y_cash,z_cash=v[i].split(" ")
        x.append(float(x_cash))
        y.append(float(y_cash))
        z.append(float(z_cash))

    for i in range(0,len(f)):
        _,vertex1,vertex2,vertex3=f[i].split(" ")
        vertex1_1,vertex1_2,vertex1_3=vertex1.split("/")
        vertex2_1, vertex2_2, vertex2_3 = vertex2.split("/")
        vertex3_1, vertex3_2, vertex3_3 = vertex3.split("/")

        vertex=int(vertex1_1),int(vertex2_1),int(vertex3_1),int(vertex1_2),int(vertex2_2),int(vertex3_2),int(vertex1_3),int(vertex2_3),int(vertex3_3)

        triangel.append(vertex)


def data_print():

    for i in range (0,len(v)):
      print(v[i])
      print(str(x[i])+" "+str(y[i])+" "+str(z[i]))

    for i in range(0,len(vt)):
      print(vt[i])

    for i in range(0,len(vn)):
        print(vn[i])

    for i in range(0,len(f)):
        print(f[i])
        print(triangel[i])

    print("length v- > "+str(len(v)))
    print("length vt- > " + str(len(vt)))
    print("length vn- > " + str(len(vn)))
    print("length f- > " + str(len(f)))

def min (list):
    pass
    min=0
    for i in range (0,len(list)):
        if min>list[i]:
            min=list[i]
    return min

def max (list):
    pass
    max=0
    for i in range (0,len(list)):
        if max<list[i]:
            max=list[i]
    return max

def scale_calculation(scene_x,scene_y,border,general_scale):

    x_max=max(x)
    x_min=min(x)

    y_max=max(y)
    y_min=min(y)

    z_max=max(z)
    z_min=min(z)

    x_canva=x_max+abs(x_min)
    y_canva=y_max+abs(y_min)
    z_canva=z_max+abs(z_min)

    #print("X_max -> " + str(x_max))
    #print("X_min -> " + str(x_min))

    #print("Y_max -> " + str(y_max))
    #print("Y_min -> " + str(y_min))

    #print("Z_max -> " + str(z_max))
    #print("Z_min -> " + str(z_min))

    #print("Canva_X -> " + str(x_canva))
    #print("Canva_Y -> " + str(y_canva))
    #print("Canva_Z -> " + str(z_canva))

    scale_x = (scene_x-border*2)/x_canva
    scale_y = (scene_y-border*2)/y_canva
    if scale_x<scale_y or scale_x==scale_y:
        scale_all=scale_x
    else:
        scale_all=scale_y

    scale_z =scale_all

    #print(str(scale_x))
    #print(str(scale_y))
    #print(str(scale_z))

    #print("Scale ->"+str(scale_all))
    #print(scale_all)

    return scale_all*general_scale


def recalc_points():

    scale=scale_calculation(scene_x, scene_y, border,0.55)
    print("SCALE "+str(scale))

    for i in range (0,len(x)):

        vertexs_x.append(int(x[i]*scale)+(int(scene_x/2)+border))
        vertexs_y.append(int(y[i]*scale*-1)+(int(scene_y/2)-border))
        vertexs_z.append(int(z[i]*scale*1))
        #print(str(vertexs_x[i])+" "+str(vertexs_y[i])+" "+str(vertexs_z[i]))


def Render(angel,x_ofset):

    r=[]
    fi=[]
    rotate_x=[]
    rotate_y=[]

    scale = scale_calculation(scene_x, scene_y, border,0.55)

    COLOR = (255, 255, 255)

    for i in range(0,len(z)-1):

        r.append(math.sqrt(x[i]*x[i]+z[i]*z[i]))
        fi.append(angel+math.degrees(math.atan2(1*z[i],-1*x[i])))


        rotate_x.append(int(scene_x/4)+border-int(scale*(r[i]*math.cos(math.radians(fi[i])))))
        rotate_y.append(int(scene_y/4)+border-int(scale*(r[i]*math.sin(math.radians(fi[i])))))

        #print("R " + str(r[i]))
        #print("Fi " + str(fi[i]))
        #print("X " + str(rotate_x[i]))
        #print("Y " + str(rotate_y[i]))

    for i in range(0,len(triangel)-6):

        pygame.draw.line(screen,COLOR,[rotate_x[triangel[i][0] - 1]+x_ofset, vertexs_y[triangel[i][0] - 1]], [rotate_x[triangel[i][1] - 1]+x_ofset,vertexs_y[triangel[i][1] - 1]])
        pygame.draw.line(screen,COLOR,[rotate_x[triangel[i][1] - 1]+x_ofset, vertexs_y[triangel[i][1] - 1]], [rotate_x[triangel[i][2] - 1]+x_ofset,vertexs_y[triangel[i][2] - 1]])
        pygame.draw.line(screen,COLOR,[rotate_x[triangel[i][2] - 1]+x_ofset, vertexs_y[triangel[i][2] - 1]], [rotate_x[triangel[i][0] - 1]+x_ofset,vertexs_y[triangel[i][0] - 1]])

    Clock_wise_button.draw_button()
    Counter_clock_wise_button.draw_button()


    if Show_try:
        Try_to_guess.draw_button()

    if Show_right:
        Guess_right_button.draw_button()

    if Show_wrong:
        Guess_wrong_button.draw_button()


class Button():

    def __init__(self,screen,msg,x_pos,y_pos,centring,wight):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width,self.height=wight,60
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,36)


        if centring==True:
            self.rect = pygame.Rect(0,0, self.width, self.height)
            self.rect.center = self.screen_rect.center
        else:
            self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)

        self.prep_msg(msg)

    def prep_msg(self,msg):
         self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
         self.msg_image_rect=self.msg_image.get_rect()
         self.msg_image_rect.center=self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


pygame.init()
load_data(file_name)
recalc_points()

screen=pygame.display.set_mode((scene_x+border*2,scene_y+border*2))
pygame.display.set_caption("White Rat 2000 SH++ Contest")

Clock_wise_button=Button(screen,"Clockwise",15,725,False,300)
Counter_clock_wise_button=Button(screen,"Counter сlockwise",500,725,False,300)

Guess_right_button=Button(screen,"You GUESS ! The White RAT is HAPPY !",110,10,False,600)
Guess_wrong_button=Button(screen,"Don't give up ! Try again !",110,10,False,600)
Try_to_guess=Button(screen,"Try to guess the direction of rotation!",110,10,False,600)

i=0
direction=1
direction_control=0
clockwise=True

Show_right=False
Show_wrong=False
Show_try=True

while StopShow:

    screen.fill((126,0, 126))
    Render(i, 200)
    pygame.display.update()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if Clock_wise_button.rect.collidepoint(mouse_x, mouse_y) and StopShow == True:
                if clockwise == True:
                    Show_right = True
                    Show_wrong = False
                    Show_try = False
                    #print("Clockwise -> True", i, direction_control)
                else:
                    Show_right = False
                    Show_wrong = True
                    Show_try = False
                    #print("Clockwise -> False", i, direction_control)

            if Counter_clock_wise_button.rect.collidepoint(mouse_x, mouse_y) and StopShow == True:
                if clockwise == False:
                    Show_right = True
                    Show_wrong = False
                    Show_try = False
                    #print("Counter сlockwise -> True", i, direction_control)
                else:
                    Show_right = False
                    Show_wrong = True
                    Show_try = False
                    #print("Counter сlockwise -> False", i, direction_control)




    direction_control = i
    i += direction



    if i > 0:
        if direction_control<i:
            clockwise=False
        if direction_control>i:
            clockwise=True

    if i < 0:
        if direction_control > i:
            clockwise = False
        if direction_control < i:
            clockwise = True



    if i>=360 or i<=-360:
        direction = random.choice([1, -1])







