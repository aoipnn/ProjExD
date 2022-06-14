import random

quiz = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]

kaitou1=["マスオ","ワカメ","甥"]
kaitou2=["ますお", "わかめ", "おい"]



def kaitou():
    global a
    q1 = ["マスオ", "ますお"]
    q2 = ["ワカメ", "わかめ"]
    q3 = ["甥", "おい", "甥っ子", "おいっこ"]
    q_list = [q1, q2, q3]
    text = input("答えるんだ：")
    for i in range(input(q_list)):
        if text == q_list[a]:
            print("正解！！！")
        else:
            print("出直してこい")
        return text
print("問題：")

