import sys
import random
class ReworkedList():
    m_Dictionary = []
    m_allpossibleWords = []
    m_allnineletterWords = []
    m_currentPossibleWords = []
    m_nineLetterWordsCompleted = []
    m_currentWordsCompleted = []
    m_currentNineLetterWord = ""
    m_currentnineLettersScrambled = ""
    m_number9LWordsCompleted = 0
    m_currentNumberWordsChosen = 0
    m_currentNumberPossibleWords = 0
    m_updateVariables = True
    
    def GetNineLetterWordCompleted(self):
        return self.m_nineLetterWordsCompleted
    def GetNumber9LCompleted(self):
        return self.m_number9LWordsCompleted
    def GetNineLetterWord(self):
        return self.m_currentNineLetterWord
    def GetNineLetterWordScrambled(self):
        return self.m_currentnineLettersScrambled
    def GetCurrentWordsCompleted(self):
        return self.m_currentWordsCompleted
    def GetNumberWordsChosen(self):
        return self.m_currentNumberWordsChosen
    def GetCurrentNumberPossibleWords(self):
        return self.m_currentNumberPossibleWords
    def GetPossibleWords(self):
        return self.m_currentPossibleWords
    def SetupVariables(self):
        f = open('afrwde.txt', 'r')
        lines = f.readlines()
        for line in lines:
            self.m_Dictionary.append(line)
        f.close()
        for word in self.m_Dictionary:
            if len(word) >= 5 and len(word) <= 10:
                self.m_allpossibleWords.append(word)
        for word in self.m_allpossibleWords:
            if len(word) == 10:
                self.m_allnineletterWords.append(word)
    def ChooseNineLetterWord(self):
        rightWord = False
        count = 0
        f = open('NineLetterWords','a')
        i = 0
        while (rightWord!=True):
            rightWord = True
            count = 0
            self.m_currentNineLetterWord = random.choice(self.m_allnineletterWords)
            for word in self.m_allpossibleWords:
                if(self.WordIsInList(word,self.m_currentNineLetterWord)):
                    count += 1
                if(count > 50):
                    rightWord = False
                    break
            self.m_allnineletterWords.remove(self.m_currentNineLetterWord)
            if rightWord == True:
                f.write(str(self.m_currentNineLetterWord)+'\n')
            if(len(self.m_allnineletterWords)==0):
                break
        f.close()
    def ScrambleNineLetterWord(self,num=8):
        numLetters1 = 0
        numLetters2 = 0
        numLetters3 = 0
        numLetters4 = 0
        numLetters5 = 0
        numLetters6 = 0
        numLetters7 = 0
        numLetters8 = 0
        numLetters9 = 0
        listNumLetters = [numLetters1, numLetters2, numLetters3, numLetters4, numLetters5, numLetters6, numLetters7, numLetters8, numLetters9]
        i = 0 
        for word in self.m_allpossibleWords:  
            for i in range(len(self.m_currentNineLetterWord)):        
                if self.m_currentNineLetterWord[i] in word:
                    if i == 0:
                        numLetters1 += 1
                    if i == 1:
                        numLetters2 += 1
                    if i == 2:
                        numLetters3 += 1
                    if i == 3:
                        numLetters4 += 1
                    if i == 4:
                        numLetters5 += 1
                    if i == 5:
                        numLetters6 += 1
                    if i == 6:
                        numLetters7 += 1
                    if i == 7:
                        numLetters8 += 1
                    if i == 8:
                        numLetters9 += 1
        listDict = {"Letter0":numLetters1,"Letter1":numLetters2,"Letter2":numLetters3,
                    "Letter3":numLetters4,"Letter4":numLetters5,"Letter5":numLetters6,
                    "Letter6":numLetters7,"Letter7":numLetters8,"Letter8":numLetters9}
        sortedListDic = sorted(listDict.values())
        self.m_currentnineLettersScrambled = ""
        sortedNumbers = []
        i = 0
        moreSortedNumbers = []
        for number in sortedListDic:
            sortedNumbers.append(str(list(listDict.keys())[list(listDict.values()).index(number)]))
            listDict.pop(sortedNumbers[i])
            i += 1
        for sort in sortedNumbers:
            self.m_currentnineLettersScrambled += self.m_currentNineLetterWord[int(sort.replace("Letter",""))]
        temp = list(self.m_currentnineLettersScrambled)
        temp[num], temp[8] = temp[8], temp[num]
        for i in range(7):
            if i != 7:
                k = random.randrange(i,7)
            temp[i], temp[k] = temp[k], temp[i]
        self.m_currentnineLettersScrambled = temp
    def WordIsInList(self, word, keyWord):
        listkeyword = list(keyWord)
        listword = list(word) 
        b = True
        for x in listword:
            if x in listkeyword:
                listkeyword.remove(x)
                continue
            else:
                b = False
                break
        return b 
    def CurrentPossibleWords(self,updateVariables=False):
        if (self.m_updateVariables == updateVariables):
            self.m_Dictionary.clear()
            self.m_allpossibleWords.clear()
            f = open('afrwde.txt', 'r')
            lines = f.readlines()
            for line in lines:
                self.m_Dictionary.append(line)
            f.close()
            for word in self.m_Dictionary:
                if len(word) >= 5 and len(word) <= 10:
                    self.m_allpossibleWords.append(word)
        self.m_currentPossibleWords.clear()
        self.m_currentNumberPossibleWords = 0
        for word in self.m_allpossibleWords:
            if (self.WordIsInList(word, self.m_currentNineLetterWord)) and self.WordIsInList(str(self.m_currentnineLettersScrambled[8]),word):
                self.m_currentPossibleWords.append(word)
                self.m_currentNumberPossibleWords += 1
    def TakeWordFromPlayer(self, word):
        wordAttempt = word
        wordAttempt += '\n'
        if (wordAttempt in self.m_currentPossibleWords):
            self.m_currentWordsCompleted.append(word)
            self.m_currentPossibleWords.remove(wordAttempt)
            self.m_currentNumberWordsChosen += 1
            return True
        else:
            return False
    def FirstRound(self):

        #Code to save all the stats of previous game

        self.m_currentWordsCompleted.clear()
        self.m_currentNumberWordsChosen = 0
        self.m_currentNumberPossibleWords = 0
        self.SetupVariables()
        self.ChooseNineLetterWord()  
        self.ScrambleNineLetterWord()
        self.CurrentPossibleWords()

    def NextRound(self):
        self.m_currentWordsCompleted.clear()
        self.m_currentNumberWordsChosen = 0
        self.m_currentNumberPossibleWords = 0
        self.m_number9LWordsCompleted += 1
        self.m_nineLetterWordsCompleted.append(self.m_currentNineLetterWord)
        self.ChooseNineLetterWord()  
        self.ScrambleNineLetterWord()
        self.CurrentPossibleWords()
    
    def SkipRound(self):
        self.m_currentWordsCompleted.clear()
        self.m_currentNumberWordsChosen = 0
        self.m_currentNumberPossibleWords = 0
        self.ChooseNineLetterWord()
        self.ScrambleNineLetterWord()
        self.CurrentPossibleWords()
    def ChangeMiddleLetter(self, num=8):
        self.m_currentWordsCompleted.clear()
        self.m_currentNumberWordsChosen = 0
        self.m_currentNumberPossibleWords = 0
        self.ScrambleNineLetterWord(num)
        self.CurrentPossibleWords()   
    def ChooseOwnNineLetterWord(self,word=""):
        self.m_currentNineLetterWord = word.upper() + '\n'
        if self.m_currentNineLetterWord in self.m_nineLetterWordsCompleted:
            self.m_nineLetterWordsCompleted.remove(self.m_currentNineLetterWord)
        self.m_currentWordsCompleted.clear()
        self.m_currentPossibleWords.clear()
        self.m_currentNumberWordsChosen = 0
        self.m_currentNumberPossibleWords = 0
        self.ScrambleNineLetterWord()
        self.CurrentPossibleWords()
    def SaveGame(self):
        f = open('SaveFile.txt', 'w')
        saveList = list()
        saveList.append(self.m_currentNumberWordsChosen)
        saveList.append(self.m_currentNumberPossibleWords)
        saveList.append(self.m_number9LWordsCompleted)
        for word in saveList:
            f.write(str(word)+'\n')
        saveList.append(self.m_currentNineLetterWord)
        saveList.append(self.m_currentnineLettersScrambled)
        temp = ""
        for i in self.m_currentnineLettersScrambled:
            temp += str(i)
        f.write(str(saveList[3]))
        f.write(temp)
        f.close()
        f = open('Klaar9LWoorde.txt','w')
        for word in self.m_nineLetterWordsCompleted:
            f.write(str(word)+'\n')
        f.close()
        f = open('WoordeInLys.txt','w')
        for word in self.m_currentWordsCompleted:
            f.write(str(word)+'\n')
        f.close()
    def LoadGame(self):
        f = open('SaveFile.txt','r')
        lines = f.readlines()
        #self.m_nommerWoordeGekies = int(lines[0])
        #self.m_currentNumberPossibleWords = int(lines[1])
        self.m_number9LWordsCompleted = int(lines[2])
        self.m_currentNineLetterWord = lines[3]
        #self.m_currentNineLetterWord = self.m_negeLetterWoord.replace('\n','')
        self.m_currentnineLettersScrambled = lines[4]
        #self.m_currentnineLettersScrambled = self.m_negeLetterWoordScrambled.replace('\n','')
        f.close()
        self.m_currentNumberWordsChosen = 0
        self.m_currentWordsCompleted.clear()
        self.m_nineLetterWordsCompleted.clear()
        f = open('Klaar9LWoorde.txt','r')
        lines = f.readlines()
        for line in lines:
            self.m_nineLetterWordsCompleted.append(str(line).replace('\n',''))
        f.close()
        f = open('WoordeInLys.txt','r')
        sines = f.readlines()
        m_woordeInLys = []
        for sine in sines:
            m_woordeInLys.append(str(sine).replace('\n',''))
        f.close()
        self.CurrentPossibleWords()
        for word in m_woordeInLys:
            someWord = str(word).replace('\n','')
            self.TakeWordFromPlayer(someWord)