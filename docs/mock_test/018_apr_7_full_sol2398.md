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
a) Look at numbers of the form abcde with distinct digits from the set \(\{0,1,2,3,4,5\}\) such that \(a \neq 0\) and \(3 \mid(a+b+c+d+e)\).
Since \(3 \mid(1+\cdots+5)=15\), there are \(5 !=120\) such numbers with no digit zero.
If 0 is included, then 3 must be excluded. For \(a=1,2,4\) and \(5\), there are \(4!\) numbers each.   So \(120+96=216\), totally.<br>
<i>Source: A1, MMC 2015.</i>
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

<details open><summary>Sol.</summary>
<b>Ans.</b> (c) and (d).<br>

(a) is not true if \(a_i=1/i\) and \(b_i=0\).<br>

\[ 0 \leq (a_i-b_i)^2 = 2a_i^2 + 2b_i^2-(a_i+b_i)^2 \leq 2a_i^2 + 2b_i^2 \]

(c) and (d): Since \(\sum a_i^2 \) and \(\sum b_i^2\) are absolutely convergent, \(\sum 2a_i^2+2b_i^2 \)
is also convergent.
<br>
For sufficiently large \(i\), \(|a_i-b_i|<1\) so \( |a_i-b_i|^3 \leq |a_i-b_i|^2 \). Since \( (a_i-b_i)^3 \)
is absolutely convergent it is convergent.


<br><i>Why is (b) not true?</i>

<br><b>Proposition.</b> The sum \( \sum_{i=1}^\infty 1/n^p \) converges if \( p > 1\) and diverges when \( 0 \leq p \leq 1\).
<br><i>Proof.</i> See the following article for proofs of both assertions: Cohen and Knight, Convergence and divergence of \( \sum_{i=1}^\infty 1/n^p \) [<a href="https://www.jstor.org/stable/2690283">paper</a>].<br>

<a href="https://math.stackexchange.com/questions/29450/self-contained-proof-that-sum-limits-n-1-infty-frac1np-converges-for">Alternate proof</a> on stack exchange.


<br>

(b) is not true if we we pick \(a_i = 1/i^{0.6} \) and \(b_i=0\) and invoke the above proposition. 
</details>



<li>
<p>
Suppose \( S=\{1,2,3,4,5,6\} \).  Find the number of pairs \( (A,B) \)
that can be formed such that \(A \subseteq S\) and \(B\subset A\).
</p>
</li>

<details open><summary>Sol.</summary>
Consider the pairs where \(A \subseteq S\) and \(B\subseteq A\). Each element in \(S\) has three choices:<br>
(i) It can be in \(B\)<br>
(i) It can be in \(A\setminus B\)<br>
(iii) It can be in \(S\setminus A\)<br>
Hence, there are \(3^6\) such pairs. From this we subtract the number of pairs where \(B=A\). There are \( 2^6 \) of 
these. Hence, the required number is \( 3^6 - 2^6 = 665 \).<br>

<i>Source: Slight variation of an ISI Tomato problem.</i>
</details>



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
Ans: (a) and (d). \(p\) and \(q\) must be odd.<br>


\begin{align*}
1+a \frac{p}{q} + b \left(\frac{p}{q}\right)^{2}+3{\left(\frac{p}{q}\right)}^{3} &= 0 \\
q^3+a pq^2 +b p^2q+3p^3 &= 0 \\
q^3 \mod p  & \equiv 0 \\
3p^3 \mod q  & \equiv 0 \\
\implies  q|3 \text{ and } p=1 &
\end{align*}

Hence, \(p\) and \(q\) must be odd.<br>  


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
(d) We show that \( y = x\).  For a contradiction, assume that \(x < y\). Then \(\sqrt{x^2+2y} > x+1\) and hence the conditions tell us that \(\sqrt{x^2+2y}>x+\frac{5}{3}\) and \(\sqrt{y^2+2x}>y+\frac{2}{3}\). But this implies \(y>\frac{5}{3}x\) and \(x>\frac{2}{3}y\) which is a contradiction as \(\frac{5}{3} \cdot \frac{2}{3}>1\).<br>

<i>Due to symmetry of the problem, the alternative options were silly. Solution due to Tinturn from AoPS.</i>
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

