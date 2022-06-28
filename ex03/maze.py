import tkinter as tk
import maze_maker
import random

#グローバル変数
key = ""             #押されたキーを代入する関数
cx, cy =150, 150     #こうかとんの現在地を表す変数
mx, my = 1, 1
tmr = 0
jid = None
draw0 = 0            #最初に表示されるこうかとんの画像


#こうかとんを表示する関数
def draw(png_num):
    global tori, cx, cy, tori_id
    png = f"ex03/fig/{png_num}.png"
    tori = tk.PhotoImage(file = png)
    tori_id = canvas.create_image(cx, cy,
    image = tori, tag = "tori")

#押された数字キーに対応して画像を変更する関数
def change_img():
    img_list = ["0", "1", "2", "3", "4", "5" ,"6" ,"7", "8", "9"]
    if key in img_list:
        canvas.delete(tori_id)
        draw(key)
    maze.after(100, change_img)

#keyに押されたキーを代入する関数
def key_down(event):
    global key
    key = event.keysym

#keyの値を初期化する関数
def key_up(event):
    global key
    key = ""

#スタート地点とゴール地点決定する関数
def startgoal():
    global g_x, g_y
    while True:
        g_x = random.randint(12, 14)
        g_y = random.randint(5, 8)
        if meilo_list[g_y][g_x] == 0:
            break
    canvas.create_rectangle(100,100,200,200,fill = "yellow")               
    canvas.create_rectangle(g_x*100,g_y*100,(g_x*100)+100,
    (g_y*100)+100,fill = "blue")


#ゴール地点に到達するまで1秒ずつカウントする関数
def count_up():
    global tmr, jid
    tmr = tmr + 1
    label["text"] = tmr
    jid = maze.after(1000, count_up)

#ゴールしたかを判定しカウントを止める関数
def count_stop():                                                          
    global jid                                                           
    if mx == g_y and my == g_x:
        message = tk.Message(maze, text = "GOAL", font = ("" , 40),  #ゴール地点到達後"GOAL"が出現する
        bg = "red", fg = "white")
        message.pack()                                
        maze.after_cancel(jid)  

#押したキーによってこうかとんを移動させる関数
def main_proc():                                                         
    global cx, cy, key, tori, mx, my                                     
    if key == 'Up'      and  meilo_list[mx-1][my] == 0:                         
        cy -= 100                                                        
        mx -= 1                                                          
        
    elif key == 'Down'  and  meilo_list[mx+1][my] == 0:                    
        cy += 100                                                       
        mx += 1                                                         

    elif key == 'Right' and  meilo_list[mx][my+1] == 0:                   
        cx += 100                                                        
        my += 1                                                          

    elif key == 'Left'  and  meilo_list[mx][my-1] == 0:                    
        cx -= 100                                                        
        my -= 1  

    canvas.coords("tori", cx, cy)
    if  mx == g_y and my == g_x:                                  
        pass                                                             
    else:                                                                
        maze.after(100, main_proc)               #0.1秒に1回main_procを実行する                                    
    count_stop()


if __name__ == "__main__":

    #ウィンドウ作成
    maze = tk.Tk()
    maze.geometry("1500x900")
    maze.title("迷えるこうかとん")

    #ウィンドウ上にキャンバスを作成
    canvas = tk.Canvas(maze, width = 1500,
    height = 900,bg = 'black')   
    canvas.place(x=0, y=0)     

    maze.bind("<KeyPress>", key_down)            #キーを押すとkey_down関数を実行する           
    maze.bind("<KeyRelease>", key_up)            #キーを離すとkey_up関数を実行する
    maze.after(100, main_proc)
    label = tk.Label(font=("Ubunt Mono", 70),
                     bg = "gray1",fg = "snow")   
    label.pack()
    meilo_list = maze_maker.make_maze(15, 9)     #1:壁/0:床を表すリスト

    maze_maker.show_maze(canvas, meilo_list)

    count_up()
    startgoal()
    change_img()
    draw(draw0)
    maze.mainloop()