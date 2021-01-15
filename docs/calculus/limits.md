---
layout: default
title: Limits
nav_order: 1
parent: Calculus
---


# Functions and Limits



### Vanilla application of L'Hospital
{: .d-inline-block }

A3, 2010
{: label .label-blue}

Evaluate the limit:

\\[ \lim_{x \rightarrow 1}\left(\frac{n- \displaystyle \sum_{k=1}^n x^{k}}{1-x}\right) \\]


<details><summary>Solution</summary>

We apply the L'Hospital's rule and differentiate both the numerator and the denominator.

\begin{array}{rl}
 \lim_{x\rightarrow 1}&\displaystyle \frac{-n x^{n-1}-(n-1) x^{n-2}-\cdots-x-1}{-1}  \\
 =&\frac{n(n-1)}{2}
\end{array}


</details>


<p></p>

<details><summary>Practice Problem</summary>
<p>
Explain what is wrong with the use of L'Hospital's rule. Find the correct limit.

\[\lim_{x \rightarrow 1} \frac{2 x^{3}-3 x+1}{x^{4}-1}=\lim_{x \rightarrow 1} \frac{6 x^{2}-3}{4 x^{3}}=\lim_{x \rightarrow 1} \frac{12 x}{12 x^{2}}=\lim_{x \rightarrow 1} \frac{1}{x}=1\]

</p>
</details>



---


### L'Hospital again
{: .d-inline-block}

A4, 2012
{: .label}


<p>
Prove the following limit.
</p>

<p>
\[ \lim_{x \rightarrow \infty} \frac{x^{100} \ln (x)}{e^{x} \arctan \left(\frac{\pi}{3}+\sin x\right)}=0 \]
</p>

<details><summary>Solution</summary>

<p>
For some positive constant \(k\) we can ensure that \(\arctan \left(\frac{\pi}{3}+\sin x\right)> k\) for any \(x\).

For example, \(k=\arctan(0.0001)\) will work. This is because \(\pi>3.142, \sin (x) \geq-1\) and \(\arctan\) is an increasing function.
</p>

<p>
Further, \(\ln (x)< x\) for \(x> 0\). So the given ratio must lie between 0 and \(x^{101} / c e^{x} \). If we apply the L'Hospital's rule 102 times, we get the result.
</p>


</details>


---

### Asymptotes
{: .d-inline-block}

A5, 2020
{: .label}


<p>
Write whether the \(3\) functions \(\frac{x^3}{(x^2-x)}, \ \frac{(x^2-x)}{x^3},\ \frac{(x^3-x)}{(x^3+x)}\) have horizontal asymptotes, vertical asymptotes and removable discontinuities.
</p>


<details><summary>Solution</summary>
<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">

<h4>How to find a horizontal asymptote?</h4>

Let us consider the case when the given function is of the form:

\[ f(x) = \frac{a_1x^m+a_2x^{m-1}+\cdots+a_m}{b_1x^n+b_2x^{n-1}+\cdots+b_n} \]

<ul>
<li>If \(m> n\), then there is no horizontal asymptote. </li>
<li>If \(m< n\), then \(y=0\) a horizontal asymptote. </li>
<li>If \(m=n\), then \(y=a_1/b_1\) a horizontal asymptote.</li>
</ul>
</div>


We can apply this directly to the given functions. The first function has no horizontal asymptotes. The second and third functions have
\(y=0\) and \(y=1\) as their horizontal asymptotes, respectively.

<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">
<h4>How to find a vertical asymptote?</h4>
Vertical asymptotes occur at those points where the denominator is zero and the numerator is non-zero.
</div>

<p>
The first two functions have \(x=1\) and \(x=0\) as their vertical asymptotes. The denominator is always positive for the third function, so there
are no vertical asymptotes for this function.
</p>

<h4>Removable discontinuities</h4>
<p>
In all the functions, the term \(x\) can be factored out from the numerator and the denominator.
Hence, \(x=0\) is a removable discontinuity for all the functions.
</p>


</details>

---


### Limit of \\(x^{x^{x}}\\)
{: .d-inline-block }

B1a, 2017
{: .label }

<p>
(a) Evaluate \( \lim_{x \rightarrow 0^{+}}\left(x^{x^{x}}-x^{x}\right) \)
</p>


<details><summary>Solution</summary>

