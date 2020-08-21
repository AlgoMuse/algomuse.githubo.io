---
layout: default
title: Number theory
nav_order: 8
---


# Number theory


1. TOC
{:toc}



## (Ir)rationality


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
\\(\sqrt{3}\sqrt{7}\quad\quad\\) | Square the above number and remove the integer part.|


But we know that \\(\sqrt{21}\\) is not rational and hence a contradiction.

---

### Irrational fraction
{: .d-inline-block}

A3, 2012
{: .label }

Prove that \\(\frac{\ln (12)}{\ln (18)}\\) is irrational.


#### Solution

We know that \\(\frac{\ln (12)}{\ln (18)}=\log_{18}(12) .\\) Suppose this is rational, say \\(=\frac{a}{b}\\) where \\(a, b\\) are integers with \\(b \neq 0\\).
Then \\(18^{\frac{a}{b}}=12,\\) so \\(18^{a}=12^{b} .\\) By factoring into primes this gives \\(3^{2 a} 2^{a}=3^{b} 2^{2 b},\\) which by unique factorization can happen only if \\(2 a=b\\) and \\(a=2 b\\). But this gives \\(a=b=0\\), a contradiction.


---

### Summations
{: .d-inline-block}

A1, 2014
{: .label}

<p>
Let \(\alpha, \beta\) and \(c\) be positive numbers less than \(1,\) with \(c\) rational and \(\alpha, \beta\) irrational.
</p>

<p>
(a) The number \(\alpha+\beta\) must be irrational.
</p>

<p>
(b) The infinite sum \(\sum_{i=0}^{\infty} \alpha c^{i}=\alpha+\alpha c+\alpha c^{2}+\cdots\) must be irrational.
</p>

<p>
(c) The value of the integral \(\int_{0}^{\pi}(\beta \cos x+c) d x\) must be irrational.
</p>

Sol.

<p>
False-True-True
</p>

---

### A polynomial integer
{: .d-inline-block}

B2, 2014
{: .label}

<p>
Let \(x\) be a real number such that \(x^{2014}-x^{2004}\) and \(x^{2009}-x^{2004}\) are both integers. Show that \(x\) is an integer. <br>

Hint: it may be useful to first prove that \(x\) is rational.
</p>


Sol.

<p>
Here is one of several possible ways. \(x^{2014}-x^{2009}=x^{2009}\left(x^{5}-1\right)\) and \(x^{2004}\left(x^{5}-1\right)\) are integers, which we may assume to be nonzero (else \(x=0\) or 1 and we are done). Dividing, we get that \(x^{5}\) is rational. Now dividing the integer \(x^{2004}\left(x^{5}-1\right)\) by the rational number \(x^{5}-1,\) we see that \(x^{2004}\) is rational. since 2004 and 5 are coprime, \(x\) is rational as well. (E.g., \(x^{5}\) is rational, so \(\left(x^{5}\right)^{401}=x^{2005}\) is rational. Now divide by the rational number \(x^{2004}\).)
Let \(x=\frac{a}{b}\) with \(a, b\) coprime integers.
</p>

<p>
Consider the integer \(\displaystyle \frac{a^{2000}}{b^{2009}}-\frac{a^{2004}}{b^{2004}}=\frac{a^{2009}-b^{5} a^{2004}}{b^{2000}}\).
If a prime \(p\) divides the denominator, it must divide the numerator as well.
</p>

<p>
Now \(p \mid b,\) so \(p \mid b^{5} a^{2004},\) so \(p \mid a^{2009}\) and finally \(p \mid a,\) a contradiction. Thus \(b=1,\) i.e., \(x\) is an integer.
</p>



---


## Divisibility

### Numbers of the form \\(a^2-b^2\\)
{: .d-inline-block}


A5, 2018
{: .label}

<p>List in increasing order all positive integers \(n \leq 40\) such that \(n\) cannot be written in the form \(a^{2}-b^{2},\) where \(a\) and \(b\) are positive integers.
</p>


Sol.

<p> 1,4 and all even number s of the form \(4 k+2\).</p>

---

### Fermat's little theorem
{:b .d-inline-block}

A5, 2010
{: .label .label-blue}

<p>
Find the remainder given by \(3^{89} \times 7^{86}\) when divided by 17.
</p>

Sol.

<p>
The usual trick is to try to get numbers that are 1,-1 modulo the divisor. In this case, \(16\equiv -1 \mod 17\). We cannot get 16 directly but notice
that \( 21 \equiv 4 \mod 17 \), which we can get.
</p>

<p>
\(3^{89} 7^{86} \equiv 3^{3}(3 \cdot 7)^{86} \equiv 27 \cdot 4^{86} \equiv 10\left(4^{2}\right)^{43} \equiv 10(-1)^{43} \equiv-10 \equiv 7\)
</p>


