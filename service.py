import numpy as np
import bentoml
from bentoml.models import BentoModel

@bentoml.service
class IrisClassifier:
    model_ref = BentoModel("iris_clf:or57obftco4pdbdj")

    def __init__(self):
        self.model = bentoml.sklearn.load_model(self.model_ref)

    @bentoml.api
    def classify(self, input_series: np.ndarray) -> np.ndarray:
        return self.model.predict(input_series)