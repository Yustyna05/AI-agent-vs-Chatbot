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

def find_risky_skus(threshold_days=30):
    stock, sales, _ = load_data()

    # aggregate per SKU
    stock_sku = stock.groupby("SKU")["Stock"].sum()
    sales_sku = sales.groupby("SKU")["Sales"].sum()

    merged = stock_sku.to_frame().join(sales_sku, how="left").fillna(0)

    # avoid divide by zero
    merged["coverage_days"] = merged.apply(
        lambda r: (r["Stock"] / r["Sales"] * 30) if r["Sales"] > 0 else 999,
        axis=1
    )

    risky = merged[merged["coverage_days"] < threshold_days]

    return risky
