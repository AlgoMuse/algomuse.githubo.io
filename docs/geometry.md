---
layout: default
title: Geometry
nav_order: 5
---


# Geometry
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

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

### A chord within a rectangle &#65290;
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


### Midpoints of a quadrilateral
{: .d-inline-block}

B2a, 2012
{: .label}


<p>
Consider a convex quadrilateral \(\mathrm{ABCD}\). Let \(\mathrm{E}, \mathrm{F}, \mathrm{G}\) and \(\mathrm{H}\) be the midpoints of the sides \(\mathrm{AB}, \mathrm{BC}, \mathrm{CD}\) and \(\mathrm{DA}\), respectively. Show that \(\mathrm{EFGH}\) is a parallelogram whose area is half that of \(\mathrm{ABCD}\).
</p>


Sol.

<p>
Consider the diagonals AC and BD. By the basic proportionality theorem in triangle ABC, we get that \(\mathrm{EF}\) and \(\mathrm{AC}\) are parallel and \(\mathrm{AC}=2 \mathrm{EF} .\) Moreover, ABC and EBF are similar. Using triangles ADC and HDG, we similarly get that AC is parallel to HG, AC \(=2 \mathrm{HG}\). Thus EF and HG are parallel. Likewise FG and EH are parallel (both parallel to BD), so EFGH is a parallelogram. Also by similarity, Area(ABC) \(=4\) Area \((\mathrm{EBF}),\) Area \((\mathrm{ADC})=\) 4 Area \((\mathrm{HDG}),\) Area \((\mathrm{BAD})=4\) Area \((\mathrm{EAH})\) and \(\mathrm{Area}(\mathrm{BCD})=4\) Area \((\mathrm{FCG}) .\) ( Note. \(\mathrm{So}\)
far convexity of \(\mathrm{ABCD}\) is unnecessary. But the next steps need it, draw pictures and see. \()\)
\(\operatorname{Area}(\mathrm{EFGH})=\operatorname{Area}(\mathrm{ABCD})-[\operatorname{Area}(\mathrm{EBF})+\operatorname{Area}(\mathrm{FCG})+\operatorname{Area}(\mathrm{GDH})+\operatorname{Area}(\mathrm{HAE})]\)
\(=\operatorname{Area}(\mathrm{ABCD})-\frac{1}{4}[\operatorname{Area}(\mathrm{ABC})+\operatorname{Area}(\mathrm{BCD})+\operatorname{Area}(\mathrm{CDA})+\operatorname{Area}(\mathrm{DAB})]\)
\(=\operatorname{Area}(\mathrm{ABCD})-\frac{1}{2} \operatorname{Area}(\mathrm{ABCD})=\frac{1}{2} \operatorname{Area}(\mathrm{ABCD})\)
</p>

---

### Specific midpoints
{: .d-inline-block}

B2b, 2012
{: .label}


<p>
b) Let \(\mathrm{E}=(0,0), \mathrm{F}=(0,-1), \mathrm{G}=(1,-1), \mathrm{H}=(1,0) .\) Find all points \(\mathrm{A}=(p, q)\) in the
first quadrant such that \(\mathrm{E}, \mathrm{F}, \mathrm{G}\) and \(\mathrm{H}\) respectively are the midpoints of the sides \(\mathrm{AB}\), \(\mathrm{BC}, \mathrm{CD}\) and \(\mathrm{DA}\) of a convex quadrilateral \(\mathrm{ABCD}\).
</p>

Sol.

<p>
If \(\mathrm{A}=(p, q)\) is such a point, then \(\mathrm{E}=(0,0)\) being the midpoint of \(\mathrm{AB}\) is equivalent to having \(\mathrm{B}=(-p,-q) .\) Similarly we get \(\mathrm{C}=(p, q-2), \mathrm{D}=(2-p,-q) .\) In particular \(\mathrm{AC}=\) \(\mathrm{BD}=2, \mathrm{AC}\) is vertical and \(\mathrm{BD}\) horizontal. By the reasoning in part a \(),\) these facts imply that the quadrilateral constructed from the midpoints of the sides of \(\mathrm{ABCD}\) is a square of side \(1 .\) So we just need to ensure that the listed coordinates make \(\mathrm{ABCD}\) into a convex quadrilateral. This happens if and only if \(p, q\) are both positive (which is given) and \(<1\). It is easy to see that these conditions are sufficient to make ABCD a convex quadrilateral. For necessity see the following (pictures will help). If \(p>1\) then \(A\) will be to the right of \(\mathrm{H}\) and so \(\mathrm{D}\) to the left of \(\mathrm{H.}\) If \(q>1,\) then \(\mathrm{B}\) will be below \(\mathrm{F}\) and so \(\mathrm{C}\) will be above \(\mathrm{F} .\) If \(p\) or \(q=1,\) then three of the points \(\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}\) become collinear. In all cases \(\mathrm{ABCD}\) will not be a convex quadrilateral. If both \(p, q>1,\) ABCD will even be self-intersecting.
</p>



