import unittest
import MySQLConnection

class TestsqlInput(unittest.TestCase):
    def test_nospace(self):
        with self.assertRaises(AssertionError):
            MySQLConnection.sqlInput("INSERT INTO people (name, email, phonenumber) VALUES (%s, %s, %s)","nospace")

if __name__ == '__main__':
    unittest.main()