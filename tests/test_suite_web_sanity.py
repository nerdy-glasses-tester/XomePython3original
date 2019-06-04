import unittest
from tests.webtests.login.login_test import LoginTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
#tc2 = unittest.TestLoader().loadTestsFromTestCase()

# Create a test suite combining all test classes
#smokeTest = unittest.TestSuite([tc1, tc2])
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#pytest -s -v tests/test_suite_web_sanity.py --browser chrome --os none --html=htmlreport.html
