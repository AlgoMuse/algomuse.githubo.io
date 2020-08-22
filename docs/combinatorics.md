---
layout: default
title: Combinatorics
nav_order: 7
---


# Combinatorics


### Serendipitous sum
{:b .d-inline-block}

B4, 2011
{: .label}

<p>
Let S be the set of all 5-digit numbers that contain the digits 1,3,5,7 and 9 exactly once (in usual base 10 representation).
Show that the sum of all elements of S is divisible by 11111. Find this sum.
</p>


<details><summary>Solution</summary>

<p>
Each number appears in the \(i\)th place exactly \(4!\) times for
\(i\in {1,\ldots,5}\). So the sum of numbers corresponding to each place is

<br>

\[ 4!(1+3+5+7+9) = 4!\times 25 = 600 \]

<br>
The total sum is therefore:

<br>

\[ 10^4\cdot 600 + 10^3\cdot 600 + 10^2\cdot 600 + 10^1\cdot 600 + 600 = 6666600 \]

</p>

</details>

---


### Sum of a finite series
{: .d-inline-block}


A4, 2019
{: .label}


<p>
The sum \( S = 1 + 111 + 11111 + \cdots + \underbrace{11 \cdots 1}_{2k+1} \)
</p>

<details><summary>Solution</summary>


<p>

\begin{align}
9S &= 9 + 999 + 99999 + \cdots + \underbrace{99 \cdots 9}_{2k+1} \\
&= (10-1) + (1000-1) + \cdots + (100^{2k+1}-1) \\
&= \frac{10(100^{k+1} - 1)}{99} - (k+1) \\
S&= \frac{ 10^{2k+3} - 99k - 109}{99\times 9}
\end{align}

</p>

</details>

---

### Impossible solid
{: .d-inline-block}

B6, 2011
{: .label }

<p>Show that there is no solid figure with exactly 11 faces such that each face is a polygon
having an odd number of sides.
</p>

![](/assets/images/dodecahedron.png)

<details><summary>Solution</summary>

<p>Let us add up the number of sides from each face and call this number T.  It is given that there are 11 faces and each face has odd sides, so T is odd. However,
in any solid each side is counted twice since two faces intersect to form a side. So T must be even, which is a contradiction. Hence such a solid cannot exist.</p>

</details>

---

### Progression of squares
{: .d-inline-block}

A4, 2010
{: .label }

Show that there is no infinite arithmetic progression consisting of distinct integers all
of which are squares.

<details><summary>Solution</summary>

<p>
Suppose the infinite A.P. is given by
</p>

<p>
\[ a_0^2 < a_1^2 < a_3^2 < \cdots \]
</p>


<p>
Without loss of generality, assume that \(a_0>0\). Let the common difference be \(d\neq 0\).
</p>

<p>
The difference between any two consecutive squares in the A.P. is unbounded, hence at some point \( a_i^2 - a_{i-1}^2 > d \).
</p>


</details>

---


### Letter arrangement
{: .d-inline-block}

A1, 2011
{: .label }


The word MATHEMATICS consists of 11 letters. The number of distinct ways to rearrange these letters is.

- [ ] 11!
- [ ] 11!/3
- [ ] 11!/6
- [ ] 11!/8


<details><summary>Solution</summary>

<p>11!/8</p>


</details>

---

### Pigeon-hole principle
{:b .d-inline-block}

A8, 2010
{: .label }

<p>
If 8 points in a plane are chosen to lie on or inside a circle of diameter \(2 \mathrm{cm}\) then show that the distance between some two points will be less than \(1 \mathrm{cm}\).
</p>



---

### Just count
{:b .d-inline-block}

B3, 2010
{: .label }

<p>
(a) A computer program prints out all integers from 0 to ten thousand in base 6 using the numerals 0,1,2,3,4 and \(5 .\) How many numerals it would have printed?
(b) A 3-digt number \(abc\) in base 6 is equal to the 3-digit number \(cba\) in base 9. Find the digits.
</p>



---

### Handshake party
{:b .d-inline-block}

<p>
In a business meeting, each person shakes hands with each other person, with the exception of Mr. L. since Mr. L arrives after some people have left, he shakes hands only with those present. If the total number of handshakes is exactly \(100,\) how many people left the meeting before Mr. L arrived? (Nobody shakes hands with the same person more than once.)
</p>

