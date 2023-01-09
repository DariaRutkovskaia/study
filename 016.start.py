# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('LightSalmon3')
# timmy.forward(100)
# my_screen =  Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Charmander','Squirtle'])
table.add_column('Type', ['Electric', 'Fire','Water'])
# ("Pansage" "Grass")
table.align = "l"
print(table)
