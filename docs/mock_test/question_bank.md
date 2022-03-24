---
layout: default
title: Question bank
nav_exclude: true
---


#  Question Bank
#### Timings: 17:00-20:00 Hrs &nbsp;&nbsp;  Date: 6 May 2021
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

<ol>

<li>
<p>
Find the sum of the coefficients of the polynomial obtained after expanding and collecting the terms of the product \(\left(5x^{2}-5x+1\right)^{10}\left(x^{4}-2x+1\right)^{20}\).
</p>
</li>

<details open><summary>Sol.</summary>
<p> The sum \(a_{n}+a_{n-1}+\ldots+a_{0}\) of the coefficients of the polynomial \(a_{n} x^{n-1}+a_{n-1} x^{n-1}+\ldots+a_{0}\) is simply the value assumed by the polynomial when 1 is substituted for \(x\).
The value of the polynomial when \(x=1\) is \((1-5+5)^{100}(1-2+1)^{10}=1^{100} 0^{10}=0\).  </p>
</details>




<p>
<li>

<p>Let \(p\) be a prime number greater than 3. What are the possible remainders when the square of \(p\) is divided by 12?</p>

<p>
(a) 1 only.<br>
(b) 1 or 5.<br>
(c) 1 or 7.<br>
(d) 1, 7, or 11.<br>
</p><br>


<details open><summary>Sol.</summary>

<p> A prime number \(>3\) cannot leave a remainder of \(0,2,3,4\), \(6,8,9\) or 10 when divided by 12. (For example, if it left a remainder of 8, it would be of the form \(12 \mathrm{k}+8\), which is divisible by 4 so is not prime). Thus such a number is of the form \(12 \mathrm{k}+1\), or \(12 \mathrm{k}+5\), or \(12 \mathrm{k}+7\), or \(12 \mathrm{k}+11\)
But \((12 \mathrm{k}+\mathrm{n})_{2}^{2}=144 \mathrm{k}^{2}+24 \mathrm{k}+\mathrm{n}^{2}\) has the same
remainder as \(\mathrm{n}^{2}\) when divided by \(12\) and since \(1,25,49\) and 121 all have remainder 1, the conclusion follows.
</p>
</details>


</li>

</p>

<p>
<li>Evaluate : \(\displaystyle\int_0^{102} \sum_{k=1}^{100} \dfrac{\prod_{n=1}^{100}(x-n)}{x-k}\,\text{dx}\) </li>
</p>

