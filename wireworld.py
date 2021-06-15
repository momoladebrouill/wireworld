import pygame as pg

import random
import math
from colorsys import hsv_to_rgb
"""à alléger et clarifier"""
# Constantes :
FPS = 60  # les fps tabernak
WIND = 750 # dimentions de la fentere
nbs=10 #le nombre de celules sur la grid
SIZE = WIND/nbs #la taille des cellules

fps = pg.time.Clock()

class dep:
    x=0
    y=0
    sped=-10
    def __repr__(self):
        return str((self.x,self.y))

def find(tup):return lieux.get(tup,0)==2

lieux={}
b = 1
mode=''
ct=0

try:
    pg.init()
    f = pg.display.set_mode(size=(WIND, WIND))
    pg.display.set_caption("crédit @ryanair aka soldat µ")
    font=pg.font.SysFont('consolas',25,1)
    while b:
        pg.display.flip()
        f.set_alpha(10)
        f.fill(0)
        b+=1
        si = pg.key.get_pressed()  # SI la touche est appuyée
        if si[pg.K_q]:dep.x-=dep.sped
        if si[pg.K_s]:dep.y+=dep.sped
        if si[pg.K_d]:dep.x+=dep.sped
        if si[pg.K_z]:dep.y-=dep.sped
        if not b%10:
            nex={}
            for pos in lieux:
                if lieux[pos]==3: nex[pos]=1
                elif lieux[pos]==2: nex[pos]=3
                elif lieux[pos]==1:
                    nei=[(pos[0]-1,pos[1]-1),(pos[0],pos[1]-1),(pos[0]+1,pos[1]-1),
                        (pos[0]-1,pos[1])        ,(pos[0]+1,pos[1]),
                        (pos[0]-1,pos[1]+1),(pos[0],pos[1]+1),(pos[0]+1,pos[1]+1)]
                    som=0
                    for i in nei: som+=find(i)
                    if som and som<3:
                        nex[pos]=2
                    else:
                        nex[pos]=1
            lieux={}
            lieux.update(nex)
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                b = False
                print(" Il y avait {0} cellules".format(len(lieux)))
            if event.type == pg.KEYDOWN:
                touche=event.dict['key']
                nbs=int(WIND/SIZE)
                if touche == pg.K_a:
                    for i in range(nbs):
                        for j in range(nbs):
                            lieux[(i,j)]=1
                elif touche == pg.K_e:
                    lieux={}
                    
            elif event.type ==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    
                    if lieux.get((x,y))==1:
                        lieux[(x,y)]=2
                    else:
                        mode='c'
                elif event.button==3:
                    mode='e'
            elif event.type == pg.MOUSEBUTTONUP:
                mode=''
                
                if event.button==4:
                    SIZE+=5
                    dep.x-=x*5
                    dep.y-=y*5
                elif event.button==5:
                    SIZE-=5
                    if SIZE<=0:
                        SIZE=1
                    else:
                        dep.x+=x*5
                        dep.y+=y*5

                nbs=int(WIND/SIZE)
                
                
        x,y=pg.mouse.get_pos()
        x=round((x-dep.x)/SIZE)-0.5
        y=round((y-dep.y)/SIZE)-0.5
        
        if mode=='c':
            
            lieux[(x,y)]=1
        elif mode=='e':
            if (x,y) in lieux:lieux.pop((x,y))
        for i,j in lieux:
            if i>-dep.x/SIZE-1 and j>-dep.y/SIZE-1 and i<-dep.x/SIZE+nbs and j<-dep.y/SIZE+nbs: # si on a besoin de le dessiner
                numo=lieux[(i,j)]
                if numo==1:
                    pg.draw.rect(f,(0,0,255),((dep.x+i*SIZE,dep.y+j*SIZE),(SIZE,SIZE)))
                elif numo==2:
                    pg.draw.rect(f,(255,255,255),((dep.x+i*SIZE,dep.y+j*SIZE),(SIZE,SIZE)))
                elif numo==3:
                    pg.draw.rect(f,(255,0,0),((dep.x+i*SIZE,dep.y+j*SIZE),(SIZE,SIZE)))
        pg.draw.rect(f,0,((x*SIZE+dep.x,y*SIZE+dep.y),(SIZE,SIZE)),width=3)
##        f.blit(font.render(str(sel),10,(0,255,0)),(0,0))
##        f.blit(font.render(str({'x':x,'y':y,'size':SIZE}),10,(0,255,0)),(0,20))
        
        fps.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()
