#random とbrython使用のためのimport#
import random
from browser import document

#抽選の条件#
num = 1
atari = int(100)
while True :
    random_num = random.randint(1,8192) 
    if  atari == random_num : 
        break
    else :
        num += 1

#結果を返す関数#
def god_kekka(ev):

    kekka = str(num)
    
    rslt = document["result"]
    rslt.text = kekka

#ブラウザ側のbuttonのclickで関数を呼び出し
sub_elt = document["submit_button"]
sub_elt.bind("click", god_kekka)
