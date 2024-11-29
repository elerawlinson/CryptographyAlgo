<h1>Functions and Algorithms Related to Public Key Cryptography</h1>

<h2>Description</h2>
<p>Project consists of implementations of several algorithms and functions which are relevant and/or important to the mathematics of modern public key encryption.</p>

<p>The first file, modpow, computes positive and negative modular powers; this function works for numbers at a cryptographic scale. This function is utilized in encryption schemas such as D-H key establishment.</p>

<p>The second file, bsgs, is an implementation of the Giant Step Baby Step algorithm, a means of solving the DLP in O(&#8730;n).</p>

<p>The last file finds a solution x to a list of congruences.</p>

<p>MR Prime Test utilizes the Miller Rabin prime test to determine if a given number is Prime. The Miller Rabin test utilizes two featuers of prime numbers to return "Not Prime" if the number is not prime and "Prime" if the number is most likely prime. The two key features of prime moduli are that any number in the unit group a, to the power of p-1 is congruent to 1 mod p for any prime modulus p. The second feature of prime moduli is that the square root of any number congruent to 1 mod a prime modulus must be +-1.</p>



