---
layout: default
title: Home
nav_order: 1
description: "In-depth solutions to all CMI entrance exam questions."
permalink: /
last_modified_date: 2020-04-27T17:54:08+0000

---


# CMI Tomato

This website is for class XI and XII students who wish to pursue B.Sc. at Chennai Mathematical Institute.<br>

**Disclaimer.** This is an unofficial resource and is not affiliated to CMI.
{: .fs-3 .bg-grey-lt-000 .text-gray-004 }

---

#### Announcement
{: .fs-4}

- Congrats to everybody to made it to CMI!


---



## Problems from CMI 2022 paper [Work in progress]


### Part A: Screening part

<ol>

<li>
Suppose \( a_0, a_1, a_2, \ldots, \) is an arithmetic progression such that \(a_0\) and \(a_1\) are positive integers. 
Suppose \( g_0, g_1, a_2, \ldots, \) is a geometric progression such that \(g_0=a_0\) and \(g_1=a_1\). Which of the following are true?

<ol>
<li> \( a_5^2 \geq a_0a_{10}\) </li><br>
<li> The number \( a_0 + a_1 + \cdots + a_{10}\) is divisible by \(a_5\).</li><br>
<li> If \( \sum_{i=0}^{\infty} a_i \) tends to \( \infty \) then \( \sum_{i=0}^{\infty} g_i \) tends to \(\infty\).</li><br>
<li> If \( \sum_{i=0}^{\infty} g_i \) is finite then \( \sum_{i=0}^{\infty} a_i \) tends to \(-\infty\).</li><br>
</ol>
</li>


<details open><summary>Sol.</summary>
<ol>
<li> TRUE. \(a_5^2 \geq a_0 \cdot a_{10} \implies 25d^2 \geq 0\) which is true.</li>
<li> TRUE. \(a_0 + 5d \; | \; 11(a + 5d)\)</li>
<li> TRUE.  AP has a common difference of \(d>0\), the common ratio of GP is >1.</li>
<li> TRUE. gp is finite then common ratio \(<1\) so \(a_1/a_0 < 1\) so \(d/a_0\) is negative so \(d\) is negative so AP sum goes to -inf.</li>
</ol>
</details>





<li>
\(A\) and \(B\) are probability events such that \( P(A) \) and \(P(B)\) is strictly between 0 and 1. We say that the events
are <i>mutually exclusive</i> if \( P(A\cap B) = 0 \).  We say the events \(A\) and \(B\) are exhaustive if \(P(A\cup B)=1\).
Let \(A^c\) denote the complement of \(A\).  <br>

<ol>
<li>\(A\) and \(B\) are mutually exclusive if and only if \(A^c\) and \(B^c\) are exhaustive.</li>
<li>\(A\) and \(B\) are independent if and only if \(A^c\) and \(B^c\) are independent.</li>
<li>\(A\) and \(B\) cannot be simultaneously independent and exhaustive.</li>
<li>\(A\) and \(B\) cannot be simultaneously mutually exclusive and exhaustive.</li>
</ol>
</li>


<details open><summary>Sol.</summary>
<ol>
<li> TRUE. \(A \cap B = \phi \iff A^c \cup B^c = S \) </li>
<li> TRUE. If \(A\) and \(B\) are independent, then \(P(A\cap B) = P(A) \cdot P(B) \implies P(A^c \cap b^c) = P[(A \cup B)^c] = P(A^c) P(B^c)\).</li>
<li> TRUE. Exhaustive means \(P(A \cup B)=1\). We have \(P(A \cup B) = P(A) + P(B) - P(A \cap B) = 1 - (1-P(A))(1-P(B)) < 1\). Hence A and B cannot be both exhaustive and independent.</li>
<li> FALSE. \(A, B\) can be both mutually exclusive and exhaustive. Eg \(\{H\}\) and \(\{T\}\) are mutually exclusive and exhaustive for a coin toss.</li>
</ol>
</details>