---

### Is a square?
{: .d-inline-block}

A6, 2019
{: label .label-blue}

For what values of \\( n \\) is \\( n^6 + n^4 + 1 \\) a square of a natural number?


#### Solution

We will handle odd and even cases separately.

*Lemma.* Every odd square is \\(1 \bmod 8\\).

\\[ (2k+1)^2=4k^2+4k+1=4(k^2+k)+1 \\]

Since \\( 4(k^2+k) \\) is divisible by 8, the lemma follows. \\(\square\\)

*Case 1.* If \\(n\\) is odd, then the given expression \\(S:=n^6+n^4+1\\) cannot be a square since \\(S\equiv 3\pmod 8\\). Hence \\(n\\) is not odd.

*Case 2.* If \\(n=2\\), we have \\(S=81\\), so we have one solution. If \\(n>2\\) and is even we have:

\\[ \left(n^3+\frac{n}{2}\right)^2=n^6+n^4+\frac{n^2}{4}> S > n^6+n^4-2n^3+\frac{n^2}{4}-n+1=\left(n^3+\frac{n}{2}-1\right)^2 \\]

\\( S \\) is a number strictly inbetween two consecutive squares, so there are no solutions for \\(n>2\\).

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



### Primes in an algebraic equation
{: .d-inline-block}

B6, 2016
{: .label}

<p>
Find all pairs \((p, n)\) of positive integers where \(p\) is a prime number and \(p^{3}-p=n^{7}-n^{3}\)
</p>

Sol.


<p>
The given equation is \(p(p-1)(p+1)=n^{3}\left(n^{2}+1\right)(n+1)(n-1) .\) As the factor \(p\) on the LHS is a prime, it must divide one of the factors \(n-1, n, n+1, n^{2}+1\) on the RHS.
</p>

<p>
<i>Key lemma.</i> \(p>n^{2}\)<br>
</p>

<p>
<i>Proof</i> The LHS \(=p^{3}-p\) is an increasing function of \(p\) for \(p \geq 1,\) e.g. because the derivative \(3 p^{2}-1\) is positive.
So for any given \(n \geq 1\), there is exactly one real value of \(p\) for which LHS=RHS.
Trying \(p=n^{2}\) gives LHS\(=n^{6}-n^{2}< n^{7}-n^{3}=\)RHS. This is because \(n^{7}-n^{3}-\left(n^{6}-n^{2}\right)=\left(n^{6}-n^{2}\right)(n-1)>0\). \(\,\square\)
</p>



<p>
As the prime \(p\) is greater than \(n^{2},\) it cannot divide any of \(n-1, n, n+1 .\) So \(p\) must divide \(n^{2}+1\) and therefore we must have \(p=n^{2}+1,\) again because \(p>n^{2} .\) Substituting this in the given equation, we get \(\left(n^{2}+1\right) n^{2}\left(n^{2}+2\right)=n^{3}\left(n^{2}+1\right)(n+1)(n-1)\). Canceling common factors gives \(n^{2}+2=n^{3}-n,\) i.e. \(2=n^{3}-n^{2}-n .\) This has a unique integer solution \(n=2,\) e.g. because the factor \(n\) on the RHS must divide 2 and now one checks that \(n=2\) works. So \(n=2\) and the prime \(p=n^{2}+1=5\) give a unique solution to the given equation.
</p>


---


## Unique prime factorization


### Six consecutive numbers
{:b .d-inline-block}

B3, 2011
{: .label }

Prove that there are infinitely many perfect squares that can be written as a sum of six consecutive natural numbers. Find the smallest such square.

#### Solution

The sum of six consecutive numbers is of the form:

\\[ \frac{(n+6)(n+7)}{2} - \frac{n(n+1)}{2} \text{ for some } n\\]


The above expression simplifies to \\(3(2n+7)\\). This number is a perfect square whenever \\(2n+7=3k^2\\). Any odd number greater than one can be substituted for \\(k\\). The smallest value of \\(k\\) is 3, so the smallest such square is 81.

\\[ 81 = 11+12+\cdots+16 \\]

---

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

### Number of divisors
{: .d-inline-block}

A1, 2019
{: label .label-blue}


For a natural number \\(m,\\) define \\(\Phi_{1}(m)\\) to be the number of divisors of \\(m\\) and for \\(k \geq 2\\) define \\(\Phi_{k}(m):=\Phi_{1}\left(\Phi_{k-1}(m)\right) .\\) For example, \\(\Phi_{2}(12)=\Phi_{1}(6)=4 .\\) Find the minimum \\(k\\) such that

\\[ \Phi_{k}\left(2019^{2019}\right)=2 \\]


<details markdown="1">

<summary>Solution</summary>

