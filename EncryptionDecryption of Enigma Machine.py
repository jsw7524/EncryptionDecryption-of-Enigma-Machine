import sys
import math

class EnigmaMachine:
    def __init__(self):
        self.rotor0="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor1=""
        self.rotor2=""
        self.rotor3=""
                       
    def EncodeROTOR(self, rotor, offset, ch):
        i=ord(ch)-ord('A')
        return rotor[(i+offset)%26]

    def DecodeROTOR(self, rotor, offset, ch):
        for i, c in enumerate(rotor):
            if c==ch:
                return self.rotor0[(i+offset)%26]
        return "?"

    def Encode(self, data, offset):
        phrase0=[self.EncodeROTOR(self.rotor0,offset+i,c) for i,c in enumerate(data)]
        phrase1=[self.EncodeROTOR(self.rotor1,0,c) for i,c in enumerate(phrase0)]
        phrase2=[self.EncodeROTOR(self.rotor2,0,c) for i,c in enumerate(phrase1)]   
        phrase3=[self.EncodeROTOR(self.rotor3,0,c) for i,c in enumerate(phrase2)]                   
        return ''.join(phrase3)
        
    def Decode(self, data, offset):
        phrase3=[self.DecodeROTOR(self.rotor3,0,c) for i,c in enumerate(data)]
        phrase2=[self.DecodeROTOR(self.rotor2,0,c) for i,c in enumerate(phrase3)]
        phrase1=[self.DecodeROTOR(self.rotor1,0,c) for i,c in enumerate(phrase2)]
        phrase0=[self.DecodeROTOR(self.rotor0,-offset-i,c) for i,c in enumerate(phrase1)]                
        return ''.join(phrase0)



# operation = input()
# offset = int(input())
# enigma.rotor1= input()
# enigma.rotor2= input()
# enigma.rotor3= input()
# message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
enigma=EnigmaMachine()
enigma.rotor1= "BDFHJLCPRTXVZNYEIWGAKMUSQO"
enigma.rotor2= "AJDKSIRUXBLHWTMCQGZNPYFVOE"
enigma.rotor3= "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
assert "KQF"==enigma.Encode("AAA", 4)
assert "AAA"==enigma.Decode("KQF", 4)