---
layout: default
title: Integrals
parent: Calculus
nav_order: 3
---


# Integrals



### A routine substitution
{: .d-inline-block }

A4, 2018
{: .label}

<p>Evaluate:</p>

<p>
\[I = \int_{0}^{\frac{\pi}{2}} \frac{d x}{(\sqrt{\sin x}+\sqrt{\cos x})^{4}}\]
</p>


<details><summary>Solution</summary>

<p>
Multiply both the numerator and denominator by \(\sec^2 x\).
</p>

<p>
\begin{align}
& I =\int_{0}^{\pi / 2} \frac{\mathrm{sec}^{2} x \mathrm{d} x}{(\sqrt{\tan x}+1)^{4}} \\\\
\mathrm{let} \tan x=t^{2} & \Rightarrow \sec^2 x \mathrm{d} x=2 t\mathrm{d}t \\\\
\Rightarrow \quad & I =\int_{0}^{\infty} \frac{2t \mathrm{d}t}{(t+1)^{4}} \Rightarrow I =\int_{0}^{\infty}\left[\frac{2}{(t+1)^{3}}-\frac{2}{(t+1)^{4}}\right] \mathrm{d}t \\
\Rightarrow \quad & I=\left.\frac{-1}{(\mathrm{t}+1)^{2}}+\frac{2}{3(\mathrm{t}+1)^{3}}\right\rvert_{0}^{\infty} \\
\Rightarrow \quad & I=\frac{1}{3}
\end{align}
</p>
</details>


---

#### Problem credits

<img src="/assets/images/smt.png" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
The Stanford Math Tournament (SMT) is an annual student-run math competition for high school students. It has been running since 1999.
The above problem is taken from its <a href="https://sumo.stanford.edu/pdfs/smt2013/calculus-problems.pdf">2013 calculus question paper</a> (P9).
</p>
{: .fs-4 .fw-300 }

---


### Absolute integrals
{: .d-inline-block}

A7, 2017
{: .label}

<p>Evaluate: </p>

<p>(a) \(\int_{-3}^{3}\left|3 x^{2}-3\right| d x\)</p>

<p>(b) \(f^{\prime}(1)\) where \(f(t)=\int_{0}^{t}\left|3 x^{2}-3\right| d x\)</p>

<details><summary>Solution</summary>

 <p>(a) Due to symmetry, we can double the integral from 0 to 3. So the value is \(2I\), where:</p>

<p>
\begin{align}
I &=\int_{0}^{1} (3-3x^{2}) \text{d}x  +  \int_{1}^{3} (3 x^{2}-3) \text{d}x  \\
  &=\left. 3x-x^3 \right\rvert_{0}^1  +  \left. (x^{3}-3x)\right\rvert_{1}^3  \\
  &=2 + 20 \\
  &=22\\
\end{align}


Hence, \(\int_{-3}^{3}\left|3 x^{2}-3\right| d x = 44 \).

</p>

<p></p>

<p>(b) \(\left|3 x^{2}-3\right|\) is a continuous function so by the fundamental theorem of calculus, \(f^{\prime}(1)=\) \(\left|3 \times 1^{2}-3\right|=0\)</p>


</details>


---


### Volume of a cave
{: .d-inline-block}

B7, 2011
{: .label}


<p>
In this problem we want to find the volume of a cave described by equations. The base of the cave is in the XY-plane and
the vertical direction is parallel to the Z-axis. The base of the cave lies in the XY-plane bounded by the parabola \(y^{2}=1-x\)
and the Y-axis. Each cross-section of the cave perpendicular to the X-axis is a square.
</p>

<p>(a) Show how to write a definite integral that will calculate the volume of this cave.</p>

<p></p>

<p>(b) Evaluate this definite integral. Can you find the volume without using indefinite integrals?</p>


<details><summary>Solution</summary>

<p>(a) The volume of the cave is given by the following triple integral:</p>

<p>
\[ \int_{x=0}^{1} \int_{y=-\sqrt{1-x}}^{\sqrt{1-x}} \int_{z=0}^{2\sqrt{1-x}} \mathrm{d}x \mathrm{d}y \mathrm{d}z \]