A number \\(n\\) that has prime factorizaton \\( p_1^{k_1} p_2^{k_2}\ldots p_t^{k_t} \\) has \\( (k_1+1)(k_2+1)\ldots(k_t+1) \\) divisors.


|Iteration | Number | Factorization | Result
|:------|:------|:----------|:------
1 | \\(2019^{2019}\\) | \\(3^{2019}\cdot 673^{2019}\\)  |  \\(2020^2 \\)
2 | \\(2020^2     \\) | \\(2^4\cdot 5^2\cdot 101^2 \\)  |  \\(45 \\)
3 | \\(45         \\) | \\(3^2\cdot 5              \\)  |  \\(6 \\)
4 | \\(6          \\) | \\(3\cdot 2                \\)  |  \\(4 \\)
5 | \\(4          \\) | \\(2^2                     \\)  |  \\(3 \\)
6 | \\(3          \\) | \\(3                       \\)  |  \\(2 \\)



*Comment. A bit tedious task for a first problem. Is there a simpler way?*

</details>




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


---

### When is \\(a^2-a\\) divisible by 10000?
{: .d-inline-block}

B3, 2015
{: .label }

<p>
(a) Show that there are exactly 2 numbers \(a\) in \(\{2,3, \ldots, 9999\}\) for which \(a^{2}-a\) is divisible by \(10000 .\) Find these values of \(a\).
</p>

<p>
(b) Let \(n\) be a positive integer. For how many numbers \(a\) in \(\left\{2,3, \ldots, n^{2}-1\right\}\) is \(a^{2}-a\) divisible by \(n^{2} ?\) State your answer suitably in terms of \(n\) and justify.
</p>

Sol.

<p>
(a) We have \(10000=16 \times 625\) as product of prime powers. Recall the notation \(a \mid b,\) meaning \(b\) is divisible by a. We have \(10000 \mid a^{2}-a\) if and only if \((625 \mid a(a-1)\) and \(16 \mid a(a-1)) .\) Because \(a\) and \(a-1\) cannot share a factor, in turn this is equivalent to having both the conditions \((1) 625 \mid a\) or \(625 \mid a-1\) AND
(2) \(16 \mid a\) or \(16 \mid a-1 .\) Now if the coprime integers 16 and 625 both divide the same natural number (in our case \(a\) or \(a-1),\) their product 10000 will also divide this number. In our case this would force \(a=0,1,\) or \(\geq 10000,\) all of which are not allowed. Thus the given requirement on \(a\) is equivalent to having either (1) \(16 \mid a\) and \(625 \mid a-1\) OR
(2) \(16 \mid a-1\) and \(625 \mid\) a. Each case has a unique solution, respectively \(a=9376\) and \(a=625\) (e.g. use modular arithmetic:
in case \(1,\) we have \(a=625 k+1,\) which is \(k+1\) mod \(16,\) forcing \(k=15\) because \(16 \mid a\) and \(a \in\{2,3, \ldots, 9999\})\)
</p>

<p>
(b) Let \(n=p_{1}{ }^{e_{1}} \ldots p_{k}{ }^{e_{k}}\) be the factorization of \(n\) into powers of distinct primes. The analysis in part (a) tells that required values of \(a\) are obtained as follows: write \(n^{2}=x y\) as a product of two coprime integers and find values of \(a\) in \(\left\{2,3, \ldots, n^{2}-1\right\}\) that are simultaneously 0 mod \(x\) and 1 mod \(y\). These are precisely the values of \(a\) that we want. This is because each \(p_{i}^{2 e_{i}}\) must divide \(a\) or \(a-1,\) as \(a\) and \(a-1\) are coprime.


Now the Chinese remainder theorem tells you that there is always an \(a\) that is 0 mod \(x\) and 1 mod \(y\). Moreover it is unique modulo \(x y=n^{2}\) because difference between any two solutions would be divisible by \(x y\).

The total number of ways to write \(n^{2}=x y\) as a product of coprime integers is exactly \(2^{k}\) as it amounts to choosing which of the \(k\) distinct primes to include in \(x\) and then the rest go into \(y\). (Notice that \(x\) and \(y\) are not interchangeable.) However, we have to delete the two cases \(x=1, y=n^{2}\) and \(y=1, x=n^{2},\) as these will respectively lead to solutions \(a=1\) and \(a=0\) or \(n^{2},\) which are not in \(\left\{2,3, \ldots, n^{2}-1\right\} .\) Finally it is easy to see that different choices of \(x\) lead to different values of \(a\). This is because, of the primes \(p_{1}, \ldots, p_{k}\) in the factorization of \(n,\) precisely the ones dividing \(x\) will divide \(a\) and the remaining primes will not, because they divide \(a-1\).

