Public Key Encryption & Prime Factorization

Public Key Encryption is a de facto standard used in internet based communication. Without which remote working, online shopping, online banking, even social media postings would not be possible. It solved the biggest hurdle in secure communication – that of sharing the encryption key between the two parties before they could begin to communicate in a secure manner. Now, the proverbial Bob & Alice, could start communicating without having to establish an encryption key. 

Some time back I read a book by the name ‘The Code Book’ written by Siman Sing. Siman is a British mathematician & author of Indian descent. He has written books on mathematics, in a language that a non-mathematician can also understand and enjoy. One such book is ‘The Code Book’.

‘The Code Book’ is about human being’s quest to communicate in coded language and equally earnest pursuit by other humans to de-code others coded communication. Book describes, in very entertaining way, history of ‘encryption’ and ‘decryption’ starting from ancient times to current latest & greatest form of encryption — Public Key Cryptography. Siman tells about how Mary the Queen of Scots was sent to gallows because the encrypted messages she was sending to her collaborators were actually decrypted by Queen Elizabeth’s spymaster and these were then used against her as evidence for treason. All the significant happenings in the world of cryptography — substitution ciphers, frequency analysis, Vigenère Cipher, Enigma machine etc. are described in a delightful way, without getting into too much technicalities.

Towards the end of the book , off course, are the chapters on Public Key Cryptography (PKC henceforth) & Pretty Good Privacy. The biggest hurdle in the 2000 year odd history of sending secret messages was the problem of key exchange. Before Bob & Alice could initiate sending secret message they first had to come together and agree upon the encoding key, as the same will be used by both parties for encoding as well as decoding the messages. PKC solved this problem by some clever mathematical devices like prime factorization and circular mathematics. What I understood from the book was, though there is some complicated mathematics involved, at the base of PKC is an observation that it is extremely hard to find prime factors of a large composite number.

This observation kept intriguing me and now when I got some free time from my 9 to 6 job, I started to devote some time to find a method to do this factorization. As a result of this effort, I have devised an algorithm to find prime factors of a composite number which is multiplication of two prime numbers. It is not a general purpose factorization algorithm but one for a specific use case – that of factoring a composite number that is a product of two primes which are of almost equal length. It is actually elementary mathematic, one which we learn in middle school, back when even calculators weren’t allowed in school, leave alone iPad.
This is how we were taught to multiply two large numbers :
 
![image](https://github.com/user-attachments/assets/dc10cbbd-36cb-4b2c-883c-1412b0f0175c)


If we are multiplying 2153 by 2897 then first we multiply by 7 (the least significant number of the multiplier) to 2153. Then leave least significant place blank and multiply by 9 (the next digit after 7) to 2153. Then leave two least significant places blank and multiply by 8 to 2153. We go on like this till we reach most significant digit of multiplier ie 2 of 2897 in this example. Finally add the numbers to get the product.

Now, what we need is opposite of this ie we are given the product viz. 6237241 and need to find out factors viz. 2153 & 2897. So to get 1 (the last digit of our composite number) last digits of two prime factors need to be either [1,1] or [3,7] or [9,9]. Note that all prime numbers, except 2, are odd numbers, so they must have last digit as either of 1,3,7 or 9 (5 although odd , no prime number can be ending with 5). 

Moving on, to get last two digits of product , 41 in this example, we try [0-9]1 and [0-9]1 and get 10 possible pairs. Also try [0-9]3 and [0-9]7 and get another 10 possible pairs. Continuing in this manner towards left we will get our two prime factors.

I converted this algorithm into python code and have tested it on large composite number up to 21 digits (prime factors of which were of 10 digits, near to 10 billion). 
Theoretically, this algorithm can find factors for any composite number, regardless of its size. Practically, I run into disk size problem and also run time goes on increasing exponentially. Note that I am running on my home laptop and not on a powerful server.

Then I tried another implementation of this algorithm – one using recursion. This is a perfect use case for recursive program as same logic of finding possible factors is to be repeated as we move from left to right on the composite number. But in this implementation I run into what I think is limitation of Python. At one point in logic I need Python to clear entire call stack from past recursive calls and restart a new. But to the best of my research Python does not allow to do that.

I have uploaded both versions of program on github (solcrypto65/PrimeFacts (github.com)) public repository. I now invite the expert Python programmers to give it a try. Some of the things to try , which I did not have skills to do, is using multi threading, multi processing features of Python on more powerful machine.