(b)

\[ \int_{x=0}^{1} \int_{y=-\sqrt{1-x}}^{\sqrt{1-x}}  2\sqrt{1-x}\; \mathrm{d}x \mathrm{d}y  \]

\[ \int_{x=0}^{1} 4(1-x) \mathrm{d}x = 2 \text{m}^3 \]

</p>

<p>Here is an alternate way to find the volume: The area of the cross-section of the cave goes from 4 sq.m to 0 sq.m linearly as \(x\) goes from 0 to 1. So volume is \(\frac{1}{2} \times 1 \times 4 = 2 \text{m}^3\).</p>


</details>

---

### Routine definite integral in disguise
{: .d-inline-block}

B3, 2019
{: .label}

<p>Evaluate \(\int_{0}^{\infty}\left(1+x^{2}\right)^{-(m+1)} d x,\) where \(m\) is a natural number.</p>

<details><summary>Solution</summary>

<p>

Put \(x=\tan u\). This changes the integral to

\[ I= \int_{0}^{\pi/2}\cos^{2m}(u) du \]

\[ I=\frac{1}{4} \int_{0}^{2 \pi}\cos^{2m}(u) du \]


\[\begin{aligned}
\cos ^{n} \theta &=2^{-n}\left(\mathrm{e}^{\mathrm{i} \theta}+\mathrm{e}^{-\mathrm{i} \theta}\right)^{n} \\
&=2^{-n} \sum_{k=0}^{n}\left(\begin{array}{l}n \\ k\end{array}\right) \mathrm{e}^{\mathrm{i} k \theta} \mathrm{e}^{-\mathrm{i}(n-k) \theta} \\
&=2^{-n} \sum_{k=0}^{n}\left(\begin{array}{l}n \\ k\end{array}\right) \mathrm{e}^{\mathrm{i}(2 k-n) \theta} \\
\cos^{2m}\theta &=2^{-2m} \sum_{k=0}^{2m} \binom{2m}{k}  \mathrm{e}^{\mathrm{i}(2k-2m) \theta \quad\quad\quad (1) }
\end{aligned}\]


\[\text{ Since } \int_{0}^{2 \pi} e^{i \ell x} d x=\left\{\begin{array}{ll}2 \pi & (\ell=0) \\ 0 & (\ell \neq 0)\end{array}\right.\]

only one term in \((1)\) is non-zero, when \(k=m\).

\[\int_{0}^{2 \pi} \cos ^{2m} x d x=\frac{2 \pi}{2^{2m}} \binom{2m}{m} \]


\[I = \frac{1}{4} \cdot \frac{2\pi}{2^{2m}} \cdot \binom{2m}{m}\]

</p>

</details>




---


### Convergence of \\(e^{\text{quadratic}}\\)
{: .d-inline-block}


A2, 2014
{: .label}


<p>
Consider the integral \(I=\int_{1}^{\infty} e^{a x^{2}+b x+c} d x,\) where \(a, b, c\) are constants. Some combinations of values for these constants are given below and you have to decide in each case whether the integral \(I\) converges.
</p>

<p>(A) \(I\) converges for \(a=-1 \quad b=10 \quad c=100\)</p>
<p>(B) \(I\) converges for \(a=1 \quad b=-10 \quad c=-100\)</p>
<p>(C) \(I\) converges for \(a=0 \quad b=-1 \quad c=100\)</p>
<p>(D) \(I\) converges for \(a=0 \quad b=0 \quad c=-100\)</p>

<details><summary>Solution</summary>
TFTF
</details>

---


### A perplexing integral
{: .d-inline-block}

B5, 2010
{: label .label-blue}



<p>
Prove that \(\int_{1}^{b} a^{\log_{b} x} d x>\ln b\) where \(a, b>0, b \neq 1\).
</p>


<details open><summary>No solution</summary>
<p>
There is a mistake in this problem. The above statement is not true. See <a href="https://math.stackexchange.com/questions/2182860/proving-the-inequality-int-1b-a-log-bxdx-ln-b">this discussion</a> on Math Stack Exchange for details.
</p>
</details>



---

### Riemann sum
{: .d-inline-block}

B4, 2012
{: .label}

<p>
Define
\[
x=\sum_{i=1}^{10} \frac{1}{10 \sqrt{3}} \frac{1}{1+\left(\frac{i}{10 \sqrt{3}}\right)^{2}}
\]


\[
y=\sum_{i=0}^{9} \frac{1}{10 \sqrt{3}} \frac{1}{1+\left(\frac{i}{10 \sqrt{3}}\right)^{2}}
\]

</p>

<p>
Prove the two inequalities:
</p>

<p>
(a) \(x<\frac{\pi}{6}<y\)
</p>

<p>
</p>

<p>
(b) \(\frac{x+y}{2}<\frac{\pi}{6}\)
</p>

<p>
Hint: Connect the sums to an integral.
</p>


<details open><summary>Solution (a)</summary>
<p>
a) Let \(f(t)=1 /\left(1+t^{2}\right) .\) Then \(y\) and \(x\) are respectively the left and right hand Riemann sums for \(f\) over the interval \(\left[0, \frac{1}{\sqrt{3}}\right]\) using 10 equal parts, each of width \(1 / 10 \sqrt{3} .\) since \(f\) is a positive decreasing function, \(y\) must be greater than the area under \(f\) over the given interval and
\(x\) must be lesser than the area. The area under \(f\) over \(\left[0, \frac{1}{\sqrt{3}}\right]\) is:
</p>

