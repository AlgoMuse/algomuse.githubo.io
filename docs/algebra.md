---
layout: default
title: Algebra
nav_order: 3
---


# Algebra


[](http://yufeizhao.com/olympiad/intpoly.pdf)
[](https://sites.math.northwestern.edu/~mlerma/problem_solving/putnam/training-poly.pdf)




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

\begin{align}
\text{Parity of }f(r) &= \text{Parity of }r \times \text{Parity of} \sum_{i=1}^n c_i  + \text{Parity of }c_0 \\
\text{Parity of }f(r) &= \text{odd}
\end{align}

Since \( f(r) \) is an odd number \(r\) cannot be a root of the polynomial.

</p>

</details>

---

### Binomial expansion
{: .d-inline-block}

B2, 2011
{: label .label-blue}

Show that the power of \\(x\\) with the largest coefficient in the polynomial \\(\displaystyle (1 + 2x/3)^{20}\\) is 8. In other words, if
we write the given polynomial as \\( \sum_i a_ix^i\\) then the largest coefficient \\(a_i\\) is \\(a_8\\).


#### Solution

The co-efficient \\( a_i = \binom{20}{i} \left(\frac{2}{3}\right)^i \\). Consider the ratio of two consecutive terms: \\( a_{i+1}/a_i \\).

\begin{align}
\text{ratio } &= \frac{2}{3} \times \left(  \frac{20!}{20-i-1!i+1!}/\frac{20!}{20-i!i!} \right) \\\\\\\\
&\\\\\\\\
  &= \frac{2}{3} \cdot \frac{20-i!i!}{20-i-1!i+1!} = \frac{2(20-i)}{3(i+1)}
\end{align}


The ratio \\( a_{i+1}/a_i > 1\\) upto \\(i\leq 7\\) and strictly less than 1 for \\(i>7\\). Hence, the sequence of co-efficients is bitonic with the peak occuring at \\(a_8\\).

---

### AM-GM inequality
{: .d-inline-block}

A4, 2011
{: label .label-blue}

Given positive real numbers \\( a_1, a_2, \ldots , a_{2011} \\) whose product \\(a_1 a_2 \cdots a_{2011}=1\\),
what can you say about their sum \\( S = a_1 + a_2 + · · · + a_{2011} \\)?

- [ ] \\( S\; \\) can be any positive number.
- [ ] \\( 1 \leq S \leq 2011\\).
- [x] \\( 2011 \leq  S \text{ and }  S\;\\) is unbounded above.
- [ ] \\( 2011 \leq  S \text{ and }  S\;\\) is bounded above.

#### Solution
The first inequality follows from AM-GM inequality. To see why \\(S\\) is unbounded, set
\\( a_1=n \\), \\(a_2=1/n\\) and the rest of \\( a_is\\) to 1. The sum \\(S>n\\) for any \\(n\\).


---

### Roots of a quadratic
{: .d-inline-block}

A6, 2011
{: label .label-blue}

The equation \\(x^{2}+b x+c=0\\) has nonzero real coefficients satisfying \\(b^{2}>4 c\\). Moreover, exactly one of \\(b\\) and \\(c\\) is irrational. Consider the solutions \\(p\\) and \\(q\\) of this equation.
- [ ] Both \\(\; p\; \\) and \\(\; q\; \\) must be rational.
- [ ] Both \\( \;p\; \\) and \\( \;q\; \\) must be irrational.
- [ ] One of \\(\; p\; \\) and \\(\; q\; \\) is rational and the other irrational.
- [ ] We cannot conclude anything about rationality of \\(\; p\; \\) and \\(\; q\; \\) unless we know \\(\; b\; \\) and \\(\; c\; \\).

#### Solution

(B) Let \\(p\\) and \\(q\\) be the roots of the equation. The condition in the problem implies that both are real and non-zero. We know that \\(p+q=-b\\) and \\(pq=c\\).
If one root is rational and the other is irrational, then both \\(b\\) and \\(c\\) must be irrational. If both the roots are rational, then both \\(b\\) and \\(c\\) must be rational. Hence, both \\(p\\) and \\(q\\) must be irrational.




### Polynomial factorization
{: .d-inline-block}

B5, 2011
{: label .label-blue}

It is given that the complex number \\(i−3\\) is a root of the polynomial \\(3x^4+10x^3+Ax^2+Bx−30\\),
where \\(A\\) and \\(B\\) are unknown real numbers.  Find the other roots.

#### Solution

Complex roots come in conjugates, so \\(-i-3\\) must also be a root. So \\( (x-i+3)(x+i+3) = (x^2+6x+10) \\) must be a factor. The given
polynomial can writen as
\\[ (x^2+6x+10)(ax^2+bx+c) \\]

By comparing the co-efficients, \\(a=3,b=-8,\text{and }c=-3\\). Hence the polynomial is:

\\[ (x^2+6x+10)(3x^2-8x-3) \\]
\\[ (x^2+6x+10)(x-3)(3x+1) \\]

Hence the other roots are 3 and -1/3.


---


### Only one real root
{: .d-inline-block}

B8, 2011
{: label .label-blue}




Suppose \\(f(x) = x^3 + x^2 + cx + d\\), where \\(c\\) and \\(d\\) are real numbers. Prove that if \\(c>1/3\\),
then \\(f\\) has exactly one real root.

*Requires calculus too*.

#### Solution

Since the function has odd degree as the highest power, it has at least one
real root. To show that the function has exactly one real root
we have to show, that it is monotonic in the whole \\(\mathbb{R}\\).
This can be done by showing that \\(f'(x)\\) is always positive when \\(c>1/3\\).

\\[ f'(x) = 3x^2+2x+c \\]

The discriminant of the above quadratic, \\(2^2-4\cdot3\cdot c\\), is negative when \\(c>1/3\\).
Hence, \\(f'(x)\\) is always positive in \\(\mathbb{R}\\).


---


### Monotonic again
{: .d-inline-block}

B1, 2017
{: label .label-blue}


Find the number of solutions to \\(e^{x}=\frac{x}{2017}+1\\)

#### Solution

This problem is similar to the last one. We need to show that the function is monotonic in some interval.
Consider the function:
\begin{align}
f(x)&=  e^x -\frac{x}{2017} - 1 \\\\\\\\
f'(x)&=  e^x -\frac{1}{2017}
\end{align}


The derivative is positive when \\(x>x_0=-\log 2017\\).

-  We have \\(f(x_0)<0\\) and \\( f(-\infty)>0 \\) so there is one solution in the interval \\( (-\infty,x_0)\\).
-  \\( x = 0 \\) is another solution.

Hence, there are two solutions to the equation.




### Find a rational polynomial with a given a root
{: .d-inline-block }

B1, 2012
{: .label}


<p>
a) Find a polynomial \(p(x)\) with real coefficients such that \(p(\sqrt{2}+i)=0\).
</p>

<p>
b) Find a polynomial \(q(x)\) with rational coefficients and having the smallest possible degree such that \(q(\sqrt{2}+i)=0 .\)
</p>

<p>
c) Show that any other polynomial with rational coefficients and having \(\sqrt{2}+i\) as a root has \(q(x)\) as a factor.
</p>



Sol.


<p>
(a) Non-real roots of a polynomial with real coefficients occur in conjugate pairs. \(p(x)=\) \((x-(\sqrt{2}+i))(x-(\sqrt{2}-i))=x^{2}-2 \sqrt{2} x+3\) works.
</p>
<p>
(b)\(\sqrt{2}+i\) satisfies \(x^{2}-2 \sqrt{2} x+3=0,\) i.e., \(x^{2}+3=2 \sqrt{2} x\) and so satisfies \(\left(x^{2}+3\right)^{2}=\) \(8 x^{2} .\) So \(q(x)=\left(x^{2}+3\right)^{2}-8 x^{2}\) works. A cubic with rational coefficients will not work because, after dividing by the necessarily rational leading coefficient, it must be of the form \(\left(x^{2}-2 \sqrt{2} x+3\right)(x-r) .\) This forces the coefficients \(-3 r\) and \(-2 \sqrt{2}-r\) to be both rational, which is impossible.
Let \(f(x)\) be a polynomial with rational coefficients such that \(f(\sqrt{2}+i)=0 .\)
</p>

<p>
(c)
Divide \(f(x)\) by \(q(x)\) using long division to get quotient \(a(x)\) and remainder \(b(x),\) both polynomials with rational coefficients. Using \(f(\sqrt{2}+i)=0\) and \(q(\sqrt{2}+i)=0\) in the equation \(f(x)=\) \(q(x) a(x)+b(x)\) gives \(b(\sqrt{2}+i)=0 .\) Now if the remainder \(b(x)\) is a nonzero polynomial, then it would have rational coefficients, degree less than 4 and \(\sqrt{2}+i\) as a root. But we just proved that this is impossible. Hence \(b(x)=0,\) i.e., \(f(x)\) is a multiple of \(q(x)\)
</p>




### Polynomial that gives only prime powers
{: .d-inline-block }


B8, 2012
{: .label }

<p>
Let \(f(x)\) be a polynomial with integer coefficients \(f(n)\) evaluates to a <i>prime power</i> for every integer \(n\). A prime power is a number of the form \(p^{k}\), where \(p\) is prime and \(k\) a positive integer. Prove that \(f(x)\) is a constant.
<br>
a) If such a polynomial \(f(x)\) exists, then there is a polynomial \(g(x)\) with integer coefficients such that for each nonnegative integer \(n, g(n)=\) a perfect power of a fixed prime number.
</p>

<p>
b) Show that a polynomial \(g(x)\) as in part a must be constant.
</p>


