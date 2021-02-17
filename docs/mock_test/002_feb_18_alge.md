---
layout: default
title: Mock test 2
nav_exclude: true
---


#  MT #2: Algebra
#### Timings: 17:00-20:00 Hrs &nbsp;&nbsp;  Date: 18 Feb 2021
{: .fs-3 .text-grey-004 }

---

### Instructions

- You are responsible for keeping time. Email all your solutions by 20:00 Hrs IST.
- Write your answers with a dark pen on white paper.
- Find an email from me with the subject line 'Mock test #2 Algebra'. Send your solutions (images) as replies to this email.
- Make sure that the handwriting is clear and no image is blurred.
- Adjust/Reduce the resolution of the camera so that each image is less than 500 KB in size.
- Total marks: 100 (10x4=40 for Part A + 6x10=60 for Part B)
{: .bg-grey-lt-000 .p-6 }


**For students who miss the live test (members only)**<br>
Self-administer the mock test and email your solutions before 19 Feb, 23:59 Hrs. Your solutions will be evaluated
but marks won't counted for official use in the future. Solutions submitted after 19 Feb, 23:59 Hrs will not be evaluated.
{: .bg-grey-lt-000 .p-6 }


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

For example, if it possible for \(m\) to be 4, then the polynomials
might look like this:

<br><img src="/assets/images/mt_2_polynomial.png"/>

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
<li>
<i>Notation.</i> \( { }^nC_{k} \) represents the binomial coefficient.<br>
(i) Simplify \[ \sum_{j=0}^{n} \sum_{i=j}^{n}{ }^{n} C_{i}{ }^{i} C_{j}  \] <br><br>
(ii) Calculate the value of the expression (i) when \( n=5 \). [1 mark]
</li>
</p>


<p>
<li>
Let \( f(x) = 37 x^{4}-37 x^{3}-x^{2}+9 x-2 \). Then let the four roots of
\( f(x) \)  be \( r_{1}, r_{2}, r_{3}\)  and \( r_{4} \). Find the value of

\[ \left(r_{1}+r_{2}+r_{3}\right)\left(r_{1}+r_{2}+r_{4}\right)\left(r_{1}+r_{3}+r_{4}\right)\left(r_{2}+r_{3}+r_{4}\right) \]

</li>
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
<b>B1.</b> Consider the polynomial \(f(x) = a_{n}x^n +a_{n-1}x^n + \cdots + a_{1}x+a_{0}\),
where each coefficient \(a_{i}\) is either \(0\) or \(1\). If \( f(2) = 14\),
find the polynomial \(f(x)\).
</p>





<p>
<b>B2.</b> Compute the smallest value \(p\) such that, for all \(q> p\), the polynomial  \( x^3 - 7x^2 +qx +16 = 0 \) has exactly one real root.
</p>


<p>
<b>B3.</b> Let \(f(x)=a_{0} x^{n}+\cdots+a_{n}\) be a non-constant polynomial with real coefficients satisfying

\[ f(x) f\left(x^{2}\right)=f\left(x^{3}+x\right) \]

for all real numbers \(x\).

Show that \(f\)  has no real root.
</p>

<p>
<b>B4.</b> Show that \(p(x)\) does not have any real roots where:
\[  p(x)=x^{2 n}-2 x^{2 n-1}+3 x^{2 n-2}-4 x^{2 n-3}+\cdots-2 n x+(2 n+1) \]

</p>


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




<!--

https://sumo.stanford.edu/pdfs/smt2011/algebra-solutions.pdf