<p>
\[\int_{0}^{1 / \sqrt{3}} f(t) d t=\lvert \tan^{-1}(t)\rvert_{0}^{1 / \sqrt{3}}=\frac{\pi}{6}\]
</p>

<p>
This implies that \(x< \frac{\pi}{6}< y\).
</p>

</details>

<p>
</p>


<details open><summary>Solution (b)</summary>

<p>
b) \(\frac{x+y}{2}\) can be interpreted as the sum of areas of 10 trapezoids as follows. Dividing
\(\left[0, \frac{1}{\sqrt{3}}\right]\) into 10 equal parts, let the \(i\)th subinterval be \(\left[x_{i}, x_{i+1}\right]\)
with \(i=0,1, \ldots, 10 .\) Then the \(i\) -th trapezoid has base \(\left[x_{i}, x_{i+1}\right]\) and it has two vertical sides,
the left one of height \(f\left(x_{i}\right)\) and the right one of height \(f\left(x_{i+1}\right)\).
</p>

<p style="text-align:center;"><img src="/assets/images/trapezoid_B4_2012.png" width="250px"></p>


<p><i>Claim</i>: The function \(f\) is concave </p>

<p>
<i>Proof:</i>
In the interval \(\left(0, \frac{1}{\sqrt{3}}\right)\), we have \(f^{\prime \prime}(t)=\frac{6 t^{2}-2}{\left(1+t^{2}\right)^{3}}<0\). \(\square\).
</p>


<p>
Since \(f\) is concave, the total area of trapezoids is less than the area under \(f\).
</p>



</details>





---


### Vanilla integrals
{: .d-inline-block}

A6, 2013
{: .label}


<p>
Compute the integrals below, whenever possible. If it does not exist, say so.
</p>

<p>
The notation \([x]\) denotes the integer part of \(x\).
</p>

<p>
<ul>
<li>(a) \(\int_{1}^{4} x^{2} d x\). </li>
<li>(b) \(\int_{1}^{3}[x]^{2} d x\). </li>
<li>(c) \(\int_{1}^{2}\left[x^{2}\right] d x\). </li>
<li>(d) \(\int_{-1}^{1} \frac{1}{x^{2}} d x\).</li>
</ul>
</p>


<details><summary>Solution</summary>

<p>
a) \(\int_{1}^{4} x^{2} d x=\frac{x^{3}}{3}\rvert_{1} ^{4}=21\) using the fundamental theorem of calculus.
</p>

<p>
b) \(\int_{1}^{3}[x]^{2} d x=1\left(1^{2}\right)+1\left(2^{2}\right)=5=\) area under the piecewise constant function \([x]^{2}\)
</p>

