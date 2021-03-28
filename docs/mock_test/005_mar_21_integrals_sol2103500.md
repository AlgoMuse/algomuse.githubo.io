---
layout: default
title: Mock test 5
nav_exclude: true
---


#  MT #5: Integral Calculus
#### Timings: 10:30-13:30 Hrs &nbsp;&nbsp;  Date: 21 March 2021
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg.
{: .fs-3 }

**For this part, answers must be written without any explanation.**


<ol>


<li>Suppose \(n\) be a fixed positive integer. If \( \int_{1}^{k} x^{n-1} dx = \frac{1}{n} \), what is the value of \(k\)?</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> \( 2^{1/n} \)
</details>


<li> Evaluate \( \displaystyle \int_{0}^{2} \frac{1}{\left( x-\frac{1}{2} \right)^2+\frac{3}{4}} dx \).  </li>

<details open><summary>Sol.</summary>

<b>Ans.</b> \( \frac{\pi}{\sqrt{3}} \) <br>


Substitute \( \sqrt{3}u/2 = x-1/2 \) and \(dx = \sqrt{3}du/2\).

\begin{align*}
I&=\frac{2}{\sqrt{3}} \int_{-1/\sqrt{3}}^{\sqrt{3}} \frac{1}{u^2+1} du \\
&=\frac{2}{\sqrt{3}} \tan^{-1} u \vert_{-1/\sqrt{3}}^{\sqrt{3}} \\
&=\frac{2}{\sqrt{3}} \frac{\pi}{2} \\
&=\frac{\pi}{\sqrt{3}}
\end{align*}

</details>

<li> Let \( f(x) \) be a continuous real-valued function on \([0, 1]\) for which

\[ \int_{0}^{1} f(x)dx = 0 \text{ and }\;\;\;  \int_{0}^{1} xf(x) dx = 1 \]

Give an example of such a function.

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> \(f(x) = 12x-6 \).<br>
Assume that \( f(x) = ax+b \) and solve the above two equations.
</details>



<li>
Consider the integral \( \int_{0}^{\infty} \frac{ \sin^2 x }{\pi^2 - x^2} dx \). Which of these statements are true?
<br>
(a) The integral does not exist as the function is not defined at \( x=\pi \).<br>
(b) There is a removable singularity at \(x=\pi\) but the integral does not exist.<br>
(c) There is a removable singularity at \(x=\pi\) and the integral exists.
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (c) At \(x=\pi\) the limit of integrand is zero. We can check this via L'Hospital rule.
Hence, there is a removable singularity.
</details>


<li>
Find the volume of the solid obtained when the region bounded by \( y=\sqrt{2x}\), \( y=-x \) and the line \(x=6\) is revolved around the  x-axis.
<br>
<img src="/assets/images/two_curves.png"/>
</li>

<details open><summary>Sol.</summary>
<p>
From \(x=0\) to \(x=2\) we have \(\sqrt{2x} \geq|-x|,\) so from \(x=0\) to \(x=2\) the volume swept out
by the curve determines the volume. From \(x=2\) to \(x=6\),
the volume swept by the line determines the volume. Hence, we need two integrals.
</p>

<p>
\[ \int_{0}^{2} \pi (\sqrt{2x})^2 \text{d}x + \int_{2}^6 \pi x^2  \text{d}x = \frac{220\pi}{3} \]
</p>

Similar problem: <a href="/docs/calculus/integrals/#sweep-volume">A3, 2017</a>.

</details>


<li>
Let \( f(x) = \sum_{n=0}^{\infty} \frac{x2^n}{n!} \) be a function defined in the interval \( [0,10] \). Find the value of:
\[ \int_{0}^{10} f(x) dx \]
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> \(50e^2\) <br>
The function \(f(x) = xe^2\) since \( e^2 = \sum_{n=0}^{\infty} \frac{2^n}{n!} \).
</details>


