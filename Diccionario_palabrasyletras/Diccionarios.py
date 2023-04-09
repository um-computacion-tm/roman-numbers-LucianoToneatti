import unittest

def count_letters(word):
    result= {}
    for letter in word:
        if letter in result:
           result[letter] += 1
    else:
      return result


class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        result = count_letters('a')
        self.assertEqual(result, {'a':1})
    
    def test_complex(self):
        result = count_letters('l')
        self.assertEqual(result, {'l':1})

if __name__ == '__main__':

    unittest.main() 
    
