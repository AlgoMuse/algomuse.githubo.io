---
layout: default
title: Trigonometry
nav_order: 92
---


# Trigonometry

### Impossible polynomial
{: .d-inline-block }

B4, 2021
{: .label .label-blue}

<p>
Show that there is no polynomial \(p(x)\) such that \(\cos \theta = p(\sin \theta)\) for every \(\theta\).

<details><summary>Solution</summary>
Put \( \theta = 0 \) and \(\theta = \pi\). Then \(p(0) = 1 \) and \(p(0)=-1\) which cannot be the case.
</details>
</p>

---

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
\cos x\left(\cos ^{2} x-\frac{1}{2}\right)=0
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


### Three arctans
{: .d-inline-block}

A10, 2021
{: .label}



<p> Let \(f(x) = \arctan(x) \) and \(g(v) = \int_0^{v} f(x) dx \).<br>


(a) \(f(1)=\pi/4\)<br>
(b) \(f(1)+f(2)+f(3)=\pi\) <br>
(c) \(g(v)\) is an increasing function in \( \mathbb{R} \).<br>
(d) \(g(v)\) is an odd function.<br>
</p>


<details><summary>Solution</summary>

<p>
(a) True.<br>
(b) True. See below. <br>
(c) False. \(g(-v) = - \int_{-v}^0 f(x) dx = g(v)\). So \(g\) is convex.<br>
(d) False. \(g\) is an even function.<br>

<i>Explanation for (b)</i>. Let \( \arctan(1)=x ; \arctan (2)=y ;\) and \(\arctan (3)=z\).<br>

\[\tan (x+y)=\frac{\tan x+\tan y}{1-\tan x \cdot \tan y}=\frac{1+2}{1-2}=-3\]

Put \(u = x+y\) and evaluate:
\[\tan (z+u)=\frac{\tan z+\tan u}{1-\tan z \cdot \tan u}=\frac{-3+3}{1-9}=0\]

So \( \tan( x+y+z ) = 0\).  Hence, \(\arctan (1)+\arctan (2)+\arctan (3)=x+y+z=\pi\).

<br>

</p>

</details>


---

### Intersection of a line and periodic function I
{: .d-inline-block}

A1, 2012
{: .label}

<p>
Find the number of real solutions to the equation \(x=99 \sin (\pi x)\).
</p>

<details><summary>Solution</summary>

<p>
Since the equation is symmetric, if \(r\) is a solution then \(-r\) is also a solution. Hence, we restrict to finding the positive roots.
Note that \(x=0\) is also a root.
</p>

<p>
The function \(99 \sin \pi x\) is positive when \(2k < x < 2k+1 \). It equals \(x\) when \(x\leq 99\). The positive cycle of \(\sin\pi x\) meets \(y=x\) twice, so there are 198 positive solutions.
Counting the zero gives 199 solutions.
</p>

</details>

---


### Intersection of a line and periodic function II
{: .d-inline-block}

A3, 2011
{: .label}

<p>
Find the number of solutions to the equation \(4 \sin (3x+2)=1\) in the domain \(x\in[0,2\pi]\).
</p>

<details open><summary>Solution</summary>

<p>
We want the number of intersection points between the line \(y=1\) and the periodic function \(f(x) = 4\sin (3x+2) \). The function \(f\) has period \(2\pi/3\). Between every maxima and a minima, there is exactly one solution.
</p>
<p>
At \(x=0\) and \(x=2\pi\), \(f\) is close to maxima. So all we need to do is find the number of minimas of \(f\) in the given domain and multiply it by 2.
</p>

<p style="text-align:center;"><img src="/assets/images/A3_2011.svg"></p>

<p>
The minimas occur at \(\displaystyle x=\left( \frac{\pi}{2}-\frac{2}{3} + \frac{2\pi k}{3}   \right)\) for \( k\in\{0,1,2\} \). Hence, there are six solutions to the given equation.
</p>



</details>

---


### A Saw-tooth function
{: .d-inline-block}

A9, 2015
{: .label}


Let \\(f(x)=\\sin ^{-1}(\\sin (\\pi x))\\). Write the values of the following.

1. \\(f(2.7)\\)
1. \\(f^{\\prime}(2.7)\\)
1. \\(\\int_{0}^{2.5} f(x) d x\\)
1. The smallest positive \\(x\\) at which \\(f^{\\prime}(x)\\) does not exist.

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

<i>The problem is nearly the same as the previous problem from 2015 paper. </i>

<p>From the graph, we see that only the last statement is false.</p>

</details>

---


### Use of telescoping
{: .d-inline-block}

A5, 2016
{: .label}

<p>
Find the value of the following sum of 100 terms.
</p>

