from classes import Charizard, Blastoise 

shiny_charizard = Charizard("Shiny Charizard")

shiny_blastoise = Blastoise("Shiny Blastoise")

print(" ")
print(shiny_charizard)
print(shiny_blastoise)
print(" ")

x = 1

while (x < 6):

    print(f"{shiny_charizard.str_name} atk! Dragon Breath ==> {shiny_charizard.launch_atk()}")
    print(f"{shiny_blastoise.str_name} atk! Water Cannon ==> {shiny_blastoise.launch_atk()}\n")
    x += 1





