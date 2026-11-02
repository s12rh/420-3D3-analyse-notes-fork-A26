from models.cours import Cours
from models.session import Session
from models.groupe_cours import GroupeCours
from models.etudiant import Etudiant


class Programme:
    def __init__(self, nom: str):
        self.nom = nom
        self.cours: list[Cours] = []

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

    def moyenne(self) -> float:
        if not self.cours:
            return 0.0
        return round(sum(c.moyenne() for c in self.cours) / len(self.cours), 1)

    def nb_etudiants(self) -> int:
        return sum(c.nb_etudiants() for c in self.cours)
    
    def to_dict(self) -> dict:
        """Sérialise le programme pour le frontend.

        ⚠️  Même problème une troisième fois — si on ajoute
        un niveau, il faut modifier cette méthode aussi.
        """
        enfants = []
        for cours in self.cours:
            sessions_dict = []
            for session in cours.sessions:
                groupes_dict = []
                for groupe in session.groupes:
                    etudiants_dict = []
                    for etudiant in groupe.etudiants:
                        etudiants_dict.append({
                            "type": "etudiant",
                            "nom": etudiant.nom_complet(),
                            "moyenne": etudiant.moyenne(),
                            "nb_etudiants": 1,
                            "evaluations": etudiant.evaluations
                        })
                    groupes_dict.append({
                        "type": "groupecours",
                        "nom": groupe.nom,
                        "moyenne": groupe.moyenne(),
                        "nb_etudiants": groupe.nb_etudiants(),
                        "enfants": etudiants_dict
                    })
                sessions_dict.append({
                    "type": "session",
                    "nom": session.nom,
                    "moyenne": session.moyenne(),
                    "nb_etudiants": session.nb_etudiants(),
                    "enfants": groupes_dict
                })
            enfants.append({
                "type": "cours",
                "nom": cours.nom,
                "moyenne": cours.moyenne(),
                "nb_etudiants": cours.nb_etudiants(),
                "enfants": sessions_dict
            })

        return {
            "type": "programme",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": enfants
        }
