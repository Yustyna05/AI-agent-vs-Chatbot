import pandas as pd


def load_data():
    stock = pd.read_csv("data/Stock.csv", sep=";")
    sales = pd.read_csv("data/Sales.csv", sep=";")
    cogs = pd.read_csv("data/COGS.csv", sep=";")

    # Convert numeric columns from string to float
    stock["Stock"] = (
        stock["Stock"]
        .astype(str)
        .str.replace(" ", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    sales["Sales"] = (
        sales["Sales"]
        .astype(str)
        .str.replace(" ", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    return stock, sales, cogs


def basic_inventory_stats():
    stock, sales, cogs = load_data()

    return {
        "total_stock": stock["Stock"].sum(),
        "total_sales": sales["Sales"].sum(),
        "avg_stock": stock["Stock"].mean(),
        "avg_sales": sales["Sales"].mean()
    }
