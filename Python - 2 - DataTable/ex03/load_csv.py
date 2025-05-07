import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the specified path and return it as a pandas
    DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame or None: The loaded dataset as a pandas DataFrame, or
    None if there was an error.

    This function loads a CSV dataset from the given path using the
    pandas library.
    It prints the dimensions of the loaded dataset and returns the
    dataset as a DataFrame.

    Normally you can see dimensions end of the DataFrame,
    we added extra to the top.

    If there is an error (e.g., bad path, bad format), None is returned.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimension {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    load()
