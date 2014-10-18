"""
Здравствуйте Алмас!
Код индийский,Извините за это) делала из того, что знаю.
Вот ссылки откуда я все это брала (делала только по туториалам):
https://www.youtube.com/watch?v=VReH9L84pTA
https://www.youtube.com/watch?v=mEX0R1NOk7Q
Надеюсь не запутаетесь)
"""

import pygame,sys,pygame.mixer
import math
import random
from pygame.locals import*

pygame.init()

sound = pygame.mixer.Sound("C:/Python27/All_for_game/Ment.wav")
fale=pygame.mixer.Sound("C:/Python27/All_for_game/fale.wav")
clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()
screen=pygame.display.set_mode((1100,668))
pygame.display.set_caption("Sun System")

window=pygame.Surface((400,30))


info_string=pygame.Surface((400,30))



bg = pygame.image.load("C:/Python27/All_for_game/6.jpg").convert_alpha()
image=pygame.image.load("C:/Python27/All_for_game/4.png").convert_alpha()#Ракета
aster=pygame.image.load("C:/Python27/All_for_game/2.png").convert_alpha()#Астероид большой
salut=pygame.image.load("C:/Python27/All_for_game/GO2.png").convert_alpha()
aster1=pygame.transform.scale(aster,(70,70))
aster2=pygame.transform.scale(aster1,(35,35))






x=0
y=0





a=150
b=326
c=485
d=680
f=753
g=900
h=1100
i=1390
j=1510
k=1600
l=1770
m=1700
n=1950
o=2000
p=2160
r=2250
s=2370
t=2480

q=150
ab=230
ac=370
ad=300
ae=70
af=250
ag=160
ah=445
aj=600
ak=70
al=150
am=190
an=230
ao=390
ap=440
ar=560
bs=700
bt=90
ai=387

pygame.font.init()
speed_font=pygame.font.Font(None,32)


def asteroid():
        
        info_string.fill((45,80,40))
        screen.blit(aster,(a,q))
        screen.blit(aster,(b,ab))
        screen.blit(aster1,(c,ac))
        screen.blit(aster,(d,ad))
        screen.blit(aster1,(f,af))
        screen.blit(aster,(g,ag))
        screen.blit(aster1,(h,ah))
        screen.blit(aster2,(i,ai))
        screen.blit(aster1,(j,aj))
        screen.blit(aster,(k,ak))
        
        screen.blit(aster1,(l,al))
        screen.blit(aster2,(m,am))
        screen.blit(aster1,(n,an))
        screen.blit(aster,(o,ao))
        screen.blit(aster2,(p,ab))
        screen.blit(aster2,(r,ar))
        screen.blit(aster1,(s,s))

        info_string.blit(speed_font.render('Time;',1,(210,120,200)),(10,5))




run=True


speed=1
while run:
    sound.play()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    screen.blit(info_string,(0,0))
    asteroid()
    pygame.display.flip()
    

    a=a-0.5
    b=b-0.5
    c=c-0.5
    d=d-0.5
    f=f-0.5
    g=g-0.5
    h=h-0.5
    i=i-0.5
    j=j-0.5
    k=k-0.5
    l=l-0.5
    m=m-0.5
    n=n-0.5
    o=o-0.5
    p=p-0.5
    r=r-0.5
    s=s-0.5
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                sys.exit()
        elif e.type == pygame.KEYDOWN and e.key==K_DOWN:
                y=y+70
        elif e.type == pygame.KEYUP and e.key==K_UP:
                y=y-70
        if (a-100)<x and (a+70)>x and y>(q-70) and y<(q+70):
                sound.stop()
                image=salut
                sound=fale
                screen.blit(image,(x-50,y))
                sound.play()
        elif (b-100)<x and (b+70)>x and y>(ab-70) and y<(ab+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (c-100)<x and (c+70)>x and y>(ac-70) and y<(ac+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (d-100)<x and (d+70)>x and y>(ad-70) and y<(ad+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (f-100)<x and (f+70)>x and y>(af-70) and y<(af+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (g-100)<x and (g+70)>x and y>(ag-70) and y<(ag+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (h-100)<x and (h+70)>x and y>(ah-70) and y<(ah+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (i-100)<x and (i+70)>x and y>(ai-70) and y<(ai+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (j-100)<x and (j+70)>x and y>(aj-70) and y<(aj+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (k-100)<x and (k+70)>x and y>(ak-70) and y<(ak+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (l-100)<x and (l+70)>x and y>(al-70) and y<(al+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (m-100)<x and (m+70)>x and y>(am-70) and y<(am+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (n-100)<x and (n+70)>x and y>(an-70) and y<(an+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (o-100)<x and (o+70)>x and y>(ao-70) and y<(ao+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (p-100)<x and (p+70)>x and y>(ap-70) and y<(ap+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (r-100)<x and (r+70)>x and y>(ar-70) and y<(ar+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (s-100)<x and (s+70)>x and y>(bs-70) and y<(bs+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()
        elif (t-100)<x and (t+70)>x and y>(bt-70) and y<(bt+70):
                sound.stop()
                sound=fale
                image=salut
                screen.blit(image,(x-50,y))
                sound.play()


run=False


pygame.quit()