---




### Matching pairs of points
{: .d-inline-block}

B6a, 2012
{: .label}


<p>
For \(n>1\), a configuration consists of \(2 n\) distinct points in a plane, \(n\) of them red, the remaining \(n\) blue, with no three points collinear. A pairing consists of \(n\) line segments, each with one blue and one red endpoint, such that each of the given \(2 n\) points is an endpoint of exactly one segment. Prove the following.
a) For any configuration, there is a pairing in which no two of the \(n\) segments intersect. (Hint: consider total length of segments.)
</p>

Sol.

<p>
For any configuration, there are only finitely many pairings. Choose one with least possible total length of segments. Here no two of the \(n\) segments can interest, because if \(R B\) and \(R^{\prime} B^{\prime}\) intersect in point \(X\) then we get a contradiction as follows. Using triangle inequality in triangles \(R X B^{\prime}\) and \(R^{\prime} X B,\) we get \(R B^{\prime}+R^{\prime} B<R B+R^{\prime} B^{\prime}\) (draw a picture). So replacing \(R B\) and \(R^{\prime} B^{\prime}\) with \(R^{\prime} B\) and \(R B^{\prime}\) would give a pairing with smaller total length.
</p>

---





### Red-blue points
{: .d-inline-block}

B6b, 2012
{: .label}

<p>
Given \(n\) red points (no three collinear), we can place \(n\) blue points such that any pairing in the resulting configuration will have two segments that do not intersect.
</p>

Sol.

<p>
Given \(n\) red points, find a triangle \(A B C\) such that \(A\) is a red point and all other red points are inside triangle \(ABC\). This is always possible since \(B\) and \(C\) can be placed anywhere, as long as \(ABC\) is a triangle. Place one blue point at \(B\) and \(n-1\) blue points at \(C\). This will ensure that
there will be a non-intersecting pair of lines involving vertex A.
</p>


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


Sol.

<p>
All the statements are true.

Draw a picture and see that the bisector of \(\angle A O B\) splits this angle into two angles of \(60^{\circ}\) each and meets the circle, say in point \(C^{\prime} .\) Now the triangles \(O A C^{\prime}\) and \(O B C^{\prime}\) are both equilateral, so \(A C^{\prime}=O C^{\prime}=B C^{\prime},\) making \(C^{\prime}=C,\) the cirumcenter of triangle \(A O B\).
Similarly, letting \(C D^{\prime}\) be a diameter of the circle \(S,\) it is easy to deduce that \(\angle A O D^{\prime}=\angle B O D^{\prime}=120^{\circ}\) and that triangle \(A B D^{\prime}\) is also equilateral with \(O\) as its centroid.
Hence \(C D^{\prime} \perp A B,\) line \(B O \perp A D^{\prime}\) and line \(A O \perp B D^{\prime},\) making \(D^{\prime}=D,\) the orthocenter of triangle \(A O B\).
</p>


---


### Isosceles triangle
{: .d-inline-block}

A3, 2013
{: .label}

<p>
In triangle ABC, the bisector of angle A meets side BC in point D and the bisector of angle \(\mathrm{B}\) meets side \(\mathrm{AC}\) in point \(\mathrm{E}\). Given that \(\mathrm{DE}\) is parallel to \(\mathrm{AB},\) show that \(\mathrm{AE}=\mathrm{BD}\) and that the triangle \(\mathrm{ABC}\) is isosceles.
</p>

Sol.

