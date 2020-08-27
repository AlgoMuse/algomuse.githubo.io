---
layout: default
title: GCD
parent: Number theory
nav_order: 1
---


## GCD
{: .no_toc  }


#### Problems
{: .no_toc  }

1. TOC
{:toc}

---

### Magic number
{: .d-inline-block}

A3, 2015
{: .label}


<p>
A positive integer \(n\) is called a magic number if it has the following property: if \(a\) and \(b\) are two positive numbers that are not coprime to \(n\) then \(a+b\) is also not coprime to \(n\) For example, 2 is a magic number, because sum of any two even numbers is also even. Which of the following are magic numbers?
</p>

<p>
(i) 129<br>
(ii) 128<br>
(iii) 127<br>
(iv) 100<br>

</p>

<details><summary>Solution</summary>

<p>
Only 128 and 127 are magic numbers. See that \(n\) is a magic number if and only if \(n\) is a power of a prime.
</p>

<p>
Otherwise, write \(n=a b\) with \(a, b\) coprime.
</p>

</details>

---



### Euclidean algorithm
{: .d-inline-block}

B5, 2015
{: .label}


<p>For an arbitrary integer \(n,\) let \(g(n)\) be the \(G C D\) of \(2 n+9\) and \(6 n^{2}+11 n-2 \).
What is the largest positive integer that can be obtained as the value of \(g(n) ?\) If \(g(n)\) can be arbitrarily large,
state so explicitly and prove it.
</p>

<details><summary>Solution</summary>

<p>
Long division gives \(6 n^{2}+11 n-2=(2 n+9)(3 n-8)+70 .\) By Euclidean algorithm, \(G C D\left(6 n^{2}+11 n-2,2 n+9\right)=G C D(2 n+9,70) .\) Thus \(g(n)\) divides \(70 .\) But since \(g(n)\) divides \(2 n+9,\) which is odd, \(g(n)\) divides \(35 .\) When \(n=13,2 n+9=35\) and hence \(g(13)=35 .\) Thus the maximum value of \(g(n)\) is \(35 .\)
</p>

</details>

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

<details><summary>Solution</summary>

<p>
Given \(n=p q=110179\). The number of integers relatively prime to \(n\) and smaller than \(n\) is \((p-1)(q-1) .\) So we have \(p q-p-q+1=109480 .\) We get \(p+q=700 .\) Now \(p, q\) are solutions to the quadratic \(x^{2}-700 x+110179\).
</p>

<p>
The discriminant of this quadratic is \(\sqrt{490000-440716}=\sqrt{49284}=222\). So we get \(p=\frac{700+222}{2}=461\) and \(q=\frac{700-222}{2}=239\).
</p>

</details>

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


<details><summary>Solution</summary>

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

</details>

---




### Sample a divisor
{: .d-inline-block}

A4, 2017
{: .label}

<p>
Positive integers \(a\) and \(b,\) possibly equal, are chosen randomly from among the divisors of \(400 .\) The numbers \(a, b\) are chosen independently, each divisor being equally likely to be chosen. Find the probability that \(\operatorname{gcd}(a, b)=1\) and \(\operatorname{lcm}(a, b)=400\)
</p>

<details><summary>Solution</summary>

<p>
\(400=5^{2} \times 2^{4}\) has \((2+1) \times(4+1)=15\) factors, so total number of pairs \((a, b)\) is \(225 .\) For \(a, b\) to be coprime, they should have no prime factor in common and then their lcm is just their product, which is required to be \(400 .\) So there are only four allowed pairs:<br>
(1,400),(400,1),(25,16) and (16,25).
</p>

<p>
The probability is \(\frac{4}{225}\).
</p>


</details>






