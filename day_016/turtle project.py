from prettytable import PrettyTable
table = PrettyTable()


table.add_column("column_header1",["row1","row2","row3"])
table.add_column("column_header2",["row11","row12","row13"])
print(table)