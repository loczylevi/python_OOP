
import random

class Jatek:
    def __init__(self, hp, damage, kill_counter=0):
        self.hp = hp
        self.damage = damage
        self.kill_counter = kill_counter
        
    def harc(self, enemy):
        enemy.hp -= self.damage
        return self.damage
    
    
warrior1 = Jatek(100,40)

goblin = Jatek(150,20)

while warrior1.hp > 0 and goblin.hp > 0:
    print(f"Warrior stat:\nHitPoint: {warrior1.hp}\nDamage: {warrior1.damage}")
    print(f"\nGoblin stat:\nHitPoint: {goblin.hp}\nDamage: {goblin.damage}")
    print("____________________________________\n")
    print("Te támadod a goblint")
    sebzes = warrior1.harc(goblin)
    print(f"Goblin {sebzes} sebzést kapott")
    print(f"Goblin hpja: {goblin.hp}")
    
    if goblin.hp <= 0:
        print("\n------Goblin meghalt!------\n")
        warrior1.kill_counter += 1
        break
    
    print("\nGoblin vissza támad")
    sebzes = goblin.harc(warrior1)
    print(f"Goblin {sebzes} sebzést okozott neked")
    print(f"Te hp-d: {warrior1.hp}")
    print("____________________________________\n")
    
    if warrior1.hp <= 0:
        print("\n------Meghaltál! ._.  ------\n")
        goblin.kill_counter += 1
        break
   

    
print(f"Warrior stat:\nHitPoint: {warrior1.hp}\nDamage: {warrior1.damage}\nkillek: {warrior1.kill_counter}")
print(f"\nGoblin stat:\nHitPoint: {goblin.hp}\nDamage: {goblin.damage}\nkillek: {goblin.kill_counter}")

    
    
    




        
