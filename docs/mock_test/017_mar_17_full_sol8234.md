---
layout: default
title: Mock test 1 Full-syllabus test
nav_exclude: true
---


#  Mock test #1 '23: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 17 March 2023
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg or PartA.png.
{: .fs-3 }

**For this part, answers must be written without any explanation.**

<ol>



<li><p> For how many integers a with \(1 \leq a \leq 100, a^{a}\) is a square?<br>
(a) 50 <br> (b) 51 <br> (c) 55 <br> (d) 56
</p>
</li>

<details open><summary>Sol.</summary>
(c) <i>Case 1</i>: all even integers, then \((2 k)^{2 k}=\left[(2 k)^{k}\right]^{2}\).
There are 50 even integers between 1 and 100.<br>
<i>Case 2:</i> \(a\) is an odd number which is a square <i>i.e.</i> \(1,9,25,49,81\).  
</details>

<li><p> Let \(A\) be a non-empty subset of real numbers and \(f: A \rightarrow A\) be a function such that \(f(f(x))=x\) for all \(x \in A\). Then \(f(x)\) is

(a) a bijection<br>

(b) one-one but not onto<br>

(c) onto but not one-one<br>

(d) neither one-one nor onto<br>

</p>
</li>

<details open><summary>Sol.</summary>
(a) If \(f(x)=f(y)\), then \(f(f(x))=f(f(y))\) implies \(x=y\).
Therefore, \(f\) is a one-one function.
By definition, \(f\) is onto. Hence \(f\) is a bijection.
</details>


<li><p> If \(a+b+c=0\), then the quadratic equation \(3 a x^{2}+2 b x+c=0\) has<br>
(a) at least one root in \((0,1)\) <br>
(b) one root in \((1,2)\) and the other in \((-1,0)\) <br>
(c) both imaginary roots <br>
(d) a repeated root<br>
</p>
</li>


<details open><summary>Sol.</summary>
(a)
\begin{align*}
\mbox{Let }   f’ (x) &= 3ax^2 + 2bx + c \\
    f (x) &= ax^3 + bx + cx + d\\
f (0)  &= d\\
f (1)  &= a + b + c + d \\
\end{align*}

Since we are given that \(a + b + c = 0\), \(f (1) = d\) and \(f(0) = f (1)\).
Rolle’s theorem can be applied in the interval \((0, 1)\). \(f'(c) = 0\) for some \(0 < c < 1\).
There will be at least one root of the equation \(3ax^2 + 2bx + c = 0\) in the interval \((0, 1)\).
</details>

<li><p> The system of equations

\begin{gathered}
2 x+p y+6 z=8 \\
x+2 y+q z=5 \\
x+y+3 z=4
\end{gathered}

has no solution for<br>
(a) \(p \neq 2, q \neq 3\) <br>
(b) \(p \neq 2, q=3\) <br>
(c) \(p=2, q=3\) <br>
(d) \(p=2, q \neq 3\)
</p>
</li>


<details open><summary>Sol.</summary>
(b) 

\[ \left[ \begin{array}{lll} 2 & p & 6 \\ 1 & 2 & 1 \\ 1 & 1 & 3  \end{array} \right] \left[ \begin{array}{l} x\\ y\\ z \end{array}\right] = \left[ \begin{array}{l} 8 \\ 5\\ 4 \end{array} \right] \]

The determinant of the \(3\times 3\) matrix is \((p-2)(q-3)\). If no solution exists, then either \(p=2\) or \(q=3\).

<ul>
<li>Case 1. \(p=2\) The first and the last equations are the same. A solution always exists.</li>
<li>Case 2. \(q=3\) We have seen that \(p\neq 2\). The solution does not exist for the option (b). The difference of first two and the last two equations give a different value of \(y\).</li>
</ul>

</details>



<li><p> A relation \(R\) is defined on the set of positive integers as \(x R y\) if \(2 x+y \leq 5\). The relation \(R\) is<br>
a) reflexive<br>
b) symmetric<br>
c) transitive<br>
d) None of these<br>
</p>
</li>

<details open><summary>Sol.</summary>

(d) \((2,2) \notin R\), so relation \(R\) is not reflexive.

Since \((1,3) \in R\) but \((3,1) \notin R\), so relation \(R\) is not symmetric.

Since \((2,1) \in R\) and \((1,3) \in R\) but \((2,3) \notin R\), so relation \(R\) is not transitive.

</details>



<li><p>
An ant starts at the point \((0,0)\). It can travel along the integer lattice, only moving in the positive \(x\) and \(y\) directions. In how many ways it can reach \((4,4)\)
without passing through \((2,2)\)?
</p>
</li>