<p>
\(\angle E A D=\angle D A B=\angle E D A,\) the first equality because \(A D\) bisects \(\angle E A B\) and the second because alternate angles made by line \(A D\) intersecting parallel lines \(D E\) and \(A B\) are equal. Thus \(\triangle E A D\) is isosceles with \(E A=E D .\) Similarly \(E D=D B\) using the fact that \(B E\) bisects \(\angle D B A\) also intersects parallel lines \(D E\) and \(A B .\) Therefore \(E A=\) \(E D=D B .\) Now by the basic proportionality theorem, \(\frac{C E}{E A}=\frac{C D}{D B} .\) As the denominators \(E A\) and \(D B\) are equal, the numerators must be equal as well, i.e., \(C E=C D .\) Finally, \(C A=C E+E A=C D+D B=C B,\) so \(\triangle A B C\) is isosceles.
</p>

---

### Tangent to a cubic
{: .d-inline-block}

A4, 2014
{: .label}

<p>

Find the slope of a line \(L\) that satisfies both of the following properties:
(i) L is tangent to the graph of \(y=x^{3}\)
(ii) L passes through the point \((0,2000)\).
</p>

Sol.

<p>
300
</p>


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

Sol.

<p>
 \(0,\) infinite, 1,2
</p>


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


Sol.

<p>
3 and 3.
</p>

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

Sol.

<p>
The area of the circular region \(S=\left\{(x, y) \mid x^{2}+y^{2} \leq 144\right\}\) is \(144 \pi .\) The condition \(\sin (2 x+3 y) \leq 0\) is equivalent to \(2 x+3 y\) being in one of the intervals \([k \pi,(k+1) \pi],\) where \(k\) is an odd integer. The key point is that due to the symmetry of the circle \(S\) about any diameter, in particular the diameter \(2 x+3 y=0,\) the strip inside \(S\) lying between the lines \(2 x+3 y=k \pi\) and \(2 x+3 y=(k+1) \pi\) is the mirror image of strip lying between the lines \(2 x+3 y=-k \pi\) and \(2 x+3 y=-(k+1) \pi .\) For each integer \(k,\) precisely one of these two equal strips is included in the desired area. Thus the desired area is half that of \(S,\) i.e., \(72 \pi\)
</p>


---

### Quadrilateral with circles
{: .d-inline-block}

B6a, 2014
{: .label}

<p>
Two circles \(G_{1}, G_{2}\) intersect at points \(X, Y\). Choose two other points \(A, B\) on \(G_{1}\) as shown in the figure. The line segment from \(A\) to \(X\) is extended to intersect \(G_{2}\) at point \(L\). The line segment from \(L\) to \(Y\) is extended to meet \(G_{1}\) at point \(C\). Likewise the line segment from \(B\) to \(Y\) is extended to meet \(G_{2}\) at point \(M\) and the segment from \(M\) to \(X\) is extended to meet \(G_{1}\) at point \(D .\) Show that \(A B\) is parallel to \(C D\)
</p>

Sol.

<p>
Draw segment \(B D .\) Now \(\angle B D C=\angle B Y C=\angle L Y M=\angle L X M=\angle A X D=\) \(\angle A B D,\) where the second and the fourth equalities are due to opposite angles and the other three equalities due to angles being in the same arc. Therefore \(A B\) and \(C D\) are parallel.
</p>


---

### On Ceva's theorem
{: .d-inline-block}

B6b, 2014
{: .label}

