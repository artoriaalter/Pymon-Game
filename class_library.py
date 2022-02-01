import random
class Game:
    def __init__(self, player):
        self.player = player

    def game_start(self):
        while True:
            print("What do you want to do?")
            print("""
            1. Catch a Pymon
            2. View your status
            3. Quit the gam
            """)
            choice = int(input())

            if choice == 1:
                self.player.catch_pymon()

                if self.check_balls() == False:
                    break

            elif choice == 2:
                print(self.player)

            elif choice == 3:
                print("See you soon!")
                break
            else:
                print("Invalid input!")

    def check_balls(self):
        if self.player.pyballs == 0:
            print("Game Over! You've used all of your balls.")
            print("In this gameplay, you were able to catch {total} Pymons in total.".format(total = sum(self.player.pymons.values())))
            return False
        else:
            pass


class Player:
    def __init__(self, name):
        self.name = name
        self.pymons = {}
        self.pyballs = 20
        self.level = 1

    def __repr__(self):
        player_description = """
        {name} is a {level} level Pymon tamer, and owns {pyball} pyballs.
        Current Pymons are given below:
        """.format(name=self.name, level = self.level, pyball = self.pyballs)

        for pymon, number in self.pymons.items():
            player_description += "\n{pymon}: {number}\n".format(pymon=pymon, number = number)

        return player_description

    def catch_pymon(self):
        possibility_randomizer = random.randint(1,5)
        level_randomizer = random.randint(1, self.level + 2)
        possible_pymons = ["Gitmon","Atommon","Codecademymon","Bugmon"]
        pymon = Pymon(random.choice(possible_pymons), level_randomizer)
        print("{name} threw his ball to catch a {pymon}...".format(name = self.name, pymon = pymon ))
        print(pymon)
        if possibility_randomizer <= 2:
            print("You trapped a {type} inside your pyball.".format(type = pymon.type))


            if  pymon.level <= self.level:
                print("You caught a {type}!".format(type = pymon.type))
                if pymon.type in self.pymons:
                    self.pymons[pymon.type] += 1
                else:
                    self.pymons[pymon.type] = 1
                self.level += 1
            else:
                print("{type} was able to break out of your ball and escape! You better get stronger!".format(type = pymon.type))
                self.pyballs -= 1
                self.level += 1

        else:
            print("{type} dodged the ball and escaped! Good luck next time!".format(type = pymon.type))
            self.pyballs -= 1
        print("You have {pyball} pyballs left".format(pyball = self.pyballs))


class Pymon:
    def __init__(self, type, level):
        self.type = type
        self.level = level


    def __repr__(self):
        return "This Pymon is a {level} level {type}".format(level = self.level, type = self.type)
