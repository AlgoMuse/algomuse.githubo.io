---
layout: default
title: Mock test 2
nav_exclude: true
---


#  MT #2: Algebra

#### Timings: 17:00-20:00 Hrs &nbsp;&nbsp;  Date: 18 Feb 2021
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg.
{: .fs-3 }

**For this part, answers must be written without any explanation.**



<ol>

<p>
<li>Let \(p_1(x),p_2(x),\ldots,p_m(x)\) be \(m\) distinct polynomials such that:<br>

\[ p_1(x) = p_2(x) = \ldots = p_m(x) \mbox{ if } x<0 \]

What is the largest possible value of \(m\)?

For example, if it is possible for \(m\) to be 4, then the polynomials
might look like this:

<p style="text-align:center">
<br><img src="/assets/images/mt_2_polynomial.png"/>
</p>

</li>
</p>


<p>
<li>Find a polynomial \(q(x)\) with integer coefficients with \(\sqrt{3}+i\) as a root. In case there are multiple candidates,
pick a polynomial with the least degree.</li>
</p>


<p>
<li>
(i) Find the remainder when \(f(x)=6x^{16}+4x^{22}+5x^{12}+x^{2}\) is divided by \((x^{2}+1)\). [2 marks] <br><br>
(ii) Find the remainder when \(x f(x)\) is divided by \((x^{2}+1)\). [2 marks]
</li>
</p>


<p>
<li>
Find two quadratic polynomials \( p(x) \) and \( g(x) \)  that satisfy
the following conditions:

<ol>
<li>Both \(p(x)\)  and \(g(x)\)  have two distinct real roots.</li>
<li>The sum \( p(x)+g(x) \)  has no real root.</li>
</ol>

</li>
</p>


<p>
<li> A grazing field has \(10\) kgs of grass. Every Sunday a herd of cows eats \(x\) kgs of grass. Over a week's time the grass grows by \( 10\% \). What
is the maximum value of \(x\) that will allow the cows to feed indefinitely without running out of grass?
</li>
</p>




<p>
<li>
Consider the simultaneous equations in variables \(x\) and \(y\), where \(k\) is a constant:

\begin{align*}
2x + y &= kx + 4 \\
x + 2y &= ky + 6k
\end{align*}

For what values of \(k\) does the system not have a solution?


</li>
</p>



<p>
<li>
<i>Notation.</i> \( { }^nC_{k} \) represents the binomial coefficient.<br>

Consider the set of prime numbers less than 100 (listed below). Pick two numbers \(n\) and \(k\) with \(n > k \) from this set such that
\( {}^nC_{k} \) is maximized.

<p style="text-align:center">
<img src="/assets/images/primes_100.png"/>
</p>

</li>
</p>


<p>
<li>
We have numbers \( x_1,\ldots,x_{51} \) such that each \(x_i\) is either \(+1\) or \(-1\). What is the minimum value of following sum?

\[  \left\lvert  \sum_{ 1\leq i < j \leq 51 } x_ix_j  \right\rvert  \]

</li>
</p>


<i>Problem source: </i> PRMO 2019.<br>



<p>
<li>
<i>Notation.</i> \( [n] \) denotes the set of numbers \( \{1,2,\ldots,n\} \). Assume \(n>100\) for this problem.<br><br>
A function \(f:[n]\rightarrow \mathbb{R} \) is defined as follows:<br>


\[
f(x) = \begin{cases} 0 &\mbox{if } x = 1 \\
 1 & \mbox{if } x = n \\
 \frac{1}{2} (f(x-1) + f(x+1))  & \mbox{if } 1 < x < n
 \end{cases}
\]

What is the value of \( f(3) \) in terms of \(n\)?

</li>
</p>







<p>
<li>
Let \( f(x) = 37 x^{4}-37 x^{3}-x^{2}+9 x-2 \). Let the four roots of
\( f(x) \)  be \( r_{1}, r_{2}, r_{3}\)  and \( r_{4} \). Find the value of

\[ \left(r_{1}+r_{2}+r_{3}\right)\left(r_{1}+r_{2}+r_{4}\right)\left(r_{1}+r_{3}+r_{4}\right)\left(r_{2}+r_{3}+r_{4}\right) \]

</li>
<i>Problem source: </i> Stanford Math Tournament.<br>
</p>


<p>


</p>





</ol>


<!--

https://www.madhavacompetition.in/MMC-Jan-2019.pdf
1. Let $f(x)=a_{0} x^{n}+\cdots+a_{n}$ be a non-constant polynomial with real coefficients satisfying
$$
f(x) f\left(2 x^{2}\right)=f\left(2 x^{3}+x\right)
$$
for all real numbers $x$.
(a) Show that $a_{n} \neq 0$.
(b) Show that $f$ has no real root.






8. $P(x)$ and $Q(x)$ are two polynomials such that
$$
P(P(x))=P(x)^{16}+x^{48}+Q(x)
$$
Find the smallest possible degree of $Q$.
Answer: 35
Solution: Note: we use the notation $O\left(x^{n}\right)$ to denote an arbitrary polynomial whose degree is at most $n$.

