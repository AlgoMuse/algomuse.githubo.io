---
layout: default
title: Mock test 2 Full-syllabus test
nav_exclude: true
---


#  Mock test #2 '23: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 7 April 2023
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg or PartA.png.
{: .fs-3 }

**For this part, answers must be written without any explanation.**

<ol>

<li>How many five digit positive integers that are divisible by 3 can be formed using the digits \(0,1,2,3,4\) and 5, without any of the digits getting repeated?<br>
a) 216 <br>
b) 96 <br>
c) 120 <br>
d) 625 <br>
</li>

<details open><summary>Sol.</summary>
a) Numbers of the form abcde with distinct digits from the set \(\{0,1,2,3,4,5\}\) such that \(a \neq 0\) and \(3 \mid(a+b+c+d+e)\). Since \(3 \mid(1+\cdots+5)=15\), there are \(5 !=120\) such numbers with no digit zero. If 0 is included, then 3 must be excluded; so for \(a=1,4\) ! numbers like 10245 ; for \(a=2,4\) ! numbers like 20145 ; for \(a=4,4\) ! numbers like 40245 ; for \(a=5,4 !\) numbers like 50124 . So \(120+96=216\), totally.<br>
<i> A1, MMC 2015.</i>
</details>



<li>
Suppose \(a_i\) and \(b_i\) are real numbers such that \(\sum_1^\infty a_i^2\) and \(\sum_1^\infty b_i^2\) converge. Which of these statements is true?

<ol>
<li>The sequence \(\sum_1^\infty |a_i-b_i| \) converges. </li>
<li>The sequence \(\sum_1^\infty |a_i-b_i|^{3/2} \) converges. </li>
<li>The sequence \(\sum_1^\infty (a_i-b_i)^2 \) converges. </li>
<li>The sequence \(\sum_1^\infty (a_i-b_i)^3 \) converges. </li>
</ol>
</li>


<li>
<p>
Suppose \( S=\{1,2,3,4,5,6\} \).  Find the number of pairs \( (A,B) \)
that can be formed such that \(A \subseteq S\) and \(B\subset A\).
</p>
</li>


<li> Let \( f(x)=1+ax+bx^{2}+3x^{3}\) be a polynomial where \(a\) and \(b\) are integers. Suppose \(f(x)\) has a
rational root \(\frac{p}{q}\), where \(\text{gcd}(p,q)=1\). Which of the following statements are true?<br>

<ol>
<li>\(p\) must be even. </li>
<li> \(q\) must be even. </li>
<li> \(p\) must be odd. </li>
<li> \(q\) must be odd. </li>
</ol>

</li>

<details open><summary>Sol.</summary>
\(p\) and \(q\) must be odd. MT6. The previous two questions are also from MT6.
</details>



<li> Positive integers \(x, y\) satisfy the following conditions:

\[ \{\sqrt{x^2 + 2y}\}> \frac{2}{3}; \hspace{10mm} \{\sqrt{y^2 + 2x}\}> \frac{2}{3} \]

where \( \{x\}\) denotes the fractional part of \(x\). For example, \( \{2.34\} = 0.34\).


Which of the following is/are true?<br>

<ol>
<li> Either \(y = x + 1\) or \( x = y + 1\). </li>
<li> \(y > x\). </li>
<li> \(y = \lfloor 2x/3 \rfloor \). </li>
<li> \(y = x \). </li>
</ol>

</li>


<details open><summary>Sol.</summary>

Solution due to Tinturn from AoPS.</i> We show that \( y = x\).
Otherwise, wlog \(x < y\). Then \(\sqrt{x^2+2y}>x+1\) and hence the conditions tell us that \(\sqrt{x^2+2y}>x+\frac{5}{3}\) and \(\sqrt{y^2+2x}>y+\frac{2}{3}\).
But this implies \(y>\frac{5}{3}x\) and \(x>\frac{2}{3}y\) which is a contradiction as \(\frac{5}{3} \cdot \frac{2}{3}>1\).

</details>





<li>Which of the following equations has the greatest number of real solutions?<br>

<ol>
<li>\(x^{3}=10-x\)</li>
<li>\(x^{2}+5 x-7=x+8\)</li>
<li>\(7 x+5=1-3 x\)</li>
<li>\(e^{x}=x\)</li>
</ol>

</li>

<details open><summary>Sol.</summary>

Answer: (b)<br>

(a) Has one real root and two complex roots.<br>
(b) Has two real roots.<br>
(c) This is a linear equation, so it has one real root.<br>
(d) Since \( e^{x} > x \), there are no real roots.<br>

</details>

<li>In how many regions is the plane divided when the following equations are graphed, not considering the axes? 

\[ y=x^{2} \]
\[ y=2^{x} \]

<ol>
<li>3</li>
<li>4</li>
<li>5</li>
<li>6</li>
</ol>

</li>

<details open><summary>Sol.</summary>
(d) We plot the graphs of the two functions \(y=x^{2}\) and \(y=2^{x}\) and observe that it has six regions.
</details>


<li>
A positive integer \(n\) is such that \( \left(n 2^{n}-1\right) \) is divisible by 3. 
Which form does \(n\) take (for a positive integer \(k\))?<br>

