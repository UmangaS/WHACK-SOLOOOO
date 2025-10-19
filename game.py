import random

class Player:
    def __init__(self):
        self.health = 20
        self.attack = 5
        self.defense = 3
        self.weapon = random.choice(["Glass Window", "Mac n' Cheese", "Rocky Rock"])


    def displayMsg(self, msg):
        return msg

    def setHealth(self, health):
        self.health -= (1 - self.defense) / 10 * health
        if self.health <= 0:
            self.displayMsg("Game Over. You have died.")
            return

    def getHealth(self):
        return self.health
    
    def setAttack(self, increase):
        self.atack += increase

    def getAttack(self):
        return self.attack
    
    def setDefense(self, increase):
        self.defense += increase

    def getDefense(self):
        return self.defense

class Game:
    def __init__(self):
        self.level = 1
        self.enemyHealth = self.level * 20
        self.player = ""
        self.enemies = [["Troll", 3 * self.level, 2 * self.level], ["Ogre", 5, 2], ["Goblin", 1, 3]]
        self.moves = ["Attack", "Block", "Recover"]
        self.setPlayer()
        self.turns = 0
        

    def setPlayer(self):
        print("Start your adventure.")
        self.player = Player()
        print(f"You have been assigned the deadley weapon - {self.player.weapon}")
        self.playTurn()


    def chooseBuff(self):
        print("Due to your performance, you get to choose a buff!")
        while True:
            choice = str(input("Please choose: \n1) Attack \n2) Defense")).title()
            if choice in ["1", "2", "Attack", "Defense"]:
                break
            print("Please choose either 1, 2, 'Attack', or 'Defense'. ")

        amount = random.randrange(10) / 10
        if choice in ["Attack", "1"]:
            print(f"Your attack has been increased by {amount}. ")
            self.player.setAttack(amount)
        else:
            print(f"Your defense has been increased by {amount}. ")
            self.player.setDefense(amount)

        



    def buff(self):
        print("You will recieve a random buff")
        buff = random.choice(["attack", "defense"])
        amount = random.randrange(10) / 10

        print(f"You have received a buff to your {buff} by an amount of {amount}.")
        if buff == "attack":
            self.player.setAttack(amount)
        else:
            self.player.setDefense(amount)



    def playTurn(self):
        if self.level % 5 == 0:
            self.buff()

        # continue game 
        enemy = random.choice(self.enemies)
        print(f"You have encountered a {enemy[0]}. It has {enemy[1]} health and {enemy[2]} attack. ")
        while enemy[1] >= 1:
            move = str(input("What is your move? \n1) Attack \n2)Block \n3)Recover")).title()
            if not (move in self.moves or move in ["1", "2", "3"]):
                print("Please say either 'Attack', 'Block', or 'Recover'. Alternatively say the corresponding integers. ")

            else:
                enemyMove = random.choice(self.moves)

                success = 0
                loss = 0
                
                
                
                # what beats what
                # player attacks
                if (move == "Attack" or move == "1"):
                    if enemyMove == "Attack":
                        print("You both attacked each other. ")
                        damageOut = self.player.getAttack()
                        damageIn = enemy[2] 
                        print(f"You inflicted a raw damage of {damageOut}. \nYou received a raw damage of {damageIn}.")
                        self.player.setHealth(damageIn * -1) 
                        enemy[1] -= damageOut

                    elif enemyMove == "Defense":
                        print(f"The {enemy[0]} blocked your attack!")
                        damageIn = abs(self.player.getAttack() - enemy[1])
                        print(f"You received raw damage of {damageIn}.")
                        self.player.setHealth(damageIn * -1)
                        loss += 1

                    else:
                        print(f"You caught the {enemy[0]} off guard with your huge {self.player.weapon}!")
                        damageOut = self.player.getAttack()
                        print(f"You inflicted a raw damage of {damageOut}. ")
                        enemy[1] -= damageOut
                        success += 1


                # player blocks
                elif (move == "Block" or move == "2"):
                    if enemyMove == "Attack":
                        print(f"The {enemy[0]} attacked you, but you blocked! ")
                        damageOut = abs(self.player.getDefense() - enemy[2])
                        print(f"You inflicted a raw damage of {damageOut}.")
                        enemy[1] -= damageOut
                        success += 1

                    elif enemyMove == "Defense":
                        print(f"The {enemy[0]} blocked, and so did you. \nNothing happens.")

                    else:
                        print(f"You prepared the block, but the {enemy[0]} was just recovering!")
                        healthOut = enemy[2] // enemy[1]
                        print(f"The {enemy[0]} recovered {healthOut} health. ")
                        enemy[2] += healthOut
                        loss += 1
                    

                # player recovers
                else:
                    if enemyMove == "Attack":
                        print(f"You were caught off guard! {enemy[0]} attacked you whilst you were recovering! ")
                        damageIn = enemy[2] 
                        print(f"You received a raw damage of {damageIn}.")
                        self.player.setHealth(damageIn * -1) 
                        loss += 1

                    elif enemyMove == "Defense":
                        print(f"The {enemy[0]} blocked, but you were just recovering! ")
                        healthIn = self.player.getAttack() // self.player.getHealth()
                        print(f"You received {healthIn} health.")
                        self.player.getHealth(healthIn)
                        success += 1

                    else:
                        print(f"You and the {enemy[0]} both recovered health!")
                        healthIn = self.player.getAttack() // self.player.getHealth()
                        healthOut = enemy[2] // enemy[1]
                        print(f"You healed by {healthIn}. \nThe {enemy[0]} healed by {healthOut}.")
                        self.player.getHealth(healthIn)
                        enemy[1] += healthOut


                print(f"Your stats: \nHealth: {self.player.getHealth} \nAttack: {self.player.getAttack()} \nDefense: {self.player.getDefense()}")
                print(f"Enemy stats: \aHealth: {enemy[1]} \nAttack: {enemy[2]}")

                

        if success > loss:
            self.chooseBuff()

        print(f"You have beat level {self.level}. Proceeding to next level. ")
        self.level += 1


if __name__ == "__main__":
    Game()