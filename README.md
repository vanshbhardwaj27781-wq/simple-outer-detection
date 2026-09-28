# Simple Outlier Detection

## Objective
Identify unusually high or low values using the IQR method.

## Tools
- Python
- Pandas

## Dataset
I used a small Retail Sales dataset with these columns:
- Date
- Category
- Product
- Quantity
- Sales

## What I did
1. Loaded the dataset using Pandas.
2. Selected the `Sales` column.
3. Calculated Q1 and Q3.
4. Calculated IQR = Q3 - Q1.
5. Calculated the lower and upper bounds using:
   - Lower Bound = Q1 - 1.5 × IQR
   - Upper Bound = Q3 + 1.5 × IQR
6. Flagged values outside these limits as outliers.
7. Saved the result in `outlier_table.csv`.

## Result
Q1 = 2425.00  
Q3 = 7375.00  
IQR = 4950.00  
Lower Bound = -5000.00  
Upper Bound = 14800.00  

Total outliers found: **7**

## Important point
Outliers should not be removed automatically. I would first check whether the value is a real transaction or a data-entry error.

## How to run
Open this folder in VS Code and run:

```bash
python -m pip install pandas
python outlier_detection.py
```

The script creates/updates `outlier_table.csv`.

## Interview Questions
**What is an outlier?**  
An outlier is a value that is unusually high or low compared with most other values.

**Should every outlier be removed?**  
No. It should be investigated first because it may be a valid observation.
