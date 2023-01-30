
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        #lista de classes
        dict_class = {}
        for i in range (train_dataset.size):
            amostra, classe = train_dataset[i].get[1]
            if classe not in dict_class:
                dict_class[classe] = []
            dict_class[classe].append(amostra)

            #calcular os centroides por classe
            #para isso, guardar o vetor junto do item da amostra
            tam = len(amostra)
        

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """

        return []

    
