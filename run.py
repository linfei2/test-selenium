import unittest
from tests.register_page_test import RegistrationTest

registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

test_suite = unittest.TestSuite([registration_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
