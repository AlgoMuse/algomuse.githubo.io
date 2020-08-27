---
layout: default
title: (Ir)rationality
parent: Number theory
nav_order: 2
---


## (Ir)rationality
{: .no_toc  }


#### Problems
{: .no_toc  }

1. TOC
{:toc}

---

### Rationality preserving operations
{:b .d-inline-block}

A11, 2010
{: .label .label-blue}

Using the fact that \\(\sqrt{n}\\) is an irrational number whenever \\(n\\) is not a perfect square, show that \\(S=\sqrt{3}+\sqrt{7}+\sqrt{21}\\) is irrational.

<details markdown="1">
<summary>Solution</summary>

Our proof works by showing a series of "If x is rational so is y". Suppose the given number is rational. The the following sequence of numbers must be rational too.


|---|---|
\\(7\sqrt{3}+3\sqrt{7}+\sqrt{21}\\) | Square the given number and subtract the integer part|
\\(6\sqrt{3}+2\sqrt{7}\quad\\) | Subtract X from the above number. Since X is assumed to be rational, this number must be rational too.|
\\(\sqrt{3}\sqrt{7}\quad\quad\\) | Square the above number and remove the integer part.|


But we know that \\(\sqrt{21}\\) is not rational and hence a contradiction.

</details>

---

### Irrational fraction
{: .d-inline-block}

A3, 2012
{: .label }

Prove that \\(\frac{\ln (12)}{\ln (18)}\\) is irrational.


<details>
<summary>Solution</summary>

<p>
We know that \(\frac{\ln (12)}{\ln (18)}=\log_{18}(12) .\) Suppose this is rational, say \(=\frac{a}{b}\) where \(a, b\) are integers with \(b \neq 0\).
Then \(18^{\frac{a}{b}}=12,\) so \(18^{a}=12^{b} .\) By factoring into primes this gives \(3^{2 a} 2^{a}=3^{b} 2^{2 b},\) which by unique factorization can happen only if \(2 a=b\) and \(a=2 b\). But this gives \(a=b=0\), a contradiction.
</p>

</details>


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

<details><summary>Solution</summary>

<p>
False-True-True
</p>

</details>

---

### A polynomial integer
{: .d-inline-block}

B2, 2014
{: .label}

<p>
Let \(x\) be a real number such that \(x^{2014}-x^{2004}\) and \(x^{2009}-x^{2004}\) are both integers. Show that \(x\) is an integer. <br>

Hint: it may be useful to first prove that \(x\) is rational.
</p>


<details><summary>Solution</summary>

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



</details>



