"""
test_employee.py
"""
import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run once at the beginning"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Run once at the end"""
        pass

    def setUp(self):
        """Run before each test"""
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        """Run after each test"""
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
