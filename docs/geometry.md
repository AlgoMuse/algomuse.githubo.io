---
layout: default
title: Geometry
nav_order: 4
---


# Geometry
{: .no_toc}

#### Topics
{: .no_toc  }

1. TOC
{:toc}

---

## Triangles [11]


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
It is clear that \(1< a \leq b \leq c<10\). Now, \(c< a+b\) a nd \(c=20-a-b\) implies \(10< a+b ;\) this also means that \(b \geq a\) and \(b \geq 11-a\). Moreover, we a lso have \(b \leq 20-a-b .\) One can furt her conclude that \(a \leq 6,\) ot herw ise \(7 \leq b \leq 6 .\) So a s \(a\) ranges from 2 to 6 we have that \(b\) takes the follow ing values \(a=2, b=9 ; a=3, b=\) \(8 ; a=4, b \in\{7,8\} ; a=5, b \in\{6,7\} ; a=6, b \in\{6,7\} .\) The total number of possible
triangles is 8.
</p>

</details>

---

### Triangle construction
{: .d-inline-block}

A10, 2014
{: .label}

<p>
In each of the following independent situations we want to construct a triangle \(A B C\) satisfying the given conditions. In each case state state how many such triangles \(A B C\) exist up to congruence.
(i) \(A B=30 \quad B C=95 \quad A C=55\)
(ii) \(\angle A=30^{\circ} \quad \angle B=95^{\circ} \quad \angle C=55^{\circ}\)
(iii) \(\angle A=30^{\circ} \quad \angle B=95^{\circ} \quad B C=55\)
\((\mathrm{iv}) \angle A=30^{\circ} \quad A B=95 \quad B C=55\)
</p>

<details><summary>Solution</summary>

<p>
 \(0,\) infinite, 1,2
</p>


</details>

---


### Isosceles triangle
{: .d-inline-block}

A3, 2013
{: .label}

<p>
In triangle ABC, the bisector of angle A meets side BC in point D and the bisector of angle \(\mathrm{B}\) meets side \(\mathrm{AC}\) in point \(\mathrm{E}\). Given that \(\mathrm{DE}\) is parallel to \(\mathrm{AB},\) show that \(\mathrm{AE}=\mathrm{BD}\) and that the triangle \(\mathrm{ABC}\) is isosceles.
</p>

<details><summary>Solution</summary>

<p>
\(\angle E A D=\angle D A B=\angle E D A,\) the first equality because \(A D\) bisects \(\angle E A B\) and the second because alternate angles made by line \(A D\) intersecting parallel lines \(D E\) and \(A B\) are equal. Thus \(\triangle E A D\) is isosceles with \(E A=E D .\) Similarly \(E D=D B\) using the fact that \(B E\) bisects \(\angle D B A\) also intersects parallel lines \(D E\) and \(A B .\) Therefore \(E A=\) \(E D=D B .\) Now by the basic proportionality theorem, \(\frac{C E}{E A}=\frac{C D}{D B} .\) As the denominators \(E A\) and \(D B\) are equal, the numerators must be equal as well, i.e., \(C E=C D .\) Finally, \(C A=C E+E A=C D+D B=C B,\) so \(\triangle A B C\) is isosceles.
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

<details><summary>Solution</summary>

<p>
Note that triangles \(A B A^{\prime}, C A C^{\prime}\) and \(B C B^{\prime}\) are congr ue nt by the SAS test. Triang les \(B A^{\prime} Q, C B^{\prime} R\) and \(A C^{\prime} P\) are a lso co ngr ue nt. By using the property of opposite a ng les we get that all the three angles of the triangle \(P Q R\) are the same. Hence it is an equila teral triangle.

Dropping the perpendicular bisector \(A O\) on the side \(B C\) we get the follow ing :
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

B2, 2010
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

If \(O\) is the center of the hexagon, consider triangles \(O A Q\) and \(O C S .\) By the \(S A S\) test these are congruent. Similarly, triangles \(O A P\) and \(O C T\) are congr ue nt. Conver sely, suppose \(\frac{P A}{A Q}=\frac{T C}{C S}=k(\) say \(),\) then

\[
P Q=T S \Longrightarrow P A+A Q=T C+C S \Longrightarrow A Q(k+1)=C S(k+1) \Longrightarrow A Q=C S
\]