<p style="text-align:center">
<img src="/assets/images/mt018_a7.jpg"/>
</p>

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

(c) Note that \(2^{2} \equiv 1(\bmod 3)\). Hence, \(2^{2 k} \equiv 1(\bmod 3)\).

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



<li>On the real line place an object at 1. After every flip of a fair coin, move the object to the right by 1 unit if the outcome is Head and to the left by 1 unit if the outcome is Tail.
Let \(n\) be a fixed positive integer. Game ends when the object reaches either 0 or \(n\). Let \( P(n) \) denote the
probability of the object reaching \(n\). Write down the value of \( P(3) \).
</li>

<details open><summary>Sol.</summary>
(a) Starting the game at 1 , the possible outcomes to reach 3 without reaching zero are HH, HTHH, HTHTHH and so on.
Hence the probability of reaching 3 without going to zero is given by a geometric series \(\frac{1}{2^{2}}+\frac{1}{2^{4}}+\frac{1}{2^{6}}+\cdots\) which adds up to \(\frac{1}{3}\). Hence \(P(3)=\frac{1}{3}\).<br>

<i>Source: C3, 2019. Madhava</i>
</details>



<li> If \(1, w_{1}, w_{2}, w_{3}, w_{4}, w_{5}\) are distinct roots of \(x^{6}-1\), then<br>
(a) \(1+w_{i}+w_{i}^{2}+w_{i}^{3}+w_{i}^{4}+w_{i}^{5}=0\) for \(i=1,2,3,4,5\). <br>
(b) \(1+w_{i}^{2}+w_{i}^{4}+w_{i}^{6}+w_{i}^{8}+w_{i}^{10}=0\) for \(i=1,2,3,4,5\). <br>
(c) \(1+w_{i}^{3}+w_{i}^{6}+w_{i}^{9}+w_{i}^{12}+w_{i}^{15}=0\) for \(i=1,2,3,4,5\). <br>
(d) \(1+w_{i}^{5}+w_{i}^{10}+w_{i}^{15}+w_{i}^{20}+w_{i}^{25}=0\) for \(i=1,2,3,4,5\).
</li>


<details open><summary>Sol.</summary>
Ans: (a) and (d).<br>

\(w_i\)s are the roots of the equation \[ (x^6-1) = (x-1)(1+x+x^2+x^3+x^4+x^5) \].

Notice that -1 is also a root. So (b) cannot be true for \(w_i = -1\).
For  \(i\), \(w_i^k = w_i^{k+6}\). We can infer the correct options by making this substitution.<br>

<i>Source: C5, 2021. MMC</i>
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

Note that the frog's coordinates before and after the jump are integers. For example, the frog can jump to \( (3,4) \) or \( (-3,4) \) or \( (5,0) \), etc. 
from the origin. Similarly, the frog can reach either the point \( (10,0) \) or \( (7,7) \) in two jumps.<br>

(a) True or False: The frog can reach any given point with integer coordinates in a finite number of jumps. [2 points]<br>

(b) What is the minimum number of jumps required to reach the point \( (180,180) \) [8 points]?<br>

For both the parts (a) and (b), explain your reasoning.

</p>


<details open><summary>Sol.</summary>
(a) True. The frog can move right or up by one unit by doing a sequence of moves. To move right the frog makes three jumps: \( (3,4),(3,-4) \) and \( (-5,0) \). To move up it does \( (4,3),(-4,3)\) and \( (0,-5)\).<br>

(b) <b>Claim 1.</b> The frog can reach the target in 52 jumps.<br>

<i>Proof.</i> Jump \( (3,4) \) and \( (4,3) \) 25 times each.  We will be at \( (7,7)\times 25 = (175,175) \). Then, do a \( (5,0) \) jump and  \( (0,5) \) jump. \( \;\;\; \square \)<br><br>



<b>Claim 2.</b> The frog cannot reach the target in less than 52 jumps.<br>
<i>Proof.</i> Let \( (x_i,y_i)\)  denote the position of the frog after \(i\) jumps. Consider the quantity \( z_i = x_i + y_i \).
If frog reaches the target in \(d\) steps, then \(z_d = 180+180 = 360\). The value of \(z_0=0\). The value of \(z_i\) can only 
increase by at most 7 more than \(z_{i-1}\). So an upper bound of \( z_{51} \) is \( 7 \times 51 = 357 < 360\). Hence, at least 52 steps are necessary to reach the target. \(\;\;\square\).

