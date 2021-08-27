---
layout: default
title: Triangles
parent: Geometry
nav_order: 1
---


# Triangles
{: .no_toc}

#### Problems
{: .no_toc  }

1. TOC
{:toc}

---


### Possible triangles
{: .d-inline-block}

A3, 2021
{: .label}

<p>
\(ABC\) is a triangle such that \(AB=1\) cm and \(\angle CAB = 20.21^{\circ}\). Let \(N(x)\) denote the number of non-congruent triangles
such that \(BC=x\) cm, where \(x\) is a positive real number.  There exists an \(x\) such that:<br>
(a)  \(N(x)=0\).<br>
(b)  \(N(x)=1\).<br>
(c)  \(N(x)=2\).<br>
(d)  \(N(x)=3\).<br>
</p>


<details><summary>Solution</summary>
(a) True.<br>
(b) True.<br>
(c) True.<br>
(d) False. <br>

<i>Explanation. </i> Consider the line \(l\) that passes through \(A\) at an angle \(20.21^\circ\) to \(AB\). Let the length
of the shortest distance from \(l\) to \(B\) be \(d\). If \(x< d\) there is no solution. If \(x=d\) there is
exactly one solution. If \(1>x>d\), there are two solutions.<br>

</details>



---


### Midpoint of a median
{: .d-inline-block}

B2, 2010
{: .label}

<p>
Take a triangle ABC and draw BE as a median. Suppose M is the mid-point of BE.
The line passing through points A and M  meets BC at D.  What is the ratio AM:MD?
</p>

<p>
Hint: Draw a line from E that is parallel to AD.
</p>

<p style="text-align:center;"><img src="/assets/images/B2_2011.svg"></p>

<details open><summary>Solution</summary>

<p>
The hint gives away the problem. We solve the problem by using similarity of triangles.
</p>


<p>
(i) \( \triangle ADC \sim \triangle EFC \)
</p>

<p>
Equality AE = EC \(\implies\)  AC=2EC \(\implies\) AD=2EF.
</p>

<p>
(ii) \( \triangle BMD \sim \triangle BEF \)
</p>

<p>
Equality BM = ME \(\implies\)  MD=EF/2.
</p>

<p>
From (i) and (ii), we have 4MD=AD. So, the ratio AM:MD=3.
</p>


</details>


---

### Isoceles triangle
{: .d-inline-block}

B1, 2013
{: .label}

<p>
In triangle PQR, the bisector of angle P meets side QR in point D and the bisector of angle Q meets side PR in point E. Given that DE is parallel to PQ, show that PE = QD and that the triangle PQR is isosceles.
</p>


<p style="text-align:center;"><img src="/assets/images/2013_bisector_isoceles.svg"></p>


<details><summary>Solution</summary>

<p>
<i>Claim</i>. \(\angle E P D=\angle D P Q=\angle E D P\)
</p>
<p>
<i>Proof.</i> The first equality comes from the problem statement.
</p>

<p>
Consider the second equality. Alternate angles made by line \(P D\) intersecting parallel lines \(D E\) and \(P Q\) are equal.
Thus \(\triangle E P D\) is isosceles with \(E P=E D \).
Similarly \(E D=D Q\) using the fact that \(Q E\) bisects \(\angle D Q P\) also intersects parallel lines \(D E\) and \(P Q\).
Therefore \(E P=\) \(E D=D Q .\) Now by the basic proportionality theorem, \(\frac{R E}{E P}=\frac{R D}{D Q} .\) As the denominators \(E P\) and \(D Q\) are equal, the numerators must be equal as well, i.e., \(R E=R D .\) Finally, \(R P=R E+E P=R D+D Q=R Q,\) so \(\triangle P Q R\) is isosceles.
</p>


</details>




---


### A chord within a rectangle
{: .d-inline-block}

A2, 2011
{: .label}

In a rectangle ABCD, the length BC is twice the width AB. Pick a point P on side BC
such that the lengths of AP and BC are equal. The measure of angle CPD is

- [ ] \\(75^{\circ}\\)
- [ ] \\(60^{\circ}\\)
- [ ] \\(45^{\circ}\\)
- [ ] none of the above



<details>
<summary>Solution</summary>
<p>

Let the length of AB be one unit and BC be two units, respectively. We draw a perpendicular from vertex P to X. Since APX is a right angled triangle:

