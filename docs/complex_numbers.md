---
layout: default
title: Complex numbers
nav_order: 91
---


# Complex numbers



### Trigonometric values via complex numbers
{: .d-inline-block}

B5, 2012
{: .label }

<p>
Using the steps below, find the value of \(x^{2012}+x^{-2012},\) where \(x+x^{-1}=\frac{\sqrt{5}+1}{2}\)
</p>

<p>
(a) For any real \(r,\) show that \(\left|r+r^{-1}\right| \geq 2 .\) What does this tell you about the given \(x ?\)
</p>

<p>
(b) Show that \(\cos \left(\frac{\pi}{5}\right)=\frac{\sqrt{5}+1}{4}\).
Compare \(\sin \left(\frac{2 \pi}{5}\right)\) and \(\sin \left(\frac{3 \pi}{5}\right)\)

</p>

<p>
(c) Combine conclusions of parts a and b to express \(x\) and therefore the desired quantity in a suitable form.
</p>


<details>
<summary>Solution</summary>

<p>
(a) Because of the absolute value we may assume that \(r > 0\) by replacing \(r\) with \(-r\) if necessary. Now use AM-GM inequality or the fact that \((\sqrt{r}-\sqrt{1 / r})^{2} \geq 0 .\) since \(x+x^{-1}=\frac{\sqrt{5}+1}{2}<2\) given \(x\) must be a non-real complex number.
</p>

<p>
(b) Let \(\theta=\frac{\pi}{5} .\) Then \(\sin (2 \theta)=\sin (\pi-2 \theta)=\sin (3 \theta) .\) Using the formulas for \(\sin (2 \theta)\) and
\(\sin (3 \theta),\) canceling \(\sin \theta\left(\text { it is nonzero) and substituting } \sin^{2} \theta=1-\cos ^{2} \theta,\right.\) gives the
quadratic equation \(4 \cos ^{2} \theta-2 \cos \theta-1=0 .\) since \(\cos \theta > 0\), we get \(\cos \theta=\frac{\sqrt{5}+1}{4}\)
</p>

<p>
(c) Let \(x=d e^{i \alpha}=d(\cos \alpha+i \sin \alpha) .\) Then \(x^{-1}=d^{-1} e^{-i \alpha}=d^{-1}(\cos \alpha-i \sin \alpha) .\) Adding
and using that \(x+x^{-1}=\frac{\sqrt{5}+1}{2}=2 \cos \left(\frac{\pi}{5}\right),\) we get \(d=1\) and \(\alpha=\pm \theta .\)

So \(x=e^{\pm \frac{1 \pi}{5}}\).

<br>

\begin{align}
x^{2012}+x^{-2012} &= 2 \cos \left(\frac{2012 \pi}{5}\right)\\
 &=2 \cos \left(402 \pi+\frac{2 \pi}{5}\right)\\
 &=2 \cos \left(\frac{2 \pi}{5}\right)\\
 &=2 \cos ^{2}\left(\frac{\pi}{5}\right)-1 \\
 &=\frac{\sqrt{5}-1}{2}\\
\end{align}

</p>

</details>

---

### Complex polygon
{: .d-inline-block}

B2, 2020
{: .label}


<p>
2. (i) Let \(z=e^{\frac{2i\pi}{n}}\) where \(n\geq 2\) is a positive integer. Prove that \(\sum_{k=0}^{n-1}z^k=0.\)
</p>

<details><summary>Solution</summary>

<p>
Since \(z^n=1\), we have \(z^n-1=0\).
</p>

<p>
\[ z^n-1 = (z^{n-1} + z^{n-2} + \cdots + 1)(z-1) = 0 \]
</p>

<p>For \(n\geq 2 \), \(z\neq 1\). So the first factor must be zero. This proves the statement.
</p>
</details>


---

<p>
2. (ii) Prove that \(\cos 1^\circ + \cos 41^\circ + \cos 81^\circ + \cdots + \cos 321^\circ = 0\)
</p>


<details><summary>Solution</summary>

<p>
\begin{align}
A &:= \cos 1^\circ + \cos 41^\circ + \cos 81^\circ + \cdots + \cos 321^\circ \\
B &:= \sin 1^\circ + \sin 41^\circ + \sin 81^\circ + \cdots + \sin 321^\circ \\
\end{align}
</p>


<p>
Notice that \(40^\circ=2\pi/9\). Let \( \theta = 1^\circ = \pi/180 \). Then:
</p>

<p>
\[ A+iB = e^{i\theta} \left( \sum_{k=0}^{8} e^{ \frac{2\pi i}{9}k } \right) \]
</p>

<p>
From problem 2(i), we know that RHS of the above equation is zero. Since \(A\) and \(B\) are real numbers, both of
them must be individually zero. In particular, \(A=0\), which proves the statement.
</p>


</details>

---





### Power of a complex number
{: .d-inline-block}

A13, 2010
{: .label}


