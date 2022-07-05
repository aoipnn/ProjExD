from re import T
import pygame as pg
import sys
import random

def main():
    #練習1
    pg.display.set_caption("逃げろ! こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))           #Surface
    screen_rct = screen_sfc.get_rect()                     #Rect
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")         #Surface
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)   
    clock = pg.time.Clock()                    #時間計測用のオブジェクト
    # clock.tick(0.2)                              #1fpsの時を刻む
    # pg.display.update()

    kkimg_sfc = pg.image.load("ex04/fig/6.png")    #Surface
    pg.transform.rotozoom(kkimg_sfc, 0, 2.0)      #Surface
    kkimg_rct = kkimg_sfc.get_rect()                #Rect
    kkimg_rct.center = 900, 400

    #練習５
    bmimg_sfc = pg.Surface((20, 20))            #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()             #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    #練習6
    vx, vy = +1, +1




    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct) 

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #練習4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: 
            kkimg_rct.centery -= 1     #Y座標を-1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        #練習6
        bmimg_rct.move_ip(vx, vy)
        #練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)



  
            

        pg.display.update()
        clock.tick(1000)   


    
                 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