<p>
First consider the limit
\[
\begin{align}
\lim_{x \rightarrow 0^{+}} x^{x}  \\
&=\lim_{x \rightarrow 0^{+}}\left(e^{x\log x}\right) \\
&=\lim_{x \rightarrow 0^{+}}\left(e^{\frac{\log x}{1 / x}}\right)
\end{align}
\]
</p>


<p>Now consider just the exponent:
\[
\begin{align}
\lim_{x \rightarrow 0^{+}} \frac{\log x}{1 / x} \\
&=\lim_{x \rightarrow 0} \frac{1 / x}{-1 / x^{2}} \\
&=0
\end{align}
\]
substituting the value 0 from (2) in equation (1) we get that the limit is 1.
</p>


<p>
Now
\[
\begin{align}
\lim_{x \rightarrow 0^{+}}\left(x^{x^{x}}-x^{x}\right) \\
&=\lim_{x \rightarrow 0^{+}} x^{x^{x}}-\lim_{x \rightarrow 0^{+}} x^{x} \\
&=\lim_{x \rightarrow 0^{+}} x^{\lim_{x \rightarrow 0^{+}} x^{x}}-\lim_{x \rightarrow 0^{+}} x^{x} \\
&=0-1 \\
&=-1
\end{align}
\]
</p>

</details>

<p><i><b>Reference</b>. This problem is based on a general result: A tower of even number of \(x\)s tends to zero
and a tower of odd number of \(x\)s tends to one [1].<br>

[1] <a href="http://math.depaul.edu/~mash/limitofx%5ex%5e.pdf">The limit of x** as x tends to zero</a> J. Marshall Ash,  Mathematics Magazine, 69 (1996), 207-209.</i></p>


---


### Constrained function
{: .d-inline-block}

B4, 2020
{: .label}

<p>
i) A continuous function \(f(x)\) has the property that \(f(x^2)=f(x)^2.\) If the domain of \(f\) is \([0,1]\) and \(f(0)\neq 0,\) then show that \(f\) is unique and find \(f.\)
</p>

<details><summary>Solution</summary>

<p>
Since \(f(0)\) is non-zero, \(f(0)=f(0)^2 \implies f(0)=1\). Since \(f(x) = f(\sqrt{x})^2 \), the range of \(f\) is non-negative.
We will show that \(f(x)=1\).
</p>

<p>
Let \(p\in (0,1)\) be an arbitrary point and \(f(p) = q\).

\begin{align}
f(p^2) &= f(p)^2 = q^2 \\
f(p^4) &= q^4 \\
&\vdots \\
f(p^{2^n}) &= q^{2^n}
\end{align}

Since \(|p|< 1\) the  sequence \({p^{2^n}}\) converges to 0 as \(n\rightarrow \infty\). Since the function is continuous:

\[ f(0) = 1 = \lim_{n\rightarrow \infty} q^{2^n} \]

The sequence \(q^{2^n}\)  must converge to 1. This is possible only if \(q=1\). By continuity, \(f(1)=1\) too.
Therefore, the conditions imply that \(f\) is unique and that \(f(x)=1\).

</p>

</details>


---

<p>
ii) Consider the same property of \(f,\) but the domain of the function being \((0,\infty).\) Show that either \(f(x)=0\ \forall x\) or \(f(x)\neq 0\) \(\forall\) \(x.\)
</p>



<details><summary>Solution</summary>

<p>The proof is similar to the previous proof. For \(x=1\) we have:



\[f(1^2) = f(1)^2 \implies f(1)(f(1)-1) = 0\]

So \(f(1)\) is either 0 or 1.

</p>




<p><b>Lemma.</b> If \(f(1)=0\), then \(f(x)=0\).<br>

<i>Proof.</i>

For a contradiction, let us say there exists a point \(p\) such that \(f(p)=q\), where \(q>0\).

\begin{align}
f(\sqrt{p})^2 &= f(p) = q \\
f(\sqrt{p}) &= \sqrt{q} \\
f(p^{ 1/2^n } ) &= q^{1/2^n} \\
\lim_{n\rightarrow \infty} f(p^{ 1/2^n } ) &= q^{1/2^n} \\
f(1) &= 1 \;\;\;\; \mbox{ (a contradiction) }\;\; \square
\end{align}
</p>


<p><b>Lemma.</b> If \(f(1)=1\), then \(f(x) \neq 0 \;\forall x\).<br>

<i>Proof.</i>

