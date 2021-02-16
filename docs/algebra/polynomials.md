---
layout: default
title: Polynomials
parent: Algebra
nav_order: 1
---



# Polynomials
{: .no_toc}


[](http://yufeizhao.com/olympiad/intpoly.pdf)
[](https://sites.math.northwestern.edu/~mlerma/problem_solving/putnam/training-poly.pdf)

#### Topics
{: .no_toc }

1. TOC
{:toc}

---


## Nature of polynomial roots [6]

<!-- {: .fw-300 .text-grey-dk-000 } -->



### Roots of a quartic polynomial
{: .d-inline-block}

A5, 2017
{: .label}

<p>
Find all the roots of the polynomial:
\[ x^{4}+x^{3}+2 x^{2}+x+1=0 \]
</p>

<details><summary>Solution</summary>
<p> We factor the polynomial as follows: \(x^{4}+x^{3}+2 x^{2}+x+1=\left(x^{2}+1\right)\left(x^{2}+x+1\right)\).
</p>

<p>
So the roots are \(i,-i,\omega\) and \(\omega^2\).
</p>
</details>


---


### Roots of a quadratic
{: .d-inline-block}

A6, 2011
{: label .label-blue}

<p>
The equation \(x^{2}+b x+c=0\) has non-zero real coefficients satisfying \(b^{2}>4 c\). Moreover, exactly one of \(b\) and \(c\) is irrational. Consider the solutions \(p\) and \(q\) of this equation.
</p>

<p>Which of these statements are correct?</p>


- [ ] Both \\(\; p\; \\) and \\(\; q\; \\) must be rational.
- [ ] Both \\( \;p\; \\) and \\( \;q\; \\) must be irrational.
- [ ] One of \\(\; p\; \\) and \\(\; q\; \\) is rational and the other irrational.
- [ ] We cannot conclude anything about rationality of \\(\; p\; \\) and \\(\; q\; \\) unless we know \\(\; b\; \\) and \\(\; c\; \\).

<details><summary>Solution</summary>


<p>
(b) Both \( \;p\; \) and \( \;q\; \) must be irrational. <br>


Since the discriminant is positive, both the roots must be real. Since \(c\neq 0\), the roots must be non-zero. We know that \(p+q=-b\) and \(pq=c\).
If one root is rational and the other is irrational, then both \(b\) and \(c\) must be irrational. If both the roots are rational, then both \(b\) and \(c\) must be rational. Hence, both \(p\) and \(q\) must be irrational.



</p>

</details>

---

### Find the possible coefficients given the roots
{: .d-inline-block}

A7, 2018
{: .label }


<p>Suppose \(x^{3}+a x^{2}+b x+8=0\) is a cubic equation with integer coefficients.
Both \(r\) and \(-r\) are the roots of the equation, where \(r>0\) is a real number.
List all possible pairs of values \((a, b)\).
</p>

<details><summary>Solution</summary>

<p>
Let the third root be \(s\).
By Vieta's formulas we have<br>

\begin{align}
-r+r+s &= -a \\
-rs + rs -r^2 &= b \\
-r^2s &= -8
\end{align}

which implies that \(b=-r^2\) must be negative and  \(ab=8\).
</p>


<p>
So the possible pairs of values of \((a, b)\) are \(\{ (-1,-8), (-2,-4), (-4,-2), (-8,-1) \} \).
</p>


</details>


---
### 0,1-polynomial
{: .d-inline-block}

A7, 2011
{: label .label-blue}


<p>
When does the polynomial \(1+x+\cdots+x^{n}\) have \(x-a\) as a factor? Here \(n\) is a positive integer greater than 1000 and \(a\) is a real number.
</p>

- [ ] if and only if \\(\;a=-1\\).
- [ ] if and only if \\(\;a=-1\;\\) and \\(\;n\;\\) is odd.
- [ ] if and only if \\(\;a=-1\;\\) and \\(\;n\;\\) is even.
- [ ] We cannot decide unless \\(\;n\;\\) is known.


<details><summary>Solution</summary>

<p>

(b) We have:

\[f(x)=\frac{1-x^{n+1}}{1-x} \mbox{ for } x\neq 1\]

If \(a\) is a root of \(f\), then \(a^{n+1}=1\).

Since \(f(1)=n\), 1 cannot be a root of \(f\). So \(a\neq 1\). The only other possibility is \(a=-1\) with \(n\) being odd.


</p>

</details>






---

### Parity of a polynomial
{: .d-inline-block}

A2, 2010
{: .label .label-blue}

<p>
A polynomial \(f(x)\) has integer coefficients such that \( f(0)\) and \( f(1)\) are both odd numbers.
Prove that \( f(x) = 0 \) has no integer solutions.
</p>

<details>
<summary> Solution </summary>

<p>
Suppose \(f(x)=c_{n} x^{n}+c_{n-1} x^{n-1}+\cdots+c_{0}\)

Since \( f(0) \) and \( f(1) \) are odd numbers, \(c_0\) is odd and

\[ \text{Parity of } \sum_{i=1}^n c_i \text{ is even}\]


Suppose \(f(x)\) has an integer root \(r\). Let us see what happens to the parity of \( f(r) \).

For \(n\geq 1\), the parity of \(r^n\) is the same as that of \(r\). So:

\begin{align}
\text{Parity of }f(r) &= \text{Parity of }r \times \text{Parity of} \sum_{i=1}^n c_i  + \text{Parity of }c_0 \\
\text{Parity of }f(r) &= \text{odd}
\end{align}

Since \( f(r) \) is an odd number, \(r\) cannot be a root of the polynomial.

</p>

</details>

---


### Degree constraint on the polynomial
{: .d-inline-block}

B5, 2011
{: label .label-blue}

<p>
It is given that the complex number \(i−3\) is a root of the polynomial \(p(x) = 3x^4+10x^3+Ax^2+Bx−30\),
where \(A\) and \(B\) are unknown real numbers.  Find the other roots.
</p>

<details><summary>Solution</summary>

<p>
Complex roots come in conjugates, so \(-i-3\) must also be a root. So \( (x-i+3)(x+i+3) = (x^2+6x+10) \) must be a factor of \(p(x)\):

\[ p(x) = (x^2+6x+10)(ax^2+bx+c) \]

By comparing the coefficients, \(a=3,b=-8,\text{and }c=-3\). Hence the polynomial is:

\[ (x^2+6x+10)(3x^2-8x-3) \]
\[ = (x^2+6x+10)(x-3)(3x+1) \]

Hence, the other roots are 3 and -1/3.

</p>


</details>

---


### Only one real root
{: .d-inline-block}

B8, 2011
{: label .label-blue}


<p>
Suppose \(f(x) = x^3 + x^2 + cx + d\), where \(c\) and \(d\) are real numbers. Prove that if \(c>1/3\),
then \(f\) has exactly one real root.
</p>

*Requires calculus too*.

<details><summary>Solution</summary>

<p>
Since the function has an odd degree as the highest power, it has at least one
real root. The function has exactly one real root since it is monotonic in \(\mathbb{R}\), as proved below.
</p>


<p>
<b>Lemma.</b> \(f(x)\) is a monotonic function in \( \mathbb{R} \).<br>

<b>Proof.</b> Consider the derivative of \(f\).

\[ f'(x) = 3x^2+2x+c \]


The discriminant of the above quadratic, \(2^2-4\cdot3\cdot c\), is negative when \(c>1/3\). Hence, \(f'(x)\) is always positive in \(\mathbb{R}\).


To see why \(f(x)\) is a strictly increasing function, consider any two points \(a\) and \(b\) in \(\mathbb{R}\) with \(b > a\). By mean value theorem,
there exists an \(\alpha \in (a,b)\) such that:

\begin{align}
f^{\prime}(\alpha) &= \frac{f(b) - f(a)}{b-a} \\
f(b) - f(a) &= f^{\prime}(\alpha) (b-a) > 0 \\\\
& \Rightarrow\;  f(b) > f(a) \quad\quad\square
\end{align}

</p>


</details>

---

### Polynomial with positive coefficients
{: .d-inline-block}

A5, 2015
{: .label}

<p>
Consider the polynomial \(p(x)=\left(x+a_{1}\right)\left(x+a_{2}\right) \cdots\left(x+a_{10}\right)\) where \(a_{i}\) is a real number for each \(i=1, \ldots, 10\).
Suppose all the eleven coefficients of \(p(x)\) are positive.

Which of these statements are true?

<ul>
<li>(i) The polynomial \(p(x)\) must have a global minimum. </li>
<li>(ii) Each \(a_{i}\) must be positive.</li>
<li>(iii) All real roots of \(p^{\prime}(x)\) must be negative.</li>
<li>(iv) All roots of \(p^{\prime}(x)\) must be real.</li>
</ul>


</p>

<details><summary>Solution</summary>


<p>
All of them are true.
</p>

<p>
(i) Since the degree is even, \(p(x)\) goes to \(+\infty\) as \(x \rightarrow \pm \infty .\) So \(p(x)\) must have a global minimum somewhere.
</p>


<p>
(ii) The roots of \(p(x)\) are \(-a_{i}\)s. Since the coefficients of \(p(x)\) are positive, no nonnegative number is a root of \(p(x)\).
Thus all the \(a_i\)s are positive.
</p>

<p>
(iii) and (iv)  All 10 roots of \(p(x)\) are real and negative. There is a root of \(p^{\prime}(x)\) between consecutive roots of \(p(x)\) (this is valid even in case of multiple roots). So all 9 roots of \(p^{\prime}(x)\) are real and negative as well. For negativity, one can also note that all coefficients of \(p^{\prime}(x)\) are positive and apply the logic in (ii) to \(p^{\prime}(x)\).
</p>


</details>

---





### Find a rational polynomial with a given root
{: .d-inline-block }

B1, 2012
{: .label}


<p>
a) Find a polynomial \(p(x)\) with \(\sqrt{2}+i\) as a root and \(p(x)\) having real coefficients.
</p>

<p>
b) Find a polynomial \(q(x)\) with rational coefficients and having the least degree such that \(\sqrt{2}+i\) is a root.
</p>

<p>
c) Show that any other polynomial \(f(x)\) with rational coefficients and \(p(\sqrt{2}+i)=0\) has \(q(x)\) as a factor.
</p>




<details><summary>Solution</summary>

<p>
(a) Non-real roots of a polynomial with real coefficients occur in conjugate pairs.

\begin{align}
\text{Let }  p(x) &= (x-(\sqrt{2}+i))(x-(\sqrt{2}-i)) \\
&=x^{2}-2 \sqrt{2} x+3
\end{align}

Since all the coefficients are real, the above quadratic is an example.

</p>

<p>
(b) The above polynomial \(p(x)\) has one irrational coefficient. We try squaring it as follows:
</p>

<p>
\begin{align}
(x-(\sqrt{2}+i))(x-(\sqrt{2}-i)) & = 0 \\
x^{2}-2 \sqrt{2} x+3 & = 0 \\
x^{2}+3 & = 2 \sqrt{2} x \\
(x^{2}+3)^2 & = 8x^2
\end{align}
</p>

<p>
So \( q(x) = (x^2+3)^2 - 8x^2 \) is a polynomial with integer coefficients with \(\sqrt{2}+i\) as one of its roots. We
found a polynomial with degree 4. We show that 4 is the least degree for which such a polynomial exists.
</p>


<p>
<b>Lemma.</b> There is no cubic polynomial \(q(x)\) with rational coefficients with \( q(\sqrt{2} + i) = 0 \).
</p>

<p>
<b>Proof.</b> Let \( \sqrt{2}+i \), \(\sqrt{2}-i\) and \(r\) be the roots of such a cubic, if it exists. We have:

\begin{align}
q(x) & = (x^{2}-2 \sqrt{2} x+3)(x-r) \\
& = x^{3}-(2 \sqrt{2}-r)x^2 + 2\sqrt{2}r x - 3r
\end{align}

If \(q\) has only rational coefficients, both \(2\sqrt{2}-r\) and \( 3r \) must be rational (Contradiction). \(\;\;\square\)
</p>

<p>
(c)
Let \(f(x)\) be a polynomial with rational coefficients such that \(f(\sqrt{2}+i)=0\).

Divide \(f(x)\) by \(q(x)\) using long division to get quotient \(a(x)\) and remainder \(b(x),\) both
polynomials with rational coefficients.

\[ f(x)=q(x)a(x)+b(x) \]

Using \(f(\sqrt{2}+i)=0\) and \(q(\sqrt{2}+i)=0\) in the equation gives \(b(\sqrt{2}+i)=0\).
Now if the remainder \(b(x)\) is a nonzero polynomial, then it would have rational coefficients, degree less than 4 and \(\sqrt{2}+i\) as a root.
But we have proved in part (b) that such a polynomial does not exist. Hence, \(b(x)=0\) which implies that \(f(x)\) is a multiple of \(q(x)\).



</p>

</details>

---


### Dependent roots
{: .d-inline-block}

B5, 2020
{: .label}

<p>
A monic polynomial has the following property: If \(r\) is a root, then \(r^2 -4\) is also a root. Let us denote this property by \(\tau\).
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
four cases. The polynomials obtained are numbered from (i) to (vi) in the table below.
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



### Repeated roots
{: .d-inline-block}

A9, 2010
{: .label}

<p>
Suppose \(\displaystyle f(x)=\frac{x^{n}}{n!}+\frac{x^{n-1}}{(n-1)!}+\cdots+x+1\).
</p>

<p>
Show that \(f(x)=0\) has no repeated roots.
</p>

<i>Requires calculus</i><br>

<details><summary>Solution</summary>


<p>
Since zero cannot be a root of \(f(x)\), we focus only on the non-zero roots. Let us assume, for a contradiction, that \(f\) has a repeated root \(r\neq 0\).</p>

<p>
<b>Fact.</b> If \(r\) is a repeated root both \(f(r)\) and \(f^{\prime}(r)\) must be zero.
</p>


<p>
On differentiating \(f(x)\), we get:<br>
\[ f^{\prime}(x)=\frac{x^{n-1}}{(n-1) !}+\frac{x^{n-2}}{(n-2) !}+\cdots+x+1 \]
</p>


<p>
\[ f(x)-f^{\prime}(x)=\frac{x^{n}}{n!} \]
</p>

<p>
Therefore, \(r\) cannot be a repeated root since RHS \(\displaystyle = \frac{r^{n}}{n!} \neq 0 \).
</p>

</details>





---


## Polynomial functions [5]


### Polynomial that gives only prime powers
{: .d-inline-block }

B8, 2012
{: .label }

<p>
Let \(f(x)\) be a polynomial with integer coefficients \(f(n)\) evaluates to a <i>prime power</i> for every integer \(n\). A prime power is a number of the form \(p^{k}\), where \(p\) is prime and \(k\) a positive integer. Prove that \(f(x)\) is a constant.
</p>

<p>
a) If such a polynomial \(f(x)\) exists, then there is a polynomial \(g(x)\) with integer coefficients such that for each nonnegative integer \(n\),
\(g(n)\) is a perfect power of a fixed prime number.
</p>