<p>
c) \(\int_{1}^{2}\left[x^{2}\right] d x=1(\sqrt{2}-1)+2(\sqrt{3}-\sqrt{2})+3(2-\sqrt{3})=5-\sqrt{2}-\sqrt{3}\) since the function \([x]^{2}\) is constant on intervals \([1, \sqrt{2}),[\sqrt{2}, \sqrt{3}),[\sqrt{3}, 2)\). It takes the values 1,2 and 3 on these intervals, respectively.
</p>


<p>
d) \(\int_{-1}^{1} \frac{1}{x^{2}} d x=2 \lim_{t \rightarrow 0^{+}} \int_{t}^{1} \frac{1}{x^{2}} d x=2 \lim_{t \rightarrow 0^{+}}\left(-1+\frac{1}{t}\right)=\infty .\) The fundamental theorem
does not apply over the interval [-1,1] because \(\frac{1}{x^{2}}\) goes to \(\infty\) in the interval. So the integral does not exist.
</p>

</details>

---


### Differentiability Challenge
{: .d-inline-block}

B4, 2014
{: .label}

<p>(i) Let \(f\) be continuous on [-1,1] and differentiable at \(0 .\) For \(x \neq 0,\) define a function \(g\) by \(g(x)=\frac{f(x)-f(0)}{x} .\) Can \(g(0)\) be defined so that the extended function \(g\) is continuous at \(0 ?\)</p>

<p>(ii) For \(f\) as in part (i), show that the following limit exists.</p>

<p>\[ \lim_{r \rightarrow 0^{+}}\left(\int_{-1}^{-r} \frac{f(x)}{x} d x+\int_{r}^{1} \frac{f(x)}{x} d x\right) \]</p>

<p>(iii) Give an example showing that without the hypothesis of \(f\) being differentiable at \(0,\) the conclusion in (ii) need not hold.</p>

<details><summary>Solution (i)</summary>


<p>(i) Yes. We must define \(g(0)=\lim_{x \rightarrow 0} g(x)=f^{\prime}(0),\) which exists by hypothesis.</p>

</details>

<p></p>

<details><summary>Solution (ii)</summary>
<p>(ii) Consider \(\int_{-1}^{-r} g(x) d x=\int_{-1}^{-r} \frac{f(x)}{x} d x-\int_{-1}^{-r} \frac{f(0)}{x} d x=\int_{-1}^{-r} \frac{f(x)}{x} d x-f(0) \ln r . \quad\) Similarly</p>

<p>\[\int_{r}^{1} g(x) d x=\int_{r}^{1} \frac{f(x)}{x} d x-\int_{r}^{1} \frac{f(0)}{x} d x=\int_{r}^{1} \frac{f(x)}{x} d x+f(0) \ln r\]</p>

<p>Thus the expression inside the given limit is equal to \(\int_{-1}^{-r} g(x) d x+\int_{r}^{1} g(x) d x,\) as \(\pm f(0) \ln r\) cancels out.</p>

<p>Applying the fundamental theorem of calculus to the continuous function \(g,\) we get an anti-derivative \(G\) of \(g,\) where \(G\) is defined on [-1,1] by \(G(t)=\int_{-1}^{t} g(x) d x .\) So the given</p>

<p>

\begin{align}
\text { limit }&=\lim_{r \rightarrow 0^{+}}\left(\int_{-1}^{-r} g(x) d x+\int_{r}^{1} g(x) d x\right) \\
&=\lim_{r \rightarrow 0^{+}}(G(-r)-G(-1)+G(1)-G(r)) \\
&=G(0)-0+G(1)-G(0)\\
&=G(1)
\end{align}

<br>
We have used the fundamental theorem to evaluate the integrals and the fact that \(G\) is differentiable.
</p>

</details>

<p></p>