Sol.

<p>(a)
Write \(f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0} .\) Then \(a_{0}=f(0)=p^{k}\) for some prime
\(p\) and integer \(k > 0\). Define \(g(x)=f(p x) .\) Then \(g(x)\) is a polynomial such that for each nonnegative integer \(n, g(n)=f(p n)=\) a perfect power of a prime number. This prime number has to be \(p,\) because by evaluating we see that \(g(n)=f(p n)\) is divisible by \(p\).
</p>


<p>(b)
Let \(g(x)=b_{n} x^{n}+b_{n-1} x^{n-1}+\cdots+b_{1} x+b_{0} .\) Then \(b_{0}=g(0)=p^{k} .\) Consider \(g\left(m p^{k+1}\right)=\)
\(b_{n}\left(m p^{k+1}\right)^{n}+b_{n-1}\left(m p^{k+1}\right)^{n-1}+\cdots+b_{1}\left(m p^{k+1}\right)+p^{k} .\) Clearly for each non-negative integer
\(m,\) this expression is divisible by \(p^{k},\) but not by \(p^{k+1}\) (since it is \(p^{k}\) modulo \(p^{k+1}\) ). This forces \(g\left(m p^{k+1}\right)=p^{k}\) for all \(m,\) since it must be a perfect power of \(p .\) Thus the polynomial \(g\) takes the value \(p^{k}\) infinitely often, so it must be identically equal to \(p^{k}\). (Otherwise the polynomial \(g(x)-p^{k}\) would have infinitely many roots.) To finish the problem, note that since \(g(x)=f(p x)\) is constant, \(f(x)\) must be constant by the same logic.
</p>


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


