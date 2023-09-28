import random

class Organism:

    def __init__(self, str_name):

        self.str_name = str_name 

        self.int_lvl = random.randint(1,50)
        self.int_hp = 100
        self.atk_pwr = 1
        self.def_pwr = 1 
        self.spc_pwr = 1
    
    def __str__(self):
        return (f"Go {self.str_name}! {self.str_name} is level {self.int_lvl} and has a HP of {self.int_hp} XD")
    
    def launch_atk(self):
        self.atk_pwr = random.randint(1,30)
        return self.atk_pwr 
    
    def launch_def(self):
        self.def_pwr = random.randint(1, 30)
        return self.def_pwr 
    

class Charizard(Organism):

    def spc_atk(self):
        self.spc_pwr = 100

class Blastoise(Organism):

    def spc_atk(self):
        self.spc_pwr = 85


    


