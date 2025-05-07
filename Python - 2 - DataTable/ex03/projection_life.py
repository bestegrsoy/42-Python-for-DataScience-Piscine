import matplotlib.pyplot as plt
from load_csv import load


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
    except Exception as e:
        print(f"Error converting {x}: {e}")
        return None


def life_expectancy_vs_gnp():
    """
    Visualizes the relationship between GDP and life
    expectancy for the year 1900.

    This function loads data from two CSV files:
    - 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    for GDP data
    - 'life_expectancy_years.csv' for life expectancy data

    It creates a scatter plot showing the correlation between
    gross domestic product
    and life expectancy across countries for the year 1900.

    Raises:
        ValueError: If the DataFrames are empty or if data for
        the year 1900 is not available.

    Returns:
        None: Displays the matplotlib scatter plot.
    """
    try:
        df_income = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life_expectancy = load("life_expectancy_years.csv")

        if df_income is None or df_life_expectancy is None:
            raise ValueError("DataFrames are empty or not loaded properly")

        year = 1900
        if (str(year) not in df_income.columns or
                str(year) not in df_life_expectancy.columns):
            raise ValueError(f"Year {year} data not available")

        # Ülkelerin kesişimlerini al
        countries = df_income.index.intersection(df_life_expectancy.index)

        # 1900 yılına ait verileri al
        gnp_1900 = df_income.loc[countries, str(year)].apply(convert_to_float)
        life_expectancy_1900 = (df_life_expectancy.loc[countries, str(year)]
                                .apply(convert_to_float))

        # Grafik oluştur
        plt.scatter(gnp_1900, life_expectancy_1900, label=f"Year {year}",
                    color='blue')

        plt.title(f"{year}")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xticks(
            [300, 1000, 10000],
            [f"{x}" if x < 1000 else f"{int(x/1000)}k"
             for x in [300, 1000, 10000]]
        )

        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    life_expectancy_vs_gnp()