<br>

So \(\triangle A Q O \cong \triangle C T O,\) so that \(O Q=O T .\) Also, \(\angle A O Q=\angle C O T\) a nd \(\angle A O P=\) \(\angle C O S,\) so \(Q, O\) and \(T\) are collinear.
</p>

<br>

<p>
(b) Next suppose we have inscribed a square \(A B C D\) in a hexagon \(P Q R S T U\), with \(A\) on \(P Q, B\) on \(Q R, C\) on \(S T\) and \(D\) on \(T U\). We claim that \(\triangle A Q B\) is
congruent to \(\triangle C T D .\) This will prove that both diagonals pass thro ugh the center of the hexagon (using the criterion proved above). Proof: We know that \(P A \| S T\) and \(A C\) is a transver sal. So \(\angle Q A C=\angle T C A\), also \(\angle B A C=\angle D C A=45^{\circ} .\) So \(\angle Q A B=\angle D C T\)
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
(d) Finally we want to show that there is a unique way of inscribing a square in a reg ular hexagon. Proof: It \(w\) ill be enough to show that the ratios \(\frac{Q B}{B R}\) and \(\frac{Q A}{A P}\) are equal. Suppose on the contrary that the se rat ios aren't equal. Let \(\angle Q A B=\alpha\) and \(\angle Q B A=\beta\). Note that then \(\angle O A Q=45^{\circ}+\alpha\) and \(\angle O B Q=45^{\circ}+\beta .\) Also, \(\alpha+\beta=60^{\circ},\) since \(\angle A Q B=120^{\circ}\)
Let \(A^{\prime}\) be a point on \(Q R\) such that \(\frac{Q A^{\prime}}{A^{\prime} R}=\frac{Q A}{A P}\). Since \(\triangle B O A^{\prime}\) is isosceles, \(\angle O B A^{\prime}\) equals \(\angle O A^{\prime} B,\) so that
\(180^{\circ}=\angle O B A^{\prime}+\angle O B Q=\angle O B Q+\angle O A^{\prime} B=\angle O B Q+\angle O A Q=45^{\circ}+\beta+45^{\circ}+\alpha\)
so \(\alpha+\beta=0^{\circ},\) a contradiction since \(\alpha+\beta=60^{\circ}\)
</p>


</details>

---




## Quadrilaterals [3]


### Interior point in a parallelogram
{: .d-inline-block}

B4, 2019
{: .label}


<p>
Let \(A B C D\) be a parallelogram. Let \(O\) be a point in its interior such that \(\angle A O B+\) \(\angle D O C=180^{\circ} .\)
Show that \(\angle O D C=\angle O B C\).
</p>

<details><summary>Solution</summary>

<p>
Note that there exists an external point \(P\) such that \(A P\) is parallel to \(D O, B P\) is parallel to \(C O\) and \(O P\) is parallel to \(B C\).
Now \(A O B P\) is a cyclic quadrilateral. Rest is a straight-forward calculation involving angles.
</p>




</details>

---



### Midpoints of a quadrilateral
{: .d-inline-block}

B2a, 2012
{: .label}


<p>
Consider a convex quadrilateral \(\mathrm{ABCD}\). Let \(\mathrm{E}, \mathrm{F}, \mathrm{G}\) and \(\mathrm{H}\) be the midpoints of the sides \(\mathrm{AB}, \mathrm{BC}, \mathrm{CD}\) and \(\mathrm{DA}\), respectively. Show that \(\mathrm{EFGH}\) is a parallelogram whose area is half that of \(\mathrm{ABCD}\).
</p>


<details><summary>Solution</summary>

