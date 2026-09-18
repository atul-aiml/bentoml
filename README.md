# BentoML Iris Classifier

A minimal machine learning service built with [BentoML](https://www.bentoml.com/) that trains a Support Vector Machine (SVM) classifier on the classic Iris dataset and serves it as a REST API.

## Overview

This project demonstrates a simple end-to-end ML deployment workflow:

1. **Train** a scikit-learn SVM model on the Iris dataset
2. **Save** the trained model to the BentoML local model store
3. **Serve** the model as an API endpoint using BentoML's service framework
4. **Test** the deployed service with sample requests

## Project Structure

```
bentoml/
├── bentofile.yaml     # BentoML build configuration
├── requirements.txt   # Python dependencies
├── service.py          # BentoML service definition (inference API)
├── train.py            # Model training script
├── test.py             # Script to test the running service
└── .gitignore
```

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/atul-aiml/bentoml.git
   cd bentoml
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Train the model

Run the training script to fit the SVM classifier on the Iris dataset and save it to the BentoML model store:

```bash
python train.py
```

This will output a confirmation with the saved model tag, e.g.:
```
Model saved: Model(tag="iris_clf:xxxxxxxx")
```

### 2. Serve the model

Start the BentoML service locally:

```bash
bentoml serve service.py:IrisClassifier
```

By default, the service will be available at `http://localhost:3000`. You can explore the interactive Swagger UI at `http://localhost:3000` in your browser.

### 3. Test the service

With the service running, execute the test script in a separate terminal to send a sample prediction request:

```bash
python test.py
```

## Building a Bento

To package the service, model, and dependencies into a deployable artifact (a "Bento"):

```bash
bentoml build
```

This uses the configuration defined in `bentofile.yaml`.

## Containerizing (optional)

Once built, you can containerize the Bento into a Docker image:

```bash
bentoml containerize iris_classifier:latest
```

## Tech Stack

- **[BentoML](https://www.bentoml.com/)** — model serving and packaging framework
- **[scikit-learn](https://scikit-learn.org/)** — SVM model training
- **[NumPy](https://numpy.org/)** — numerical input handling

## License

This project is open source and available for personal or educational use.