\begin{align}
AX^2 &= AP^2 - PX^2  \\\\
AX^2 &= 2^2 - 1^2  \\\\
AX &= \sqrt{3} \\\\
\end{align}

Hence, the length of CP is \( 2-\sqrt{3} \). The angle CPD is \( \arctan \frac{1}{CP}  = \arctan \frac{1}{2 - \sqrt{3}} \) .

We can verify that the answer is \( 75^{\circ} \).



<p style="text-align:center;"><img src="/assets/images/rectangle_2011.svg"></p>


\begin{align}
\tan(A+B) &= \frac{\tan A + \tan B}{1-\tan A \tan B} \\\\
\tan(45+30) &= \frac{\tan 45 + \tan 30}{1-\tan 45 \tan 30} \\\\
&= \frac{1 + 1/\sqrt{3}}{1-1/\sqrt{3}}\\\\
&= \frac{\sqrt{3}+1}{\sqrt{3}-1} = \frac{2}{(\sqrt{3}-1)^2}\\\\
&= \frac{1}{2-\sqrt{3}}\\\\
\end{align}

</p>
</details>


---

### Non-congruent triangles with fixed perimeter
{: .d-inline-block}

A8, 2018
{: .label}


<p>
How many non-congruent triangles are there with integer lengths \(a \leq b \leq c\) such that \(a+b+c=20 ?\)
</p>

<details><summary>Solution</summary>

<p>
It is clear that \(1< a \leq b \leq c<10\). Now, \(c< a+b\) and \(c=20-a-b\) implies \(10< a+b ;\) this also means that \(b \geq a\) and \(b \geq 11-a\). Moreover, we also have \(b \leq 20-a-b .\) One can further conclude that \(a \leq 6,\) otherwise
\(7 \leq b \leq 6 .\) So as \(a\) ranges from 2 to 6 we have that \(b\) takes the following values
\(a=2, b=9 ; a=3, b=\) \(8 ; a=4, b \in\{7,8\} ; a=5, b \in\{6,7\} ; a=6, b \in\{6,7\} .\) The total number of possible
triangles is 8.
</p>

</details>

---

### Triangle construction
{: .d-inline-block}

A10, 2014
{: .label}

<p>
In each of the following independent situations we want to construct a triangle \(A B C\) satisfying the given conditions. In each case state state how many such triangles \(A B C\) exist up to congruence.<br>
(i) \(A B=30 \quad B C=95 \quad A C=55\).<br>
(ii) \(\angle A=30^{\circ} \quad \angle B=95^{\circ} \quad \angle C=55^{\circ}\).<br>
(iii) \(\angle A=30^{\circ} \quad \angle B=95^{\circ} \quad B C=55\).<br>
\((\mathrm{iv}) \angle A=30^{\circ} \quad A B=95 \quad B C=55\).<br>
</p>

<details><summary>Solution</summary>

<p>
 \(0,\) infinite, 1,2
</p>


</details>

---

### Segments inside a triangle
{: .d-inline-block}

B4, 2018
{: .label}

<p>
Let \(A B C\) be an equilateral triangle with side length \(2 .\) Point \(A^{\prime}\) is chosen on side \(B C\) such that the length of \(A^{\prime} B\) is \(k<1\). Likewise points \(B^{\prime}\) and \(C^{\prime}\) are chosen on sides \(C A\) and \(A B\) with \(A C^{\prime}=C B^{\prime}=k\). Line segments are drawn from points \(A^{\prime}, B^{\prime}, C^{\prime}\) to their corresponding opposite vertices. The intersections of these line segments form a triangle, labeled \(P Q R\) in the interior.
Show that the triangle \(P Q R\) is an equilateral triangle with side length \(\frac{4(1-k)}{\sqrt{k^{2}-2 k+4}}\).
</p>

<p style="text-align:center;"><img src="/assets/images/2018_b4.png"></p>

<details><summary>Solution</summary>

<p>
Note that triangles \(A B A^{\prime}, C A C^{\prime}\) and \(B C B^{\prime}\) are congruent by the SAS test. Triangles \(B A^{\prime} Q, C B^{\prime} R\) and \(A C^{\prime} P\) are a lso congruent. By using the property of opposite angles we get that all the three angles of the triangle \(P Q R\) are the same. Hence it is an equilateral triangle.