(a) \(6k+2\) or \(6k+4\)<br>
(b) \(6k+3\) or \(6k+5\)<br>
(c) \(6k+4\) or \(6k+5\)<br>
(d) \(6k+1\) or \(6k+4\)<br>

</li>

<details open><summary>Sol.</summary>

Note that \(2^{2} \equiv 1(\bmod 3)\). Hence, \(2^{2 k} \equiv 1(\bmod 3)\).

Thus if \(n\) is even then \(2^{n} \equiv 1(\bmod 3)\) and if \(n\) is odd then \(2^{n} \equiv 2(\bmod 3)\).

\[
    2^n \equiv  
    \begin{cases}
        1 (\bmod 3) \;\; &\mbox{if } n \mbox{ is even} \\
        2 (\bmod 3) \;\; &\mbox{if } n \mbox{ is odd}
    \end{cases}
\]

\[
    n2^n-1 \equiv  
    \begin{cases}
        n-1 (\bmod 3) \;\; &\mbox{if } n \mbox{ is even} \\
        2n-1 (\bmod 3) \;\; &\mbox{if } n \mbox{ is odd}
    \end{cases}
\]

 We are given that \(3 \mid\left(n 2^{n}-1\right)\).  Hence, \((n-1) \equiv 0(\bmod 3)\) if \(n\) is even and \(3 \mid(-n-1)\) if \(n\) is odd. Hence, \(n=6 k+4\)  or \(n=6 k+5\).  
</details>




</ol>



## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---


<p><b>B1.</b> A frog is intially at the origin of a co-ordinate plane. It wants to reach a destination point by making a sequence of jumps.
The frog can jump from point \( (x_1,y_1) \) to  point
\((x_2,y_2)\) if the points are exactly 5 units apart in distance or, in other words, if they satisfy:

\[ \sqrt{ (x_1-x_2)^2 + (y_1-y_2)^2 } = 5 \]

Note the the frog's coordinates before and after the jump are integers. For example, the frog can jump to \( (3,4) \) or \( (-3,4) \) or \( (5,0) \), etc. 
from the origin. Similarly, the frog can reach either the point \( (10,0) \) or \( (7,7) \) in two jumps.<br>

(a) True or False: The frog can reach any given point with integer coordinates in a finite number of jumps. [2 points]<br>

(b) What is the minimum number of jumps required to reach the point \( (180,180) \) [8 points]?<br>

For both the parts (a) and (b), explain your reasoning.

</p>


---

<p><b>B2</b>.  Prove that every positive rational number can be written in the form \( a/b \) such that both \(a\)
and \(b\) are products of factorials of primes. For example,
\[
\frac{10}{9} = \frac{2!\cdot 5!}{3!\cdot 3! \cdot 3!}.
\]

Note that the primes appearing in \(a\) or \(b\) need not be distinct.

</p>


<details open><summary>Sol.</summary>
Every positive rational number can be uniquely written in lowest terms as \(a / b\) for \(a, b\) positive integers.
We prove the statement in the problem by induction on the largest prime dividing either \(a\) or \(b\) (where this is considered to be 1 if \(a=b=1\) ).
For the base case, we can write \(1 / 1=2 ! / 2 !\). For a general \(a / b\), let \(p\) be the largest prime dividing either \(a\) or \(b\); then \(a / b=p^k a^{\prime} / b^{\prime}\) for some \(k \neq 0\) and positive integers \(a^{\prime}, b^{\prime}\) whose largest prime factors are strictly less than \(p\). We now have \(a / b=(p !)^k \frac{a^{\prime}}{(p-1) !^k b^{\prime}}\), and all prime factors of \(a^{\prime}\) and \((p-1) !^{k k} b^{\prime}\) are strictly less than \(p\). By the induction assumption, \(\frac{a^{\prime}}{(p-1) ! k^{\prime} b^{\prime}}\) can be written as a quotient of products of prime factorials, and so \(a / b=(p !)^k \frac{a^{\prime}}{(p-1) !^k b^{\prime}}\) can as well. This completes the induction.
<i>Source: 2009 Putnam.</i>
</details>


---




<p><b>B3.</b> Consider the following two functions defined on the interval \( [0,1] \):

\[ f(x)=\sin \left(\frac{\pi \sin \frac{\pi x}{2}}{2}\right) \]

and

\[ g(x)=\frac{2}{\pi} \arcsin \left(\frac{2}{\pi} \arcsin x\right) \]

(i) Show that the graphs of \( f(x) \) and \(g(x)\) are symmetric about the line \(y=x\). [3 marks]<br>

(ii) Let \(0 < a < 1\) be a fixed number. Show that there are at least two values of \(x\) in the interval \( (0,1) \) such that:

\[ \int_0^x(f(t)+g(t)-2 t) = \frac{(a-g(a))(f(a)-a)}{2}  \]


[7 marks]
</p>


<details open><summary>Sol.</summary>

Observe that the functions

\[ f(x)=\sin \left(\frac{\pi \sin \frac{\pi x}{2}}{2}\right) \]