<p>
b) Show that \(g(x)\) as in part (a) must be a constant polynomial.
</p>

<p>
c) Show that \(f(x)\) is a constant polynomial.
</p>


<details><summary>Solution</summary>

<p>(a)
Write \(f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0} .\) Then \(a_{0}=f(0)=p^{k}\) for some prime
\(p\) and integer \(k > 0\). Define \(g(x)=f(p x) .\) Then \(g(x)\) is a polynomial such that for each nonnegative integer \(n, g(n)=f(p n)=\) a perfect power of a prime number. This prime number has to be \(p,\) because by evaluating we see that \(g(n)=f(p n)\) is divisible by \(p\).
</p>


<p>(b)
Let \(g(x)=b_{n} x^{n}+b_{n-1} x^{n-1}+\cdots+b_{1} x+b_{0} .\) Then \(b_{0}=g(0)=p^{k} .\) Consider:

\[ g\left(m p^{k+1}\right)=(b_{n}\left(m p^{k+1}\right)^{n}+b_{n-1}\left(m p^{k+1}\right)^{n-1}+\cdots+b_{1}\left(m p^{k+1}\right)+p^{k}\]

Clearly for each non-negative integer \(m\), this expression is divisible by \(p^{k},\) but not by \(p^{k+1}\) (since it is \(p^{k}\) modulo \(p^{k+1}\) ). This forces \(g\left(m p^{k+1}\right)=p^{k}\) for all \(m,\) since it must be a perfect power of \(p .\) Thus the polynomial \(g\) takes the value \(p^{k}\) infinitely often, so it must be identically equal to \(p^{k}\). (Otherwise the polynomial \(g(x)-p^{k}\) would have infinitely many roots.) To finish the problem, note that since \(g(x)=f(p x)\) is constant, \(f(x)\) must be constant by the same logic.
</p>


</details>

---




### Sum of squares polynomial
{: .d-inline-block}

A4, 2013
{: .label}

<p>
A polynomial \(f(x)\) with real coefficients is said to be a sum of squares (SoS) if we can write \(f(x)=p_{1}(x)^{2}+\cdots+p_{k}(x)^{2},\) where \(p_{1}(x), \ldots, p_{k}(x)\) are polynomials with real coefficients. <br>

Which statements given below are true?

</p>

<p>
a) If a polynomial \(f(x)\) is a SoS, then the coefficient of every odd power of \(x\) in \(f(x)\) must be 0.
</p>

