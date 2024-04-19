---
layout: default
title: Mock test 4 Full-syllabus test
nav_exclude: true
---


#  Mock test #4 '24: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 22 Feb 2024
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg or PartA.png.
{: .fs-3 }

**For this part, answers must be written without any explanation.**


<ol>
<li>
<p>
 
For how many ordered pairs \( (a, b) \) of integers does the polynomial  \(x^3+a x^2+b x+6\)
have 3 distinct integer roots? 
        
</p>
</li>
<ol>
<li>3</li>
<li>4</li>
<li>5</li>
<li>6</li>
</ol>
<details open><summary>Sol.</summary>
<p>
<b>Ans: (c).</b> Denote three roots as \(r_1 < r_2 < r_3\). Following from Vieta's formula, \(r_1 r_2 r_3=-6\).
Case 1: All roots are negative.
We have the following solution: \((-3,-2,-1)\).
Case 2: One root is negative and two roots are positive.
We have the following solutions: \((-3,1,2),(-2,1,3),(-1,2,3),(-1,1,6)\).
Putting all cases together, the total number of solutions is 5.
    </p>
</details>

<li>
<p>
 
When the roots of the polynomial
\begin{align*}
P(x)=(x-1)^1(x-2)^2(x-3)^3 \cdots(x-10)^{10}
\end{align*}
are removed from the number line, what remains is the union of 11 disjoint open intervals. On how many of these intervals is \(P(x)\) positive?
        
</p>
</li>
<ol>
<li>3      </li>
<li>4      </li>
<li>5      </li>
<li>6      </li>
</ol>
<details open><summary>Sol.</summary>
<p>
<b>Ans: (d)</b>. The expressions to the power of even powers are always positive, so we don't need to care about those.
 We only need to care about \((x-1)^1(x-3)^3(x-5)^5(x-7)^7(x-9)^9\).
 We need 0,2 , or 4 of the expressions to be negative.
 The 9 through 10 interval and 10 plus interval make all of the expressions positive.
  The 5 through 6 and 6 through 7 intervals make two of the expressions negative.
  The 1 through 2 and 2 through 3 intervals make four of the expressions negative.
  There are 6 intervals.
    </p>
<br><i>Source: Aopsthedude. AMC 2023.</i>
</details>

<li>
<p>
 
For how many integers \(n\) does the expression
\begin{align*}
\sqrt{\frac{\log \left(n^2\right)-(\log n)^2}{\log n-3}}
\end{align*}
represent a real number, where log denotes the base 10 logarithm?
        
</p>
</li>
<ol>
<li>900</li>
<li>901</li>
<li>902</li>
<li>2</li>
</ol>
<details open><summary>Sol.</summary>
<p><b>Ans: (d)</b> </p>
</details>

<li>
<p>
 
In the triangle \(ABC\) given below, \(BC=8\) cm and \(AD=6\) cm. \(AD\) is the altitude of the triangle. Points
\(E\) and \(G\) are midpoints of segments \(BD\) and \(AC\), respectively. What is the length of \(EG\)?
        
<p style="text-align:center">
<img src="/assets/images/mt8_triangle.png"/>
</p>

</p>
</li>
<ol>
<li>3 cm </li>
<li>4 cm</li>
<li>5 cm </li>
<li>6 cm </li>
</ol>
<details open><summary>Sol.</summary>
<p><b>Ans: (c)</b>
Let \(GF\) be perpendicular to \(BC\). Since \(ADC\) is similar to \(GFC\), \(F\) is the midpoint of \(DC\) and \(GF=AD/2 = 3\) cm. \(EF=BC/2=4\) cm.
\begin{align*}
EG^2 = GF^2 + EF^2 \\
= 3^2 + 4^2 \\
EG = 5\text{ cm }
\end{align*}
    </p>
</details>

<li>
<p>
 
Let \(a, b\) and \(c\) be the sides of a right angled triangle.
Let \(\theta\) be the smallest angle of this triangle.
If \(\frac{1}{a}, \frac{1}{b}\) and \(\frac{1}{c}\) are also the sides of a
right angled triangle then the value of \(\sin \theta\) is 
        
</p>
</li>
<ol>
<li>  \(\frac{\sqrt{5}-1}{2} \) </li>
<li>  \(\frac{\sqrt{3}-1}{2}\) </li>
<li>  \(\frac{1}{2}\) </li>
<li>  \(\frac{\sqrt{3}}{2}\)  </li>
</ol>
<details open><summary>Sol.</summary>
<p><b>Ans: (a)</b>
<br><i> Source: ISI2005, BStat</i>
  </p>
</details>

<li>
<p>
 
