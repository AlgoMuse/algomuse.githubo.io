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

<p>
<li>

There are three pastures of area 35 acres, 10 acres and 65 acres.  On a certain date the owner places 17, 7 and 23 cows  in the pastures, respectively.
The grass in the first pasture is exhausted after 7 weeks, and that in the second after 4 weeks.

For how long can the 23 cows be grazed in the third pasture?

<br>Assume that initially there is the same amount of grass/unit area and
that new grass grows at the same constant rate in all three pastures.

</li>
</p>

<details open><summary>Sol.</summary>
Let us take as a unit of grass the amount initially available in each acre, i.e. the first pasture has 35 units, the second 10, the third 65. Suppose that grass grows at a rate of runits/week/acre, and each cow eats at a rate of c units/week.

Then in the first pasture, after 7 weeks \(35+7.35 r\) units of grass are eaten by 17 cows, so \(35+7.35 \mathrm{r}=7.17 . \mathrm{c}\)
From the second pasture we have \(10+4.10 \mathrm{r}=4.7 \mathrm{c}\). If the third pasture is exhausted after \(\mathrm{n}\) weeks, \(65 \mathrm{r}=\mathrm{n} .23 \mathrm{c}\)
Solving these equations simultaneously, we find \(\mathrm{n}=13\).
</details>





<p>
<li> Find the shortest distance from the point \(A=(0,2)\) to the arc of the parabola \(y=x^2\) which is between \(x=0\) and \(x=1\).
</li>
</p>

<details open><summary>Sol.</summary>
If \(B\) is a point on the parabola, we have:
\begin{align*}
AP^2 &= x^2 + (2-y)^2 \\
 &= x^2 + (2-x^2)^2 \\
 &= x^4 - 3x^2 + 4 \\
 &= (x^2-3/2)^2 + 7/4 \\
\end{align*}

The minimum is attained when \(x=1\). Hence, the minimum value of \(AB\) is \(  \left( (1-3/2)^2 + (7/4)^2 \right)^{1/2} \).


</details>

<p>
<li>

We have an \(n\times n\) grid of points, where \(n\) is an even number. There is a black spot at the
center of the grid. In how many ways can we draw a rectangle with corners as the grid points such
that the spot is inside the rectangle? An example of a rectangle is shown for a grid of size \(n=6\):

<p style="text-align:center">
<img src="/assets/images/mt10_lattice.png"/>
</p>


</li>
</p>




<p>
<li>

<p>A prime number greater than 3 is divided by 12. What is the remainder?</p>

<details open><summary>Sol.</summary>
<p> A prime number \(>3\) cannot leave a remainder of \(0,2,3,4\), \(6,8,9\) or 10 when divided by 12. (For example, if it left a remainder of 8, it would be of the form \(12 \mathrm{k}+8\), which is divisible by 4 so is not prime). Thus such a number is of the form \(12 \mathrm{k}+1\), or \(12 \mathrm{k}+5\), or \(12 \mathrm{k}+7\), or \(12 \mathrm{k}+11\)
But \((12 \mathrm{k}+\mathrm{n})_{2}^{2}=144 \mathrm{k}^{2}+24 \mathrm{k}+\mathrm{n}^{2}\) has the same
remainder as \(\mathrm{n}^{2}\) when divided by \(12\) and since \(1,25,49\) and 121 all have remainder 1, the conclusion follows.
</p>
</details>


</li>

</p>





<!-- SAQ 1 -->
<p>
<li> Let \(A\) be a \(3 \times 3\) matrix with entries from the set \(\{-1 , +1\}\). Also, it is given that the first row and the first column of \(A\) contains only \((+1)\). Find the maximum value of determinant of \(A\).</li>
</p>


<details open><summary><b><i>Solution :</i></b></summary>
Let's assume the matrix is
\(\)\textbf A=\begin{bmatrix} +1 & +1 & +1 \\ +1 & (-1)^a & (-1)^b \\ +1 & (-1)^c & (-1)^d\end{bmatrix}$$ and thus $$\det(\textbf A)=(-1)^{a+d}+(-1)^{b}+(-1)^{c}-(-1)^{b+c}-(-1)^{a}-(-1)^{d}$$ <br>

