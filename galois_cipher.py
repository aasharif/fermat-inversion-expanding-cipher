# Fermat Inversion Expanding Cipher - Uses Fermat inversion
# (via Fermat's Little Theorem) to encipher plaintext.

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

"""
This program will perform a form of classical substitutive encipherment using
Fermat's Little Theorem and encoding/decoding to/from a phonetic alphabet.
"""

import math
import sys

# Table class for the textual Galois field.


class Table:
    """
    The class for the symbol table mapping.

    Attributes
    ----------
    size : int
        The length of the alphabet set used in the mapping.
    symbols : list[str]
        The symbols of the alphabet (not yet mapped).
    mapped_symbols : list[str]
        The symbols of the alphabet (mapped; they should appear shuffled).
    lookup_table: list[tuple[str, str]]
        The zip() mapping association between symbols and mapped_symbols.

    Methods
    -------
    anpa_enc(mess: str)
        Encodes the message into augmented NATO phonetic alphabet.
    anpa_dec(mess: str)
        Decodes the message from augmented NATO phonetic alphabet.
    enc(mess: str)
        Enciphers the message after calling anpa_enc() to encode.
    dec(mess: str)
        Deciphers the message after calling anpa_dec() to decode.
    display()
        Print symbols and mapped_symbols in a manner reminiscent
        of a lookup table.
    """
    size: int = int()
    symbols: list[str] = []
    mapped_symbols: list[str] = []
    lookup_table: list[tuple[str, str]] = []

    # Constructor for the Galois field.
    def __init__(self, alphabet):

        # Define the symbols and the size.
        self.symbols = list(dict.fromkeys(list(alphabet)))
        self.size = len(self.symbols)

        # Check if the length of the symbol list is prime
        # A prime modulus is required to perform the encryption
        for index in range(len(self.symbols)):

            # Check to see if the length of the symbol list
            # is co-prime to all element indices
            if (math.gcd(index, len(self.symbols)) != 1 and index > 0):
                print("Non-prime modulus...", len(self.symbols))
                sys.exit()

        # Generate the mapping of symbols for the lookup table
        for index in range(len(self.symbols)):
            self.mapped_symbols.append(
                self.symbols[pow(index, self.size-2, self.size)])

        # Zip the symbols along with the associated symbols
        self.lookup_table = zip(self.symbols, self.mapped_symbols)

    # TODO: Obfuscation and frequency shuffling.

    # Obfuscation functions
    def anpa_enc(self, mess):
        """
        Encode the message mess to an augmented NATO phonetic alphabet.

        Parameters
        ----------
        mess : str
            The message to be encoded to the phonetic alphabet.
        """
        alph = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
                "NOPQRSTUVWXYZ0123456789.,;: ?-!\"\'\\()[]<>=+/"
                )
        npa = ("Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,India,"
               "Juliett,Kilo,Lima,Mike,November,Oscar,Papa,Queen,Romeo,"
               "Sierra,Tango,Uniform,Victor,Whiskey,X-ray,Yankee,Zulu,"
               "Amsterdam,Baltimore,Casablanca,Danemark,Edison,Florida,"
               "Gallipoli,Havana,Italia,Jerusalem,Kilogramme,Liverpool,"
               "Madagascar,New-York,Oslo,Paris,Quebec,Roma,Santiago,Tripoli,"
               "Upsala,Valencia,Washington,Xanthippe,Yokohama,Zurich,Zero,One,"
               "Two,Three,Four,Five,Six,Seven,Eight,Nine,Fullstop,Comma,"
               "Halfstop,Colon,Space,Qmark,Hyp,Ex,Quotemark,Squotemark,"
               "Backslash,Lpar,Rpar,Lbrace,Rbrace,Lt,Gt,Eq,Plus,Slash"
               )
        alph = list(dict.fromkeys(list(alph)))
        npa = npa.split(',')
        out = []
        for letter in mess:
            out.append(npa[alph.index(letter)])
        return ''.join(out)

    def anpa_dec(self, mess):
        """
        Decode the message mess from an augmented NATO phonetic alphabet.

        Parameters
        ----------
        mess : str
            The message to be decoded from the phonetic alphabet.
        """
        alph = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
                "NOPQRSTUVWXYZ0123456789.,;: ?-!\"\'\\()[]<>=+/"
                )
        npa = ("Alfa,Bravo,Charlie,Delta,Echo,Foxtrot,Golf,Hotel,"
               "India,Juliett,Kilo,Lima,Mike,November,Oscar,Papa,"
               "Queen,Romeo,Sierra,Tango,Uniform,Victor,Whiskey,"
               "X-ray,Yankee,Zulu,Amsterdam,Baltimore,Casablanca,"
               "Danemark,Edison,Florida,Gallipoli,Havana,Italia,"
               "Jerusalem,Kilogramme,Liverpool,Madagascar,New-York,Oslo,"
               "Paris,Quebec,Roma,Santiago,Tripoli,Upsala,Valencia,Washington,"
               "Xanthippe,Yokohama,Zurich,Zero,One,Two,Three,"
               "Four,Five,Six,Seven,Eight,Nine,Fullstop,Comma,"
               "Halfstop,Colon,Space,Qmark,Hyp,Ex,Quotemark,"
               "Squotemark,Backslash,Lpar,Rpar,Lbrace,Rbrace,Lt,Gt,"
               "Eq,Plus,Slash")
        alph = list(dict.fromkeys(list(alph)))
        npa = npa.split(',')
        message = mess
        for paw in npa:
            message = message.replace(paw, alph[npa.index(paw)], -1)
        return ''.join(message)

    # Decryption function
    def dec(self, mess):
        """
        Decipher the original message.

        Parameters
        ----------
        mess : str
            The message to be deciphered.
        """
        dec = []
        for letter in mess:
            message_index = self.symbols.index(letter)
            dec.append(self.mapped_symbols[message_index])
        dec = self.anpa_dec(''.join(dec))
        print(dec)

    # Encrypt function
    def enc(self, mess):
        """
        Encipher the original message.

        Parameters
        ----------
        mess : str
            The message to be enciphered.
        """
        enc = []
        mess = self.anpa_enc(mess)
        for letter in mess:
            message_index = self.symbols.index(letter)
            enc.append(self.mapped_symbols[message_index])
        print(''.join(enc))
        return ''.join(enc)

    # Print the lookup table.
    def display(self):
        """
        Print the symbols and the mapped symbols in a manner
        reminiscent of a lookup table.
        """
        print(''.join(self.symbols))
        print(''.join(self.mapped_symbols))


# Generate a lookup table for the following alphabet
wkbs = Table(
    ("`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p["
     "']\\|}{\\:\\?\\>\\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()"))

# Get the message to be operated upon
MESSAGE = str(input("\nEnter a message: "))

# Choose an option to perform (encipher or decipher)
OPT = str(input("\nEnter option: "))

# Newline to separate text
print()

if OPT.upper() == 'E':
    wkbs.enc(MESSAGE)

if OPT.upper() == 'D':
    wkbs.dec(MESSAGE)