<br><i>Source: Slight variation of Problem A1, Putnam 2021.</i><br>

</details>

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
We prove the statement in the problem by induction on the largest prime dividing either \(a\) or \(b\).
For the base case, we can write \(1 / 1=2 ! / 2 !\). For a general \(a / b\), let \(p\) be the largest prime dividing either \(a\) or \(b\); then \(a / b=p^k a^{\prime} / b^{\prime}\)
for some \(k \neq 0\) and positive integers \(a^{\prime}, b^{\prime}\) whose largest prime factors are strictly less than \(p\). We now have \(a / b=(p!)^k \frac{a^{\prime}}{(p-1) !^k b^{\prime}}\),
and all prime factors of \(a^{\prime}\) and \((p-1)!^{k} b^{\prime}\) are strictly less than \(p\). By the induction assumption, \(\frac{a^{\prime}}{(p-1)!^k b^{\prime}}\) can be written
as a quotient of products of prime factorials, and so \(a / b=(p !)^k \frac{a^{\prime}}{(p-1) !^k b^{\prime}}\) can as well. This completes the induction.<br>

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
and that \(f\) is concave while \(g\) is convex.

Now let

\[ F(x)=\int_0^x(f(t)+g(t)-2 t) \mathrm{d} t=\int_0^x((f(t)-t)-(t-g(t))) \mathrm{d} t \]

be the left-hand side of the equation, and let

\[ A=\frac{(a-g(a))(f(a)-a)}{2} \]

The figure below shows the situation geometrically. We have \( F(0) = F(1) = 0 \) and \( A > 0 \)
and \( F(a) > A \). Hence, there is a solution to the equation \( F(x) = A\) on the interval \( (0,a) \)
and a solution on the interval \( (a,1) \).

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

<i>Solution due to <a href="/assets/images/mock_test_18/Heraclides_Ponticus/B4.jpg">Heraclides Ponticus</a>.</i><br>

We show that the series is divergent.

The term \( \lceil \sin n \rceil\) is 0 or 1 depending on whether \( \sin n \) is positive or negative.  Also, \( \sin x\)
changes the sign between integer multiples of \(\pi\).  Consider the interval \( \left[(n+1)\pi,n\pi\right] \). The interval has a width of \( (n+1) \pi-n \pi=\pi\). Since 
\( 3<\pi<4 \), there are exactly three natural numbers in this interval. Hence the given series is as follows:

\[ 
\frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{4}+\frac{1}{5}+\frac{1}{6}+\frac{1}{7^2}+\frac{1}{8^2}+\frac{1}{9^2}+\frac{1}{10}-\frac{1}{19}+\frac{1}{12}
\]

Collecting the terms with exponent 1 gives the following subseries.
\[
 \left\{\frac{1}{6}+\frac{1}{12}+\frac{1}{18} \cdots\right\} = \frac{1}{6} \sum_{k=1}^{\infty} \frac{1}{k} 
\]
But since this is a subseries of the original one in question (with all terms positive), the original series is also divergent.

<br><i>Source: Simon Marais '22.</i>

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


---

<p><b>B6</b>.   Let \(A_{1}=\{1\}, A_{n+1}=\left\{3 k, 3 k+1: k \in A_{n}\right\}\) for all \(n \geq 1\) and \(A=\bigcup_{n=1}^{\infty} A_{n}\).<br>
(i) What is the set \(A_3\)? [2 marks]<br>
(ii) Can 2017 be written as the sum of two elements of \(A\)? Explain your reasoning. [8 marks]<br>
</p>

<details open><summary>Sol.</summary>
Convert all the numbers to base-3 representation. \(A_1=\{1\}, A_2=\{10,11\} , A_3=\{100,110,101,111\}\).
The set \( A_{k} \) contains all the \(k\)-digit numbers having 0s and 1s in its base-3 representation. The
number \(2017\) can be expressed as \(2017_3 = 2202201 = 1101100 + 1101101\).
<br><i>Source: B1, 2017 Madhava.</i>
</details>





