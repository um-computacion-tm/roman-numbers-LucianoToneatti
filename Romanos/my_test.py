
import unittest
from my_romanos import decimal_to_roman
from my_romanos import roman_to_decimal
        
class TestDecimanalToRogman(unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")

    def test_2(self):
        resultado = decimal_to_roman(2)        
        self.assertEqual(resultado, "II")

    def test_3(self):
        resultado = decimal_to_roman(3)        
        self.assertEqual(resultado, "III")

    def test_4(self):        
        resultado = decimal_to_roman(4)       
        self.assertEqual(resultado, "IV")

    def test_5(self):        
        resultado = decimal_to_roman(5)        
        self.assertEqual(resultado, "V")

    def test_6(self):       
        resultado = decimal_to_roman(6)        
        self.assertEqual(resultado, "VI")

    def test_7(self):      
        resultado = decimal_to_roman(7)   
        self.assertEqual(resultado, "VII")

    def test_8(self):       
        resultado = decimal_to_roman(8)        
        self.assertEqual(resultado, "VIII")

    def test_9(self):        
        resultado = decimal_to_roman(9)        
        self.assertEqual(resultado, "IX")

    def test_10(self):        
        resultado = decimal_to_roman(10)        
        self.assertEqual(resultado, "X")

    def test_11(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, "L")

    def test_12(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")

    def test_13(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, "D")

    def test_14(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, "M")

    def test_15(self):
        resultado = decimal_to_roman(350)
        self.assertEqual(resultado, "CCCL")

    def test_16(self):
        resultado = decimal_to_roman(750)
        self.assertEqual(resultado, "DCCL")

    def test_17(self):
        resultado = decimal_to_roman(950)
        self.assertEqual(resultado, "CML")

    def test_18(self):
        resultado = decimal_to_roman(453)
        self.assertEqual(resultado, "CDLIII")

    def test_19(self):
        resultado = decimal_to_roman(97)
        self.assertEqual(resultado, "XCVII")

    def test_20(self):
        resultado = decimal_to_roman(678)
        self.assertEqual(resultado, "DCLXXVIII")

class TestRomantodecimal(unittest.TestCase):
    def test_1(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)

    def test_3(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)

    def test_4(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)

    def test_5(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)

    def test_6(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)

    def test_7(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)

    def test_8(self):
        resultado = roman_to_decimal('VIII')
        self.assertEqual(resultado, 8)

    def test_9(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)

    def test_10(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

    def test_11(self):
        resultado = roman_to_decimal('L')
        self.assertEqual(resultado, 50)

    def test_12(self):
        resultado = roman_to_decimal('C')
        self.assertEqual(resultado, 100)

    def test_13(self):
        resultado = roman_to_decimal('D')
        self.assertEqual(resultado, 500)

    def test_14(self):
        resultado = roman_to_decimal('M')
        self.assertEqual(resultado, 1000)

    def test_15(self):
        resultado = roman_to_decimal('CCCL')
        self.assertEqual(resultado, 350)

    def test_16(self):
        resultado = roman_to_decimal('DCCL')
        self.assertEqual(resultado, 750)

    def test_17(self):
        resultado = roman_to_decimal('CML')
        self.assertEqual(resultado, 950)

    def test_18(self):
        resultado = roman_to_decimal('CDLIII')
        self.assertEqual(resultado, 453)

    def test_19(self):
        resultado = roman_to_decimal('XCVII')
        self.assertEqual(resultado, 97)

    def test_20(self):
        resultado = roman_to_decimal('DCLXXVIII')
        self.assertEqual(resultado, 678)

if __name__ == '__main__':
    unittest.main()   