<li>
Suppose we have a matrix \(A\) as defined below. Which of the following are true?
\[ A = \begin{bmatrix} 1 & 2 & 3 \\ 10 & 20 & 30 \\ 11 & 22 & k \end{bmatrix} \]

<ol>
<li>\(A\) is not invertible regardless of the value of \(k\).</li>
<li>There exists a unique \(k\) such that the determinant of \(A\) is zero.</li>
<li>The set of solutions \( \vec{v}=(x,y,z) \) to \(A\vec{v}=0\) is either a plane or a line passing through the origin.</li>
<li>If \(A\vec{v}=[p\;\; q\;\; r]^{\top}\) has a solution, then \(q=10p\).</li>
</ol>

</li>


<details open><summary>Sol.</summary>
<li> TRUE. As the first two rows are multiples of one another, det(A)=0 regardless of k.</li>
<li> FALSE. Because A is true.</li>
<li> TRUE. \(A\vec{v} = 0\). If \(k=33\), then we would get only one equation :- \(x+2y=3\) means plane passing through origin. If \(k \neq 33\), we get two distinct equations: \(x+2y+z=0\) and \(11x+22y+kz=0\) now combine to give equation of a line via origin.   </li>
<li> TRUE.</li>
</details>




<li>
Consider the three statements about a function defined on \( [0,1]\). <br>
(I) \(f\) is differentiable on \( [0,1] \).<br>
(II) \(f\) is continuous on \( [0,1] \).<br>
(III) \(f\) attains it maximum and minimum in \( [0,1] \).<br>
Pick the correct statements.<br>

<ol>
<li> (I) implies (II).</li>
<li> (II) implies (III).</li>
<li> not (III) implies not (I).</li>
<li> No two of the three statements are equivalent to one another.</li>
</ol>


</li>


<details open><summary>Sol.</summary>
<li> TRUE.  At every point $f'(x)$ exists so right and left hand continuous. </li>
<li> TRUE.  It is basically a trivial sorta theorem that every continuous function chives max min in a closed interval.</li>
<li> TRUE.  if not max min then it is not differentiable.</li>
<li> TRUE. I implies II but II doesn't imply I, I implies III but  III doesn't imply I, II implies III but III doesn't imply  II.</li>
</details>




<li>
Which of these are true?
<ol>
<li> \(a = 1/\ln 3 \implies 3^a = e \).</li>
<li> \( \sin(0.02) < 2\sin(0.01) \).</li>
<li> \( \arctan(0.01) > 0.01 \).</li>
<li> \( 4 \int_{0}^1 \arctan x \, dx = \pi - \ln 4 \).</li>
</ol>
</li>




<details open><summary>Sol.</summary>
<li> TRUE. \(log_{e}3 = 1/a \implies e^{1/a} = 3 \implies 3^a = e\)</li>
<li> TRUE. Can solve this problem by using the on-screen calculator. Alternatively, you may use Taylor expansion.</li>
<li> FALSE.  </li>
<li> TRUE. </li>
</details>




<li>
Which of the options are true about the function \(f\) as defined below:
\[ f(x) = \frac{1}{|\ln x|} \left( \frac{1}{x} + \cos x  \right) \] 
<ol>
<li> As \(x\rightarrow \infty\), the sign of \(f\) changes infinitely many times.</li>
<li> \(\lim_{x\rightarrow \infty} f(x) \) does not exist.</li>
<li> \(\lim_{x\rightarrow 1} f(x) = \infty \).</li>
<li> \(\lim_{x\rightarrow 0^+} f(x) = 1\).</li>
</ol>
</li>





<li>
Let \(f_0(x) = x\),\(f_1(x)=x^x\),\(f_2(x) = x^{x^x}\), etc. For \(x>0\) which of the following options are true?
<ol>
<li> \(\lim_{x\rightarrow 0^+} f_1(x) = 1\)</li>
<li> \(\lim_{x\rightarrow 0^+} f_2(x) = 1\)</li>
<li> \( \int_0^{1} f_3 dx = 1  \)</li>
<li> \( f_{123}^\prime(1) = 1  \)</li>
</ol>
</li>


