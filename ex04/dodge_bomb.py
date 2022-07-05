from re import T
import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def main():
    #練習1:ウィンドウ作成
    pg.display.set_caption("逃げろ! こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))           #Surface
    screen_rct = screen_sfc.get_rect()                     #Rect
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")         #Surface
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)   
    clock = pg.time.Clock()                    #時間計測用のオブジェクト

    kkimg_sfc = pg.image.load("ex04/fig/6.png")    #Surface
    pg.transform.rotozoom(kkimg_sfc, 0, 2.0)      #Surface
    kkimg_rct = kkimg_sfc.get_rect()                #Rect
    kkimg_rct.center = 900, 400

    #練習５:爆弾を作成
    bmimg_sfc = pg.Surface((20, 20))            #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()             #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    #練習6:爆弾を移動させる
    vx, vy = +1, +1




    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct) 

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習4:
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: 
            kkimg_rct.centery -= 1     #Y座標を-1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 1     #Y座標を+1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 1     #X座標を-1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 1     #X座標を+1

        #練習7:こうかとんと爆弾が外に出ないようにする
        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP] == True: 
                kkimg_rct.centery += 1     #Y座標を-1
            if key_states[pg.K_DOWN] == True:
                kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True:
                kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                kkimg_rct.centerx -= 1

        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        #練習6
        bmimg_rct.move_ip(vx, vy)
        #練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        #練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate
        
        #練習8:こうかとんと爆弾がぶつかった後の処理
        if kkimg_rct.colliderect(bmimg_rct):
            tkm.showinfo("", "GAME OVER!!")     
            return

        pg.display.update()
        clock.tick(1000) #1000fpsの時を刻む

#爆弾が壁にぶつかると反射する関数
def check_bound(rct, screen_rect):
    yoko, tate = +1, +1
    if rct.left < screen_rect.left or screen_rect.right < rct.right:
        yoko = -1
        yoko -= 0.1   #壁に反射すると爆弾の速さが0.1速くなる
    if rct.top < screen_rect.top or screen_rect.bottom < rct.bottom:
        tate = -1
        tate -= 0.1   #壁に反射すると爆弾の速さが0.1速くなる
    return yoko, tate
                 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