We first try to find a $Q$ with degree $<48 .$ It turns out this is feasible. Let $d$ be the degree of
P. $P(P(x))$ has degree $d^{2}$, and $P(x)^{16}+x^{48}+Q(x)$ has degree $\max (16 d, 48)$. Since 48 is not a perfect square, the degree must be $16 d$, which implies $d=16$.
$$
\begin{array}{l}
\text { Now let } R(x)=P(x)-x^{16}, \text { so } \\
\qquad R(P(x))=x^{48}+Q(x)
\end{array}
$$
Since $R$ applied to a degree- 16 polynomial yields a degree- 48 polynomial, the degree of $R$ must be $3 .$ So, we have $P(x)=x^{16}+a x^{3}+O\left(x^{2}\right)$ for some $a \neq 0 ;$ we can also show from here that in fact $a=1$. Therefore,
$$
P(P(x))=P(x)^{16}+P(x)^{3}+O\left(P(x)^{2}\right)=P(x)^{16}+x^{48}+3 x^{35}+O\left(x^{34}\right)
$$
Hence, if the degree of $Q$ is $<48,$ it must be exactly 35.






https://sumo.stanford.edu/pdfs/smt2019/algebra-exam.pdf
5. Let $f(x)=36 x^{4}-36 x^{3}-x^{2}+9 x-2 .$ Then let the four roots of $f(x)$ be $r_{1}, r_{2}, r_{3},$ and $r_{4}$ Find the value of
$$
\left(r_{1}+r_{2}+r_{3}\right)\left(r_{1}+r_{2}+r_{4}\right)\left(r_{1}+r_{3}+r_{4}\right)\left(r_{2}+r_{3}+r_{4}\right)
$$
Answer: $\frac{1}{6}$ Solution 1: Note that $s=r_{1}+r_{2}+r_{3}+r_{4}=\frac{36}{36}=1$. Then
$$
\begin{aligned}
\left(r_{1}+r_{2}+r_{3}\right)\left(r_{1}+r_{2}+r_{4}\right)\left(r_{1}+r_{3}+r_{4}\right)\left(r_{2}+r_{3}+r_{4}\right) &=\left(s-r_{4}\right)\left(s-r_{3}\right)\left(s-r_{2}\right)\left(s-r_{1}\right) \\
&=\frac{f(s)}{36} \\
&=\frac{36-36-1+9-2}{36} \\
&=\frac{1}{6}
\end{aligned}
$$



-->





## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


<p>
<b>B1.</b> Prove the following inequality for \( a, b>0 \):
\[ \large \sqrt[2021]{a b^{2020}} \leq  \frac{ a+2020b }{2021}  \]
</p>

<i>Problem source: </i> Problem solving strategies. Prob. 4, Inequalities.<br>


<p>
<b>B2.</b> Consider the polynomial \(f(x) = a_{n}x^n +a_{n-1}x^{n-1} + \cdots + a_{1}x+a_{0}\),
where each coefficient \(a_{i}\) is either \(0\) or \(1\). If \( f(2) = 14\),
find the polynomial \(f(x)\).
</p>





<p>
<b>B3.</b> Compute the smallest value \(p\) such that, for all \(q> p\), the polynomial  \( x^3 - 7x^2 +qx +16 = 0 \) has exactly one real root.
</p>

<i>Problem source: </i> Stanford Math Tournament.<br>

<p>
<b>B4.</b> Let \(f(x)=a_{0} x^{n}+\cdots+a_{n}\) be a non-constant polynomial with real coefficients satisfying

\[ f(x) f\left(x^{2}\right)=f\left(x^{3}+x\right) \]

for all real numbers \(x\).

Show that \(f\)  has no real root.
</p>



<p>
<b>B5.</b> Show that \(p(x)\) does not have any real roots where:
\[  p(x)=x^{2 n}-2 x^{2 n-1}+3 x^{2 n-2}-4 x^{2 n-3}+\cdots-2 n x+(2 n+1) \]

<br><i>Problem source: </i> Problem solving strategies. Prob. 5, Polynomials.<br>
</p>


<p><b>B6.</b> (i) Simplify \[ \sum_{j=0}^{n} \sum_{i=j}^{n}{ }^{n} C_{i}{ }^{i} C_{j}  \] <br><br>
(ii) Calculate the value of the expression (i) when \( n=5 \).
</p>

<i>Problem sources for B4 and B6: </i> Madhava Mathematics Competition 2019.<br>

<!--

Madhava 2011
Solution :

If $x \leq 0$ then $p(x)>0 .$ Let $x>0$ $p(x)=x^{2 n}-2 x^{2 n-1}+3 x^{2 n-2}-4 x^{2 n-3}+\cdots-2 n x+(2 n+1)$
$x p(x)=x^{2 n+1}-2 x^{2 n}+3 x^{2 n-1}-4 x^{2 n-2}+\cdots-2 n x^{2}+(2 n+1) x$
$$
6
$$
$x p(x)+p(x)=x^{2 n+1}-x^{2 n}+x^{2 n-1}-x^{2 n-2}+\cdots+x+(2 n+1)$
$(1+x) p(x)=x\left(\frac{1+x^{2 n+1}}{1+x}\right)+(2 n+1)$
$\Rightarrow p(x)>0$ for $x>0 .$



-->





