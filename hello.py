import pandas as pd

path_to_csv = "./csv/survey_results_public.csv"


for i, chunk in enumerate(pd.read_csv(path_to_csv, chunksize=40000)):
    chunk.to_csv(f"./csv_chunks/chunk{i}.csv", index=False)
