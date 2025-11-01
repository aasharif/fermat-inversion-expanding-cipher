# Galois Field Expanding Cipher - Uses a Galois field (finite field) to
# encipher plaintext.

# Copyright (C) 2020-2025 Alexander Sharif

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.

# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see
# <https://www.gnu.org/licenses/agpl-3.0.html>.



# EXPERIMENTAL. DO NOT USE. USE `galois_cipher.py` INSTEAD.
import math

# Table class for the textual Galois field.

class Table:
    size=0
    symbols=list()
    mappedSymbols=list()
    lookupTable=list()

    # Constructor for the Galois field.
    def __init__(self,alphabet):

        # Define the symbols and the size.

        self.symbols=list(dict.fromkeys([letter for letter in alphabet]))
        self.size=len(self.symbols)

        # Check if the modulus is prime.

        for index in range(len(self.symbols)):
            if(math.gcd(index,len(self.symbols))!=1 and index > 0):
                 print("Non-prime modulus...",len(self.symbols))
                 exit()

        # Generate the symbol lookup table.

        for index in range(len(self.symbols)):
            self.mappedSymbols.append(self.symbols[pow(index,self.size-2,self.size)])
        self.lookupTable=zip(self.symbols,self.mappedSymbols)

    # TODO: Obfuscation and frequency shuffling.

    # Obfuscation functions

    def ANPA_enc(self, mess):
        Alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;: ?-!"
        NPA="Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,Juliett,Kilo,Lima,Mike,November,Oscar,Papa,Queen,Romeo,Sierra,Tango,Uniform,Victor,Whiskey,X-ray,Yankee,Zulu,Amsterdam,Baltimore,Casablanca,Danemark,Edison,Florida,Gallipoli,Havana,Italia,Jerusalem,Kilogramme,Liverpool,Madagascar,New-York,Oslo,Paris,Quebec,Roma,Santiago,Tripoli,Upsala,Valencia,Washington,Xanthippe,Yokohama,Zurich,Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Fullstop,Comma,Halfstop,Colon,Space,Qmark,Hyp,Ex"
        Alph=list(dict.fromkeys([letter for letter in Alph]))
        NPA=NPA.split(',')
        out=list()
        print(Alph,NPA)
        for letter in mess:
            out.append(NPA[Alph.index(letter)])
        return ''.join(out)

        E^(cos(sqrt(2)/2+I*sin(sqrt(2)/2)))*E^(.5+sqrt(3)/2*I)

    def ANPA_dec(self, mess):
        Alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;: ?-"
        NPA="Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,Juliett,Kilo,Lima,Mike,November,Oscar,Papa,Queen,Romeo,Sierra,Tango,Uniform,Victor,Whiskey,X-ray,Yankee,Zulu,Amsterdam,Baltimore,Casablanca,Danemark,Edison,Florida,Gallipoli,Havana,Italia,Jerusalem,Kilogramme,Liverpool,Madagascar,New-York,Oslo,Paris,Quebec,Roma,Santiago,Tripoli,Upsala,Valencia,Washington,Xanthippe,Yokohama,Zurich,Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Fullstop,Comma,Halfstop,Colon,Space,Qmark,Hyp"
        Alph=list(dict.fromkeys([letter for letter in Alph]))
        NPA=NPA.split(',')
        messa=mess
        for PAW in NPA:
            messa=messa.replace(PAW,Alph[NPA.index(PAW)],-1)
            #print(messa)
        print (messa)

    # Transliteration
    def tranlit(self,mess):
        for letter in mess:
            print()
    # Cipher function

    def dec(self, mess):
        enc=list()
        for letter in mess:
            mi=self.symbols.index(letter)
            enc.append(self.mappedSymbols[mi])
        enc=self.ANPA_dec(''.join(enc))
        print(enc)

    def enc(self, mess):
        enc=list()
        mess=self.ANPA_enc(mess)
        for letter in mess:
            mi=self.symbols.index(letter)
            enc.append(self.mappedSymbols[mi])
        print(''.join(enc))
        return (''.join(enc))

    # Print the lookup table.

    def display(self):
        print(''.join(self.symbols))
        print(''.join(self.mappedSymbols))

#a1 = Table("øπ»≤“˚ꜲꜳÆæꝎꝏŒœꜨꜩỺỻǶƕﬆﬅʤɯʫʥᵺʧʣАаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя’åß∂—∫¶•€‹›‡±∏‰◊¿ ≥!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefaaaaaaaaghijklmnopqrstuvwxyz{|}~µ∫≈≠¶¢£™®†∑∆©ƒ∞§«")
wkbs = Table("`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p[']\|}{\:\?\>\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()")
#a1.display()

wkbs.display()

m = str(input("\nEnter a message: "))

opt = str(input("\nEnter option:"))

if (opt.upper()=='E'):
    wkbs.enc(m)

if (opt.upper()=='D'):
    wkbs.dec(m)

