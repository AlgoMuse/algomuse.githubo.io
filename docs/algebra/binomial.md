---
layout: default
title:  Binomials and Inequalities
parent: Algebra
nav_order: 3
---


## Binomial expansion [2]

### Largest coefficient
{: .d-inline-block}

B2, 2011
{: label .label-blue}

<p>
Show that the power of \(x\) with the largest coefficient in the polynomial \(\displaystyle (1 + 2x/3)^{20}\) is 8. In other words, if
we write the given polynomial as \( \sum_i a_ix^i\) then the largest coefficient \(a_i\) is \(a_8\).
</p>


<details><summary>Solution</summary>

<p>
The coefficient \( a_i = \binom{20}{i} \left(\frac{2}{3}\right)^i \). Consider the ratio of two consecutive terms: \( a_{i+1}/a_i \).

\begin{align}
\text{ratio } &= \frac{2}{3} \times \left(  \frac{20!}{20-i-1!i+1!}/\frac{20!}{20-i!i!} \right) \\
&\\
  &= \frac{2}{3} \cdot \frac{20-i!i!}{20-i-1!i+1!} = \frac{2(20-i)}{3(i+1)}
\end{align}


The ratio \( a_{i+1}/a_i > 1\) up to \(i\leq 7\) and strictly less than 1 for \(i>7\). Hence, the sequence of coefficients is <a href="https://en.wiktionary.org/wiki/bitonic">bitonic</a> with the peak occurring at \(a_8\).
</p>


</details>

---


### Coefficient ratio
{: .d-inline-block}

A7, 2015
{: .label}


<p>
(i) By the binomial theorem \((\sqrt{2}+1)^{10}=\sum_{i=0}^{10} C_{i}(\sqrt{2})^{i},\) where \(C_{i}\) are appropriate constants. Write the value of \(i\) for which \(C_{i}(\sqrt{2})^{i}\) is the largest among the 11 terms in this sum.
</p>

<p>
(ii) For every natural number \(n,\) let \((\sqrt{2}+1)^{n}=p_{n}+\sqrt{2} q_{n},\) where \(p_{n}\) and \(q_{n}\) are integers. Calculate \(\lim _{n \rightarrow \infty}\left(\frac{p_{n}}{q_{n}}\right)^{10}\).
</p>


<details><summary>Solution</summary>

<p>
(i) \(i=6\). Consider the ratio:
<br>

\[\frac{C_{i+1}(\sqrt{2})^{t+1}}{C_{i}(\sqrt{2})^{4}}\]

<br>

This ratio is \(>1\) till \(i=5\) and \(<1\) from \(i=6\) onwards. Similar to problem B2, 2011.
</p>


<p>
(ii) 32.
Using binomial expansion see that \((\sqrt{2}-1)^{n}=\pm\left(p_{n}-\sqrt{2} q_{n}\right),\) where the sign depends on the parity of \(n .\) As \(n \rightarrow \infty,(\sqrt{2}-1)^{n} \rightarrow 0\) since \((\sqrt{2}-1)<1 .\) Thus \(\left(p_{n}-\sqrt{2} q_{n}\right) \rightarrow 0\) and so \(\frac{p_{n}}{q_{n}} \rightarrow \sqrt{2}\)<br>
</p>

</details>

---



## Inequalities [2]


### AM-GM inequality
{: .d-inline-block}

A4, 2011
{: label .label-blue}


<p>
Given positive real numbers \( a_1, a_2, \ldots , a_{2011} \) whose product \(a_1 a_2 \cdots a_{2011}=1\),
what can you say about their sum \( S = a_1 + a_2 + · · · + a_{2011} \)?
</p>

- [ ] \\( S\; \\) can be any positive number.
- [ ] \\( 1 \leq S \leq 2011\\).
- [ ] \\( 2011 \leq  S \text{ and }  S\;\\) is unbounded above.
- [ ] \\( 2011 \leq  S \text{ and }  S\;\\) is bounded above.


<details><summary>Solution</summary>

<p>
\( 2011 \leq  S \text{ and }  S\;\) is unbounded above.
</p>

