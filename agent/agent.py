from agent.planner import create_plan
from agent.tools import analyze_inventory
from agent.memory import AgentMemory


class AIAgent:
    def __init__(self, objective: str):
        self.objective = objective
        self.memory = AgentMemory()
        self.plan = create_plan(objective)

    def run(self):
        final_result = None

        for step in self.plan:
            self.memory.add(f"Executing: {step}")

            if "Analyze" in step:
                final_result = analyze_inventory()
                self.memory.add(f"Result: {final_result}")

        self._save_report(final_result)
        return final_result

    def _save_report(self, result: dict):
        with open("reports/agent_report.txt", "w", encoding="utf-8") as f:
            f.write("AI AGENT ANALYSIS REPORT\n")
            f.write("========================\n\n")
            f.write(f"Objective:\n{self.objective}\n\n")
            f.write("Results:\n")

            for key, value in result.items():
                f.write(f"- {key.replace('_', ' ').title()}: {value:.2f}\n")

            f.write("\nExecution steps:\n")
            for step in self.memory.show():
                f.write(f"- {step}\n")
