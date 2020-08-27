---
layout: default
title: Complex numbers
nav_order: 91
---


# Complex numbers


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


## Power of a complex number
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
Let \(A, B, C\) be angles such that \(e^{i A}, e^{i B}, e^{i C}\) form an equilateral triangle in the complex plane. Find values of the given expressions.
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

Sol.


<p>
a) \(e^{i A}+e^{i B}+e^{i C}=0\) by taking the vector sum of the three points on the unit circle.
</p>

<p>
b) \(\cos A+\cos B+\cos C=0=\) real part of \(e^{i A}+e^{i B}+e^{i C},\) which is 0 by part a.
</p>

<p>
c) \(\cos 2 A+\cos 2 B+\cos 2 C=0\) because the points \(e^{2 i A}, e^{2 i B}, e^{2 i C}\) on the unit circle also form an equilateral triangle in the complex plane, since taking \(B=A+(2 \pi / 3), C=A+(4 \pi / 3)\), we get \(2 B=2 A+(4 \pi / 3)\) and \(2 C=2 A+(8 \pi / 3)=2 A+(2 \pi / 3)+2 \pi\) and the last term \(2 \pi\) does not change the position of the point.
</p>

<p>
d) \(\cos ^{2} A+\cos ^{2} B+\cos ^{2} C=\frac{3}{2}\) because, using the formula for \(\cos 2 \theta\) in part \(c,\) we get
\(\cos ^{2} A+\cos ^{2} B+\cos ^{2} C=\sin ^{2} A+\sin ^{2} B+\sin ^{2} C\) and the sum of the LHS and the RHS
in this equation is \(3 .\)
</p>