<li>
For any real number \(x\), let \([x]\) denote the greatest integer \(m\) such that \(m \leq x\).
Find the value of \( \int_{-2}^{2} [x^2 – 2]dx \).
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> \( 2(1-\sqrt{2}-\sqrt{3}) \).


\begin{align*}
\int_{-2}^{2} [x^2 – 2]dx &= 2 \int_0^2 [x^2-2] dx \\
&= 2( \int_0^1 -2\; dx + \int_1^\sqrt{2} -1\; dx + \int_\sqrt{2}^\sqrt{3} 0\; dx + \int_\sqrt{3}^2 1\; dx ) \\
&=2( -2 + (1-\sqrt{2}) + (2-\sqrt{3}) ) \\
&=2( 1-\sqrt{2}-\sqrt{3})
\end{align*}

</details>



<li>
What is the area bounded by the curve \( y = \ln x \), the x-axis and the straight line \(x=3\)?
</li>

<details open><summary>Sol.</summary>
\begin{align*}
\text{Area} &= \int_1^3 \ln x dx \\
 &=  x\ln x -x \rvert_1^3  \\
 &=  3\ln 3 -2
\end{align*}

</details>

<li>
Suppose \(f(x)\) is a double differentiable function with \(f^{\prime}(0) = 1\) and \(f^{\prime}(1) = 2\). What is the value of the integral below? If it possible
for the integral to take multiple values, write <b>Indeterminate</b>.

\[ \int_{0}^{1} f^\prime(x) f^{\prime\prime}(x) dx  \]

</li>

<details open><summary>Sol.</summary>
Substitute \( f^\prime(x) = z \).
\[ \int_{0}^{1} z\; dz = \frac{z^2}{2} = \frac{3}{2}  \]

</details>

<li>Compute the limit:
\[ \lim_{n\rightarrow\infty} n^3 \int_{0}^{1/n} x^{100x+2} dx \]
</li>


<details open><summary>Sol.</summary>
<b>Ans.</b> 1/3.<br>

\( x^{100x} \rightarrow 1\) as \(n\rightarrow \infty\). So:

\[ \lim_{n\rightarrow\infty} n^3 \int_{0}^{1/n} x^{2} dx = 1/3 \]

</details>


</ol>


## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


<p> <b>B1.</b> Let \( f:[0,1] \rightarrow \mathbb{R}^+ \) be a continous function such that \( \int_{0}^{1} f(t) dt = \frac{1}{3} \). Show
that there exists \( c\in(0,1) \) such that \( \int_{0}^{c} f(t) dt = c-\frac{1}{2}\).
</p>

<details open><summary>Sol.</summary>
<p>
Let \(F(x) := \int_0^x f(t) dt - x + 1/2 \). Since \( F(x) \) is a sum of
two continous functions, \(F(x)\) is continous.<br>

\begin{align*}
F(0) &= \int_0^0 - 0 + 1/2 = 1/2 \\
F(1) &= \int_0^1 - 1 + 1/2 = - 1/6 \\
\end{align*}

<i>Intermediate value theorem</i>. Since \( F(0) <0 \) and \(F(1)>0\), there
must be a \(c\) such that \(F(c) = \int_0^c f(t) dt - c +1/2 = 0\). In other words,


\[ \int_0^c f(t) dt = c - \frac{1}{2} \]

</p>

</details>


<p> <b>B2.</b> Let \( f(x) \) be a real-valued function defined on the interval \( [1,\infty) \). The following equations hold:

\begin{align*}
f(1) &= 1 \\
f^{\prime}(x) &= \frac{1}{x^2+f(x)^2}
\end{align*}
</p>

<p> Prove that \( \lim_{x\rightarrow \infty} f(x) < 1 + \pi/4 \).  </p>


<details open><summary>Sol.</summary>

<p>
As \( f^{\prime} \) is positive, \(f\) is an increasing function, so we have, for \( t>1, f(t)> f(1)=1 \). Therefore, for \( t>1 \)


