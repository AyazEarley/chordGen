import random
transitionTable = {
    'I' : {"V6": 15, "V64 I6": 5, "V": 10,
           "IV": 20, "IV64 I" : 5, "IV6": 5,
            "ii" : 10, "ii6" : 10,
            "vi" : 10,
            "iii" : 3, "iii64 iv6": 1, "iii64 vi" : 1},
    'I6' : {"V64 I" : 5, "V": 10,
            "IV": 45,
            "ii": 10, "ii6": 25,
            "vii06 + I": 5},
    
    'ii' : {"V" : 90, "I6 ii6" : 10},
    'ii6' : {"V" : 90, "I6 ii" : 10},

    'iii': {"IV" : 80, "vi" : 20},

    'IV' : {"I" : 20, "I6" : 20, "V" : 40, "ii" : 15, "ii6" : 5},
    'IV6' : {"I" : 10, "V" : 40, "V6": 30, "ii6" : 15, "ii": 5},

    'V' : {"I" : 80, "I6": 10, "vi" : 10},
    'V6' : {"I" : 100},

    'vi' : {"IV" : 30, "ii" : 50, "I": 5, "V": 15 }
    

}

numChords = 5
chords = "I"
for i in range(numChords + 1):
    previous = chords.split()[-1]
    options = transitionTable[previous]
    next = random.choices(list(options.keys()), weights = list(options.values()))[0]
    chords += " " + next

print(chords)



