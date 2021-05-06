---
layout: default
title: Mock test 7 Combinatorics
nav_exclude: true
---


#  MT #7: Combinatorics & Geometry
#### Timings: 17:00-20:00 Hrs &nbsp;&nbsp;  Date: 6 May 2021
{: .fs-3 .text-grey-004 }

---

### Instructions

- You are responsible for keeping time. Email all your solutions by 20:05 Hrs IST.
- Write your answers with a dark pen on white paper.
- Find an email from me with the subject line 'Mock test #7: Combinatorics and Geometry'. Send your solutions (images) as replies to this email.
- Adjust/Reduce the resolution of the camera so that each image is less than 500 KB in size.
- Total marks: 100 (10x4=40 for Part A + 6x10=60 for Part B)
{: .bg-grey-lt-000 .p-6 }


**For students who miss the live test (members only)**<br>
Self-administer the mock test and email your solutions before 7 May, 23:59 Hrs. Your solutions will be evaluated
but marks won't be counted for official use in the future. Solutions submitted after 7 May, 23:59 Hrs will not be evaluated.
As per the rules of CMI entrance exam, no calculators or log tables must be used.
{: .bg-grey-lt-000 .p-6 }


---

## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg.
{: .fs-3 }

**For this part, answers must be written without any explanation.**





<ol>




<p>
<li>
We have 9 identical white beads and 2 identical black beads. How
many distinct bracelets can we make using all the beads? Two bracelets are considered the same
upto flipping and rotation.
</li>
</p>

<p>
<li>
We want to go from corner A to corner B in the figure shown below. If we
can only move right or up, how many distinct ways are there to go from A to B?

<p style="text-align:center">
<img src="/assets/images/frame_walk.png"/>
</p>

</li>
</p>


<li>
<p>A unit square is inscribed in a circle. A smaller square sits on the
top edge of the larger square. The top edge of the smaller square touches circle. Find
the length of the smaller square.
</p>

<p style="text-align:center">
<img src="/assets/images/mt7_small_square.png"/>
</p>

</li>

<!--
Let the side length of the smaller square be \(x\). The following equation must hold:
\[ \left(\frac{x}{2}\right)^{2}+\left(x+\frac{1}{2}\right)^{2}=\left(\frac{1}{\sqrt{2}}\right)^{2} \]

Hence, \(x=1/5\).

-->

<li>
<p>
Count the number of ordered sequences of \(1\)s and \(5\)s that add up to \(13\).<br>
For example, \( (1,1,5,1,5) \) and \( (1,1,1,1,1,1,1,1,1,1,1,1,1) \) are valid sequences.
</p>
</li>

<!--

There are 3 sets of 1s and 5s that sum to 13.<br>
For a given set suppose there are \(n\) 5s we have a total of \( (13-5n)+n=13-4n\)
numbers so we want to compute:
\[ \sum_{n=0}^{2} \binom{13-4n}{n} =    \]


-->


<p>
<li>
Find the number of non-zero solutions to the equation: \(z^{2}+2 \bar{z}=0\).
</li>
</p>




<!--
3. We have $\left|z^{2}\right|=|-2 \bar{z}|=2|z| .$ Suppose $z \neq 0 .$ Then $|z|^{2}=4=z \bar{z}$
Hence the equation becomes $z^{2}+2 \frac{4}{z}=0$ i.e. $z^{3}+8=0 .$ Hence there are 3 non zero solutions.
-->


<p>
<li>We have a triangle \(ABC\) and \(AD\) bisects the angle \(BAC\). We know the following
measurements: \(AB=10\) cm, \(CD=2 BD\) and the area of the triangle \(ABC\) is 50 sq. cm. Find the value
of the \(\angle BAD\) in degrees.
</li>
</p>


<p style="text-align:center">
<img src="/assets/images/mt7_triangle.png"/>
</p>





<!--
SMT 2019

Solution: Since $A D$ bisects $\angle B A C$, we have by the Angle-Bisector Theorem that $\frac{A B}{B D}=$ $\frac{A C}{C D} \Longrightarrow A C=\frac{C D}{B D} \cdot A B=20 .$ Let $E$ be the point on $A C$ such that $B E \perp A C .$ Since the area of $\triangle A B C$ is 50, we have $\frac{A C \cdot B E}{2}=50 \Longrightarrow B E=5 .$ But $\triangle A B E$ is a right triangle and $A B=2 B E$, so $\triangle A B E$ must be a $30-60-90$ triangle. It follows that $\angle B A C=30^{\circ}$ so $\angle B A D=15^{\circ}$
-->




<p>
<li>
In the complex plane shown below, \(PQR\) is an arc with center at \(A\).  The values of the points are:
\(A=-1+0i\), \(P=-1+\sqrt{2}+\sqrt{2}i\), \(Q=1+0i\) and \(R=-1+\sqrt{2}-\sqrt{2}i\). Which pair of inequalities
represent the the shaded region?  <br>


<p style="text-align:center">
<img src="/assets/images/argand_plane.png"/>
</p>


<ol>
<li>\(|z+1|<2,|\arg (z+1)|<\frac{\pi}{2}\)</li>
<li>\(|z-1|<2,|\arg (z-1)|<\frac{\pi}{2}\)</li>
<li>\(|z+1|>2,|\arg (z+1)|<\frac{\pi}{4}\)</li>
<li>\(|z-1|>2,|\arg (z+1)|<\frac{\pi}{4}\)</li>
</ol>