---

### Intersection family
{:b .d-inline-block}

B3, 2012
{: .label}


<p>
(a) We want to choose subsets \(A_{1}, A_{2}, \ldots, A_{k}\) of \(\{1,2, \ldots, n\}\) such that any two of the chosen subsets have nonempty intersection. Show that the size \(k\) of any such collection of subsets is at most \(2^{n-1}\)
</p>

<p>
(b) For \(n>2\) show that we can always find a collection of \(2^{n-1}\) subsets \(A_{1}, A_{2}, \ldots\) of \(\{1,2, \ldots, n\}\) such that any two of the \(A_{i}\) intersect, but the intersection of all \(A_{i}\) is empty.
</p>


<details><summary>Solution</summary>

<p>
(a) If a set \(A\) is in such a collection \(\mathcal{C},\) then the complement of \(A\) cannot be in \(\mathcal{C}\). <br>
Therefore \(|\mathcal{C}| \leq \frac{1}{2}(\) total number of subsets of \(\{1,2, \ldots, n\})=\frac{1}{2} 2^{n}=2^{n-1}\)
</p>

<p>
(b) <i>Solution 1.</i> Take all \(2^{n-1}\) subsets of \(\{1,2, \ldots, n\}\) containing \(1\), remove the singleton set \(\{1\}\) and instead include its complement.
</p>

<p>
(b) <i>Solution 2.</i> For \(n=3,\) the four sets \(\{1,2\},\{2,3\},\{1,3\},\{1,2,3\}\) give a unique solution.
For \(n>3\) take the union of each of these 4 sets with all \(2^{n-3}\) subsets of \(\{4, \ldots, n\}\).
</p>


</details>

---

### Seating boys and girls
{:b .d-inline-block}

A5, 2013
{: .label}


<p>
There are 8 boys and 7 girls in a group. For each of the tasks specified below, write an expression (without simplifying) for the number of ways of doing it.
</p>


<p>
(a) Sitting in a row so that all boys sit contiguously and all girls sit contiguously, i.e., no girl sits between any two boys and no boy sits between any two girls.
</p>

<p>
(b) Sitting in a row so that between any two boys there is a girl and between any two girls there is a boy
</p>

<p>
(c) Choosing a team of six people from the group
</p>


<p>
(d) Choosing a team of six people consisting of unequal number of boys and girls
</p>


<details><summary>Solution</summary>

<p>
 \(2 \times 8 ! \times 7 !\) (The factor of 2 arises because the two blocks of boys and girls can switch positions.)
</p>

<p>
 \(8 ! \times 7 !\) (There is no factor of 2 because there must be a boy at each end.)
</p>

<p>
 \(\left(\begin{array}{c}15 \\ 6\end{array}\right)\)
</p>

<p>
 \(\left(\begin{array}{c}15 \\ 6\end{array}\right)-\left(\begin{array}{l}8 \\ 3\end{array}\right)\left(\begin{array}{l}7 \\ 3\end{array}\right)=\left(\begin{array}{l}8 \\ 6\end{array}\right)+\left(\begin{array}{l}8 \\ 5\end{array}\right)\left(\begin{array}{l}7 \\ 1\end{array}\right)+\left(\begin{array}{l}8 \\ 4\end{array}\right)\left(\begin{array}{l}7 \\ 2\end{array}\right)+\left(\begin{array}{l}8 \\ 2\end{array}\right)\left(\begin{array}{l}7 \\ 4\end{array}\right)+\left(\begin{array}{l}8 \\ 1\end{array}\right)\left(\begin{array}{l}7 \\ 5\end{array}\right)+\left(\begin{array}{l}7 \\ 6\end{array}\right)\)
</p>



</details>

---





### Difference equations III
{:b .d-inline-block}

B6, 2013
{: .label}


<p>
Define \(f_{k}(n)\) to be the sum of all possible products of \(k\) distinct integers chosen from the set \(\{1,2, \ldots, n\},\) i.e.,
<br>

\[ f_{k}(n)=\sum_{1 \leq i_{1}<i_{2}<\ldots<i_{k} \leq n} i_{1} i_{2} \ldots i_{k} \]

</p>