<details open><summary>Sol.</summary>
In total, the ant must travel 8 units, meaning there are \(\left(\begin{array}{l}8 \\ 4\end{array}\right)\) ways for it to reach \((5,5)\), ignoring the missing point. Likewise, there are \(\left(\begin{array}{l}4 \\ 2\end{array}\right)\) ways to reach the missing point, and \(\left(\begin{array}{l}4 \\ 2\end{array}\right)\) ways to travel from the missing point to the end. Thus, there are \(\left(\begin{array}{l}8 \\ 4\end{array}\right)-\left(\begin{array}{l}4 \\ 2\end{array}\right)\left(\begin{array}{l}4 \\ 2\end{array}\right)=34\) ways.
</details>


<li><p>
In the circle given below, the diameter \( \overline{EB} \) is parallel to \(\overline{DC}\) and \( \overline{AB} \) is parallel to \( \overline{ED} \).
 Also, \(\angle AEB\) and \(\angle ABE\) are in the ratio of 4:5.  Which of the following statements are true?<br>

<p style="text-align:center">
<img src="/assets/images/mt17_cyclic_quad.png"/>
</p>

(a) \(\angle ABE + \angle BCD = 180^\circ \) <br>
(b) \( \angle BCD = 120^\circ \) <br>
(c) \( \angle BCD = 130^\circ \) <br>
(d) \( \angle ABE = 40^\circ \) <br>

</p></li>


<details open><summary>Sol.</summary>
Ans: (a) and (c). <br>
Since \(EB\) is the diameter, \(\angle EAB = 90^\circ\).  We are given that \(\angle AEB: \angle ABE::4:5\), so \(\angle AEB=40^\circ\) and \( \angle ABE=50^\circ\).
\( \angle ABE = \angle BED \) since they are alternate angles. \(EBCD\) is a cyclic quadrilateral, so the opposite angles add to \(180^\circ\). This means 
\( \angle BED + \angle BCD = 180^\circ \).

<!-- Source: AMC 10B 2011 -->
</details>


<li><p> Suppose \(a\) and \(b\) are real numbers such that:
\[ \lim_{x \rightarrow 0} \frac{\sin ^2 x}{e^{a x}-b x-1}=\frac{1}{2} \]
What are the possible values for the ordered pair \( (a, b) \)?<br>
(a) (2,2)<br>
(b) (2,-2)<br>
(c) (-2,2)<br>
(d) (-2,-2)<br>
</p>
</li>

<details open><summary>Sol.</summary>
Ans: (a) and (d).<br>
Since this is in an indeterminate form, we can use L'Hôpital's Rule to obtain
\[ \lim_{x \rightarrow 0} \frac{\sin 2 x}{a e^{a x}-b}=\frac{1}{2} \]
However, the numerator goes to zero, so the denominator must also go to zero to give us another indeterminate form. This implies that \(a=b\). Using L'Hôpital's Rule again, we have that
\[ \lim_{x \rightarrow 0} \frac{2 \cos 2 x}{a^2 e^{a x}}=\frac{1}{2} \]
The numerator goes to 2 , so the denominator must go to 4 . Therefore, \(a=b= \pm 2\), giving us \((a, b)=(2,2)\) and \((-2,-2)\).

<!-- Source: SMT 2013 -->
</details>


<li><p>Let \(\operatorname{Im}(z)\) denote the imaginary part of the complex number \(z\). What is the value
of the expression \( \operatorname{Im}\left(\sum_{n=0}^{\infty} \frac{e^{i n x}}{n !}\right) \)?<br>

(a) \(e^{\cos x} \sin \sin x\)  <br>
(b) \(e^{\sin x} \sin \cos x\) <br>
(c) \(e^{\cos x} \cos \sin x\) <br>
(d) \(e^{\sin x} \cos \cos x\) 

</p>
</li>

<details open><summary>Sol.</summary>
(a) \[ \operatorname{Im}\left(e^{e^{i x}}\right)=\operatorname{Im}\left(e^{\cos x+i \sin x}\right)=e^{\cos x} \cdot \operatorname{Im}\left(e^{i \sin x}\right)=e^{\cos x} \sin \sin x \]

</details>

<li><p>Which of the following inequalities are true for any natural number \(n>4\)?<br>
(a) \( \sqrt{n} \leq \sqrt[n]{n !} \)<br>
(b) \( \sqrt[n]{n !} \leq \frac{n+1}{2}\)<br>
(c) \( \sqrt{n} \geq \sqrt[n]{n !} \)<br>
(d) \( \sqrt[n]{n !} \geq \frac{n+1}{2}\)<br>
</p>
</li>

<details open><summary>Sol.</summary>
(a) and (b).
</details>



</ol>



## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---



<p><b>B1.</b>
A pair of prime numbers that differ by 2 are called <i>twin primes</i>. Examples of twin primes are \( \{3,5\} \), \( \{11,13\} \), etc.<br>

