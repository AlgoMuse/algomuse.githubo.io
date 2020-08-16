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
first quadrant such that \(\mathrm{E}, \mathrm{F}, \mathrm{G}\) and \(\mathrm{H}\) respectively are the midpoints of the sides \(\mathrm{AB}\), \(\mathrm{BC}, \mathrm{CD}\) and \(\mathrm{DA}\) of a convex quadrilateral ABCD.
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
For \(n=2,\) place the two blue points on opposite sides of the line passing through the given two red points. There are two possible pairings and the two segments in either one do not intersect. We use a similar idea in general.<br>

Given \(n\) red points, find a triangle \(A B C\) such that \(A\) is a red point and all other red points are inside triangle \(ABC\). This is always possible since \(B\) and \(C\) can be placed anywhere, as long as \(ABC\) is a triangle. Place one blue point at \(B\) and all other blue points in the region opposite to triangle \(A B C\) at vertex \(C .\) (More precisely, let \(C\) be between \(A\) and \(A^{\prime}\) and also between \(B\) and \(B^{\prime} .\) Place the remaining blue points inside triangle \(A^{\prime} C B^{\prime} .\) ) Now in any pairing, if \(A\) and \(B\) are connected, then \(A B\) will not intersect any other segment. Otherwise the two segments having \(A\) and \(B\) as vertices will not intersect. Draw a picture to see this.
</p>


---