Sol.

<p> FTFT </p>

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


Sol.

<p>
(a) Define \(f(0)=0, f(1)=1\) and \(f(-1)=-1\). For every other real number \(x,\) arbitrarily equate \(f(x)\) to 0,-1 or 1. Any such function
satisfies the given condition.
</p>



<p>
If \(f\) is a polynomial, then we make two cases.<br>
</p>

<p>
(i) If \(f(x)=\) a constant \(c,\) then the given condition is equivalent to \(c=c^{2013},\) which happens precisely for three values of \(c,\) namely \(c=0,1,-1\) (since we have \(c\left(c^{2012}-1\right)=0,\) so \(c=0\) or \(c^{2012}=1\) ). Thus there are three constant functions with the given property.
</p>

<p>
(ii) If \(f(x)\) is a non-constant polynomial, then consider its range set \(A=\{f(x) \mid x \in \mathbb{R}\}\).
Now for all \(a \in A,\) we have by the given property \(f(a)=a^{2013}\).
So the polynomial \(f(x)-x^{2013}\) has all elements of \(A\) as its roots.
Since there are infinitely many values in \(A\) (e.g. applying the intermediate value theorem because \(f\) is continuous), the polynomial \(f(x)-x^{2013}\) has infinitely many roots and thus must be the zero polynomial, i.e., \(f(x)=x^{2013}\) for all real number \(x\).
</p>

---

### Polynomial division
{: .d-inline-block }

A8, 2014
{: .label}

<p>
(i) What is the remainder when \(f(x)=7 x^{32}+5 x^{22}+3 x^{12}+x^{2}\) is divided by \((x^{2}+1)\)?  <br><br>
(ii) What is the remainder when \(x f(x)\) is divided by \((x^{2}+1)\)?
</p>


Sol.

<p>
(i) \(4\)<br>
(ii) \(4x\)<br>
</p>




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



Sol.

<p>
(i) After expanding the powers of \((x-1),\) the degree \(n\) terms of \(f(x)\) and \(f(x-1)\) cancel out.  The degree \(n-1\) term from \(f(x)\)
cancels with the leading term of \(a_{n-1}(x-1)^{n-1}\). The only remaining term of degree \(n-1\) has to come from \(a_{n}(x-1)^{n}\).
So \(\Delta f(x)=n a_{n} x^{n-1}+\) lower degree \(x\) terms. This is similar to the derivative. <br><br>


