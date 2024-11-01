import pandas as pd

df_hokej = pd.read_csv('rezultati_hokej.csv')
print(df_hokej.columns)

df_smal = df_hokej[df_hokej['dolzine kazni'].astype(str).str.contains(r'\b(5 min|20 min|0 min)\b', regex=True)]
print(df_smal)
print(len(df_smal))