<li>
Let \(N=\{1,2,\ldots,9\}\) and \(L=\{a,b,c\}\).
<ol>
<li> \(L \cup N\) is arranged on a line with the letters appearing consecutively (in any order). The number of such arrangements are less than \(10!\times 5\).</li>
<li>More than half of the functions from \(N\) to \(L\) have \(b\) in their range.</li>
<li>The number of one-to-one functions from \(L\) to \(N\) is less than 512.</li>
<li>The number of functions \(N\) to \(L\) that do not map consecutive numbers to consecutive letters is greater than 512.</li>
</ol>
</li>


<li> Let \(z\) be a non-real complex number and \(f(z) = z^{222} + \frac{1}{z^{222}}\). Which of the statements are correct?<br>
<ol>
<li>If \(|z|=1\), then \(f(z)\) must be real.</li>
<li>If \(z+1/z=1\), then \(f(z)=2\).</li>
<li>If \(z+1/z\) is real, then \(|f(z)|\leq 2\).</li>
<li>If \(f(z)\) is real, then \(f(z)>0\).</li>
</ol>
</li>


<li>
Let \(P\) denote some arrangement of the numbers \({1,2,\ldots,n}\). A <i>move</i> on \(P\) consists of exchanging the position of element 1 with
the position of another element. For example, if \(P=[3,1,4,2]\), then by making one move we can get either \(P=[1,3,4,2]\), \(P=[3,4,1,2]\) or \(P=[3,2,4,1]\).
\(P\) is said to be <i>sorted</i> if the numbers are in increasing order. Which of the statements are true?<br>

<ol>
<li>The arrangement \([9, 1, 2, 3, 4, 5, 6, 7, 8]\) can be sorted in 8 moves and no fewer.</li>
<li>\( [1, 3, 4, 5, 6, 7, 8, 9, 2]\) can be sorted in 8 moves and no fewer. </li>
<li>\( [1, 3, 4, 2, 9, 5, 6, 7, 8] \) cannot be sorted by any number of moves.</li>
<li>There exists an arrangement of 99 numbers, i.e. 1 to 99, that cannot be sorted by any number of moves.</li>
</ol>
</li>



</ol>



### Part B: Subjective questions


<p>

<b>B1</b>. Consider the figure shown below (not drawn to scale). We have the following relation:
\[ \frac{WZ}{YX} = \frac{PW}{XP} = \frac{QZ}{YQ} = k \]

Prove that \( XR = XP \).

<p style="text-align:center">
<img src="/assets/images/cmi2022_b1.png"/>
</p>


</p>

---

<p>
<b>B2</b>. <i>This question was straight from a previous <a href="/docs/mock_test/001_feb_7_nt_trig/">CMI Tomato's mock test</a>!</i><br>

(i) Consider a coordinate grid made up of horizontal and vertical lines of the form \(x=k\) and \(y=k\), where \(k\in \mathbb{Z}\).
Consider a line segment OA where O is the origin and A is the point \(  (10,4) \). Notice that this line segment passes through the
interior of 12 cells. In the figure below, the shaded cells are the ones through which the line passes.
</p>

<p style="text-align:center">
<img src="/assets/images/mt_1_grid.jpg"/>
</p>

<p>
In general, how many cells does the line from the origin to \( (m,n) \) pass through? Assume that \(m\) and \(n\) are positive integers.<br>

(ii) Consider all the cells in the square region from \( (0,0) \)  to \( (n,n) \). What is the maximum number of cells any line can pass through in this region? This line 
need not pass through any integer points.
</p>


---

<p><b>B3.</b> Let \(f(x) = 1 + x + x^2 + \cdots + x^n\). Find the local minima of \(f(x)\). Find the local maxima of \(f(x)\). For each local maxima or minima \( (c,f(c)) \),
find the integer \(k\) such that \( k\leq c < k+1 \). <br>
</p>

<p>
Hint: Use the definition of \(f\) as well as the closed formula. Treat \(x\geq 0\) and \(x<0\) separately.
</p>

---

