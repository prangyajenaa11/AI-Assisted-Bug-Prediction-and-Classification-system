import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    metrics_df = pd.read_csv("data/code_metrics.csv")
    bug_df = pd.read_csv("data/bug_reports.csv")

    # Handle missing values
    metrics_df.fillna(0, inplace=True)
    bug_df.fillna("Unknown", inplace=True)

    # Encode categorical variables
    le = LabelEncoder()
    bug_df["bug_type"] = le.fit_transform(bug_df["bug_type"])
    bug_df["severity"] = le.fit_transform(bug_df["severity"])

    # Merge dataframes
    merged_df = pd.merge(metrics_df, bug_df, on="file_path")

    # Split into features and target variable
    X = merged_df.drop("bug_type", axis=1)
    y = merged_df["bug_type"]

    return X, y

if __name__ == "__main__":
    X, y = preprocess_data()