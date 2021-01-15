---
layout: default
title: Derivatives
parent: Calculus
nav_order: 2
---


# Continuity and differentiability of functions



### Maximize area of a rectangle
{: .d-inline-block}

A3, 2019
{: .label}


<p>There is a piece of land next to a straight river. You are required to cut off a rectangular portion of the land,
with the river forming one of the sides of the rectangle. The fence will have three sides to it.
You have 60 meters of fencing. What is the maximum area that you can enclose?
</p>


<details><summary>Solution</summary>

<p>
Let the length and width of the rectangular fence be \(x\) and \(60-2x\), respectively. The area of the enclosure is:
</p>


<p style="text-align:center;"><img src="/assets/images/cmi2019_a3.svg"></p>

<p>
\[ A(x) = (60-2x)x \]
</p>

<p>
which is maximized when \(A^{\prime}=0=60-4x\). Hence, \(x\) should be \(15\) meters. Thus the maximum enclosure is 450 sq.mts.
</p>


</details>

---

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


<details><summary>Solution</summary>

<p>
False-True-True-False.
</p>

<p>
If \(g\left(x_{1}\right)=g\left(x_{2}\right),\) then \(x_{1}=f\left(g\left(x_{1}\right)\right)=f\left(g\left(x_{2}\right)\right)=x_{2},\) so \(g\) is one-to-one. Also \(f\) is onto because each \(x \in T\) is in the image of \(f,\) namely \(x=f(g(x)) .\) The other two statements are false, for example by constructing an \(S\) that is a larger finite set than \(T\).
</p>

</details>

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

<details><summary>Solution</summary>

<p>
True-False-True-True
</p>

<p>
In parts a and b, we have \(|f(x)-f(a)|\) lying between \(\pm 39|x-a| .\) As \(x \rightarrow a\) \(\pm 39|x-a| \rightarrow 0\) and hence \(f(x)-f(a) \rightarrow 0,\) so \(f\) is continuous. But it need not be differentiable, for example \(f(x)=|x|\) satisfies \(f(x)-f(y)=|x|-|y| \leq|x-y| \leq 39|x-y| \cdot\) But \(f\) is not differentiable at \(0 .\)
</p>