<p>
b) If \(f(x)=x^{2}+p x+q\) has a non-real root, then \(f(x)\) is a sum of squares.
</p>

<p>
c) If \(f(x)=x^{3}+p x^{2}+q x+r\) has a non-real root, then \(f(x)\) is a sum of squares.
</p>

<p>
d) If a polynomial \(f(x) > 0\) for all real values of \(x,\) then \(f(x)\) is a sum of squares.
</p>



<p><em> <b>Aside.</b> This kind of polynomial shows up in a research area called algebraic complexity theory. A few former CMI students and faculty
work in this area. For example, take a look at this <a href="https://www.cse.iitk.ac.in/users/nitin/theses/sanyal-2020.pdf">master's thesis [pdf]</a> by Abhiroop Sanyal, if you're curious.
</em>
</p>


<details><summary>Solution</summary>

<p> False-True-False-True </p>

<p> (a) Counterexample: \( (x+1)^2 = x^2+2x+1 \)  </p>

<p>
(b) Complete the square to get \(f(x)=x^{2}+p x+q=\left(x+\frac{p}{2}\right)^{2}+\left(\frac{4 q-p^{2}}{4}\right)\). Since the roots are non-real the discriminant is negative, which implies \(4 q-p^{2} > 0\).
</p>


<p>
(c) Note that \(f(x) \rightarrow-\infty\) as \(x \rightarrow-\infty,\) so in particular \(f(x)\) takes negative values and hence can never be a sum of squares. This applies to any odd degree polynomial.
</p>