<p>
A triangle \(C D E\) is given. A point \(A\) is chosen between \(D\) and \(E\) A point \(B\) is chosen between \(C\) and \(E\) so that \(A B\) is parallel to \(C D .\) Let \(F\) denote the point of intersection of segments \(A C\) and \(B D .\) Show that the line joining \(E\) and \(F\) bisects both segments \(A B\) and segment \(C D .\) (Hint: You may use Ceva's theorem. Alternatively, you may additionally assume that the trapezium \(A B C D\) is a cyclic quadrilateral and proceed.)
</p>

Sol.

<p>
Let line \(E F\) meet segment \(C D\) in point \(H\) and segment \(A B\) in point \(I .\) By Ceva's theorem in \(\triangle C D E,\) we have \(\frac{D A}{A E} \frac{E B}{B C} \frac{C H}{H D}=1 .\) As \(A B\) and \(C D\) are parallel, \(\frac{D A}{A E}=\frac{B C}{E B}\) so \(C H=D H .\) Also by the basic proportionality theorem, \(\frac{A I}{D H}=\frac{A E}{D E}=\frac{B E}{C E}=\frac{B I}{C H}\) and since \(C H=D H, A I=B I .\) (If you assume additionally that \(A B C D\) is cyclic, it is easy to see using equality of angles in the same arc and of alternate angles made by a transversal that the triangles \(D E C\) and \(D F C\) are isosceles and in fact line \(E F\) is the perpendicular bisector of segments \(C D\) and \(A B .)\)
</p>


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

Sol.

<p>
Extend \(A D\) and \(B C\) to meet in \(E\) and take \(F=\) the point of intersection of \(A C\) and \(B D .\) By parts (i) and (ii), the line \(E F\) is the bisector of two parallel chords and hence contains a diameter of the circle \(G_{1}\). Repeat the procedure with some other points \(A^{\prime}\) and \(B^{\prime}\) on \(G_{1}\) to get another diameter of \(G_{1}\). The intersection of the two diameters is the center of \(G_{1}\). Repeat the procedure for \(G_{2}\).

Note: If lines \(A D\) and \(B C\) do not meet, they are parallel. Then \(A B C D\) must be a rectangle (why?) and its diagonals are diameters, which intersect in the centre of \(G_{1}\). Note that here we have to assume that we can decide if two lines are parallel, which is implicit in the given assumption that if two lines intersect, then we can actually find the point of intersection by extending the given finite segments.
</p>




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


Sol.

<p>
Center \(=(10,0),\) radius \(=6\). Use the distance formula and the Pythagorean theorem to get \(y^{2}+(x+8)^{2}-6^{2}=9\left(y^{2}+(x-8)^{2}-4\right)\). Simplifying gives \(y^{2}+(x-10)^{2}=6^{2}\) Another way, assuming the locus to be a circle: note that the ratio of the radii of \(C_{1}, C_{2}\) and that of the tangents is the same (namely 3 ). Now use similar triangles to see that
2 the desired circle intersects the X-axis at coordinates 4 and 16, giving a diameter of the desired circle (why?)
</p>



### Straight-edge with circle
{: .d-inline-block}

B6, 2015
{: .label}

<p>
You are given the following: a circle, one of its diameters \(A B\) and a point \(X\).

(a) Using only a straight-edge, show in the given figure how to draw a line perpendicular to \(A B\) passing through \(X .\) No credit will be given without full justification. (Recall that a straight-edge is a ruler without any markings. Given two points, a straight-edge can be used to draw the line passing through the given points.)

(b) Reconsider your procedure to see if it can be made to work if the point \(X\) is in some other position, e.g.,
when it is inside the circle or to the "left/right" of the circle.
Clearly specify all positions of the point \(X\) for which your procedure in part (a), or a small extension/variation of it, can be used to obtain the perpendicular to \(A B\) through \(X\).
Justify your answer.
</p>


Sol.

<p>
Line AX cuts the circle in C. Line BX cuts the circle in D. Lines AD and BC intersect in E. Line XE is perpendicular to line AB. Reason: Angles ADB and ACB are right angles, being angles in a semicircle. The altitudes of triangle \(\mathrm{XAB}\) are concurrent. Two of them are \(\mathrm{AD}\) and \(\mathrm{BC},\) so the third is contained in line XE. (Notice that we always use lines rather than line segments - this is important for part (b).)

You are given the following: a circle, one of its diameters \(A B\) and a point \(X\).

\mathrm{Case } 1 : ~ \text { Suppose } \mathrm { X } \text { is not on the line } \mathrm { AB } \text { (so XAB is a triangle), nor on the } tangents to the circle at \(A\) (so line XA meets the circle in a point \(C\) different from \(A\) ), nor on the tangent at \(\mathrm{B}\) (so line \(\mathrm{XB}\) meets the circle in a point \(\mathrm{D}\) different from \(\mathrm{B}\) ) nor on the given circle (so \(\mathrm{C}, \mathrm{D}\) and \(\mathrm{X}\) are all different). In this case the exact same procedure will work so long as we understand that the altitudes and their intersection point may lie outside triangle XAB. This is because the lines XA and XB meet the circle in two distinct points \(\mathrm{C}\) and \(\mathrm{D}\) that are different from \(\mathrm{X}, \mathrm{A}\) and \(\mathrm{B}\).
\mathrm{Case } ~ 2 :  Suppose X is on one  of the  two tangents, say the tangent at A,but X is different from A.
In this case XA itself is the desired line! In terms of the construction, here we have \(\mathrm{A}=\mathrm{C}=\mathrm{E}\). Of course we have to assume that we can detect whether a line meeting a circle does so in one point or two. But this assumption is implicit in Case 1 also, because there we need to be able to identify the second point of intersection!  \mathrm{Case } ~ 3: If \(\mathrm{X}\) is on line \(\mathrm{AB}\), then \(\mathrm{XAB}\) is not a triangle. If \(\mathrm{X}\) is not on line \(\mathrm{AB}\) but \(\mathrm{X}\) is on the circle, then \(\mathrm{XAB}\) is a triangle but \(\mathrm{X}=\mathrm{C}=\mathrm{D}=\mathrm{E},\) so we cannot draw line XE. Thus in these cases, the above procedure fails. Nonetheless even in these cases it is possible to draw a perpendicular through \(\mathrm{X}\) to line \(\mathrm{AB}\) using only a straightedge.
It is a challenge to you to find a suitable procedure!

</p>

---

### Triangle with segments
{: .d-inline-block}

A10, 2016
{: .label}




<p>

You are given a triangle ABC, a point D on segment AC, a point E on segment. AB and a point F on segment BC.
Let BD and CE intersect in point P. Join P with F. Suppose that the following is true:<br>
\(\angle\)EPB=\(\angle\)BPF=\(\angle\)FPC=\(\angle\)CPD  and PD=PE=PF.


An indicative triangle is shown below.

<p style="text-align:center;"><img src="/assets/images/2016_q10.png"></p>

(i) AP must bisect \(\angle\) BAC.
(ii) \(\triangle\) ABC must be isosceles.
(iii) A, P, F must be collinear.
(iv) \(\angle\) BAC must be \(60^{\circ}\)


</p>


Sol.

<p>
TFFT
BP and CP are angle bisectors meeting at P,
so AP bisects \(\angle\)A since the angle bisectors are concurrent.
The angles marked with symbol o at point P are all \(60^{\circ}\) because \(\angle\)EPD is twice this common value.
It follows that half the sum of \(\angle\)B and \(\angle\)C is \(60^{\circ}\). So \(\angle\)A is \(60^{\circ} \).

The others are false, in fact check that any triangle with \(\angle A=60^{\circ},\) angle bisectors BD and CE,
their point of intersection P and PF bisecting \(\angle\)BPC will satisfy the given data.
All four statements are true if and only if the triangle ABC is equilateral.

</p>


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


Sol.

<p>
A bubble at the point \(P=\left(a, a^{2}\right)\) must be tangential to the parabola at \(\left(a, a^{2}\right) .\) (Why?) It must also be symmetric with respect to Y-axis (why?) and so its center \(O\) must be on the Y-axis. The radius \(O P\) of this bubble is perpendicular to the common tangent to the parabola and to the bubble at \(P .\) The slope of this tangent = \(2 a,\) so the slope of radius \(O P=\frac{-1}{2 a}(\) for \(a \neq 0) .\) Let \(Q=\left(0, a^{2}\right) .\) Using triangle \(O P Q\) slope of \(O P=\frac{-O Q}{a}=\frac{-1}{2 a}\). Therefore \(O Q=\frac{1}{2},\) regardless of the value of \(a\)
<br>

(a) By Pythagoras, \(O P^{2}=\left(\frac{1}{2}\right)^{2}+a^{2}=1 .\) So \(a^{2}=\frac{3}{4}\) and \(P=\left(0, \frac{3}{4}+\frac{1}{2}\right)=\left(0, \frac{5}{4}\right)\)
3

<br>

(b) For any nonzero \(a,\) the radius of the bubble satisfies \(O P^{2}=\left(\frac{1}{2}\right)^{2}+a^{2},\) so \(O P>\frac{1}{2}\) The smallest bubble is at the origin and its radius is \(\frac{1}{2}\). (One cannot just directly take \(a=0\) in the above calculations. Argue by continuity or do a separate calculation at the origin. \()\)

</p>