<details><summary>Solution (iii)</summary>
<p>(iii) Define \(f(x)=\frac{1}{-\ln \frac{x}{2}}\) for \(x \in(0,1], f(x)=\frac{1}{\ln \left|\frac{1}{2}\right|}\) for \(x \in[-1,0),\) and \(f(0)=0 .\) Verify that this works: \(f\) is continuous at 0 and so on \([-1,1] .\) It is not differentiable at 0 as the relevant limit is \(+\infty .\) The two integrals in the desired limit are equal (because \(f\) is an odd function, so \(\frac{f(x)}{x}\) is even \()\) and each integral is \(+\infty\) as it amounts to \(\lim_{t \rightarrow 0^{+}} \ln |\ln t| .\) Can you see how one might think of such \(f ?\) E.g., check that choices like \(|x|\) or even \(x^{\frac{1}{3}}\) do not work. Compare the behavior of these functions at \(x=0\) with that of chosen \(f .\)</p>

</details>

---

### Continuity based on integral conditions
{: .d-inline-block}

A10, 2019
{: .label}

<p>Let \(f: \mathbb{R} \rightarrow \mathbb{R}\)</p>
<p>(a) There is no continuous function \(f\) for which \(\int_{0}^{1} f(x)(1-f(x)) d x<\frac{1}{4}\)</p>
<p>(b) There is only one continuous function \(f\) for which \(\int_{0}^{1} f(x)(1-f(x)) d x=\frac{1}{4}\)</p>
<p>(c) There are infinitely many continuous functions \(f\) for which \(\int_{0}^{1} f(x)(1-f(x)) d x=\frac{1}{4}\)</p>

<details><summary>Solution</summary>


<p>(a) False. \( f(x) = 0 \) is a counterexample. </p>


<p>(b) False. There are infinitely many candidates for \(f\). The maximum value of \( f(x)(1-f(x)) \) in the interval \(x \in (0,1)\) is \(1/4\).
This value is attained only when \(f(x)=1/2\). So \(f\) is unique in the interval \( (0,1) \). But \(f\) is defined on \(\mathbb{R}\), so outside the interval \((0,1)\),
\(f\) can be any continuous function.</p>


<p>(c) True. See part (b). </p>


</details>




---
### Slowly slope changing function
{: .d-inline-block}

B4, 2015
{: .label}

<p>Let \(f: \mathbb{R} \rightarrow \mathbb{R}\) be a twice differentiable function, where \(\mathbb{R}\) denotes the set of real numbers. Suppose that for all real numbers \(x\) and \(y,\) the function \(f\) satisfies</p>

<p>\[ f^{\prime}(x)-f^{\prime}(y) \leq 3|x-y| \]</p>


<p>(a) Show that for all \(x\) and \(y,\) we must have \(\left|f(x)-f(y)-f^{\prime}(y)(x-y)\right| \leq 1.5(x-y)^{2}\)</p>

<p>(b) Find the largest and smallest possible values for \(f^{\prime \prime}(x)\) under the given conditions.</p>


<details><summary>Solution</summary>

<p>(a) Note that the given inequality stays valid if we take absolute value of the LHS, because we may interchange \(x\) and \(y\) without affecting RHS.</p>

<p>
Fix \(x, y\) and let \(t=x-y .\) For now let \(x \geq y,\) i.e. \(t \geq 0 .\) For \(h \in[0, t],\) the value of \(y+h\) varies between \(y\) and \(x .\) We are given that \(\left|f^{\prime}(y+h)-f^{\prime}(y)\right| \leq 3|h|\). Integrate with respect to \(h\) over the interval \([0, t]\) to get:

\[\int_{0}^{t}\left|f^{\prime}(y+h)-f^{\prime}(y)\right| d h \leq \int_{0}^{t} 3|h| d h=1.5 t^{2}\]

<br>

The following inequality follows from Lemma 1 (proved below).

</p>

<p>
\[\left|\int_{0}^{t} f^{\prime}(y+h)-f^{\prime}(y) d h\right| \leq \int_{0}^{t}\left|f^{\prime}(y+h)-f^{\prime}(y)\right| d h .\]
</p>

<p>
Combining with the previous inequality we have:
\[\left|\int_{0}^{t} f^{\prime}(y+h)-f^{\prime}(y) d h\right| \leq 1.5 t^{2}\]
</p>

<p>
Finally we calculate the LHS.
<br>