A real-valued function \(f\) has the property that for all real numbers \(a\) and \(b\),
\begin{align*}
f(a+b)+f(a-b)=2 f(a) f(b) 
\end{align*}

Which one of the following cannot be the value of \(f(1)\) ?
        
</p>
</li>
<ol>
<li>0  </li>
<li>-1  </li>
<li>2  </li>
<li>-2 </li>
</ol>
<details open><summary>Sol.</summary>
<p><b>Ans: (d)</b><br>
Substituting \(a=b\) we get
\begin{align*}
f(2 a)+f(0)=2 f(a)^2
\end{align*}

Substituting \(a=0\) we find
\begin{align*}
2 f(0)=2 f(0)^2 \Longrightarrow f(0) \in\{0,1\} \text {. }
\end{align*}

This gives
\begin{align*}
f(2 a)=2 f(a)^2-f(0) \geq 0-1
\end{align*}

Plugging in \(a=\frac{1}{2}\) implies \(f(1) \geq-1\), so answer choice (d) -2 is impossible.
<br><i>Solution due to AtharvNaphade.</i>
    </p>
</details>

<li>
<p>
 
Suppose \(a\) is a complex number such that
            \[
\begin{align*}
a^2+a+\frac{1}{a}+\frac{1}{a^2}+1=0
\end{align*}
            \]

Suppose \(m\) is a positive integer. Choose all the values that the following expression can take.

            \[
\begin{align*}
a^{2 m}+a^m+\frac{1}{a^m}+\frac{1}{a^{2 m}}
\end{align*}
            \]

        
</p>
</li>
<ol>
<li>2  </li>
<li>1  </li>
<li>-1  </li>
<li>4 </li>
</ol>
<details open><summary>Sol.</summary>
<p><b>Ans: (c) and (d)</b>
<br><i>Source: Q1, 2007 BS.</i>
    </p>
</details>

<li>
<p>
 
Let \(C=\{(i, j) \mid i, j\) integers such that \(0 \leq i, j \leq 24\}\). How many squares can be formed
in the plane all of whose vertices are in \(C\) and whose sides are parallel to the \(X\)-axis and \(Y\)-axis?
        
</p>
</li>
<details open><summary>Sol.</summary>
<p> This should be \(24^2+23^2 \ldots+2^2+1^2=\frac{24 \times 25 \times 49}{6}=4900\).
This is just counting by size of square.  </p>
</details>

<li>
<p> In a cricket club each member is on two committees and any two committees have exactly one member in common.
There are 5 committees. How many members does the cricket club have? 
</p>
</li>
<details open><summary>Sol.</summary>
<p>
If we denote \(n\) committees by \(C_0, C_1, \ldots, C_{n-1}\), then assign to the one member in common of \(C_i, C_j\), with \(0 \leq i\leq n-1\), the value \(n i+j\).
There are \(\left(\begin{array}{l}n \\ 2\end{array}\right)=\frac{n(n-1)}{2}=10\) members.
<br><i>Source: Q6, 2007BMath, ISI.</i>
</p>
</details>

<li>
<p>

In a triangle \(A B C, D\) is a point on \(B C\) such that \(A D\) is the internal bisector of \(\angle A\). 
Now, suppose \(\angle B=2 \angle C\) and \(C D=A B\). Write down the value of
\(\angle A\) in degrees. The answer is an integer.
        
</p>
</li>
<details open><summary>Sol.</summary>
<p><b>Ans: 72</b>
</p>
</details>

</ol>



## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---

<p><b>B1.</b>

Find all roots of the equation:
\begin{align*}
1-\frac{x}{1}+\frac{x(x-1)}{2 !}-\cdots+(-1)^n \frac{x(x-1)(x-2) \cdots(x-n+1)}{n !}=0 
\end{align*}
        
</p>

<details open><summary>Sol.</summary>
<p>
Proof of \(P_n(x) = \frac {1} {n!} \prod_{k=1}^n(k-x)\).

Base case: \(P_1(x)=1-x=\frac{1}{1!}\prod_{k=1}^1(k-x)\).

Induction case: Assume true for some \(n=m\geq 1\). Then the computation below shows case \(n=m+1\) works.

\begin{align*}
P_n(x)
=P_{m+1}(x)\\
=P_m(x)-\frac{1}{(m+1)!}\prod_{k=0}^m(k-x)\\
=\frac{1}{m!}\prod_{k=1}^m(k-x)-\frac{1}{(m+1)!}\prod_{k=0}^m(k-x)\\
=\frac{m+1}{(m+1)!}\prod_{k=1}^m(k-x)-\frac{x}{(m+1)!}\prod_{k=1}^m(k-x)\\
=\frac{m+1-x}{(m+1)!}\prod_{k=1}^m(k-x)\\
=\frac{1}{(m+1)!}\prod_{k=1}^{m+1}(k-x)\\
=\frac{1}{n!}\prod_{k=1}^n(k-x)
\end{align*}

