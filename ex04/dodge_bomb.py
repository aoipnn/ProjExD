import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ! こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))           #Surface
    # screen_rct = screen_sfc.getrect()                       #Rect
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")                     #Surface
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)   
    clock = pg.time.Clock()                    #時間計測用のオブジェクト
    # clock.tick(0.2)                              #1fpsの時を刻む
    # pg.display.update()

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)    

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock.tick(1000)   
                 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