\[ f^{\prime}(t)=\frac{1}{t^{2}+f^{2}(t)}<\frac{1}{t^{2}+1} \]

so


\begin{aligned}
f(x) &=1+\int_{1}^{x} f^{\prime}(t) d t \\
&<1+\int_{1}^{x} \frac{1}{t^{2}+1} d t \\
&<1+\int_{1}^{\infty} \frac{1}{t^{2}+1} d t \\
&=1+\frac{\pi}{4}
\end{aligned}

hence, \( \lim_{x \rightarrow \infty} f(x) \) exists and is, at most, \( 1+\frac{\pi}{4} \cdot \). The strict inequality holds because

\[ \lim_{x \rightarrow \infty} f(x)=1+\int_{1}^{\infty} f^{\prime}(t) d t<1+\int_{1}^{\infty} \frac{1}{t^{2}+1} d t=1+\frac{\pi}{4} \]

</p>

</details>


<p>
<b>B3.</b> Consider the parabola given by \(y = x^2\). The normal is
constructed at a point \(P\) and meets the parabola again in \(Q\).
Determine the coordinate of \(P\) for which the arc length along the parabola
between \(P\) and \(Q\) is minimized.<br>


<p style="text-align:center">
<img src="/assets/images/mt5_normal.jpg"/>
</p>

</p>


<details open><summary>Sol.</summary>

We may assume that \(u>0\), as the arc length for \(u\) and \(-u\) is the
same. The tangent to the parabola at \(\left(u, u^{2}\right)\) has slope
\(2u\), and so the normal has slope \(-1/2u\).

The equation of the normal is

\[ y-u^{2}=-\frac{1}{2 u}(x-u) \]

and this intersects the parabola at the point

\[ \left(-u-\frac{1}{2 u}, u^{2}+1+\frac{1}{4 u^{2}}\right) \]

The arc length is given by

\[ f(u)=\int_{-u-(1 / 2 u)}^{u} \sqrt{1+4 x^{2}} d x=F(u)-F(-u-(1 / 2 u)) \]

where \(F\) is a function for which \( F^{\prime}(x)=\left(1+4 x^{2}\right)^{1 / 2}\).

Then

\begin{align*}
f^{\prime}(u) &=F^{\prime}(u)-F^{\prime}(-u-(1 / 2 u))\left(-1+\frac{1}{2 u^{2}}\right) \\
&=\left(1+4 u^{2}\right)^{1 / 2}-\left(1+4 u^{2}+4+u^{-2}\right)^{1 / 2}\left(-1+\frac{1}{2 u^{2}}\right) \\
&=\left(1+4 u^{2}\right)^{1 / 2}-\left(4 u^{4}+5 u^{2}+1\right)^{1 / 2}\left(\frac{-1}{u}+\frac{1}{2 u^{3}}\right) \\
&=\left(1+4 u^{2}\right)^{1 / 2}\left[1+\frac{\left(u^{2}+1\right)^{1 / 2}\left(2 u^{2}-1\right)}{2 u^{3}}\right]
\end{align*}


\(f^\prime\) is zero if and only if \(2 u^{3}=-\left(u^{2}+1\right)^{1 / 2}\left(2 u^{2}-1\right) \).

Thus \( 4 u^{6}=\left(u^{2}+1\right)\) \(\left(4 u^{4}-4 u^{2}+1\right) \Leftrightarrow 0=-3 u^{2}+1\),
and we have that \( f^{\prime}(1 / \sqrt{3})=0 \). Hence \( f(u) \) decreases on the interval \( (0,1 / \sqrt{3}) \) and
increases on the interval \( (1 / \sqrt{3}, \infty) \).

Hence, the arc length is minimized when \(P\) is the one of the points

\[ \left(\frac{1}{\sqrt{3}}, \frac{1}{3}\right),\left(-\frac{1}{\sqrt{3}}, \frac{1}{3}\right) \]


</details>

<p>
<b>B4.</b> Let \( f(x) \) be a continous function defined on the interval \(I=[0,1]\) with the property
\[ yf(x) + xf(y) \leq 1 \]

