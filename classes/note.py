import numpy as np
from info import freq_to_notes

class Note:
    
    def __init__(self, pitch, signal, loudness, timestamp, duration=None, typ=None):
        self.pitch = round(pitch, 3)
        self.signal = round(signal, 3)
        self.loudness = round(loudness, 3)
        self.timestamp = timestamp
        self.given_pitch = self.closest_pitch(pitch)
        
        self.duration = duration
        self.typ = typ
        
        note_info = freq_to_notes[self.given_pitch]
        self.id     = note_info["id"]
        self.note   = note_info["note"]
        self.octave = note_info["octave"]
        self.alter  = note_info["alter"]
        
    def closest_pitch(self, pitch):
        pitches = np.array(list(freq_to_notes.keys()))
        idx = (np.abs(pitches - pitch)).argmin()
        return pitches[idx]
    
    def getInfo(self):
        return (self.timestamp, self.id, self.signal, self.pitch, self.given_pitch,
                self.loudness, self.note, self.octave, self.alter)
    
    def describe(self):
        note = str(self.note)
        note += ("#" if self.alter else "")
        print("\n{}, octave: {}, actual pitch: {}Hz, ideal pitch: {}Hz".format(note, self.octave, self.pitch, self.given_pitch))
        print("timestamp: {}".format(self.timestamp))
