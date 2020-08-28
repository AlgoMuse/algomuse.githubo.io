---
layout: default
title: Solvability of equations
parent: Algebra
nav_order: 2
---



## Solvability of equations [9]


### Charity
{:b .d-inline-block}

A1, 2015
{: .label}

<p>
Ten people sitting around a circular table decide to donate some money for charity. You are told that the amount donated by each person was the average of the money donated by the two persons sitting adjacent to him/her.
One person donated Rs. \(500\).
</p>

<p>
Choose the correct option for the following two questions.
</p>

<p>
<b>Q1.</b> What is the total amount donated by the 10 people?
</p>

<p>
(a) exactly Rs. 5000
(b) less than Rs. 5000
(c) more than Rs. 5000
(d) cannot decide.
</p>

<p>
<b>Q2.</b> What is the maximum amount donated by an individual?
</p>

<p>
(a) exactly Rs. 500
(b) less than Rs. 500
(c) more than Rs. 500
(d) cannot decide.
</p>

<details><summary>Solution</summary>

<p>
<b>A1.</b>  Exactly Rs. \(5000\).
</p>

<p>
<b>A2.</b>  Exactly Rs. \(500\).
</p>

<p>
Consider the person who donated Rs. 500.  Suppose the neighbor to the left donates \(500+x\).
Then the one on the right donates \(500-x\).  But continuing leftward, the amounts donated are \(500+2 x, 500+3 x, \ldots,\)
forcing \(x\) to be \(0,\) since you come around to the neighbor to the right.
</p>

</details>

---

### Integers in a function range
{: .d-inline-block}

A2, 2018
{: .label}

<p>
Consider the following function defined for all real numbers \(x\)

\[ f(x)=\frac{2018}{10+e^{x}} \]

How many integers are there in the range of \(f\)?
</p>


<details><summary>Solution</summary>


<p>
There are 201 integers.
</p>

<p>
The function is strictly decreasing as \(x\) goes from \(-\infty\) to \(\infty\). The range of the function is \((0,201.8)\).
By continuity, all the integers in range appear as values of \(f(x)\).
</p>

</details>

---

### GDP vs Per-capita GDP
{: .d-inline-block}

A2, 2016
{: .label}


<p>
A country's GDP grew by \(7.8 \%\) within a period. During the same period the country's per-capita-GDP defined as the ratio of GDP to the total population, increased by 10\%.
By what percentage did the total population change during this period?
</p>

<details><summary>Solution</summary>

<p>
Per-capita GDP is \(\frac{\text { GDP }}{\text { population }}\). Letting \(G\) and \(P\) denote the old GDP and population respectively, the new per-capita GDP is \(\frac{1.078 G}{(1+x) P}\) where \(x\) is the unknown percent change in population we wish to calculate. The percent increase in per-capita GDP is \(10 \%=0.1\) So we have \(\frac{1.078}{1+x}=1.1 .\) Solving for \(x\) we get \(1+x=\frac{1.078}{1.1}=\frac{98 \times 11}{100 \times 11}=0.98 .\) So \(x\) is -0.02 So population decreased by \(2 \%\)
</p>

</details>

---







### Solving a cubic root equation
{: .d-inline-block}

A3, 2018
{: .label }

<p>List all solutions of the following equation. Need not simplify the solutions.

\[ \large \sqrt[3]{x+4}-\sqrt[3]{x}=1 \]
</p>

<details><summary>Solution</summary>

<p>
Put \(t=\sqrt[3]{x}\) to get:

\begin{align}
\left(t^{3}+4\right)&=(1+t)^{3} \\
4&=t^{3}+3t^2+3t+1 \\
t^{2}+t-1&=0\\
\end{align}

Solving for \(t\) and then \(x\) we get:

\[ x = \left( \frac{-1\pm\sqrt{5}}{2} \right)^{1/3} \]


<i><b>Comment</b>. The official CMI paper glibly says: <q>Solve it and then take the cube root of the solutions. The two solutions are \(-2 \pm \sqrt{5}\)</q>.
 No explanation is given on why it is easy to take cube roots of \(t\).</i>


</p>

</details>

---



### Solve: \\(p(x)^{q(x)} = 1\\)
{: .d-inline-block}

B2a, 2018
{: .label}


<p>
Find all real solutions of the equation:

\[ \left(x^{2}-2 x\right)^{x^{2}+x-6}=1 \]

</p>


<details><summary>Solution</summary>

<p>
The equation is of the form \(a^b=1\). This can happen only in three cases:
<br>

(i) Either \(a=1\), which means \(x^2-2x=1\). So \(x=1\pm\sqrt{2}\).<br>
(ii) or \(a=-1\) and \(b\) is an even integer. So \(x=1\) works.<br>
(iii) or \(b=0\) and \(a\neq 0\). Which happens when \(x=-3\) or \(1\). The value \(x=2\) makes \(a=b=0\) <br>

So \(x=-3,1,1 \pm \sqrt{2}\) are the only solutions.
</p>


</details>

---


### Solve: \\(\sqrt[3]{a}-\sqrt[3]{b} = 1\\)
{: .d-inline-block}

B2b, 2018
{: .label}


<p>
The following expression is an integer. Find its value.

\[\sqrt[3]{6 \sqrt{3}+10}-\sqrt[3]{6 \sqrt{3}-10} \]

</p>

<details><summary>Solution</summary>

<p>
Let \(a=\sqrt{3}+10\) and \(b=\sqrt{3}-10\).  We have \(a^{3}-b^{3}=20\) and \(a b=2 .\) Putting it in \((a-b)^{3}\) we get \((a-b)^{3}=20-6(a-b)\).
This cubic has one real root \(a-b=2\) and two complex roots.
</p>


