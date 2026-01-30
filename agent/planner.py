def create_plan(objective: str):

    obj = objective.lower()

    # new plan for warning / risk analysis
    if "risk" in obj or "warning" in obj or "reorder" in obj:
        return [
            "Load inventory data",
            "Analyze stock and sales",
            "Find risky SKUs",
            "Report warning"
        ]

    # default plan
    return [
        "Load inventory data",
        "Analyze stock and sales",
        "Check goal",
        "Report results"
    ]