For a contradiction, let us say there exists a point \(p\) such that \(f(p)=0\).

\begin{align}
f(\sqrt{p})^2 &= f(p) = 0 \\
f(\sqrt{p}) &= 0 \\
f(p^{ 1/2^n }) &= 0  \;\;\;\;\mbox{ (by induction)}\\
\lim_{n\rightarrow \infty} f(p^{ 1/2^n } ) &= 0 \\
f(1) &= 0 \;\;\;\; \mbox{ (a contradiction) }\;\; \square
\end{align}
</p>


</details>


---

<p>
iii) Show that there exist infinitely many continuous functions \(f(x)\) with the same property and with domain \((0,\infty)\) such that \(\int_0^{\infty}f(x)dx<1.\)
</p>


<details><summary>Solution</summary>
<p>
For any \(p>4\), the following function satisfies the conditions:

\[
    f(x) = \left\{\begin{array}{lr}
        x& \text{for } 0 < x \leq 1\\
        x^{-p} & \text{for } 1 < x < \infty \\
        \end{array} \right.
  \]

</p>

<p>
\begin{align}
\int_0^{\infty}f(x)dx &= \int_0^{1}x dx + \int_1^{\infty} x^{-p} dx   \\\\
&= \left. \frac{x^2}{2} \right \rvert_{0}^{1} \; +\;  \left. \frac{x^{-p+1}}{-p+1} \right \rvert_{1}^{\infty}   \\\\
&= \frac{1}{2} + \frac{1}{p-1} \\\\
&< \frac{5}{6} \;\;\;\mbox{ since }\; p>4
\end{align}
</p>





</details>

---



### Surjective if and only if injective
{: .d-inline-block}

B11, 2011
{: .label}


<p>A function \(f\) from a set \(X\) to itself satisfies \(f^{m}=f^{n}\) for fixed positive integers \(m\) and \(n\) with \(m> n\).
The notation \(f^{n}\) stands for \(f \circ f \circ \cdots \circ f(n\) times). Show that \(f\) is one-to-one (injective) if and only if \(f\) is onto (surjective).
</p>


<details><summary>Solution</summary>

<p><i>Claim 1</i>: If \(f\) is one-to-one, then it is onto.</p>

<p><i>Proof: </i> Let \(m=n+k\).

\[f^m(x) = f^n(x) \implies f^n( f^k(x) ) = f^n(x) \implies f^k(x) = x \text{ for all } x\]

The second implication follows since \(f(p)=f(q)\) implies that \(p=q\) for a one-to-one function. Since \(f^k\) is an identity function, its range must
be \(X\). So the range of \(f\) must also be \(X\), which proves the claim. \(\;\square\)

</p>

<p></p>

<p><i>Claim 2</i>: If \(f\) is onto, then it is one-to-one.</p>

<p><i>Proof: </i> We prove by contradiction. Assume that \(f\) is onto but not one-to-one. So there must be an \(x\)

such that \(f(a_1) = f(b_1) = x\) for some \(a_1\neq b_1\). Since \(f\) is onto we should be able to find two numbers \(a_2\) and \(b_2\) such that

\[ f(a_2) = a_1 \text{ and } f(b_2) = b_1 \]

Also, \(a_1\neq b_1 \implies a_2\neq b_2\). It follows that:

\[ f^2(a_2) = x \text{ and } f^2(b_2) = x \]

In general, for every natural number \(t>1\), we should be able to find two different numbers \(a_t,b_t\)
with the property that \(f^t(a_t) = f^t(b_t) = x\) and \(f(a_t) = a_{t-1} \text{ and } f(b_t) = b_{t-1} \).

In particular, consider the numbers \(a_m\) and \(b_m\), where \(f^m(a_m) = f^m(b_m) = x\). Due to the condition \(f^m=f^n\), we have:


\[ x =  f^m(a_m) = f^n(a_m) = a_{m-n} = a_k \]
\[ x = f^m(b_m) = f^n(b_m) = b_{m-n} = b_k \]


This implies that \( a_k=b_k \), which is a contradiction.

<br>

<p style="text-align:center;"><img src="/assets/images/b11_2011.svg"></p>

Hence, the function \(f\) is one-to-one if \(f\) is onto. \(\;\quad\square\)



</p>

</details>




---

### Smallest prime factor function
{: .d-inline-block }

A9, 2017
{: .label}

<p>
Let \(f\) be a continuous function from \(\mathbb{R}\) to \(\mathbb{R}\) (where \(\mathbb{R}\) is the set of all real numbers) that satisfies the following property: <br>
</p>

<p>
For every natural number \(n\)
</p>

<p>
\[ f(n)= \text{the smallest prime factor of }n \]
</p>


<p>
For example, \(f(12)=2, f(105)=3 .\) Calculate the following.
</p>

<p>
(a) \(\lim_{x \rightarrow \infty} f(x)\)
</p>

<p>
(b) The number of solutions to the equation \(f(x)=2016\)
</p>

<details><summary>Solution</summary>

<p>
(a) \(f(x)\) will take value 2 for all even \(x\). At the same time, primes provide an increasing infinite sequence of positive integers for which \(f(x)=x .\) Thus \(\lim_{x \rightarrow \infty} f(x)\) does not exist.
</p>

<p>
(b) By intermediate value theorem, for each prime \(p> 2016\) there is an \(x\) between \(p\) and \(p+1\) such that \(f(x)=2016\)
</p>

</details>

---



### Limit of a log of an exponent
{: .d-inline-block}

A9, 2019
{: .label}

<p>Consider \(f: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}\) defined as follows:</p>

