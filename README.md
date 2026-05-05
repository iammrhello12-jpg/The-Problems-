# AI Agent Project

A simple, open-source AI agent designed for intent classification and automated responses. This project is built using Python, Scikit-learn, and FastAPI.

## Features
- **Intent Classification**: Uses TF-IDF and Naive Bayes to classify user input.
- **FastAPI Interface**: A clean REST API for interacting with the agent.
- **Dockerized**: Ready for deployment using Docker.
- **Easily Trainable**: Simple CSV-based training data format.

## Project Structure
- `src/agent/`: Core logic and API implementation.
- `data/`: Training data in CSV format.
- `scripts/`: Utility scripts for training the model.
- `tests/`: Unit and integration tests.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training

To train the model with your own data, update `data/intents.csv` and run:

```bash
python scripts/train.py
```

## Running the API

Start the FastAPI server:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
uvicorn agent.main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive documentation at `http://localhost:8000/docs`.

## Deployment with Docker

Build the Docker image:

```bash
docker build -t ai-agent .
```

Run the container:

```bash
docker run -p 8000:8000 ai-agent
```

## Deployment with Vercel

This project is configured for easy deployment to Vercel.

1. Install the Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

## Mobile App (Android APK)

The project includes a Kivy-based mobile interface.

### Build APK

To build the Android APK, you need to have `buildozer` installed along with its dependencies (Android SDK, NDK, etc.).

```bash
buildozer android debug
```

The generated APK will be in the `bin/` directory.

### Run locally

You can test the mobile UI on your desktop if you have Kivy installed:

```bash
python src/mobile/main.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