Dropping the perpendicular bisector \(A O\) on the side \(B C\) we get the following :
\[
\begin{aligned}
A A^{\prime 2} &=A O^{2}+A^{\prime} A^{2} \\
&=(1-k)^{2}+(\sqrt{3})^{2} \\
&=k^{2}-2 k+4
\end{aligned}
\]
Observe that triangles \(A B A^{\prime}\) and \(B Q A^{\prime}\) are similar by the AAA test: \(A^{\prime} Q B\) and \(A^{\prime} B A\) are 60 degrees and \(A^{\prime} B Q\) and \(A^{\prime} A B\) are corresponding angles. Therefore:
\[
\begin{aligned}
\frac{A B}{B Q} &=\frac{B A^{\prime}}{Q A^{\prime}}=\frac{A^{\prime} A}{A^{\prime} B} \\
\frac{2}{B Q} &=\frac{k}{Q A^{\prime}}=\frac{\sqrt{k^{2}-2 k+4}}{k} \\
B Q &=\frac{2 k}{\sqrt{k^{2}-2 k+4}} \\
Q A^{\prime} &=\frac{k^{2}}{\sqrt{k^{2}-2 k+4}}
\end{aligned}
\]
Now using \(A A^{\prime}=A P+P Q+Q A^{\prime}\) we get
\[
P Q=\frac{4(1-k)}{\sqrt{k^{2}-2 k+4}}
\]


</p>


</details>


---



### Rhombus within a triangle
{: .d-inline-block}

A12, 2010
{: .label}


In an isoceles triangle ABC  with A at the apex, the height and the base are both equal to
1cm. Points D, E and F are chosen from each side such that BDEF is a rhombus.  Find the length of the side of this rhombus.

