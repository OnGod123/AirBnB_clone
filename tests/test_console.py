import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        del self.cmd

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.cmd.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("created", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.cmd.do_show("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("show", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.cmd.do_destroy("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("destroyed", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.cmd.do_all("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("all", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.cmd.do_update("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("updated", output)

    @patch('sys.exit')
    def test_quit(self, mock_exit):
        with self.assertRaises(SystemExit):
            self.cmd.do_quit("")
        mock_exit.assert_called_once()

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.cmd.emptyline()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        result = self.cmd.do_EOF("")
        self.assertTrue(result)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()