<p>
(a) For \(k>1,\) write a recursive formula for the function \(f_{k},\) i.e., a formula for \(f_{k}(n)\) in terms of \(f_{\ell}(m),\) where \(\ell<k\) or \((\ell=k\) and \(m<n)\)
</p>

<p>
(b) Show that \(f_{k}(n),\) as a function of \(n,\) is a polynomial of degree \(2k\).
</p>

<p>
(c) Express \(f_{2}(n)\) as a polynomial in variable \(n\).
</p>

<details>
<summary>Solution (a)</summary>

<p>
(a) Break up the terms in the definition of \(f_{k}(n)\) into two groups: the terms in which \(i_{k}=n\) add up to \(n f_{k-1}(n-1)\) and the remaining terms, i.e., the ones in which \(i_{k} \leq n-1,\) add up to \(f_{k}(n-1) .\) So we get \(f_{k}(n)=n f_{k-1}(n-1)+f_{k}(n-1)\)
c) By part a we have \(f_{2}(n)-f_{2}(n-1)=n f_{1}(n-1)=n \times \frac{n(n-1)}{2}=\frac{1}{2}\left(n^{3}-n^{2}\right)\). Similarly
\(f_{2}(n-1)-f_{2}(n-2)=\frac{1}{2}\left((n-1)^{3}-(n-1)^{2}\right)\) and so on up to \(f_{2}(2)-f_{2}(1)=\frac{1}{2}\left(2^{3}-2^{2}\right)\)
Note that \(f_{2}(1)=0,\) which we may also write as \(\frac{1}{2}\left(1^{3}-1^{2}\right) .\) Adding up, we get for any \(n \geq 1, f_{2}(n)=\sum_{j=1}^{j=n} \frac{1}{2}\left(j^{3}-j^{2}\right)=\frac{1}{2}\left(\frac{n^{2}(n+1)^{2}}{4}-\frac{n(n+1)(2 n+1)}{6}\right),\) where we have used
standard formulas for the sum of first \(n\) cubes and of first \(n\) squares.
</p>
</details>

<p></p>

<details>
<summary>Solution (b)</summary>
<p>
(b) We prove the statement by induction on \(k .\) First \(f_{1}(n)=\sum_{i=1}^{n} i=\frac{n(n+1)}{2},\) a polynomial of degree 2 as desired. For \(k>1,\) we have by part a the equation \(f_{k}(n)-f_{k}(n-1)=\) \(n f_{k-1}(n-1) .\) The right hand side is a polynomial of degree \(1+2(k-1)=2 k-1,\) where \(2(k-1)\) is the degree of \(f_{k-1}(n-1)\) by induction and the added 1 comes from the factor
n. since successive differences in the values of \(f_{k}\) are given by a polynomial of degree \(2 k-1,\) the function \(f_{k}\) on positive integers is given by a polynomial of degree 1 more, i.e., of degree \(2 k\)
Note: The previous statement is a standard fact, which can be explained as follows. If we assume that \(f_{k}(n)\) is a polynomial, then its degree is easily found, because for any polynomial \(f\) of degree \(m,\) its "successive difference" function \(f(x)-f(x-1)\) is a polynomial of degree \(m-1 .\) (Reason: If the leading term of \(f(x)\) is \(a x^{m},\) then the leading term in \(f(x)-f(x-1)\) is \(a m x^{m-1},\) as seen by expanding the power of \(x-1\) in \(a x^{m}-a(x-1)^{m}\) The remaining terms in \(f(x)-f(x-1)\) do not matter because by expanding powers of \(x-1\) in them and simplifying, we only get monomials of degree \(< m-1 .)\)
(2) In fact, based on the difference equation, \(f_{k}(n)\) must be a polynomial in the variable \(n .\) This is a consequence of the following well-known fact.
</p>
</details>

<p></p>

<details>
<summary>Solution (c)</summary>
<p>
(c) <i>Claim</i>. Given a polynomial \(h(x)\) of degree \(d\), there is a polynomial \(g(x)\) of degree \(d+1\) such that \(g(x)-g(x-1)=h(x)\).