<details>
<summary>Solution</summary>
<p>
We want to find the side length of the rhombus \(BDEF\).  We will find the length of \(EF\) first. Let \( AX \) and \( EX' \) be the perpendiculars of triangles \(ABC\) and \(EFC\), respectively.

<p style="text-align:center;"><img src="/assets/images/cmi2010_bisector.svg"></p>

We know that \( FX'= EX'/2 \)  since \( ABC \cong EFC \).

\begin{align}
EF &= \frac{\sqrt{5}}{2}EX' \hskip{3pt} \text{since }EX'F\text{ is a right angled triangle}
\label{eq:triangle}\tag{1}
\end{align}


All we have to do is find the length of \( EX' \).

\begin{align}
\tan \theta & = \frac{EX'}{BX'} \\
\tan \theta & = \frac{EX'}{BC-X'C} \\
& = \frac{EX'}{1 - EX'/2} \hskip{5pt} \text{ since } ABX \cong EFX' \\
EX' & = \frac{2\tan \theta}{2+\tan \theta} \hskip{5pt} \text{ by rearranging } \label{eq:ex}\tag{2} \\
\\
\\
\tan 2\theta & = \frac{AX}{BX} = \frac{2\tan \theta}{1-\tan^2\theta} \\
2 & = \frac{2\tan \theta}{1-\tan^2\theta} \\
\tan \theta & = \frac{-1+\sqrt{5}}{2} \\
EX' & = (2\sqrt{5}-4) \hskip{5pt} \text{by substituting the value of }\tan \theta\text{ in \eqref{eq:ex}}
\\
\\
EF & = \frac{\sqrt{5}}{2}(2\sqrt{5}-4) \hskip{5pt} \text{From \eqref{eq:triangle}} \\
 & = (5-2\sqrt{5})
\end{align}



Hence the side length of the rhombus is  \( (5-2\sqrt{5}) \) cm.
</p>

</details>

---

### Rational triangle
{: .d-inline-block}

B4, 2010
{: .label}

If all the sides and area of a triangle were rational numbers then show that the
triangle is got by ‘pasting’ two right-angled triangles having the same property.

<details>
<summary>Solution</summary>
<p>
Let ABC be a triangle with rational sides and rational area. Let \( B\) be the largest angle.

<p style="text-align:center;"><img src="/assets/images/triangle_slice.svg"></p>

Drop a perpendicular from the largest angled corner. We get two right angled triangles with altitude \(BD\).

\[ \Delta ABC = \frac{1}{2}AC\cdot BD \]

Hence, \( BD\) must be rational.

Now we need to show that \(AD\) and \(DC\) are rational.


\begin{align}
AD^2 + BD^2 &= AB^2\\
DC^2 + BD^2 &= BC^2\\
AD^2 - DC^2 &= AB^2 - BC^2\\
AD - DC &= \frac{AB^2 - BC^2}{AD+DC}\\
AD - DC &= \frac{AB^2 - BC^2}{AC}
\end{align}


Hence, \(AD-DC\) is rational. Together with the fact that \(AD+DC\) is rational, we infer that \(AD\) and \(DC\) must be rational too. <br>

<b>Try this</b>. Prove that any rational triangle can be split into two rational triangles one of which is similar to the original one.
</p>

</details>


---

### Triangle with segments
{: .d-inline-block}

A10, 2016
{: .label}

<p>

You are given a triangle ABC, a point D on segment AC, a point E on segment. AB and a point F on segment BC.
Let BD and CE intersect in point P. Join P with F. Suppose that the following is true:<br>
\(\angle\)EPB=\(\angle\)BPF=\(\angle\)FPC=\(\angle\)CPD  and PD=PE=PF.


An indicative triangle is shown below, there could be other triangles too.

<p style="text-align:center;"><img src="/assets/images/2016_q10.png"></p>

<ul>
<li>(i) AP must bisect \(\angle\) BAC.</li>
<li>(ii) \(\triangle\) ABC must be isosceles.</li>
<li>(iii) A, P, F must be collinear.</li>
<li>(iv) \(\angle\) BAC must be \(60^{\circ}\)</li>
</ul>
</p>


<details><summary>Solution</summary>

<p>

TFFT<br>

(i) BP and CP are angle bisectors meeting at P, so AP bisects \(\angle\)A since the angle bisectors are concurrent. <br>

(iv) The angles marked with symbol o at point P are all \(60^{\circ}\) because \(\angle\)EPD is twice this common value.
It follows that half the sum of \(\angle\)B and \(\angle\)C is \(60^{\circ}\). So \(\angle\)A is \(60^{\circ} \).  <br>

The others are false, in fact check that any triangle with \(\angle A=60^{\circ},\) angle bisectors BD and CE,
their point of intersection P and PF bisecting \(\angle\)BPC will satisfy the given data.
</p>


</details>

---



### Matching pairs of points
{: .d-inline-block}

B6a, 2012
{: .label}


<p>
For \(n>1\), a configuration consists of \(2 n\) distinct points in a plane, \(n\) of them red, the remaining \(n\) blue, with no three points collinear. A pairing consists of \(n\) line segments, each with one blue and one red endpoint, such that each of the given \(2 n\) points is an endpoint of exactly one segment. Prove the following.
a) For any configuration, there is a pairing in which no two of the \(n\) segments intersect. (Hint: consider total length of segments.)
</p>

<details><summary>Solution</summary>

<p>
For any configuration, there are only finitely many pairings. Choose one with least possible total length of segments. Here no two of the \(n\) segments can interest, because if \(R B\) and \(R^{\prime} B^{\prime}\) intersect in point \(X\) then we get a contradiction as follows. Using triangle inequality in triangles \(R X B^{\prime}\) and \(R^{\prime} X B,\) we get \(R B^{\prime}+R^{\prime} B<R B+R^{\prime} B^{\prime}\) (draw a picture). So replacing \(R B\) and \(R^{\prime} B^{\prime}\) with \(R^{\prime} B\) and \(R B^{\prime}\) would give a pairing with smaller total length.
</p>

</details>

---





### Red-blue points
{: .d-inline-block}

B6b, 2012
{: .label}

<p>
Given \(n\) red points (no three collinear), we can place \(n\) blue points such that any pairing in the resulting configuration will have two segments that do not intersect.
</p>

<details><summary>Solution</summary>

<p>
Given \(n\) red points, find a triangle \(A B C\) such that \(A\) is a red point and all other red points are inside triangle \(ABC\). This is always possible since \(B\) and \(C\) can be placed anywhere, as long as \(ABC\) is a triangle. Place one blue point at \(B\) and \(n-1\) blue points at \(C\). This will ensure that
there will be a non-intersecting pair of lines involving vertex \(A\).
</p>


</details>

---

### Square inside a hexagon
{: .d-inline-block}

B6, 2017
{: .label}



<p>
You are given a regular hexagon. We say that a square is inscribed in the hexagon if it can be drawn in the interior such that all the four vertices lie on the perimeter of the hexagon.
<ul>
<li>(a) A line segment has its endpoints on opposite edges of the hexagon. Show that it passes through the center of the hexagon if and only if it divides the two edges in the same ratio.</li>
<li>(b) Suppose a square \(A B C D\) is inscribed in the hexagon such that \(A\) and \(C\) are on the opposite sides of the hexagon. Prove that center of the square is same as that of the hexagon.</li>
<li>(c) Suppose the side of the hexagon is of length \(1 .\) Then find the length of the side of the inscribed square whose one pair of opposite sides is parallel to a pair of opposite sides of the hexagon.</li>
<li>(d) Show that, up to rotation, there is a unique way of inscribing a square in a regular hexagon.</li>
</ul>

</p>



<details><summary>Solution</summary>

<p>

(a) Suppose a seg ment \(A C\) meets with opposite sides \(P Q\) and \(T S\) of a hexagon and \(O\) is the midpoint of \(A C .\) We show that
\(\frac{P A}{A Q}=\frac{T C}{C S} \Longleftrightarrow O\) is the center of the hexagon.

If \(O\) is the center of the hexagon, consider triangles \(O A Q\) and \(O C S .\) By the \(S A S\) test these are congruent. Similarly, triangles \(O A P\) and \(O C T\) are congruent. Conversely, suppose \(\frac{P A}{A Q}=\frac{T C}{C S}=k(\) say \(),\) then

\[
P Q=T S \Longrightarrow P A+A Q=T C+C S \Longrightarrow A Q(k+1)=C S(k+1) \Longrightarrow A Q=C S
\]

<br>

So \(\triangle A Q O \cong \triangle C T O,\) so that \(O Q=O T .\) Also, \(\angle A O Q=\angle C O T\) a nd \(\angle A O P=\) \(\angle C O S,\) so \(Q, O\) and \(T\) are collinear.
</p>

<br>

<p>
(b) Next suppose we have inscribed a square \(A B C D\) in a hexagon \(P Q R S T U\), with \(A\) on \(P Q, B\) on \(Q R, C\) on \(S T\) and \(D\) on \(T U\). We claim that \(\triangle A Q B\) is
congruent to \(\triangle C T D .\) This will prove that both diagonals pass through the center of the hexagon (using the criterion proved above). Proof: We know that \(P A \| S T\) and \(A C\) is a transversal. So \(\angle Q A C=\angle T C A\), also \(\angle B A C=\angle D C A=45^{\circ} .\) So \(\angle Q A B=\angle D C T\)
Similar ly, \(\angle Q B A=\angle C D T\). Also, \(\angle A Q B=\angle C T D,\) since they are angles in a regular hexagon. Moreover, \(A B=C D\). As a result we get that \(\triangle Q B A \cong\) \(\triangle T D C\)

So we have \(Q B=T D\) and \(Q A=T C\). This in turn implies that \(B R=D U\) and \(P A=C S\) Thus,
\[
\frac{Q B}{B R}=\frac{T D}{D U} \text { and } \frac{P A}{A Q}=\frac{S C}{C T}
\]

<br>
Hence \(A C\) and \(B D\) pass through the center of the hexagon.
</p>

<br>
<p>
(c) Let \(D U=x\) so \(D P=1-x\). Observe that \(D C=2 x \sin 30\) and \(D A=2(1-\)
\(x) \sin 60 .\) since \(D C=D A\) we solving the equations for \(x\) we get \(x=\frac{2}{\sqrt{3}+1}\) Consequently the side \(D C=\sqrt{3}(\sqrt{3}-1)\)
</p>
<br>

<p>
(d) Finally we want to show that there is a unique way of inscribing a square in a regular hexagon. Proof: It \(w\) ill be enough to show that the ratios \(\frac{Q B}{B R}\) and \(\frac{Q A}{A P}\) are equal. Suppose on the contrary that these ratios aren't equal. Let \(\angle Q A B=\alpha\) and \(\angle Q B A=\beta\). Note that then \(\angle O A Q=45^{\circ}+\alpha\) and \(\angle O B Q=45^{\circ}+\beta .\) Also, \(\alpha+\beta=60^{\circ},\) since \(\angle A Q B=120^{\circ}\)
Let \(A^{\prime}\) be a point on \(Q R\) such that \(\frac{Q A^{\prime}}{A^{\prime} R}=\frac{Q A}{A P}\). Since \(\triangle B O A^{\prime}\) is isosceles, \(\angle O B A^{\prime}\) equals \(\angle O A^{\prime} B,\) so that
\(180^{\circ}=\angle O B A^{\prime}+\angle O B Q=\angle O B Q+\angle O A^{\prime} B=\angle O B Q+\angle O A Q=45^{\circ}+\beta+45^{\circ}+\alpha\)
so \(\alpha+\beta=0^{\circ},\) a contradiction since \(\alpha+\beta=60^{\circ}\)
</p>


</details>

---

### Triangle in a square
{: .d-inline-block}

B1b, 2021
{: .label}

<p>
\(ABCD\) is a square. Point \(X\) lies on a circle with \(AY\) as the diameter. Points \(X\) and \(Y\) lie on the sides of the
square such that \(AX=4\) cm and \(AY=5\) cm. What is the area of the square \(ABCD\)?<br>
</p>

<p style="text-align:center">
<img src="/assets/images/cmi_2021_square.png"/>
</p>


<details><summary>Solution I via cyclic quadrilateral</summary>

<br><i>Sol. due to Abhishek Goel.</i><br><br>

Since \( \angle AXY + \angle ABY = 180^{\circ} \), \(AXYB\) is a cyclic quadrilateral.
Suppose the chord \(XY\) subtends an angle \(\theta\) at \(A\) and \(B\) as shown:

<p style="text-align:center">
<img src="/assets/images/cmi2021_b1_sol.png"/>
</p>


Let the side-length of the square be \(x\).

\begin{align*}
\text{From triangle } AXY \text{ we have} \tan \theta &= \frac{3}{4} \\
\text{From triangle } XCB \text{ we have} \tan \theta &= \frac{XC}{CB} \\
\therefore XC &= \frac{3}{4}x \\
DX &= x-XC = \frac{1}{4}x\\
AD^2+DX^2 &= AX^2\\
x^2+\left(\frac{x}{4}\right)^2 &= 4^2\\
x &= \frac{16}{\sqrt{17}}\\
\text{Area of the square} &= \frac{256}{17}
\end{align*}
</details>

<p></p>

<details><summary>Solution II via similar triangles</summary>
\begin{align*}
\angle DAX &= \angle CXY\\
\implies \Delta DAX &\sim \Delta CXY \\
\frac{XY}{AX} &= \frac{XC}{AD} \\
\frac{3}{4} &= \frac{XC}{AD} \\
XC &= \frac{3}{4} AD \\
DX &= CD-CX = \frac{1}{4}AD\\
AD^2+DX^2 &= 4^2\\
AD^2+\frac{AD^2}{16} &= 16\\
AD &= \frac{16}{\sqrt{17}}\\
\text{Area of the square} &= \frac{256}{17}
\end{align*}


<i>Problem source: <a href=" https://www.youtube.com/watch?v=aQsb5jfqSYo">Presh Talwalkar's channel</a>.</i>

</details>


---

### Midpoints of a quadrilateral
{: .d-inline-block}

B2a, 2012
{: .label}


<p>
Consider a convex quadrilateral \({ABCD}\). Let \({E}, {F}, {G}\) and \({H}\) be the midpoints of the sides \({AB}, {BC}, {CD}\) and \({DA}\), respectively. Show that \({EFGH}\) is a parallelogram whose area is half that of \({ABCD}\).
</p>

<p style="text-align:center;"><img src="/assets/images/B2a_2012.svg"></p>

<details><summary>Solution</summary>

<p>
<b>Lemma.</b> \(EFGH\) is a parallelogram.
</p>

<p>
<i>Proof.</i> Consider the diagonal \(AC\). By the basic proportionality theorem:

<ul>
<li> \({EF}\) and \({AC}\) are parallel.</li>
<li> \({AC}=2 {EF} \)</li>
<li> \(\Delta ABC \sim \Delta EBF\). </li>
</ul>
</p>


<p>
A similar argument to diagonal \(BD\) implies the lemma. \(\quad\square\)
</p>


<p>
Let \((X)\) denote the area of shape \(X\).
</p>


<p>
\begin{align}
(ABCD) = (ABC) + (ACD) \\
1/2 \cdot (ABCD) = (EFB) + (HGD)
\end{align}
</p>

<p>
By applying the above argument to the diagonal \(BD\) and triangles \(CFG\) and \(AEH\), we get the following:
</p>

<p>
\begin{align}
(ABCD) = (ABD) + (BCD) \\
1/2\cdot (ABCD) = (CFG) + (AEH)
\end{align}
</p>

<p>
Together we get:
</p>

<p>
\begin{align}
1/2\cdot (ABCD) &= (CFG) + (AEH) + (EFB) + (HGD) \\
(EFGH) &= \frac{1}{2} (ABCD)
\end{align}
</p>



</details>

---

### Specific midpoints
{: .d-inline-block}

B2b, 2012
{: .label}


<p>
Let \(E=(0,0)\), \(F=(0,-1)\), \(G=(1,-1)\) and \(H=(1,0)\). Find all points \({A}=(p, q)\) in the
first quadrant such that \({E}, {F}, {G}\) and \({H}\) respectively are the midpoints of the sides \({AB}\), \({BC}, {CD}\) and \({DA}\) of a convex quadrilateral \({ABCD}\).
</p>



<details><summary>Solution</summary>


<p>
Let us draw the square \(EFGH\) on the coordinate plane (see the figure below). From the previous problem we know
that the diagonals of \(ABCD\) must be parallel to the axes. Suppose the two diagonals lie on the lines \(x=p\) and \(y=-q\),
respectively. Since the diagonals pass through \(EFGH\), we must have \( p\in (0,1) \) and \( q\in(0,1) \).
</p>


<p>
<figure>
<p style="text-align:center;"><img src="/assets/images/B2b_2012.svg"></p>
<figcaption>In the figure, we are contemplating how the quadrilateral \(ABCD\) could be positioned if the diagonals lie on \(x=p\) and \(y=-q\). It turns out that fixing the diagonals determines the quadrilateral \(ABCD\) uniquely.</figcaption>
</figure>
</p>

<p></p>



<p><i>Notation.</i> Let \(\mbox{proj}_x PQ\) (resp. \(\mbox{proj}_y PQ\)) denote the length of the
projection of segment \(PQ\) on the \(x\)-axis (resp. \(y\)-axis).
</p>



<p>
<b>Lemma 1. </b> The coordinates of vertices \(A\) and \(B\) are \( (p,q) \) and \( (-p,-q) \), respectively.
</p>

<p>
Since \(E\) is the mid-point of \(AB\), we have \(|AE|=|BE|\).
</p>



<p>
\begin{align*}
    \mbox{proj}_y BE &= q = \mbox{proj}_y AE \implies  A=(p,q) \\
    \mbox{proj}_x AE &= p = \mbox{proj}_x BE \implies  B=(-p,-q) \quad\square
\end{align*}
</p>


<p>
<b>Lemma 2.</b> The coordinates of vertices \(C\) and \(D\) are \( (p,2-q) \) and \( (2-p,-q) \), respectively.
</p>

<p>
Let us calculate the \(y\)-coordinate of \(C\) first. Since \(F\) is the mid-point of \(BC\) we have \(|BF|=|CF|\).
</p>

<p>
\begin{align*}
\mbox{proj}_y BF &= 1-q = \mbox{proj}_y CF \implies  C=(p,2-q) \\
\end{align*}
</p>

<p>
Now we calculate the \(x\)-coordinate of \(D\). Since \(G\) is the mid-point of \(CD\) we have \(|CG|=|GD|\).
</p>

<p>
\begin{align*}
\mbox{proj}_x CG &= 1-p = \mbox{proj}_x GD \implies  D=(2-p,-q)  \quad\square
\end{align*}
</p>

<p>
From the above lemmas we infer that once the diagonals are fixed, the quadrilateral \(ABCD\) also gets fixed.
There is a one-to-one correspondence between the pair of numbers \( (p,-q) \) and the quadrilateral \(ABCD\).
The vertex \(A\) can take a value \((p,q)\) with \(p\in(0,1) \) and \(q \in (0,1) \). The set of all possible points for vertex \(A\)
is shaded in the above figure.
</p>



</details>



