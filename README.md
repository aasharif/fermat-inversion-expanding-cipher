# Fermat-Inversion-Expanding-Cipher

This is a classically inspired substition cipher used to perform data encryption and decryption. The classical substitution is performed using a Fermat inversion on a set of symbols of prime cardinality (length). This cipher first encodes a plaintext using a set of pre-selected keywords and then substitutes each character in a given keyword for another character using Fermat inversion via Fermat's Little Theorem.

The particular mapping for the Fermat inversion is as follows (note $`p-2`$ is used and not $`p-1`$ due to 0-based indexing):

$`i^{(p-2)} \equiv p`$

Where $`i`$ is the index of the character in the set of prime length $`p`$.

Therefore, this creates a bijection from the symbol set $`S`$ to itself:

$`S_m \mapsto S_k`$ and $`S_k \mapsto S_m`$ where $`m`$ and $`k`$ are index varaibles and $`m \ne k`$  

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
