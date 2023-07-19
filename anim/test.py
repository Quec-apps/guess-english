_x = """Toy Story
 Spider Man
 Inside Out
 Coco
 Aladdin
 Paddington
 The Incredibles
 Zootopia
 Up
 Pinocchio
 Finding Dory
 The LEGO Movie
 Moana
 Isle of Dogs
 Kubo and the Two Strings
 How To Train Your Dragon
 Shaun the Sheep Movie
 WALL E
 Dumbo
 Ratatouille
 My Life as a Zucchini
 Only Yesterday 
 The Lego Batman  
 101 Dalmatians
 Beauty and the Beast
 Chicken Run
 The Nightmare Before Christmas
 Monsters Inc
 Fantasia
 Grave of the Fireflies
 Your Name
 The Iron Giant
 Spirited Away
 Tower
 Song of the Sea
 The Lion King
 Who Framed Roger Rabbit
 Waltz with Bashir
 Anomalisa
 Yellow Submarine
 Wallace and Gromit
 Fantastic Mr Fox
 Ernest and Celestine
 Snow White and the Seven Dwarfs
 The Secret World of Arrietty
 Ralph Breaks the Internet
 Frozen
 The Red Turtle
 Long Way North
 I Lost My Body
 The Breadwinner
 Ghost in the Shell
 The Little Mermaid
 Lady and the Tramp
 The Triplets of Belleville
 Big Hero 6
 Bambi
 Princess Mononoke
 My Neighbor Totoro
 Arthur Christmas
 Antz
 A Bugs Life
 Mary and Max
 Ponyo
 Klaus
 Teen Titans Go
 Bolt
 Missing Link
 Tangled
 ParaNorman
 Frankenweenie
 James and the Giant Peach
 Shrek
 Rango
 The Wind Rises
 Winnie the Pooh
 The Simpsons Movie
 Boy and the World
 The Peanuts Movie
 When Marnie Was There
 Millennium Actress
 Kung Fu Panda
 Sleeping Beauty
 Wreck It Ralph
 The Illusionist
 Tarzan
 Howls Moving Castle
 REDLINE 
 THE THIEF AND THE COBBLER 
 MONSTER HOUSE 
 ANASTASIA 
 TEKKONKINKREET
 WIZARDS 
 THE PEANUTS MOVIE
 THE LAST UNICORN
 THE CASTLE OF CAGLIOSTRO
 HAPPY FEET  
 THE PRINCESS AND THE FROG 
 angry birds
 ice age"""

splited = _x.split("\n")

ct = ''
for i in splited:
    ct+=f"""a++;window['q'+a] = "{i.strip()}";\n"""

f = open('HollyWood Anim Output.txt', 'a')
f.write(ct)
f.close()