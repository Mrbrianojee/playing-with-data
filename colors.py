import pandas as pd

color_table =  pd.io.parsers.read_table("Colors.txt")
print(color_table)