<p>
(d) Since all roots of \(f\) are non-real and occur in conjugate pairs, \(f(x)\) is a product of quadratic polynomials each of which is a sum of squares as shown in part (b).
</p>



<p><i><b>Further reading.</b> A generalization of part (d) is connected to <a href="http://www.math.ens.fr/~benoist/articles/CarresEMS.pdf">Hilbert's 17th problem [pdf]</a>.</i></p>


</details>

---

### Polynomials that exponentiate
{: .d-inline-block }

B4, 2013
{: .label}

<p>
Suppose  \(f(x)\) is a function from \(\mathbb{R}\) to \(\mathbb{R}\) such that \(f(f(x))=f(x)^{2013}\).
</p>

<p>
(a) Show that there are infinitely many such functions.
</p>

<p>
(b) Exactly four of those functions are polynomials.
</p>

<details><summary>Solution</summary>

<p>
(a) Define \(f(0)=0, f(1)=1\) and \(f(-1)=-1\). For every other real number \(x,\) arbitrarily equate \(f(x)\) to 0,-1 or 1. Any such function
satisfies the given condition.
</p>



<p>
(b) If \(f\) is a polynomial, then we make two cases.<br>
</p>

<p>
(i) If \(f(x)=\) a constant \(c,\) then the given condition is equivalent to \(c=c^{2013},\) which happens precisely for three values of \(c,\) namely \(c=0,1,-1\) (since we have \(c\left(c^{2012}-1\right)=0,\) so \(c=0\) or \(c^{2012}=1\) ). Thus there are three constant functions with the given property.
</p>