\[\left|\int_{0}^{t} f^{\prime}(y+h) d h-\int_{0}^{t} f^{\prime}(y) d h\right|=\left|f(y+t)-f(y)-f^{\prime}(y) t\right|\]

<br>
where the first integral is calculated using the fundamental theorem of calculus and the second one is just the integral of the constant \(f^{\prime}(y) .\) Substituting \(x-y\) for \(t\) gives the desired result.
</p>

<p>The case when \(x\leq y\) is analogous.</p>


<p> (b) We have, for \(x \neq y,\left|\frac{f^{\prime}(x)-f^{\prime}(y)}{x-y}\right| \leq 3,\) so \(-3 \leq \frac{f^{\prime}(x)-f^{\prime}(y)}{x-y} \leq 3 .\) Taking limit as \(y \rightarrow x\)
we get \(-3 \leq f^{\prime \prime}(x) \leq 3 .\) It is easy to provide examples where \(f^{\prime \prime}\) attains the extreme values \(\pm 3,\) e.g. \(f(x)=\pm 1.5 x^{2} .\) These satisfy the hypothesis and have constant \(f^{\prime \prime}=\pm 3\)
</p>



<p><b>Lemma 1.</b>

<p> \[ \left|\int_{a}^{b} f(x) d x\right| \leq \int_{a}^{b}|f(x)| d x \] </p>


<p> <i>Proof.</i><br> </p>

<p> \[ -|f(x)| \leq f(x) \leq|f(x)| \] </p>


<p> for all \(x\); hence </p>

<p>
\[
-\int_{a}^{b}|f(x)| d x \leq \int_{a}^{b} f(x) d x \leq \int_{a}^{b}|f(x)| d x
\]
</p>

<p>
The lemma follows since \(-a \leq x \leq a \implies  |x|\leq a  \) if \(a \geq 0\). \(\quad \square\)
</p>


</p>


</details>

---


### Leibniz rule
{: .d-inline-block}

B6, 2019
{: .label}


<p>(a) Compute \(\frac{d}{dx}\left[\int_{0}^{e^{x}} \log (t) \cos ^{4}(t) dt\right]\)</p>

<p></p>

<p>(b) For \(x>0\) define \(F(x)=\int_{1}^{x} t \log (t) d t\)</p>

<p>i. Determine the open interval(s) (if any) where \(F(x)\) is decreasing and the open interval(s) (if any) where \(F(x)\) is increasing.</p>

<p>ii. Determine all the local minima of \(F(x)\) (if any) and the local maxima of \(F(x)\) (if any)</p>


<details><summary>Solution</summary>


<p>
(a) The general form of Leibniz rule is:<br>

\[\frac{\mathrm{d}}{\mathrm{d} x} \int_{a(x)}^{b(x)} f(x, t) \mathrm{d} t=f(x, b(x)) \cdot b^{\prime}(x)-f(x, a(x)) \cdot a^{\prime}(x)+\int_{a(x)}^{b(x)} \frac{\partial}{\partial x} f(x, t) \mathrm{d} t\]
</p>

<p>Applying the rule above gives the following answer: \(e^{x} x \cos^{4}(e^{x})\)</p>


<p>(b)
</p>

<p>
\begin{aligned}
F^{\prime}(x) &=\frac{d}{d x} \int_{1}^{x} t \log t \mathrm{d} t \\
&=x \log x
\end{aligned}
</p>


<p>Therefore \(F^{\prime}(1)=0 .\) Moreover, \(F^{\prime \prime}(x)=1+\log x .\) Hence one concludes that \(F\) is decreasing on \((0,1),\) increasing on \((1, \infty)\) and has a local minima at \(x=1\)</p>

</details>



---



### Sweep volume
{: .d-inline-block}

A3, 2017
{: .label}

<p>
Find the volume of the solid obtained when the region bounded by \(y=\sqrt{x}, y=-x\) and the line \(x=4\) is revolved around the \(x\) -axis.
</p>

<p style="text-align:center;"><img src="/assets/images/2017_sweep_volume.svg" width="250px"></p>

<details><summary>Solution</summary>

