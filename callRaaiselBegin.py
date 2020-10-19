import sys
import copy
from PyQt5 import QtCore, QtGui
from woordRaaisel import *
from ReworkedList import *
from raaiselBegin import Ui_Dialog as RaaiselBeginDialog
from verkeerdeWoord import Ui_Dialog as VerkeerdeWoordDialog
from moontlikeWoorde import Ui_Dialog as MoontlikeWoordeDialog
from kiesEieWoord import Ui_Dialog as KiesEieWoordDialog
from VoegWoordByWoodeboek import Ui_Dialog as VoegByWoordeboekDialog
from raaiselsKlaarGedoen import Ui_Dialog as RaaiselsKlaarGedoenDialog
from maksimumEnMinimum import Ui_Dialog as MaksimumEnMinimumDialog
from gameSaved import Ui_Dialog as GameSavedDialog
class GameSaved(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = GameSavedDialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.GameSaved)

    def GameSaved(self):
        self.reject()
class RaaiselsKlaarGedoen(QtWidgets.QDialog):
    def __init__(self, Game=ReworkedList(), parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = RaaiselsKlaarGedoenDialog()
        self.ui.setupUi(self)
        SomeGame = Game
        raaiselsGedoen = copy.deepcopy(SomeGame.GetNineLetterWordCompleted())
        if(len(raaiselsGedoen)>0):
            for word in raaiselsGedoen:
                if(len(word)>3):
                    wordAttempt = word.replace('\n','')
                    self.ui.textEdit.append(wordAttempt)
        self.ui.pushButton.clicked.connect(self.RaaiselsKlaar)
        self.ui.pushButton.setFocus(True)
        self.ui.pushButton.setAutoDefault(True)        
    def RaaiselsKlaar(self):
        self.reject()
        
class VoegWoordBy(QtWidgets.QDialog):
    def __init__(self,game=ReworkedList(), parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VoegByWoordeboekDialog()
        self.someGame = game
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.VoegWoordBy)
        self.ui.lineEdit.returnPressed.connect(self.VoegWoordBy)
        self.ui.lineEdit.setFocus(True)
    def VoegWoordBy(self):
        word = self.ui.lineEdit.text().upper() + '\n'
        if(word not in self.someGame.m_currentPossibleWords):
            f = open('afrwde.txt','a')
            f.write(str(self.ui.lineEdit.text()).upper()+'\n')
            f.close()
        self.reject()

class KiesEieWoord(QtWidgets.QDialog):
    def __init__(self, Game=ReworkedList(), parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = KiesEieWoordDialog()
        self.ui.setupUi(self)
        self.Game = Game
        self.ui.pushButton.clicked.connect(self.KiesWoord)
        self.ui.lineEdit.returnPressed.connect(self.KiesWoord)
        self.ui.lineEdit.setFocus(True)
    def KiesWoord(self):
        self.Game.ChooseOwnNineLetterWord(self.ui.lineEdit.text())
        self.reject()

class MoontlikeWoorde(QtWidgets.QDialog):
    def __init__(self, PossibleWords, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MoontlikeWoordeDialog()
        self.ui.setupUi(self)
        self.MoontlikeWoorde = list(PossibleWords)
        self.ui.textEdit.clear()
        for word in self.MoontlikeWoorde:
            someWord = word.replace('\n','')
            self.ui.textEdit.append(someWord)
        self.ui.pushButton.clicked.connect(self.GaanVoort)
        self.ui.pushButton.setAutoDefault(True)
    def GaanVoort(self):
        self.reject()

class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Game = ReworkedList()
        self.Game.FirstRound()
        self.num = 0
        global NuweGame
        global OuGame
        self.GameSetup()
        self.ui.pushKlaar.clicked.connect(self.CheckWord)
        self.ui.pushNuweWoord.clicked.connect(self.NuweRondte)
        self.ui.pushMoontlikeWoorde.clicked.connect(self.MoontlikeWoorde)
        self.ui.actionB_re_Raaisel.triggered.connect(self.SaveGame)
        self.ui.actionLaai_Ou_Raaisel.triggered.connect(self.LoadGame)
        self.ui.pushKiesWoord.clicked.connect(self.KiesWoord)
        self.ui.actionNuwe_Spel.triggered.connect(self.NuweGame)
        self.ui.pushVoegByWoordeboek.clicked.connect(self.VoegByWoordeBoek)
        self.ui.pushRaaiselsKlaarGedoen.clicked.connect(self.RaaiselsKla)
        self.ui.lineEditKiesWoord.returnPressed.connect(self.CheckWord)
        self.ui.pushChangeMiddleLetter.clicked.connect(self.ChangeMiddleLetter)
        self.ui.lineEditKiesWoord.setFocus(True)
    def ChangeMiddleLetter(self): 
        num = self.num
        num %= 9
        print(num)
        #num -= 1 
        self.Game.ChangeMiddleLetter(num)
        self.GameSetup()
        self.ui.textEditWoordLys.clear()
        self.ui.lineEditKiesWoord.setFocus(True)
        self.num += 1
    def RaaiselsKla(self):
        raaiselsKla = RaaiselsKlaarGedoen(self.Game)
        raaiselsKla.exec_()
        self.ui.lineEditKiesWoord.setFocus(True)
        
    def VoegByWoordeBoek(self):
        voegByWoordeboek = VoegWoordBy(self.Game)
        voegByWoordeboek.exec_()
        self.Game.CurrentPossibleWords(True)
        wordsInList = copy.deepcopy(self.Game.GetCurrentWordsCompleted())
        for word in wordsInList:
            self.Game.m_currentWordsCompleted.remove(word)
            self.Game.m_currentNumberWordsChosen -= 1
            self.Game.TakeWordFromPlayer(word)         
        self.GameSetup()
        self.ui.lineEditKiesWoord.setFocus(True)
        
    def NuweGame(self):
        self.Game.NextRound()
        self.GameSetup()
        self.ui.textEditWoordLys.clear()
        self.ui.lineEditKiesWoord.setFocus(True)
    def KiesWoord(self):
        kiesWoord = KiesEieWoord(self.Game)
        kiesWoord.exec_()
        self.ui.textEditWoordLys.clear()
        self.GameSetup()
        self.ui.lineEditKiesWoord.setFocus(True)
        

        
    def LoadGame(self):
        self.Game.LoadGame()
        self.GameSetup()
        self.ui.lineEditKiesWoord.setFocus(True)
        

    def SaveGame(self):
        self.Game.SaveGame()
        saveGame = GameSaved()
        saveGame.exec_()
        self.ui.lineEditKiesWoord.setFocus(True)

        
    def MoontlikeWoorde(self):
        moontlikeWoorde = MoontlikeWoorde(self.Game.GetPossibleWords())
        moontlikeWoorde.exec_()
        self.ui.lineEditKiesWoord.setFocus(True)

    def NuweRondte(self):
        self.ui.textEditWoordLys.clear()
        self.Game.NextRound()
        self.GameSetup()
        self.ui.lineEditKiesWoord.setFocus(True)

    def CheckWord(self):
        wordAttempt = str(self.ui.lineEditKiesWoord.text()).upper()
        self.ui.lineEditKiesWoord.clear()
        if(self.Game.TakeWordFromPlayer(wordAttempt)):
            self.RoundUpdate()
        else:
            verkeerdeWoord = VerkeerdeWoord()
            verkeerdeWoord.exec_()
        self.ui.lineEditKiesWoord.setFocus(True)
        
    def RoundUpdate(self):
        self.ui.lineNommerWoordeGemaak.setText(str(self.Game.GetNumberWordsChosen()))
        woordeGekies = self.Game.GetCurrentWordsCompleted()
        self.ui.textEditWoordLys.clear()
        for word in woordeGekies:
            someWord = str(word).replace('\n','')
            self.ui.textEditWoordLys.append(someWord)
        self.ui.lineEditKiesWoord.setFocus(True)
            
    def GameSetup(self):
        self.RoundUpdate()
        ScrambledNineLetterWord = []
        ScrambledNineLetterWord = self.Game.GetNineLetterWordScrambled()     
        self.ui.lineNommerRaaiselsKlaar.setText(str(self.Game.GetNumber9LCompleted()))
        self.ui.lineNommerWoordeGemaak.setText(str(self.Game.GetNumberWordsChosen()))
        self.ui.lineMoontlikeWoorde.setText(str(self.Game.GetCurrentNumberPossibleWords()))
        self.ui.label_1_1.setText(str(ScrambledNineLetterWord[0]))
        self.ui.label_1_2.setText(str(ScrambledNineLetterWord[1]))
        self.ui.label_1_3.setText(str(ScrambledNineLetterWord[2]))
        self.ui.label_2_1.setText(str(ScrambledNineLetterWord[3]))
        self.ui.label_2_2.setText(str(ScrambledNineLetterWord[8]))
        self.ui.label_2_3.setText(str(ScrambledNineLetterWord[5]))
        self.ui.label_3_1.setText(str(ScrambledNineLetterWord[6]))
        self.ui.label_3_2.setText(str(ScrambledNineLetterWord[7]))
        self.ui.label_3_3.setText(str(ScrambledNineLetterWord[4]))

        
        
        
        
        

class VerkeerdeWoord(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = VerkeerdeWoordDialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ProbeerWeer)
        

    def ProbeerWeer(self):
        self.reject()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