(ii)  We use induction on the degree of \(f .\) If \(f(x)=a_{0}\) is constant, \(b_{0}=a_{0}\) works uniquely (base case).
<br>
<i> Inductive hypothesis. </i> Assume the result for polynomials of degree strictly less than \(n\) and let \(f\) be of degree \(n,\) so \(a_{n} \neq 0 .\) We are forced to take \(b_{n}=n ! a_{n}\) by comparing leading coefficients of \(f(x)\) and \(\sum_{i=0}^{n} b_{i} p_{i}(x) .\)
<br>
Now \(f(x)-b_{n} p_{n}(x)\) is a polynomial of degree \(d < n\) and hence by induction equals \(\sum_{i=0}^{d} b_{i} p_{i}(x)\) for unique \(b_{0}, \ldots, b_{d}\) Therefore \(f(x)=\sum_{i=0}^{n} b_{i} p_{i}(x),\) where \(b_{d+1}, \ldots, b_{n-1}\) are all \(0 .\) To see uniqueness of \(b_{i}^{\prime} s,\) let \(\sum_{i=0}^{n} b_{i} p_{i}(x)=\sum_{i=0}^{n} c_{i} p_{i}(x) .\) Subtract all terms with \(b_{i}=c_{i} .\) If any terms are remaining, compare the leading coefficients on each side to get a contradiction.
<br>
<br>


<i><b>Alternate solution</b>. If we are allowed to use linear algebra, it is a one-line proof.</i>
The \( p_i \)s form a basis for polynomial functions, so any polynomial has a unique representation.
<br><br>

(iii) Substitute \(x=0,1,2, \ldots\) one by one in the equation \(f(x)=\sum_{i=0}^{n} b_{i} p_{i}(x)\) and solve for \(b_{0}, b_{1}, b_{2}, \ldots\) successively. \(x=0\) gives \(b_{0}=f(0) .\) Using \(x=1\) and 2 gives \(b_{1}=f(1)-b_{0}\) \(b_{2}=f(2)-b_{0}-2 b_{1} .\) In general, for all integers \(t, p_{i}(t)=\left(\begin{array}{c}t \\ i\end{array}\right)\) is an integer. Further, \(p_{i}(t)=0\) if \(0 \leq t < i\) and 1 if \(t=i .\) So \(b_{t}=f(t)-\sum_{i=0}^{t-1} b_{i}\left(\begin{array}{c}t \\ i\end{array}\right),\) which is an integer by induction.
</p>

---


2015-q1
---

A4, 2015
{: .label}

<p>
Consider the polynomial \(p(x)=\left(x+a_{1}\right)\left(x+a_{2}\right) \cdots\left(x+a_{10}\right)\) where \(a_{i}\) is a real number for each \(i=1, \ldots, 10 .\) Suppose all of the eleven coefficients of \(p(x)\) are positive. For each of the following statements, decide if it is true or false. Write your answers as a sequence of four letters \((\mathrm{T} / \mathrm{F})\) in correct order.<br>

<ul>
<li>(i) The polynomial \(p(x)\) must have a global minimum. </li>
<li>(ii) Each \(a_{i}\) must be positive.</li>
<li>(iii) All real roots of \(p^{\prime}(x)\) must be negative.</li>
<li>(iv) All roots of \(p^{\prime}(x)\) must be real.</li>
</ul>


</p>

Sol.

All are true.

<p>
(i) The degree is even, so \(p(x)\) goes to \(+\infty\) as \(x \rightarrow \pm \infty .\) So \(p(x)\) must attain a global minimum somewhere by continuity.
</p>

<p>
(ii) The roots of \(p(x)\) are \(-a_{i}\) By positivity of coefficients of \(p(x),\) no nonnegative number is a root of \(p(x) .\) Thus all \(a_i\)s are positive.
</p>

<p>
(iii) and (iv)  All 10 roots of \(p(x)\) are real and negative. There is a root of \(p^{\prime}(x)\) between consecutive roots of \(p(x)\) (this is valid even in case of multiple roots). So all 9 roots of \(p^{\prime}(x)\) are real and negative as well. For negativity, one can also note that all coefficients of \(p^{\prime}(x)\) are positive and apply the logic in (ii) to \(p^{\prime}(x)\).
</p>


---

2015-q2
---

A7, 2015
{: .label}


<p>
(i) By the binomial theorem \((\sqrt{2}+1)^{10}=\sum_{i=0}^{10} C_{i}(\sqrt{2})^{i},\) where \(C_{i}\) are appropriate constants. Write the value of \(i\) for which \(C_{i}(\sqrt{2})^{i}\) is the largest among the 11 terms in this sum.
</p>

<p>
(ii) For every natural number \(n,\) let \((\sqrt{2}+1)^{n}=p_{n}+\sqrt{2} q_{n},\) where \(p_{n}\) and \(q_{n}\) are integers. Calculate \(\lim _{n \rightarrow \infty}\left(\frac{p_{n}}{q_{n}}\right)^{10}\).
</p>


Sol.

<p>
(i) \(i=6 .\) One way: simplify the ratio \(\frac{C_{i+1}(\sqrt{2})^{t+1}}{C_{i}(\sqrt{2})^{4}}\) and see that this ratio is \(>1\) till \(i=5\) and \(<1\) from \(i=6\) onwards.
</p>

