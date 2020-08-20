---
layout: default
title: Complex numbers
nav_order: 91
nav_exclude: true
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




