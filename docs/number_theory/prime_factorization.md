---
layout: default
title: Prime factorization
parent: Number theory
nav_order: 4
---


## Prime factorization
{: .no_toc  }


#### Problems
{: .no_toc  }

1. TOC
{:toc}

---


### Six consecutive numbers
{:b .d-inline-block}

B3, 2011
{: .label }

Prove that there are infinitely many perfect squares that can be written as a sum of six consecutive natural numbers. Find the smallest such square.

<details><summary>Solution</summary>

<p>
The sum of six consecutive numbers is of the form:
</p>

<p>
\[ \frac{(n+6)(n+7)}{2} - \frac{n(n+1)}{2} \text{ for some } n\]
</p>


<p>
The above expression simplifies to \(3(2n+7)\). This number is a perfect square whenever \(2n+7=3k^2\). Any odd number greater than one can be substituted for \(k\). The smallest value of \(k\) is 3, so the smallest such square is 81.
</p>

<p>
\[ 81 = 11+12+\cdots+16 \]
</p>

</details>

---

### Two variables one equation
{: .d-inline-block}

C1, 2011
{: label .label-blue}

Show that there are exactly 16 pairs of integers \\((x,y)\\) such that
\\(11x+8y+17=xy\\).

<details><summary>Solution</summary>


<p>
An equation of the form \(xy=ax+by+c\) can be written as:
</p>
<p>
\[  (x-a)(y-b) = c+ab  \]
</p>

<p>
So the given equation is:
</p>

<p>
\[  (x-8)(y-13) = 105  \]
</p>

<p>
The number of solutions to the above equation is the number of divisors of 105.
We can factorize 105 as \( 1\cdot 3\cdot 5\cdot 7\). Every subset of these four numbers corresponds to a divisor, so there are \(2^4=16\) solutions.
</p>

</details>

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

<details><summary>Solution</summary>

<p>
We have:
\[N=\left(10^{5}+10^{3}+10\right) x+\left(10^{4}+10^{2}+1\right) y=10101(10 x+y)= 3 \times 7 \times 13 \times 37 \times(10 x+y)\]

</p>

<p>
Therefore for \(N\) to be a perfect power, the primes 3,7,13,37 must all occur (and in fact with equal power) as factors in the prime factorization of \(10 x+y .\)
In particular \(10 x+y \geq 10101\).  But since \(x\) and \(y\) are digits, each is between 0 and \(9,\) so \(10 x+y \leq 99\).
So \(N\) cannot be a perfect power.
</p>

</details>

---

### Prime factorization and divisibility
{: .d-inline-block}

A6, 2014
{: .label }

Find the smallest \\(n\\) for which \\(\displaystyle \frac{50!}{24^n} \\) is *not* an integer.

<details><summary>Solution</summary>


<p>The expression will not be an integer if and only if the numerator has a prime power lesser
than the corresponding power in the denominator.
</p>

<p>
We have \( 24=2^3\cdot 3\). Let us find the the powers of 2 and 3 in \(50!\).
</p>


<p>
The power of 2 is given by:
\[  \lfloor 50/2 \rfloor + \lfloor 50/4 \rfloor + \lfloor 50/8 \rfloor + \lfloor 50/16 \rfloor + \lfloor 50/32 \rfloor = 47 \]
</p>

<p>
The power of 3 is given by:
</p>

<p>
\[  \lfloor 50/3 \rfloor + \lfloor 50/9 \rfloor + \lfloor 50/27 \rfloor = 22 \]
</p>


<p>
The numerator is of the form: \( 2^{47}3^{22}\cdot k \).
If \(n=16\), the denominator has \(2^{48}\) as a factor which is sufficient to make the number a non-integer.
</p>


</details>

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

<details><summary>Solution</summary>

<p>
(a) We have \(10000=16 \times 625\) as product of prime powers. Recall the notation \(a \mid b,\) meaning \(b\) is divisible by a. We have \(10000 \mid a^{2}-a\) if and only if \((625 \mid a(a-1)\) and \(16 \mid a(a-1)) .\) Because \(a\) and \(a-1\) cannot share a factor, in turn this is equivalent to having both the conditions \((1) 625 \mid a\) or \(625 \mid a-1\) AND
(2) \(16 \mid a\) or \(16 \mid a-1 .\) Now if the coprime integers 16 and 625 both divide the same natural number (in our case \(a\) or \(a-1),\) their product 10000 will also divide this number. In our case this would force \(a=0,1,\) or \(\geq 10000,\) all of which are not allowed. Thus the given requirement on \(a\) is equivalent to having either (1) \(16 \mid a\) and \(625 \mid a-1\) OR
(2) \(16 \mid a-1\) and \(625 \mid\) a. Each case has a unique solution, respectively \(a=9376\) and \(a=625\) (e.g. use modular arithmetic:
in case \(1,\) we have \(a=625 k+1,\) which is \(k+1\) mod \(16,\) forcing \(k=15\) because \(16 \mid a\) and \(a \in\{2,3, \ldots, 9999\})\)
</p>

<p></p>

<p>
(b) Let \(n=p_{1}{ }^{e_{1}} \ldots p_{k}{ }^{e_{k}}\) be the factorization of \(n\) into powers of distinct primes. The analysis in part (a) tells us that required values of \(a\) are obtained as follows: write \(n^{2}=x y\) as a product of two coprime integers and find values of \(a\) in \(\left\{2,3, \ldots, n^{2}-1\right\}\) that are simultaneously 0 mod \(x\) and 1 mod \(y\). These are precisely the values of \(a\) that we want. This is because each \(p_{i}^{2 e_{i}}\) must divide \(a\) or \(a-1,\) as \(a\) and \(a-1\) are coprime.
</p>

<p></p>


<p>
Now the Chinese remainder theorem tells us that there is always an \(a\) that is 0 mod \(x\) and 1 mod \(y\). It is also unique modulo \(x y=n^{2}\) because difference between any two solutions would be divisible by \(x y\).
</p>

<p></p>

<p>
The total number of ways to write \(n^{2}=x y\) as a product of coprime integers is exactly \(2^{k}\) as it amounts to choosing which of the \(k\) distinct primes to include in \(x\) and then the rest go into \(y\). (Notice that \(x\) and \(y\) are not interchangeable.) However, we have to delete the two cases \(x=1, y=n^{2}\) and \(y=1, x=n^{2},\) as these will respectively lead to solutions \(a=1\) and \(a=0\) or \(n^{2},\) which are not in \(\left\{2,3, \ldots, n^{2}-1\right\} .\) Finally it is easy to see that different choices of \(x\) lead to different values of \(a\). This is because, of the primes \(p_{1}, \ldots, p_{k}\) in the factorization of \(n,\) precisely the ones dividing \(x\) will divide \(a\) and the remaining primes will not, because they divide \(a-1\).
</p>

<p>
Thus the final answer is \(2^{k}-2 .\) Note that this matches with the special case in part (a). Finally, note that there was nothing special about taking a square: instead of \(n^{2}\) it could be any positive integer \(m\) and we would proceed the same way to find requisite integers \(a\) in \(\{2,3 \ldots, m-1\}\) based on prime factorization of \(m\)
</p>

</details>

---


### Primes in an algebraic equation &#65290;
{: .d-inline-block}

B6, 2016
{: .label}

<p>
Find all pairs \((p, n)\) of positive integers where \(p\) is a prime number and \(p^{3}-p=n^{7}-n^{3}\)
</p>

<details><summary>Solution</summary>


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


</details>






