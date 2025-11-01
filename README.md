# Galois-Field-Expanding-Cipher

This is a classically inspired substition cipher used to perform data encryption and decryption. The classical substitution is perfomed using a Galois field (alternatively known as a finite field). This cipher first encodes a plaintext using a set of keywords and then substitutes each character for another character using modular exponentiation inverses over a finite field.

## Example Run of Encryption
```python
# Table of symbols
  wkbs =  Table("""`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p[']\\|}{\\:\\?\\>\\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()""")

# Enter a message 
Enter a message: Hello

# E to encrypt or D to decrypt
Enter option: E

/JgJkJPB[CGOfJGOfJieBJ^
```

## Example Run of Decryption of the Above
```python
# Table of symbols
  wkbs =  Table("""`1234567890-=qazxswcderfvtgbnhymjuik,ol./;p[']\\|}{\\:\\?\\>\\<POIUYTREWQASDFGHJKLLK<MNBVCXZ~!@#%^&()""")

# Enter a message 
Enter a message: /JgJkJPB[CGOfJGOfJieBJ^

# E to encrypt or D to decrypt
Enter option: D

Hello
```
