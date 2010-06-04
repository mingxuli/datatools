# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import cal
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtTest import QTest

class  CalTestCase(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.form = cal.Form()
        self.lineEdit = self.form.lineEdit
        self.browser = self.form.browser

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testCal(self):
        self.lineEdit.setText("1+1")
        QTest.keyPress(self.lineEdit,Qt.Key_Enter,Qt.NoModifier, -1)
        self.assertEquals(self.browser.toPlainText().count(),5, self.browser.toPlainText().count())

if __name__ == '__main__':
    unittest.main()

