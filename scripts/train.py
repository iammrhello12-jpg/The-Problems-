import sys
import os

# Add src to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agent.model import SimpleAgent

def main():
    print("Training the agent...")
    agent = SimpleAgent()
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'intents.csv'))
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model.joblib'))

    agent.train(data_path)
    agent.save(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