<p>
From \(x=0\) to \(x=1\) we have \(\sqrt{x} \geq|-x|,\) so from \(x=0\) to \(x=1\) the volume swept out by the curve determines the volume. From \(x=1\) to \(x=4\), the volume swept by the line determines the volume. Hence, we need two integrals.
</p>

<p>
From \(x=0\) and \(x=1\) we calculate volume obtained by revolving the area below \(y=\sqrt{x}\).

\[ \int_{0}^{1} \pi (\sqrt{x})^2 \text{d}x = \left.\frac{\pi x^2}{2} \right\rvert_{0}^{1} = \frac{\pi\cdot 1^2}{2} - \frac{\pi\cdot 0^2}{2} = \frac{\pi}{2} \]


Similarly, from \(x=1\) to \(x=4\) we have \(|-x| \geq \sqrt{x},\) so here we just have to take the volume obtained by the revolving the area below \(y=x\).

\[ \int_{1}^{4} \pi x^2 \text{d}x = \left.\frac{\pi x^3}{3} \right\rvert_{1}^{4} = \frac{64\pi}{3} - \frac{\pi}{3} =  21\pi \]

Thus total volume of the resulting solid: \( 21.5 \pi \).

</p>



</details>





---

### Definite integral
{: .d-inline-block}

B3, 2016
{: .label}


<p>Consider the function \(f(x)=x^{\cos (x)+\sin (x)}\) defined for \(x \geq 0\).</p>
<p>(a) Prove that</p>

<p>\[ 0.4 \leq \int_{0}^{1} f(x) d x \leq 0.5 \]</p>

<p>(b) Suppose the graph of \(f(x)\) is being traced on a computer screen with the uniform speed of \(1 \mathrm{cm}\) per second (i.e., this is how fast the length of the curve is increasing). Show that at the moment the point corresponding to \(x=1\) is being drawn, the \(x\) coordinate is increasing at the rate of</p>

<p>\[ \frac{1}{\sqrt{2+\sin (2)}} \mathrm{cm} \text { per second } \]</p>



<details><summary>Solution</summary>

<p>(a) It is easy to see that for \(0 \leq x \leq 1,\) we have \(1 \leq \cos (x)+\sin (x) \leq \sqrt{2},\) and so</p>

<p>\[ x^{1} \geq x^{\cos (x)+\sin (x)} \geq x^{\sqrt{2}} \]</p>

<p>As all three functions are non-negative in \([0,1],\) we can integrate the inequalities over that interval to get</p>

<p>\[ \frac{1}{2} \geq \int_{0}^{1} f(x) d x \geq \frac{1}{\sqrt{2}+1}>\frac{1}{1.5+1}=0.4 \]</p>

<p>(b) Length of the curve from \(x=0\) to any given \(x\) is \(l(x)=\int_{0}^{x} \sqrt{1+f^{\prime}(u)^{2}} d u\) It is given that \(\frac{d l}{d t}=1 \mathrm{cm} /\) second at all times. One needs to find \(\frac{d x}{d t}\) when \(x=1\)</p>

<p>By chain rule \( \displaystyle \frac{d l}{d t}=\frac{d l}{d x} \frac{d x}{d t} .\)</p>

<p> By the fundamental theorem of calculus:</p>

<p>
\[\frac{d l}{d x}=\sqrt{1+f^{\prime}(x)^{2}}\]
</p>

<p>From Lemma 1, we have \(f^{\prime}(1)=\cos (1)+\sin (1)\).</p>

<p>So at \(x=1\) we have<br></p>

<p>
\[ \frac{d l}{d x}=\sqrt{1+(\cos (1)+\sin (1))^{2}}=\sqrt{2+\sin 2}\]


The statement follows by substituting in the first equation.

</p>


<p><b>Lemma 1:</b> \(f^{\prime}(1) = \sin(1) + \cos(1)\)</p>

<p>\[f^{\prime}(x) = x^{(\cos (x)+\sin (x))-1}(-x \log (x) \sin (x)+x \log (x) \cos (x)+(\cos (x)+\sin (x))) \]
</p>

<p>Substitute \(x=1\) and \(\log (1) = 0\) in the above equation.\(\;\square\)
</p>


</details>


---