<p>
Consider the diagonals AC and BD. By the basic proportionality theorem in triangle ABC, we get that \(\mathrm{EF}\) and \(\mathrm{AC}\) are parallel and \(\mathrm{AC}=2 \mathrm{EF} .\) Moreover, ABC and EBF are similar. Using triangles ADC and HDG, we similarly get that AC is parallel to HG, AC \(=2 \mathrm{HG}\). Thus EF and HG are parallel. Likewise FG and EH are parallel (both parallel to BD), so EFGH is a parallelogram. Also by similarity, Area(ABC) \(=4\) Area \((\mathrm{EBF}),\) Area \((\mathrm{ADC})=\) 4 Area \((\mathrm{HDG}),\) Area \((\mathrm{BAD})=4\) Area \((\mathrm{EAH})\) and \(\mathrm{Area}(\mathrm{BCD})=4\) Area \((\mathrm{FCG}) .\) ( Note. \(\mathrm{So}\)
far convexity of \(\mathrm{ABCD}\) is unnecessary. But the next steps need it, draw pictures and see. \()\)
\(\operatorname{Area}(\mathrm{EFGH})=\operatorname{Area}(\mathrm{ABCD})-[\operatorname{Area}(\mathrm{EBF})+\operatorname{Area}(\mathrm{FCG})+\operatorname{Area}(\mathrm{GDH})+\operatorname{Area}(\mathrm{HAE})]\)
\(=\operatorname{Area}(\mathrm{ABCD})-\frac{1}{4}[\operatorname{Area}(\mathrm{ABC})+\operatorname{Area}(\mathrm{BCD})+\operatorname{Area}(\mathrm{CDA})+\operatorname{Area}(\mathrm{DAB})]\)
\(=\operatorname{Area}(\mathrm{ABCD})-\frac{1}{2} \operatorname{Area}(\mathrm{ABCD})=\frac{1}{2} \operatorname{Area}(\mathrm{ABCD})\)
</p>

</details>

---

### Specific midpoints
{: .d-inline-block}

B2b, 2012
{: .label}


<p>
b) Let \(\mathrm{E}=(0,0), \mathrm{F}=(0,-1), \mathrm{G}=(1,-1), \mathrm{H}=(1,0) .\) Find all points \(\mathrm{A}=(p, q)\) in the
first quadrant such that \(\mathrm{E}, \mathrm{F}, \mathrm{G}\) and \(\mathrm{H}\) respectively are the midpoints of the sides \(\mathrm{AB}\), \(\mathrm{BC}, \mathrm{CD}\) and \(\mathrm{DA}\) of a convex quadrilateral \(\mathrm{ABCD}\).
</p>





<details><summary>Solution</summary>

<p>
If \(\mathrm{A}=(p, q)\) is such a point, then \(\mathrm{E}=(0,0)\) being the midpoint of \(\mathrm{AB}\) is equivalent to having \(\mathrm{B}=(-p,-q) .\) Similarly we get \(\mathrm{C}=(p, q-2), \mathrm{D}=(2-p,-q) .\) In particular \(\mathrm{AC}=\) \(\mathrm{BD}=2, \mathrm{AC}\) is vertical and \(\mathrm{BD}\) horizontal. By the reasoning in part a \(),\) these facts imply that the quadrilateral constructed from the midpoints of the sides of \(\mathrm{ABCD}\) is a square of side \(1 .\) So we just need to ensure that the listed coordinates make \(\mathrm{ABCD}\) into a convex quadrilateral. This happens if and only if \(p, q\) are both positive (which is given) and \(<1\). It is easy to see that these conditions are sufficient to make ABCD a convex quadrilateral. For necessity see the following (pictures will help). If \(p>1\) then \(A\) will be to the right of \(\mathrm{H}\) and so \(\mathrm{D}\) to the left of \(\mathrm{H.}\) If \(q>1,\) then \(\mathrm{B}\) will be below \(\mathrm{F}\) and so \(\mathrm{C}\) will be above \(\mathrm{F} .\) If \(p\) or \(q=1,\) then three of the points \(\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}\) become collinear. In all cases \(\mathrm{ABCD}\) will not be a convex quadrilateral. If both \(p, q>1,\) ABCD will even be self-intersecting.
</p>


</details>

---

## Circles [10]

### Circle inside a triangle inside a circle
{: .d-inline-block}

A1, 2017
{: .label}


<p>
Consider the following construction in a circle.
Choose points \(A, B, C\) on the given circle such that \(\angle A B C\) is \(60^{\circ}\) and \(A B=B C\).
Draw another circle that is tangential to the chords \(A B, B C\) and to the original circle.
Do the above construction in the unit circle to obtain a circle \(S_{1}\).
Repeat the process in \(S_{1}\) to obtain another circle \(S_{2} .\) What is the radius of \(S_{2}\)?
</p>

<details><summary>Solution</summary>