(a) Prove that every twin prime pair other than \( \{3,5\} \) must be of the form \( \{6k-1,6k+1\} \) where \(k\) is a positive integer. [2 marks]<br>
(b) Prove that for any prime number \( p \geq 7\), the numbers \( p-2, p, p+2 \) cannot be in an arithmetic progression of primes. [2 marks]<br>
(c) Find the number of primes \(p\) such that \(p, p+10, p+14\) are all prime numbers. [6 marks]<br>
</p>


<details open><summary>Sol.</summary>
(a) Every odd number must be of the form \(6k+1,6k+3\) or \(6k+5\). Since \( 3 \mid 6k+3 \), primes larger than 3 can only be of the form \(6k+1\) or \(6k-1\).<br>
(b) From (a), we know that the first two primes are of the form \(\{6k-1,6k+1\}\), this implies that the third prime must be \(6k+3\) (a contradiction).<br>
(c) If \(p=3\), we note that \(3,13,17\) are all prime. Thus \(p=3\) is a solution. Any other prime is either of the type \(3 k+1\) or \(3 k+2\). If \(p=3 k+1\) for some integer \(k \geq 0\), then \(p+14=3(k+5)\) is not a prime. If \(p=3 k+2\) for some integer \(k \geq 0\), then \(p+10=3(k+4)\) is not a prime. Thus \(p=3\) is the only solution.
</details>



---

<p><b>B2.</b> Consider the \(n\)th degree polynomial \( p(x)=n\left(x^n+1\right)-2\left(x^{n-1}+\cdots+x\right) \). If \(n>1\), how
many negative coefficients does \(p(x)^2\) have? Express your answer in terms of \(n\) and explain your reasoning.
</p>

<details open><summary>Sol.</summary>
(a) We show that \(p(x)\) has \(2 n-2\) negative coefficients. 
\[
\begin{aligned}
p(x)^2= & n^2\left(x^{2 n}+x^n+1\right)-2 n\left(x^n+1\right)\left(x^{n-1}+\cdots+x\right) \\
& +\left(x^{n-1}+\cdots+x\right)^2
\end{aligned}
\]
For \(i \in\{1, \ldots, n-1, n+1, \ldots, n-1\}\), the coefficient of \(x^i\) in \(p(x)^2\) is at most \(-2 n\) (coming from the cross term) plus \(-2 n+2\) (from expanding \(\left(x^{n-1}+\cdots+x\right)^2\)), and hence negative.
</details>


---

<p><b>B3.</b> Let \( f\) be a function defined on natural numbers as follows. \( f(1) = 1 \) and for every \(n>1\), \(f\) is given by:

\[ f(n) = f(n-\lfloor \sqrt{n} \rfloor) + n \]


In the above relation \( \lfloor x \rfloor \) denotes the greatest integer less than or equal to \(x\). From the above equation we can derive the first few values of \( f\):


\[
\begin{aligned}
f(1) &= 1\\
f(2) &= f(2-\lfloor \sqrt{2} \rfloor ) + 2 = f(1) + 2 = 3\\
f(3) &= f(3-\lfloor \sqrt{3} \rfloor ) + 3 = f(2) + 3 = 6
\end{aligned}
\]

(a) Find the values of \( f(4) \) and \( f(5) \). [2 marks]<br>
(b) Prove that there exists a positive number \(n_0\) such that \(f(n) \leq 3n\sqrt{n} \) for every \(n > n_0\). [8 marks]<br>

</p>


<details open><summary>Sol.</summary>
(a) \(f(4) = f(2) + 4 = 7\) and \(f(5) = 11\).<br>
(b) See Anaximander's <a href="/assets/images/mock_test_17/Anaximander/B3.jpg">solution</a>.
</details>



---

<p><b>B4.</b> Ramesh and Kiran are two friends who practice piano every day at school. Ramesh goes to the piano room every day at a random time
between 1 PM and 8 PM. He practices for three hours. Kiran goes to the piano room every day at a random time between 5 PM and 11 PM and practices for one hour. 
The block of time practice need not be contained in the given time interval for the arrival. For example, Ramesh could arrive at 7 PM and practice till 10 PM. <br>

(i) What is the probability that Ramesh and Kiran meet on a given day? &nbsp; [7 marks]<br>
(ii) What is the probability that Ramesh and Kiran meet on at least two days in a given span of 5 days? &nbsp; [3 marks]<br>


</p>


<details open><summary>Sol.</summary>
(i) Let \(x\) (resp. \(y\)) be the time Ramesh (resp. Kiran) enters the music room. If \(y > x\), they only meet if \( y-x \leq 3\). Similarly, if \(x < y\),
they meet only if \( x-y \leq 1 \). We know that \( x \in [1,8] \) and \(y \in [5,11]\). The portion of interest is shown
in the figure below (note that the intersection of axes is (1,5) in the picture). The space of all outcomes corresponds
to the area of the rectangle which is \( 6\times 7 = 42 \) sq. units. The favorable outcomes corresponds to the area of the shaded region.