<i>Proof:</i> Induction on \(d,\) the degree of \(h .\) If \(h(x)=c\) a constant, then \(g(x)=c x\) works.
Now for \(d>1,\) it is enough to find a polynomial \(g(x)\) such that \(g(x)-g(x-1)=x^{d}\) (because if \(h(x)=c x^{d}+\tilde{h}(x),\) where \(\tilde{h}\) has degree \(< d\), by induction we find \(\tilde{g}\) for \(h\) and then \(c g(x)+\tilde{g}(x)\) works for \(h(x)) .\) To find such \(g(x)\), notice that for \(g_{1}(x)=x^{d+1},\) we have \(h_{1}(x)=g_{1}(x)-g_{1}(x-1)=(d+1) x^{d}+h_{2}(x),\) where \(h_{2}(x)\)
is a polynomial of degree \(d-1 .\) By induction \(h_{2}(x)=g_{2}(x)-g_{2}(x-1)\) for a polynomial \(g_{2}(x)\) of degree \(d .\) Now \(g(x)=\frac{1}{d+1}\left(g_{1}(x)-g_{2}(x)\right)\) works. \(\:\square\).
</p>
</details>



---

### Count the number of functions
{:b .d-inline-block}

B3, 2014
{: .label}

<p>
(i) How many functions are there from the set \(\{1, \ldots, k\}\) to the set \(\{1, \ldots, n\} ?\)
</p>

<p>
(ii) Let \(P_{k}\) denote the set of all subsets of \(\{1, \ldots, k\} .\) Find a formula for the number of functions \(f\) from \(P_{k}\) to \(\{1, \ldots, n\}\) such that \(f(A \cup B)=\) the larger of the two integers \(f(A)\) and \(f(B)\).
</p>

<p>
Verify using your formula that that for \(k=3\) and \(n=4\) there are 100 such functions.
</p>

<p>
Example: When \(k=2,\) the set \(P_{2}\) contains 4 elements:
the empty set \(\phi,\{1\},\{2\}\) and \(\{1,2\} .\)
</p>

<p>
The function \(f\) given by \(\phi \rightarrow 2,\{1\} \rightarrow 3,\{2\} \rightarrow 4,\{1,2\} \rightarrow 4\) satisfies the given condition.
But the function \(g\) given by \(\phi \rightarrow 2,\{1\} \rightarrow 3,\{2\} \rightarrow 4,\{1,2\} \rightarrow 5\) does not, because \(g(\{1\} \cup\{2\})=g(\{1,2\})=5 \neq\) the larger of \(g(\{1\})\) and \(g(\{2\})=\max (3,4)=4\)
</p>

<details><summary>Solution</summary>

<p>
(i) As there are \(n\) choices each for the values of \(f(1), \ldots, f(k)\) and as all these choices are independent of each other, the number of functions is \(n^{k}\).
</p>

<p>
(ii) Note that \(f(A)=\max \{f(\{j\}) \mid j \in A\}\), so the function \(f\) is completely decided by its values on the empty set \(\phi\) and on the one element subsets \(\{1\},\{2\}, \ldots,\{k\} .\) If \(f(\phi)=i,\) then each of \(f(\{1\}), f(\{2\}), \ldots, f(\{k\})\) can be chosen to be any of the numbers \(i, i+1, \ldots, n\) Thus there are \(k\) independent choices for each of which there are \(n-i+1\) options. So the number of desired functions for which \(f(\phi)=i\) is \((n-i+1)^{k} .\) Now we sum over all values of \(i=1,2, \ldots, n\) to get the total number to be \(1^{k}+2^{k}+\cdots+n^{k} .\) (When \(k=3\) and \(n=4\) we get \(1^{3}+2^{3}+3^{3}+4^{3}=100,\) as mentioned in the problem.)
</p>


</details>

---


### Ordered binary strings
{:b .d-inline-block}

A2, 2015
{: .label}

<p> Consider all finite letter-strings formed by using only two letters A and B. We consider the usual dictionary order on these strings.
For example, ABAA < ABB  and  AB < ABAA.</p>


<p>
For each of the statements below, state if it is true or false.
</p>

<p>
(a) Let \(w\) be an arbitrary string. There exists a unique string \(y\) satisfying both the following properties:<br>
(i) \(w < y\) and<br>
(ii) there is no string \(x\) with \(w < x < y\)
</p>