and

\[ g(x)=\frac{2}{\pi} \arcsin \left(\frac{2}{\pi} \arcsin x\right) \]

are inverse to each other on the interval \([0,1]\) and hence their graphs are symmetric about the line \(y=x\).

Also, notice that \(f(0)=g(0)=0, f(1)=g(1)=1\), both \(f\) and \(g\) are increasing,
and that \(f\) is concave downward while \(g\) is concave upward.

Now let

\[ F(x)=\int_0^x(f(t)+g(t)-2 t) \mathrm{d} t=\int_0^x((f(t)-t)-(t-g(t))) \mathrm{d} t \]

be the left-hand side of the equation, and let

\[ A=\frac{(a-g(a))(f(a)-a)}{2} \]


<p style="text-align:center">
<img src="/assets/images/mt018_simon22.png"/>
</p>

<i>Source: Simon Marais '22.</i>

</details>




---

<p><b>B4</b>.  Determine whether the series
\[ \sum_{n=1}^{\infty} \frac{1}{n^{1+[\sin n\rceil}} \]

is convergent or divergent.
Here \(\lceil x\rceil\) denotes the least integer greater than or equal to \(x\).

</p>


<details open><summary>Sol.</summary>

We show that the series is divergent.
For all \(n \geq 1\) the integer \(\lceil(2 n-1) \pi\rceil\) is the smallest integer greater than \((2 n-1) \pi\). It therefore belongs to the interval \((2 n-1) \pi, 2 n \pi)\), because this interval necessarily contains an integer since it has length \(\pi>1\). It follows that \(\sin (\lceil(2 n-1) \pi\rceil)<0\) for all \(n \geq 1\), because \(\sin\) is negative on this interval.

Consider the subsequence \(n_k=\lceil(2 k-1) \pi\rceil \quad(k \geq 1)\) of the sequence \(1,2,3, \ldots\). Then we have \(1+\left\lceil\sin n_k\right\rceil=1+0=1\) for all \(k \geq 1\). Furthermore,

\[ n_k=\lceil(2 k-1) \pi\rceil<(2 k-1) \pi+(2 k-1)=(2 k-1)(\pi+1)<2 k(\pi+1) \]

Hence, \(\frac{1}{n_k}>\frac{1}{2(\pi+1)} \cdot \frac{1}{k}\), and since \(\sum_{k=1}^{\infty} \frac{1}{2(\pi+1)} \cdot \frac{1}{k}\) is divergent, we have that

\[ \sum_{k=1}^{\infty} \frac{1}{n_k}=\sum_{k=1}^{\infty} \frac{1}{n_k^{1+\left\lceil\sin n_k\right\rceil}} \]

is divergent. But since this is a subseries of the original one in question (with all terms positive), the original series is also divergent.


</details>



---


<p><b>B5</b>. Point \(T\) is chosen in the plane of a rhombus \(ABCD\) so that \(\angle ATC + \angle BTD = 180^\circ\), and circumcircles of triangles \(ATC\) and \(BTD\) are tangent to each other. <br>

(i) Suppose \( O_1 \) and \( O_2 \) are the circumcenters of \(\triangle ATC\) and \(\triangle BTD\), respectively. Prove that
quadrilaterals \( ABO_1O_2 \) and \( DCO_2O_1\) are cyclic. [5 marks]<br>
(ii) Show that \(T\) is equidistant from diagonals of \(ABCD\). [5 marks]<br>
</p>


<details open><summary>Sol.</summary>
Let \(O_1\) and \(O_2\) denote the circumcenter of \(\triangle ATC\) and \(BTD\) respectively. Since \(ABCD\) is rhombus we clearly have \(O_1 \in BD\) and \(O_2 \in AC\). Moreover, points \(O_1, O_2, T\) are collinear as \(\odot(ATC)\) and \(\odot(BTD)\) are tangent at point \(T\). 

Observe the following: 
\[ \angle BO_2D = 360^{\circ}-2 \angle BTD = 2\angle ATC =\angle AO_1C\] 
This implies that \(\angle O_1AC = \angle O_2BD= \angle O_1CA = \angle O_2DB\), hence quadrilaterals \(ABO_1O_2\) and \(DCO_1O_2\) are cyclic. In particular this gives us \(\angle BAO_2 = \angle BO_1T = \alpha\) and \(\angle ABO_1 = \angle O_1O_2C = \beta\). 


<p style="text-align:center">
<img src="/assets/images/mt18_b5.png"/>
</p>


Let \(X\) and \(Y\) be projections of point \(T\) on the lines \(AC\) and \(BD\) respectively and \(M\) intersection of \(AC\) and \(BD\). Observe that: 
\[ \frac{TY}{TX} = \frac{TO_1 \sin \alpha}{TO_2 \sin \beta} =\frac{AO_1 \sin \alpha}{BO_2 \sin \beta} = \frac{AM \sin \alpha}{MB \sin \beta} =1  \]
So \(TX=TY\) as needed.


<i>Proposed by Fedir Yudin.</i>
<i>https://artofproblemsolving.com/community/c6h3046178p27437928</i>

</details>









