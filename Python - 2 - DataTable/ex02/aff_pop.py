from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def convert_to_float(x):
    """
    Converts string values with 'M' (million) or 'B' (billion)
    suffixes to float numbers.

    Args:
        x: The input value to convert, can be string or numeric.

    Returns:
        float: Converted value. Returns NaN if conversion fails.

    Examples:
        >>> convert_to_float('5M')
        5000000.0
        >>> convert_to_float('2.5B')
        2500000000.0
    """
    try:
        x = str(x).strip()
        if x.endswith('M'):
            return float(x[:-1]) * 1_000_000
        elif x.endswith('B'):
            return float(x[:-1]) * 1_000_000_000
        return float(x)
    except Exception:
        return float('nan')


def aff_life():
    """
    Visualizes population data for Turkey and France from 1800 to 2040.

    Loads population data from 'population_total.csv', processes it,
    and creates a line plot showing population trends for both countries.
    The y-axis is formatted to display values in millions (M) or billions (B).

    Raises:
        ValueError: If the DataFrame is empty or if a specified country
        is not found.

    Returns:
        None: Displays the matplotlib plot.
    """
    try:
        df = load("population_total.csv")
        if df is None:
            raise ValueError("DataFrame is empty")
        df.set_index("country", inplace=True)

        countries = ["Turkey", "France"]
        start_year = 1800
        end_year = 2040

        all_years = [int(col) for col in df.columns if col.isdigit()]
        selected_years = [year for year in all_years
                          if start_year <= year <= end_year]
        str_years = list(map(str, selected_years))

        for country in countries:
            if country not in df.index:
                raise ValueError(f"{country} not found in dataset.")

            years = sorted(map(int, str_years))
            raw_values = df.loc[country, map(str, years)]
            values = np.array([convert_to_float(val) for val in raw_values])

            plt.plot(years, values, label=country)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(selected_years[::40])
        plt.ylabel("Population")
        plt.yticks(
            range(20_000_000, 81_000_000, 20_000_000),
            [f"{int(y/1e6)}M" for y in range(20_000_000,
                                             81_000_000, 20_000_000)]
        )
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    aff_life()
