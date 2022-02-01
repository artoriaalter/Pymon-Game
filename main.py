from class_library import *

print("""Welcome to ArtoriaAlter's very first program, Pymon catching game! In this game, you should try to catch as much
Pymons as possible. Of course, it isn't any different than gambling as everything depends on the random numbers! I wrote this game to implement my knowledge about Object-Oriented-Programming.
""")


name = input("Tell me your name.\n")

print("Okay {name}, let's start!\n".format(name=name))

game = Game(Player(name))

game.game_start()