<p> <b>B4.</b> For a function \( f:\mathbb{R}^+ \rightarrow \mathbb{R}^+\), define \(A_r\) and \(B_r\) as follows:

\[ A_r := \int_{1}^{r} f(x)\, dx \;\;\;\;\; B_r := \int_{r}^{r^2} f(x)\, dx \]

Find all continuous functions \( f:\mathbb{R}^+\rightarrow\mathbb{R}^+ \) for which \(A_r=B_r\) for every positive \(r\).<br>
Hint: Find an equation relating \(f(x)\) with \(f(x^2)\). Then consider the function \(xf(x)\).

</p>

---
<p>
<b>B5.</b> 

A pair of distinct real numbers \((r, s)\) is considered to be a good pair if
\[ r^{3}+s^{2}=s^{3}+r^{2} \]
(i) Find a good pair \((a, l)\) such that \(l\) takes the maximum value possible. <br>
 Find a good pair \( (s,b) \) such that \(s\) takes the minimum value possible.<br>
 For any good pair \( (c, d) \), other than the ones found above, show that there exists another real number \(e\) such that \( (c, e) \) and \( (d, e) \) are both good pairs.<br>
(ii) Prove that there are infinitely many rational good pairs.<br>
</p>

<p>
Hints: Consider the function \(f=x^3-x^2\). <br>
(i) For a good pair \( (r,s) \), can you write \(s\) in terms of \(r\)?<br>
(ii) You can use the fact that there are infinitely many right-angle triangles with integer sides that are not similar to each other.<br> 
</p>

---

<p>
<b>B6.</b> Let \(p\) denote a prime number in this question.<br>
(i) Show that \(x^2+x-1\) has at most two roots \( \pmod{p} \). In other words show that the cardinality of the set \(S\) (defined below) is at most two.
\[ S = \{ n\in \mathbb{N} |  \;\;\; 1\leq n \leq p, \;\; s.t. \;\;\; p|n^2+n-1  \}  \]
Also, find all the primes \(p\) for which the cardinality of \(S\) is one.<br>
(ii) Find all \(n\leq 121\) such that \(n^2+n-1\) is divisible by \(121\).<br>
(iii) What can we say about the roots of \(x^2+x-1\) \(\pmod{p^2}\)?
</p>



---

#### What's on this site?
{: .fs-4}

- In-depth solutions to previous CMI entrance exam questions. This includes questions from 2010 and 2011 for which official solutions are not given.

- Topic-wise classification of all problems ordered by increasing difficulty. This helps you to specialize in a topic.

{: .fs-4 .fw-300 }



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
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#rationality-preserving-operations';" onmouseover = "display('A11_2010')"></button>
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
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#irrational-fraction';" onmouseover = "display('A3_2012')"></button>
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
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#summations';" onmouseover = "display('A1_2014')"></button>
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
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#a-polynomial-integer';" onmouseover = "display('B2_2014')"></button>
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
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#counting-students';" onmouseover = "display('A1_2020')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#vector-perpendicular-to-a-plane';" onmouseover = "display('A2_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#absolute-integrals-ii';" onmouseover = "display('A3_2020')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#yet-another-dice-roll';" onmouseover = "display('A4_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#asymptotes';" onmouseover = "display('A5_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#concave-function';" onmouseover = "display('A6_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#guess-the-polynomial';" onmouseover = "display('A7_2020')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#number-of-divisors-ii';" onmouseover = "display('A8_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#binomial-polynomial';" onmouseover = "display('A9_2020')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#chinese-remainder-theorem';" onmouseover = "display('A10_2020')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#cyclic-trapezoids';" onmouseover = "display('B1_2020')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#complex-polygon';" onmouseover = "display('B2_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#spider-walk';" onmouseover = "display('B3_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#constrained-function';" onmouseover = "display('B4_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#dependent-roots';" onmouseover = "display('B5_2020')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#counting-relations';" onmouseover = "display('B6_2020')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#monotonic-functions';" onmouseover = "display('A1_2021')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#divisibility-tests';" onmouseover = "display('A2_2021')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#possible-triangles';" onmouseover = "display('A3_2021')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#integer-cubic-polynomial';" onmouseover = "display('A4_2021')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#set-of-powers';" onmouseover = "display('A5_2021')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#stationary-points';" onmouseover = "display('A6_2021')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#two-equations';" onmouseover = "display('A7_2021')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#cross-product-of-vectors';" onmouseover = "display('A8_2021')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#simple-limits';" onmouseover = "display('A9_2021')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#three-arctans';" onmouseover = "display('A10_2021')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/functions/#composition';" onmouseover = "display('B1_2021')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#coin-toss-and-a-dice-roll';" onmouseover = "display('B2_2021')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#principle-of-inclusion-exclusion';" onmouseover = "display('B3_2021')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#impossible-polynomial';" onmouseover = "display('B4_2021')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#convergence-of-an-improper-integral';" onmouseover = "display('B5_2021')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#two-player-card-game';" onmouseover = "display('B6_2021')"></button>
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

