
import sys
import random
class WorkWithList():
    m_woordeboek = []
    m_AlleMoontlikeWoorde = []
    m_moontlikeWoorde = []
    m_woordeAlGekies = []
    m_woordeInLys = []
    m_negeLetterWoord = ""
    m_negeLetterWoordScrambled = ""
    m_nommerRaaiselsKlaar = 0
    m_nommerWoordeGekies = 0
    m_nommerMoontlikeWoorde = 0
    m_maksimumLetters = 400
    m_minimumLetters = 0
    def NuweGame(self):
        self.m_woordeboek.clear()
        self.m_AlleMoontlikeWoorde.clear()
        f = open('afrwde.txt', 'r')
        lines = f.readlines()
        for line in lines:
            self.m_woordeboek.append(line)
        f.close()
        for word in self.m_woordeboek:
            if len(word) >= 5 and len(word) <= 10:
                self.m_AlleMoontlikeWoorde.append(word)
        self.m_nommerRaaiselsKlaar = 0
        self.m_nommerWoordeGekies = 0
        self.m_nommerMoontlikeWoorde = 0
        self.m_woordeInLys.clear()
        self.m_moontlikeWoorde.clear()
        self.m_woordeAlGekies.clear()
        self.KiesNegeLetterWoord()
        self.NineLettersScrammbled()
       
    def TakeWordFromPlayer(self, word):
        wordAttempt = word
        wordAttempt += '\n'

        if (wordAttempt in self.m_moontlikeWoorde):
            if (self.WordIsInList(word,self.m_negeLetterWoord)) and (word not in self.m_woordeInLys):
                self.m_woordeInLys.append(word)
                someWord = word
                someWord += '\n'
                self.m_moontlikeWoorde.remove(someWord)
                self.m_nommerWoordeGekies += 1
                return True
            else:
                return False
        else:
            return False
    def GetRaaiselsAlKlaar(self):
        return m_woordeAlGekies


    def GetWoordeAlGeKies(self):
        return self.m_woordeAlGekies
    def MoontlikeWoordeLys(self):
        self.m_woordeboek.clear()
        self.m_AlleMoontlikeWoorde.clear()
        f = open('afrwde.txt', 'r')
        lines = f.readlines()
        for line in lines:
            self.m_woordeboek.append(line)
        f.close()
        for word in self.m_woordeboek:
            if len(word) >= 5 and len(word) <= 10:
                self.m_AlleMoontlikeWoorde.append(word)
        self.m_moontlikeWoorde.clear()
        self.m_nommerMoontlikeWoorde = 0
        for word in self.m_AlleMoontlikeWoorde:
            if (self.WordIsInList(str(self.m_negeLetterWoordScrambled[8]),word)):
                if (self.WordIsInList(word, self.m_negeLetterWoord)):
                    self.m_moontlikeWoorde.append(word)
                    self.m_nommerMoontlikeWoorde += 1
    def GetScrambledNineLetter(self):
        return self.m_negeLetterWoordScrambled
    def SetMinimumWoorde(self, minimum):
        self.m_minimumLetters = minimum
    def SetMaksimumWoorde(self, maksimum):
        self.m_maksimumLetters = maksimum
    def GetNommerRaaiselsKlaar(self):
        return self.m_nommerRaaiselsKlaar
    def GetNommerWoordeGekies(self):
        return self.m_nommerWoordeGekies
    def GetNommerMoontlikeWoorde(self):
        return self.m_nommerMoontlikeWoorde
    def GetWoordeInLys(self):
        return self.m_woordeInLys
    def GetMoontlikeWoorde(self):
        return self.m_moontlikeWoorde
    def GetNegeLetterWoord(self):
        return self.m_negeLetterWoord    
    def SaveGame(self):
        f = open('SaveFile.txt', 'w')
        saveList = list()
        saveList.append(self.m_nommerWoordeGekies)
        saveList.append(self.m_nommerMoontlikeWoorde)
        saveList.append(self.m_nommerRaaiselsKlaar)
        for word in saveList:
            f.write(str(word)+'\n')
        saveList.append(self.m_negeLetterWoord)
        saveList.append(self.m_negeLetterWoordScrambled)
        f.write(saveList[3])
        f.write(saveList[4])
        f.close()
        f = open('WoordeAlGekies.txt','w')
        for word in self.m_woordeAlGekies:
            f.write(str(word)+'\n')
        f.close()
        f = open('WoordeInLys.txt','w')
        for word in self.m_woordeInLys:
            f.write(str(word)+'\n')
        f.close()

    def LaaiGame(self):
        f = open('SaveFile.txt','r')
        lines = f.readlines()
        #self.m_nommerWoordeGekies = int(lines[0])
        self.m_nommerMoontlikeWoorde = int(lines[1])
        self.m_nommerRaaiselsKlaar = int(lines[2])
        self.m_negeLetterWoord = lines[3]
        #self.m_negeLetterWoord = self.m_negeLetterWoord.replace('\n','')
        self.m_negeLetterWoordScrambled = lines[4]
        #self.m_negeLetterWoordScrambled = self.m_negeLetterWoordScrambled.replace('\n','')
        f.close()
        self.m_woordeAlGekies.clear()
        f = open('WoordeALGekies.txt','r')
        lines = f.readlines()
        for line in lines:
            self.m_woordeAlGekies.append(str(line).replace('\n',''))
        f.close()
        f = open('WoordeInLys.txt','r')
        sines = f.readlines()
        m_woordeInLys = []
        for sine in sines:
            m_woordeInLys.append(str(sine).replace('\n',''))
        f.close()
        if(len(self.m_moontlikeWoorde)==0):
            self.MoontlikeWoordeLys()
        for word in m_woordeInLys:
            someWord = str(word).replace('\n','')
            self.TakeWordFromPlayer(someWord)
            


    def NineLettersScrammbled(self):
        
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
        for word in self.m_AlleMoontlikeWoorde:
            i = 0     
            for i in range(len(self.m_negeLetterWoord)):        
                if self.m_negeLetterWoord[i] in word and (self.WordIsInList(word,self.m_negeLetterWoord)):
                    if i == 1:
                        numLetters1 += 1
                    if i == 2:
                        numLetters2 += 1
                    if i == 3:
                        numLetters3 += 1
                    if i == 4:
                        numLetters4 += 1
                    if i == 5:
                        numLetters5 += 1
                    if i == 6:
                        numLetters6 += 1
                    if i == 7:
                        numLetters7 += 1
                    if i == 8:
                        numLetters8 += 1
                    if i == 9:
                        numLetters9 += 1
        listDict = {"Letter0":numLetters1,"Letter1":numLetters2,"Letter2":numLetters3,
                    "Letter3":numLetters4,"Letter4":numLetters5,"Letter5":numLetters6,
                    "Letter6":numLetters7,"Letter7":numLetters8,"Letter8":numLetters9}
        sortedListDic = sorted(listDict.values())
        self.m_negeLetterWoordScrambled = ""
        sortedNumbers = []
        i = 0
        moreSortedNumbers = []
        for number in sortedListDic:
            sortedNumbers.append(str(list(listDict.keys())[list(listDict.values()).index(number)]))
            listDict.pop(sortedNumbers[i])
            i += 1
        for sort in sortedNumbers:
            self.m_negeLetterWoordScrambled += self.m_negeLetterWoord[int(sort.replace("Letter",""))]
        
    def KiesNegeLetterWoord(self, SomeWord=""):
        minimumWoorde = self.m_minimumLetters
        maksimumWoorde = self.m_maksimumLetters
        regteNegeLetterWoord = False
        nineLetterWord = SomeWord.upper()
        if(len(nineLetterWord)==9):
            if nineLetterWord  in self.m_woordeAlGekies:
                self.m_woordeAlGekies.remove(nineLetterWord)
            self.m_negeLetterWoord = nineLetterWord
            self.NineLettersScrammbled()
            for word in self.m_AlleMoontlikeWoorde:
                if (self.WordIsInList(word,nineLetterWord)) and self.WordIsInList(self.m_negeLetterWoordScrambled[8],word):
                    self.m_moontlikeWoorde.append(word)
                    self.m_nommerMoontlikeWoorde += 1                          
        else:
            while(regteNegeLetterWoord==False):
                nineLetterWord = random.choice(self.m_AlleMoontlikeWoorde)
                if len(nineLetterWord) == 10 and nineLetterWord not in self.m_woordeAlGekies:
                    self.m_negeLetterWoord = nineLetterWord
                    self.m_woordeAlGekies.append(self.m_negeLetterWoord)
                    self.NineLettersScrammbled() 
                    for word in self.m_AlleMoontlikeWoorde:
                        if (self.WordIsInList(word,nineLetterWord)) and self.WordIsInList(self.m_negeLetterWoordScrambled[8],word):
                            self.m_moontlikeWoorde.append(word)
                            self.m_nommerMoontlikeWoorde += 1
                            regteNegeLetterWoord = True


        """          
    def MoontlikeWoordeSpelerKanKry(self):
        for word in self.m_AlleMoontlikeWoorde:
            if (self.WordIsInList(word,self.m_negeLetterWoord)):
                self.m_nommerMoontlikeWoorde += 1
        """
    def KiesSelfWoord(self,word):
        if(len(word)==9):
            self.m_negeLetterWoord = str(word).upper()+'\n'
            self.KiesNegeLetterWoord(word)
            self.NineLettersScrammbled()
            self.MoontlikeWoordeLys()
        else:
            pass
    def NuweRondte(self):
        self.m_nommerWoordeGekies = 0
        self.m_woordeInLys.clear()
        self.m_moontlikeWoorde.clear()
        self.m_nommerRaaiselsKlaar += 1
        self.KiesNegeLetterWoord()
        self.NineLettersScrammbled()
        self.MoontlikeWoordeLys()
        if (len(self.m_negeLetterWoord)>5):
            return True
        else:
            return False

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
