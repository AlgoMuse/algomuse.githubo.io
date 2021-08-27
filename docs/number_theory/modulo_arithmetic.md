---
layout: default
title: Modulo arithmetic
parent: Number theory
nav_order: 3
---


## Modulo Arithmetic
{: .no_toc}

#### Problems
{: .no_toc}

1. TOC
{:toc}

---


### Divisibility tests
{: .d-inline-block}

A2, 2021
{: .label}


<p>If \(p\) is a prime number, which of the following are true?<br>

(a) For every prime \(p\), \(p^2-p\) is divisible by 3. <br>
(b) For every prime \(p>3\), exactly \(p-1\) or \(p+1\) is divisible by 6.<br>
(c) For every prime \(p>3\), \(p^2-1\) is divisible by 24.<br>
(d) For every prime \(p>3\), one of \(p+1\),\(p+3\) and \(p+5\) is divisible by 8.
</p>


<details><summary>Solution</summary>
<br>
(a) False. \(5^2-5\) is not divisible by 3.<br>
(b) True. Both 3 and 2 must be factors of either \(p-1\) or \(p+1\). Since \(p\) is an odd prime, it is not divisible by 3. So either \(p-1\) or \(p+1\) is divisible by 3. But \(p-1\) and \(p+1\) are both even.<br>
(c) True. \(p\) is either \(4k+1\) or \(4k+3\). So \(p^2-1\) has 8 and 3 as factors.<br>
(d) False. Put \(p=17\). <br>
</details>


---

### Difference of squares
{: .d-inline-block}

A5, 2018
{: .label}

<p>List in increasing order all positive integers \(n \leq 40\) such that \(n\) cannot be written in the form \(a^{2}-b^{2},\) where \(a\) and \(b\) are positive integers.
</p>


<details><summary>Solution</summary>

<p> 1,4 and all even number s of the form \(4 k+2\).</p>

</details>

---

### Fermat's little theorem
{:b .d-inline-block}

A5, 2010
{: .label .label-blue}

<p>
Find the remainder given by \(3^{89} \times 7^{86}\) when divided by 17.
</p>

<details><summary>Solution</summary>

<p>
The usual trick is to try to get numbers that are 1,-1 modulo the divisor. In this case, \(16\equiv -1 \mod 17\). We cannot get 16 directly but notice
that \( 21 \equiv 4 \mod 17 \), which we can get.
</p>

<p>
\(3^{89} 7^{86} \equiv 3^{3}(3 \cdot 7)^{86} \equiv 27 \cdot 4^{86} \equiv 10\left(4^{2}\right)^{43} \equiv 10(-1)^{43} \equiv-10 \equiv 7\)
</p>


</details>

---

### Chinese remainder theorem
{: .d-inline-block}

A10, 2020
{: label .label-blue}


<p>
Find positive integers \(a,b,c\leq 475\) such that:
</p>

<p>
\begin{align}
a\equiv 0\pmod {25} & \quad a\equiv 1\pmod {19} \\ \\
b\equiv 1\pmod {25} & \quad b\equiv 0\pmod {19} \\ \\
c\equiv 10\pmod{25} & \quad c\equiv 4\pmod {19}
\end{align}
</p>


<details><summary>Solution</summary>

<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">

<h3>Background: Chinese remainder theorem (CRT)</h3>

<p>
We want to find a \(p\) such that:

\begin{align}
p \equiv p_{1} &\: \left(\bmod\; n_{1}\right) \\
p \equiv p_{2} &\: \left(\bmod\; n_{2}\right)
\end{align}

where \(n_{1}\) and \(n_{2}\) are coprime.

Bezout's theorem proves the existence of two integers \(m_{1}\) and \(m_{2}\) such that:

\[ m_{1} n_{1}+m_{2} n_{2}=1 \]

The integers \(m_{1}\) and \(m_{2}\) can be found by the extended Euclidean algorithm.

A solution is given by

\[ p=p_{1} m_{2} n_{2}+p_{2} m_{1} n_{1} \]

Further, the solution is unique modulo \(n_1n_2\).
</p>
</div>

The numbers 25 and 19 are co-prime and we can apply CRT directly to our problem.

\[ -3\times 25 + 4\times 19 = 1 \]

So we have:

\begin{align}
n_1 &= 25 &  n_2 &= 19 \\
m_1 &= -3 &  m_2 &= 4
\end{align}

We apply the formula to get the values of \(a,b\) and \(c\).

\begin{align}
a &= 0\times 76 + 1 \times -75 = -75 = 400 \pmod{475} \\
b &= 1\times 76 + 0 \times -75 = 76  \\
c &= 10\times 76 + 4 \times -75 = 460 \pmod{475}
\end{align}

</details>


---


### Is a square?
{: .d-inline-block}

A6, 2019
{: label .label-blue}

For what values of \\( n \\) is \\( n^6 + n^4 + 1 \\) a square of a natural number?


<details><summary>Solution</summary>

<p>
We will handle odd and even cases separately.
</p>

<p>
<i>Lemma.</i> Every odd square is \(1 \bmod 8\).
</p>

\[ (2k+1)^2=4k^2+4k+1=4(k^2+k)+1 \]

Since \( 4(k^2+k) \) is divisible by 8, the lemma follows. \(\square\)

<p></p>

<p>
<i>Case 1.</i> If \(n\) is odd, then the given expression \(S:=n^6+n^4+1\) cannot be a square since \(S\equiv 3\pmod 8\). Hence \(n\) is not odd.
</p>

