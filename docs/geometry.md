---
layout: default
title: Geometry
nav_order: 5
---


# Geometry



### Rhombus within a triangle
{: .d-inline-block}

B2, 2010
{: .label}


In an isoceles triangle ABC  with A at the apex, the height and the base are both equal to
1cm. Points D, E and F are chosen from each side such that BDEF is a rhombus.  Find the length of the side of this rhombus.

#### Solution

We want to find the side length of the rhombus \\(BDEF\\).  We will find the length of \\(EF\\). Let \\( AX \\) and \\( EX' \\) be the perpendiculars of triangles \\(ABC\\) and \\(EFC\\), respectively.

<p style="text-align:center;"><img src="/assets/images/cmi2010_bisector.svg"></p>

We know that \\( FX'= EX'/2 \\)  since \\( ABC \cong EFC \\).

\begin{align}
EF &= \frac{\sqrt{5}}{2}EX' \hskip{3pt} \text{since }EX'F\text{ is a right angled triangle}
\label{eq:triangle}\tag{1}
\end{align}


All we have to do is find the length of \\( EX' \\).

\begin{align}
\tan \theta & = \frac{EX'}{BX'} \\\\\\\\
\tan \theta & = \frac{EX'}{BC-X'C} \\\\\\\\
& = \frac{EX'}{1 - EX'/2} \hskip{5pt} \text{ since } ABX \cong EFX' \\\\\\\\
EX' & = \frac{2\tan \theta}{2+\tan \theta} \hskip{5pt} \text{ by rearranging } \label{eq:ex}\tag{2} \\\\\\\\
\\\\\\\\
\\\\\\\\
\tan 2\theta & = \frac{AX}{BX} = \frac{2\tan \theta}{1-\tan^2\theta} \\\\\\\\
2 & = \frac{2\tan \theta}{1-\tan^2\theta} \\\\\\\\
\tan \theta & = \frac{-1+\sqrt{5}}{2} \\\\\\\\
EX' & = (2\sqrt{5}-4) \hskip{5pt} \text{by substituting the value of }\tan \theta\text{ in \eqref{eq:ex}}
\\\\\\\\
\\\\\\\\
EF & = \frac{\sqrt{5}}{2}(2\sqrt{5}-4) \hskip{5pt} \text{From \eqref{eq:triangle}} \\\\\\\\
 & = (5-2\sqrt{5})
\end{align}



Hence the side length of the rhombus is  \\( (5-2\sqrt{5}) \\) cm.

### Rational triangle
{: .d-inline-block}

B4, 2010
{: .label}

If all the sides and area of a triangle were rational numbers then show that the
triangle is got by ‘pasting’ two right-angled triangles having the same property.

#### Solution

Let ABC be a triangle with rational sides and rational area. Let \\( B\\) be the largest angle.

<p style="text-align:center;"><img src="/assets/images/triangle_slice.svg"></p>

Drop a perpendicular from the largest angled corner. We get two right angled triangles with altitude \\(BD\\).

\\[ \Delta ABC = \frac{1}{2}AC\cdot BD \\]

Hence, \\( BD\\) must be rational.

Now we need to show that \\(AD\\) and \\(DC\\) are rational.


\begin{align}
AD^2 + BD^2 &= AB^2\\\\\\\\
DC^2 + BD^2 &= BC^2\\\\\\\\
AD^2 - DC^2 &= AB^2 - BC^2\\\\\\\\
AD - DC &= \frac{AB^2 - BC^2}{AD+DC}\\\\\\\\
AD - DC &= \frac{AB^2 - BC^2}{AC}
\end{align}


Hence, \\(AD-DC\\) is rational. Together with the fact that \\(AD+DC\\) is rational, we infer that \\(AD\\) and \\(DC\\) must be rational too.


**Try this**. Prove that any rational triangle can be split into two rational triangles one of which is similar to the original one.

---

### Geometry with basic trigonometry
{: .d-inline-block}

A2, 2011
{: .label}

In a rectangle ABCD, the length BC is twice the width AB. Pick a point P on side BC
such that the lengths of AP and BC are equal. The measure of angle CPD is

- [ ] \\(75^{\circ}\\)
- [ ] \\(60^{\circ}\\)
- [ ] \\(45^{\circ}\\)
- [ ] none of the above


#### Solution


Let the length of AB be one unit and BC be two units, respectively. We draw a perpendicular from vertex P to X. Since APX is a right angled triangle:

\begin{align}
AX^2 &= AP^2 - PX^2  \\\\\\\\
AX^2 &= 2^2 - 1^2  \\\\\\\\
AX &= \sqrt{3} \\\\\\\\
\end{align}

Hence, the length of CP is \\( 2-\sqrt{3} \\). The angle CPD is \\( \arctan \frac{1}{CP}  = \arctan \frac{1}{2 - \sqrt{3}} \\) .

We can verify that the answer is \\( 75^{\circ} \\).



<p style="text-align:center;"><img src="/assets/images/rectangle_2011.svg"></p>


\begin{align}
\tan(A+B) &= \frac{\tan A + \tan B}{1-\tan A \tan B} \\\\\\\\
\tan(45+30) &= \frac{\tan 45 + \tan 30}{1-\tan 45 \tan 30} \\\\\\\\
&= \frac{1 + 1/\sqrt{3}}{1-1/\sqrt{3}}\\\\\\\\
&= \frac{\sqrt{3}+1}{\sqrt{3}-1} = \frac{2}{(\sqrt{3}-1)^2}\\\\\\\\
&= \frac{1}{2-\sqrt{3}}\\\\\\\\
\end{align}




### Intersecting circle
{: .d-inline-block}

B6, 2010
{: .label}

Let \\(C_1, C_2\\) be two circles of equal radii \\(r\\). If \\(C_1\\) passes through the centre of \\(C_2\\), prove
that the area of the region common to them is \\( \frac{r^2}{6}(4\pi - \sqrt{27})\\).


#### Solution

The radius of each circle is \\(r\\). The required common area is same as twice the area of the sector ACD minus the area of the rhombus ACBD.

The rhombus ACBD is made up of two equilateral triangles so its area is \\( 2\times \frac{\sqrt{3}}{4}\times r^2 \\).

<p style="text-align:center;"><img src="/assets/images/intersect_circle.svg"></p>


\begin{align}
\text{Common area} &= 2\times \text{Area of sector ACD} - 2\times\Delta ABC \\\\\\\\
&= 2\times\frac{\pi}{3}r^2 - 2\times \frac{\sqrt{3}}{4}r^2 \\\\\\\\
&=\frac{r^2}{6}(4\pi - \sqrt{27})
\end{align}