<p>
(ii) 32.
Using binomial expansion see that \((\sqrt{2}-1)^{n}=\pm\left(p_{n}-\sqrt{2} q_{n}\right),\) where the sign depends on the parity of \(n .\) As \(n \rightarrow \infty,(\sqrt{2}-1)^{n} \rightarrow 0\) since \((\sqrt{2}-1)<1 .\) Thus \(\left(p_{n}-\sqrt{2} q_{n}\right) \rightarrow 0\) and so \(\frac{p_{n}}{q_{n}} \rightarrow \sqrt{2}\)<br>
</p>

---


2015-q3
---

B3, 2015
{: .label }

<p>
(a) Show that there are exactly 2 numbers \(a\) in \(\{2,3, \ldots, 9999\}\) for which \(a^{2}-a\) is divisible by \(10000 .\) Find these values of \(a\).
</p>

<p>
(b) Let \(n\) be a positive integer. For how many numbers \(a\) in \(\left\{2,3, \ldots, n^{2}-1\right\}\) is \(a^{2}-a\) divisible by \(n^{2} ?\) State your answer suitably in terms of \(n\) and justify.
</p>

Sol.

<p>
(a) We have \(10000=16 \times 625\) as product of prime powers. Recall the notation \(a \mid b,\) meaning \(b\) is divisible by a. We have \(10000 \mid a^{2}-a\) if and only if \((625 \mid a(a-1)\) and \(16 \mid a(a-1)) .\) Because \(a\) and \(a-1\) cannot share a factor, in turn this is equivalent to having both the conditions \((1) 625 \mid a\) or \(625 \mid a-1\) AND
(2) \(16 \mid a\) or \(16 \mid a-1 .\) Now if the coprime integers 16 and 625 both divide the same natural number (in our case \(a\) or \(a-1),\) their product 10000 will also divide this number. In our case this would force \(a=0,1,\) or \(\geq 10000,\) all of which are not allowed. Thus the given requirement on \(a\) is equivalent to having either (1) \(16 \mid a\) and \(625 \mid a-1\) OR
(2) \(16 \mid a-1\) and \(625 \mid\) a. Each case has a unique solution, respectively \(a=9376\) and \(a=625\) (e.g. use modular arithmetic:
in case \(1,\) we have \(a=625 k+1,\) which is \(k+1\) mod \(16,\) forcing \(k=15\) because \(16 \mid a\) and \(a \in\{2,3, \ldots, 9999\})\)
</p>

<p>
(b) Let \(n=p_{1}{ }^{e_{1}} \ldots p_{k}{ }^{e_{k}}\) be the factorization of \(n\) into powers of distinct primes. The analysis in part (a) tells that required values of \(a\) are obtained as follows: write \(n^{2}=x y\) as a product of two coprime integers and find values of \(a\) in \(\left\{2,3, \ldots, n^{2}-1\right\}\) that are simultaneously 0 mod \(x\) and 1 mod \(y\). These are precisely the values of \(a\) that we want. This is because each \(p_{i}^{2 e_{i}}\) must divide \(a\) or \(a-1,\) as \(a\) and \(a-1\) are coprime.


Now the Chinese remainder theorem tells you that there is always an \(a\) that is 0 mod \(x\) and 1 mod \(y\). Moreover it is unique modulo \(x y=n^{2}\) because difference between any two solutions would be divisible by \(x y\).

The total number of ways to write \(n^{2}=x y\) as a product of coprime integers is exactly \(2^{k}\) as it amounts to choosing which of the \(k\) distinct primes to include in \(x\) and then the rest go into \(y\). (Notice that \(x\) and \(y\) are not interchangeable.) However, we have to delete the two cases \(x=1, y=n^{2}\) and \(y=1, x=n^{2},\) as these will respectively lead to solutions \(a=1\) and \(a=0\) or \(n^{2},\) which are not in \(\left\{2,3, \ldots, n^{2}-1\right\} .\) Finally it is easy to see that different choices of \(x\) lead to different values of \(a\). This is because, of the primes \(p_{1}, \ldots, p_{k}\) in the factorization of \(n,\) precisely the ones dividing \(x\) will divide \(a\) and the remaining primes will not, because they divide \(a-1\).

Thus the final answer is \(2^{k}-2 .\) Note that this matches with the special case in part (a). Finally, note that there was nothing special about taking a square: instead of \(n^{2}\) it could be any positive integer \(m\) and we would proceed the same way to find requisite integers \(a\) in \(\{2,3 \ldots, m-1\}\) based on prime factorization of \(m\)
</p>

---



2015-q4
---

B5, 2015
{: .label}


