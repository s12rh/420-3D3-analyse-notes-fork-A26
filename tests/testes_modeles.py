# tests/test_modeles.py
import pytest
from models.etudiant import Etudiant
from models.composite import GroupeCours, Cours


class TestEtudiant:
    def test_moyenne_une_evaluation(self):
        e = Etudiant("Alice", "Roy", {"TP1": 80.0})
        assert e.moyenne() == 80.0

    def test_moyenne_plusieurs_evaluations(self):
        e = Etudiant("Alice", "Roy", {"TP1": 80.0, "TP2": 90.0, "Exam": 70.0})
        assert e.moyenne() == 80.0

    def test_moyenne_arrondie_a_un_decimal(self):
        e = Etudiant("Alice", "Roy", {"TP1": 100.0, "TP2": 85.0})
        assert e.moyenne() == 92.5

    def test_moyenne_sans_evaluation_retourne_zero(self):
        e = Etudiant("Alice", "Roy", {})
        assert e.moyenne() == 0.0

    def test_nb_etudiants_est_toujours_un(self):
        e = Etudiant("Alice", "Roy", {"TP1": 75.0})
        assert e.nb_etudiants() == 1

    def test_nom_complet(self):
        e = Etudiant("Alice", "Roy", {})
        assert e.nom == "Alice Roy"


class TestGroupeCours:
    def test_moyenne_groupe_vide_retourne_zero(self):
        g = GroupeCours("Groupe 01")
        assert g.moyenne() == 0.0

    def test_moyenne_un_etudiant(self):
        g = GroupeCours("Groupe 01")
        g.ajouter(Etudiant("Alice", "Roy", {"TP1": 80.0}))
        assert g.moyenne() == 80.0

    def test_moyenne_plusieurs_etudiants(self):
        g = GroupeCours("Groupe 01")
        g.ajouter(Etudiant("Alice", "Roy", {"TP1": 80.0}))
        g.ajouter(Etudiant("Bob", "Tremblay", {"TP1": 60.0}))
        assert g.moyenne() == 70.0

    def test_nb_etudiants_groupe_vide(self):
        g = GroupeCours("Groupe 01")
        assert g.nb_etudiants() == 0

    def test_nb_etudiants_apres_ajout(self):
        g = GroupeCours("Groupe 01")
        g.ajouter(Etudiant("Alice", "Roy", {"TP1": 80.0}))
        g.ajouter(Etudiant("Bob", "Tremblay", {"TP1": 60.0}))
        assert g.nb_etudiants() == 2

    def test_retirer_etudiant(self):
        g = GroupeCours("Groupe 01")
        alice = Etudiant("Alice", "Roy", {"TP1": 80.0})
        g.ajouter(alice)
        g.retirer(alice)
        assert g.nb_etudiants() == 0


class TestHierarchie:
    def test_cours_agregge_ses_groupes(self):
        cours = Cours("420-3D3")
        g1 = GroupeCours("Groupe 01")
        g1.ajouter(Etudiant("Alice", "Roy", {"TP1": 80.0}))
        g2 = GroupeCours("Groupe 02")
        g2.ajouter(Etudiant("Bob", "Tremblay", {"TP1": 60.0}))
        cours.ajouter(g1)
        cours.ajouter(g2)
        assert cours.moyenne() == 70.0
        assert cours.nb_etudiants() == 2