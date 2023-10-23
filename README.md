# Mobile Phone Price Prediction

This Python project involves predicting mobile phone prices based on features like brand, storage, and RAM. The dataset used for this project is 'Mobile phone price.csv'.

## What I'm Learning

- Data preprocessing and cleaning using Pandas.
- Feature encoding using OneHotEncoder and ColumnTransformer.
- Understanding and handling categorical variables in machine learning.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries using the following command:
   pip install pandas scikit-learn
3. Place the 'Mobile phone price.csv' file in the same directory as your Python script.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the Python file (main.py).
6. Run the program using a Python interpreter
7. The program will execute, preprocess the data, and perform mobile phone price prediction.

## Example Output
Transformed X
   0    1    2    3    4    5    6    7    8
0  1.0  0.0  0.0  0.0  1.0  0.0  2.0  2.0  2.0
1  1.0  0.0  0.0  0.0  1.0  0.0  2.0  2.0  2.0
2  1.0  0.0  0.0  0.0  1.0  0.0  2.0  2.0  2.0
3  1.0  0.0  0.0  0.0  1.0  0.0  2.0  2.0  2.0
4  1.0  0.0  0.0  0.0  1.0  0.0  2.0  2.0  2.0
Transformed New
   Price ($)  Brand_Apple  Brand_Samsung  Storage_32  Storage_64  RAM_4  RAM_8
0        999            1             0          0          1      0      1
1       1100            1             0          0          1      0      1
2        750            1             0          1          0      1      0
3        800            1             0          1          0      1      0
4        950            1             0          1          0      1      0

## Acknowledgments:
This program was created as part of the DS, AI and Machine Learning course offered by the National Emerging Skills Program (NESP).
