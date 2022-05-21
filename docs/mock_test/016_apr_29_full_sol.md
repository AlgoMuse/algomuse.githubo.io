---
layout: default
title: Mock test 4 Full-syllabus test
nav_exclude: true
---


#  Mock test #4 '22: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 29 April 2022
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


<p><b>B1.</b> Let \(f : (0,\infty) \implies \mathbb{R}\) be a continuous function satisfying \(f(1)=5\) and \(f\left( \dfrac{x}{x+1} \right) = f(x) + 2\) for all positive reals \(x\).<br>
(a) Find \(\lim_{x \rightarrow \infty} f(x)\).<br>
(b) Show that  \(\lim_{x \rightarrow 0^+} f(x) = \infty\)<br>
(c) Find one example of such a function.<br>
</p>


<details open><summary>Sol.</summary>
(a) \(\lim_{x \to \infty}f(x) =  \lim_{x \to \infty} f\left( \dfrac{x}{x+1}\right) - 2 = f(1) - 2 = 5 - 2 = 3\)<br>
(b) <i>Claim</i>. \(\lim_{x \to 0^{+}} f(x) = \infty\)<br>
 <i>Proof.</i> \(f(1/(x+1))=f(1/x)+2\). So if \(a_n=1/n\). \(f(a_{n+1})=f(a_n)+2\).
So \(f(a_n)\) diverges. \(\square\)
(c) \(f(n)= 5+2(1/n -1)\).
</details>


---


<p><b>B2.</b> If \(n\) is a natural number, prove that<br>
(a) \(\log_{10}(n+1)>\frac{3}{10 n}+\log_{10} n\)<br>
(b) \(\log n !>\frac{3 n}{10}\left(\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}-1\right)\).<br>
</p>

<details open><summary>Sol.</summary>
 a) The inequality is equivalent in showing:<br>
 \[ {(1 + \frac{1}{n})}^{10n} \geq 1000 \]
 But \( {(1 + \frac{1}{n})}^{n} \) is a decreasing function after \( n \geq 3\) and reaches its limit \(e\).  So, we have:
 \[ {({(1 + \frac{1}{n})}^{n})}^{10} > e^{10} > 2^{10} > 1000 \]

 b) \[ L  = \sum_{k = 1}^{n} \ln k \ge \int_1^n \ln x \; \mbox d x \]
    \[ =  n ( \ln n - 1) + 1 > \frac{3}{10} n \left( -1 + \ln n \right) \]
    \[  \frac{3}{10} n \left( -1 + \int_1^n \frac{\mbox d x}{x} \right) \ge \frac{3}{10} n \left( -1 + \sum_{k = 2}^n \frac{1}{k} \right) \]
</details>




---

<p><b>B3.</b> Show that any integer greater than \(10\) whose digits are all members of \(\{1, 3, 7, 9\}\) has a prime factor \(\geq 11\).
</p>


<details open><summary>Sol.</summary>
For the sake of contradiction, let all prime factors be \(\leq 11\) so this means that all prime factors are either \(2, 3, 5, 7\). So, if \(2\) is a prime factor then it the digits should include \(2, 4, 6, 8, 0\) and if \(5\) is a prime factor then it the digits should include \(5\). So \(3, 7\) left. Means the number is of the form of \(3^a \cdot 7^b\). Now we observe the ten's digit of these numbers are even. So, we can see that the tens digit of \(21\) is even. Now no matter what we multiply to this number, the output will also have it's tens digit as even because if we take a number A which have even tens digit and 1,3,7,9 unit digit and take a number B  which have even tens digit and 1,3,7,9 unit digit and if you multiply them and you get C then it also have even tens digit and 1,3,7,9 unit digit which means it is closed under multiplication. And we are at a contradiction and implies there is one prime factor \(\geq 11\).
</details>

---

<p><b>B4.</b> Let \(f(x)=\dfrac{a_i}{x+a_i} + \dfrac{a_2}{x+a_2} + \cdots + \dfrac{a_n}{x+a_n}\) where \(a_i\) are unequal positive reals. Find the sum of the lengths of the intervals in which \(f(x) \geq 1\).<br>
</p>

<details open><summary>Sol.</summary>
Without loss of generality, assume \(a_1 > a_2 > \cdots > a_n.\) The graph of each \(a_i/(x + a_i)\) is a rectangular hyperbola with asymptotes \(x = -a_i\) and \(y = 0\). So it is not hard to see that the graph of \(f(x)\) is made up of \(n+1\) strictly decreasing parts. For \(x < -a_1\), \(f(x)\) is negative. For \(x\)  \((-a_i, a_{i+1})\), \(f(x)\) decreases from \(\infty\) to \(-\infty\). Finally, for \(x > -a_n\), \(f(x)\) decreases from \(\infty\) to \(0\). Thus \(f(x)=1\) at \(n\) values \( b_1 < b_2 < \cdots < b_n\) and \(f(x) \geq 1\) on the n intervals \((-a_1,b_1), (-a_2,b_2), \cdots, (-a_n,b_n)\). So the sum of the lengths of these intervals is \(\sum (a_i + b_i)\). We show that \(\sum b_i = 0\).<br>

