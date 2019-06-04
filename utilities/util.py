"""
Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.verifyTextContains("Irvine", "East Irvine")

"""
import utilities.custom_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text --> :: " + actualText)
        self.log.info("Expected Text --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text --> :: " + actualText)
        self.log.info("Expected Text --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True