<p>
(ii) If \(\mathrm{deg}(f)\geq 1\), then consider its range set \(A=\{f(x) \mid x \in \mathbb{R}\}\).
Now for all \(a \in A,\) we have by the given property \(f(a)=a^{2013}\).
So the polynomial \(f(x)-x^{2013}\) has all elements of \(A\) as its roots.
Since there are infinitely many values in \(A\) (e.g. applying the intermediate value theorem because \(f\) is continuous), the polynomial \(f(x)-x^{2013}\) has infinitely many roots and thus must be the zero polynomial, i.e., \(f(x)=x^{2013}\) for all real number \(x\).
</p>

</details>

---


### Recursive polynomial
{: .d-inline-block}

A9, 2018
{: .label}


<p>
Consider a sequence of polynomials with real coefficients defined recursively as follows:
\begin{align}
p_{0}(x)&:=\left(x^{2}+1\right)\left(x^{2}+2\right) \cdots\left(x^{2}+1009\right) \\
p_{k+1}(x)&:=p_{k}(x+1)-p_{k}(x)
\end{align}

with subsequent polynomials defined by  for \(k \geq 0 .\) Find the least number \(n\) for which \[ p_{n}(1)=p_{n}(2)=\cdots=p_{n}(5000) \]

</p>

<details><summary>Solution</summary>

