# What is Wiener's Attack ? 
According to wikipedia.com, the Wiener's attack, named after cryptologist Michael J. Wiener, is a type of cryptographic attack against RSA. The attack uses the continued fraction method to expose the private key d when d is small.
# How does it work ?
Note that

{\displaystyle \lambda (N)=\operatorname {lcm} (p-1,q-1)={\frac {(p-1)(q-1)}{G}}={\frac {\varphi (N)}{G}}}{\displaystyle \lambda (N)=\operatorname {lcm} (p-1,q-1)={\frac {(p-1)(q-1)}{G}}={\frac {\varphi (N)}{G}}}
where {\displaystyle G=\gcd(p-1,q-1)}G=\gcd(p-1,q-1)

Since

{\displaystyle ed\equiv 1{\pmod {\lambda (N)}}}{\displaystyle ed\equiv 1{\pmod {\lambda (N)}}},
there exists an integer K such that

{\displaystyle ed=K\times \lambda (N)+1}{\displaystyle ed=K\times \lambda (N)+1}
{\displaystyle ed={\frac {K}{G}}(p-1)(q-1)+1}ed={\frac  {K}{G}}(p-1)(q-1)+1
Defining {\displaystyle k={\frac {K}{\gcd(K,G)}}}k={\frac  {K}{\gcd(K,G)}} and {\displaystyle g={\frac {G}{\gcd(K,G)}}}g={\frac  {G}{\gcd(K,G)}}, and substituting into the above gives:

{\displaystyle ed={\frac {k}{g}}(p-1)(q-1)+1}ed={\frac  {k}{g}}(p-1)(q-1)+1.
Divided by {\displaystyle dpq}dpq:
{\displaystyle {\frac {e}{pq}}={\frac {k}{dg}}(1-\delta )}{\frac  {e}{pq}}={\frac  {k}{dg}}(1-\delta ), where {\displaystyle \delta ={\frac {p+q-1-{\frac {g}{k}}}{pq}}}\delta ={\frac  {p+q-1-{\frac  {g}{k}}}{pq}}.
So, {\displaystyle {\frac {e}{pq}}}{\frac  {e}{pq}} is slightly smaller than {\displaystyle {\frac {k}{dg}}}{\frac  {k}{dg}}, and the former is composed entirely of public information. However, a method of checking[clarification needed] and guess is still required.

By using simple algebraic manipulations and identities, a guess can be checked for accuracy.[1]
# FAQ 
If you have any questions feel free to reach out to me ! 