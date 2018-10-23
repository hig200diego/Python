#QUEM LAVA A PANELA GAME

import random

print("#"*25)
print('QUEM LAVA A PANELA GAME')
print("#"*25)
print()

def quemLava(resultado):
    while True:
        if resultado == 1:
            return 'FLÁVIO SE FERROU!'
        elif resultado == 2:
            return 'DIEGO SE FERROU!'
            break
        else:
            return 'Continue sorteando. Boa sorte!'

print(quemLava(random.randint(1, 15)))
    
    
    

        
   
