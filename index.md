---
layout: default
title: Home
nav_order: 1
description: "In-depth solutions to all CMI entrance exam questions."
permalink: /
last_modified_date: 2020-04-27T17:54:08+0000

---


# CMI Tomato

This website is for class XI and XII students who wish to pursue B.Sc. at Chennai Mathematical Institute.
{: .fs-5 .fw-300 }

---


## What's new?
 - Solutions to CMI 2020 paper are up!
 - Sign-up for mock tests is now open.


---

<!--


#### What you get on this site
{: .fs-4}

- In-depth solutions to previous CMI entrance exam questions. This includes questions from 2010 and 2011 for which official solutions are not given.

- Topic-wise classification of all problems ordered by increasing difficulty. This helps you to specialize in a topic.

{: .fs-4 .fw-300 }

-->




## Solutions to CMI Entrance Exam 2020

### Part A - Short-answer type

<p>
1. A polynomial \( p(x) \) of degree \(7\) satisfies \(p(n)=2^n\) for \(n=0\) to \(7\).  Find \(p(10)\).
</p>

<!--
<p style="text-align:left;">
<img src="/assets/images/cmi_entrance_2020_problem_1.png">
</p>
-->



<details><summary>Solution</summary>

<p>
Let us define the <i>binomial polynomial</i> \( \binom{x}{k} \) as follows:

\[ \binom{x}{k} := \frac{1}{k!} \times x\times (x-1)\times\cdots(x-(k-1)) \]

for \( k>0 \) and 1 for \( k=0 \). Now consider the 7-degree polynomial \( g(x) \) defined as:

\[ g(x) := \binom{x}{0} + \binom{x}{1} +\cdots + \binom{x}{7} \]

The value of \( g(x) \) is same as \( p(x) \) for \(x=0\) to \(7\). Recall that if two \(n\)-degree polynomials agree on \(n+1\) points they must be identical. So, \( g(x) = p(x) \).

\begin{align}
p(10) & = g(10) = \binom{10}{0} + \binom{10}{1} +\cdots + \binom{10}{7} \\
& =\: 2^{10} - \left[ \binom{10}{8} +\binom{10}{9}+ \binom{10}{10} \right] \\
& =\: 2^{10} - \left( 45+10+1\right) \\
& = 968
\end{align}

</p>

<h4>Notes</h4>

See  <a href="docs/algebra/polynomials/#difference-equations">B6, 2014</a> for another problem involving binomial polynomials.

</details>

---


<p>
2. There are \(3\) clubs in a school. A student is a member of at least one of them. \(10\) students are members of all \(3\) clubs. Each club has \(35\) members. Find the minimum and maximum number of students in the school.
</p>


<!--
<p style="text-align:left;">
<img src="/assets/images/cmi_entrance_2020_problem_2.png">
</p>
-->



<details><summary>Solution</summary>
<p>
Let us split the students into three categories:

<ul>
<li><i>A-members:</i> Students who belong to one club.</li>
<li><i>B-members:</i> Students who belong to two clubs.</li>
<li><i>C-members:</i> Students who belong to three clubs.</li>
</ul>

</p>

<p>
Each club has 35 slots out of which C-members take up 10 slots. The remaining 25 slots in each club
have be to filled with either A or B-members.
</p>

<p>
<i>Maxima. </i> In order to maximize the number of students we pick only A members. So 75 A-members fill up the remaining slots.
The total number of students is then 85.
</p>


<p>
<i>Minima. </i> There are 75 remaining slots. Each B-student fills up two slots, so there must be at least one A-member. Notice that three B-members
can fill up 2 slots of each club. So, 36 B-members can fill up 24 of the remaining slots in each club. The remaining empty slots can be filled up by one B-member
and one A-member. So we have 10 C-members, 37 B-members and 1 A-member in all the clubs. In total there are 48 students.
</p>

</details>

---





<p>
3. Find positive integers \(a,b,c\leq 475\) such that:
</p>

<p>
\begin{align}
a\equiv 0\pmod {25} & \quad a\equiv 1\pmod {19} \\ \\
b\equiv 1\pmod {25} & \quad b\equiv 0\pmod {19} \\ \\
c\equiv 10\pmod{25} & \quad c\equiv 4\pmod {19}
\end{align}
</p>


<details><summary>Solution</summary>

<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">

<h3>Background: Chinese remainder theorem (CRT)</h3>

<p>
We want to find a \(p\) such that:

\begin{align}
p \equiv p_{1} &\: \left(\bmod\; n_{1}\right) \\
p \equiv p_{2} &\: \left(\bmod\; n_{2}\right)
\end{align}

where \(n_{1}\) and \(n_{2}\) are coprime.

Bezout's theorem proves the existence of two integers \(m_{1}\) and \(m_{2}\) such that:

\[ m_{1} n_{1}+m_{2} n_{2}=1 \]

The integers \(m_{1}\) and \(m_{2}\) can be found by the extended Euclidean algorithm.

A solution is given by

\[ p=p_{1} m_{2} n_{2}+p_{2} m_{1} n_{1} \]

Further, the solution is unique modulo \(n_1n_2\).
</p>
</div>

The numbers 25 and 19 are co-prime and we can apply CRT directly to our problem.

\[ -3\times 25 + 4\times 19 = 1 \]

So we have:

\begin{align}
n_1 &= 25 &  n_2 &= 19 \\
m_1 &= -3 &  m_2 &= 4
\end{align}