Multiplying \(f(x) = 1\) by \(\Pi (x + a_j)\) we get a polynomial of degree \(n\):
\[\Pi(x + a_j) - \sum_i(a_i \Pi_{j \neq i}(x+a_j) ) = 0 \]
The coefficient of \(x^n\) is \(1\) and the coefficient of \(x^{n-1}\)
is \(\sum a_j - \sum a_i = 0\). Hence the sum of the roots, which is \(\sum b_i\), is zero.
</details>


---

<p><b>B5.</b> Let ABCD be a cyclic quadrilateral. Suppose that there exists a circle with center in AB that is tangent to the other sides of the quadrilateral. <br>
(a) Prove that \(AB = AD+BC\).<br>
(b) Determine, in terms of \(x = AB\) and \(y =CD\), the maximum possible area of the quadrilateral.
</p>

<details open><summary>Sol.</summary>
(a) Let the circle have center \(O\) on \(AB\) and radius \(R\). Let \(\angle OAD = \theta, \angle OBC = \phi \). Since \(ABCD\) is cyclic, \(\angle ADC = 180^{\circ} - \phi \), so \(\angle ODA = 90^{\circ} - \phi / 2\). If \(AD\) touches the circle at \(X\), then \(AD = AX + XD = r\cot \theta + r \tan(\phi/2)\). Similarly for \(\phi\), so \(AD + BC = r/\sin \theta + r/\sin \phi = AO + OB = AB\).
<br>
<i>(b) Claim.</i> The maximum possible area is  \[(\frac{h}{2} + \frac{k}{2})\sqrt{(\frac{hk}{2} - \frac{h^2}{4})} \] where \(h = |CD|, k = |AB|\).<br>

<i>Proof.</i>Suppose \(AD\) and \(BC\) meet at \(H\) (we deal below with the case where they are parallel). Then \(HCD\) and \(HAB\) are similar,
so area \(HCD = (CD^2/AB^2)\) area \(HAB\) and area \(ABCD = (1 - CD^2/AB^2)\) area \(HAB\). Also 
\[AB/CD = HA/HC = HB/HD = (HA+HB)/(HC+HD) = (cont.) \]
\[(HA+HB)/(HB-BC+HA-DA) = (HA+HB)/(HA+HB-AB) \]. Hence \(HA+HB = AB^2/(AB-CD) \),
which is fixed. Now for fixed \(HA+HB\) we maximise the area of \(HAB\) by taking \(HA = HB\) and hence \(AD = BC\). 
<br>
Put \(h = CD, k= AB\). SO \(k \cos \theta + h = k\). Hence \(\cos \theta = (1-h/k)\). Hence \(\sin \theta = \sqrt{(2h/k - h^2/k^2)}\). So area \(ABCD = 1/2(h+k) 1/2 k \sin \theta = (\frac{h}{2} + \frac{k}{2})\sqrt{(\frac{hk}{2} - \frac{h^2}{4})}\). 
<br>
If \(AD\) and \(BC\) are parallel then \(A\) and \(B\) must lie on the circle, so that \(\angle DAB = \angle ABC = 90^{\circ}.\) But \(ABCD\)
is cyclic, so it must be a rectangle. Hence \(AB = CD\) and area \(ABCD = k^2/2\). In this case still gives the correct answer. \( \square \)
</details>



---

<p><b>B6.</b> Let \(o(n)\) be the number of \(2n-\)tuples \((a_1, a_2, \cdots , a_n, b_1, b_2, \cdots , b_n)\) such that each \(a_i, b_j = 0\) or \(1\) and \(a_1b_1 + a_2b_2 + \cdots + a_nb_n\) is odd. Similarly, let \(e(n)\) be the number for which the sum is even. Find the value of the ratio \(o(n)/e(n)\) in terms of \(n\).
</p>


<details open><summary>Sol.</summary>
We can show that it's \(2n-1\) by induction. For \(n=2\) we have the word \(aba\), and it's clear that we can't continue to add letters. Assume we have shown the maximal length to be \(2k-1\) for \(k<n\). Now we can only work with \(n>2\).
First assume that each letter appears at least \(3\) times. Then from the word we can extract a subword using only the first \(n-1\) letters and satisfying the condition, which has length at least \(3(n-1)>2n-1\) because \(n>2\), but this contradicts the induction hypothesis. There is, thus, a letter \(a\) which appears at most twice. Now disregard \(a\) from our word. What we get is a word using only \(n-1\) letters and satisfying the condition. It must then be \(\le 2(n-1)-1=2n-3\). This, together with the fact that \(a\) appears at most twice, shows that the length of our word on \(n\) letters is \(\le 2n-3+2=2n-1\).
We can construct the example \(a_1,a_2,\ldots,a_n,a_{n-1},\ldots,a_1\) in order to show that \(2n-1\) is attainable.
</details>