<p>
Consider the center \(\mathrm{O}\) and diameter \(\mathrm{BD}\) of the unit circle. It is easy to see that \(S_{1}\) passes through \(D\) and its center \(E\) lies between \(O\) and \(D .\) Let \(r\) be the radius of \(S_{1},\) so length of \(\mathrm{ED}\) is \(r .\) Consider the perpendicular from \(\mathrm{E}\) to chord \(\mathrm{BA}\), meeting \(\mathrm{BA}\) in point \(\mathrm{F}\). Then length of \(\mathrm{EF}\) is also \(r\) and therefore in the \(30-60-90\) triangle \(\mathrm{BEF}\), the length of the hypotenuse \(\mathrm{BE}\) is \(2 r .\) Thus \(2=\mathrm{BD}=\mathrm{BE}+\mathrm{ED}=3 r,\) thus \(r=\frac{2}{3} .\) By similarity, the radius of \(S_{2}\) is \(\frac{2}{2} \times \frac{2}{2}=\frac{4}{a}\)
</p>

</details>

---

### Progression of circles
{: .d-inline-block}

A1, 2018
{: .label}



<p>
Consider an equilateral triangle \(A B C\) with altitude 3 centimeters. A circle is inscribed in this triangle, then another circle
is drawn such that it is tangent to the inscribed circle and the sides \(A B, A C .\) Infinitely many such circles are drawn; each tangent to the previous circle and the sides \(A B, A C .\) The figure shows the construction after 2 steps.

Find the sum of the areas of all these circles.
</p>

<details><summary>Solution</summary>

<p>
The radius of the (first) inscribed circle is \(1 .\) Its not hard to see that that a s you go on inscribing the circles the corresponding radii decrease by \(1 / 3\). Let \(A\) denote the total area of these circles then

\[
\begin{aligned}
A &=\pi(1)^{2}+\pi(1 / 3)^{2}+\pi(1 / 9)^{2}+\cdots \\
&=\pi+\pi(1 / 3)^{2}\left[1+(1 / 3)^{2}+(1 / 9)^{2}+\cdots\right] \\
&=\pi+(1 / 9) A \\
&=(9 / 8) \pi
\end{aligned}
\]

</p>

</details>

---

### Circumcenter and orthocenter
{: .d-inline-block}

A3, 2013
{: .label}

<p>
Let \(S\) be a circle with center O. Suppose \(A, B\) are points on the circumference of \(S\) with \(\angle A O B=120^{\circ}\).
For triangle \(A O B,\) let \(C\) be its circumcenter and \(D\) its orthocenter (i.e., the point of intersection of the three lines containing the altitudes).
For each statement below, write whether it is TRUE or FALSE.

<ul>
<li> The triangle \(A O C\) is equilateral.</li>
<li> The triangle \(A B D\) is equilateral.</li>
<li> The point \(C\) lies on the circle \(S\).</li>
<li> The point \(D\) lies on the circle \(S\).</li>
</ul>

</p>


<details><summary>Solution</summary>

<p>
All the statements are true.

Draw a picture and see that the bisector of \(\angle A O B\) splits this angle into two angles of \(60^{\circ}\) each and meets the circle, say in point \(C^{\prime} .\) Now the triangles \(O A C^{\prime}\) and \(O B C^{\prime}\) are both equilateral, so \(A C^{\prime}=O C^{\prime}=B C^{\prime},\) making \(C^{\prime}=C,\) the cirumcenter of triangle \(A O B\).
Similarly, letting \(C D^{\prime}\) be a diameter of the circle \(S,\) it is easy to deduce that \(\angle A O D^{\prime}=\angle B O D^{\prime}=120^{\circ}\) and that triangle \(A B D^{\prime}\) is also equilateral with \(O\) as its centroid.
Hence \(C D^{\prime} \perp A B,\) line \(B O \perp A D^{\prime}\) and line \(A O \perp B D^{\prime},\) making \(D^{\prime}=D,\) the orthocenter of triangle \(A O B\).
</p>


</details>

---


### Cyclic polygon
{: .d-inline-block}

A11, 2014
{: .label}

<p>
A11. Let \(A_{n}=\) the area of a regular \(n\) -sided polygon inscribed in a circle of radius 1 (i.e., vertices of this regular \(n\) -sided polygon lie on a circle of radius 1 ).
(i) Find \(A_{12}\).
(ii) Find \(\left\lfloor A_{2014}\right\rfloor,\) i.e., the greatest integer \(\leq A_{2014}\)
</p>


