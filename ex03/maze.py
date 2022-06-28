import tkinter as tk
import maze_maker

#グローバル変数
key = ""             #押されたキーを代入する関数
cx, cy =150, 150     #こうかとんの現在地を表す変数
mx, my = 1, 1

#こうかとんを表示する関数
def draw():
    global tori, cx, cy
    png_num = 1
    png = f"ex03/fig/{png_num}.png"
    tori = tk.PhotoImage(file = png)
    tori_id = canvas.create_image(cx, cy,
    image = tori, tag = "tori")

#keyに押されたキーを代入する関数
def key_down(event):
    global key
    key = event.keysym

#keyの値を初期化する関数
def key_up(event):
    global key
    key = event.keysym
    key = ""

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
    maze.after(100, main_proc)
    canvas.coords("tori", cx, cy)

if __name__ == "__main__":

    #ウィンドウ作成
    maze = tk.Tk()
    maze.geometry("1500x900")
    maze.title("迷えるこうかとん")

    #ウィンドウ上にキャンバスを作成
    canvas = tk.Canvas(maze, width = 1500,
    height = 900,bg = 'black')   
    canvas.place(x=0, y=0)     

    maze.bind("<KeyPress>", key_down)                       
    maze.bind("<KeyRelease>", key_up)  
    maze.after(100, main_proc)
    meilo_list = maze_maker.make_maze(15, 9) #1:壁/0:床を表すリスト
    maze_maker.show_maze(canvas, meilo_list)
    draw()
    maze.mainloop()