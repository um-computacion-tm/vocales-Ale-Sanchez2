import unittest
from Contadorvocales import contar_vocales

class testvocales (unittest.TestCase):
    def testzzz(self):
        result = contar_vocales("zzz")
        self.assertEqual(result, {})
    def testA(self):
        result = contar_vocales("a")
        self.assertEqual(result, {'a': 1})
    def testABC(self):
        result = contar_vocales("abc")
        self.assertEqual(result, {'a': 1})
    def testACA(self):
        result = contar_vocales("aca")
        self.assertEqual(result, {'a': 2})
    def testBANANA(self):
        result = contar_vocales("banAna")
        self.assertEqual(result, {'a': 2, 'A': 1})
    def testBESE(self):
        result = contar_vocales("bEse")
        self.assertEqual(result, {'e': 1, 'E': 1})
    def testMURCIELAGO(self):
        result = contar_vocales("mUrcIelagO")
        self.assertEqual(result, {'a': 1, 'e':1, 'I':1, 'O':1, 'U':1})
    def testZZZZ(self):
        result = contar_vocales("ZZZZZ")
        self.assertEqual(result, {})
    def testAEIOU(self):
        result=contar_vocales("aeiouAEIOU")
        self.assertEqual(result, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1})
    def testAEIOYconAcentos(self):
        result=contar_vocales("áéíóúÁÉÍÓÚ")
        self.assertEqual(result, {'á': 1, 'é': 1, 'í': 1, 'ó': 1, 'ú': 1, 'Á': 1, 'É': 1, 'Í': 1, 'Ó': 1, 'Ú': 1})
    def testOtorrinolarigologista(self):
        result=contar_vocales("Otorrinolarigologista")
        self.assertEqual(result, {'a': 2, 'i': 3, 'o': 4, 'O':1 })
    def testOtorrinolaringologistaconAcentos(self):
        result=contar_vocales("Otorrinolaringólogista")
        self.assertEqual(result, {'a': 2, 'i': 3, 'o': 3, 'ó': 1, 'O':1})

if __name__ == '__main__':
    unittest.main()