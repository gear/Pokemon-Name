import urllib

def getPokemonDB(rootURL, ext):
    pkmDB = open('pkmDB', 'w')
    for i in range(1, 722):
        url = rootURL + str(i).zfill(3) + '.' + ext
        print url
        try:
            response = urllib.urlopen(url)
        except Exception:
            pkmDB.write("URL Error - ID:%d" % (i))
            continue
        src = response.read()
        response.close()
        name = src.find("&#12")
        nameend = src.find(";</td></tr>\n")
        stat = src.find("Base Stats")
        pkmDB.write("%d,%s,%s\n" % (i , src[name:nameend], src[stat+20:stat+23]))
    pkmDB.close()

def parsePokemonDB(filename='pkmDB'):
    pkmDB = open(filename, 'r')
    pkmpar = open('pkmpar2', 'w')
    pad = '00000,'
    for line in pkmDB:
        strBuffer = ''
        countComma = 0
        for char in line:
            if (char != '&' and char != '#'):
                if (char == ';' or char == ','):
                    strBuffer += ','
                    countComma += 1
                else:
                    strBuffer += char
        # 7 is fixed number of entries for each record
        while (7 - countComma) > 0 :
            la = strBuffer[:-4]
            na = strBuffer[-4:]
            strBuffer = la + pad + na;
            countComma += 1
        pkmpar.write(strBuffer)

def addClassification(filename='PokemonDB_test.arff'):
    pkmDB = open(filename, 'r')
    pkmFX = open('PokemonDB_FIX.arff', 'w')
    for line in pkmDB:
        strBuffer = ''
        isWrite = True
        for char in line:
            if (char == '?'):
                laint = int(strBuffer[-4:-1])
                if (laint >= 450):
                    strBuffer += 'strong'
                    isWrite = True
                else:
                    if (laint >= 360):
                        strBuffer += 'medium'
                        isWrite = False
                    else:
                        strBuffer += 'weak'
                        isWrite = True
            strBuffer += char
        if (isWrite):
            pkmFX.write(strBuffer)

def genNameOnly(filename='pkmDB'):
    pkmDB = open(filename, 'r')
    pkmpar = open('PokemonName', 'w')
    pad = '?,'
    for line in pkmDB:
        strBuffer = ''
        countComma = 0
        for char in line:
            if (char != '&' and char != '#'):
                if (char == ';' or char == ','):
                    if (countComma > 0):
                        strBuffer += ','
                    countComma += 1
                else:
                    if (countComma > 0):
                        strBuffer += char
        # 7 is fixed number of entries for each record
        while (7 - countComma) > 0 :
            la = strBuffer[:-4]
            na = strBuffer[-4:]
            strBuffer = la + pad + na;
            countComma += 1
        pkmpar.write(strBuffer)



'''
def createNameMatrix(filename='pkmpar'):
    pkmpar = open(filename, 'r')
    for line in pkmpar:
        cnt = 0
        for char in line:
            if (char == ','):
                cnt += 1
            else:
                if cnt == 1:

'''
