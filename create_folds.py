import os
import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":
    file_path = "/Users/insomni_.ak/Documents/Machine Learning/Melanoma Detection"
    df = pd.read_csv(os.path.join(file_path, "train.csv"))
    
