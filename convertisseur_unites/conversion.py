"""Conversions d'unités par catégorie, via un facteur commun vers une unité de référence.

Chaque catégorie définit un dict {unité: facteur vers l'unité de référence}, sauf la
température qui a sa propre logique (la conversion n'est pas un simple facteur).
"""

from __future__ import annotations

# Unité de référence : le mètre
LONGUEUR = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "pouce": 0.0254, "pied": 0.3048, "yard": 0.9144, "mile": 1609.344,
}

# Unité de référence : le kilogramme
POIDS = {
    "mg": 1e-6, "g": 0.001, "kg": 1.0, "tonne": 1000.0,
    "once": 0.028349523125, "livre": 0.45359237,
}

# Unité de référence : le litre
VOLUME = {
    "ml": 0.001, "cl": 0.01, "l": 1.0,
    "gallon_us": 3.785411784, "pinte_us": 0.473176473,
}

# Unité de référence : le mètre par seconde
VITESSE = {
    "m/s": 1.0, "km/h": 1 / 3.6, "mph": 0.44704, "noeud": 0.5144444444444445,
}

CATEGORIES = {"longueur": LONGUEUR, "poids": POIDS, "volume": VOLUME, "vitesse": VITESSE}


def convertir(valeur: float, unite_depart: str, unite_arrivee: str, categorie: str) -> float:
    """Convertit une valeur entre deux unités d'une catégorie donnée (hors température)."""
    if categorie not in CATEGORIES:
        raise ValueError(f"catégorie inconnue : {categorie} (attendu : {', '.join(CATEGORIES)}, ou 'temperature')")
    table = CATEGORIES[categorie]
    if unite_depart not in table:
        raise ValueError(f"unité inconnue '{unite_depart}' pour la catégorie {categorie}")
    if unite_arrivee not in table:
        raise ValueError(f"unité inconnue '{unite_arrivee}' pour la catégorie {categorie}")
    valeur_reference = valeur * table[unite_depart]
    return valeur_reference / table[unite_arrivee]


TEMPERATURE_UNITES = {"c", "f", "k"}


def convertir_temperature(valeur: float, unite_depart: str, unite_arrivee: str) -> float:
    """Convertit une température entre Celsius (c), Fahrenheit (f) et Kelvin (k)."""
    d, a = unite_depart.lower(), unite_arrivee.lower()
    if d not in TEMPERATURE_UNITES or a not in TEMPERATURE_UNITES:
        raise ValueError("unité de température inconnue (attendu : c, f ou k)")

    # D'abord vers Celsius
    if d == "c":
        celsius = valeur
    elif d == "f":
        celsius = (valeur - 32) * 5 / 9
    else:  # k
        celsius = valeur - 273.15
        if valeur < 0:
            raise ValueError("une température en Kelvin ne peut pas être négative")

    # Puis de Celsius vers la cible
    if a == "c":
        return celsius
    if a == "f":
        return celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("résultat en Kelvin négatif : température physiquement impossible")
    return kelvin
