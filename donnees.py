from models.etudiant import Etudiant
from models.groupe_cours import GroupeCours
from models.session import Session
from models.cours import Cours
from models.programme import Programme
from models.composite import Composite



def construire_programme() -> Composite:

    # --- Étudiants ---
    alice   = Etudiant("Alice",   "Tremblay", {"TP1": 78, "TP2": 85, "Examen": 91})
    bob     = Etudiant("Bob",     "Nguyen",   {"TP1": 65, "TP2": 70, "Examen": 74})
    carla   = Etudiant("Carla",   "Diaz",     {"TP1": 92, "TP2": 88, "Examen": 95})
    # ...

    # --- 3D3 — Automne 2026 ---
    groupe_3d3_01 = Composite("Groupe 01", type_noeud="groupecours")
    groupe_3d3_01.ajouter(alice)
    groupe_3d3_01.ajouter(bob)

    groupe_3d3_02 = Composite("Groupe 02", type_noeud="groupecours")
    groupe_3d3_02.ajouter(carla)
    # ...

    session_3d3_a25 = Composite("Automne 2025", type_noeud="session")
    session_3d3_a25.ajouter(groupe_3d3_01)

    cours_3d3 = Composite("3D3 — Programmation orientée objet", type_noeud="cours")
    cours_3d3.ajouter(session_3d3_a25)
    # ...

    departement_informatique = Composite("Département d'informatique", type_noeud="departement")
    departement_informatique.ajouter(cours_3d3)
    departement_informatique.ajouter(cours_1d1)

    # --- Programme ---
    programme = Composite("Techniques de l'informatique", type_noeud="programme")
    programme.ajouter(cours_3d3)