</li>
</p>


<p>
<li>

Let \(t \in \mathbb{N}\). The number of elements in set \(\left\{\left(\cos \frac{n\pi}{t}+i \sin \frac{n\pi}{t}\right) \mid n \in \mathbb{N}\right\}\)
is

<ol>
<li> Infinite </li>
<li> \(t\)</li>
<li> \(t+1\)</li>
<li> \(2t\) </li>
<li> \(2t+1\) </li>
<li> \(2t-1\) </li>
<li> None of the above.</li>
</ol>

</li>
</p>

<!--

Solution: (d)
The number of elements in the given set is equal to the number of
\(q\)th roots of \(\{\cos n \pi+$ $i \sin n \pi \mid n \in \mathbb{N}\}=\{\pm 1\}\)
which are \(2q\) in number since the \(q\)th roots of 1 are distinct from the \(q\)th  roots of \(-1\).

-->



<li>
<p>
An ant is initially at a corner of a cube. At each time step, it moves along an edge
to a random adjacent vertex. What is the probability that it returns to the starting
position after four time steps?
</p>

<p style="text-align:center">
<img src="/assets/images/mt7_ant.png"/>
</p>

<!--
SMT 2011 General. Ans: 21/81 = 7/27.
-->

</li>


<li>
<p>\(ABCD\) is a square such that the side \(AB\) lies on the line \(y=x+4\) and the points \(C\) and \(D\) lie
on the parabola \(y^2 = x \). Find a possible set of values for the points \(A,B,C\) and \(D\).
</p>
</li>

<!--
SMT 2013 Geometry.
-->



</ol>



## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.

---



<p>
<b>B1.</b> \(ABCD\) is a cyclic quadrilateral with side lengths as follows.  \(AB = 6\) cm,
\(BC = 12\) cm, \(CD = 3\) cm and \(DA = 6\) cm. Find the length of \(EF\)
in the figure shown below.
</p>

<p style="text-align:center">
<img src="/assets/images/mt7_cyclic.png"/>
</p>

<!--
SMT. Ans = 10\sqrt{2}. Use similar triangles.
-->


---

<p>
<b>B2.</b>
Count the number of ordered pairs of positive integers \( (a, b) \)
such that the complex number \(z=a+bi\)  satisfies \(|z+2|^{2}+|z-2|^{2}<40\).
<br>
</p>


<!--
The inequality reduces to

\begin{align*}
(2+z)(2+\bar{z})+(2-z)(2-\bar{z}) & < 50 \\
\Rightarrow 4+2 z+2 \bar{z}+z \bar{z}+4-2 z-2 \bar{z}+z \bar{z} & < 50 \\
\Rightarrow 8+2|z|^{2} & < 50 \\
\Rightarrow a^{2}+b^{2} & < 21
\end{align*}


So we need to compute the number of ordered pairs of positive integers
\( (a, b) \) such that \( a^{2}+b^{2}<21 \).
When \(a=1, b\) can range from 1 to 4 (inclusive);
when \(a=2, b\) can range from 1 to 4 ; when \(a=3, b\) can range from 1
to 3 ; and when \(a=4, b\) can equal 1 or 2 , for a total of 13 ordered pairs.
-->

---

<p>
<b>B3.</b> Let \([n]\) denote the set of numbers \( \{1,2,\ldots,n\} \). A bijection \(f:[n] \rightarrow [n]\)
is said to be <i>neat</i> if for every \(i \in \{2,3,\ldots,n\}\) we can find
a \(j< i\) such that \( |f(i)-f(j)| = 1 \).<br>

(a) Prove that if \(f\) is neat bijection, then either \(f(n)=1\) or \(f(n)=n\). [4 marks]<br>
(b) Find the number of neat bijections. [6 marks]  <br>

</p>


<!--
https://prase.cz/kalva/putnam/psoln/psol655.html
-->

---


<p>
<b>B4.</b> For any given \(k\), show that the following equation has a solution where \(x_i\geq 3\) for all \(i\) and \(y\geq 3\).

\[ x_{1} !x_{2} ! \cdots x_{k} !=y ! \]

</p>



---


<p><b>B5.</b> Let \( A=(0,0) \) and \( C=(1,0) \). Let \(B\) be a point
on the line \(y=x+1\). Suppose \(B\) is the point of tangency of a circle
with chord \(AC\). In other words, a circle with chord \(AC\) touches the
line \(y=x+1\) at point \(B\).<br>

(a) Find all possible values of point \(B\). [5 marks]<br>

(b) Among the possible values found in (a), for which value is
the angle \(ABC\) maximized? Explain. [5 marks]

</p>

---

<p><b>B6.</b>

Let \(A\) be a sequence of \(n\) positive integers.
Let us note down the sum of every sub-sequence of \(A\) into a set \(S\).
The sequence \(A\) is called <i>k-good</i> if \(S\) contains all the values in the range \( \{1..k\}\).<br>

For example, the sequence \([1, 2, 3]\) is 3-good but not 4-good. <br><br>
The sequence \([1, 3, 2]\) is 6-good. The subsequences that give numbers upto 6 are:\( [1],[2],[3],[1,3],[3,2],[1,2,3]\).<br><br>


Find a sequence \(A\) of length 20 that is 100-good.

</p>






