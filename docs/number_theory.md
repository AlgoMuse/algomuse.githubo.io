---
layout: default
title: Number theory
nav_order: 8
---


# Number theory


### Rationality preserving operations
{:b .d-inline-block}

A11, 2010
{: .label .label-blue}

Using the fact that \\(\sqrt{n}\\) is an irrational number whenever \\(n\\) is not a perfect square, show that \\(S=\sqrt{3}+\sqrt{7}+\sqrt{21}\\) is irrational.

#### Solution

Our proof works by showing a series of "If x is rational so is y". Suppose the given number is rational. The the following sequence of numbers must be rational too.


|---|---|
\\(7\sqrt{3}+3\sqrt{7}+\sqrt{21}\\) | Square the given number and subtract the integer part|
\\(6\sqrt{3}+2\sqrt{7}\quad\\) | Subtract X from the above number. Since X is assumed to be rational, this number must be rational too.|
\\(\sqrt{3}\sqrt{7}\quad\quad\\) | \text{ Square the above number and remove the integer part.|


But we know that \\(\sqrt{21}\\) is not rational and hence a contradiction.

---



### Pigeon-hole principle
{:b .d-inline-block}

B1, 2010
{: .label }

Let \\(a_{1}, a_{2}, \ldots, a_{100}\\) be 100 positive integers. Show that for some \\(m, n\\) with \\(1 \leq m \leq n \leq\\) \\(100, \sum_{i=m}^{n} a_{i}\\) is divisible by 100.

#### Solution

Consider the remainders of the sequence when divided by 100. If some \\(a_k\bmod100=0\\), then \\(m=n=k\\) will work. Otherwise, the reminders are between 1 and 99 for every number.
Since there are 100 numbers, there must be two indices \\(i\\) and \\(j\\) such that \\(a_i\bmod 100=a_j\bmod 100\\). Pick \\(m=i\\) and \\(n=j\\), if \\( i < j \\).


**Try this**. Prove that there exists a number consisting of only 1s and 0s that is divisible by 3.


### Prime-factorization of squares
{:b .d-inline-block}

B3, 2011
{: .label }

Prove that there are infinitely many perfect squares that can be written as a sum of six consecutive natural numbers. Find the smallest such square.

#### Solution

The sum of six consecutive numbers is of the form:

\\[ \frac{(n+6)(n+7)}{2} - \frac{n(n+1)}{2} \text{ for some } n\\]


The above expression simplifies to \\(3(2n+7)\\). This number is a perfect square whenever \\(2n+7=3k^2\\). Any odd number greater than one can be substituted for \\(k\\). The smallest value of \\(k\\) is 3, so the smallest such square is 81.

\\[ 81 = 11+12+\cdots+16 \\]


### Two variables one equation
{: .d-inline-block}

C1, 2011
{: label .label-blue}

Show that there are exactly 16 pairs of integers \\((x,y)\\) such that
\\(11x+8y+17=xy\\).

#### Solution


An equation of the form \\(xy=ax+by+c\\) can be written as:
\\[  (x-a)(y-b) = c+ab  \\]

So the given equation is:

\\[  (x-8)(y-13) = 105  \\]

The number of solutions to the above equation is the number of divisors of 105.
We can factorize 105 as \\( 1\cdot 3\cdot 5\cdot 7\\). Every subset of these four numbers corresponds to a divisor, so there are \\(2^4=16\\) solutions.

---

### Proving irrationality
{: .d-inline-block}

A3, 2012
{: .label }

Prove that \\(\frac{\ln (12)}{\ln (18)}\\) is irrational.


#### Solution

We know that \\(\frac{\ln (12)}{\ln (18)}=\log_{18}(12) .\\) Suppose this is rational, say \\(=\frac{a}{b}\\) where \\(a, b\\) are integers with \\(b \neq 0\\).
Then \\(18^{\frac{a}{b}}=12,\\) so \\(18^{a}=12^{b} .\\) By factoring into primes this gives \\(3^{2 a} 2^{a}=3^{b} 2^{2 b},\\) which by unique factorization can happen only if \\(2 a=b\\) and \\(a=2 b\\). But this gives \\(a=b=0\\), a contradiction.


---

### Pigeon-hole on pairs
{: .d-inline-block}

A7, 2012
{: .label }

A sequence of integers \\(c_{n}\\) starts with \\(c_{0}=0\\) and satisfies \\(c_{n+2}=a c_{n+1}+b c_{n}\\) for \\(n \geq 0,\\) where \\(a\\) and \\(b\\) are integers. For any positive integer \\(k\\) with \\(g c d(k, b)=1,\\) show that \\(c_{n}\\) is divisible by \\(k\\) for infinitely many \\(n\\)


#### Solution


Consider pairs of consecutive entries of the sequence modulo \\(k,\\) i.e., \\(\left(\bar{c}\_{n}, \bar{c}\_{n+1}\right)\\), where \\(\bar{a}\\) denotes \\(a\\) modulo \\(k\\). Since there are only finitely many possibilities (namely \\(k^{2}\\) ), some pair of consecutive residues will repeat. Suppose \\(\left(\bar{c}\_{i}, \bar{c}\_{i+1}\right)=\left(\bar{c}\_{i+p}, \bar{c}\_{i+p+1}\right)\\) for some \\(i\\).
We will show that in fact the previous equation holds for all \\(i,\\) i.e., whole sequence of consecutive pairs is periodic.  This will prove in
particular that \\(\left(\bar{c}\_{0}, \bar{c}\_{1}\right)=\left(\bar{c}\_{p}, \bar{c}\_{p+1}\right)=\left(\bar{c}\_{2 p}, \bar{c}\_{2 p+1}\right)=\cdots\\)
since \\(c_{0}=0\\) is divisible by \\(k,\\) so is \\(c_{i p}\\) for all \\(i\\)
The equation \\(c_{n+2}=a c_{n+1}+b c_{n}\\) shows that \\(\bar{b} \bar{c}\_{n}=\bar{c}\_{n+2}-\bar{a} \bar{c}\_{n+1}\\).

Now \\(gcd(k, b)=1\\) means \\(b\\) is invertible modulo \\(k,\\) i.e., there is a \\(b^{\prime}\\) with \\(\overline{b b^{\prime}}=\overline{1} .\\)
Therefore \\(\bar{c}\_{n}=\bar{b}^{\prime}\left(\bar{c}\_{n+2}-\bar{a} \bar{c}\_{n+1}\right)\\)
Thus knowing a pair of consecutive residues uniquely determines the previous residue (this is why we considered pairs of residues). Therefore \\(\left(\bar{c}\_{i}, \bar{c}\_{i+1}\right)=\left(\bar{c}\_{i+p}, \bar{c}\_{i+p+1}\right)\\) implies \\(\left(\bar{c}\_{i-1}, \bar{c}\_{i}\right)=\left(\bar{c}\_{i+p-1}, \bar{c}\_{i+p}\right)\\) and (by the given recurrence) \\(\left(\bar{c}\_{i+1}, \bar{c}\_{i+2}\right)=\left(\bar{c}\_{i+p+1}, \bar{c}\_{i+p+2}\right)\\)
Thus the whole sequence \\(\left(\bar{c}\_{n}, \bar{c}\_{n+1}\right)\\) becomes periodic as soon as a single such pair repeats.

---

### Prime factorization and perfect squares again
{: .d-inline-block}

B3, 2013
{: .label }

A positive integer \\(N\\) has its first, third and fifth digits equal and its second, fourth and sixth digits equal. In other words, when written in the usual decimal system it has the form \\(x y x y x y,\\) where \\(x\\) and \\(y\\) are the digits.
 Show that \\(N\\) cannot be a perfect power, i.e., \\(N\\) cannot equal \\(a^{b},\\) where \\(a\\) and \\(b\\) are positive integers with \\(b>1\\).

#### Solution

We have:
\\[N=\left(10^{5}+10^{3}+10\right) x+\left(10^{4}+10^{2}+1\right) y=10101(10 x+y)= 3 \times 7 \times 13 \times 37 \times(10 x+y)\\]

Therefore for \\(N\\) to be a perfect power, the primes 3,7,13,37 must all occur (and in fact with equal power) as factors in the prime factorization of \\(10 x+y .\\)
In particular \\(10 x+y \geq 10101\\).  But since \\(x\\) and \\(y\\\) are digits, each is between 0 and \\(9,\\) so \\(10 x+y \leq 99\\).
So \\(N\\) cannot be a perfect power.

---

### Prime factorization and divisibility
{: .d-inline-block}

A6, 2014
{: .label }

Find the smallest \\(n\\) for which \\(\displaystyle \frac{50!}{24^n} \\) is *not* an integer.

#### Solution

The expression will not be an integer if and only if the numerator has a prime power lesser
than the corresponding power in the denominator.

We have \\( 24=2^3\cdot 3\\). Let us find the the powers of 2 and 3 in \\(50!\\).


The power of 2 is given by:
\\[  \lfloor 50/2 \rfloor + \lfloor 50/4 \rfloor + \lfloor 50/8 \rfloor + \lfloor 50/16 \rfloor + \lfloor 50/32 \rfloor = 47 \\]

The power of 3 is given by:
\\[  \lfloor 50/3 \rfloor + \lfloor 50/9 \rfloor + \lfloor 50/27 \rfloor = 22 \\]


The numerator is of the form: \\( 2^{47}3^{22}\cdot k \\). If \\(n=16\\), the denominator has \\(2^{48}\\) as a factor which is sufficient to make the number a non-integer.


<!--


2014_q1.png
![](/assets/images/number_theory/2014_q1.png)
2014_a1.png
![](/assets/images/number_theory/2014_a1.png)

---


2014_q3.png
![](/assets/images/number_theory/2014_q3.png)
2014_a3.png
![](/assets/images/number_theory/2014_a3.png)


---



2015_q1.png
![](/assets/images/number_theory/2015_q1.png)

2015_a1.png
![](/assets/images/number_theory/2015_a1.png)

---


2016_q1.png
![](/assets/images/number_theory/2016_q1.png)

2016_a1.png
![](/assets/images/number_theory/2016_a1.png)

---

2016_q2.png
![](/assets/images/number_theory/2016_q2.png)

2016_a2.png
![](/assets/images/number_theory/2016_a2.png)

---

2016_q3.png
![](/assets/images/number_theory/2016_q3.png)

2016_a3.png
![](/assets/images/number_theory/2016_a3.png)


---

2017_q1.png
![](/assets/images/number_theory/2017_q1.png)

2017_a1.png
![](/assets/images/number_theory/2017_a1.png)

---


2018_q1.png
![](/assets/images/number_theory/2018_q1.png)

2018_a1.png
![](/assets/images/number_theory/2018_a1.png)

---

2019_q1.png
![](/assets/images/number_theory/2019_q1.png)

2019_a1.png
![](/assets/images/number_theory/2019_a1.png)

---

2019_q2.png
![](/assets/images/number_theory/2019_q2.png)

2019_a2.png
![](/assets/images/number_theory/2019_a2.png)


-->