<p>
The first inequality follows from AM-GM inequality. To see why \(S\) is unbounded, set
\( a_1=n \), \(a_2=1/n\) and the rest of \( a_is\) to 1. The sum \(S>n\) for any \(n\).
</p>


</details>

---

### AM-GM inequality II
{: .d-inline-block}

B5, 2012
{: .label }

<p>
Suppose  \(x+x^{-1}=\frac{\sqrt{5}+1}{2}\).
</p>

<p>
(a) For any real \(r,\) show that \(\left|r+r^{-1}\right| \geq 2 .\) What kind of a number is \(x\)?
</p>

<details>
<summary>Solution</summary>

<p>
Without loss of generality, we may assume that \(r > 0\). Now use the AM-GM inequality:<br>

\[ \frac{ r+\frac{1}{r}  }{2} \geq \sqrt{ r \cdot \frac{1}{r} }  \]


since \(x+x^{-1}=\frac{\sqrt{5}+1}{2}<2\), the number \(x\) must be a non-real complex number.
</p>


</details>


---

### Points on a sphere
{: .d-inline-block}

B2, 2015
{: .label}


<p>
Let \(p, q\) and \(r\) be real numbers with \(p^{2}+q^{2}+r^{2}=1\)
</p>

<p>
(a) Prove the inequality \(3 p^{2} q+3 p^{2} r+2 q^{3}+2 r^{3} \leq 2\)
</p>

<p>
(b) Also find the smallest possible value of \(3 p^{2} q+3 p^{2} r+2 q^{3}+2 r^{3} \).
</p>

<p>
Specify exactly when the smallest and the largest possible value is achieved.
</p>

<details>

<summary>Solution</summary>

<p> We have

\begin{align}
3p^{2} q+3 p^{2} r+2 q^{3}+2 r^{3}&=(q+r)\left(3 p^{2}+2 q^{2}+2 r^{2}-2 q r\right)\\
&=((q+r)\left(3\left(p^{2}+q^{2}+r^{2}\right)-\left(q^{2}+r^{2}+2 q r\right)\right)\\
&=(q+r)\left(3-(q+r)^{2}\right)\\
&=x\left(3-x^{2}\right)=3 x-x^{3}
\end{align}

where \(x=q+r.\)
</p>

<p>
Let us examine possible values of \(x\) in view of the constraint \(p^{2}+q^{2}+r^{2}=1\).
</p>

<p>
We have \(2 q r \leq q^{2}+r^{2}\) e.g. because \((q-r)^{2} \geq 0 .\)
</p>

<p>
Adding \(q^{2}+r^{2},\) we get \(q^{2}+r^{2}+2 q r \leq \) \(2 q^{2}+2 r^{2} \leq 2,\) because \(q^{2}+r^{2} \leq p^{2}+q^{2}+r^{2}=1\).
Thus \((q+r)^{2} \leq 2\). So \(-\sqrt{2} \leq q+r \leq \sqrt{2}\)
</p>

<p>
Note that equalities are achieved precisely when \(p=0\) and \(q=r=\pm 1 / \sqrt{2}\).
</p>

<p>
Thus altogether we have to find extrema of the odd function \(f(x)=3 x-x^{3}\) over the interval \([-\sqrt{2}, \sqrt{2}] .\) The critical points are when \(f^{\prime}(x)=3-3 x^{2}=0,\) i.e. \(x=\pm 1 .\) Thus we need to see only \(f(\pm \sqrt{2})=\pm \sqrt{2}\) and \(f(\pm 1)=\pm 2 .\) Therefore \(-2 \leq 3 p^{2} q+3 p^{2} r+\) \(2 q^{3}+2 r^{3} \leq 2 .\) Moreover, \(3 p^{2} q+3 p^{2} r+2 q^{3}+2 r^{3}=\pm 2\) precisely when \(x=q+r=\pm 1\)
</p>

<p>
In each case, this gives a line segment in the \(q r\) -plane joining (±1,0) and \((0,\pm 1) .\) Note that both these segments lie within the circle \(q^{2}+r^{2}=1,\) so each point on them leads to two valid points \((p, q, r)\) on the unit sphere.
</p>

</details>