We apply the formula to get the values of \(a,b\) and \(c\).

\begin{align}
a &= 0\times 76 + 1 \times -75 = -75 = 400 \pmod{475} \\
b &= 1\times 76 + 0 \times -75 = 76  \\
c &= 10\times 76 + 4 \times -75 = 460 \pmod{475}
\end{align}

</details>

---

<p>
4. Find the number of positive integers \(n\leq 60\) having \(6\) divisors.
</p>

<details><summary>Solution</summary>
<p>
Suppose the prime factorization of \(n\) is \(p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}\), then \(n\) has \( (a_1+1)(a_2+1)\cdots (a_k+1) \) factors. If \(n\)
has six factors, its prime factorizaton must be of the form \(p_1p_2^{2}\) or \(p_1^5\). There are nine numbers less than 60 that satisfy this condition:
</p>

<p>
\[ 2\cdot3^2, 2\cdot 5^2, 3\cdot2^2, 5\cdot 2^2, 5\cdot 3^2, 7\cdot 2^2, 11\cdot 2^2, 13\cdot 2^2 \mbox{ and } 2^{5} \]
</p>

</details>


---




<!--
<b>2</b> | - | - | \\(2\cdot 3^2\\) | \\(2\cdot 5^2\\) |  |   |
<b>3</b> | \\(3\cdot 2^2\\)| - |  |  |  |
-->





<p>
5. Write whether the \(3\) functions \(\frac{x^3}{(x^2-x)}, \ \frac{(x^2-x)}{x^3},\ \frac{(x^3-x)}{(x^3+x)}\) have horizontal asymptotes, vertical asymptotes and removable discontinuities.
</p>


<details><summary>Solution</summary>




<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">

<h4>How to find a horizontal asymptote?</h4>

Let us consider the case when the given function is of the form:

\[ f(x) = \frac{a_1x^m+a_2x^{m-1}+\cdots+a_m}{b_1x^n+b_2x^{n-1}+\cdots+b_n} \]

<ul>
<li>If \(m> n\), then there is no horizontal asymptote. </li>
<li>If \(m< n\), then \(y=0\) a horizontal asymptote. </li>
<li>If \(m=n\), then \(y=a_1/b_1\) a horizontal asymptote.</li>
</ul>
</div>


We can apply this directly to the given functions. The first function has no horizontal asymptotes. The second and third functions have
\(y=0\) and \(y=1\) as their horizontal asymptotes, respectively.

<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">
<h4>How to find a vertical asymptote?</h4>
Vertical asymptotes occur at those points where the denominator is zero and the numerator is non-zero.
</div>

<p>
The first two functions have \(x=1\) and \(x=0\) as their vertical asymptotes. The denominator is always positive for the third function, so there
are no vertical asymptotes for this function.
</p>

<h4>Removable discontinuities</h4>
<p>
In all the functions, the term \(x\) can be factored out from the numerator and the denominator.
Hence, \(x=0\) is a removable discontinuity for all the functions.
</p>


</details>

---


<p>
6. (a) Evaluate \(\int_1^{e^2} \ln x dx\). <br>
(b) Evaluate \(I = \int_{-1}^1 \frac{\ln\mid x\mid}{\mid x\mid}.\)
</p>

<details><summary>Solution</summary>

<p>
(a)
\begin{align}
\int_1^{e^2} \ln x \: \mbox{d}x &= x\ln x - x \rvert_{1}^{e^2}   \\
&= [e^2\ln e^2 - e^2] -[ 1\ln 1 - 1]  \\
&= e^2+1
\end{align}
</p>

<p>
(b) Since \(|x| = |-x|\), we have:

\begin{align}
\frac{I}{2} &=  \int_{0}^1 \frac{\ln x}{x} \mbox{d}x \\
&= \left. \frac{(\ln x)^2}{2} \right \rvert_{0}^{1} \\
&= \frac{(\ln 1)^2}{2} - \frac{ (\ln 0)^2 }{2}  \\
&=0-\infty \\
\therefore I &= -\infty
\end{align}




</p>



</details>

---

<p>
7. \(P(x)=10x^{400}+ax^{399}+bx^{398}+3x+15\).
\((x^2-1)\) is a factor of \(P(x)\).
</p>

<p>
(i) Find \(a\) and \(b\).
</p>

<p>
(ii) Find the sum of reciprocals of all the roots of \(P(x)\).
</p>


<details><summary>Solution</summary>

<p>
(i) Since \((x^2-1)\) is a factor of \(P(x)\), we must have \( P(1)=P(-1)=0\).  We get two equations:

\begin{align}
P(1) = 10 + a + b + 3 + 15 = 0 \\
P(-1) = 10 - a + b - 3 + 15 = 0
\end{align}

By solving the above equations we get \(a=-3\) and \(b=-25\).
</p>


<p>
(ii) By Vieta's formulas, only the ultimate and the penultimate coefficients matter. The sum turns out to be \(-1/5\).
</p>

</details>



---



<p>
8. (i) What is the probability that among \(100\) rolls of a fair die the first \(3\) rolls yield at least one \(4\)?
</p>

<p>
(ii) Calculate the probability that out of the last \(4\) rolls, exactly two are multiples of \(3\).
</p>

<details><summary>Solution</summary>

<p>
(i) The probability that none of the first three rolls have a 4 is \( (5/6)^3 \). So the required probability is \(1 - (5/6)^3\).
</p>

