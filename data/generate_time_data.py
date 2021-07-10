import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from aesjosephus.time import time_df

def main(n: int):
    FILE_NAME = "time_data"

    df = time_df(n)
    df.to_csv(os.path.join(os.path.dirname(__file__), f'{FILE_NAME}.csv'), index=False)

if __name__ == "__main__":
    main(100)