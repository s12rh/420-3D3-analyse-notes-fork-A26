from models.composant import Composant
from abc import ABC, abstractmethod

class Composite(Composant):
    
    def __init__(self, nom: str, type_noeud: str):
        super().__init__(nom)
        self.type_noeud = type_noeud
        self._enfants: list[Composant] = []

    def to_dict(self) -> dict:
        return {
            "type": self.type_noeud,
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [enfant.to_dict() for enfant in self._enfants]

        }

# Utilisation
groupe = Composite("Groupe 01", type_noeud="groupecours")
session = Composite("A26", type_noeud="session")