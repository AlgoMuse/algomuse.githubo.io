---
layout: default
title: Functions
parent: Calculus
nav_order: 1
---


# Functions

### One-to-one I
{: .d-inline-block }

A1, 2013
{: .label}


<p>
For sets \(S\) and \(T,\) let \(f: S \rightarrow T\) and \(g: T \rightarrow S\) be functions such that \(f(g(x))=x\) for each \(x \). State which of the statements are true.
</p>


<p>
<ul>
<li>(a) The function \(f\) must be one-to-one.</li>
<li>(b) The function \(g\) must be one-to-one.</li>
<li>(c) The function \(f\) must be onto.</li>
<li>(d) The function \(g\) must be onto.</li>
</ul>
</p>


Sol.

<p>
False-True-True-False.
</p>

<p>
If \(g\left(x_{1}\right)=g\left(x_{2}\right),\) then \(x_{1}=f\left(g\left(x_{1}\right)\right)=f\left(g\left(x_{2}\right)\right)=x_{2},\) so \(g\) is one-to-one. Also \(f\) is onto because each \(x \in T\) is in the image of \(f,\) namely \(x=f(g(x)) .\) The other two statements are false, for example by constructing an \(S\) that is a larger finite set than \(T\).
</p>

---

### Continuity
{: .d-inline-block }

A2, 2013
{: .label}

<p>
Let \(f: \mathbb{R} \rightarrow \mathbb{R}\) be a function, where \(\mathbb{R}\) is the set of real numbers. For each statement below, write whether it is TRUE or FALSE.
</p>

<p>
<li>a) If \(|f(x)-f(y)| \leq 39|x-y|\) for all \(x, y\) then \(f\) must be continuous everywhere.</li>
<li>b) If \(|f(x)-f(y)| \leq 39|x-y|\) for all \(x, y\) then \(f\) must be differentiable everywhere.</li>
<li>c) If \(|f(x)-f(y)| \leq 39|x-y|^{2}\) for all \(x, y\) then \(f\) must be differentiable everywhere.</li>
<li>d) If \(|f(x)-f(y)| \leq 39|x-y|^{2}\) for all \(x, y\) then \(f\) must be constant.</li>
</p>

Sol.

<p>
True-False-True-True
</p>

<p>
In parts a and b, we have \(|f(x)-f(a)|\) lying between \(\pm 39|x-a| .\) As \(x \rightarrow a\) \(\pm 39|x-a| \rightarrow 0\) and hence \(f(x)-f(a) \rightarrow 0,\) so \(f\) is continuous. But it need not be differentiable, for example \(f(x)=|x|\) satisfies \(f(x)-f(y)=|x|-|y| \leq|x-y| \leq 39|x-y| \cdot\) But \(f\) is not differentiable at \(0 .\)
</p>

<p>
In parts c and d, we have \(\left|\frac{f(x)-f(a)}{x-a}\right| \leq 39|x-a|,\) so by reasoning as for part a, we have \(\lim_{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=0,\) i.e., \(f^{\prime}(a)=0\) for all \(a,\) so \(f\) is a constant function.
</p>

---

### Rolle's theorem III
{: .d-inline-block}

A9, 2013
{: .label}


<p>
Let \(\mathbb{R}=\) the set of real numbers. A continuous function \(f: \mathbb{R} \rightarrow \mathbb{R}\) satisfies \(f(1)=1\), \(f(2)=4, f(3)=9\) and \(f(4)=16 .\) Answer the following questions.
</p>

<p>
(i) Which of the options must be in the range of \(f\)?
</p>

<p>
(a) 5 (b) 25 (c) both (d) neither
</p>


<p>
(ii) Suppose \(f\) is differentiable. Then which of these intervals must contain an \(x\) so that \(f^{\prime}(x)=2 x\) ?
</p>

<p>
(a) (1,2) (b) (2,4) (c) both (d) neither
</p>


<p>
(iii) Suppose \(f\) is differentiable twice. Which of these intervals should contain an \(x\) such that \(f^{\prime \prime}(x)=2\)?
</p>

<p>
(a) (1,2) (b) (2,4) (c) both (d) neither
</p>

<p>
(iv) Suppose \(f\) is a polynomial, then which of the following are possible values of its degree?
</p>

<p>
(a) 3 (b) 4 (c) both (c) neither
</p>

Sol.

<p>
(i) \(5\).  By the intermediate value theorem over the interval \([2,3]\). Also \(f(x)\) may not take the value \(25,\). For a counterexample,
take \(f(x)=x^{2}\) for \(x<4\) and \(f(x)=16\) for \(x \geq 4\).
</p>


<p>
(ii) Both.
</p>

<p>
(iii) (2,4)
</p>

<p>
(iv) 4
</p>

<p>
For parts b, c and d, let \(g(x)=f(x)-x^{2}\). We have \(g(1)=g(2)=g(3)=g(4)=0\). For part b, applying Rolle's theorem to \(g(x)\) gives \(g^{\prime}(x)=0\) for some values of \(x\) in each of the intervals \((1,2),(2,3),(3,4) .\) For these values of \(x,\) we have \(f^{\prime}(x)=g^{\prime}(x)+2 x=2 x\)
</p>

<p>
For part c, take from part b values \(r \in(2,3)\) and \(s \in(3,4)\) with \(g^{\prime}(r)=0=g^{\prime}(s)\). Applying Rolle's theorem to \(g^{\prime}(x)\) in the interval \([r, s],\) we get for some \(x \in(r, s) \subset(2,4)\) the equality \(g^{\prime \prime}(x)=0\) and so \(f^{\prime \prime}(x)=g^{\prime \prime}(x)+2=2 .\) There need not be an \(x \in(1,2)\) with \(f^{\prime \prime}(x)=2\)
i.e., \(g^{\prime \prime}(x)=0 .\) There are many ways to arrange this, for example let \(g(x)=\sin (\pi x) .\) Then
</p>


<p>
\(g^{\prime \prime}(x)=-\pi^{2} \sin (\pi x),\) which is 0 only when \(x\) is an integer, in particular \(g^{\prime \prime}(x) \neq 0\) for any \(x \in(1,2)\)
For part d, note that \(g(x),\) now being a polynomial vanishing at 1,2,3 and \(4,\) must be divisible by \((x-1)(x-2)(x-3)(x-4) .\) So \(g(x),\) if non-zero, must have degree at least 4 Thus \(f(x)=x^{2}\) or a polynomial of degree at least 4
</p>









