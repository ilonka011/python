import pandas as pd

column = ['Elona', 'Batman', 'Spongebob']
titled_column = { 'name': column,
                'height': [1.68, 1.8, 0.25],
                'weight': [62, 93, 2] }
data = pd.DataFrame(titled_column)
print(data)
