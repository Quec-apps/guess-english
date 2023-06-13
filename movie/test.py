_x = """The Godfather
 The Silence of the Lambs
 The Empire Strikes Back
 The Shawshank Redemption
 The Shining
 Casablanca
 One Flew Over the Cuckoo's Nest
 The Dark Knight
 Aliens
 Schindler's List
 Inception
 Alien
 Some Like It Hot
 Blade Runner
 Se7en
 Apocalypse Now
 Angry Men
 The Lord of the Rings
 Terminator
 Die Hard
 Gone with the Wind
 Taxi Driver
 Pulp Fiction
 The Bridge on the River Kwai
 North by Northwest
 Rear Window
 Léon
 Back to the Future
 Citizen Kane
 Goodfellas
 Memento
 American Beauty
 As Good as It Gets
 Forrest Gump 
 Singin' in the Rain
 Braveheart
 Saving Private Ryan
 Rain Man
 The King's Speech
 2001: A Space Odyssey
 Kill Bill
 Avanti
 The Good, the Bad and the Ugly
 Amélie
 Modern Times
 Lost in Translation
 Full Metal Jacket
 Requiem for a Dream
 Fight Club 
 No Country for Old Men
 Django Unchained
 Children of Men
 The Lives of Others
 The Prestige
 V for Vendetta
 Chinatown
 City of God
 To Have and Have Not
 Fargo
 Life of Pi 
 Vertigo
 Slumdog Millionaire
 Trainspotting
 Interstellar
 The Thing
 The Third Man
 12 Monkeys 
 Life Is Beautiful
 The Pianist
 Magnolia
 The Dark Knight Rises
 The Hobbit
 Mad Max
 12 Years a Slave
 Indiana Jones
 O Brother, Where Art Thou
 Inglourious Basterds
 The Departed
 A Beautiful Mind
 District 9
 The Piano
 Mystic River
 The Insider 
 L.A. Confidential
 Heat
 The Usual Suspects
 Cool Hand Luke
 Eternal Sunshine of the Spotless Mind
 City Lights
 The Matrix
 Sin City
 Misery
 What's Eating Gilbert Grape
 Monty Python and the Holy Grail
 The Deer Hunter
 Scarface
 A Clockwork Orange
 The Elephant Man
 Papillon
 Lawrence of Arabia
 East of Eden
 Hotel Rwanda
 Dances with Wolves
 Batman Begins 
 Skyfall
 The Treasure of the Sierra Madre
 The Untouchables
 The Truman Show
 The Apartment
 The Big Sleep
 Amour
 The Grump
 Thelma & Louise
 Downfall
 Rocky
 Gran Torino
 Strangers on a Train
 Who's Afraid of Virginia Woolf
 The Exorcist
 The Terminator
 The Hobbit: An Unexpected Journey
 Kill Bill 
 Gladiator
 Traffic
 Zodiac
 The Green Mile
 Halloween
 Casino
 Jaws
 Once Upon a Time in the West
 Notorious
 The Great Escape
 Goldfinger
 Death Proof
 Argo
 Milk
 Being John Malkovich
 Black Swan
 The Others
 Brokeback Mountain
 Jackie Brown
 Casino Royale
 Platoon
 The Thin Red Line
 The Hunger Games: Catching Fire
 American History X
 Dead Poets Society
 The Visitor
 Talk to Her
 The Girl with the Dragon Tattoo
"""

splited = _x.split("\n")

ct = ''
for i in splited:
    ct+=f"""a++;window['q'+a] = "{i.strip()}";\n"""

f = open('HollyWood Movie Output.txt', 'a')
f.write(ct)
f.close()