<p>
(b) It is possible to give an infinite decreasing sequence of strings, i.e. a sequence \(w_{1}, w_{2}, \ldots,\) such that \(w_{i+1}< w_{i}\)
for each positive integer \(i\)
</p>

<p>
(c) Fewer than 50 strings are smaller than ABBABABB
</p>


<details><summary>Solution</summary>

<p>True.  Append A to \(w\). </p>
<p>True.  B, AB, AAB, AAAB, ... </p>
<p>False. There are infinitely many such strings e.g. A, AA, AAA, AAAA, </p>

</details>

---


### Number plates
{:b .d-inline-block}

A8, 2015
{: .label}

<p>
The format for car license plates in a small country is two digits followed by three vowels,
e.g. \(04\) IOU. A license plate is called "confusing" if the digit 0 (zero) and the vowel O are both present on it. For example \(04 ~ I O U\) is confusing but \(20 \mathrm{AEI}\) is not.
(i) How many distinct number plates are possible in all?
(ii) How many of these are not confusing?
</p>

<details><summary>Solution</summary>

<p>
(i) \(10^{2} \times 5^{3}=12500\)
(ii) \(10^{2} \times 4^{3}\) plates without vowel \(\mathrm{O}+9^{2} \times\left(5^{3}-4^{3}\right)\) plates with vowel O but without 0. This gives \(6400+4941=11341\).
</p>

</details>

---


### Conditional probability
{:b .d-inline-block}

A11, 2015
{: .label}

<p>
There are four distinct balls labelled 1,2,3,4 and four distinct bins labelled \(\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D} .\) The balls are picked up in order and placed into one of the four bins at random. Let \(E_{i}\) denote the event that the first \(i\) balls go into distinct bins. Calculate the following probabilities.
Notation: \(\operatorname{Pr}[X]=\) the probability of event \(X\) taking place. \(\operatorname{Pr}[X \mid Y]=\) the probability of event \(X\) taking place, given that event \(Y\) has taken place.
</p>

<details><summary>Solution</summary>

<p>
(i) \(\operatorname{Pr}\left[E_{4}\right]=\frac{4 !}{4^{4}}=\frac{3}{32}\)
(ii) \(\operatorname{Pr}\left[E_{4} \mid E_{3}\right]=\frac{1}{4}\)
(iii) \(\operatorname{Pr}\left[E_{4} \mid E_{2}\right]=\frac{24}{4^{2}}=\frac{1}{8}\)
(iv) \(\operatorname{Pr}\left[E_{3} \mid E_{4}\right]=1\)
</p>


</details>

---


### Logical puzzle
{:b .d-inline-block}

A1, 2016
{: .label}

<p>
Four children K, L, M and R are about to run a race. They make some predictions as follows.
K says: M will win. Myself will come second.
R says: M will come second. L will be third.
M says: L will be last. R will be second.
After the race, it turns out that each person has made exactly one correct and one incorrect prediction. Write the result of the race in the order from first to the last.
</p>

<details><summary>Solution</summary>

