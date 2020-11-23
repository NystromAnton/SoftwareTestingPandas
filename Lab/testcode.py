import bibtex
import unittest

class TestAuthorExtract(unittest.TestCase):
    """Functions for testing the extraction of author names.

    Note that the rules for extracting bibtex author names is actually
    quite complicated. As these test cases illustrate. I haven´t
    implemented alla the cases."""

    def setUp(self):
        self.simple_author_1 = "Smith"
        self.simple_author_2 = "Jones"
        self.author_1 = "John Smith"
        self.author_2 = "Bob Jones"
        self.author_3 = "Justin Kenneth Pearson"
        self.surname_first_1 = "Pearson, Justin Kenneth"
        self.surname_first_2 = "Van Hentenryck, Pascal"
        self.multiple_authors_1 = "Pearson, Justin and Jones, Bob"
        self.multiple_authors_2 = "Pearson, Justin and Jones, Bob and Johan and Billy Bob and Isac Newton, person"
    def test_author_1(self):
        #Test only surnames.
        (Surname, First) = bibtex.extract_author(self.simple_author_1)
        self.assertEqual( (Surname, First), ('Smith',''))
        (Surname, First) = bibtex.extract_author(self.simple_author_2)
        self.assertEqual( (Surname, First), ('Jones',''))

    def test_author_2(self):
        #Test simple firstname author.
        (Surname, First) = bibtex.extract_author(self.author_1)
        self.assertEqual( (Surname, First), ('Smith','John'))
        (Surname, First) = bibtex.extract_author(self.author_2)
        self.assertEqual( (Surname, First), ('Jones','Bob'))

    def test_author_3(self):
        (Surname, First) = bibtex.extract_author(self.author_3)
        self.assertEqual( (Surname, First), ('Pearson','Justin Kenneth'))

    def test_surname_first(self):
        (Surname, First) = bibtex.extract_author(self.surname_first_1)
        self.assertEqual( (Surname, First), ('Pearson','Justin Kenneth'))
        (Surname, First) = bibtex.extract_author(self.surname_first_2)
        self.assertEqual( (Surname, First), ('Van Hentenryck','Pascal'))

    def test_multiple_authors(self):
        Authors = bibtex.extract_authors(self.multiple_authors_1)
        self.assertEqual(Authors[0], ('Pearson','Justin'))
        self.assertEqual(Authors[1], ('Jones','Bob'))
    
    def test_multiple_authors_hard(self):
        Authors = bibtex.extract_authors(self.multiple_authors_2)
        self.assertEqual(Authors[0], ('Pearson','Justin'))
        self.assertEqual(Authors[1], ('Jones','Bob'))
        self.assertEqual(Authors[2], ('Johan',''))
        self.assertEqual(Authors[3], ('Bob','Billy'))
        self.assertEqual(Authors[4], ('Isac Newton','person'))

if __name__ == '__main__':
    unittest.main()
