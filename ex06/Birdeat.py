import pygame as pg
import sys
import random
import pygame.mixer


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
            
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

#リンゴを描写する関数
class tama:
    def __init__(self,size,image,vxy,scr: Screen):
        self.sfc = pg.image.load(image)                   
        self.sfc = pg.transform.rotozoom(self.sfc, 0,size)
        self.rct = self.sfc.get_rect()                   
        self.rct=self.sfc.get_rect() # Rect
        self.rct.centerx = 1700
        self.rct.centery = random.randint(0,900)
        self.vx, self.vy = vxy # 練習6


    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr: Screen):#移動を制御
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.blit(scr)

    
def music():
    pygame.mixer.init()    # 初期設定
    pygame.mixer.music.load("ex06/fig/MusMus-BGM-146.mp3")     # 音楽ファイルの読み込み
    pygame.mixer.music.play(-1)                                # 音楽の再生回数(無限)

def main():
    font = pg.font.Font(None, 55)
    score = 0

    ysp=random.randint(1,4)
    ysp1=random.randint(1,4)
    ysp2=random.randint(1,4)

    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "ex06/fig/pg_bg.jpg")
    kkt = Bird("ex06/fig/6.png", 2.0, (900, 400))
    ane = tama(0.5,"ex06/fig/apple.png",(-ysp,0),scr)#リンゴを生成
    ane1 = tama(0.5,"ex06/fig/apple.png",(-ysp1,0),scr)#リンゴを生成
    ane2 = tama(0.5,"ex06/fig/apple.png",(-ysp2,0),scr)#リンゴを生成
    beam = None

    music()
    while True:
        scr.blit()
        text = font.render(str(score), True, (255,0,0))   # 描画する文字列の設定
        scr.sfc.blit(text, [1600//2, 100])

        ysp=random.randint(1,4)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beam.append(kkt.attack())

        kkt.update(scr)
        ane.update(scr)
        ane1.update(scr)
        ane2.update(scr)

        pg.display.update()
        clock.tick(1000)

        if kkt.rct.colliderect(ane.rct):#リンゴに当たった時の処理
            score+=10
            ane.rct.move_ip(1800,ysp)
            ane.rct.centery = random.randint(0,900)
            
        if kkt.rct.colliderect(ane1.rct):#リンゴに当たった時の処理
            score+=10
            ane1.rct.move_ip(1800,ysp)
            ane1.rct.centery = random.randint(0,900)

        if kkt.rct.colliderect(ane2.rct):#リンゴに当たった時の処理
            score+=10
            ane2.rct.move_ip(1800,ysp)
            ane2.rct.centery = random.randint(0,900)

#リンゴが画面外に出たときの処理
        if ane.rct.left<=0: # 領域外  
            ane.rct.move_ip(1800,ysp)
            ane.rct.centery = random.randint(0,900) 

        if  ane1.rct.left<=0:# 領域外
            ane1.rct.move_ip(1800,ysp)
            ane1.rct.centery = random.randint(0,900)

        if ane2.rct.left<=0: # 領域外
            ane2.rct.move_ip(1800,ysp)
            ane2.rct.centery = random.randint(0,900)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or リンゴのRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()