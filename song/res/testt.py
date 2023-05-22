_x = """Shape Of You
 https://youtu.be/JGwWNGJdvx8
 Lovely
 https://youtu.be/V1Pl8CzNzCw
 Middle Of The Night
 https://youtu.be/oSHzUD-uqKY
 Unstoppable
 https://youtu.be/YaEG2aWJnZ8
 Runaway
 https://youtu.be/d_HlPboLRL8
 Please Don't Go
 https://youtu.be/S2oxFIsENgM
 Snap 
 https://youtu.be/Lo4_K4relMg
 Let Me Down Slowly
 https://youtu.be/s-bZD3O3P80
 Sugar & Brownies
 https://youtu.be/KuPg14K-e6s
 Senorita
 https://youtu.be/Pkh8UtuejGw"""

splited = _x.split("\n")

songName = splited[: :2]
linkName = splited[1: :2]
# print(songName)
# print(linkName)

import random

def produce(i_value):
    _val = songName[random.randint(0, (len(songName))-1)]
    if _val == i_value:
        produce(i_value)
    else:
        return _val

tmpRepeat=0
for i in songName:
    print(f"""b++;
window["q"+b] = "{i}"; //Ans{tmpRepeat+1}
window["q1"+b] = "{produce(i)}";
window["q2"+b] = "{produce(i)}";
window["q3"+b] = "{produce(i)}";
window["q4"+b] = "{produce(i)}";
window["li"+b] = '{linkName[tmpRepeat]}';
""")
    tmpRepeat+=1