<p>
\(n=2018\). Note that \(\operatorname{deg} p_{0}(x)=2018\) and \(\operatorname{deg} p_{k}(x)=2018-k\).
Define \(g_{n}(x)=p_{n}(x)-p_{n}(1)\), hence \(g_{n}(x)\) has degree \(2018-n\) and 5000 roots.
</p>

</details>

---

### Binomial polynomial
{: .d-inline-block }

A9, 2020
{: .label}


<p>
A polynomial \( p(x) \) of degree \(7\) satisfies \(p(n)=2^n\) for \(n=0\) to \(7\).  Find \(p(10)\).<br>

Hint: Notice that the polynomial \( g(x) = 1 + x + \frac{x(x-1)}{2} \) equals \(2^x\) for \(x\in\{0,1,2\}\).
</p>


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

The next problem (<a href="/docs/algebra/polynomials/#difference-equations">B5, 2014</a>) also involves binomial polynomials.

</details>



---
### Difference equations
{: .d-inline-block }

B5, 2014
{: .label}


<p>
(i) Let \(f(x)=a_{n} x^{n}+\cdots+a_{1} x+a_{0}\) be a polynomial with real non-zero coefficients. What is the leading term of the polynomial \( \Delta f(x):=f(x)-f(x-1) \)?
</p>

<p>
(ii) Define polynomials \(p_{n}\) of degree \(n\) as follows:

<br>

\begin{align}
p_{0}(x) & =1 \\
p_{1}(x) &=x \\
p_{2}(x) &=\frac{x(x-1)}{2} \\
p_{3}(x) &=\frac{x(x-1)(x-2)}{3!} \cdots \\
&\vdots \\
p_{n}(x)&=\frac{1}{n!} x(x-1)(x-2) \cdots(x-n+1) \\
\end{align}



<br>
Show that for any polynomial \(f\) of degree \(n,\) there exist unique real numbers \(b_{0}, b_{1}, \ldots, b_{n}\) such that \(f(x)=\sum_{i=0}^{n} b_{i} p_{i}(x)\)
</p>



<p>
(iii) A polynomial \(f(x)\) is called  <em>integer-valued</em> if \(f(n)\) is an integer for every integer \(n\). Show that if an integer-valued polynomial is
expressed in terms of \(p_n\)s as above, the coefficients \(b_{i}\)s obtained in part (ii) are integers.
</p>



<details><summary>Solution</summary>

<p>
(i) After expanding the powers of \((x-1),\) the degree \(n\) terms of \(f(x)\) and \(f(x-1)\) cancel out.  The degree \(n-1\) term from \(f(x)\)
cancels with the leading term of \(a_{n-1}(x-1)^{n-1}\). The only remaining term of degree \(n-1\) has to come from \(a_{n}(x-1)^{n}\).
So \(\Delta f(x)=n a_{n} x^{n-1}+\mathrm{lower\; degree\; terms}\). This is similar to the derivative. <br><br>
</p>