<p>
<i>Case 2.</i> If \(n=2\), we have \(S=81\), so we have one solution. If \(n>2\) and is even we have:
</p>

<p>
\[ \left(n^3+\frac{n}{2}\right)^2=n^6+n^4+\frac{n^2}{4}> S > n^6+n^4-2n^3+\frac{n^2}{4}-n+1=\left(n^3+\frac{n}{2}-1\right)^2 \]
</p>

<p>
\( S \) is a number strictly inbetween two consecutive squares, so there are no solutions for \(n>2\).
</p>


</details>

---



### Pigeon-hole principle
{:b .d-inline-block}

B1, 2010
{: .label }

<p>
Let \(a_{1}, a_{2}, \ldots, a_{100}\) be 100 positive integers. Show that for some \(m, n\) with \(1 \leq m \leq n \leq\) \(100, \sum_{i=m}^{n} a_{i}\) is divisible by 100.
</p>

<details><summary>Solution</summary>

<p>
Consider the remainders of the sequence when divided by 100. If some \(a_k\bmod100=0\), then \(m=n=k\) will work. Otherwise, the reminders are between 1 and 99 for every number.
</p>
<p>
Since there are 100 numbers, there must be two indices \(i\) and \(j\) such that \(a_i\bmod 100=a_j\bmod 100\). Pick \(m=i\) and \(n=j\), if \( i < j \).
</p>



</details>

<p>
<i>Similar problem</i>. Prove that there exists a number consisting of only 1s and 0s that is divisible by 3.
</p>

---

### Pigeon-hole on pairs
{: .d-inline-block}

B7, 2012
{: .label }

<p>
A sequence of integers \(c_{n}\) starts with \(c_{0}=0\) and satisfies \(c_{n+2}=a c_{n+1}+b c_{n}\) for \(n \geq 0,\) where \(a\) and \(b\) are integers. For any positive integer \(k\) with \(g c d(k, b)=1,\) show that \(c_{n}\) is divisible by \(k\) for infinitely many \(n\)
</p>


<details><summary>Solution</summary>

<p>
Let \( r_i = c_i \mod k \). We want to prove that the sequence of \(r_i\)s has infinitely many zeroes.
</p>

<p><b>Lemma.</b> For all  \(i> 0\),  \(r_i\) and \(r_{i+1}\) uniquely determine \(r_{i-1}\). </p>


<p><i>Proof</i>.  Since \(k\) and \(b\) are co-prime, \(b\) has an inverse modulo \(k\). That is, there is a unique number \(b^{-1}\) such that \( bb^{-1} = 1\).
</p>

<p>
\begin{align}
    b^{-1}r_{n+2}&=b^{-1}ar_{n+1}+bb^{-1}r_{n} \\
    r_{n} &=   b^{-1}(ar_{n+1} - r_{n+2}) \quad\quad\square
\end{align}
</p>


<p>
The lemma implies that there are infinite number of zeros in the sequence of \(r_i\)s. If not, we can find the last zero. Look at the infinite sequence
starting from the last zero. Since there are only \(k^2\) distinct pairs, some pair must repeat by pigeon-hole principle. Let \(ab\) be the <i>first</i>
pair of consecutive numbers that repeats. Let \(x\) and \(y\) be the numbers that come before the first and the second instance of the pair.
Due to the above lemma, given the pair \(ab\), the previous number is unique. So \(x=y\).  But this violates our assumption that \(ab\) is the first pair that repeats.
</p>

<p style="text-align:center;"><img src="/assets/images/B7_2012.svg"></p>


</details>

---

### Perfect square in a sequence
{: .d-inline-block}

B4, 2017
{: .label}


<p>The domain of a function \(f\) is the set of natural numbers. The function is defined as follows:</p>

<p>\[ f(n)=n+\lfloor\sqrt{n}\rfloor \]</p>

<p>where \(\lfloor k\rfloor\) denotes the smallest integer less than or equal to \(k .\) For example, \(\lfloor\pi\rfloor=\) \(3,\lfloor 4\rfloor=4 .\) Prove that for every natural number \(m\) the following sequence contains at least one perfect square</p>

<p>\[ m, f(m), f^{2}(m), f^{3}(m), \ldots \]</p>


<p>The notation \(f^{k}\) denotes the function obtained by composing \(f\) with itself \(k\) times, e.g., \(f^{2}=f \circ f\)</p>

<details><summary>Solution</summary>

<p>
If \(m\) is itself a square then we are done. So assume that \(m=k^{2}+j\) for \(1 \leq j \leq 2 k\). Hence we have \(f(m)=k^{2}+j+k\). Consider the following two sets:
</p>


<br>


<p>\(A=\left\{m \text{ a natural number} \mid m=k^{2}+j \text { and } 0 \leq j \leq 2 k\right\} \)</p>

<p>\(B=\left\{m \text{ a natural number} \mid m=k^{2}+j \text { and } k+1 \leq j \leq 2 k\right\} \)</p>

<p>Suppose \(m\) is in the set \(B\). Then</p>

<p>
\[
\begin{align}
f(m) &=k^{2}+j+k \\
&=(k+1)^{2}+(j-k-1)
\end{align}
\]
</p>

<p>Hence \(f(m)\) is eit her a square or is in \(A .\) Thus it is enough to assume that \(m \in A\) In that case \(k^{2}< f(m)< (k+1)^{2},\) so \(\lfloor f(m)\rfloor=k\). Therefore</p>

<p>\[ f^{2}(m)=(k+1)^{2}+(j-1) \]</p>

<p>This clearly implies that \(f^{2 j}(m)=(k+j)^{2}\)</p>


</details>










