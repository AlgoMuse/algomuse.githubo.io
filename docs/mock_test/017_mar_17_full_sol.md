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

<li>
<p>Let \(I \subseteq R\) be an interval and \(f : I \rightarrow \mathbb{R}\) be a differentiable function. Let
 \[J =  \Bigg\{ \dfrac{f(b) - f(a)}{b-a} : a, b \in I, a< b \Bigg\} \]

Which of the following are true?<br>

(a) \(J\) is an interval.<br>
(b) \(J \subseteq f'(I)\) <br>
(c) \(f'(I) - J\) contains at most two elements.<br>
(d) \(f'(I) - J\) can contain infinite number of elements.
</p>
</li>

<details open><summary>Sol.</summary>
Ans: (a)(b) and (c).<br>
(a) \(\forall a, b f'(c)=[f(b)-f(a)]/(b-a)\) for all \(c\) in \((a,b)\). Since \(f\) is differentiable. So we basically get from this \(f(b)-f(a)/(b-a)\) covers all \(f'(x)\) except endpoints as we vary \(a,b\). By taking \(a,b\) very close to each other. So this is \(f'(I)\) except the \(f'\) of endpoints. So by definition of \(f'(I)\), \(J\) is an interval. <br>
(b) Follows from mean value theorem.<br>
(c) \(f'\) on \(I\) satisfies the Intermediate value property so \( f'(I) \) is an interval.
Then since \(J\) subset \( f'(I) \) and both are intervals noting that \(f'(a)\) is a limit of elements of \(J\) we get that \( J\) is dense in
\( f'(I) \) which implies that the intervals must have same inf and sup.
</details>




<li><p> The number of subsets of the set \(\{1,2, \cdots, 10\}\) containing at least one odd integer is<br>
(a) \(2^{10}\)<br>
(b) \(2^{5}\)<br>
(c) \({ }^{10} C_{5}\) <br>
(d) \(2^{10}-2^{5}\)
</p></li>

<details open><summary>Sol.</summary>
Ans: (d)
Total number of subsets of the set \(\{1,2, \cdots, 10\}\) is \(2^{10}\). The number of subsets of the set \(\{1,2, \cdots, 10\}\) containing only even integers is \(2^{5}\). Thus the required number is \(2^{10}-2^{5}\).
</details>

<li><p>
The number of negative solutions of the equation \(e^{x}-\sin x=0\) is<br>
(a) 1 <br>
(b) 2 <br>
(c) 0 <br>
(d) infinite.
</p></li>

<details open><summary>Sol.</summary>
Solution : (d)
Graphs of \(e^{x}\) and \(\sin x\) intersect infinitely many times for negative real numbers.
</details>


<li><p> The last two digits of \(17^{400}\) are<br>
(a) 17 <br>
(b) 09 <br>
(c) 01 <br>
(d) 89
</p></li>

<details open><summary>Sol.</summary>
Solution : (c)<br>
By Euler's theorem \(17^{40} \equiv 1(\bmod 100)\). Therefore \(17^{400} \equiv 1(\bmod 100)\).
</details>

<li><p>
Let \(a_{1}=1, a_{n+1}=\left(\frac{1+n}{n}\right) a_{n}\) for \(n \geq 1\). Then the sequence \(\left\{a_{n}\right\}\) is<br>
(a) divergent<br>
(b) decreasing<br>
(c) convergent<br>
(d) bounded.
</p></li>

<details open><summary>Sol.</summary>
Ans: (a)<br>
Note that \(a_{n}=n\) for every \(n\). Hence, \(< a_{n} >\) is an unbounded sequence. Hence, divergent.
</details>


<li><p>
Let \(f: \mathbb{R} \rightarrow \mathbb{R}\) be a differentiable function such that
\[ f(x+h)-f(x)=h f^{\prime}\left(x+\frac{1}{2} h\right) \]
for all real \(x\) and \(h\). <br>

Which of the following is/are true?<br>

(a) \(f\) is a polynomial of degree at most 1.<br>
(b) \(f\) is a polynomial of degree at most 2.<br>
(c) \(f\) is a polynomial of degree at most 3.<br>
(d) \(f\) need not be a polynomial.
</p></li>

<details open><summary>Sol.</summary>
Ans: (b).<br>
</details>


<li><p>
Let \(S=\{a, b, c\}, T=\{1,2\}\). If \(m\) denotes the number of one-one functions and \(n\) denotes the number of onto functions from \(S\) to \(T\), then the values of \(m\) and \(n\) respectively are<br>
(a) 6,0<br>
(b) 0,6<br>
(c) 5,6<br>
(d) 0,8<br>
</p></li>

<details open><summary>Sol.</summary>
Ans: (b).<br>
There can not be a one-one function from \(S\) to \(T\) because the number of elements in \(S\) is bigger than the number of elements in \(T\). The total number of functions from \(S\) to \(T\) is \(2^{3}\). Since the constant function from \(S\) to \(T\) is not onto, the number of onto functions is \(2^{3}-2=6\).
</details>


<li><p>

Let \(f: \mathbb{R} \rightarrow \mathbb{R}\) and \(g: \mathbb{R} \rightarrow \mathbb{R}\) be differentiable functions such that \(f^{\prime}(x)>g^{\prime}(x)\) for every \(x\). Then the graphs \(y=f(x)\) and \(y=g(x)\)<br>
(a) intersect exactly once.<br>
(b) intersect at most once.<br>
(c) do not intersect.<br>
(d) could intersect more than once.<br>

</p></li>

<details open><summary>Sol.</summary>
Ans: (b).<br>
Let \(h(x)=f(x)-g(x)\). Then \(h^{\prime}(x)=f^{\prime}(x)-g^{\prime}(x)>0\). Therefore \(h\) is strictly increasing. If the graph of \(h\) intersects \(X\)-axis, then \(f(x)=g(x)\) at exactly one point. It is possible that the graphs of \(f\) and \(g\) do not intersect. For example, \(f(x)=e^{x}, g(x)=0\). Therefore the graphs \(y=f(x)\) and \(y=g(x)\) intersect at most once.
</details>

<li><p>

The equation \(x^{4}+x^{2}-1=0\) has<br>
(a) two positive and two negative roots<br>
(b) one positive, one negative and two non-real roots<br>
(c) all positive roots<br>
(d) no real root<br>
</p></li>

<details open><summary>Sol.</summary>
Ans: (b)<br>
Put \(x^{2}=y\). Then the equation becomes \(y^{2}+y-1=0\). Solving this equation, we get \(x^{2}=y=\frac{-1 \pm \sqrt{5}}{2}\). When \(x^{2}=\frac{-1+\sqrt{5}}{2}\), we get two real values of \(x\), one positive and other negative. But no real \(x\) exists such that \(x^{2}=\frac{-1-\sqrt{5}}{2}\). Hence The equation \(x^{4}+x^{2}-1=0\) has one positive, one negative and two non-real roots.
</details>

<li><p> The value of \(\lim_{x \rightarrow 1} \frac{\int_{1}^{x} e^{t^{2}} d t}{x^{2}-1}\) is<br>
(a) 0<br>
(b) 1 <br>
(c) \(e\)<br>
(d) \(e/2\)<br>
</p></li>

<details open><summary>Sol.</summary>
Ans: (d)<br>
This limit is in the form \(\frac{0}{0}\). Then by L'Hospital rule, \(\lim_{x \rightarrow 1} \frac{\int_{1}^{x} e^{t^{2}} d t}{x^{2}-1}=\lim_{x \rightarrow 1} \frac{\frac{d}{d x} \int_{1}^{x} e^{t^{2}} d t}{2 x}=\lim_{x \rightarrow 1} \frac{e^{x^{2}}}{2 x}=\frac{e}{2}\)
</details>

</ol>




## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---


<p><b>B1.</b>
(a) Consider the polynomial \( p(x)=n\left(x^n+1\right)-2\left(x^{n-1}+\cdots+x\right) \). If \(n>2\), how
many negative co-efficients does \(p(x)\) have?
</p>

<details open><summary>Sol.</summary>
(a) We show that \(p(x)\) has \(2 n-2\) negative coefficients. 
\[
\begin{aligned}
p(x)^2= & n^2\left(x^{2 n}+x^n+1\right)-2 n\left(x^n+1\right)\left(x^{n-1}+\cdots+x\right) \\
& +\left(x^{n-1}+\cdots+x\right)^2
\end{aligned}
\]
For \(i \in\{1, \ldots, n-1, n+1, \ldots, n-1\}\), the coefficient of \(x^i\) in \(p(x)^2\) is at most \(-2 n\) (coming from the cross term) plus \(-2 n+2\) (from expanding \(\left.\left(x^{n-1}+\cdots+x\right)^2\right)\), and hence negative.
</details>


---



<ol>

<li><p> The number of primes \(p\) such that \(p, p+10, p+14\) are all prime numbers is<br>
a) 0<br> b) 1<br> c) 3<br> d) infinitely many
</p></li>


<details open><summary>Sol.</summary>
(b) If \(p=3\), we note that \(3,13,17\) are all prime. Thus \(p=3\) is a solution. Any other prime is either of the type \(3 k+1\) or \(3 k+2\). If \(p=3 k+1\) for some integer \(k \geq 0\), then \(p+14=3(k+5)\) is not a prime. If \(p=3 k+2\) for some integer \(k \geq 0\), then \(p+10=3(k+4)\) is not a prime. Thus \(p=3\) is the only solution.
</details>


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






