# Fermat-Inversion-Field-Expanding-Cipher

This is a classically inspired substition cipher used to perform data encryption and decryption. The classical substitution is perfomed using a Fermat inversion on a set of symbols of prime cardinality (length). This cipher first encodes a plaintext using a set of pre-selected keywords and then substitutes each character in a given keyword for another character using Fermat inversion via Fermat's Little Theorem.

## Example Run of Encryption
```
# Table of symbols
  wkbs =  Table("""`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p[']\\|}{\\:\\?\\>\\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()""")

# Enter a message 
Enter a message: Hello

# E to encrypt or D to decrypt
Enter option: E

/JgJkJPB[CGOfJGOfJieBJ^
```

## Example Run of Decryption of the Above
```
# Table of symbols
  wkbs =  Table("""`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p[']\\|}{\\:\\?\\>\\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()""")

# Enter a message 
Enter a message: /JgJkJPB[CGOfJGOfJieBJ^

# E to encrypt or D to decrypt
Enter option: D

Hello
```