<p>
In parts c and d, we have \(\left|\frac{f(x)-f(a)}{x-a}\right| \leq 39|x-a|,\) so by reasoning as for part a, we have \(\lim_{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=0,\) i.e., \(f^{\prime}(a)=0\) for all \(a,\) so \(f\) is a constant function.
</p>

</details>

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

<details><summary>Solution</summary>

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


</details>

---

### Continuity on tangents and secants
{: .d-inline-block}

A9, 2016
{: .label}


<p>Given a continuous function \(f\), define the following subsets of the set \(\mathbb{R}\) of real numbers.</p>

<p>\(T=\) set of slopes of all possible tangents to the graph of \(f\)</p>

<p>\(S=\) set of slopes of all possible secants, i.e. lines joining two points on the graph of \(f\)</p>

<p>(i) If \(f\) is differentiable, then \(S \subset T\).</p>
<p>(ii) If \(f\) is differentiable, then \(T \subset S\).</p>
<p>(iii) If \(T=S=\mathbb{R},\) then \(f\) must be differentiable everywhere.</p>
<p>(iv) Suppose 0 and 1 are in \(S\). Then every number between 0 and 1 must also be in \(S\).</p>

<details><summary>Solution</summary>

<p>TFFT</p>

<p>i The mean value theorem tells us \(S \subset T\).</p>

<p>ii \(T \subset S\) is false, example \(f(x)=\sin (x) .\) Here \(f^{\prime}(0)=1\) is in \(T\) but not in \(S\).</p>

<p>iii \(T=S=\mathbb{R}\) can happen at points where \(f\) is not differentiable.</p>

<p>iv \(S\) has mean value property, because of continuity. (TODO)</p>

</details>

---

### Irrationality and continuity
{: .d-inline-block }

A6, 2016
{: .label}


<p>
A function \(f(x)\) is defined by the following formulas
\[
f(x)=\left\{\begin{array}{ll}
x^{2}+1 & \text { when } x \text { is irrational } \\
\tan (x) & \text { when } x \text { is rational. }
\end{array}\right.
\]
</p>

<p>
At how many \(x\) in the interval \([0,4 \pi]\) is \(f(x)\) continuous?
</p>


<details><summary>Solution</summary>
<p> The given function is defined using the two functions \(x^{2}+1\) and \(\tan (x)\).</p>

<p>
Both these functions are continuous wherever they are defined. As every irrational number \(z\) has a non terminating,
non repeating decimal expansion we see that given any \(\epsilon>0\) there is a rational number \(p\) such that the distance between \(z\) and \(p\) is less than \(\epsilon\).
</p>


<p>
Using these facts we see that the given function is continuous precisely at those \(x\) in the interval \([0,4 \pi]\) where \(x^{2}+1=\tan (x)\), since \(x^{2}+1\) is positive, it will intersect \(\tan (x)\) exactly once in the intervals \(\left[0, \frac{\pi}{2}\right],\left[\pi, \frac{3 \pi}{2}\right],\left[2 \pi, \frac{5 \pi}{2}\right],\left[3 \pi, \frac{7 \pi}{2}\right],\) as \(\tan (x)\) increases from 0 to \(\infty\) in each of these intervals. \(\tan (x)\) is negative elsewhere in the given domain.
So we have 4 points of continuity.  </p>


</details>

---

### Strange question
{: .d-inline-block}


B3, 2017
{: .label }

<p>
Suppose \(p(x)\) be a polynomial of degree strictly less than hundred and such that  \(x^{3}-x\) is not one of its factors. If
\[ \frac{d^{100}}{d x^{100}}\left(\frac{p(x)}{x^{3}-x}\right)=\frac{f(x)}{g(x)} \]
for some polynomials \(f(x)\) and \(g(x)\) then find the smallest possible degree of \(f(x)\).
</p>

<details><summary>Solution</summary>
<p>
Put \(p(x)=x^2-1\), then

\begin{align}
\frac{d^{100}}{d x^{100}}\left(\frac{p(x)}{x^{3}-x}\right)=\frac{d^{100}}{d x^{100}}\left(\frac{1}{x}\right) = \frac{-100!}{x^{100}}
\end{align}

Hence, \(f(x)\) can have degree 0.
</p>






</details>

<p><i><b>Reference</b>. This problem is taken from Putnam 1992 competition, but with a typo that trivializes the problem. See the intended problem and the solution <a href="https://prase.cz/kalva/putnam/psoln/psol9210.html">here</a>.</i></p>
<p>
<i>To make the problem interesting one needs to state that neither 0,-1 or 1 are the roots of \( p(x) \) as stated in the original Putnam problem.</i>
</p>








---

### Inflection point
{: .d-inline-block}

A6, 2017
{: .label}


<p>Let \(g\) be a function such that all its derivatives exist. <br>

We say \(g\) has an inflection point at \(x_{0}\) if the second derivative \(g^{\prime \prime}\) changes sign at \(x_{0}\) i.e., if \(g^{\prime \prime}\left(x_{0}-\epsilon\right) \times g^{\prime \prime}\left(x_{0}+\epsilon\right)<0\) for all small enough positive \(\epsilon\).</p>

<p>(a) Find all values \(x_{0}\) at which \(g(x) = x^{4}(x-10)\) has an inflection point.</p>

<p>(b) If \(g^{\prime \prime}\left(x_{0}\right)=0\) then \(g\) has an inflection point at \(x_{0}\). Is this true? </p>

<p>(c) If \(g\) has an inflection point at \(x_{0}\) then \(g^{\prime \prime}\left(x_{0}\right)=0.\). Is this true? </p>


<details><summary>Solution</summary>

<p>(a) \(g^{\prime \prime}(x)=20 x^{3}-120 x^{2}=20 x^{2}(x-6)\) and this changes sign only at \(x=6 .\) </p>

<p>(b) is false. Consider the function above: \(g^{\prime \prime}(0)=0\) but \(g^{\prime \prime}\) does not change sign at \(x=0\). </p>

<p>(c) is true due to continuity. The function \(g\) is continuous since it is differentiable.</p>

</details>

---

### Concave function
{: .d-inline-block }

A6, 2020
{: .label}


<p>
Suppose \(a=20202019\) and \(b=20202021\). Fill in the blank with either \(<, >\) or \(=\).

\[ \tan^{-1} a + \tan^{-1} b \underline{\hspace{1cm}}  2 \tan^{-1} ( \frac{a+b}{2} ) \]

Hint: Look at the second derivative.
</p>

<details><summary>Solution</summary>
<p>

Let \(f(x) := \tan^{-1}x \).

\begin{align}
f^\prime(x) &= \frac{1}{1+x^2} \\
f^{\prime\prime}(x) &= \frac{-2x}{ (1+x^2)^2 } \\
\end{align}

In the domain \( (0,\infty) \), the second derivative is strictly negative. This means that
\( f(x) \) is strictly concave in this domain. Therefore \( f(x) + f(y) < 2 f( (x+y)/2) \) for any \(x,y \in (0,\infty) \).

</p>

</details>

---


### Differentiability I
{: .d-inline-block}

A3, 2014
{: .label}

<p>Given a real number \(x,\) define \(g(x)=x^{2} e^{x}\) if \(x \geq 0\) and \(g(x)=x e^{-x}\) if \(x<0\)</p>
<p>(A) The function \(g\) is continuous everywhere.</p>
<p>(B) The function \(g\) is differentiable everywhere.</p>
<p>(C) The function \(g\) is one-to-one.</p>
<p>(D) The range of \(g\) is the set of all real numbers.</p>

<details><summary>Solution</summary>
TFTT
</details>

---

### Longest diagonal in a box
{: .d-inline-block}

A12, 2014
{: .label}

<p>The total length of all 12 sides of a rectangular box is \(60 .\) (i) Write the possible values of the volume of the box. Your answer should be an interval. Now suppose in addition that the surface area of the box is given to be \(56 .\) Find, if you can, (ii) the length of the longest diagonal of the box (iii) the volume of the box.</p>

<details><summary>Solution</summary>
\((0,125], 13,\) not possible to decide
</details>


---


### Differentiable piece function
{: .d-inline-block}

A5, 2011
{: .label}


<p>
A function \(f\) is defined by \(f(x)=e^{x}\) if \(x<1\) and \(f(x)=\log_{e}(x)+a x^{2}+b x\) if \(x \geq 1\). Here \(a\) and \(b\) are unknown real numbers. Can \(f\) be differentiable at \(x=1 ?\)
</p>

- [ ] \\(f\;\\) is not differentiable at \\(\;x=1\;\\) for any \\(\;a\;\\) and \\(\;b\\).
- [ ] There exist unique numbers \\(\; a \;\\) and \\(\; b \;\\) for which \\(\;f\;\\) is differentiable at \\(\;x=1\\).
- [ ] \\(f\;\\) is differentiable at \\(\; x=1\;\\) whenever \\(\; a+b=e\\).
- [ ] \\(f\;\\) is differentiable at \\(\; x=1\;\\) regardless of the values of \\(\; a\\) and \\(\; b\\).

<details><summary>Solution</summary>

<p>
Option (B). There are unique values of \(a\) and \(b\) for which \(f\) is differentiable at \(x=1\).
</p>


<p>
For the function to be continuous at \(x=1\), we must have \( a+b = e \). For the function to be differentiable:
</p>

<p>
\[ e^x = \frac{1}{x} + 2ax + b \;\;\;\text{ at }\; x=1 \]
</p>

<p>
This means at \( x= 1\), we must have \( a=-1\) and \( b=e+1 \) for the function to be differentiable.
</p>



</details>

---

### Only one real root
{: .d-inline-block }

A8, 2011
{: label .label-blue}


<p>
Suppose \(f(x) = x^3 + x^2 + cx + d\), where \(c\) and \(d\) are real numbers. Prove that if \(c>1/3\),
then \(f\) has exactly one real root.
</p>


*Requires algebra too*.

<details><summary>Solution</summary>

<p>
Since the function has odd degree as the highest power, it has at least one
real root. To show that the function has exactly one real root
we have to show, that it is monotonic in the whole \(\mathbb{R}\).
This can be done by showing that \(f'(x)\) is always positive when \(c>1/3\).
</p>

<p>
\[ f'(x) = 3x^2+2x+c \]
</p>

<p>
The discriminant of the above quadratic, \(2^2-4\cdot3\cdot c\), is negative when \(c>1/3\).
Hence, \(f'(x)\) is always positive in \(\mathbb{R}\).
</p>

</details>

---
### Rolle's theorem I
{: .d-inline-block }

A2, 2012
{: .label}


<p>
A differentiable function \(f: \mathbb{R} \rightarrow \mathbb{R}\) has the following values: \(f(1)=2, f(2)=4\) and \(f(3)=1 \).
Show that \(f^{\prime}(x)=0\) for some \(x\).
</p>

<details><summary>Solution</summary>

<p>
Since \(f\) is differentiable, it must be continuous. By continuity, there is \(a \in(2,3)\) with \(f(a)=2=f(1)\).
Rolle's theorem says that there is \(x \in(1, a)\) with \(f^{\prime}(x)=0\).
</p>

</details>

---

### Rolle's theorem II
{: .d-inline-block }

B9, 2011
{: label .label-blue}

<p>
A real-valued function \(f(x)\) defined on a closed interval \([a,b]\) has the property
that \(f(a)=f(b)=0\) and \(f(x)=f'(x)+f^{\prime\prime}(x)\) for all \(x\) in \([a,b]\). Show that \(f(x)=0\) for
all \(x\) in \([a,b]\).
</p>

<details><summary>Solution</summary>

<p>
If \(f(x)\) is not constant, then it must attain a local maxima or minima at some value \(c\in[a,b]\).
</p>

<p>
From the condition specified:
</p>

<p>
\begin{equation}
f(c)=f'(c)+f^{\prime\prime}(c)
\label{eq:rolle}
\tag{1}
\end{equation}
</p>


<p>
If \(f(c)\) is the local maxima, then \(f(c)>0\), \(f'(c)=0\) and
\(f^{\prime\prime}(c)<0\). But Eq.\(\eqref{eq:rolle}\) does not hold in that case. A similar argument holds for local minima. Hence, \(f(x)\) is zero in the interval \([a,b]\).
</p>



</details>

---


### A simple substitution
{: .d-inline-block }

A2, 2019
{: label .label-blue}


<p>
Let \(f\) be a real valued continuous function defined on \(\mathbb{R}\) satisfying
\(f^{\prime}\left(\tan ^{2} \theta\right)=\cos 2 \theta+\tan \theta \sin 2 \theta,\) for all real numbers \(\theta\)
If \(f(0)=-\cos \frac{\pi}{12}\) then find \(f(1)\)
</p>

<details><summary>Solution</summary>

<p>
Substitute \(t=\tan^{2} \theta \). Then we have
</p>

<p>
\begin{align}
f'(\tan^2\theta) & = \cos 2\theta(1+\tan \theta \tan 2\theta ) \\
f'(\tan^2\theta) & = \frac{1-\tan^2\theta}{1+\tan^2\theta} \left( 1 + \frac{2\tan^2\theta}{1-\tan^2\theta} \right) \\
f'(t) & = \frac{1-t}{1+t} \left( 1 + \frac{2t}{1-t} \right) \quad\text{ where } t=\tan^2 \theta \\
f'(t) & = 1 \\
f(t) & = t + constant
\end{align}
</p>


<p>
Hence the answer is \(1-\cos \frac{\pi}{12}\).
</p>

</details>

---

### Application of Rolle's theorem
{: .d-inline-block }


A7, 2014
{: .label}

<p>
Let \(f(x)=(x-a)(x-b)^{3}(x-c)^{5}(x-d)^{7},\) where \(a, b, c, d\) are real numbers with \( a < b < c < d \).
Thus \(f(x)\) has 16 real roots counting multiplicities and among them 4 are distinct from each other.
Consider \(f^{\prime}(x),\) i.e. the derivative of \(f(x)\). Find the following quantities:<br>

(i) the number of real roots of \(f^{\prime}(x),\) counting multiplicities.  <br>

(ii) the number of distinct real roots of \(f^{\prime}(x)\).<br>
</p>

<details><summary>Solution</summary>

<p>
15,6
</p>


</details>

---

### Monotonic again
{: .d-inline-block}

B1c, 2017
{: label .label-blue}


<p>
Find the number of solutions to \(e^{x}=\frac{x}{2017}+1\)
</p>

<details><summary>Solution</summary>

<p>
This problem is similar to the last one. We need to show that the function is monotonic in some interval.
</p>

<p>
Consider the function:
\begin{align}
f(x)&=  e^x -\frac{x}{2017} - 1 \\
f'(x)&=  e^x -\frac{1}{2017}
\end{align}
</p>


<p>
The derivative is positive when \(x> x_0=-\log 2017\).
</p>

<p>
<ul>
<li>We have \(f(x_0)< 0\) and \( f(-\infty)>0 \) so there is one solution in the interval \((-\infty,x_0)\).</li>
<li>\( x = 0 \) is another solution.</li>
</ul>
</p>

<p>
Hence, there are two solutions to the equation.
</p>


</details>

---

### Asymptotes of a function
{: .d-inline-block}

A10, 2013
{: .label}


<p>
Let
</p>

<p>
\[ f(x)=\frac{x^{4}}{(x-1)(x-2) \cdots(x-n)} \]
</p>

<p>
where the denominator is a product of \(n\) factors, \(n\) being a positive integer. It is also given that the X-axis is a horizontal asymptote for the graph of \(f\). Answer these four questions.
<br>
(i) How many vertical asymptotes does the graph of \(f\) have?
<br>
(a) \(n\)<br>
(b) less than \(n\)<br>
(c) more than \(n\)<br>
(d) impossible to decide <br>
<br>

(ii) What can you deduce about the value of \(n ?\)
<br>
(a) \(n<4\)<br>
(b) \(n=4\)<br>
(c) \(n>4\)<br>
(d) impossible to decide
<br>
<br>
(iii) As one travels along the graph of \(f\) from left to right, at which of the following points is the sign of \(f(x)\) guaranteed to change from positive to negative?
<br>
(a) \(x=0\) <br>
(b) \(x=1\) <br>
(c) \(x=n-1\) <br>
(d) \(x=n\) <br>
<br>
<br>
(iv) How many inflection points does the graph of \(f\) have in the region \(x<0 ?\)
<br>
(a) none <br>
(b) 1 <br>
(c)  more than \(1 \quad\) <br>
(d) impossible to decide.<br>


(It is better to sketch than calculate).
</p>

<details><summary>Solution</summary>

<p>
(i) \(n\) at \(x=1,2, \ldots, n\).
</p>

<p>
(ii) \(n>4,\) because \(\lim_{x \rightarrow \pm \infty} f(x)=0\) and for this to happen, the degree of the denominator of \(f(x)\) must be greater than that of the numerator.
</p>

<p>
(iii) \(x=n-1,\) because \(f(x)\) is positive for \(x> n\) and \(f(x)\) changes sign precisely when it passes through \(x=1,2 \ldots, n .\) Note that the sign of \(f(x)\) for \(x<0\) and for \(x \in(0,1)\) depends on the parity of \(n\)
</p>

<p>
(iv) More than \(1 .\) Note that \(f(x)=0\) only at \(x=0,\) with multiplicity \(4 .\) Without loss of generality, let \(n\) be even.
Now \(f(x)> 0\) for \(x<1\) except at \(x=0\) and \(f\) has all derivatives for \(x<1\).
Due to the multiple root at \(x=0,\) the graph of \(f\) must be concave up, that is \(f^{\prime \prime}(x)> 0\) ) near \(x=0\).
Further, as \(x \rightarrow-\infty,\) the values of \(f(x)\) stay positive and \(\rightarrow 0\).
</p>

<p>
Therefore, as one traces the graph from from the origin to the left, it must become concave down at least
once and eventually concave up again so as to approach the X-axis from above.
</p>

</details>

---

### Span of the a function
{: .d-inline-block}

B5, 2013
{: .label}


<p>
Consider the function \(f(x)=a x+\frac{1}{x+1},\) where \(a\) is a positive constant. Let \(M=\) the largest value of \(f(x)\) and \(N=\)
the smallest value of \(f(x)\) for \(x \in[0,1] .\) Show that \(M-N>\frac{1}{12}\) for any \(a>0\).
</p>


<details><summary>Solution</summary>


<p>
We have \(f(0)=1, f(1)=a+\frac{1}{2}\) and \(f^{\prime}(x)=a-\frac{1}{(x+1)^{2}}\) Over the interval \([0,1],\) the value of \(f^{\prime}(x)\) increases from \(a-1\) at \(x=0\) to \(a-\frac{1}{4}\) at \(x=1\)o
</p>

<p>
What happens to the sign of \(f^{\prime}(x)\)? We do a case by case analysis.
</p>

<p>
<b>Case 1</b>. Suppose \(a \leq 1 / 4 .\) Because \(1 /(x+1)^{2} \geq 1 / 4\) on the interval \([0,1], f^{\prime}(x) \leq 0,\) so the maximum is at 0 and the minimum is at \(x=1\). So the difference is \(1-(1 / 2+a)=\) \(1 / 2-a \geq 1 / 4 \geq 1 / 12\)
</p>


<p> </p>

<p>
<b>Case 2.</b> Suppose \(a \geq 1\). Then \(f^{\prime}(x) \geq 0\) on the interval [0,1] , so maximum is at 1 and minimum at
0. We get \(a+1 / 2-1=a-1 / 2 \geq 1 / 2 \geq 1 / 12\)
</p>

<p> </p>
<p>
<b>Case 3.</b> Suppose \(1 / 4 \leq a \leq 1 .\) Now \(f^{\prime}(x)=0\) at \(\tilde{x}=\frac{1}{\sqrt{a}}-1 .\) For this range of \(a, \tilde{x} \in[0,1]\) In the interval \([0, \tilde{x}], f^{\prime}(x) \leq 0\) and in the interval \([\tilde{x}, 1], f^{\prime}(x) \geq 0 .\) Now we make two sub-cases depending on the endpoint at which the maximum occurs.
</p>

<p> </p>
<p>
<b>Case 3a.</b> Suppose \(1 / 4 \leq a \leq 1 / 2\). Then \(f(0) \geq f(1)\). So minimum is at \(\tilde{x},\) maximum is at \(x=0 . f(\tilde{x})=\sqrt{a}-a+\sqrt{a}=2 \sqrt{a}-a\). So the difference between maximum and minimum is \(1+a-2 \sqrt{a}=(1-\sqrt{a})^{2}\). This is smallest when \(\sqrt{a}\) is closest to 1 and so \((1-\sqrt{a})^{2} \geq(1-1 / \sqrt{2})^{2}=3 / 2-\sqrt{2} .\) This is bigger than \(1 / 12\) since \(\left(\frac{3}{2}-\frac{1}{12}\right)=17 / 12\) and
\(17^{2}=289 \geq 2 \times 12^{2}\)
</p>

<p> </p>

<p>
<b>Case 3b.</b> Suppose \(1 / 2 \leq a \leq 1\). Now \(f(1) \geq f(0)\). Max is at 1 and minimum is at \(\tilde{x}\). The difference is \(a+1 / 2-\sqrt{a}+a-\sqrt{a}=2 a-2 \sqrt{a}+1 / 2=\left(\sqrt{2 a}-\frac{1}{\sqrt{2}}\right)^{2} .\) By a calculation
similar to the above it is bigger than \(1 / 12\).
</p>


</details>


---

### Spider walk
{: .d-inline-block}

B3, 2020
{: .label}


<p>
A spider is moving along the curve \(y=x^3\) in the positive \(x-\)direction. It moves along the curve with a constant speed of \(10\) cm per second.
The spider has woven a web that connects it to the origin. The strand connecting it to the origin is taut. Find the rate of increase of the length of
the strand when \(x=\frac{1}{2}\).
</p>

<p style="text-align:center;">
<img src="/assets/images/cubic_curve.svg">
</p>


<details><summary>Solution</summary>
Let \(v_x\) and \(v_y\) define the horizontal and vertical components of the velocity of the spider. Since the speed of the spider is constant we have:

\[ \sqrt{v_x^2 + v_y^2} = 10 \mbox{ cm/s} \]


\begin{align}
y &= x^3 \\
\frac{dy}{dt} &= 3x^2 \frac{dx}{dt} \\
v_y &= 3x^2 v_x
\end{align}

When the spider is at \(x=1/2\), we have \( v_y = 3v_x/4 \). Since the speed is constant:

\begin{align}
\sqrt{ v_x^2 + \frac{9v_x^2}{16}  }  &= 10\\
\sqrt{ \frac{25v_x^2}{16} }  &= 10 \\
\frac{5v_x}{4} &= 10 \\
v_x &= 8 \mbox{ cm/s} \\
v_y &= 3v_x/4  = 6 \mbox{ cm/s}
\end{align}

We know the velocity at \(x=1/2\). Let us calculate \(dl/dt\), the rate of increase of the strand length at that moment.

\begin{align}
l  &= \sqrt{ x^2 + y^2 } \\
\frac{dl}{dt} &= \frac{1}{2\sqrt{ x^2 + y^2 }} \left(  2x\frac{dx}{dt} + 2y\frac{dy}{dt}  \right) \\\\
&= \frac{1}{\sqrt{ (1/2)^2 + (1/8)^2 }} \left(  \frac{1}{2}\cdot 8  +  \frac{1}{8} \cdot 6  \right) \\\\
&= \frac{4+3/4}{ \sqrt{\frac{1}{2^2}+\frac{1}{8^2}} } \\
&= \frac{38}{\sqrt{17}}\\
\frac{dl}{dt}&\approx 9.2 \mbox{ cm/s}
\end{align}
</details>


---






### Double derivatives
{: .d-inline-block}

A4, 2015
{: .label}

<p>Let \(A, B\) and \(C\) be unknown constants. Consider the function \(f(x)\) defined by</p>

<p>
\begin{align}
f(x) &=A x^{2}+B x+C \text { when } x \leq 0 \\
&=\ln (5 x+1) \text { when } x>0
\end{align}
</p>

<p>Write the values of the constants \(A, B\) and \(C\) such that \(f^{\prime \prime}(x),\) i.e., the double derivative of \(f,\) exists for all real \(x \). </p>


<details><summary>Solution</summary>

<p>The only problem is at \(x=0 .\) For continuity, \(\ln (0+1)=C\).</p>

<p>For \(f^{\prime}(0)\) to exist, \(f\) must be continuous and the left and right derivatives of \(f\) at \(x=0\) (which are easily seen to exist) must match, that is \(5=B\).</p>

<p>For \(f^{\prime \prime}(0)\) to exist, \(f^{\prime}(0)\) must exist and left and right derivatives of \(f^{\prime}\) at \(x=0\) must match, i.e. \(2 A=-5^{2} .\) So \(A=-\frac{25}{2}, B=5, C=0\).</p>

</details>

---

### Function with a maximum
{: .d-inline-block}

B1b, 2018
{: .label}


<p>
Suppose \(f\) is a differentiable function defined on a subset \(S\) of \(\mathbb{R}\). Define
\[
f^{\ast}(y):=\max_{x \in S}\{y x-f(x)\}
\]
whenever the above maximum is finite. For the function \(f(x)=-\ln (x),\) determine the set of points for which \(f^{\ast}\) is defined and find an expression for \(f^{\ast}(y)\) involving only \(y\) and constants.
</p>

<details><summary>Solution</summary>
First, note that the function \(f(x)\) is defined only for the positive values of \(x\).

Now if \(y \geq 0\) then the first derivative of \(x y+\ln (x)\) is \(y+\frac{1}{x}\) which is strictly positive for \(x>0 .\) Hence \(x y+\ln (x)\) is an increasing function and consequently \(f^{\ast}(y)\)
is not defined. Now if \(y<0\) then \(x=-\frac{1}{y}\) is the only critical point of \(x y+\ln (x)\). Either of the derivative test tells us that it is in fact the maxima. Hence, the domain of \(f^{\ast}(y)\) is \(y<0\) and

\[
f^{\ast}(y)=\ln \left(\frac{-1}{y}\right)-1
\]


</details>