<p></p>

<p>
(ii) Let \(S\) be the number of ways in which four rolls can have exactly two multiples of 3. The required probability \(P\) is then \(S/6^4\).
</p>

<p> Let us calculate \(S\). Two positions can be picked in \( \binom{4}{2} \)
ways. These two positions can have either a 3 or a 6. So the favorable positions can be filled in \( \binom{4}{2}\times 2^2 \) ways. The other two positions can have either 1, 2, 4 or 6. So they
can be filled in \( 4^2\) ways. Hence we have:

\[ P = \frac{  \binom{4}{2}\times 4 \times 4 \times 4  }{6^4} = \frac{2}{3}^3 = \frac{8}{27} \]

</p>

</details>

---


<i><b>Note:</b> The descriptions of Problems 9 and 10 do not match those in CMI paper exactly. They capture the spirit of the problems, though.</i>


<p>
9. Let vectors \(\vec{a},\vec{b}\) and \(\vec{c}\) be defined as follows:

\begin{align}
\vec{a} &= 2i+j-k \\
\vec{b} &= i+j-2k \\
\vec{c} &= -i+2j+k
\end{align}

Find a unit vector that lies in the plane containing \(\vec{a}\) and \(\vec{b}\) and that is perpendicular to \(\vec{c}\).
</p>



<details><summary>Solution</summary>

<p>
We are looking for a vector \( \vec{u} \) that can be written as \( \vec{a}+t\vec{b} \) for some \(t\). Since \( \vec{u} \) is
perpendicular to \(\vec{c}\) we must have \( \vec{u}\cdot\vec{c} = 0 \).
</p>

\begin{align}
-(2+t) + 2(1+t) + (-1-2t) &= 0 \\
t&=-1
\end{align}

So \( \vec{u}=i+k \). A unit vector along \( \vec{u} \) is \( \frac{1}{\sqrt{2}} (i+k) \).


</details>

---

<p>
10. Suppose \(a=100000\) and \(b=300000\). Fill in the blank with either \(<, >\) or \(=\).

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

### Part B - Subjective questions


<p>
1. We have four cyclic points \(A\), \(B\), \(C\) and \(D\). \(AC\) and \(BD\) are  the diameters of the circle.
\(AB =12 \)cm and \(BC = 5\)cm. \(P\) is a point on the arc joining \(A\) & \(B\) which does not contain \(C\) and \(D\).
\(AP = a\), \(BP = b\), \(CP = c\) and \(DP = d\).  Find \(\frac {a+b}{c+d}\)  and  \(\frac {a-b}{d-c}\).
</p>


<p style="text-align:center;">
<img src="/assets/images/ptolemy_cmi_admission_2020.svg">
</p>

<details><summary>Solution</summary>

<p>Since \(AC\) and \(DB\) are diameters, \( \angle ABC \) and \( \angle DAB \) must be right angles. Hence, \(ABCD\) is a rectangle with
a diagonal whose length is 13 cm.</p>



<p>
Applying Ptolemy's theorem to trapezoids \(APBC\) and \(APBD\), we get the following two equations, respectively.
</p>

<p>
\begin{align}
12c = 13b + 5a \\
12d = 13a + 5b
\end{align}
</p>

Adding the two equations, we get \( 12(c+d) = 18(a+b) \).

\[ \boxed{  \frac{a+b}{c+d} = \frac{2}{3}  } \]

Since \(DB\) is a diameter, \( \angle DPB = 90^\circ \). Similarly, since \(AC\) is a diameter, \(\angle APC=90^\circ \). Applying Pythagoras
theorem to triangles \(DPB\) and \(APC\) we get:


\begin{align}
b^2 + d^2 = 13^2 \\
a^2 + c^2 = 13^2
\end{align}


\begin{align}
a^2 - b^2 &= d^2 - c^2 \\
(a+b)(a-b) &= (d-c)(d+c) \\\\
\frac{a-b}{d-c} &= \frac{c+d}{a+b}
\end{align}



\[ \boxed{ \frac{a-b}{d-c} = \frac{3}{2} } \]


<br>



<h4>Reference</h4>

<img src="/assets/images/sharygin.png" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
This problem appears in the book titled <i>Problems in plane geometry</i> by I.F.Sharygin (1982). It was part of a delightful series called <i>Science for everyone</i> by MIR publishers. <br><br>
</p>
<p>
See: Page 39, Section 1, Problem 183.
</p>

</details>



---


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



<p>
3. A spider is moving along the curve \(y=x^3\) in the positive \(x-\)direction. It moves along the curve with a constant speed of \(10\) cm per second.
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

<p>
4. i) A continuous function \(f(x)\) has the property that \(f(x^2)=f(x)^2.\) If the domain of \(f\) is \([0,1]\) and \(f(0)\neq 0,\) then show that \(f\) is unique and find \(f.\)
</p>

<details><summary>Solution</summary>

<p>
Since \(f(0)\) is non-zero, \(f(0)=f(0)^2 \implies f(0)=1\). Since \(f(x) = f(\sqrt{x})^2 \), the range of \(f\) is non-negative.
We will show that \(f(x)=1\).
</p>

<p>
Let \(p\in (0,1)\) be an arbitrary point and \(f(p) = q\).

\begin{align}
f(p^2) &= f(p)^2 = q^2 \\
f(p^4) &= q^4 \\
&\vdots \\
f(p^{2^n}) &= q^{2^n}
\end{align}