<details><summary>Solution</summary>

<p>
3 and 3.
</p>

</details>

---

### Intersecting circles
{: .d-inline-block}

B6, 2010
{: .label}


<p>
Two circles of equal radii \(r\) pass through each others centers. Prove that the area of the overlapping region is \( \frac{r^2}{6}(4\pi - \sqrt{27})\).
</p>


<details>
<summary>Solution</summary>
<p>


The radius of each circle is \(r\). The required common area is same as twice the area of the sector ACD minus the area of the rhombus ACBD.

The rhombus ACBD is made up of two equilateral triangles so its area is \( 2\times \frac{\sqrt{3}}{4}\times r^2 \).

<p style="text-align:center;"><img src="/assets/images/intersect_circle.svg"></p>


\begin{align}
\text{Common area} &= 2\times \text{Area of sector ACD} - 2\times\Delta ABC \\\\
&= 2\times\frac{\pi}{3}r^2 - 2\times \frac{\sqrt{3}}{4}r^2 \\\\
&=\frac{r^2}{6}(4\pi - \sqrt{27})
\end{align}


</p>
</details>


---




### Quadrilateral with circles
{: .d-inline-block}

B6a, 2014
{: .label}

<p>
Two circles \(G_{1}, G_{2}\) intersect at points \(X, Y\). Choose two other points \(A, B\) on \(G_{1}\) as shown in the figure. The line segment from \(A\) to \(X\) is extended to intersect \(G_{2}\) at point \(L\). The line segment from \(L\) to \(Y\) is extended to meet \(G_{1}\) at point \(C\). Likewise the line segment from \(B\) to \(Y\) is extended to meet \(G_{2}\) at point \(M\) and the segment from \(M\) to \(X\) is extended to meet \(G_{1}\) at point \(D .\) Show that \(A B\) is parallel to \(C D\)
</p>

<details><summary>Solution</summary>

<p>
Draw segment \(B D .\) Now \(\angle B D C=\angle B Y C=\angle L Y M=\angle L X M=\angle A X D=\) \(\angle A B D,\) where the second and the fourth equalities are due to opposite angles and the other three equalities due to angles being in the same arc. Therefore \(A B\) and \(C D\) are parallel.
</p>


</details>

---

### On Ceva's theorem
{: .d-inline-block}

B6b, 2014
{: .label}

