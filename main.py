import pandas as pd

# Load the dataset
phones_csv = pd.read_csv('Mobile phone price.csv')

# Preprocess the 'Price ($)' column
phones_csv['Price ($)'] = phones_csv['Price ($)'].str.replace('$', '')
phones_csv['Price ($)'] = phones_csv['Price ($)'].str.replace(',', '').astype(int)

# Preprocess the 'RAM ' column
phones_csv['RAM '] = phones_csv['RAM '].str.replace('GB', '').astype(int)

# Preprocess the 'Storage ' column
phones_csv['Storage '] = phones_csv['Storage '].str.replace('GB', '').astype(int)

# Separate features (X) and target (Y)
X = phones_csv.drop('Price ($)', axis=1)
Y = phones_csv['Price ($)']

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Define categorical features for encoding
features_cat = ["Brand", "Storage ", "RAM "]

# Initialize OneHotEncoder and ColumnTransformer
hottie = OneHotEncoder()
transformer = ColumnTransformer([('One_hottie', hottie, features_cat)],
                                remainder='passthrough')

# Apply transformation on a sample of X
transformed_X = transformer.fit_transform(X.head())
print(f'transformed X :')
print(pd.DataFrame(transformed_X))

# Alternatively, use get_dummies for one-hot encoding
transformed_new = pd.get_dummies(phones_csv[['Brand', "Storage ", "RAM ", "Price ($)"]])
print('transformed new : ')
print(pd.DataFrame(transformed_new))