<p>For an arbitrary integer \(n,\) let \(g(n)\) be the \(G C D\) of \(2 n+9\) and \(6 n^{2}+11 n-2 .\) What is the largest positive integer that can be obtained as the value of \(g(n) ?\) If \(g(n)\) can be arbitrarily large, state so explicitly and prove it.
</p>

Sol.
<p>
Long division gives \(6 n^{2}+11 n-2=(2 n+9)(3 n-8)+70 .\) By Euclidean algorithm, \(G C D\left(6 n^{2}+11 n-2,2 n+9\right)=G C D(2 n+9,70) .\) Thus \(g(n)\) divides \(70 .\) But since \(g(n)\) divides \(2 n+9,\) which is odd, \(g(n)\) divides \(35 .\) When \(n=13,2 n+9=35\) and hence \(g(13)=35 .\) Thus the maximum value of \(g(n)\) is \(35 .\)
</p>

---

2016-q1
---

A2, 2016
{: .label}


<p>
A country's GDP grew by \(7.8 \%\) within a period. During the same period the country's per-capita-GDP (= ratio of GDP to the total population) increased by 10\%. During this period, the total population of the country increased/decreased by correct option and fill in the blank if possible.)
</p>

Sol.

<p>
Per-capita GDP is \(\frac{\text { GDP }}{\text { population }}\). Letting \(G\) and \(P\) denote the old GDP and population respectively, the new per-capita GDP is \(\frac{1.078 G}{(1+x) P}\) where \(x\) is the unknown percent change in population we wish to calculate. The percent increase in per-capita GDP is \(10 \%=0.1\) So we have \(\frac{1.078}{1+x}=1.1 .\) Solving for \(x\) we get \(1+x=\frac{1.078}{1.1}=\frac{98 \times 11}{100 \times 11}=0.98 .\) So \(x\) is -0.02 So population decreased by \(2 \%\)
</p>

---


2016-q2
---

A8, 2016
{: .label}


<p>
A function \(g\) satisfies the property that \(g(k)=3 k+5\) for each of the 15 integer values of \(k \operatorname{in}[1,15]\)
<ul>
<li>(i) If \(g(x)\) is a linear polynomial, then \(g(x)=3 x+5\)</li>
<li>(ii) \(g\) cannot be a polynomial of degree 10.</li>
<li>(iii) \(g\) cannot be a polynomial of degree 20.</li>
<li>(iv) If \(q\) is differentiable, then \(g\) must be a polynomial.</li>
</ul>
</p>


Sol.

<p>
TTFF<br>

If \(g(x)\) is linear, it is \(3 x+5\) because the values at 1 and 2 are 8 and 11 respectively. If \(g(x)\) is a polynomial then it is \(3 x+5\) plus a multiple of \((x-1)(x-2) \cdots(x-15) .\) So \(g(x)\) cannot be a polynomial of degree \(10 .\) But it can be a polynomial of degree 15 or more. \(g\) being differentiable does not mean that it is a polynomial. You can fit any number of differentiable functions to the given data.
</p>

---


2016-q3
---

B5, 2016
{: .label}


<p>Find a polynomial \(p(x)\) that simultaneously has both the following properties.
(i) When \(p(x)\) is divided by \(x^{100}\) the remainder is the constant polynomial 1.<br>
(ii) When \(p(x)\) is divided by \((x-2)^{3}\) the remainder is the constant polynomial 2.<br>
</p>


Sol.

<p>
Suppose a polynomial \(f(x)\) leaves a constant remainder \(r\) when divided by the polynomial \((x-c)^{k}\).
Then \(f^{\prime}(x)\) is divisible by \((x-c)^{k-1}\).
The converse is also true: suppose for a polynomial \(f(x),\) the derivative \(f^{\prime}(x)\) is divisible by \((x-c)^{k-1},\) say \(f^{\prime}(x)=q(x)(x-c)^{k-1}\).
Then \(f(x)\) leaves a constant remainder when divided by \((x-c)^{k}\). One can see this, for example, by substituting \(u=(x-c)\) in \(q(x)(x-c)^{k-1}\) and integrating.
</p>

<p>
In the given problem \(p^{\prime}(x)\) must be divisible by \(x^{99}\) as well as by \((x-2)^{2} .\) Moreover any polynomial whose derivative is divisible by \(x^{99}(x-2)^{2}\) will leave constant remainders when divided by either of \(x^{100}\) and \((x-2)^{3}\). The simplest way to find one such \(p(x)\) is to integrate \(A x^{99}(x-2)^{2}=A\left(x^{101}-4 x^{100}+4 x^{99}\right)\) to get

\[ p(x)=A\left(\frac{x^{102}}{102}-\frac{4 x^{101}}{101}+\frac{4 x^{100}}{100}\right)+B \]