<p>\[ f(a, b):=\lim_{n \rightarrow \infty} \frac{1}{n} \log_{e}\left[e^{n a}+e^{n b}\right] \]</p>

<p>(a) \(f\) is not onto i.e. the range of \(f\) is not all of \(\mathbb{R}\).</p>
<p>(b) For every \(a\) the function \(x \mapsto f(a, x)\) is continuous everywhere.</p>
<p>(c) For every \(b\) the function \(x \mapsto f(x, b)\) is differentiable everywhere.</p>
<p>(d) We have \(f(0, x)=x\) for all \(x \geq 0\)</p>


<details><summary>Solution</summary>

<p>False-True-False-True</p>

</details>

---

### Continuity of two functions
{: .d-inline-block}

A10, 2017
{: .label}


<p>
Consider the following function:
\[
f(x)=\left\{\begin{array}{ll}
x^{2} \cos \left(\frac{1}{x}\right), & x \neq 0 \\
a & x=0
\end{array}\right.
\]
</p>

<p>(a) Find the value of \(a\) for which \(f\) is continuous.</p>

<p></p>

<p>(b) \(f^{\prime}(0)\)</p>

<p></p>

<p>(c) \(\lim_{x \rightarrow 0} f^{\prime}(x)\)</p>

<details><summary>Solution</summary>

<p>(a) \(\cos \left(\frac{1}{x}\right)\) is sandwiched between -1 and \(1,\) so \(\lim_{x \rightarrow 0} f(x)=0=a\) makes \(f\) continuous.</p>

<p>(b) Now \(f^{\prime}(0)=\lim_{h \rightarrow 0} \frac{h^{2} \cos \left(\frac{1}{h}\right)-0}{h}=\lim_{h \rightarrow 0} h \cos \left(\frac{1}{h}\right)\) which is similarly 0.</p>

<p>(c) For nonzero \(x,\) calculate \(f^{\prime}(x)=2 x \cos \left(\frac{1}{x}\right)+\sin \left(\frac{1}{x}\right),\) so \(\lim_{x \rightarrow 0} f^{\prime}(x)\) does not exist
\(\operatorname{as} \lim_{x \rightarrow 0} 2 x \cos \left(\frac{1}{x}\right)=0\) and \(\lim_{x \rightarrow 0} \sin \left(\frac{1}{x}\right)\) does not exist.
</p>

</details>


---

###  Polynomial and limits
{: .d-inline-block}

B1, 2015
{: .label}


<p>(a) For any polynomial \(p(t),\) the limit \(\lim_{t \rightarrow \infty} \frac{p(t)}{e^{t}}\) is independent of the polynomial \(p .\) Justify this statement and find the value of the limit.</p>
<p>(b) Consider the function defined by</p>

<p>
\begin{align}
q(x) &=e^{-1 / x} \text { when } x>0 \\
&=0 \text { when } x=0 \\
&=e^{1 / x} \text { when } x<0
\end{align}
</p>

<p>Show that \(q^{\prime}(0)\) exists and find its value. Why is it enough to calculate the relevant limit from only one side?
</p>

<p>(c) Now for any positive integer \(n,\) show that \(q^{(n)}(0)\) exists and find its value. Here \(q(x)\) is the function in part (b) and \(q^{(n)}(0)\) denotes its \(n\) -th derivative at \(x=0\).
</p>

<details><summary>Solution</summary>

 <p>(a) If \(p(t)\) is constant, then the limit \(=0 .\) Otherwise we get a form \(\frac{\pm \infty}{\infty}\). Using L'Hospital's rule, we get \(\lim_{t \rightarrow \infty} \frac{p(t)}{e^{t}}=\lim_{t \rightarrow \infty} \frac{p^{\prime}(t)}{e^{t}}=0\) by induction on the degree of \(t\) (or apply
L'Hospital's rule repeatedly).</p>

<br>

<p>(b) The right side derivative \(=\lim_{h \rightarrow 0^{+}} \frac{q(h)-q(0)}{h}=\lim_{h \rightarrow 0^{+}} \frac{e^{-1 / h}}{h}=\lim_{h \rightarrow 0^{+}} \frac{1 / h}{e^{1 / h}}=\lim_{t \rightarrow+\infty} \frac{t}{e^{t}} \cdot\) (Let \(t=1 / h .\) As \(\left.h \rightarrow 0^{+}, t \rightarrow+\infty .\right)\) This limit is \(0,\) e.g. by part \((\mathrm{a})\) Now \(q\) is an even function, so letting \(k=-h,\) the left side derivative \(=\lim_{h \rightarrow 0^{-}} \frac{q(h)-q(0)}{h}=\) \(\lim_{k \rightarrow 0^{+}} \frac{q(-k)}{-k}=\lim_{k \rightarrow 0^{+}} \frac{q(k)}{-k} .\) Using the earlier calculation this also equals \(-0=0\) Note: It is wrong to argue that \(q^{\prime}(0)=\lim_{x \rightarrow 0} q^{\prime}(x)\) because to do so, we first need to know that \(q^{\prime}\) is continuous at \(0,\) but we have not even shown that \(q^{\prime}(0)\) exists! For the same reason it is wrong to argue below that \(q^{(n)}(0)=\lim_{x \rightarrow 0} q^{(n)}(x)\)</p>

<br>

<p>
(c) We will show by induction on \(n\) that \(q^{(n)}(0)=0 .\) The case \(n=1\) is done. (We can even start the induction at \(n=0\) by interpreting \(q^{(0)}(x)=q(x) .\) ) Assuming that we are done up to \(n\) and to prove the statement for \(n+1,\) we need to calculate \(\lim_{h \rightarrow 0} \frac{q^{(n)}(h)-q^{(n)}(0)}{h}=\) \(\lim_{h \rightarrow 0} \frac{q^{(n)}(h)}{h},\) because \(q^{(n)}(0)=0\) by induction. Therefore it is good to examine \(q^{(n)}(h)\) for \(h \neq 0 .\) This is easy to calculate by the usual rules, but the formulas will be different for positive and negative \(h .\) For \(h \neq 0,\) as \(q\) is even, \(q^{\prime}\) is odd, so \(q^{\prime \prime}\) is even, etc. and in general \(q^{(n)}(h)=(-1)^{n} q^{(n)}(-h) .\) Therefore, just as for part (b), it suffices to show that \(\lim_{h \rightarrow 0^{+}} \frac{q^{(n)}(h)}{h}=0 .\) By another induction, we see easily that for \(h>0, q^{(n)}(h)=p(1 / h) e^{-1 / h}\)
for some polynomial \(p .\left[\right.\) Proof: \(q^{\prime}(h)=\left(\frac{1}{h^{2}}\right) e^{-1 / h} .\) Assuming the result for \(n,\) we have \(q^{(n+1)}(h)=\left[p(1 / h) e^{-1 / h}\right]^{\prime}=-\frac{1}{h^{2}}\left(-p(1 / h)+p^{\prime}(1 / h)\right) e^{-1 / h},\) which has the desired form.
</p>

<p>
So we have \(\lim_{h \rightarrow 0^{+}} \frac{q^{(n)}(h)}{h}=\lim_{h \rightarrow 0^{+}} \frac{p(1 / h) e^{-1 / h}}{h}=\lim_{t \rightarrow \infty} t p(t) e^{-t}=\lim_{t \rightarrow \infty} \frac{t p(t)}{e^{t}}=0\) by part (a). Here we have again substituted \(t=1 / h\)
</p>

</details>




