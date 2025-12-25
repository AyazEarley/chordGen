import random
import pygame.midi
import time
from mido import Message, MidiFile, MidiTrack

def genChords( length, mode):


    majorTable = {
        'I' : {"V6": 15, "V64 I6": 5, "V": 10,
            "IV": 20, "IV64 I" : 5, "IV6": 5,
                "ii" : 10, "ii6" : 10,
                "vi" : 10,
                "iii" : 3, "iii64 IV6": 1, "iii64 vi" : 1},
        'I6' : {"V64 I" : 5, "V": 10,
                "IV": 45,
                "ii": 10, "ii6": 25,
                "vii06 I": 5},
        
        'ii' : {"V" : 90, "I6 ii6" : 10},
        'ii6' : {"V" : 90, "I6 ii" : 10},

        'iii': {"IV" : 80, "vi" : 20},

        'IV' : {"I" : 20, "I6" : 20, "V" : 40, "ii" : 15, "ii6" : 5},
        'IV6' : {"I" : 10, "V" : 40, "V6": 30, "ii6" : 15, "ii": 5},

        'V' : {"I" : 80, "I6": 10, "vi" : 10},
        'V6' : {"I" : 100},

        'vi' : {"IV" : 30, "ii" : 50, "I": 5, "V": 15 }
    }

    minorTable = {
            'i' : {"V6": 15, "V64 i6": 5, "V": 10,
                "iv": 20, "iv64 i" : 5, "iv6": 5,
                    "iio" : 10, "iio6" : 10,
                    "VI" : 5,
                    "VII" : 5,
                    "v6" : 5},
            'i6' : {"V64 i" : 5, "V": 10,
                    "iv": 45,
                    "iio": 10, "iio6": 25,
                    "vii06 i": 5},
            
            'iio' : {"V" : 90, "i6 iio6" : 10},
            'iio6' : {"V" : 90, "i6 iio" : 10},

            'III': {"iv" : 80, "iio6" : 20},

            'iv' : {"i" : 20, "i6" : 20, "V" : 40, "iio" : 15, "iio6" : 5},
            'iv6' : {"i" : 10, "V" : 40, "V6": 30, "iio6" : 15, "iio": 5},

            'V' : {"i" : 80, "i6": 10, "VI" : 10},
            'V6' : {"i" : 100},

            'VI' : {"iv" : 30, "iio" : 50, "i": 5, "V": 15 },

            'v6' : {"iv6" : 80, "VI" : 20},
            'VII' : {"III" : 90, "VI" : 10}
            }

    numChords = length


    if mode == "major":
        transitionTable = majorTable
        chords = "I"
    else:

        transitionTable = minorTable
        chords = 'i'
    last = chords
    for i in range(numChords + 1):
        previous = chords.split()[-1]
        options = transitionTable[previous]
        next = random.choices(list(options.keys()), weights = list(options.values()))[0]
        chords += " " + next
        last = next

    while(last != 'I' and last != 'i'):
        previous = chords.split()[-1]
        options = transitionTable[previous]
        next = random.choices(list(options.keys()), weights = list(options.values()))[0]
        chords += " " + next
        last = next
    return chords




pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(2)
velocity = 127

def playChords(chords): 
    midiTable = {
        'I' : [48, 64, 67, 72],
        'I6' : [52, 60, 67, 72],
        'ii' : [50, 62, 65, 69],
        'ii6' : [53, 62, 65, 69],
        'iii' : [52, 59, 67, 71],
        'iii64' : [47, 59, 67, 71],
        'IV' : [53, 65, 69, 72],
        'IV6' : [45, 65, 69, 72],
        'IV64' : [48, 65, 69, 72],
        'V' : [55, 62, 67, 71],
        'V6' : [47, 62, 67, 71],
        'V64' : [50, 62, 67, 71],
        'vi' : [45, 64, 69, 72],
        'vii06' : [50, 62, 65, 71],

        'i' : [48, 63, 67, 72],
        'i6' : [51, 63, 67, 72],
        'iio' : [50, 62, 65, 68],
        'iio6' : [53, 62, 65, 68],
        'III' : [51, 58, 67, 70],
        'iv' : [53, 65, 68, 72],
        'iv6' : [44, 65, 68, 72],
        'iv64' : [48, 65, 68, 72],
        'VI' : [44, 63, 68, 72],
        'VII' : [46, 62, 65, 70],
        'v6' : [46, 62, 67, 70]
    }

    chords = chords.split()
    for chord in chords:
        pitches = midiTable[chord]
        for pitch in pitches:
            player.note_on(pitch, velocity)
        time.sleep(1)
        for pitch in pitches:
            player.note_off(pitch, velocity)



from mido import MidiFile, MidiTrack, Message

def writeMIDI(filename, chords):
    midiTable = {
        'I' : [48, 64, 67, 72],
        'I6' : [52, 60, 67, 72],
        'ii' : [50, 62, 65, 69],
        'ii6' : [53, 62, 65, 69],
        'iii' : [52, 59, 67, 71],
        'iii64' : [47, 59, 67, 71],
        'IV' : [53, 65, 69, 72],
        'IV6' : [45, 65, 69, 72],
        'IV64' : [48, 65, 69, 72],
        'V' : [55, 62, 67, 71],
        'V6' : [47, 62, 67, 71],
        'V64' : [50, 62, 67, 71],
        "vi" : [45, 64, 69, 72],
        "vii06" : [50, 62, 65, 71],

        'i' : [48, 63, 67, 72],
        'i6' : [51, 63, 67, 72],
        'iio' : [50, 62, 65, 68],
        'iio6' : [53, 62, 65, 68],
        'III' : [51, 58, 67, 70],
        'iv' : [53, 65, 68, 72],
        'iv6' : [44, 65, 68, 72],
        'iv64' : [48, 65, 68, 72],
        "VI" : [44, 64, 68, 72],
        "VII" : [46, 62, 65, 70],
        "v6" : [46, 62, 67, 70]
    }

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    duration = 480
    velocity = 100

    chords = chords.split()

    for chord in chords:
        pitches = midiTable[chord]

        for i, pitch in enumerate(pitches):
            track.append(Message('note_on', note=pitch, velocity=velocity, time=0))

        for i, pitch in enumerate(pitches):
            track.append(Message('note_off', note=pitch, velocity=velocity, time=duration if i == 0 else 0))

    mid.save(filename) 