Thus the final answer is \(2^{k}-2 .\) Note that this matches with the special case in part (a). Finally, note that there was nothing special about taking a square: instead of \(n^{2}\) it could be any positive integer \(m\) and we would proceed the same way to find requisite integers \(a\) in \(\{2,3 \ldots, m-1\}\) based on prime factorization of \(m\)
</p>

---




## GCD

### Euclidean algorithm
{: .d-inline-block}

B5, 2015
{: .label}


<p>For an arbitrary integer \(n,\) let \(g(n)\) be the \(G C D\) of \(2 n+9\) and \(6 n^{2}+11 n-2 \).
What is the largest positive integer that can be obtained as the value of \(g(n) ?\) If \(g(n)\) can be arbitrarily large,
state so explicitly and prove it.
</p>

Sol.
<p>
Long division gives \(6 n^{2}+11 n-2=(2 n+9)(3 n-8)+70 .\) By Euclidean algorithm, \(G C D\left(6 n^{2}+11 n-2,2 n+9\right)=G C D(2 n+9,70) .\) Thus \(g(n)\) divides \(70 .\) But since \(g(n)\) divides \(2 n+9,\) which is odd, \(g(n)\) divides \(35 .\) When \(n=13,2 n+9=35\) and hence \(g(13)=35 .\) Thus the maximum value of \(g(n)\) is \(35 .\)
</p>


---



### Totient function
{: .d-inline-block}

A3, 2016
{: .label}

<p>
Let \(\phi(n)\) denote the number of positive integers less than \(n\) that are relatively prime to \(n\).
In other words, \(\phi(n)\) counts all \(m\) such that
\(\operatorname{gcd}(m, n)=1\).


</p>


<p>
The number \(n=110179\) is a product of two primes \(p\) and \(q\).
We also know that \(\phi(n) = 109480.\)
</p>

<p>
Find the values of \(p\) and \(q\).
</p>

Sol.

<p>
Given \(n=p q=110179\). The number of integers relatively prime to \(n\) and smaller than \(n\) is \((p-1)(q-1) .\) So we have \(p q-p-q+1=109480 .\) We get \(p+q=700 .\) Now \(p, q\) are solutions to the quadratic \(x^{2}-700 x+110179\).
</p>

<p>
The discriminant of this quadratic is \(\sqrt{490000-440716}=\sqrt{49284}=222\). So we get \(p=\frac{700+222}{2}=461\) and \(q=\frac{700-222}{2}=239\).
</p>

---


### GCD application
{: .d-inline-block}

A7, 2016
{: .label}


<p>
We want to construct a nonempty and proper subset \(S\) of the set of non-negative integers. This set must have the following properties. For any \(m\) and any \(n\)
if \(m \in S\) and \(n \in S\) then \(m+n \in S \quad\) and if \(m \in S\) and \(m+n \in S\) then \(n \in S\)
</p>

<p>(i) 0 must be in \(S\).</p>
<p>(ii) 1 cannot be in \(S\).</p>
<p>(iii) There are only finitely many ways to construct such a subset \(S\).</p>
<p>(iv) There is such a subset \(S\) that contains both \(2015^{2016}\) and \(2016^{2015}\).</p>


Sol.

<p>TTFF</p>


<p>
Since the set \(S\) is nonempty, there is an element \(m \in S\).
But then \(m=m+0\) and so \(0 \in S\). <br>
1 cannot be in \(S,\) otherwise it will contain all non-negative integers. <br>
</p>

<!-- TODO -->

<p>
By the division algorithm that if \(m, n\) are in \(S\) then so is their GCD. Therefore two coprime numbers cannot be in \(S .\) Otherwise their GCD, which is \(1,\) will be in \(S,\) a contradiction. It follows that such sets \(S\) are precisely those of the form \(n \mathbb{Z} \geq 0,\) the set of all non-negative multiples of a fixed non-negative integer \(n .\) So there are infinitely many such possible sets.
</p>

---




### Sample a divisor
{: .d-inline-block}

A4, 2017
{: .label}

<p>
Positive integers \(a\) and \(b,\) possibly equal, are chosen randomly from among the divisors of \(400 .\) The numbers \(a, b\) are chosen independently, each divisor being equally likely to be chosen. Find the probability that \(\operatorname{gcd}(a, b)=1\) and \(\operatorname{lcm}(a, b)=400\)
</p>

Sol.

<p>
\(400=5^{2} \times 2^{4}\) has \((2+1) \times(4+1)=15\) factors, so total number of pairs \((a, b)\) is \(225 .\) For \(a, b\) to be coprime, they should have no prime factor in common and then their lcm is just their product, which is required to be \(400 .\) So there are only four allowed pairs:<br>
(1,400),(400,1),(25,16) and (16,25).
</p>

<p>
The probability is \(\frac{4}{225}\).
</p>






