from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def aff_life():
    """
    Loads life expectancy data from a CSV file and displays a line plot
    showing the life expectancy projections for Turkey from 1800 to 2100.
    """
    try:
        df = load("life_expectancy_years.csv")
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or not loaded correctly")

        df.set_index("country", inplace=True)
        country = "Turkey"
        if country not in df.index:
            raise ValueError(f"{country} not found in dataset.")

        years = np.array(df.columns, dtype=int)
        values = np.array(df.loc[country], dtype=float)

        plt.plot(years, values, label=country)
        plt.title("Turkey Life Expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life Expectancy")
        plt.yticks(range(30, 91, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    aff_life()