<p>
If K comes second, then L was third (one correct answer for R). But then R would also need to be second (one correct answer for M, a contradiction. So K cannot be second. So M must have won, etc. The order is M R L K.
</p>

</details>

---


### Pairwise sums of a set
{:b .d-inline-block}

B4, 2016
{: .label}

<p>
Let \(A\) be a non-empty finite sequence of \(n\) distinct integers \(a_{1}< a_{2}< \cdots< a_{n} .\) Define

\[ A+A=\left\{a_{i}+a_{j} \mid 1 \leq i, j \leq n\right\} \]

i.e., the set of all pairwise sums of numbers from \(A\). E.g., for \(A=\{1,4\}, A+A=\{2,5,8\}\).
</p>

<p>
(a) Show that \(|A+A| \geq 2 n-1 .\) Here \(|A+A|\) means the number of elements in \(A+A\).<br>

(b) Prove that \(|A+A|=2 n-1\) if and only if the sequence \(A\) is an arithmetic progression.<br>

(c) Find a sequence \(A\) of the form \(0<1 < a_{3} < \cdots < a_{10}\) such that \(|A+A|=20\).<br>

</p>

<details><summary>Solution</summary>

<p>
(a) The following \(2 n-1\) numbers in \(A+A\) are distinct: \(a_{1}+a_{1}< a_{1}+a_{2}<\cdots< a_{1}+a_{n}< a_{2}+a_{n}< \ldots< a_{n}+a_{n}\).
</p>

<p>
A way to visualize is to write \(a_{i}+a_{j}\) at point \((i, j)\) in the XY-plane. Any step to the right or up increases the number. To reach from \(2 a_{1}\) to \(2 a_{n}\) needs \(2 n-1\) such steps. The given example is the path along bottom row and then rightmost column.
</p>


<p>
(b) Suppose the \(a_{i}\) form an arithmetic progression. Then for a fixed \(k\), the value of \(a_{i}+a_{k-i}\) is constant for all possible \(i,\) where \(2 \leq k \leq 2 n .\) For the converse use induction. There is nothing to prove for \(n=1,2 .\) For \(n>2,\) remove \(a_{n}\) from \(A\) to get a set \(B .\) Now \(|A+A|-|B+B| \geq 2,\) because the two distinct numbers \(a_{n-1}+a_{n}\) and \(2 a_{n}\) in \(A+A\) are greater than all numbers in \(B+B .\) So for \(|A+A|=2 n-1\) to happen, one must have \(|B+B|=2 n-3,\) which by induction forces \(a_{1}, \ldots, a_{n-1}\) to be in an arithmetic progression. Moreover \(a_{n-2}+a_{n}\) must be in \(B+B\) and it can only be the largest number \(2 a_{n-1}\) (because all others are smaller than \(a_{n-2}+a_{n}\) ). This shows that \(a_{n}\) is the next term of the same arithmetic progression.
</p>

<p>
(c) \(0,1,2,3,4,5,6,7,8,10.\)

<br> Can you prove that the answer is unique?
</p>



</details>

---


### Distribute oranges in boxes
{:b .d-inline-block}

A3, 2017
{: .label}

<p>
10 oranges are to be placed in 5 distinct boxes labeled \(\mathrm{U}, \mathrm{V}, \mathrm{W}, \mathrm{X}, \mathrm{Y} .\) A box may contain any number of oranges including no oranges or all the oranges. What is the number of ways to distribute the oranges so that exactly two of the boxes contain exactly two oranges each?
</p>

<details><summary>Solution</summary>

<p>
From the five distinct boxes, there are 10 ways to pick the two boxes that will have 2 oranges each. We need to distribute the remaining 6 oranges in the remaining three boxes such that none of the three boxes gets exactly 2 oranges. The possible distributions are \(6+0+0\) (which can be done in 3 ways) or \(5+1+0\) (6 ways) or \(4+1+1\) (3 ways) or \(3+3+0(3\) ways \() .\) Thus the required answer is \(10 \times(3+6+3+3)=150\)
</p>


</details>

---



### Coloring integers
{:b .d-inline-block}

B5, 2017
{: .label}

<p>
Each integer is colored with exactly one of three possible colors - black, red or white satisfying the following two rules:
</p>


<p>
<i>Rule 1</i>: The negative of a black number must be colored white.<br>
<i>Rule 2</i>:  The sum of two white numbers (not necessarily distinct) must be colored black.<br>
</p>


<p>
(a) Show that the negative of a white number must be colored black.
</p>

<p>
(b) Show that the sum of two black numbers must be colored white.
</p>

<p>
(c) Determine all possible colorings of the integers that satisfy these rules.
</p>

<details>
<summary>Solution (a)</summary>
<p>
(a) Suppose an integer \(n\) is colored white. Then \((n+n)=2 n\) is black, so \(-2 n\) is white, so \(-2 n+n=-n\) is black. Thus, the negative of a white number must be colored black.
</p>
</details>

<p></p>

<details>
<summary>Solution (b)</summary>
<p>
(b) Now suppose the integers \(n\) and \(m\) are both colored black. Then \(-n\) and \(-m\) are both white, so \(-n-m\) is back, so \(n+m\) is white. Thus, the sum of two black numbers must be colored white.
</p>
</details>

<p></p>

<details>
<summary>Solution (c)</summary>

<p>
(c) One possible coloring has all the integers colored red, since there are no condit ions on red number s.
If that is not the case, let \(n\) be the smallest positive integer that is not colored red.
Suppose the number \(n\) is colored black.
Then we claim the remaining colors are all fully determined. Namely, the numbers of the form \((3 k+1) n\) will be black,
the numbers of the for \(m(3k+2) n\) will be white, and the numbers of the form \((3k)n\) will be red,
for all integers k. And all remaining colors will be red. On the other hand, if the number \(n\)
is colored white to begin with, then the remaining numbers will be determined by the same rules, but with black and white switched.
</p>

<p>
Thus we have listed all possible colorings.
In order to prove the above claim, we first prove one more rule the colors must obey. Namely, that
</p>

<p>
<i>Lemma</i>. The sum of a black number and a white number must be colored red.
</p>

<p>
<i>Proof.</i> Suppose \(n\) is black and \(m\) is white, and that \(n+m\) is black. But then \((n+m)+(-m)\) is the sum of two black numbers, and must be colored white, which is a contradiction. Similarly, the sum of \(n\) and \(m\) cannot be white. Therefore it must be red.\(\:\square \)
</p>


<p>
Using this rule, it is easy to see that the numbers of the form \((3k+1)n\) will be black, the numbers of the form \((3k+2) n\) will be white,
and the numbers of the form \((3k)n\) will be red, for all integers k.
</p>


<p>
<i>Lemma</i>.  All the numbers that are not multiples of \(n\) are colored red.
</p>

<p>
We can prove this by contradiction. As before \(n\) is the smallest positive integer that is not red, and it is colored black.
Suppose \(m\) is the smallest positive integer that is neither red nor a multiple of \(n\).
</p>

<p>
Then \(m=qn+r\), where \(0 < r< n\) is the remainder when \(m\) is divided by \(n\).
</p>

<p>
We know this remainder is nonzero, since \(m\) is not a multiple of \(n .\) We also know that \(q > 0,\) since \(m > n\).
Suppose \(m\) is white. Then, because \(-n\) is white, we know \(m-n=(q-1) n+r\) is black, which gives us a smaller non-red positive integer that
is not a multiple of \(n\). On the other hand, suppose \(m\) is colored black. Then \(-2 n\) is black, so \(m-2 n=(q-2) n+r\) is white. If \(q<1,\) this gives us a smaller positive non-red integer that \(^{\prime}\) s not a multiple of \(n_{1}\) which is a contradiction, provided \(q>1 .\) But if \(q=1,\) and \(m-2 n=-n+r\) is white, that means that \(n-r\) is black, a contradiction. \(\:\square\)
</p>

</details>


---


### Broken calculator
{:b .d-inline-block}

A7, 2019
{: .label}

<p> A broken calculator has all its 10 digit keys and two operation keys intact. Let us call these operation keys A and B. When the calculator displays a number \(n\) pressing A changes the display to \(n+1\). When the calculator displays a number \(n\) pressing \(B\) changes the display to \(2 n .\) For example, if the number 3 is displayed then the key strokes ABBA changes the display in the following steps \(3 \rightarrow 4 \rightarrow 8 \rightarrow 16 \rightarrow 17\).  </p>

<p> If 1 is on the display what is the least number of key strokes needed to get 260 on the display?  </p>

<details><summary>Solution</summary>

<p>\(9,\) there are exactly two sequences, for example, \(BBBBBBABB\).</p>


</details>

---

### First ascent
{:b .d-inline-block}


A8, 2019
{: .label}


<p>
Let \(\pi=\pi_{1} \pi_{2} \ldots \ldots \pi_{n}\) be a permutation of the numbers \(1,2,3, \ldots, n\).<br>
We say \(\pi\) has its first ascent at position \(k<n\) if \(\pi_{1}>\pi_{2} \ldots>\pi_{k}\) and \(\pi_{k}<\pi_{k+1}\).<br>
If \(\pi_{1}>\pi_{2}>\ldots>\) \(\pi_{n-1}>\pi_{n}\) we say \(\pi\) has its first ascent in position \(n\).<br>
</p>

<p>
For example when \(n=4\) the permutation 2134 of has its first ascent at position 2
The number of permutations which have their first ascent at position \(k\) is ...
</p>

<details><summary>Solution</summary>

<p>
\(\left(\begin{array}{l}n \\ k\end{array}\right)(n-k) !-\left(\begin{array}{c}n \\ k+1\end{array}\right)(n-k-1) !\)
</p>


</details>