<p>
(ii)  We use induction on the degree of \(f .\) If \(f(x)=a_{0}\) is constant, \(b_{0}=a_{0}\) works uniquely (base case).
<br>
<i> Inductive hypothesis. </i> Assume the result for polynomials of degree strictly less than \(n\) and let \(f\) be of degree \(n,\) so \(a_{n} \neq 0 .\) We are forced to take \(b_{n}=n ! a_{n}\) by comparing leading coefficients of \(f(x)\) and \(\sum_{i=0}^{n} b_{i} p_{i}(x) .\)
<br>
Now \(f(x)-b_{n} p_{n}(x)\) is a polynomial of degree \(d < n\) and hence by induction equals \(\sum_{i=0}^{d} b_{i} p_{i}(x)\) for unique \(b_{0}, \ldots, b_{d}\) Therefore \(f(x)=\sum_{i=0}^{n} b_{i} p_{i}(x),\) where \(b_{d+1}, \ldots, b_{n-1}\) are all \(0 .\) To see uniqueness of \(b_{i}^{\prime} s,\) let \(\sum_{i=0}^{n} b_{i} p_{i}(x)=\sum_{i=0}^{n} c_{i} p_{i}(x) .\) Subtract all terms with \(b_{i}=c_{i} .\) If any terms are remaining, compare the leading coefficients on each side to get a contradiction.
</p>


<p>
<i><b>Alternate solution</b>. If we are allowed to use <a href="/docs/algebra/solvability/#solutions-to-simultaneous-equations">linear algebra</a>, it is a one-line proof.</i>
The \( p_i \)s form a basis for polynomial functions, so any polynomial has a unique representation.
</p>

<p>
(iii) Substitute \(x=0,1,2, \ldots\) one by one in the equation \(f(x)=\sum_{i=0}^{n} b_{i} p_{i}(x)\) and solve for \(b_{0}, b_{1}, b_{2}, \ldots\) successively. \(x=0\) gives \(b_{0}=f(0) .\) Using \(x=1\) and 2 gives \(b_{1}=f(1)-b_{0}\) \(b_{2}=f(2)-b_{0}-2 b_{1} .\) In general, for all integers \(t, p_{i}(t)=\left(\begin{array}{c}t \\ i\end{array}\right)\) is an integer. Further, \(p_{i}(t)=0\) if \(0 \leq t < i\) and 1 if \(t=i .\) So \(b_{t}=f(t)-\sum_{i=0}^{t-1} b_{i}\left(\begin{array}{c}t \\ i\end{array}\right),\) which is an integer by induction.
</p>

</details>

---



#### Problem credits

<img src="/assets/images/brook_taylor.jpg" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
The previous two problems are based on a topic  called method of finite differences. It was introduced by Brook Taylor (of Taylor series fame)
in 1715 and further developed by Isaac Newton. The similarity to differentiation is not an accident. Read more about it on <a href="https://en.wikipedia.org/wiki/Finite_difference">Wikipedia</a>.
</p>
{: .fs-4 .fw-300 }

Brook Taylor (1685-1731)

---





## Polynomial division [3]

### Guess the polynomial
{: .d-inline-block }

A7, 2020
{: .label}

<p>
\(P(x)=10x^{400}+ax^{399}+bx^{398}+3x+15\).
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



### Find the remainders
{: .d-inline-block }

A8, 2014
{: .label}

<p>
(i) What is the remainder when \(f(x)=7 x^{32}+5 x^{22}+3 x^{12}+x^{2}\) is divided by \((x^{2}+1)\)?  <br><br>
(ii) What is the remainder when \(x f(x)\) is divided by \((x^{2}+1)\)?
</p>


<details><summary>Solution</summary>

<p>
(i) The function has only even powers. Let us put \(z=x^{2}\). We want to know the
remainder of \(7z^{16}+5z^{11}+3z^{6}+z\) when divided by \((z+1)\). By remainder theorem,

\[ 7(-1)^{16}+5(-1)^{11}+3(-1)^{6}+(-1)=4 \]

</p>

<p>
So we have \(f(x)=q(x)\left(x^{2}+1\right)+4\), where \(q(x)\) is some polynomial.

<br>
<br>
(ii) \(x f(x)=x q(x)\left(x^{2}+1\right)+4x\), so the second remainder is \(4x\).
</p>

</details>

---

### Integer-valued polynomials
{: .d-inline-block}

A8, 2016
{: .label}

<p>
A function \(g\) has the property that \(g(n)=3n+5\) for each of the 15 integers in the range \([1,15]\).

