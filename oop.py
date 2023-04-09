class Player:
    # Constractor
    def __init__(self, name, health=100, energy=100):
        self.health = health
        self.energy = energy
        self.name = name

    def attack(self, target,  damage=1):
        print(f"{self.name} attacked {target.name} with {damage} damage")
        target.health -= damage
        self.energy -= damage
        if target.is_attacked(self.name):
            self.health -= target.damage

    def showInfo(self):
        print(f"{self.name}'s health : {self.health}, energy : {self.energy}")


class Monster:
    def __init__(self, name, health=500):
        self.health = health
        self.health_init = health
        self.damage = 10
        self.name = name

    def is_attacked(self, player_name):
        print(f"{self.name} attacked {player_name} with {self.damage} damage")
        return self.health < self.health_init

    def showInfo(self):
        print(f"{self.name}'s health : {self.health}")


player = Player(name="Balmond")
player2 = Player(name="Layla")
dragon = Monster(name="Dragon")

player.attack(target=dragon, damage=30)
player2.attack(target=dragon, damage=50)
player.showInfo()
player2.showInfo()
dragon.showInfo()
