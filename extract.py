import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df = pd.read_csv(url)
print(df.head())
print("nettoyage")