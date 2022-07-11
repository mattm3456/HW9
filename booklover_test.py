import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book("50 shades of grey", 10)
        actual = Zack.book_list.to_dict()
        expected = {'book_name': {0: '50 shades of grey'}, 'book_rating': {0:10}}
        self.assertEqual(actual, expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book("50 shades of grey", 10)
        Zack.add_book("50 shades of grey",10)
        actual = Zack.book_list.to_dict()
        expected = {'book_name': {0: '50 shades of grey'}, 'book_rating': {0:10}}
        self.assertEqual(actual, expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book('50 shades of grey',10)
        actual = Zack.has_read('50 shades of grey')
        expected = True
        self.assertEqual(actual, expected)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book('50 shades of grey',10)
        test_value = Zack.has_read('Spongebob')
        message = "Zack actually has read this"
        self.assertFalse(test_value, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book('50 shades of grey',10)
        Zack.add_book('Jurassic Park', 8)
        Zack.add_book('DaVinci Code',4)
        actual = Zack.num_books_read()
        expected = 3
        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        Zack = BookLover('Zack','zack@zack.com','romance')
        Zack.add_book('50 shades of grey',5)
        Zack.add_book('Jurassic Park', 3.2)
        Zack.add_book('DaVinci Code',1)
        Zack.add_book('Spongebob',2)
        actual = Zack.book_list
        expected = {'book_name':['50 shades of grey','Jurassic Park'], 'book_rating': [5,3.2]}
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)