10. How many polynomials $P$ of degree 4 satisfy $P\left(x^{2}\right)=P(x) P(-x) ?$
Answer: 10 Note that if $r$ is a root of $P$ then $r^{2}$ is also a root. Therefore $r, r^{2}, r^{2^{2}}, r^{2^{3}}, \cdots,$ are all roots of $P .$ Since $P$ has a finite number of roots, two of these roots should be equal. Therefore, either $r=0$ or $r^{N}=1$ for some $N>0$.
If all roots are equal to 0 or $1,$ then $P$ is of the form $a x^{b}(x-1)^{(4-b)}$ for $b=0, \ldots, 4$ Now suppose this is not the case. For such a polynomial, let $q$ denote the largest integer such that $r=e^{2 \pi i \cdot p / q}$ is a root for some integer $p$ coprime to $q$. We claim that the only suitable $q>1$ are $q=3$ and $q=5$ First note that if $r$ is a root then one of $\sqrt{r}$ or $-\sqrt{r}$ is also a root. So if $q$ is even, then one of $e^{2 \pi i \cdot p / 2 q}$ or $e^{2 \pi i \cdot p+q / 2 q}$ should also be root of $p,$ and both $p / q$ and $(p+q) / 2 q$ are irreducible fractions. This contradicts the assumption that $q$ is maximal. Therefore $q$ must be odd. Now, if $q>6,$ then $r^{-2}, r^{-1}, r, r^{2}, r^{4}$ should be all distinct, so $q \leq 6$. Therefore $q=5$ or 3

If $q=5,$ then the value of $p$ is not important as $P$ has the complex fifth roots of unity as its roots, so $P=a\left(x^{4}+x^{3}+x^{2}+x+1\right)$. If $q=3$, then $P$ is divisible by $x^{2}+x+1$. In this case we let $P(x)=a\left(x^{2}+x+1\right) Q(x)$ and repeating the same reasoning we can show that $Q(x)=x^{2}+x+1$ or $Q(x)$ is of form $x^{b}(x-1)^{2-b}$. Finally, we can show that exactly one member of all 10 resulting families of polynomials fits the desired criteria. Let $P(x)=a(x-r)(x-s)(x-t)(x-u) .$ Then, $P(x) P(-x)=a^{2}\left(x^{2}-r^{2}\right)\left(x^{2}-s^{2}\right)\left(x^{2}-\right.$
$\left.t^{2}\right)\left(x^{2}-u^{2}\right) .$ We now claim that $r^{2}, s^{2}, t^{2},$ and $u^{2}$ equal $r, s, t,$ and $u$ in some order. We can prove this noting that the mapping $f(x)=x^{2}$ maps 0 and 1 to themselves and maps the third and fifth roots of unity to another distinct third or fifth root of unity, respectively. Hence, for these polynomials, $P(x) P(-x)=a^{2}\left(x^{2}-r\right)\left(x^{2}-s\right)\left(x^{2}-t\right)\left(x^{2}-u\right)=a P\left(x^{2}\right),$ so there exist exactly 10 polynomials that fit the desired criteria, namely the ones from the above 10 families with $a=1$.



---


7. Let $P(x)$ be a polynomial of degree 2011 such that $P(1)=0, P(2)=1, P(4)=2, \ldots,$ and $P\left(2^{2011}\right)=$
2011. Compute the coefficient of the $x^{1}$ term in $P(x)$. Answer: $2-\frac{1}{2^{2010}}$
We analyze $Q(x)=P(2 x)-P(x) .$ One can observe that $Q(x)-1$ has the powers of 2 starting from $1,2,4, \cdots,$ up to $2^{2010}$ as roots. Since $Q$ has degree $2011, Q(x)-1=A(x-1)(x-2) \cdots\left(x-2^{2010}\right)$ for some $A$. Meanwhile $Q(0)=P(0)-P(0)=0,$ so
$$
Q(0)-1=-1=A(-1)(-2) \cdots\left(-2^{2010}\right)=-2^{(2010 \cdot 2011) / 2} A
$$
Therefore $A=2^{-(1005 \cdot 2011)}$. Finally, note that the coefficient of $x$ is same for $P$ and $Q-1,$ so it equals $A\left(-2^{0}\right)\left(-2^{1}\right) \cdots\left(-2^{2010}\right)\left(\left(-2^{0}\right)+\left(-2^{-1}\right)+\cdots+\left(-2^{-2010}\right)\right)=\frac{A \cdot 2^{1005 \cdot 2011}\left(2^{2011}-1\right)}{2^{2010}}=2-\frac{1}{2^{2010}}$



Suppose P(x) is a polynomial of degree d that has d real roots \( \alpha_1, \ldots, \alpha_d \).  Find a polynomial of degree (d-1) that has:
d-1 real roots \(\beta_1,\ldots,\beta_d\) such that.


http://cs-www.cs.yale.edu/homes/spielman/TALKS/Gibbs16.pdf








-->




