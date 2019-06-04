import unittest
from tests.mobiletests.login.m_login_test import MLoginTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(MLoginTests)
#tc2 = unittest.TestLoader().loadTestsFromTestCase()

# Create a test suite combining all test classes
#smokeTest = unittest.TestSuite([tc1, tc2])
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#pytest -s -v tests/test_suite_mobile_sanity.py --browser none --os android --html=htmlreport.html