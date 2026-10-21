import unittest

from convertisseur_unites.conversion import convertir, convertir_temperature


class TestLongueur(unittest.TestCase):
    def test_km_vers_m(self):
        self.assertAlmostEqual(convertir(1, "km", "m", "longueur"), 1000)

    def test_mile_vers_km(self):
        self.assertAlmostEqual(convertir(1, "mile", "km", "longueur"), 1.609344)

    def test_pouce_vers_cm(self):
        self.assertAlmostEqual(convertir(1, "pouce", "cm", "longueur"), 2.54)

    def test_meme_unite(self):
        self.assertAlmostEqual(convertir(5, "m", "m", "longueur"), 5)

    def test_unite_inconnue_leve_erreur(self):
        with self.assertRaises(ValueError):
            convertir(1, "annee-lumiere", "m", "longueur")

    def test_categorie_inconnue_leve_erreur(self):
        with self.assertRaises(ValueError):
            convertir(1, "m", "m", "duree")


class TestPoids(unittest.TestCase):
    def test_kg_vers_g(self):
        self.assertAlmostEqual(convertir(1, "kg", "g", "poids"), 1000)

    def test_livre_vers_kg(self):
        self.assertAlmostEqual(convertir(1, "livre", "kg", "poids"), 0.45359237)


class TestVolume(unittest.TestCase):
    def test_litre_vers_ml(self):
        self.assertAlmostEqual(convertir(1, "l", "ml", "volume"), 1000)

    def test_gallon_vers_litre(self):
        self.assertAlmostEqual(convertir(1, "gallon_us", "l", "volume"), 3.785411784)


class TestVitesse(unittest.TestCase):
    def test_kmh_vers_ms(self):
        self.assertAlmostEqual(convertir(36, "km/h", "m/s", "vitesse"), 10, places=5)

    def test_noeud_vers_kmh(self):
        self.assertAlmostEqual(convertir(1, "noeud", "km/h", "vitesse"), 1.852, places=3)


class TestTemperature(unittest.TestCase):
    def test_eau_gele_c_vers_f(self):
        self.assertAlmostEqual(convertir_temperature(0, "c", "f"), 32)

    def test_eau_bout_c_vers_f(self):
        self.assertAlmostEqual(convertir_temperature(100, "c", "f"), 212)

    def test_c_vers_k(self):
        self.assertAlmostEqual(convertir_temperature(0, "c", "k"), 273.15)

    def test_f_vers_c(self):
        self.assertAlmostEqual(convertir_temperature(32, "f", "c"), 0)

    def test_k_vers_c(self):
        self.assertAlmostEqual(convertir_temperature(273.15, "k", "c"), 0)

    def test_zero_absolu_interdit(self):
        with self.assertRaises(ValueError):
            convertir_temperature(-1, "k", "c")

    def test_resultat_kelvin_negatif_leve_erreur(self):
        with self.assertRaises(ValueError):
            convertir_temperature(-300, "c", "k")

    def test_unite_inconnue(self):
        with self.assertRaises(ValueError):
            convertir_temperature(0, "c", "rankine")


if __name__ == "__main__":
    unittest.main()