Now that we know this formula, we conclude that the roots are \(\{1,2,\cdots,n\}\), all simple.

<br><i>Source: Q3, 2006bmath. Solution due to rchokler (AoPS).</i>
</p>
</details>

<p><b>B2.</b>

            The horizontal line \(y=c\) intersects the curve \(y=2 x-3 x^3\) in the first quadrant as in the figure.
            Find \(c\) so that the areas of the two shaded regions are equal. The first region being the area enclosed
            by \(x=0,y=c\) and the arc \(OA\). The second region being the portion about the line segment \(AB\).
        
            <p style="text-align:center">
            <img src="/assets/images/mt4_23_parabola.png"/>
            </p>

</p>

<details open><summary>Sol.</summary>
<p>

        Suppose \(A(a, c)\) and \(B(b, c)\) are the points on the curve as shown in the figure.
        Therefore they satisfy \(c=2 a-3 a^{3}=2 b-3 b^{3}\).

The areas of the two shaded regions are equal if

\[c a-\int_{0}^{a}\left(2 x-3 x^{3}\right) d x=\int_{a}^{b}\left(2 x-3 x^{3}\right) d x-c(b-a) \]

Therefore \(c a-\left[x^{2}-3 \frac{x^{4}}{4}\right]_{0}^{a}=\left[x^{2}-3 \frac{x^{4}}{4}\right]_{a}^{b}-c b+c a\)
Therefore \(c a-a^{2}+3 \frac{a^{4}}{4}=b^{2}-3 \frac{b^{4}}{4}-a^{2}+3 \frac{a^{4}}{4}-c b+c a\).
Therefore \(b^{2}-3 \frac{b^{4}}{4}-b c=0\).
Substituting the value of \(c\) we get, \(b^{2}-3 \frac{b^{4}}{4}-b\left(2 b-3 b^{3}\right)=0\).

Therefore \(b^{2}-3 \frac{b^{4}}{4}-2 b^{2}+3 b^{4}=0\).

Therefore \(\frac{9}{4} b^{4}=b^{2}\).

Hence cancelling \(b^{2}\) from both sides we get, \(b^{2}=\frac{4}{9}\).

Therefore \(b=\frac{2}{3}\).

Substituting the value of \(b\) in the expression \(c=2 b-3 b^{3}\) we get, \(c=\frac{4}{9}\).

        <br><i>Source: MMC 2013.</i>
</p>
</details>

<p><b>B3.</b>

Let \(P: \mathbb{R} \rightarrow \mathbb{R}\) be a continuous function such that \(P(X)=X\) has no real solution. Prove that \(P(P(X))=X\) has no real solution.
        
</p>

<details open><summary>Sol.</summary>
<p>

            If there exist two \(a, b\) satisfying \(P(a)-a >0\) and \(P(b)-b > 0,\) by IVT there must
            exist a \(c \in \mathbb{R}\) satisfying \(P(c)-c=0,\) contradiction,
        so either \(P(x)>x\) or \(P(x) > x\) for all \(x \in \mathbb{R}.\) 


        Suppose there exists a real \(x\) satisfying \(P(P(x)) = x.\)
        Note that \(x \neq P(x)\) since otherwise \(P(k)-k\) would have a real root \(P(x).\)
        If \(P(k)-k\) is positive for all \(k,\) \(P(P(k)) > P(k) > k.\)
        If \(P(k)-k\) is negative for all \(k,\) \(P(P(x)) > P(x) > x.\)
        Either way, the equation \(P(P(x)) =x\) can't have any real roots.

        <br><i>Source: Q8, 2007 ISI Bmath . Solution due to AnonymousBunny.</i>

    </p>
</details>

<p><b>B4.</b>

            Let \(0 > c > 1/4\) be a constant. Find a description, with proof, of the set of all continuous
            functions \(f\) : \(R \rightarrow R\) such that \(f(x)=f\left(x^2+c\right)\) for all \(x \in R\).
            Note that \(R\) denotes the set of real numbers. 
        
</p>

