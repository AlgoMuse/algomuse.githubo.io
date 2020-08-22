---
layout: default
title: Trigonometry
nav_order: 95
---


# Trigonometry


### An easy problem
{: .d-inline-block }

A1, 2010
{: .label .label-blue}

<p>
Find all \(x\in[-\pi,\pi]\) such that \(\cos 3x + \cos x=0\).
</p>

<details><summary>Solution</summary>

<p>
\begin{array}%
\cos 3x+\cos x=4 \cos ^{3} x-3 \cos x + \cos x \\
\therefore 4 \cos ^{3} x-2 \cos x=0 \\
2 \cos x\left(\cos ^{2} x-\frac{1}{2}\right)=0
\end{array}
</p>

<p>
Either \(\cos x=0\) or \(\cos x = \pm\frac{1}{\sqrt{2}}\).
</p>


<p>
\begin{align}
\cos x&=0 \text { implies } x \in\left(\frac{\pi}{2},-\frac{\pi}{2}\right) \\
\cos x&=\frac{1}{\sqrt{2}} \text { implies } x \in\left(\frac{\pi}{4},-\frac{\pi}{4}\right) \\
\cos x&=-\frac{1}{\sqrt{2}} \text { imples } x \in\left(\frac{3 \pi}{4},-\frac{3 \pi}{4}\right)
\end{align}
</p>

<p>
Therefore, there are six solutions to the given equation.
</p>

</details>

---


### Intersection of a line and periodic function
{: .d-inline-block}

A1, 2012
{: .label}

Find the number of real solutions to the equation \(x=99 \sin (\pi x)\).

<details><summary>Solution</summary>

Since the equation is symmetric, if \(r\) is a solution then \(-r\) is also a solution. Hence, we restrict to finding the positive roots.
Note that \(x=0\) is also a root.


The function \(99 \sin \pi x\) is positive when \(2k < x < 2k+1 \). It equals x when \(x\leq 99\). The positive cycle of \(\sin\pi x\) meets \(y=x\) twice, so there are 198 positive solutions.
Counting the zero gives 199 solutions.

</details>

---

### A Saw-tooth function
{: .d-inline-block}

A9, 2015
{: .label}


Let \(f(x)=\sin ^{-1}(\sin (\pi x))\). Write the values of the following.

1. \(f(2.7)\)
1. \(f^{\prime}(2.7)\)
1. \(\int_{0}^{2.5} f(x) d x\)
1. The smallest positive \(x\) at which \(f^{\prime}(x)\) does not exist.

<details><summary>Solution</summary>


<p>
The graph of \(f\) is periodic with \(f(x)=f(x+2)\). It is defined as follows in the interval \((0,2)\).
</p>

<p>
 \[
f(x)= \begin{cases}
\pi x & 0\leq x \leq 0.5 \\
\pi-\pi x &  0.5 \leq x \leq 1.5  \\
\pi x & 1.5 \leq x \leq 2 \end{cases}
  \]
</p>

<img src="/assets/images/sawtooth.svg"/><br>

<p>
We can answer the questions by consulting the graph:
</p>

<ol>
<li> \(f(2.7)=f(0.7)=\pi- 0.7\pi=0.3\pi\) </li>
<li> \(f^{\prime}(2.7)=-\pi\)</li>
<li> \(\int_{0}^{2.5} f(x) d x=\int_{0}^{0.5} f(x) dx=\pi / 8\) </li>
<li> the smallest positive \(x\) at which \(f^{\prime}(x)\) does not exist is \(x=1/2\) </li>
</ol>


</details>

---

### Repeated saw-tooth
{: .d-inline-block}

A10, 2018
{: .label}


<p>
Recall that arcsin \(\left.(t) \text { (also known as } \sin ^{-1}(t)\right)\) is a function with domain [-1,1] and range \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right] .\) Consider the function \(f(x):=\arcsin (\sin (x))\) and answer the following questions as a series of four letters ( \(T\) for True and \(F\) for False) in order.
</p>

<ul>
<li> The function \(f(x)\) is well defined for all real numbers \(x\).</li>
<li> The function \(f(x)\) is continuous wherever it is defined.</li>
<li> The function \(f(x)\) is differentiable wherever it is continuous.</li>
</ul>


<details><summary>Solution</summary>

The problem is nearly the same as the previous problem from 2015 paper. From the graph, we see that only the last statement is false.

</details>

---


### Use of telescoping
{: .d-inline-block}

A5, 2015
{: .label}

<p>
Find the value of the following sum of 100 terms. (Possible hint: also consider the same sum with \(\sin ^{2}\) instead of \(\cos ^{2}\).)
</p>