and solve for constants \(A\) and \(B\) to ensure desired values of the constant remainders. We have \(p(0)=B=1\) and \(p(2)=A\left(\frac{2^{102}}{102}-\frac{4 \times 2^{101}}{101}+\frac{4 \times 2^{100}}{100}\right)+1=2,\) which gives \(A\)
</p>

<br>
<br>


<p>
(ii) Theoretical approach. Working through the following reasoning will be very useful for your understanding of basic arithmetic/algebra.
It explains how to implememt the Chinese remainder theorem using the Euclidean algorithm for finding GCD. This theorem states the following. One can always find an integer that leaves desired remainders when divided by two coprime integers a and b.
Suppose we are required to find an integer that leaves remainder \(r\) when divided by a and remainder \(s\) when divided by \(b\). A way to achieve this systematically is to use the Euclidean algorithm, which finds GCD of two numbers by repeated division with remainder. This algorithm also enables one to write the GCD in the form \(x a+y b,\) where the integers \(x, y\) can be found explicitly by backward substitution in the steps used to calculate the GCD. If \(a\) and \(b\) are coprime, i.e. if their GCD is \(1,\) then we can write \(1=x a+y b . \quad\) This tells you that \(x a\) is 1 modulo \(b\) and \(y b\) is 1 modulo a. Therefore,
s.xa \(+r y b\) is \(r\) modulo \(a\) and \(s\) modulo \(b\)
The relevance for this problem is that the same reasoning applies for polynomials in one variable, because in this setting too one has division with remainder. Because \(x^{100}\) and \((x-2)^{3}\) do not share a common factor, you know without any work that a polynomial with given properties must exist. The same algorithm as the previous paragraph (but now with polynomials) gives a systematic way to find it. In the given problem we could use a different trick because the specified remainders here were rather simple (constants). But there is a conceptual way as well by implementing the Chinese remainder theorem.
</p>

---


2017-q1
---

A8, 2017
{: .label}


<p>
For this question write your answers as a series of four letters (Y for Yes and N for No) in order. Is it possible to find a \(2 \times 2\) matrix \(M\) for which the equation \(M \vec{x}=\vec{p}\) has:
<li>(a) no solutions for some but not all \(\vec{p}\); exactly one solution for all other \(\vec{p} ?\)</li>
<li>(b) exactly one solution for some but not all \(\vec{p} ;\) more than one solution for all other \(\vec{p} ?\)</li>
<li>(c) no solutions for some but not all \(\vec{p}\); more than one solution for all other \(\vec{p} ?\)</li>
<li>(d) no solutions for some \(\vec{p},\) exactly one solution for some \(\vec{p}\) and more than one solution for some \(\vec{p} ?\)</li>
</p>


Sol.


<p>If \(M\) has nonzero determinant, then for any \(\vec{p},\) we see that \(M \vec{x}=\vec{p}\) has the unique solution \(\vec{x}=M^{-1} \vec{p} .\) If determinant of \(M\) is zero then we can make two cases. (i) If \(M\) is the zero matrix, then \(M \vec{x}=\vec{p}\) has infinitely many solutions for \(\vec{p}=\overrightarrow{0}\) and no solutions otherwise. (ii) If \(M\) is nonzero then it is easy to see that we are solving two equations in two variables whose left hand sides are proportional. So if the two right hand constants that make up \(\vec{p}\) are in the same proportion, then we will have infinitely many solutions (because one of the variables can be arbitrary). If the constants are not in the same proportion, then the two equations will be inconsistent and we will have no solutions. Thus the answer is NNYN. It is also possible to think geometrically in terms of (at most) two lines, each moving in a parallel family. If the lines have the same slope they either coincide or don't intersect. Otherwise they have a unique point of intersection.
Note: In general linear algebra gives the right tools to analyze matrix equations, e.g. in this problem we can say the following. If \(M=0\) then the space of solutions is either empty or two-dimensional. If \(M \neq 0\) then either there is a unique solution (precisely when determinant \(\neq 0\) ) or, when determinant is \(0,\) the space of solutions is either empty or one-dimensional. For larger matrices the possibilities are more complicated, but they can be described precisely using the language provided by linear algebra.
</p>

---



2017-q2
---

A9, 2017
{: .label}

<p>
Let \(f\) be a continuous function from \(\mathbb{R}\) to \(\mathbb{R}\) (where \(\mathbb{R}\) is the set of all real numbers) that satisfies the following property: For every natural number \(n\)
\(f(n)=\) the smallest prime factor of \(n\)
For example, \(f(12)=2, f(105)=3 .\) Calculate the following.
(a) \(\lim_{x \rightarrow \infty} f(x)\)
(b) The number of solutions to the equation \(f(x)=2016\)
</p>

Sol.

