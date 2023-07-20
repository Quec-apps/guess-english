_x = """Totoro 
 Woody
 Buzz Lightyear
 Thumper
 Olaf
 Genie
 Donkey
 Remy 
 Dug
 Simba
 Po 
 Dory
 Minions
 Toothless
 Hercules
 Mowgli
 Moana
 Carl Fredricksen
 Mike Wazowski
 Elsa
 Winnie-the-Pooh
 Helen Parr
 Heihei
 Maui
 Gramma Tala
 Gazelle
 Flash
 Judy Hopps
 Clawhauser
 Bellwether
 Zootopia
 Otters
 Hiro
 Baymax
 Jack-Jack
 Atta
 Sulley
 Bolt
 Tianna
 Naveen"""

splited = _x.split("\n")

import random

def produce(i_value):
    _val = splited[random.randint(0, (len(splited))-1)]
    if _val == i_value:
        return produce(i_value)
    else:
        return _val.strip()

cout=1
output_ = ""
for i in splited:
    output_+=f"""a++;
window["ans"+a] = "{i.strip()}"; //Ans{cout}
window["noans1"+a] = "{produce(i)}";
window["noans2"+a] = "{produce(i)}";
window["noans3"+a] = "{produce(i)}";
window["noans4"+a] = "{produce(i)}";

"""
    cout+=1

f = open('charOutput.txt', 'a')
f.write(output_)
f.close()