<p>
If \(b\) is a real number satisfying \(b^{4}+\frac{1}{b^{4}}=6,\) find the value of \(\left(b+\frac{i}{b}\right)^{16}\) where \(i=\sqrt{-1}\)
</p>

<details><summary>Solution</summary>
<p>
\begin{align}
\left(b^{2}\right)^{2}+\left(\frac{i^{2}}{b^{2}}\right)^{2}&=6\\
\left(b^{2}+\frac{i^{2}}{b^{2}}\right)^{2}&=4\\
b^{2}+\frac{i^{2}}{b^{2}}&=\pm 2
\end{align}
</p>

<p>Let us know look at the quantity we want to compute:</p>


<p>
\begin{align}
\left(b+\frac{i}{b}\right)^{16}&=\left(b^{2}+\frac{i^{2}}{b^{2}}+2 i\right)^{8}\\
&=(\pm 2+2i)^{8}\\
&=2^{8}\left(\sqrt{2} e^{\frac{i \pi}{4}}\right)^{8} \text{ or } 2^{8}\left(\sqrt{2} e^{\frac{3i \pi}{4}}\right)^{8} \\
&=2^{12}\\
&=4096
\end{align}
</p>
</details>


---


### Complex triangle
{: .d-inline-block}

A7, 2013
{: .label}


<p>
Let \(A, B, C\) be angles such that \(e^{i A}, e^{i B}, e^{i C}\) form an equilateral triangle in the complex plane. Find the values of the given expressions.
</p>

<p>
a) \(e^{i A}+e^{i B}+e^{i C}\)
</p>

<p>
b) \(\cos A+\cos B+\cos C\)
</p>

<p>
c) \(\cos 2 A+\cos 2 B+\cos 2 C\)
</p>

<p>
d) \(\cos ^{2} A+\cos ^{2} B+\cos ^{2} C\)
</p>


<details><summary>Solution</summary>


<p>
a) \(e^{i A}+e^{i B}+e^{i C}=0\) by taking the vector sum of the three points on the unit circle.
</p>

<p>
b) \(\cos A+\cos B+\cos C=0=\) real part of \(e^{i A}+e^{i B}+e^{i C},\) which is 0 by part a.
</p>

<p>
c) \(\cos 2 A+\cos 2 B+\cos 2 C=0\) because the points \(e^{2 i A}, e^{2 i B}, e^{2 i C}\) on the unit circle also form an equilateral triangle in the complex plane, since taking \(B=A+(2 \pi / 3), C=A+(4 \pi / 3)\), we get \(2 B=2 A+(4 \pi / 3)\) and \(2 C=2 A+(8 \pi / 3)=2 A+(2 \pi / 3)+2 \pi\). The last term \(2 \pi\) does not change the position of the point.
</p>

<p>
d) \(\cos ^{2} A+\cos ^{2} B+\cos ^{2} C=\frac{3}{2}\) because, using the formula for \(\cos 2 \theta\) in part \(c,\) we get
\(\cos ^{2} A+\cos ^{2} B+\cos ^{2} C=\sin ^{2} A+\sin ^{2} B+\sin ^{2} C\) and the sum of the LHS and the RHS
in this equation is \(3 .\)
</p>


</details>

---


### Maximum and minimum of an average
{: .d-inline-block}

A9, 2014
{: .label}

<p>Let \(\theta_{1}, \theta_{2}, \ldots, \theta_{13}\) be real numbers and let \(A\) be the average of the complex numbers \(e^{i \theta_{1}}, e^{i \theta_{2}} \ldots, e^{i \theta_{13}},\) where \(i=\sqrt{-1}\). As the values of \(\theta\) 's vary over all 13 -tuples of real numbers, find</p>
<p>(i) the maximum value attained by \(|A|\)</p>
<p>(ii) the minimum value attained by \(|A|\).</p>

<details><summary>Solution</summary>

<p>
(i) Each \(e^{i\theta}\) can take a maximum value of 1, which is attained when \(\theta=0\). Hence, the maximum average is also 1.
</p>

<p>
(ii) To get the minimum, place the 13 points on the vertices of a regular cyclic polygon. The average corresponds to the center of the polygon which is \((0,0)\). Hence, the minimum value \(|A|\) can take is 0.
</p>

</details>

---


### Roots of unity I
{: .d-inline-block}

A10, 2015
{: .label}

<p>(i) Suppose \(z_{1}, z_{2}\) are complex numbers. One of them is in the second quadrant and the other is in the third quadrant.
How does \(||z_{1}|-| z_{2}||\)  compare with \(\left|z_{1}+z_{2}\right|\)?</p>

<p>(ii) Complex numbers \(z_{1}, z_{2}\) and 0 form an equilateral triangle. How does \(\left|z_{1}^{2}+z_{2}^{2}\right|\) compare with\( \left|z_{1} z_{2}\right|\).</p>

