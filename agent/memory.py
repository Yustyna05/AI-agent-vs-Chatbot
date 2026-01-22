class AgentMemory:
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def show(self):
        return self.steps