<details open><summary><b><i>Solution :</i></b></summary>
Set \(f(x)~:=~\displaystyle\prod_{k=1}^{100} (x-k)\). Then \(f'(x) = f(x)\cdot \displaystyle\sum_{k=1}^{100} {1\over {x-k}}\) , which is exactly the function inside the integral.<br><br>

Hence the answer is $$f(102)-f(0) = \prod_{k=1}^{100} (102-k) - \prod_{k=1}^{100} (-k) = \prod_{k=2}^{101} k - \prod_{k=1}^{100} k = 101!-100! = \boxed{100\cdot 100!}$$
</details>



## Part B: Subjective questions

<!-- Subjective Problem 1 -->



<p><b>B.</b> Find a four digit number which on division by 149 leaves a remainder of 17 and on division by 148 leaves a remainder of 29 .
</p>
<details open><summary>Sol.</summary>
Let \(x\) represent the required four digit number, \(q_2\) the quotient obtained when \(x\) is divided by 149 , and \(q_2\) the quotient when the division is 148 . Thus
\(x=149 q_1+17\) and \(x=148 q_2+29\).
Since \(x\) is a four digit number \(7 \leqslant q_1, q_2<70\). Subtracting the above equations gives
\[149 \quad q_1-148 q_2=12\]
\[148\left(q_1-q_2\right)+q_1=12\]
Hence, since \(q_1-q_2\) is an integer its value must be zero, which gives
\(q_1=q_2=12\),  and  \(x=149 \times 12+17=1805\).
</details>







<p>
<b>B.</b>  
Three points \(A, B\) and \(C\) lie inside a circle whose radius is 1 cm. Show that \(B C^{2}+C A^{2}+A B^{2}\) is less than or equal to 9 sq. cm.
</p>


<details open><summary>Sol.</summary>
<p>
It is easily seen that we may take A, B, C on the circumference of the circle.
We seek the position of the points in order that \(A B^{2}+B C^{2}+C A^{2}\) is
maximum. We first note that if \(\theta<90^{\circ}\) and \(A C \neq B C\), then choosing \(C^{\prime}\) so that \(A C^{\prime}=B C^{\prime}\) gives a larger value of the sum of squares. Since \(\angle A C B=\angle A C^{\prime} B\) the cosine law gives


\[
\begin{gathered}
A B^{2}=A C^{2}+B C^{2}-2 A C . B C \cos \theta=A C^{\prime}^{2}+B C^{\prime} 2^{2}-2 A C^{\prime} B C^{\prime} \cos \theta \\
\text { Since } \frac{1}{2} A C \cdot B C=\frac{A r e a \Delta A B C}{\sin \theta}<\frac{A r e a \cdot \Delta A B C^{\prime}}{\sin \theta}=\frac{1}{2} A C^{\prime} \cdot B C^{\prime} \\
\text { we have } A B^{2}+A C^{2}+B C^{2}=2 A B^{2}+2 A C \cdot B C \cdot \cos \theta \\
<2 A B^{2}+2 A C^{\prime} \cdot B C^{\prime} \cos \theta=A B^{2}+A C^{\prime} 2+B C^{2} 2
\end{gathered}
\]

as asserted.

The triangle must be equilateral.<br>


<i>Source</i>. 
https://www.parabola.unsw.edu.au/files/articles/1964-1969/volume-2-1965/issue-3/vol02_no3_c.pdf

</p>

</details>




<p>
<b>B.</b> Consider the following polynomial where \(a_1,\ldots,a_n\) are distinct integers.

\[ r(x) =  \left(x-a_{1}\right)^{2}\left(x-a_{2}\right)^{2}\left(x-a_{3}\right)^{2} \ldots \left(x-a_{n}\right)^{2}+1 \]

Prove that \(r(x)\) cannot be written as the product of two other polynomials with integral coefficients.

</p>

<details open><summary>Sol.</summary>
<br>


Suppose, on the contrary, there exist polynomials \(p(x), q(x)\) with integer coefficients such that

\[ p(x) q(x)=\left(x-a_{1}\right)^{2}\left(x-a_{2}\right)^{2} \cdot \ldots\left(x-a_{n}\right)^{2}+1 \]

Since the right hand side is always positive \(p(x)\) can never vanish, and hence its sign never changes.
We may assume that \(p(x)\) and \(q(x)\) are positive for all real \(x_0\). Substituting \(x=a_k\) in (1) gives


\begin{align*}
p\left(a_{k}\right) q\left(a_{k}\right)&=1 \\
p\left(a_{k}\right)=q\left(a_{k}\right)&=1 \quad \text { for } k=1,2, \ldots n
\end{align*}


By the factor theorem \(p(x)=1+F(x)\left(x-a_{1}\right) \ldots\left(x-a_{n}\right)\)

\[  q(x)=1+G(x)\left(x-a_{1}\right) \ldots\left(x-a_{n}\right) \]

where \(F(x)\) and \(G(x)\) are polynomials. From (1) the degree of \(p(x)q(x)\) is \(2n\) so that \(F(x)\)
and \(G(x)\) both have degree 0, that is, they are constants.  Suppose \(F(x)=a\) and  and \(G(x)=b .\)
Substitution in \((1)\) now gives \(a b=1\) and \(a+b=0\), but there are no real numbers \(a\) and \(b\) satisfying these equations.

<br><i>Source: Parabola</i>.
</details>






<!-- Subjective Problem 4 -->

<p>
<b>B4.</b>
<ol type="I">
<li> Suppose \(f\) is a differentiable function from the \(\mathbb{R}\) into \(\mathbb{R}\). Suppose \(f'(x) > f(x)\) for all \(x \in \mathbb{R}\) , and \(f(x_0) = 0\) for some \(x_0 \in \mathbb{R}\). Prove that \(f(x) > 0\) for all \(x > x_0\) .</li>
<li> Show that the equation \(Ae^x = 1 + x + \frac{x^2}{2}\) , where \(A\) is a positive constant, has exactly one real root.</li>
</ol>
</p>

<i><b>Problem source : </b></i> UC Berkeley Ph.D Entrance Exam, Spring 1987<br>

<details open><summary><b><i>Solution :</i></b></summary>
<ol type="I">
<li>  Let \(g(x) = e^{-x} f(x)\) . Then, \(g'(x) =e^{-x} (f'(x) — f(x)) > 0\) . As \(g\) is an increasing function, so we have \(g(x)= e^{-x} f(x) \geqslant 0\) for \(x >x_0\) , and the conclusion follows.</li><br>

<li> Let \(f : \mathbb{R} \to \mathbb{R}\) be defined by \(f(x) = Ae^x - 1 - x - \dfrac{x^2}{2}\).<br><br>

Now, \(f(x) \to -\infty\) as \(x \to -\infty\) , and \(f(x) \to +\infty\) as \(x \to +\infty\) . Hence, as \(f\) is continuous, it has at least one real root, say \(x_0\). Observe that : $$f'(x) = Ae^x - 1 - x > Ae^x - 1 - x - \frac{x^2}{2} = f(x)\qquad\forall~ x\in\mathbb{R}$$

Thus, by part <b>(I)</b>, we deduce that \(f\) has only one real root, viz. \(x_0\). \(\blacksquare\)
</li>
</ol>
</details>




<p>
<b>B5.</b> Let \(A B C D\) be a trapezoid with \(A B\) parallel to \(C D,|A B|>|C D|\), and equal edges \(|A D|=|B C| .\) Let \(I\) be the center of the circle tangent to lines \(A B, A C\) and \(B D\), where \(A\) and \(I\) are on opposite sides of \(B D\). Let \(J\) be the center of the circle tangent to lines \(C D, A C\) and \(B D\), where \(D\) and \(J\) are on opposite sides of \(A C .\) Prove that \(|I C|=|J B|\).
</p>

<p>
<details open><summary>Sol.</summary>
Solution. Let \(\{P\}=A C \cap B D\) and let \(\angle A P B=180-2 a\). Since \(A B C D\) is an isosceles trapezoid, \(A P B\) is an isosceles triangle. Therefore \(\angle P B A=a\), which implies that \(\angle P B I=90^{\circ}-a / 2\) since \(I\) lies on the external bisector of \(\angle P B A\). Since \(I\) lies on the bisector of \(\angle C P B\), it follows that \(\angle B P I=a\) and hence that \(I P B\) is isosceles with \(|I P|=|P B|\). Similarly \(J P C\) is isosceles with \(|J P|=|P C|\). So, in the triangles \(C P I\) and \(B P J\) we have \(P I \equiv P B\) and \(P J \equiv C P\). Since \(I\) and \(J\) both lie on the internal bisector of \(\angle B P C\), it follows that triangles \(C P I\) and \(B P J\) are congruent. Therefore \(|I C|=|J B|\). \(\square\)
<i>Source: CMO 2021.</i>
</details>
</p>




<!--
Improper integrals. Exercises.
https://web.math.princeton.edu/~nelson/104/ImpIntSolns.pdf
-->




