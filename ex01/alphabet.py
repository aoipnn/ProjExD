import random
kesson = 2
mojisuu = 10
kurikaeshi = 5

def main():
    for _ in range(kurikaeshi):
        seikai = mondai()
        kaitou()

def mondai():
    global mojisuu, kesson
    alphabets = [chr(j+65) for j in range(26)]
    al_list = random.sample(alphabets, mojisuu)
    print(f"対象文字：{al_list}")

    kesson_al_list = random.sample(al_list, kesson)
    print(f"欠損文字{kesson_al_list}")


def kaitou():
    text1 = int(input("欠損文字はいくつあるでしょうか？："))
    for k in range(kesson):
            text2 = input(f"{kesson+k}つ目の文字を入力してください")

    if text1 == kesson:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        print(text2)
    
    
    

    
if __name__ == "__main__":
    main()