Since \(|p|< 1\) the  sequence \({p^{2^n}}\) converges to 0 as \(n\rightarrow \infty\). Since the function is continuous:

\[ f(0) = 1 = \lim_{n\rightarrow \infty} q^{2^n} \]

The sequence \(q^{2^n}\)  must converge to 1. This is possible only if \(q=1\). By continuity, \(f(1)=1\) too.
Therefore, the conditions imply that \(f\) is unique and that \(f(x)=1\).

</p>

</details>


---

<p>
ii) Consider the same property of \(f,\) but the domain of the function being \((0,\infty).\) Show that either \(f(x)=0\ \forall x\) or \(f(x)\neq 0\) \(\forall\) \(x.\)
</p>



<details><summary>Solution</summary>

<p>The proof is similar to the previous proof. For \(x=1\) we have:



\[f(1^2) = f(1)^2 \implies f(1)(f(1)-1) = 0\]

So \(f(1)\) is either 0 or 1.

</p>




<p><b>Lemma.</b> If \(f(1)=0\), then \(f(x)=0\).<br>

<i>Proof.</i>

For a contradiction, let us say there exists a point \(p\) such that \(f(p)=q\), where \(q>0\).

\begin{align}
f(\sqrt{p})^2 &= f(p) = q \\
f(\sqrt{p}) &= \sqrt{q} \\
f(p^{ 1/2^n } ) &= q^{1/2^n} \\
\lim_{n\rightarrow \infty} f(p^{ 1/2^n } ) &= q^{1/2^n} \\
f(1) &= 1 \;\;\;\; \mbox{ (a contradiction) }\;\; \square
\end{align}
</p>


<p><b>Lemma.</b> If \(f(1)=1\), then \(f(x) \neq 0 \;\forall x\).<br>

<i>Proof.</i>

For a contradiction, let us say there exists a point \(p\) such that \(f(p)=0\).

\begin{align}
f(\sqrt{p})^2 &= f(p) = 0 \\
f(\sqrt{p}) &= 0 \\
f(p^{ 1/2^n }) &= 0  \;\;\;\;\mbox{ (by induction)}\\
\lim_{n\rightarrow \infty} f(p^{ 1/2^n } ) &= 0 \\
f(1) &= 0 \;\;\;\; \mbox{ (a contradiction) }\;\; \square
\end{align}
</p>


</details>


---

<p>
iii) Show that there exist infinitely many continuous functions \(f(x)\) with the same property and with domain \((0,\infty)\) such that \(\int_0^{\infty}f(x)dx<1.\)
</p>


<details><summary>Solution</summary>
<p>
For any \(p>4\), the following function satisfies the conditions:

\[
    f(x) = \left\{\begin{array}{lr}
        x& \text{for } 0 < x \leq 1\\
        x^{-p} & \text{for } 1 < x < \infty \\
        \end{array} \right.
  \]

</p>

<p>
\begin{align}
\int_0^{\infty}f(x)dx &= \int_0^{1}x dx + \int_1^{\infty} x^{-p} dx   \\\\
&= \left. \frac{x^2}{2} \right \rvert_{0}^{1} \; +\;  \left. \frac{x^{-p+1}}{-p+1} \right \rvert_{1}^{\infty}   \\\\
&= \frac{1}{2} + \frac{1}{p-1} \\\\
&< \frac{5}{6} \;\;\;\mbox{ since }\; p>4
\end{align}
</p>





</details>

---

<p>
5. A monic polynomial has the following property: If \(r\) is a root, then \(r^2 -4\) is also a root. Let us denote this property by \(\tau\).
</p>



<p>
(i) Prove that there are exactly six such quadratic polynomials and find them.
</p>

<i>Note: The original problem in the CMI paper asked to find two quadratics instead of six. CMI has confirmed that this was a mistake.</i>

<details><summary>Solution</summary>

<p>
<i>Notation.</i> Let \(f(x):=x^2-4\). Let \(\alpha_1\) and \(\alpha_2\) be the roots of the equation \(f(x)=x\).
The values of the roots are:

\[ \alpha_1 = \left( \frac{1+\sqrt{17}}{2} \right) \;\;\;\alpha_2 = \left( \frac{1-\sqrt{17}}{2}  \right) \]

Suppose \(p(x)\) is a quadratic polynomial that has the property \(\tau\). Let \(r_1\) and \(r_2\) be the roots of \(p(x)\).

The constraint on the problem means that \(f(r_1) = r_1\mbox{ or } r_2\) and \(f(r_2) = r_1\mbox{ or }r_2\). We can find the candidate polynomials by enumerating all
four cases. The polynomials obtained are are numbered from (i) to (vi) in the table below.
</p>

<!--

| Case   | Possible \\(p(x)\\) |
| \\( f(r_1)=r_1 \\) and  \\( f(r_2)=r_2 \\) |  (i) \\( r_1=r_2=\alpha_1 \implies p(x) = (x-\alpha_1)^2 \\) <br><br> (ii) \\( r_1=r_2=\alpha_2 \implies p(x) = (x-\alpha_2)^2 \\) <br><br> (iii) \\( r_1=\alpha_1 \\)  and  \\(r_2=\alpha_2\\) \\(\;\implies p(x) = x^2-x-4 \\)  |
| \\( f(r_1)=r_2 \\) and \\( f(r_2)=r_1 \\) with \\( r_1\neq r_2 \\)  | \\( r_1^2 - 4 = r_2 \;\;\;(1) \\) <br> \\(  r_2^2-4 = r_1 \;\;\;(2) \\) <br><br> Subtracting (2) from (1) we get: <br> \\( r_1^2 - r_2^2 = r_2 - r_1  \\) <br> \\( r_1+r_2 = -1 \\) <br> \\( r_2 = -r_1-1 \\) <br> \\( r_1^2-4 = -r_1-1 \\) <br> \\( r_2^2-4=-r_2-1 \\) <br> <br> (iv) The previous two equations imply that \\(r_1\\) and \\(r_2\\) are the roots of the quadratic \\(p(x)=x^2+x-3\\) |
| \\( f(r_1)=r_1 \\) and \\( f(r_2)=r_1 \\) |  \\( r_1^2 - 4 = r_1 \;\;\;(1) \\) <br> \\(  r_2^2-4 = r_1 \;\;\;(2) \\) <br><br> Equating LHS of (1) and (2) we get: <br> \\( r_1^2 = r_2^2 \\) <br> So either \\( r_1=r_2 \\) (Case 1) or \\(r_1=-r_2\\). <br> (v) \\(r_1 = \alpha_1\\) and \\(r_2=-\alpha_1 \\)  implies \\( p(x) =  x^2-\alpha_1^2 \\)  <br> (vi) \\(r_1 = \alpha_2\\) and \\(r_2=-\alpha_2 \\)  implies \\( p(x) =  x^2-\alpha_2^2 \\)  |
| \\( f(r_1)=r_2 \\) and \\( f(r_2)=r_2 \\) | Same as Case 3.  |

-->

<p style="text-align:center;">
<img src="/assets/images/B5_1_cmi_exam_2020.png">
<img src="/assets/images/B5_2_cmi_exam_2020.png">
</p>




</details>

---

<p>
(ii) Consider the same property for cubic polynomials. Describe the process of finding them, but do not try to find the exact polynomials.
</p>


<details><summary>Solution</summary>

<p>
The procedure is similar to the one followed in part (i). Let the function \(f\) and \(\alpha\)s be as defined in the previous problem.
Let \(g(x)\) be a cubic polynomial with \(r_1,r_2\) and \(r_3\) as its roots.
</p>


<p>
The constraint on the problem means that:<br>

\begin{align}
f(r_1) &= r_1 \mbox{ or } r_2 \mbox{ or } r_3 \\
f(r_2) &= r_1 \mbox{ or } r_2 \mbox{ or } r_3 \\
f(r_3) &= r_1 \mbox{ or } r_2 \mbox{ or } r_3
\end{align}
</p>

<p>
We can find the candidate polynomials by enumerating all \(3^3=27\) cases.
</p>


<div style="margin-top:10px; margin-bottom: 10px; padding: 10px; border: 1px solid #cce ; border-radius: 4px;">

<h3>An example of the procedure</h3>
<p>Consider the following case:

\begin{align}
f(r_1) &= r_1 \\
f(r_2) &= r_2 \\
f(r_3) &= r_3
\end{align}

We get the following cubic polynomials as candidates for this case:

\begin{align}
&(x-\alpha_1)^3 \\
&(x-\alpha_2)^3\\
&(x-\alpha_1)^2(x-\alpha_2)\\
&(x-\alpha_1)(x-\alpha_2)^2
\end{align}
</p>

</div>





</details>

---

<p>
6. (i) Find the total number of anti-symmetric relations \(R\) from \(S \times S\) where \(S=\{1,2,3\cdots n\}.\)
An anti-symmetric relation is defined as: \((a,b)\in R\implies (b,a)\notin R.\)
</p>

<details><summary>Solution</summary>
<p>
From the definition it follows that \( (a,a) \notin R \). For any unordered pair \( \{a,b\} \) there are three possibilities:
<ul>
<li>\( (a,b) \in R \)</li>
<li>\( (b,a) \in R \)</li>
<li>\( (a,b) \notin R \)</li>
</ul>

The number of unordered pairs is \( \binom{n}{2} \). So there are \( 3^{ \binom{n}{2} } \) anti-symmetric relations.

</p>

</details>


<i>
Please <a href="/docs/disqus">leave a comment</a> if you know the description of B6 (ii) or (iii).
</i>



---

#### Acknowledgment

Thanks to AoPS-ers <b>X</b> for doing <b>y</b>!

| X | y |
|--|--|
Bhutu, Rwitabrata, Aniruddha, Himanshya, Randommathlover | Sharing the problems |
CMI_Student | Solving many problems and writing them up. |
Eduline | For spotting a mistake in problem B5 and confirming it with CMI. |


<i>Spreading the word about CMI Tomato on Facebook/WhatsApp/etc. would be greatly appreciated.</i>


---




<div id="palette1">
<h2>Browse previous years' problems</h2>

<br>

  <div class="palette">
      <div class="palette-keys">



<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#an-easy-problem';" onmouseover = "display('A1_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#parity-of-a-polynomial';" onmouseover = "display('A2_2010')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#vanilla-application-of-lhospital';" onmouseover = "display('A3_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#progression-of-squares';" onmouseover = "display('A4_2010')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#fermats-little-theorem';" onmouseover = "display('A5_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#easy-induction';" onmouseover = "display('A6_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#symmetric-log-reciprocals';" onmouseover = "display('A7_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#pigeon-hole-principle';" onmouseover = "display('A8_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#repeated-roots';" onmouseover = "display('A9_2010')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#trignometric-triangle-inequality';" onmouseover = "display('A10_2010')"></button>
<button class="button numbers" onclick="location.href='/docs/geometry/number_theory/irrationality/#rationality-preserving-operations';" onmouseover = "display('A11_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#rhombus-within-a-triangle';" onmouseover = "display('A12_2010')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#power-of-a-complex-number';" onmouseover = "display('A13_2010')"></button>
<button class="button white"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#pigeon-hole-principle';" onmouseover = "display('B1_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#midpoint-of-a-median';" onmouseover = "display('B2_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#just-count';" onmouseover = "display('B3_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#rational-triangle';" onmouseover = "display('B4_2010')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#a-perplexing-integral';" onmouseover = "display('B5_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#intersecting-circles';" onmouseover = "display('B6_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#line-passing-through-an-ap';" onmouseover = "display('B7_2010')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#letter-arrangement';" onmouseover = "display('A1_2011')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#a-chord-within-a-rectangle';" onmouseover = "display('A2_2011')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#intersection-of-a-line-and-periodic-function-ii';" onmouseover = "display('A3_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#am-gm-inequality';" onmouseover = "display('A4_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#differentiable-piece-function';" onmouseover = "display('A5_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#roots-of-a-quadratic';" onmouseover = "display('A6_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#01-polynomial';" onmouseover = "display('A7_2011')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#handshake-party';" onmouseover = "display('B1_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#largest-coefficient';" onmouseover = "display('B2_2011')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#six-consecutive-numbers';" onmouseover = "display('B3_2011')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#serendipitous-sum';" onmouseover = "display('B4_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#degree-constraint-on-the-polynomial';" onmouseover = "display('B5_2011')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#impossible-solid';" onmouseover = "display('B6_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#volume-of-a-cave';" onmouseover = "display('B7_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#only-one-real-root';" onmouseover = "display('B8_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-ii';" onmouseover = "display('B9_2011')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#two-variables-one-equation';" onmouseover = "display('B10_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#surjective-if-and-only-if-injective';" onmouseover = "display('B11_2011')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#an-old-russian-problem';" onmouseover = "display('B12_2011')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#intersection-of-a-line-and-periodic-function-i';" onmouseover = "display('A1_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-i';" onmouseover = "display('A2_2012')"></button>
<button class="button numbers" onclick="location.href='/docs/geometry/number_theory/irrationality/#irrational-fraction';" onmouseover = "display('A3_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#lhospital-again';" onmouseover = "display('A4_2012')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#tinkus-chocolate';" onmouseover = "display('A5_2012')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-a-rational-polynomial-with-a-given-a-root';" onmouseover = "display('B1_2012')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#midpoints-of-a-quadrilateral';" onmouseover = "display('B2_2012')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#intersection-family';" onmouseover = "display('B3_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#riemann-sum';" onmouseover = "display('B4_2012')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#trigonometric-values-via-complex-numbers';" onmouseover = "display('B5_2012')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#matching-pairs-of-points';" onmouseover = "display('B6_2012')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#pigeon-hole-on-pairs';" onmouseover = "display('B7_2012')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomial-that-gives-only-prime-powers';" onmouseover = "display('B8_2012')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#function-composition';" onmouseover = "display('B9_2012')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#one-to-one-i';" onmouseover = "display('A1_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#continuity';" onmouseover = "display('A2_2013')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#circumcenter-and-orthocenter';" onmouseover = "display('A3_2013')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#sum-of-squares-polynomial';" onmouseover = "display('A4_2013')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#seating-boys-and-girls';" onmouseover = "display('A5_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#vanilla-integrals';" onmouseover = "display('A6_2013')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#complex-triangle';" onmouseover = "display('A7_2013')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#sampling-a-quadratic';" onmouseover = "display('A8_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-iii';" onmouseover = "display('A9_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#asymptotes-of-a-function';" onmouseover = "display('A10_2013')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#isoceles-triangle';" onmouseover = "display('B1_2013')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#find-a-curve-given-the-tangent';" onmouseover = "display('B2_2013')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#prime-factorization-and-perfect-squares-again';" onmouseover = "display('B3_2013')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomials-that-exponentiate';" onmouseover = "display('B4_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#span-of-the-a-function';" onmouseover = "display('B5_2013')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#difference-equations-iii';" onmouseover = "display('B6_2013')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button numbers" onclick="location.href='/docs/geometry/number_theory/irrationality/#summations';" onmouseover = "display('A1_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#convergence-of-etextquadratic';" onmouseover = "display('A2_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#differentiability-i';" onmouseover = "display('A3_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#tangent-to-a-cubic';" onmouseover = "display('A4_2014')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#vertex-in-a-polygon';" onmouseover = "display('A5_2014')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#prime-factorization-and-divisibility';" onmouseover = "display('A6_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#application-of-rolle's-theorem';" onmouseover = "display('A7_2014')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-the-remainders';" onmouseover = "display('A8_2014')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#maximum-and-minimum-of-an-average';" onmouseover = "display('A9_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#triangle-construction';" onmouseover = "display('A10_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#cyclic-polygon';" onmouseover = "display('A11_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#longest-diagonal-in-a-box';" onmouseover = "display('A12_2014')"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#mix-a-sin-and-a-circle';" onmouseover = "display('B1_2014')"></button>
<button class="button numbers" onclick="location.href='/docs/geometry/number_theory/irrationality/#a-polynomial-integer';" onmouseover = "display('B2_2014')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-number-of-functions';" onmouseover = "display('B3_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#differentiability-challenge';" onmouseover = "display('B4_2014')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#difference-equations';" onmouseover = "display('B5_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#quadrilateral-with-circles';" onmouseover = "display('B6_2014')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#charity';" onmouseover = "display('A1_2015')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#ordered-binary-strings';" onmouseover = "display('A2_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#magic-number';" onmouseover = "display('A3_2015')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#double-derivatives';" onmouseover = "display('A4_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomial-with-positive-coefficients';" onmouseover = "display('A5_2015')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#circles-with-pythagoras';" onmouseover = "display('A6_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#coefficient-ratio';" onmouseover = "display('A7_2015')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#number-plates';" onmouseover = "display('A8_2015')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#a-saw-tooth-function';" onmouseover = "display('A9_2015')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#roots-of-unity-i';" onmouseover = "display('A10_2015')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#conditional-probability';" onmouseover = "display('A11_2015')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#polynomial-and-limits';" onmouseover = "display('B1_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#points-on-a-sphere';" onmouseover = "display('B2_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#when-is-a2-a-divisible-by-10000';" onmouseover = "display('B3_2015')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#slowing-slope-changing-function';" onmouseover = "display('B4_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#euclidean-algorithm';" onmouseover = "display('B5_2015')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#straight-edge-with-circle';" onmouseover = "display('B6_2015')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#logical-puzzle';" onmouseover = "display('A1_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#gdp-vs-per-capita-gdp';" onmouseover = "display('A2_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#totient-function';" onmouseover = "display('A3_2016')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-steps';" onmouseover = "display('A4_2016')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#use-of-telescoping';" onmouseover = "display('A5_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#irrationality-and-continuity';" onmouseover = "display('A6_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#gcd-application';" onmouseover = "display('A7_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#integer-valued-polynomials';" onmouseover = "display('A8_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#continuity-on-tangents-and-secants';" onmouseover = "display('A9_2016')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#triangle-with-segments';" onmouseover = "display('A10_2016')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button probability" onclick="location.href='/docs/probability/#test-preparation';" onmouseover = "display('B1_2016')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#circle-touching-a-parabola';" onmouseover = "display('B2_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#definite-integral';" onmouseover = "display('B3_2016')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#pairwise-sums-of-a-set';" onmouseover = "display('B4_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#given-the-remainders-find-the-polynomials';" onmouseover = "display('B5_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#primes-in-an-algebraic-equation-';" onmouseover = "display('B6_2016')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#circle-inside-a-triangle-inside-a-circle';" onmouseover = "display('A1_2017')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#distribute-oranges-in-boxes';" onmouseover = "display('A2_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#sweep-volume';" onmouseover = "display('A3_2017')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#sample-a-divisor';" onmouseover = "display('A4_2017')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#roots-of-a-quartic-polynomial';" onmouseover = "display('A5_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#inflection-point';" onmouseover = "display('A6_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#absolute-integrals';" onmouseover = "display('A7_2017')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solutions-to-simultaneous-equations';" onmouseover = "display('A8_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#smallest-prime-factor-function';" onmouseover = "display('A9_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#continuity-of-two-functions';" onmouseover = "display('A10_2017')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#roots-of-unity-to-rescue';" onmouseover = "display('B1_2017')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#intersecting-planes';" onmouseover = "display('B2_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#strange-question';" onmouseover = "display('B3_2017')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#perfect-square-in-a-sequence';" onmouseover = "display('B4_2017')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#coloring-integers';" onmouseover = "display('B5_2017')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#square-inside-a-hexagon';" onmouseover = "display('B6_2017')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#progression-of-circles';" onmouseover = "display('A1_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#integers-in-a-function-range';" onmouseover = "display('A2_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solving-a-cubic-root-equation';" onmouseover = "display('A3_2018')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#a-routine-substitution';" onmouseover = "display('A4_2018')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#difference-of-squares';" onmouseover = "display('A5_2018')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#counting-roots-in-a-quadrant';" onmouseover = "display('A6_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-the-possible-coefficients-given-the-roots';" onmouseover = "display('A7_2018')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#non-congruent-triangles-with-fixed-perimeter';" onmouseover = "display('A8_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#recursive-polynomial';" onmouseover = "display('A9_2018')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#repeated-saw-tooth';" onmouseover = "display('A10_2018')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#smart-induction';" onmouseover = "display('B1_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solve-pxqx--1';" onmouseover = "display('B2_2018')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#function-on-integers';" onmouseover = "display('B3_2018')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#segments-inside-a-triangle';" onmouseover = "display('B4_2018')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#combinations-with-gaps';" onmouseover = "display('B5_2018')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#carrom-board-math';" onmouseover = "display('B6_2018')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#number-of-divisors';" onmouseover = "display('A1_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#a-simple-substitution';" onmouseover = "display('A2_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#maximize-area-of-a-rectangle';" onmouseover = "display('A3_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#sum-of-a-finite-series';" onmouseover = "display('A4_2019')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#squares-on-a-chessboard';" onmouseover = "display('A5_2019')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#is-a-square';" onmouseover = "display('A6_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#broken-calculator';" onmouseover = "display('A7_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#first-ascent';" onmouseover = "display('A8_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#limit-of-a-log-of-an-exponent';" onmouseover = "display('A9_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#continuity-based-on-integral-conditions';" onmouseover = "display('A10_2019')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-number-of-functions-ii';" onmouseover = "display('B1_2019')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#counting-the-roots-outside-a-disk';" onmouseover = "display('B2_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#routine-definite-integral-in-disguise';" onmouseover = "display('B3_2019')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#interior-point-in-a-parallelogram';" onmouseover = "display('B4_2019')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#geometric-interpretation-of-algebraic-expressions';" onmouseover = "display('B5_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#leibniz-rule';" onmouseover = "display('B6_2019')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>


      </div>
  </div>

<p>


    <div style="min-height:250px" id="thetext">

<i>Hover on the cell to see the problem. Click on it to navigate to the solution.</i><br>

<button class="button algebra"></button> Algebra <br>
<button class="button geometry"></button> Geometry <br>
<button class="button numbers"></button> Number theory <br>
<button class="button calculus"></button> Calculus<br>
<button class="button combinatorics"></button> Combinatorics <br>
<button class="button probability"></button> Probability <br>
<button class="button complex"></button> Complex numbers <br>
<button class="button trigonometry"></button> Trigonometry<br>

    </div>
</p>

</div>


<hr>





## CMI entrance exam cutoff

The cutoff has been around 35% for the objective section and 40-50% overall. The objective section is used for screening.<br>

CMI does not publish the cutoff marks but they have responded to individual requests in the past. The scores shown below were shared by former students who were privy to this data.
<br>

<!--
[Subhayan Saha](https://www.quora.com/profile/Subhayan-Saha)
-->

| Year | Objective | Overall | Vetted by
|---|--|--|
2016 | 14/40 | 62/124 | Sayantani Bhattacharya [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/Why-there-is-no-interview-for-cmi-bsc-this-year)
2017 | 15/40 | 60/125 | Abhiroop Sanyal
2018 | 15/40 | 50/125 | Sutirtha Datta [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/If-the-CMI-selection-is-not-on-marks-then-what-do-they-look-for-from-the-answer-script)




## Preparation tips and interview experiences (pre-2016)


<!--
http://services.artofproblemsolving.com/download.php?id=YXR0YWNobWVudHMvMS8yLzgwZWIwOGVmNzE5YjU1ZjRkMjE5MzI4NTgwMDRmNjZmNTVmYzdlLnBkZg==&rn=TXkgaW50ZXJ2aWV3IGV4cGVyaWVuY2UucGRm
-->

- _2015 Interview experience_ by Sanjay M who posted this on AoPS. [[pdf]](/assets/images/sanjay_interview.pdf)
- _Why I joined CMI_  by Vipul Naik who joined CMI despite getting JEE AIR-154. [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://vipulnaik.com/undergraduate-institution-selection/)
- _How to prepare for CMI_ by Sai Krishna who joined CMI in 2013. [[pdf]](https://www.cmi.ac.in/~saikrishnac/files/how-to-prepare-for-cmi.pdf)
- _CMI entrance exam preparation experience_  by Ankita Sarkar who joined CMI in 2015. [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/How-did-Ankita-Sarkar-prepare-for-CMI-Entrance-exam-What-books-did-she-use)


Starting from 2016, admissions are based only on the written test and there is no interview.

---

<img src="/assets/images/manjul_bhargava.png" style="float:left;margin-right:20px;width=50px"/>

<q>When universities in the United States are looking to recruit mathematics students
from India, one of the first places they look for applications is from CMI, if not the first place. Universities that are able to get CMI students are always very proud.</q>
{: .fs-4 .fw-300 }





Manjul Bhargava
{: .fs-4 .fw-300 }

[Source](https://www.youtube.com/watch?v=FsdZLme1fj0&t=2870s)
{: .fs-1 .fw-400  }

---


## Admission rate

Acceptance offers are sent to around 90 candidates and about half of them enroll. This is the reason why the number varies from year to year. Approximate numbers are given below.

| Year | # Test-takers | # Offers | # Students enrolled
|-----|----|--|
2015 | 4000 | 70 | 40
2016 | 5500 | 90 | 44
2017 | 6000 | 90 | 45
2018 | 8000 | 95 | 48
2019 | 10000 | 100 | 61

---


## All-in-one book
<br>

<img src="/assets/images/cmi_tomato_cover.jpg" style="float:left;margin-right:20px;margin-top:0px;border-radius:1%"/>

The content of this website is available as an e-book in PDF format. You will have a permanent copy of the solutions which may be handy just in case the site
goes down.
{: .fs-4 .fw-300 }


<a href="https://gum.co/kBekW">Buy the book on Gumroad</a>


<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>




<!--
https://promys-india.org/resources/reading-list/
-->

---



#### About the author

This website is maintained by  Balasundar M, a teacher who has more than 15 years of experience in the industry and academia. He enjoys solving
olympiad-type problems over coffee.
{: .fs-3 .fw-300 }

If you have a more elegant solution to any problem than the one presented, feel free to email him at <code>mbalasundar08</code> [at] <code>gmail.com.</code>
{: .fs-3 .fw-300 }

---

#### Legal information

The contents of this website are hosted in accordance with principles of [fair use](https://www.copyright.gov/fls/fl102.html).
You agree to email me about any possible infringement of copyright law before taking legal action.
{: .fs-3 .fw-300 }

<!--
M. Balasundar is a participant in the Amazon Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to amazon.in.
{: .fs-3 .fw-300 }
-->