for \(x,y\) in \(I\). <br>

(a) Prove that:

\[ \int_{0}^{1} f(x) dx \leq \frac{\pi}{4} \]

(b) Find a function \( f(x) \) for which equality holds in problem (a).

</p>

<details open><summary>Sol.</summary>
(a) Substitute \(x =\sin\theta \) so \( dx = \cos \theta d\theta \).

\begin{align*}
2I&=\int_{0}^{\pi/2} f(\sin \theta) \cos \theta+f(\cos \theta) \sin \theta d \theta \leq \int_{0}^{\frac{\pi}{2}} 1=\frac{\pi}{2} \\
2I &\leq \frac{\pi}{2} \\
I &\leq \frac{\pi}{4}
\end{align*}

(b) Let \( f(x) = \sqrt{1-x^2}  \) be the quarter of a unit circle centered at \( (0,0) \). The area of the quarter circle is \( \pi/4\), so equality holds.

\begin{align*}
x^2 + y^2 &= 1\\
y\sqrt{1-x^2}  + x\sqrt{1-y^2} &= 1 \\
yf(x) + xf(y) &= 1
\end{align*}

</details>


<p>
<b>B5</b>. Suppose \(\displaystyle I_{n}= \int_{0}^{2} (2x-x^2)^{n}dx\). Prove that \(\displaystyle \lim_{n\rightarrow \infty} I_{n} = 0 \).
</p>

<details open><summary>Sol.</summary>
Using integration by parts, we can get the following relation:<br>

<b>Lemma. </b> \(\displaystyle (2n+1) I_n = 2nI_n \)<br>

<i>Proof.</i> See Katherine Johnson's <a href="/assets/images/mock_test_5/Katherine_Johnson/B5.jpg">answer</a>.<br>



Therefore:

\[ I_n = \prod_{i=1}^{n} (1 - \frac{1}{2i+1}) I_1 \]

\[ 0\leq I_n \leq e^{-\frac{1}{3}-\frac{1}{5}\cdots-\frac{1}{2n+1}} I_1 \]

\[ 0\leq I_n \leq 0 \;\;\;\; (e^{-\infty} \rightarrow 0) \]





</details>

<p>
<b>B6</b>. Let \( \displaystyle f(x) = \frac{x}{1+x^6\sin^2x} \). Prove that \(\displaystyle \int_0^\infty f(x)\; dx\) is bounded.
</p>


<details open><summary>Sol.</summary>

The function is always positive but it has an infinite number of spikes at \( x=n\pi\).
The spike at \( n\pi\) has height \( n\pi\), so we have to show that the integral is bounded above.<br><br>

We have \( \sin x>1 / 2 x\) for \( x<\pi / 3\).
So \( |\sin x|>1 /(n \pi)^{k}\) except possibly for \( |x|<2 /(n \pi)^{k}\).<br>

Let \(I_{n}\) be the interval centered on \( n \pi\) width \( 4 /(n\pi)^{k}\).
For \(x \in I_{n}\) we have \(f(x)<2 n \pi\), so the integral of \( f(x) \) over the interval is
less than \( 8 /(n\pi)^{k-1}\).<br><br>

The total integral over all such intervals is bounded provided that \(k>2\).<br><br>

Outside such intervals, \(x^6 \sin^{2}x > \frac{1}{2}  x^{6}/x^{2k}\), so \(f(x)<2/x^{2k-5}\).<br><br>

Hence the interval of \(f(x)\) over 0 to \( \infty\)  excluding the intervals \(I_n\) is bounded provided \(k<5/2\).<br>

By taking \(k=2.25\), for example, we get that the integral is bounded.<br>

<i>The question said \( x^5\sin^2x \) instead of \(x^6\sin^2x\). This was a typo. Marks will be given if you carried out a plan to bound the
intervals near zero and outside zero. Problem source: Putnam '42.</i>

</details>