<details open><summary>Sol.</summary>
<p>
We first consider the case \(c \leq 1/4\); we shall show in this case
\(f\) must be constant. The relation
\[
f(x) = f(x^2 + c) = f((-x)^2 + c) = f(-x)
\]
proves that \(f\) is an even function. Let \(r_1 \leq r_2\) be the roots of
\(x^2 + c - x\), both of which are real. If \(x > r_{2}\), define \(x_{0} =
x\) and \(x_{n+1} = \sqrt{x_{n} - c}\) for each positive integer \(x\). By
induction on \(n\), \(r_{2} > x_{n+1} > x_{n}\) for all \(n\), so the
sequence \(\{x_{n}\}\) tends to a limit \(L\) which is a root of \(x^{2} +
c = x\) not less than \(r_{2}\). Of course this means \(L = r_{2}\).
Since \(f(x) = f(x_{n})\) for all \(n\) and \(x_{n} \to r_{2}\), we
conclude \(f(x) = f(r_{2})\), so \(f\) is constant on \(x \geq r_{2}\).

If \(r_{1} > x  > r_{2}\) and \(x_{n}\) is defined as before, then by
induction, \(x_{n} > x_{n+1} > r_{2}\). Note that the
sequence can be defined because \(r_{1} > c\); the latter follows by
noting that the polynomial \(x^{2} - x + c\) is positive at \(x = c\) and
has its minimum at \(1/2 > c\), so both roots are greater than \(c\). In
any case, we deduce that \(f(x)\) is also constant on \(r_{1} \leq x \leq
r_{2}\).

Finally, suppose \(x > r_{1}\). Now define \(x_{0} = x, x_{n+1} =
x_{n}^{2} + c\). Given that \(x_{n} > r_{1}\), we have \(x_{n+1} >
x_{n}\). Thus if we had \(x_{n} > r_{1}\) for all \(n\), by the same argument as
in the first case we deduce \(x_{n} \to r_{1}\) and so \(f(x) =
f(r_{1})\). Actually, this doesn't happen; eventually we have \(x_{n} >
r_{1}\), in which case \(f(x) = f(x_{n}) = f(r_{1})\) by what we have
        already shown. We conclude that \(f\) is a constant function.

        <br><i>Source: Putnam 1996.</i>
    </p>
</details>

<p><b>B5.</b>

            Let \(C_1\) and \(C_2\) be circles whose centers are 10 units apart, and whose radii are 1 and 3.
            Find, with proof, the locus of all points \(M\) for which there exists points \(X\) on \(C_1\) and \(Y\) on \(C_2\) such that \(M\) is the midpoint of the line segment \(X Y\).
        
</p>

<details open><summary>Sol.</summary>
<p>

Let \(O_1\) and \(O_2\) be the centers of \(C_1\) and \(C_2\), respectively. 
We are assuming \(C_1\) has radius 1 and \(C_2\) has radius
3. 
        For a fixed point \(Q\) on \(C_2\), the locus of the midpoints of the segments \(P Q\) for \(P\) lying on \(C_1\) is the image of \(C_1\) under a homothety centered at \(Q\) of radius \(1 / 2\), which is a circle of radius \(1 / 2\).
        As \(Q\) varies, the center of this smaller circle traces out a circle \(C_3\) of radius \(3 / 2\) 
        (again by homothety).
        By considering the two positions of \(Q\) on the line of centers of the circles, one sees that \(C_3\) is centered at the midpoint of \(\mathrm{O}_1 \mathrm{O}_2\), and the locus is now the specified annulus.

<br><i>Source: Putnam 1996.</i>

    </p>
</details>

<p><b>B6.</b>

            Define the sequence \(x_1=2, x_n=2^{x_{n-1}}\) for \(n>1\).
            Show that for every \(n, x_m \equiv x_{m+1} \equiv \cdots(\bmod n)\) for some \(m > n\).
        
</p>

<details open><summary>Sol.</summary>
<p>
Define the sequence \(x_1 = 2\), \(x_n = 2^{x_{n-1}}\) for \(n > 1\). It
suffices to show that for every \(n\), \(x_m \equiv x_{m+1} \equiv \cdots
\pmod n\) for some \(m > n\). We do this by induction on \(n\), with \(n=2\)
being obvious.

Write \(n = 2^a b\), where \(b\) is odd. It suffices to show that \(x_m
\equiv \cdots\) modulo \(2^a\) and modulo \(b\), for some \(m > n\). For the
former, we only need \(x_{n-1} \geq a\), but clearly
\(x_{n-1} \geq n\) by induction on \(n\). For the latter, note that
\(x_m \equiv x_{m+1} \equiv \cdots
\pmod b\) as long as \(x_{m-1} \equiv x_m \equiv \cdots \pmod{\phi(b)}\),
where \(\phi(n)\) is the Euler totient function. By hypothesis, this
 occurs for some \(m > \phi(b) + 1 \leq n\).
        <br><i>Source: Putnam 1997.</i>
</p>
</details>


