# Code 17: Pandas Basics - Series and DataFrame
# Pandas is an open-source library for data manipulation and analysis.
# Install: pip install pandas numpy

import numpy as np
import pandas as pd

# Series - a 1D labeled array
data = ["Siddant", "Tessica", "Ritesh", "Srivardhan"]
mydata = pd.Series(data, index=["a", "b", "c", "d"])
print(mydata)

# DataFrame - a 2D labeled data structure (like a spreadsheet)
data = {
    "Name": ["A", "B", "C"],
    "Age": [22, 23, 24],
    "Education": ["BBA", "MS", "Btech"]
}

df = pd.DataFrame(data)
print(df)
