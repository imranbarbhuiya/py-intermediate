from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Name", "Age"])
table.align = "c"

print(table)
