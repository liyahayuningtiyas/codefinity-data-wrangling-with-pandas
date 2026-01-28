import pandas as pd

data = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic_2',
    index_col=0
)

# 1. Replace missing values in 'Age' with the mean of that column
data['Age'].fillna(value=data['Age'].mean(), inplace=True)

# 2. Count how many NaNs remain in 'Age'
NaN = data['Age'].isna().sum()

print(NaN)