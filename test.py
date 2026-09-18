import bentoml

model = bentoml.sklearn.load_model("iris_clf:latest")
print(model.predict([[5.9, 3., 5.1, 1.8]]))