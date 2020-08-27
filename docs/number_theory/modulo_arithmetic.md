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

### Numbers of the form \\(a^2-b^2\\)
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
Consider pairs of consecutive entries of the sequence modulo \(k,\) i.e., \(\left(\bar{c}\_{n}, \bar{c}\_{n+1}\right)\), where \(\bar{a}\) denotes \(a\) modulo \(k\). Since there are only finitely many possibilities (namely \(k^{2}\) ), some pair of consecutive residues will repeat. Suppose \(\left(\bar{c}\_{i}, \bar{c}\_{i+1}\right)=\left(\bar{c}\_{i+p}, \bar{c}\_{i+p+1}\right)\) for some \(i\).
</p>

<p>
We will show that in fact the previous equation holds for all \(i,\) i.e., whole sequence of consecutive pairs is periodic.  This will prove in
particular that \(\left(\bar{c}\_{0}, \bar{c}\_{1}\right)=\left(\bar{c}\_{p}, \bar{c}\_{p+1}\right)=\left(\bar{c}\_{2 p}, \bar{c}\_{2 p+1}\right)=\cdots\)
since \(c_{0}=0\) is divisible by \(k,\) so is \(c_{i p}\) for all \(i\)
</p>

<p>
The equation \(c_{n+2}=a c_{n+1}+b c_{n}\) shows that \(\bar{b} \bar{c}\_{n}=\bar{c}\_{n+2}-\bar{a} \bar{c}\_{n+1}\).
</p>

<p>
Now \(gcd(k, b)=1\) means \(b\) is invertible modulo \(k,\) i.e., there is a \(b^{\prime}\) with \(\overline{b b^{\prime}}=\overline{1} .\)
</p>

<p>
Therefore \(\bar{c}\_{n}=\bar{b}^{\prime}\left(\bar{c}\_{n+2}-\bar{a} \bar{c}\_{n+1}\right)\)
</p>

<p>
Thus knowing a pair of consecutive residues uniquely determines the previous residue (this is why we considered pairs of residues). Therefore \(\left(\bar{c}\_{i}, \bar{c}\_{i+1}\right)=\left(\bar{c}\_{i+p}, \bar{c}\_{i+p+1}\right)\) implies \(\left(\bar{c}\_{i-1}, \bar{c}\_{i}\right)=\left(\bar{c}\_{i+p-1}, \bar{c}\_{i+p}\right)\) and (by the given recurrence) \(\left(\bar{c}\_{i+1}, \bar{c}\_{i+2}\right)=\left(\bar{c}\_{i+p+1}, \bar{c}\_{i+p+2}\right)\)
</p>


<p>
Thus the whole sequence \(\left(\bar{c}\_{n}, \bar{c}\_{n+1}\right)\) becomes periodic as soon as a single such pair repeats.
</p>

</details>



