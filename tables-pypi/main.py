
from prettytable import PrettyTable, FRAME

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"],"l")

print(table)

