#!/usr/bin/env python

"""PyQt4 port of the dialogs/standarddialogs example from Qt v4.x"""

# This is only needed for Python v2 but is harmless for Python v3.
#import sip
#sip.setapi('QString', 2)

import sys
from PySide import QtCore, QtGui

TEXT_ITEM_COLOR = 'blue'
TEXT_CHOICE_COLOR = 'red'
BANNER_COLOR = 'black'
BANNER_TEXT_COLOR = 'white'

class Dialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        layout = QtGui.QGridLayout()
        
        self.banner = makeAppBanner("invisible-motorcycle-150.jpg")
        layout.addWidget(self.banner, 0, 0, 2, 0)
        
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(0, 200)
        layout.setColumnMinimumWidth(1, 200)
        
        

        self.testTextEntry = QtGui.QLineEdit()
        self.testTextEntry.textChanged.connect(testTextEntryAction)
        layout.addWidget(self.testTextEntry)
                
        self.testButton = QtGui.QPushButton("TEST BUTTON")
        self.testButton.clicked.connect(testAction)
        layout.addWidget(self.testButton)

        textItems = []
        
        choices = loadChoices()
        for choice in choices:
            textItems.append(makeTextItem(choice, TEXT_CHOICE_COLOR))

        addTextItems(layout, textItems)

        self.setLayout(layout)

        self.setWindowTitle("What's Missing??")
        
        def testItemChange(text):
            print("TEST ITEM CHANGE!!!")
            
        
def testAction():
    print("TEST ACTION!!")
    
def testTextEntryAction(text):
    print("YOU ENTERED " + text)
        
def addTextItems(layout, textItems):
    for item in textItems:
        layout.addWidget(item)    
        
def loadChoices():
    return [line.rstrip('\n') for line in open('whats-missing-choices.txt')]
    
def makeTextItem(text, color):
    if color == TEXT_CHOICE_COLOR:
        itemHead = "<font color=" + TEXT_CHOICE_COLOR + " size=40>"
    else:
        itemHead = "<font color=" + TEXT_ITEM_COLOR + " size=40>"
        
    itemTail = "</font>"
    
    return QtGui.QLabel(itemHead + text + itemTail)
    
def makeAppBanner(imageLocation):
    bannerHead = "<div style=\"background-color: " + BANNER_COLOR + ";\">"
                 
    image = "<img src=\"" + imageLocation + "\"\\>"
                 
    bannerTail = "</font></div>"
    
    banner = QtGui.QLabel(bannerHead + image + bannerTail)
    banner.setContentsMargins(0, 0, 0, 20)
    
    return banner

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())