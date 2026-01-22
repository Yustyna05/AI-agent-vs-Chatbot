from analysis.data_analysis import basic_inventory_stats


def chatbot_response(user_prompt: str):
    if "inventory" in user_prompt.lower():
        stats = basic_inventory_stats()
        return (
            f"Inventory analysis:\n"
            f"- Total stock: {stats['total_stock']}\n"
            f"- Average stock: {stats['avg_stock']:.2f}\n"
            f"- Total sales: {stats['total_sales']}\n"
        )

    return "I can answer questions about inventory only."