<p>
\[
\cos ^{2}\left(\frac{\pi}{101}\right)+\cos ^{2}\left(\frac{2 \pi}{101}\right)+\cos ^{2}\left(\frac{3 \pi}{101}\right)+\cdots+\cos ^{2}\left(\frac{99 \pi}{101}\right)+\cos ^{2}\left(\frac{100 \pi}{101}\right)
\]
</p>


<details><summary>Solution</summary>


<p><i>A solution without using the hint.</i></p>

<p>
Let \( x = \frac{\pi}{101} \).
</p>

<p>
Since \( \cos^2x = (\cos 2x + 1 )/2 \), the given expression is:
</p>

<p>
\[
S = \frac{n}{2} + \frac{1}{2}\cdot \left( \cos 2x + \cos 4x + \cdots + \cos 2nx \right)\quad \text{where } n=100
\]
</p>



<p>
The following identity is useful:
</p>

<p>
\[ c=\cos 2 x+\cos 4 x+\cdots+\cos 2 n x=\frac{\sin n x \cos (n+1) x}{\sin x} \]
</p>

<p>
We can prove this as follows:
</p>

<p>
\(2 \sin x(\cos 2 x+\cos 4 x+\cdots+\cos 2 n x) \)
\(=[\sin 3 x-\sin x]+[\sin 5 x-\sin 3 x]+\cdots+[\sin (2 n+1) x-\sin (2 n-1) x]\)
\(=\sin (2 n+1) x-\sin x=2 \sin n x \cos (n+1) x \)
</p>

<p>
With this simplification the original expression becomes:
</p>

\begin{align}
S&=\frac{n}{2} + \frac{1}{2} \frac{\sin(100\pi/101) \cos \pi}{\sin \pi/101}  \\
\\
&=\frac{n}{2} + \frac{1}{2} = \frac{101}{2}
\end{align}

</details>

---

### Roots of unity to rescue
{: .d-inline-block}

B1, 2017
{: .label}

<p>
Let \(A=\frac{2 \pi}{9},\) i.e., \(A=40\) degrees. Calculate the following
\[
1+\cos A+\cos 2 A+\cos 4 A+\cos 5 A+\cos 7 A+\cos 8 A
\]
</p>


<details><summary>Solution</summary>


<p>
We look at \(\cos n A\) as the real part of \(e^{i n A}\).
</p>

<p>
\begin{align}
S &=\sum_{n=0}^{8} \cos n A-\sum_{n=1}^{2} \cos (3 n A) \\
&=\operatorname{Re}\left(\sum_{n=0}^{8} e^{i n A}-\sum_{n=1}^{2} e^{i n \frac{2 \pi}{3}}\right) \\
&=\operatorname{Re}\left(0-\omega-\omega^{2}\right) \quad \text{where } \omega \text{ is a complex cube root of unity} \\
&=1
\end{align}
</p>

</details>

---


### Geometric interpretation of algebraic expressions
{: .d-inline-block}

B5, 2019
{: .label}


<p>
Three positive real numbers \(x, y, z\) satisfy
</p>
<br>
<p>
\[
\begin{array}{r}
x^{2}+y^{2}=3^{2} \\
y^{2}+y z+z^{2}=4^{2} \\
x^{2}+\sqrt{3} x z+z^{2}=5^{2}
\end{array}
\]
Find the value of \(R = 2 x y+x z+\sqrt{3} y z .\)
</p>


<details><summary>Solution</summary>

<p> <i>The RHS of equations hints that a right angle triangle in involved. The LHS expressions resemble the cosine formulas. All we have to do is find an interpretation for \(x,y\) and \(z\). This is an artificial problem.
Students are expected to play guess-the-pattern game with the examiners. </i>
</p>




<p>
Consider the right angled triangle \(ABC\) with sides 3,4,5 and an interior point \(O\) such that \(A O=x, \angle A O B=90\) and \(C O=z, \angle C O A=150\) and \(B O=\) \(y, \angle B O C=120\).
Then the three given equations are in fact cosine rule for each of the triangle prescribed above.
</p>

<p>
For example, in \(\Delta BOC\) we have:
</p>

\begin{align}
4^{2} &=y^{2}+z^{2}-2 y z \cos (120) \\
&=y^{2}+z^{2}+y z
\end{align}

<p>If we divide the expression \(R\) by 4, we get:
\[ \frac{1}{2}xy\sin 90+\frac{1}{2}xz\sin 60 + \frac{1}{2}yz\sin 60 \]

The three terms are the areas of the interior triangles which should be equal to the area of triangle \(ABC\).

\[ 6=\frac{1}{2} x y+\frac{1}{2} y z \sin 60+\frac{1}{2} \sin 30 \]

So the answer is 24.
</p>

</details>