<p>
\(f(x)\) will take value 2 for all even \(x\). At the same time, primes provide an increasing infinite sequence of positive integers for which \(f(x)=x .\) Thus \(\lim_{x \rightarrow \infty} f(x)\) does not exist. By intermediate value theorem, for each prime \(p>2016\) there is an \(x\) between \(p\) and \(p+1\) such that \(f(x)=2016\)
</p>


---



2018-q1
---

A3, 2018
{: .label }

<p>List every solution of the following equation.
\[ \sqrt[3]{x+4}-\sqrt[3]{x}=1 \]
</p>

Sol.

<p>
Put \(t=\sqrt[3]{x},\) to get \(\left(t^{3}+4\right)=(1+t)^{3}\). This leads to the quadratic \(t^{2}+t-1=0\) Solve it a nd then take the cube root of the solutions, The answer s a re \(-2 \pm \sqrt{5}\).
</p>

---



2018-q2
---

A5, 2018
{: .label}

<p>List in increasing order all positive integers \(n \leq 40\) such that \(n\) cannot be written in the form \(a^{2}-b^{2},\) where \(a\) and \(b\) are positive integers.
</p>


Sol.

<p> 1,4 and all even number s of the form \(4 k+2\).</p>

---



2018-q2a
---


B2a, 2018
{: .label}


<p>
Find all real solutions of the equation:

\[ \left(x^{2}-2 x\right)^{x^{2}+x-6}=1 \]

Explain why your solutions are the only solutions.
</p>


Sol.

<p>
\(x=-3,1,1 \pm \sqrt{2}\) are the only solutions. First, we want either \(x^{2}+x-6=0\) or \(x^{2}-2 x=1\). However, when \(x=2\) the base as well as the expo ne nt are 0 g in ing us an indeter minate for \(\mathrm{m}\). He noe \(x=2\) w ill not work Moreover, when \(x=-3\) the base is positive. Second, observe that wher \(x=1\) we get \((-1)^{-4}\) which equals 1
</p>

---


2018-q2b
---

B2b, 2018
{: .label}


<p>
The following expression is an integer. Find its value.

\[\sqrt[3]{6 \sqrt{3}+10}-\sqrt[3]{6 \sqrt{3}-10} \]

</p>

Sol.

<p>
The expression evaluates to 2.  Let the numbers be \(a, b\) respectively.  Note \(a^{3}-b^{3}=20\) and \(a b=2 .\) Putting it in \((a-b)^{3}\) we get \((a-b)^{3}=20-6(a-b)\).
This cubic has one real solution \(a-b=2\) and two complex solutions.
</p>


---



2018-q3
---

A9, 2018
{: .label}


<p>
Consider a sequence of polynomials with real coefficients defined by
\[
\begin{array}{c}
p_{0}(x)=\left(x^{2}+1\right)\left(x^{2}+2\right) \cdots\left(x^{2}+1009\right) \\
2
\end{array}
\]

with subsequent polynomials defined by \(p_{k+1}(x):=p_{k}(x+1)-p_{k}(x)\) for \(k \geq 0 .\) Find the least \(n\) such that
\[ p_{n}(1)=p_{n}(2)=\cdots=p_{n}(5000) \]

</p>

Sol.

<p>
\(n=2018\). Note that \(\operatorname{deg} p_{0}(x)=2018\) and \(\operatorname{deg} p_{k}(x)=2018-k\).
Define \(g_{n}(x)=p_{n}(x)-p_{n}(1)\), hence \(g_{n}(x)\) has degree \(2018-n\) and 5000 roots \(s\).
</p>

---





2019-q1
---


B5, 2019
{: .label}


<p>
Three positive real numbers \(x, y, z\) satisfy
\[
\begin{array}{r}
x^{2}+y^{2}=3^{2} \\
y^{2}+y z+z^{2}=4^{2} \\
x^{2}+\sqrt{3} x z+z^{2}=5^{2}
\end{array}
\]
Find the value of \(2 x y+x z+\sqrt{3} y z .\)
</p>


Sol.

<p>

Consider the right ang led triangle \(A B C\) with sides 3,4,5 and an interior point \(O\) such that \(A O=x, \angle A O B=90\) and \(C O=z, \angle C O A=150\) and \(B O=\) \(y, \angle B O C=120\). Then the three given equations are in fact cosine rule for ea ch of the triangle prescribed above. For example, in \(\Delta B O C\) we have

\[
\begin{aligned}
4^{2} &=y^{2}+z^{2}-2 y z \cos (120) \\
&=y^{2}+z^{2}+y z
\end{aligned}
\]

The area of \(\delta ABC\) (which is 6) calculated using the sine formula (for each of the smaller triangle)
gives us \[ 6=\frac{1}{2} x y+\frac{1}{2} y z \sin 60+\frac{1}{2} \sin 30 \]. So the answer is 24.


</p>