The cutoff has been around 40% for the objective section and 40-50% overall. The objective section is used for screening.<br>

CMI does not publish the cutoff marks but they have responded to individual requests in the past.
The scores shown below were shared by former students who were privy to this data.
<br>

<!--
[Subhayan Saha](https://www.quora.com/profile/Subhayan-Saha)
-->

### 2021 cutoff marks

In 2021, CMI used an unconventional criteria for admission. The cut-off for  Part A was 17/40 for everyone. More
weightage was given to Part B marks. In the general category with scholarship, students were admitted if they had >=61 marks in total
or if they had 39 or more marks in Part B. So, a student who got 17 marks in Part A and 39 marks in Part B was still admitted with scholarship. But
a student with 22 marks in Part A and 38 marks in Part B was NOT admitted in that category.


Type | General |  Reserved
-----|------|----
With scholarship| 61/100 or 39/60 in Part B | 57/100 or 35/60 in Part B
Without scholarship| 56/100 or 30/60 in Part B | 50/100 or 28/60 in Part B


There was no waiting list.

### 2020 cutoff marks

The cutoff marks for the year 2020 are given below. The marks are out of 94 instead of 100 since one question had a mistake.

Type | General |  Reserved
-----|------|----
With scholarship| 54/94 | 44/94
Without scholarship| 48/94 | 40/94
Waiting list| 45/94 | 38/94


The cutoff marks for the previous years are given below.




| Year | Objective (40 marks) | Overall | Vetted by
|---|--|--|
2016 | 14 | 62/124 | Sayantani Bhattacharya [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/Why-there-is-no-interview-for-cmi-bsc-this-year)
2017 | 15 | 60/125 | Abhiroop Sanyal
2018 | 15 | 50/125 |  -
2019 | &sim;16 | 52/100  | Ankush Agarwal
2020 | &sim;16 | 48/94  | CMI Office
2021 | 17 | 56/100  | CMI Office




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
2016 | 4000 | 90 | 44
2017 | 4000 | 90 | 45
2018 | 5000 | 95 | 48
2019 | 5500 | 100 | 61

---


## Paperback
<br>

<img src="/assets/images/cmi_tomato_cover.jpg" style="float:left;margin-right:20px;margin-top:0px;border-radius:1%"/>


The book contains the problems and solutions from the years 2010-2021.

<a href="https://www.amazon.in/CMI-Tomato-Balasundar-M/dp/1685541429/">Buy the paperback on Amazon</a>.

<!--
The content of this website is available as an e-book in PDF format. You will have a permanent copy of the solutions which may be handy just in case the site
goes down.
{: .fs-4 .fw-300 }
<a href="https://gum.co/kBekW">Buy the e-book on Gumroad</a>
-->

<br><br>
<br><br>
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



The contents of this website are hosted in accordance with principles of [fair use](https://www.copyright.gov/fair-use/index.html).
You agree to email me about any possible infringement of copyright law before taking legal action.
{: .fs-3 .fw-300 }

<!--
M. Balasundar is a participant in the Amazon Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to amazon.in.
{: .fs-3 .fw-300 }
-->




