from re import T
import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ! こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))           #Surface
    # screen_rct = screen_sfc.getrect()                     #Rect
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

  
            

        pg.display.update()
        clock.tick(1000)   


    
                 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
