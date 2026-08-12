class ReflexionAgent:
    def __init__(self):
        self.memory = []

    def execute_task(self, task_description: str):
        attempt = f"Draft solution for: {task_description}"
        critique = "Critique: Lacks edge case handling and error logging."
        improved = f"Refined solution for: {task_description} with robust error handling, unit tests, and validation."
        
        self.memory.append({
            "task": task_description,
            "initial_attempt": attempt,
            "critique": critique,
            "improved_solution": improved
        })
        return improved
