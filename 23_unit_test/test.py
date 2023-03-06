import unittest  # il built-in module per gli unit test
import main
# DRY si applica meno ai test
# python3 -m unittest runna tutti i test della folder
# python3 -m unittest -v runna tutti i test della folder verbosamente


class TestMain(unittest.TestCase):
    def setUp(self) -> None:  # funzione che viene runnata prima di ogni test
        print('about to test a function!')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hi'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))
        # equivalente
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def tearDown(self) -> None:  # viene eseguito dopo ogni test
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