From this we can see that \(\det(\textbf A)\) is always even because switching one of \((+1)\) with \((-1)\) will change the sum by \(2\). <br><br> Now observe that if we take \(\textbf{A} = \begin{bmatrix} +1 & +1 & +1 \\ +1 & -1 & +1 \\ +1 & -1 & -1\end{bmatrix}\) . Thus, \(\det(\textbf{A}) = 4\) . So, we need to check for the possibility of \(6\).<br><br>

When the determinant is \(6\), we want,
\(\)\begin{matrix}\textbf{even} &\textbf{odd} \\ a+d & b+c\\ b & a\\ c & d\end{matrix}\(\)

But now left side says that sum \((a + b + c + d)\) must be even, and the right part says that it must be odd. Contradiction!<br><br>

Thus, the maximum possible value of \(\det(\textbf{A})\) is \(\boxed{4}\).
</details>



<!-- SAQ 2 -->
<p>
<li>Evaluate : \(\displaystyle\int_0^{102} \sum_{k=1}^{100} \dfrac{\prod_{n=1}^{100}(x-n)}{x-k}\,\text{dx}\) </li>
</p>

<details open><summary><b><i>Solution :</i></b></summary>
Set \(f(x)~:=~\displaystyle\prod_{k=1}^{100} (x-k)\). Then \(f'(x) = f(x)\cdot \displaystyle\sum_{k=1}^{100} {1\over {x-k}}\) , which is exactly the function inside the integral.<br><br>

Hence the answer is $$f(102)-f(0) = \prod_{k=1}^{100} (102-k) - \prod_{k=1}^{100} (-k) = \prod_{k=2}^{101} k - \prod_{k=1}^{100} k = 101!-100! = \boxed{100\cdot 100!}$$
</details>



<!-- SAQ 5 -->
<p>
<li> Does there exist a real polynomial \(H(x)\) with integer coefficients such that \(H(13) = 21\) and \(H(50) = 122\) ? If yes, find all possible values of \(H(37)\) .</li>
</p>

<details open><summary><b><i>Solution :</i></b></summary>
Since \(H\) is an integer polynomial, so for any two integers \(a\) and \(b\) , we must have \(a - b | H(a) - H(b)\) . But here, \(\)(50 - 13) = 37 \not| 101 = 122 - 21 = H(50) - H(13)\(\) Thus, there is <b>no such polynomial</b>.
</details>




<!-- SAQ 9 -->
<p>
<li> Consider two functions \(f\) and \(g\) defined as : $$f(x) = \dfrac{1}{x+a} + \dfrac{1}{x+b} - \dfrac{1}{c_1}\quad~\&~\quad g(x) = \dfrac{1}{x+a} + \dfrac{1}{x+b} - \dfrac{1}{c_2}$$ where \(a, b, c_1, c_2\) are real constants. Both \(f\) and \(g\) have the property that their roots are equal in magnitude, but opposite in sign, i.e. if \(\alpha\) is one root of \(f\) , then its other root is \((-\alpha)\) . Simlarly, if \(\beta\) is one root of \(g\) , then the other root of \(g\) is \((-\beta)\).<br><br>

Let \(P_1\) denote the product of roots of \(f\) , and let \(P_2\) denote the product of two roots of \(g\). Find the value of \(\big(P_1 + P_2\big)\) , when \(a = 27\) , \(b = 13\) , \(c_1 = 147\) and \(c_2 = 187\) .
</li>

<details open><summary><b><i>Solution :</i></b></summary>
Consider the function $$h(x) = \dfrac{1}{x+a} + \dfrac{1}{x+b} - \dfrac{1}{c}$$ where \(c\) is any non-zero real constant.

\begin{align*}
h(x) = 0 &\implies c(2x + a + b) = (x+a)(x+b)\\
&\implies x^2 + (a+b-2c)x + (ab - bc -ca) = 0\\
\end{align*}

Now, if \(r\) and \((-r)\) are two roots of \(h\) , then : $$r^2 + (a+b-2c)r + (ab - bc -ca) = 0 \quad\&\quad r^2 - (a+b-2c)r + (ab - bc -ca) = 0$$

Adding these two, we get \(a+b-2c=0\) which implies \(c=\frac{1}{2}(a+b)\) . Now, the product of the roots of \(h\) will be : $$P = ab - bc - ca = ab - \dfrac{(a+b)^2}{2} = -\dfrac{a^2 + b^2}{2}$$ which depends only on \(a\) and \(b\).<br><br>

Thus, in our problem, $$P_1 + P_2 = -\dfrac{a^2 + b^2}{2} - \dfrac{a^2 + b^2}{2} = -(27^2 + 13^2) = \boxed{-898}\quad\blacksquare$$
</details>
</p>



## Part B: Subjective questions

<!-- Subjective Problem 1 -->

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




<p>
<b>B1.</b> Let \(n \geq 2\) be is a natural number. \(B\) is a set which contains all ordered pairs of natural numbers \((a,b)\) with the following properties: \(a,b \leqslant n\) , \(\gcd(a,b)=1\) , and \(a + b > n\) .<br><br>

Prove that : \(\displaystyle\sum_{(a,b)\in B}{\dfrac{1}{ab}} = 1\) .
</p>

<i><b>Problem source : </b></i> Mathematics Stack Exchange<br>

<details open><summary><b><i>Solution :</i></b></summary> <br>
For any integer \(n \ge 2\), let : <br>
\(\Delta = \{(a,b) \in \mathbb{Z}_{+}^2 : \gcd(a,b) = 1 \}\), <br>
\(S_n = \{(a,b) \in \Delta : 1 \le a, b \le n\}\), <br>
\(T_n = \{ (a,b) \in S_n : a+ b \le n\}\) <br><br>

The sum at hand can be rewritten as
$$s_n := \sum_{(a,b)\in B} \frac{1}{ab} =
\sum_{(a,b) \in S_n \setminus T_n}\frac{1}{ab}
= \sum_{(a,b) \in S_n} \frac{1}{ab} - \sum_{(a,b)\in T_n} \frac{1}{ab}$$

This implies for \(n \ge 3\), we have
$$s_n - s_{n-1} = \sum_{(a,b)\in S_n \setminus S_{n-1}} \frac{1}{ab}
- \sum_{(a,b) \in T_n \setminus T_{n-1}} \frac{1}{ab}$$

For any \((a,b) \in S_n\), it is easy to see \((a,b) \not\in S_{n-1}\) if and only if \(a = n\) or \(b = n\) (but not both). This means :

$$\sum_{(a,b)\in S_n \setminus S_{n-1}}\frac{1}{ab} = \sum_{(n,b)\in S_n}\frac{1}{nb} + \sum_{(a,n)\in S_n} \frac{1}{an}
= \frac{2}{n}\sum_{(a,n)\in S_n}\frac{1}{a}$$

Similarly, for any \((a,b) \in T_n\), \((a,b) \not\in T_{n-1}\) if and only if \(a+b = n\). This leads to
$$\sum_{(a,b)\in T_n \setminus T_{n-1}}\frac{1}{ab}
= \sum_{(a,b)\in \Delta, a+b = n} \frac{1}{ab}
= \frac{1}{n}\sum_{(a,b)\in \Delta, a+b = n}\left( \frac{1}{a} + \frac{1}{b}\right)
= \frac{2}{n}\sum_{(a,n) \in S_n}\frac{1}{a}$$

The last equality is true because $$\gcd(a,b) = 1 \iff \gcd(a,n) = \gcd(a,a+b) = 1$$

Combine above two results, we find for \(n \ge 3\), we have
$$s_n - s_{n-1} = 0\quad\implies\quad s_n = s_{n-1} = s_{n-2} = \cdots = s_2$$
By brute force, we know \(B = \{(1,2), (2,1)\} \implies s_2 = \frac{1}{1\cdot 2} + \frac{1}{2\cdot 1} = 1\) and we are done. \(\blacksquare\)
</details>



<!-- Subjective Problem 3 -->

<p>
<b>B3.</b>
<ol type="I">
Consider any positive real numbers \(a, b, c\) , such that \(a+b+c = 3\).
<li>Prove that : $$\big(ab\big)^\frac{2}{3} + \big(bc\big)^\frac{2}{3} + \big(ca\big)^\frac{2}{3} \leqslant 3$$</li>

<li>Using <b>(I)</b> or otherwise, prove that : \(\)S ~:=~ \dfrac{a^2}{a + 2b^2} + \dfrac{b^2}{b + 2c^2} + \dfrac{c^2}{c + 2a^2} ~\geqslant~ 1\(\)</li>
</p>
</ol>

<i><b>Problem source : </b></i> My notebook <br>

<details open><summary><b><i>Solution :</i></b></summary>
<ol type="I">
<li>Note that : \(ab + bc + ca ~\leqslant~ \dfrac{1}{3}(a + b + c)^2 = 3\) . Now, \begin{align*}
9 = 3(a + b + c) &= 2(a + b + c) + 3\\
&\geqslant 2(a + b + c) + (ab + bc +ca)\\
&= (a + b + ab) + (b + c + bc) + (c + a + ca)\\
&\geqslant 3\bigg[\big(ab\big)^\frac{2}{3} + \big(bc\big)^\frac{2}{3} + \big(ca\big)^\frac{2}{3}\bigg]
\end{align*}

which implies that : $$\quad\big(ab\big)^\frac{2}{3} + \big(bc\big)^\frac{2}{3} + \big(ca\big)^\frac{2}{3} \leqslant 3$$

<li>
Observe that by AM - GM, we have : $$\dfrac{a^2}{a + 2b^2} = a - \dfrac{2ab^2}{a + 2b^2} \geqslant a - \dfrac{2ab^2}{3\sqrt[3]{ab^2}} = a - \dfrac{2}{3}\big(ab\big)^\frac{2}{3}$$

Therefore, \(~S ~\geqslant~ \displaystyle\sum a - \displaystyle\dfrac{2}{3}\big(ab\big)^\frac{2}{3} ~=~ 3 - \dfrac{2}{3}\displaystyle\sum\big(ab\big)^\frac{2}{3}\)

Therefore, by part <b>(I)</b>, we get : $$S = 3 - \dfrac{2}{3}\bigg[\big(ab\big)^\frac{2}{3} + \big(bc\big)^\frac{2}{3} + \big(ca\big)^\frac{2}{3}\bigg] \leqslant 3 \geqslant 3 -2 = 1$$

Also, equality holds clearly when \(a=b=c=1\). \(\blacksquare\)</li>
</ol>
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



<!-- Subjective Problem 5 -->

<p>
<b>B5.</b>
<ol type="I">
<li> Evaluate the following integral : \(\displaystyle\int_{0}^{2\pi} \frac{1}{3+\cos t}dt\) </li>
<li> Show that : \(\displaystyle\lim_{x\rightarrow\infty}\dfrac{1}{x} \int_{0}^{x} \frac{1}{3+\cos t}dt = \frac{1}{2\sqrt{2}}\)</li>
</ol>
</p>

<i><b>Problem source : </b></i> My notebook<br>

<details open><summary><b><i>Solution :</i></b></summary>
<ol type="I">
<li> Firstly, observe that the integrand is symmetric around \(\pi\). Thus, \(\)\displaystyle\dfrac{1}{2\pi} \int_{0}^{2\pi} \frac{1}{3+\cos t}dt = 2\cdot\displaystyle\dfrac{1}{2\pi} \int_{0}^{\pi} \frac{1}{3+\cos t}dt\(\) Let us substitute \(\cos t = \frac{1-\tan^2\frac{t}{2}}{1+\tan^2\frac{t}{2}}\) , and put \(z = \tan\frac{t}{2}\). Then, we'll have : $$I := \int_{0}^{\pi} \frac{1}{3+\cos t}dt = \int_{0}^{\pi} \frac{1+\tan^2 \frac{t}{2}}{4+2\tan^2 \frac{t}{2}}dt$$
Observe that we can substitute \(\tan\frac{t}{2} = z\) directly, to get : $$I = \int_0^\infty \dfrac{2}{2(2 + z^2)} dz = \dfrac{1}{\sqrt{2}} \tan^{-1}\big(\frac{z}{\sqrt{2}}\big)\bigg\vert_0^\infty = \dfrac{\pi}{2\sqrt{2}}$$

Thus, \(\displaystyle\int_{0}^{2\pi} \frac{1}{3+\cos t}dt = 2I = \dfrac{\pi}{\sqrt{2}}\) </li><br>

<li> Define : \(f(t)=\frac{1}{3+\cos t}\) . Observe that \(f\) is periodic with period = \(2\pi\).

Therefore, for any \(x \in \mathbb{R}\), if \(N = \left\lfloor\frac{x}{2\pi}\right\rfloor\), then we have : $$\int_0^x f(t)\,dt = N \int_0^{2\pi}f(t)\,dt + \int_0^{x- 2\pi N}f(t)\,dt := A +B$$
Observe that : $$|B| = \left|\int_0^{x- 2\pi N}f(t)\,dt \right| \leq \int_0^{2\pi}|f(t)|\,dt\,$$
Thus, $$\lim_{x\to\infty}  \frac{1}{x} \int_0^x f(t)\,dt = \frac{1}{2\pi}\left(\lim_{x\to\infty} \frac{2\pi}{x} \left\lfloor \frac{x}{2\pi} \right\rfloor \right)\int_0^{2\pi}f(t)\,dt =\frac{1}{2\pi} \int_0^{2\pi}f(t)\,dt\,$$

Hence, we obtain : $$\lim_{x\to\infty}  \frac{1}{x} \int_0^x \dfrac{1}{3+\cos t}\,dt = \frac{1}{2\pi}\int_0^{2\pi}\dfrac{1}{3+\cos t}\,dt =\frac{1}{2\sqrt{2}}\quad\blacksquare$$
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



<p>
<b>B</b>Let \(n \geq 2\) be some fixed positive integer and suppose that \(a_{1}, a_{2}, \ldots, a_{n}\) are positive real numbers satisfying \(a_{1}+a_{2}+\cdots+a_{n}=2^{n}-1\)
Find the minimum possible value of

\[ \frac{a_{1}}{1}+\frac{a_{2}}{1+a_{1}}+\frac{a_{3}}{1+a_{1}+a_{2}}+\cdots+\frac{a_{n}}{1+a_{1}+a_{2}+\cdots+a_{n-1}} \]
</p>

<p>
<details open><summary>Sol.</summary>



Solution. We claim the the minimum possible value of this expression is \(n .\) Observe that by AM-GM, we have that

\begin{align*}
\frac{a_{1}}{1}+& \frac{a_{2}}{1+a_{1}}+\cdots+\frac{a_{n}}{1+a_{1}+a_{2}+\cdots+a_{n-1}} \\
&=\frac{1+a_{1}}{1}+\frac{1+a_{1}+a_{2}}{1+a_{1}}+\cdots+\frac{1+a_{1}+a_{2}+\cdots+a_{n}}{1+a_{1}+a_{2}+\cdots+a_{n-1}}-n \\
& \geq n \cdot \sqrt[n]{\frac{1+a_{1}}{1} \cdot \frac{1+a_{1}+a_{2}}{1+a_{1}} \cdots \frac{1+a_{1}+a_{2}+\cdots+a_{n}}{1+a_{1}+a_{2}+\cdots+a_{n-1}}}-n \\
&=n \cdot \sqrt[n]{1+a_{1}+a_{2}+\cdots+a_{n}}-n \\
&=2 n-n=n
\end{align*}


Furthermore, equality is achieved when \(a_{k}=2^{k-1}\) for each \(1 \leq k \leq n\).
<i>Source: CMO 2021</i>
</details>
</p>




<p>

</p>

<details open><summary>Sol.</summary>


\begin{align*}
&=\frac{1}{3} \pi r^{2} h-\frac{1}{3} \pi r_{1}^{2}(h-10) \\
&=\frac{1}{3} \pi\left(r^{2} h-r_{1}^{2}(h-10)\right) \\
&=\frac{1}{3} \pi r_{2}^{2} \times 11
\end{align*}



\[ r^{2} h-r_{1}^{2}(h-10)=11 r_{2}^{2} \]

To find the height of the empty space in the second scenario, we just need to calculate what $h-11$ is.
It's clear from a similar triangles argument that

\begin{align*}
\frac{r_{1}}{r}&=\frac{h-10}{h} \Rightarrow r_{1}=\frac{r(h-10)}{h} \\
\frac{r_{2}}{r}&=\frac{11}{h} \quad \Rightarrow \quad r_{2}=\frac{11 r}{h}
\end{align*}


Hence, we can now substitute equations (2) and (3) into equation (1) to give

\[ r^{2} h-\frac{r^{2}(h-10)^{2}}{h^{2}}(h-10)=11 \frac{11^{2} r^{2}}{h^{2}} \Rightarrow h-\frac{(h-10)^{3}}{h^{2}}=\frac{11^{3}}{h^{2}} \]

Now, solving for \(h\) gives:

\begin{align*}
h^{3}-(h-10)^{3} &=11^{3} \\
h^{3}-\left(h^{3}-30 h^{2}+300 h-1000\right) &=11^{3} \\
30 h^{2}-300 h-331 &=0
\end{align*}


and so

\[ h=\frac{150 \pm \sqrt{32430}}{30} \]

Since \(h>0\), then

\[ h=\frac{150+\sqrt{32430}}{30} \approx 11.00277 \cdots \mathrm{cm} \]

</details>


<p>
<b>B6</b>. \(ABC\) is an equilateral triangle and \(P\) is point on the circumcircle of \(ABC\). \(P\) is
any point on the arc \(AC\). Prove that \(PB=PA+PC\).

<p style="text-align:center">
<img src="/assets/images/mt10_circumcircle.png"/>
</p>



</p>

<p>
<b>B3.</b> In how many ways can \(2^{100}\) be expressed as a sum of four squares of integers?
</p>

<details open><summary>Sol.</summary>
We solve for the general case of \(2^n\). If \(\mathrm{n}=1,2^{\mathrm{n}}=2^{1}=2\) which is expressible In only one way as \(1^{2}+1^{2}+0^{2}+0^{2}\). If \(n=2,2^{n}=2^{2}=4\) which is expressible in two ways as \(2^{2}+0+0+0\), or as \(1^{2}+1^{2}+1^{2}+1^{2}\)
If \(n \geqslant 3,2^{n}\) is divisible by 8. Now the square of an odd number leaves a remainder of 1 on division by 8. \(\left[(2 k+1)^{2}\right.\) \(=8 \cdot \frac{\mathrm{k}(\mathrm{k}+1)}{2}+1\) where \(\frac{\mathrm{k}(\mathrm{k}+1)}{2} 1 \mathrm{~s}\) an integer, as
either \(k\) or \(k+1\) must be even.] It follows that \(x_{1}{ }^{2}+x_{2}{ }^{2}+x_{3}{ }^{2}+x_{4}{ }^{2}\) cannot be
divisible by 8 if any of the \(x_{1}\) are odd numbers. Therefore,
1f \(n \geq 3\) and \(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=2^{n}(1)\)
every \(x_{1}\) 1s even, \(x_{1}=2 X_{1}\) say, and \(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=2^{n-2}\)
Every solution of (1) may be obtained by doubling up the \(\mathrm{X}_{1} \mathrm{~s}\) in a solution of \((2)\), so that \((1)\) and \((2)\) have the same number of solutions. Hence, repeating the argument, the number of solutions of \(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=2^{n}\)
1s the same as the number of solutions of \(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=2^{1}\)
If \(n\) is odd, namely 1 , or of
\(x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}=2^{2}\)
If \(\mathrm{n} 1 \mathrm{~s}\) even, namely 2 .
</details>







<!--
Improper integrals. Exercises.
https://web.math.princeton.edu/~nelson/104/ImpIntSolns.pdf
-->




