import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

def main(): 
    listings_df = pd.read_csv('listings.csv')
    listings_df = listings_df.drop(["Total lot size"], axis=1)
    

if __name__ == "__main__":
    main()