Which of the statements are true?<br>

<ul>
<li>(i) If \(g(x)\) is a linear polynomial, then \(g(x)=3 x+5\)</li>
<li>(ii) \(g\) cannot be a polynomial of degree 10.</li>
<li>(iii) \(g\) cannot be a polynomial of degree 20.</li>
<li>(iv) If \(q\) is differentiable, then \(g\) must be a polynomial.</li>
</ul>
</p>


<details><summary>Solution</summary>

<p>
True-True-False-False<br>

<p>
(i) If \(g(x)\) is linear, it is uniquely determined by any two values.<br>
</p>

<p>
(ii) If \(g(x)\) is a polynomial then it is of the form \(q(x)(x-1)(x-2) \cdots(x-15) + 3x+5\), where \(q(x)\) is some polynomial.
So \(g(x)\) cannot be a polynomial of degree 10.
</p>

<p>
<i>The official solution states this fact without a proof. Why should the polynomial have a \(3x+5\) term? It is not clear.  Where is the consecutive property of integers getting used? </i>
</p>

<i>This problem is related to difference equations on integer-valued functions. See this <a href=" https://web.math.rochester.edu/people/faculty/doug/otherpapers/Cahen-Chabert.pdf">paper</a> and in particular Proposition 1 on page 313.</i>


<p>
(iii) \(g(x)\) can have any degree more than 15. To get 20, pick \(q(x)\) to be \(x^5\) in the expression in (ii).
</p>

<p>
(iv) Pick \(q(x)=\sin x\), for a counterexample.
</p>

</p>

</details>

---

### Given the remainders, find the polynomials
{: .d-inline-block}

B5, 2016
{: .label}


<p>Find a single polynomial \(p(x)\) that has these two properties:<br>

(i) If \(p(x)\) is divided by \(x^{100}\), the remainder is the constant polynomial 1.<br>

(ii) If \(p(x)\) is divided by \((x-2)^{3}\), the remainder is the constant polynomial 2.<br>
</p>

<p><i>Requires calculus.</i></p>

<details><summary>Solution</summary>

<p>
Conditions (i) and (ii) imply that for some polynomials \(q(x)\) and \( r(x) \), we should be able to express \(p(x)\) as:
</p>

<p>
\begin{align}
p(x) &= q(x)x^{100} + 1 \\
p(x) &= r(x)(x-2)^{3} + 2
\end{align}
</p>

<p>
<b>Key observation.</b> If we did not have the plus one terms at the end, we could have simply multiplied the two RHS terms. Taking the
derivative makes the 1s go away. So let us look at \( p^\prime{(x)} \).
</p>

<p>
\begin{align}
p^\prime(x) &= 100q(x)x^{99} + q^\prime(x) x^{100} \\
&= x^{99}\times (100q(x) + q^\prime(x) x^{100})
\end{align}
</p>


\begin{align}
p^\prime(x) &= 3r(x)(x-2)^{2} + r^\prime(x) (x-2)^{3} \\
&= (x-2)^2 \times ( 3r(x) + r^\prime(x)(x-2) )
\end{align}



<p>So \(p\prime(x)\) has \(x^{99}\)  and  \( (x-2)^{2} \) as factors. We may assume</p>

<p>
\[ p^\prime(x) =  Ax^{99}(x-2)^2 \]
</p>

<p>
for some constant \(A\). The assumption is justified since any polynomial whose derivative is divisible by \(x^{99}(x-2)^{2}\) will leave constant remainders when divided by either of \(x^{100}\) and \((x-2)^{3}\).
</p>

<p>
So let us find \( p(x) \) by integrating \( p^\prime (x) \):
</p>

<p>
\[ p(x)=A\left(\frac{x^{102}}{102}-\frac{4 x^{101}}{101}+\frac{4 x^{100}}{100}\right)+B \]
</p>


<p>
We use properties (i) and (ii) to calculate \(A\) and \(B\).
</p>


<p>
\begin{align}
p(0)&=B=1 \\
p(2)&=A\left(\frac{2^{102}}{102}-\frac{4 \times 2^{101}}{101}+\frac{4 \times 2^{100}}{100}\right)+1=2
\end{align}
</p>

<p>
So \(A=2\) and \(B=1\).
</p>



</details>

---