<i>A similar problem was discussed on [Quora](https://www.quora.com/How-do-I-prove-that-sqrt-3-5-sqrt-2-+7-sqrt-3-5-sqrt-2-7-is-an-integer) in 2017.</i>

</details>

---

### Symmetric log reciprocals
{: .d-inline-block}

A7, 2010
{: .label}


<p>
If \(a, b, c\) are real numbers \(> 1\), then show that:<br>
</p>

<p>

\[ \frac{1}{1+\log_{a^{2} b} \frac{c}{a}}+\frac{1}{1+\log_{b^{2} c} \frac{a}{b}}+\frac{1}{1+\log_{c^{2} a} \frac{b}{c}}=3 \]
</p>

<details><summary>Solution</summary>

<p>
We will make use of the identity: \(\log_{x} a+\log_{x} b=\log_{x} a b\).
</p>


<p>
\begin{align}
\frac{1}{1+\log_{a^{2} b}\left(\frac{c}{a}\right)}&=\frac{1}{\log_{a^{2} b}\left(a^{2} b\right)+\log_{a^{2} b}\left(\frac{c}{a}\right)} \\
&=\frac{1}{\log_{a^{2} b}\left(\frac{c}{a} \cdot a^{2} b\right)} \\
&=\frac{1}{\log_{a^{2} b}(a b c)}\\
&\\
&=\log_{a b c}\left(a^{2} b\right)
\end{align}
</p>


<p>
Hence the given expression is:
</p>

<p>
\(\log_{a b c}\left(a^{2} b\right)+\log_{a b c}\left(b^{2} c\right)+\log_{a b c}\left(c^{2} a\right)\)
\(=\log_{a b c}(a b c)^{3}\)
\(=3\)
</p>

</details>

---

### Solutions to simultaneous equations
{: .d-inline-block}

A8, 2017
{: .label}


<p>
State Yes or No for each of these questions.<br>
Is it possible to find a \(2 \times 2\) matrix \(A\) for which the equation \(A \vec{x}=\vec{b}\) has:

<ul>
<li>(a) no solutions for some but not all \(\vec{b}\); exactly one solution for all other \(\vec{b} ?\)</li>

<li>(b) exactly one solution for some but not all \(\vec{b} ;\) more than one solution for all other \(\vec{b} ?\)</li>

<li>(c) no solutions for some but not all \(\vec{b}\); more than one solution for all other \(\vec{b} ?\)</li>

<li>(d) no solutions for some \(\vec{b},\) exactly one solution for some \(\vec{b}\) and more than one solution for some \(\vec{b} ?\)</li>

</ul>

</p>


<details><summary>Solution</summary>


<p>

No-No-Yes-No.<br>

Suppose \(A\) has nonzero determinant. Then for any \(\vec{b},\) we see that \(A \vec{x}=\vec{b}\) has the unique solution \(\vec{x}=A^{-1} \vec{b}\).

If determinant of \(A\) is zero then we can make two cases:<br>

(i) If \(A\) is the zero matrix, then \(A \vec{x}=\vec{b}\) has infinitely many solutions for \(\vec{b}=\overrightarrow{0}\) and no solutions otherwise.<br><br>

(ii) If \(A\) is nonzero then it is easy to see that we are solving two equations in two variables whose left hand sides are proportional.

So if the two right hand constants that make up \(\vec{b}\) are in the same proportion, then we will have infinitely many solutions (because one of the variables can be arbitrary).
If the constants are not in the same proportion, then the two equations will be inconsistent and we will have no solutions.
</p>

</details>

---

#### Problem credits

<img src="/assets/images/LADRcover.png" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
The statements in the problem are basic facts in linear algebra (LA).
It is a good idea to be familiar with LA although the syllabus does not mention it.
Read the first three chapters of the book by Sheldon Axler.
Another LA problem from CMI exam: B5 part(b) from 2014.
</p>
{: .fs-4 .fw-300 }

<br><br>
<br><br>
[View on Amazon](https://amzn.to/3hbctgO)

---

### Reduce to a quadratic
{: .d-inline-block}

B2B, 2019
{: .label}

<p>
Find real numbers \(x\) that satisfy:

\[\frac{8^{x}+27^{x}}{12^{x}+18^{x}}=\frac{7}{6}\]
</p>

<details><summary>Solution</summary>

<p>
\[\frac{\left(2^{x}\right)^{3}+\left(3^{x}\right)^{3}}{\left(2^{x}\right)^{2} \cdot 3^{x}+\left(3^{x}\right)^{2} \cdot 2^{x}}=\frac{7}{6}\]
</p>

<p>Putting \(a=2^x\) and \(b=3^x\) in the above equation, we get:</p>


<p>\[ \frac{a^3 + b^3}{a^2b+ab^2} = \frac{7}{6} \]</p>

<p>\[ \frac{ (a+b)(a^2+b^2-ab) }{ab(a+b)} = \frac{7}{6} \]</p>

<p>\[ \frac{ (a+b)(a^2+b^2-ab) }{ab(a+b)} = \frac{7}{6} \]</p>

<p>\[ 6a^2 - 13ab + 6b^2 = 0 \]</p>

<p>\[ 6t^{2}-13t+6=0 \text{ where } t=a/b \]</p>

<p>The above quadratic has \(t = 3/2\)  and \(t=2/3\) as the roots. So \(x=\pm 1\) satisfies the original equation.</p>



</details>








<!--
#### Request to CMI faculty
<p>
Please do not pose elementary facts from advanced topics as high-school questions. Linear algebra is not part of XII mathematics.
</p>
-->

