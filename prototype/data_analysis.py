```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class DataAnalysis:
    def __init__(self, data_set):
        self.data_set = data_set

    def load_data(self):
        try:
            data = pd.read_csv(self.data_set)
            return data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def preprocess_data(self, data):
        # Remove null values
        data = data.dropna()

        # Standardize the data
        scaler = StandardScaler()
        data = scaler.fit_transform(data)

        return data

    def analyzeData(self, data):
        # Apply PCA for dimensionality reduction
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(data)

        return principalComponents

if __name__ == "__main__":
    data_analysis = DataAnalysis("data_set.csv")
    data = data_analysis.load_data()
    if data is not None:
        data = data_analysis.preprocess_data(data)
        result = data_analysis.analyzeData(data)
        print(result)
```