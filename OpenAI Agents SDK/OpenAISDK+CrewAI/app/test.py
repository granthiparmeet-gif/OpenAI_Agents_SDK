from agents import Runner
from .agent import agent

if __name__ == "__main__":
    result = Runner.run_sync(agent, "Write about the impact of digital twins in healthcare.")
    print(result.final_output)