<p style="text-align:center">
<img src="/assets/images/mt017_b4.jpg"/>
</p>

The probability that Ramesh and Kiran meet is:<br>

\begin{align*}
\mbox{Fraction of the shaded regions} = \frac{1}{2} ( 6\cdot 6 - 2\cdot 2) = \frac{16}{42}  = \frac{8}{21}
\end{align*}


(ii) Let \(p\) denote the probablity of meeting on a given day. The probability that they never meet is
\( (1-p)^5 \). The probability that they meet on exactly one day is \(5p(1-p)^4\). Substituting the value of
\(p\) from (i), we see that the probability that they meet on less than two days is \(0.37\). Hence, the required
probablity is \(\approx 0.63\).


</details>

---
<p><b>B5.</b> In the figure given below, \(ABC\) is an equilateral triangle. The line drawn from vertex \(A\) meets
\(BC\) at \(D\) and the circumcircle at \(P\). Prove that<br>

(i) \(PA = PB + PC\)<br>

(ii) \(\frac{1}{PD} = \frac{1}{PB} + \frac{1}{PC}\)<br>

<p style="text-align:center">
<img src="/assets/images/mt17_cquad.png"/>
</p>



</p>

<details open><summary>Sol.</summary>
 \(A B P C\) is cyclic. By Ptolemy's theorem,
\[
A B \cdot P C+A C \cdot P B=A P \cdot B C .
\]
But \(A B=B C=C A\) (equilateral triangle). So
\[
P A=P B+P C \qquad (1)
\]

Now divide (1) by \(P B \cdot P C\). We get \[\frac{1}{P C}+\frac{1}{P B}=\frac{P A}{P B \cdot P C}\].

Now it is enough to prove that \[\frac{P A}{P B \cdot P C}=\frac{1}{P D}\]

which is the same as

\[
\frac{P A}{P B}=\frac{P C}{P D} \qquad (2)
\]

Consider \(\triangle A B P\) and \(\triangle C D P\)

\[
\begin{aligned}
& \angle B A P=\angle D C P \\
& \angle A P B=\angle A C B=60^{\circ} \\
& \angle A P C=\angle A B C=60^{\circ} 
\end{aligned}
\]



Hence \(\angle A P B=\angle A P C=\angle D P C\) and so \(\triangle A B P\) is similar to \(\triangle C D P\). So,
\[
\frac{P A}{P C}=\frac{P B}{P D} \text { or } \frac{P A}{P B}=\frac{P C}{P D} .
\]
Hence (2) is proved.<br>

<i>Source: Non-routine problems in mathematics. V.K. Krishnan. AMTI.</i>

</details>



---



<p><b>B6.</b> Consider the function \( f(r) \):<br>

\[ f(r)=\int_0^{\pi / 2} x^r \sin x d x \]

Prove that:<br>

(i) \( f(r) < \frac{(\pi / 2)^{r+1}}{r+1} \qquad \)    [2 marks]<br>
(ii) \( f(r) > \frac{(\pi / 2)^{r+1}}{r+2} \qquad  \)  [5 marks]<br>
(iii) \( \int_0^{\pi / 2} x^r \cos x d x=\frac{f(r+1)}{r+1} \qquad \) [3 marks] <br>


</p>



<details open><summary>Sol.</summary>
(i) Since \( \sin x \) is less than 1 in the interval \( x \in (0,\pi/2) \),
\[ f(r)<\int_0^{\pi / 2} x^r d x=\frac{(\pi / 2)^{r+1}}{r+1} \]
(ii) <b>Lemma.</b> For \(x \in (0,\pi/2)\) we have \( \sin x \geq 2 x / \pi\).<br>

<i>Proof.</i> Let \( g(x) := \sin x/x \). We will show that \( g(x) \) is a decreasing function by proving that 
\( g^\prime (x) < 0 \). 

\begin{align*}
\sin x &> x \mbox{ in } x \in (0,\pi/2)\\
\implies \sin x &> x \cos x \mbox{ in } x \in (0,\pi/2)\\
g^\prime(x) &= \frac{x \cos x - \sin x}{x^2} < 0 \;\;\;\;\; \square \\
\end{align*}




\[ f(r)>\int_0^{\pi / 2} \frac{2 x^{r+1}}{\pi} d x=\frac{(\pi / 2)^{r+1}}{r+2} \]
(iii) \( \int_0^{\pi / 2} x^r \cos x d x=\frac{1}{r+1} \int_0^{\pi / 2} x^{r+1} \sin x d x=\frac{f(r+1)}{r+1} \)
</details>











