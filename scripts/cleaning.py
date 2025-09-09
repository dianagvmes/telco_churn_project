import pandas as pd

def load_file(path):
    """Loads an Excel file into df"""
    df = pd.read_excel(path)
    return df

def check_data(df, name=""):
    """Prints shape and head of df"""
    print(f"--- {name} ---")
    print("Shape:", df.shape)
    print(df.head())
    print("\n")

def clean_column_names(df):
    """Makes column names lowercase and replaces spaces with underscores."""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

def merge_two(df1, df2, on_column):
    """Merges 2 dfs on a common column (left join)."""
    merged = pd.merge(df1, df2, on=on_column, how="left")
    return merged

def fill_missing(df):
    """Fills missing values: numbers with 0, objects with 'Unknown'."""
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(0)
    return df

def save_csv(df, path):
    """Saves DataFrame to a CSV file."""
    df.to_csv(path, index=False)
    print(f"Saved to {path}")
