import unittest as ut
import zadania as z

class TestZadanie(ut.TestCase):
    def test_zliczenie_znakow(self):
        self.assertEqual(z.ile_znakow("tekst"), {"t" : 2, "e" : 1, "k" : 1, "s" : 1})
        self.assertEqual(z.ile_znakow(""), {})

    def test_usuwanie_duplikatow(self):
        self.assertEqual(z.usuwanie_duplikatow_z_listy([1, 2, 1, 5, 6]),[1, 2, 5, 6])
        self.assertEqual(z.usuwanie_duplikatow_z_listy([]), [])
        self.assertEqual(z.usuwanie_duplikatow_z_listy([1, 1, 1]),[1])
        self.assertEqual(z.usuwanie_duplikatow_z_listy(["a", "b", "a"]),["a", "b"])


    def test_ile_dni(self):
        self.assertEqual(z.ile_dni(3, 2027), 31)
        self.assertEqual(z.ile_dni(2, 2027), 28)
        self.assertEqual(z.ile_dni(2, 2028), 29)

    def reszta(self):
        self.assertEqual(z.reszta(30,30), 0)
        self.assertEqual(z.reszta(50,30), 20)

if __name__ == "__main__":
    ut.main()