---
layout: default
title: Circles
parent: Geometry
nav_order: 2
---

## Circles [11]
{: .no_toc  }

#### Problems
{: .no_toc  }

1. TOC
{:toc}

---


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

<p style="text-align:center;"><img src="/assets/images/2018_a1.png"></p>


<details><summary>Solution</summary>

<p>
Let us calculate the radius of the largest inscribed circle.

<p style="text-align:center;"><img src="/assets/images/cmi2018_a1_sol.svg"></p>

\begin{align}
BD &= \frac{AD}{\tan 60^{\circ}} = \frac{3}{\sqrt{3}} = \sqrt{3} \\
OD &= BD\times \tan 30^{\circ} = 1 \text{cm}
\end{align}

</p>

<p>
Hence, the size of the largest circle is 1 cm. The next triangle's base passes through point P. We know that AP=1 cm, which is 1/3rd the size of the altitude of the original triangle. Hence, the next circle that is inscribed is 1/3rd the size of the largest circle. The radii follow a geometric progression.
</p>

<p>

Let \(A\) denote the total area of these circles then:

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

Consider the figure shown below. The bisector of \(\angle A O B\) splits this angle into two angles of \(60^{\circ}\) each and meets the circle,
at point \(C^{\prime} \).

<p style="text-align:center;"><img src="/assets/images/a3_2013.svg"></p>

Now the triangles \(O A C^{\prime}\) and \(O B C^{\prime}\) are both equilateral, so \(A C^{\prime}=O C^{\prime}=B C^{\prime},\) making \(C^{\prime}=C,\) the circumcenter of triangle \(A O B\).
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
 Let \(A_{n}=\) the area of a regular \(n\) -sided polygon inscribed in a circle of radius 1 (i.e., vertices of this regular \(n\) -sided polygon lie on a circle of radius 1 ).
(i) Find \(A_{12}\).
(ii) Find \(\left\lfloor A_{2014}\right\rfloor,\) i.e., the greatest integer \(\leq A_{2014}\)
</p>


<details><summary>Solution</summary>

<p>
The area of an \(n\)-sided regular polygon is given by

\[ A = \frac{nr^2}{2} \sin \left( \frac{2\pi}{n} \right) \]

</p>

<p>
(i) \( A_{12} = 6 \sin(\pi/6 ) = 3\).
</p>

<p>
(ii) 3. \( A_{2014} = 1012 \sin(\pi/1012) \approx \pi \), since for small values of \(x\), \(\sin x \approx x\).
</p>

<p>
Another way to reason is to observe that a polygon with many sides is approximately close to a circle.
Since the area of the circle is \(\pi\), the polygon's area must also be close to \(\pi\).

</p>

</details>

---

### Cyclic trapezoids
{: .d-inline-block}

B1, 2020
{: .label}

<p>
We have four cyclic points \(A\), \(B\), \(C\) and \(D\). \(AC\) and \(BD\) are  the diameters of the circle.
\(AB =12 \)cm and \(BC = 5\)cm. \(P\) is a point on the arc joining \(A\) & \(B\) which does not contain \(C\) and \(D\).
\(AP = a\), \(BP = b\), \(CP = c\) and \(DP = d\).  Find \(\frac {a+b}{c+d}\)  and  \(\frac {a-b}{d-c}\).
</p>


<p style="text-align:center;">
<img src="/assets/images/ptolemy_cmi_admission_2020.svg">
</p>

<details><summary>Solution</summary>

<p>Since \(AC\) and \(DB\) are diameters, \( \angle ABC \) and \( \angle DAB \) must be right angles. Hence, \(ABCD\) is a rectangle with
a diagonal whose length is 13 cm.</p>



<p>
Applying Ptolemy's theorem to trapezoids \(APBC\) and \(APBD\), we get the following two equations, respectively.
</p>

<p>
\begin{align}
12c = 13b + 5a \\
12d = 13a + 5b
\end{align}
</p>

Adding the two equations, we get \( 12(c+d) = 18(a+b) \).

\[ \boxed{  \frac{a+b}{c+d} = \frac{2}{3}  } \]

Since \(DB\) is a diameter, \( \angle DPB = 90^\circ \). Similarly, since \(AC\) is a diameter, \(\angle APC=90^\circ \). Applying Pythagoras
theorem to triangles \(DPB\) and \(APC\) we get:


\begin{align}
b^2 + d^2 = 13^2 \\
a^2 + c^2 = 13^2
\end{align}


\begin{align}
a^2 - b^2 &= d^2 - c^2 \\
(a+b)(a-b) &= (d-c)(d+c) \\\\
\frac{a-b}{d-c} &= \frac{c+d}{a+b}
\end{align}



\[ \boxed{ \frac{a-b}{d-c} = \frac{3}{2} } \]


<br>



<h4>Reference</h4>

<img src="/assets/images/sharygin.png" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
This problem appears in the book titled <i>Problems in plane geometry</i> by I.F.Sharygin (1982). It was part of a delightful series called <i>Science for everyone</i> by MIR publishers. <br><br>
</p>
<p>
See: Page 39, Section 1, Problem 183.
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



### Quadrilateral with circles
{: .d-inline-block}

B6a, 2014
{: .label}

<p>
Two circles \(G_{1}, G_{2}\) intersect at points \(X, Y\). Choose two other points \(A, B\) on \(G_{1}\) as shown in the figure. The line segment from \(A\) to \(X\) is extended to intersect \(G_{2}\) at point \(L\). The line segment from \(L\) to \(Y\) is extended to meet \(G_{1}\) at point \(C\). Likewise the line segment from \(B\) to \(Y\) is extended to meet \(G_{2}\) at point \(M\) and the segment from \(M\) to \(X\) is extended to meet \(G_{1}\) at point \(D .\) Show that \(A B\) is parallel to \(C D\)
</p>


<p style="text-align:center;"><img src="/assets/images/cmi2014_b6_cyclic.svg"></p>


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

<p style="text-align:center;"><img src="/assets/images/cmi2014_b6_triangle.svg"></p>


<details><summary>Solution</summary>

<p>
By Ceva's theorem in \(\triangle C D E,\) we have \(\frac{D A}{A E} \frac{E B}{B C} \frac{C H}{H D}=1 .\) As \(A B\) and \(C D\) are parallel, \(\frac{D A}{A E}=\frac{B C}{E B}\) so \(C H=D H .\) Also by the basic proportionality theorem, \(\frac{A I}{D H}=\frac{A E}{D E}=\frac{B E}{C E}=\frac{B I}{C H}\) and since \(C H=D H, A I=B I\).
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

(a) Using only a straight-edge, show in the figure below how to draw a line perpendicular to \(A B\) passing through \(X\).
Given two points, a straight-edge can be used to draw the line passing through the given points.


<p style="text-align:center;"><img src="/assets/images/b6_2015.svg"></p>

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
(b) Please refer to the figure shown below. We will do a case-by-case analysis:<br>


<p style="text-align:center;"><img src="/assets/images/b6_2015ans.svg"></p>


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

B12, 2011
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


