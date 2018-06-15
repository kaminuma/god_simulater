import random
from browser import document


num = 1
atari = int(100)
    while True :
        random_num = random.randint(1,8192) 
        if  atari == random_num :
            break
        else :
            num += 1

def god_kekka(ev):

    kekka = str(num)
    
    rslt = document["result"]
    rslt.text = kekka


sub_elt = document["submit_button"]
sub_elt.bind("click", god_kekka)
