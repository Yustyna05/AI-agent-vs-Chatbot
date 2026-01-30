import pandas as pd


def analyze_inventory():
    stock = pd.read_csv("data/Stock.csv", sep=";")
    sales = pd.read_csv("data/Sales.csv", sep=";")

    stock["Stock"] = pd.to_numeric(stock["Stock"], errors="coerce")
    sales["Sales"] = pd.to_numeric(sales["Sales"], errors="coerce")

    return {
        "total_stock": stock["Stock"].sum(),
        "avg_stock": stock["Stock"].mean(),
        "total_sales": sales["Sales"].sum()
    }


def find_risky_skus():
    stock = pd.read_csv("data/Stock.csv", sep=";")
    sales = pd.read_csv("data/Sales.csv", sep=";")

    stock["Stock"] = pd.to_numeric(stock["Stock"], errors="coerce")
    sales["Sales"] = pd.to_numeric(sales["Sales"], errors="coerce")

    stock_total = stock.groupby("SKU")["Stock"].sum()
    sales_total = sales.groupby("SKU")["Sales"].sum()

    df = pd.concat([stock_total, sales_total], axis=1)

    df["coverage_days"] = df["Stock"] / (df["Sales"] / 30)

    risky = df[df["coverage_days"] < 15]

    return risky.reset_index()
