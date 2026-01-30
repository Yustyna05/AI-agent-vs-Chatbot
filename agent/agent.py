from agent.planner import create_plan
from agent.tools import analyze_inventory, find_risky_skus
from agent.memory import AgentMemory
import os


class AIAgent:
    def __init__(self, objective: str):
        self.objective = objective
        self.memory = AgentMemory()
        self.plan = create_plan(objective)

    def run(self):
        final_result = None
        risky_df = None

        for step in self.plan:
            self.memory.add(f"Executing: {step}")

            if "Analyze" in step:
                final_result = analyze_inventory()
                self.memory.add(f"Analysis result calculated")

            if "risky" in step.lower():
                risky_df = find_risky_skus()
                self.memory.add(f"Risky SKUs found: {len(risky_df)}")

        self._save_report(final_result, risky_df)

        return final_result

    def _save_report(self, result: dict, risky_df):
        os.makedirs("reports", exist_ok=True)

        with open("reports/agent_report.txt", "w", encoding="utf-8") as f:
            f.write("AI AGENT ANALYSIS REPORT\n")
            f.write("========================\n\n")
            f.write(f"Objective:\n{self.objective}\n\n")

            if result:
                f.write("Results:\n")
                for key, value in result.items():
                    f.write(f"- {key.replace('_', ' ').title()}: {value:.2f}\n")

            if risky_df is not None and not risky_df.empty:
                f.write("\nRisky SKUs detected (coverage < 15 days):\n")
                for _, row in risky_df.iterrows():
                    f.write(
                        f"- SKU: {row['SKU']} | Stock: {row['Stock']:.2f} | "
                        f"Sales: {row['Sales']:.2f} | Coverage Days: {row['coverage_days']:.2f}\n"
                    )

                risky_df.to_csv("reports/risky_skus.csv", index=False)

            f.write("\nExecution steps:\n")
            for step in self.memory.show():
                f.write(f"- {step}\n")