<p>
A triangle \(C D E\) is given. A point \(A\) is chosen between \(D\) and \(E\) A point \(B\) is chosen between \(C\) and \(E\) so that \(A B\) is parallel to \(C D .\) Let \(F\) denote the point of intersection of segments \(A C\) and \(B D .\) Show that the line joining \(E\) and \(F\) bisects both segments \(A B\) and segment \(C D .\) (Hint: You may use Ceva's theorem. Alternatively, you may additionally assume that the trapezium \(A B C D\) is a cyclic quadrilateral and proceed.)
</p>

<details><summary>Solution</summary>

<p>
Let line \(E F\) meet segment \(C D\) in point \(H\) and segment \(A B\) in point \(I .\) By Ceva's theorem in \(\triangle C D E,\) we have \(\frac{D A}{A E} \frac{E B}{B C} \frac{C H}{H D}=1 .\) As \(A B\) and \(C D\) are parallel, \(\frac{D A}{A E}=\frac{B C}{E B}\) so \(C H=D H .\) Also by the basic proportionality theorem, \(\frac{A I}{D H}=\frac{A E}{D E}=\frac{B E}{C E}=\frac{B I}{C H}\) and since \(C H=D H, A I=B I .\) (If you assume additionally that \(A B C D\) is cyclic, it is easy to see using equality of angles in the same arc and of alternate angles made by a transversal that the triangles \(D E C\) and \(D F C\) are isosceles and in fact line \(E F\) is the perpendicular bisector of segments \(C D\) and \(A B .)\)
</p>


</details>

---

### Straight-edge construction
{: .d-inline-block}

B6c, 2014
{: .label}

<i>Use the results of the previous two problems.</i>

<p>
Describe a procedure to do the following task: given two circles \(G_{1}\) and \(G_{2}\) intersecting at two points \(X\) and \(Y\) determine the center of each circle using only a straightedge.

<br>
A straightedge is a ruler without any markings. Given two points \(A, B,\) a straightedge allows one to construct the line segment joining \(A, B\).
Also, given any two non-parallel segments, we can use a straightedge to find the intersection point of the lines containing the two segments by extending them if necessary.

</p>

<details><summary>Solution</summary>

<p>
Extend \(A D\) and \(B C\) to meet in \(E\) and take \(F=\) the point of intersection of \(A C\) and \(B D .\) By parts (i) and (ii), the line \(E F\) is the bisector of two parallel chords and hence contains a diameter of the circle \(G_{1}\). Repeat the procedure with some other points \(A^{\prime}\) and \(B^{\prime}\) on \(G_{1}\) to get another diameter of \(G_{1}\). The intersection of the two diameters is the center of \(G_{1}\). Repeat the procedure for \(G_{2}\).

Note: If lines \(A D\) and \(B C\) do not meet, they are parallel. Then \(A B C D\) must be a rectangle (why?) and its diagonals are diameters, which intersect in the centre of \(G_{1}\). Note that here we have to assume that we can decide if two lines are parallel, which is implicit in the given assumption that if two lines intersect, then we can actually find the point of intersection by extending the given finite segments.
</p>


</details>

---


### Straight-edge with circle
{: .d-inline-block}

B6, 2015
{: .label}

<p>
You are given the following: a circle, one of its diameters \(A B\) and a point \(X\).
<br>

(a) Using only a straight-edge, show in the given figure how to draw a line perpendicular to \(A B\) passing through \(X .\) No credit will be given without full justification. (Recall that a straight-edge is a ruler without any markings. Given two points, a straight-edge can be used to draw the line passing through the given points.)

<br>

(b) Reconsider your procedure to see if it can be made to work if the point \(X\) is in some other position, e.g.,
when it is inside the circle or to the "left/right" of the circle.
Clearly specify all positions of the point \(X\) for which your procedure in part (a), or a small extension/variation of it, can be used to obtain the perpendicular to \(A B\) through \(X\).
Justify your answer.
</p>


<details><summary>Solution</summary>

<p>
(a) Line AX cuts the circle in C. Line BX cuts the circle in D. Lines AD and BC intersect in E. Line XE is perpendicular to line AB. Reason: Angles ADB and ACB are right angles, being angles in a semicircle. The altitudes of triangle \(\mathrm{XAB}\) are concurrent. Two of them are \(\mathrm{AD}\) and \(\mathrm{BC},\) so the third is contained in line XE.

<br>
(b) We will do a case-by-case analysis:<br>

<i>Case 1</i>: Suppose  X is not on the line AB so XAB is a triangle, nor on the  tangents to the circle at \(A\) (so line XA meets the circle in a point \(C\) different from \(A\) ),
nor on the tangent at \(\mathrm{B}\) (so line \(\mathrm{XB}\) meets the circle in a point \(\mathrm{D}\) different from \(\mathrm{B}\) ) nor on the given circle (so \(\mathrm{C}, \mathrm{D}\) and \(\mathrm{X}\) are all different). In this case the exact same procedure will work so long as we understand that the altitudes and their intersection point may lie outside triangle XAB. This is because the lines XA and XB meet the circle in two distinct points \(\mathrm{C}\) and \(\mathrm{D}\) that are different from \(\mathrm{X}, \mathrm{A}\) and \(\mathrm{B}\).

<br><br>

<i>Case 2</i>:  Suppose X is on one  of the  two tangents, say the tangent at A,but X is different from A.  In this case XA itself is the desired line! In terms of the construction, here we have \(\mathrm{A}=\mathrm{C}=\mathrm{E}\). Of course we have to assume that we can detect whether a line meeting a circle does so in one point or two. But this assumption is implicit in Case 1 also, because there we need to be able to identify the second point of intersection! <br>
<br><br>

<i>Case 3</i>: If \(\mathrm{X}\) is on line \(\mathrm{AB}\), then \(\mathrm{XAB}\) is not a triangle. If \(\mathrm{X}\) is not on line \(\mathrm{AB}\) but \(\mathrm{X}\) is on the circle, then \(\mathrm{XAB}\) is a triangle but \(\mathrm{X}=\mathrm{C}=\mathrm{D}=\mathrm{E},\) so we cannot draw line XE. Thus in these cases, the above procedure fails. <br>




</p>

</details>

---











### An old Russian problem
{: .d-inline-block}

B6, 2011
{: .label}

<p>In the quadrilateral ABCD shown below, AM and CN are the altitudes of the triangles ABD and CBD, respectively. Show that BN=DM.</p>

<p style="text-align:center;"><img src="/assets/images/cyclic_quad_ques.svg"></p>

<details>
<summary>Solution</summary>

The four points form the vertices of a cyclic quadrilateral with center as O. Drop a perpendicular from O to
DB with P as the base. P must bisect DB, so DP=BP.

<p style="text-align:center;"><img src="/assets/images/cyclic_quad_sol.svg"></p>

Here is the key.  Since AO = CO, their projections on BD are equal, so MP = NP. Subtracting gives DM = DP - MP = BP - NP = BN.


<p><i>Solution is due to Alexander Bogomolny who discussed this problem on <a href="https://www.cut-the-knot.org/Curriculum/Geometry/GeoGebra/ProjectionsInInscribedQuadrilateral.shtml">cut-the-knot</a> before it appeared in the CMI paper.</i></p>


</details>



---

## Co-ordinate system [5]



### Tangent to a cubic
{: .d-inline-block}

A4, 2014
{: .label}

<p>

Find the slope of a line \(L\) that satisfies both of the following properties:
(i) L is tangent to the graph of \(y=x^{3}\)
(ii) L passes through the point \((0,2000)\).
</p>

<details><summary>Solution</summary>

<p>
300
</p>


</details>

---

### Circles with pythagoras
{: .d-inline-block}

A6, 2015
{: .label}

<p>
Fill in the blanks. Let \(C_{1}\) be the circle with center (-8,0) and radius \(6 .\)
Let \(C_{2}\) be the circle with center (8,0) and radius 2.
Given a point \(P\) outside both circles, let \(\ell_{i}(P)\) be the length of a tangent segment from \(P\) to circle \(C_{i}\).
The locus of all points \(P\) such that \(\ell_{1}(P)=3 \ell_{2}(P)\) is a circle with radius \(\underline{\;\;}\) and center at \((\underline{\;\;}\;,\;\underline{\;\;})\).
</p>


<details><summary>Solution</summary>

<p>
Center \(=(10,0),\) radius \(=6\). Use the distance formula and the Pythagorean theorem to get \(y^{2}+(x+8)^{2}-6^{2}=9\left(y^{2}+(x-8)^{2}-4\right)\). Simplifying gives \(y^{2}+(x-10)^{2}=6^{2}\) Another way, assuming the locus to be a circle: note that the ratio of the radii of \(C_{1}, C_{2}\) and that of the tangents is the same (namely 3 ). Now use similar triangles to see that
2 the desired circle intersects the X-axis at coordinates 4 and 16, giving a diameter of the desired circle (why?)
</p>


</details>

---

### Circle touching a parabola
{: .d-inline-block}

B2, 2016
{: .label}

<p>
The <i>region</i> inside the parabola \(y=x^{2}\) is the set of points \((a, b)\) such that \(b \geq a^{2}\)
We are interested in those circles all of whose points are in this region.
A bubble at a point \(P\) on the graph of \(y=x^{2}\) is the largest such circle that contains \(P\).
Assume that there is a unique such circle at any given point on the parabola.

<ul>
<li> (a) A bubble at some point on the parabola has radius \(1 .\) Find the center of this bubble.</li>
<li> (b) Find the radius of the smallest possible bubble at some point on the parabola. Justify.</li>
</ul>

</p>


<details><summary>Solution</summary>

<p>
A bubble at the point \(P=\left(a, a^{2}\right)\) must be tangential to the parabola at \(\left(a, a^{2}\right) .\) (Why?) It must also be symmetric with respect to Y-axis (why?) and so its center \(O\) must be on the Y-axis. The radius \(O P\) of this bubble is perpendicular to the common tangent to the parabola and to the bubble at \(P .\) The slope of this tangent = \(2 a,\) so the slope of radius \(O P=\frac{-1}{2 a}(\) for \(a \neq 0) .\) Let \(Q=\left(0, a^{2}\right) .\) Using triangle \(O P Q\) slope of \(O P=\frac{-O Q}{a}=\frac{-1}{2 a}\). Therefore \(O Q=\frac{1}{2},\) regardless of the value of \(a\)
</p>

<p>
(a) By Pythagoras, \(O P^{2}=\left(\frac{1}{2}\right)^{2}+a^{2}=1 .\) So \(a^{2}=\frac{3}{4}\) and \(P=\left(0, \frac{3}{4}+\frac{1}{2}\right)=\left(0, \frac{5}{4}\right)\)
</p>

<p>
(b) For any nonzero \(a,\) the radius of the bubble satisfies \(O P^{2}=\left(\frac{1}{2}\right)^{2}+a^{2},\) so \(O P>\frac{1}{2}\) The smallest bubble is at the origin and its radius is \(\frac{1}{2}\). (One cannot just directly take \(a=0\) in the above calculations. Argue by continuity or do a separate calculation at the origin. \()\)
</p>



</details>

---

### Mix a sin and a circle
{: .d-inline-block}

B1, 2014
{: .label}

<p>
Find the area of the region in the \(X Y\) plane consisting of all points in the set
\[
\left\{(x, y) \mid x^{2}+y^{2} \leq 144 \text { and } \sin (2 x+3 y) \leq 0\right\}
\]
</p>

<details><summary>Solution</summary>

<p>
The area of the circular region \(S=\left\{(x, y) \mid x^{2}+y^{2} \leq 144\right\}\) is \(144 \pi .\) The condition \(\sin (2 x+3 y) \leq 0\) is equivalent to \(2 x+3 y\) being in one of the intervals \([k \pi,(k+1) \pi],\) where \(k\) is an odd integer. The key point is that due to the symmetry of the circle \(S\) about any diameter, in particular the diameter \(2 x+3 y=0,\) the strip inside \(S\) lying between the lines \(2 x+3 y=k \pi\) and \(2 x+3 y=(k+1) \pi\) is the mirror image of strip lying between the lines \(2 x+3 y=-k \pi\) and \(2 x+3 y=-(k+1) \pi .\) For each integer \(k,\) precisely one of these two equal strips is included in the desired area. Thus the desired area is half that of \(S,\) i.e., \(72 \pi\)
</p>


</details>

---


### Intersecting planes
{: .d-inline-block}

B2, 2017
{: .label}


<p>
Let \(L\) be the line of intersection of the planes \(x+y=0\) and \(y+z=0\)

<ul>
<li>(a) Write the vector equation of \(L\), i.e., find \((a, b, c)\) and \((p, q, r)\) such that
\(L=\{(a, b, c)+\lambda(p, q, r) \mid \lambda\) is a real number. \(\}\) </li>
<li>(b) Find the equation of a plane obtained by rotating \(x+y=0\) about \(L\) by \(45^{\circ}\) </li>
</ul>


</p>

<details><summary>Solution</summary>

<p>
Clearly the line \(L\) passes through the origin. Moreover \(L\) is in the direction perpendicular to the normals to the both the planes. The direction vector can be obtained by comp ut ing follow ing cross product
\[
(i+j) \times(j+\hat{k})=i-j+\hat{k}
\]
Hence \(L\) can be written as
\(L=\{(0,0,0)+\lambda(1,-1,1) \mid \lambda\) is a real number \(\}\)
First, note that the equation of a ny plane that contains the line \(L\) is given by
\[
x+(1+\lambda) y+\lambda z=0
\]
Second, note that one can rotate the plane \(x+y=0\) in either clockw ise or in a nticlo ckwise dire ction. Conseque nt ly there are two such planes. The normal of one of the planes makes an angle of \(45^{\circ}\) with the normal of \(x+y=0\) and the ot her normal makes an a ng le of \(135^{\circ}\).
\[
\begin{array}{c}
(i+j) \cdot(i+(1+\lambda) j+\lambda \hat{k})=\pm|i+j \| i+(1+\lambda) j+\lambda \hat{k}| \cos \left(\frac{\pi}{4}\right) \\
2+\lambda=\pm \sqrt{1+(1+\lambda)^{2}+\lambda^{2}} \\
\lambda^{2}-2 \lambda-2=0 \\
\lambda=1 \pm \sqrt{3}
\end{array}
\]
So the equation of the plane is
\[
x+y+(1 \pm \sqrt{3})(y+z)=0
\]

</p>


</details>



---