<p>
\[
\cos ^{2}\left(\frac{\pi}{101}\right)+\cos ^{2}\left(\frac{2 \pi}{101}\right)+\cos ^{2}\left(\frac{3 \pi}{101}\right)+\cdots+\cos ^{2}\left(\frac{99 \pi}{101}\right)+\cos ^{2}\left(\frac{100 \pi}{101}\right)
\]
</p>

<p>
You may use this hint: also consider the same sum with \(\sin ^{2}\) instead of \(\cos ^{2}\).)
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
&=\frac{n}{2} - \frac{1}{2} = \frac{99}{2}
\end{align}

</details>

---

### Trignometric triangle inequality
{: .d-inline-block}

A10, 2010
{: .label}


<p>
Consider the following equations:
</p>

<p>
\[\cos x+\cos y+\cos z=\frac{3 \sqrt{3}}{2}\]
</p>
<p>
\[\sin x+\sin y+\sin z=\frac{3}{2}\]
</p>

<p>
Show that \(\displaystyle x=\frac{\pi}{6}+2 k \pi, y=\frac{\pi}{6}+2 \ell \pi, z=\frac{\pi}{6}+2 m \pi\) for some \(k, \ell, m \in \mathbf{Z}\).
</p>


<details><summary>Solution I</summary>
<i>Solution due to Piyush Jha.</i><br><br>
For any real numbers  \(a_{1}, \ldots, a_n\) and \(b_1, \ldots, b_n\), we know from Cauchy-Swarchz inequality that
\[
\left(\sum_{i=1}^{n} a_i b_i\right)^{2} \leq\left(\sum_{i=1}^{n} a_i^{2}\right)\left(\sum_{i=1}^{n} b_{i}^{2}\right)
\]
and equality holds if and only if there exists a nonzero constant \(\mu\) such that for all \(1 \leq i \leq n, \mu a_{i}=b_{i}\).<br>

Applying Cauchy-Swarchz inequality on \((\cos x, \cos y, \cos z)\) and on \((1,1,1)\) we get

\begin{align}
(\cos x+\cos y+\cos z)^{2} &\leq\left((\cos x)^{2}+(\cos y)^{2}+(\cos z)^{2}\right)\left(1^{2}+1^{2}+1^{2}\right) \\
\frac{9}{4} &\leq \left((\cos x)^{2}+(\cos y)^{2}+(\cos z)^{2}\right)
\end{align}

Now applying same on \( (\sin x, \sin y, \sin z)\) and \((1,1,1)\) gives:

\begin{align}
\frac{9}{4}& \leq\left(\sin^{2} x+\sin ^{2} y+\sin^{2} z\right)\left(1^{2}+1^{2}+1^{2}\right)\\
\frac{3}{4}& \leq\left(1-\cos ^{2} x+1-\cos ^{2} y+1-\cos ^{2} z\right)\\
\frac{9}{4}& \geq\left(\cos^{2} x+\cos ^{2} y+\cos ^{2} z\right)
\end{align}

which implies that \( \cos^{2} x+\cos^{2} y+\cos^{2} z=\frac{9}{4}\), that means Cauchy-Schwarz inequality is tight and there must exist
a \(\kappa\) such that \(\cos x = \cos y = \cos z = \kappa\). From the problem statement \(\kappa = \frac{\sqrt{3}}{2}\) and the solution follows.
</details>

<p></p>

<details><summary>Solution II</summary>

<p>
Squaring both the equations and adding gives:
</p>

\[(\cos x+\cos y+\cos z)^{2}+(\sin x+\sin y+\sin z)^{2}=9\]

\[\Rightarrow \cos (x-y)+\cos (y-z)+\cos (z-x)=3\]

<p>The maximum value of \(\cos \theta\) is 1. So, the above equation can be satisfied with equality only when each of the terms is 1. This implies
that the only solutions are those that are given in the problem.</p>

<p><i>Altenatively, we can use complex numbers and triangle inequality to prove the statement</i></p>

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

<p>The RHS of equations hints that a right angle triangle is involved. The LHS expressions resemble the cosine formulas. All we have to do is find an interpretation for \(x,y\) and \(z\).</p>


<p>
Consider the right angled triangle \(ABC\) with sides 3,4,5 and an interior point \(O\) such that \(A O=x, \angle A O B=90\) and \(C O=z, \angle C O A=150\) and \(B O=\) \(y, \angle B O C=120\).
Then the three given equations are in fact cosine rule for each of the triangle prescribed above.
</p>


<p style="text-align:center;"><img src="/assets/images/B5_2019.svg"></p>


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


<i>This is an artificial problem.  Students are expected to play guess-the-pattern game with the examiners.</i>


</details>