<p>(iii) Let \(1, z_{1}, z_{2}, z_{3}, z_{4}, z_{5}, z_{6}, z_{7}\) be the complex 8 -th roots of unity. Find the value of \(\prod_{i=1, \ldots, 7}^{\Pi}\left(1-z_{i}\right),\) where the symbol \(\Pi\) denotes product.</p>


<details><summary>Solution</summary>

<p>(i) ||\(z_{1}|-| z_{2}||<\left|z_{1}+z_{2}\right| .\) One way: using triangle inequality for \(z_{1}+z_{2}\) and \(-z_{2}\) we get \(\left|z_{1}\right| \leq\left|z_{1}+z_{2}\right|+\left|-z_{2}\right|\) and so \(\left|z_{1}\right|-\left|z_{2}\right| \leq\left|z_{1}+z_{2}\right| .\) Now we may take absolute value on the LHS because switching \(z_{1}\) and \(z_{2}\) keeps RHS the same. For equality, \(z_{1}+z_{2}\) and \(-z_{2}\) must point in the same direction, so \(z_{1}\) and \(z_{2}\) must be along the same line. But they are in quadrants 2 and \(3,\) so this cannot happen.</p>

<p></p>

<p>(ii) \(z_{2}\) must be obtained by rotating \(z_{1}\) by angle \(\pi / 3,\) say in the counterclockwise direction (otherwise interchange the two). Then \(z_{2}=z_{1} e^{\frac{\pi i}{3}}\). Then \(z_{1}^{2}+z_{2}^{2}=z_{1}^{2}\left(1+e^{\frac{2 \pi i}{3}}\right)\) and \(z_{1} z_{2}=z_{1}^{2} e^{\frac{\pi i}{3}} . \quad\) Now \(1+e^{\frac{2 \pi i}{3}}=e^{\frac{\pi i}{3}}\) (see by calculation or picture), so we have in fact \(z_{1}^{2}+z_{2}^{2}=z_{1} z_{2}\)</p>

<p></p>

<p>(iii) We have \(\prod_{i=1, \ldots, 7}\left(x-z_{i}\right)=\frac{x^{8}-1}{x-1}=1+x+\ldots+x^{7}\). Putting \(x=1\) gives \(\prod_{1=1, \ldots, 7}\left(1-z_{i}\right)=8\)</p>

</details>

---


### Counting roots in a quadrant
{: .d-inline-block}

A6, 2018
{: .label}

<p>Consider the equation</p>

<p>\[ z^{2018}=2018^{2018}+i \]</p>

<p>where \(i=\sqrt{-1}\)</p>
<p>(a) How many complex solutions does this equation have?</p>
<p>(b) How many solutions does each of the four quadrants have?</p>


<details><summary>Solution</summary>

<p>(a) In general, the equation \(z^n = re^{i\theta}\) has \(n\) solutions given by:

\[ r^{1 / n} \exp \left[\frac{i(\theta+2 k \pi)}{n}\right] \text{ for each }  0 \leq k \leq n-1 \]

The given equation has 2018 complex solutions, since we can express the complex number in the RHS as \(re^{i\theta}\) for some small \(\theta\).
</p>


<p>(b) Instead of looking at the given equation, first consider the solutions to: \(x^{2018}=r\). Two of them are real values:
\( r^{1/2018} \) and \( -(r)^{1/2018} \). The other 2016 are distributed equally in the four quadrants, 504 each.
</p>

<p>
If we rotate the solutions to \(x^{2018}=r\) by a tiny angle in the counter-clockwise direction, we get the solutions to the given equation. (The value of \(r\) being
\( \sqrt{ 2018^{2018\cdot 2} + 1^2 } \)).  This gives 505 values each in the first and third quadrant but still 504 in the second and fourth quadrant.
</p>

</details>

---

### Counting the roots outside a disk
{: .d-inline-block}

B2A, 2019
{: .label}


<p>How many complex roots \(w\) of the equation \(z^{2019}-1=0\) satisfy \(|w+1| \geq \sqrt{2+\sqrt{2}}\)</p>



<details><summary>Solution</summary>

<p>Such roots can be expressed as follows</p>

<p>\[ w=\frac{\cos (2 \pi k)}{2019}+i \frac{\sin (2 \pi k)}{2019} \quad \text { for } k=0,\pm 1, \ldots,\pm 1009 \]</p>

<p>Therefore,</p>

<p>\[ |w+1|^{2}=2+2 \frac{\cos (2 \pi k)}{2019} \]</p>

<p>Hence we want to find all \(k\) such that</p>

<p>\[ \frac{\cos (2 \pi k)}{2019} \geq \frac{1}{\sqrt{2}} \]</p>

<p>Which is same as</p>

<p>
\[
\begin{array}{l}
\quad\left|\frac{2 \pi k}{2019}\right| \leq \frac{\pi}{4} \\
\text { i.e. }|k| \leq 252
\end{array}
\]
</p>

<p>So there are 505 solutions.</p>


</details>
