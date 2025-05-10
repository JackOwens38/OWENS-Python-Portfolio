import pandas as pd
import os

# Ensure you are using the correct relative path
file_path = os.path.join(os.path.dirname(__file__), 'data', 'EoC_Final.csv')
df = pd.read_csv(file_path)