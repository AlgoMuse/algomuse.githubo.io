---
layout: default
title: Coordinate system
parent: Geometry
nav_order: 3
---


## Coordinate system
{: .no_toc  }


#### Problems
{: .no_toc  }

1. TOC
{:toc}

---

### Line passing through an A.P.
{: .d-inline-block}

B7, 2010
{: .label}


<p>Let \(p_{1}, p_{2}, \ldots, p_{n}\) and \(q_{1}, q_{2}, \ldots, q_{n}\) be two different arithmetic progressions.
Prove that the sequence of points \(S=\left(p_{1}, q_{1}\right),\left(p_{2}, q_{2}\right), \ldots,\left(p_{n}, q_{n}\right)\) is collinear.
</p>

<details><summary>Solution</summary>
<p>
Let the common difference of the elements in the first AP and the second AP be \(h\) and \(k\), respectively.
</p>

<p>
Any line segment that connects two consecutive points has a slope equal to:

\[ \frac{q_{i+1}-q_i}{p_{i+1}-p_i} = \frac{k}{h} \]
</p>

<p>
The points in \(S\) lie on the line that passes through \(\left(p_1,q_1\right)\) with slope \(k/h\).  Therefore, all the points in \(S\) must be collinear.
</p>


</details>




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

<details><summary>Solution</summary>

<p>
300
</p>


</details>

---

### Circles with Pythagoras
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
Center \(=(10,0),\) radius \(=6\). Using the distance formula and the Pythagorean theorem we get:
\[y^{2}+(x+8)^{2}-6^{2}=9\left(y^{2}+(x-8)^{2}-4\right)\]
Simplifying gives \(y^{2}+(x-10)^{2}=6^{2}\).
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
(b) For any nonzero \(a,\) the radius of the bubble satisfies \(O P^{2}=\left(\frac{1}{2}\right)^{2}+a^{2},\) so \(O P>\frac{1}{2}\) The smallest bubble is at the origin and its radius is \(\frac{1}{2}\).
</p>



</details>

---

### Vector perpendicular to a plane
{: .d-inline-block}

A2, 2020
{: .label }

<p>
Let vectors \(\vec{a},\vec{b}\) and \(\vec{c}\) be defined as follows:

\begin{align}
\vec{a} &= 6i+6j+9k \\
\vec{b} &= 7i+8j+10k \\
\vec{c} &= 2i-3j+4k
\end{align}

Let \(P\) be the plane containing vectors \(\vec{a}\) and \(\vec{b}\). Find a unit vector that lies in the plane \(P\) and
is perpendicular to vector \(\vec{c}\).
</p>



<details><summary>Solution</summary>

<p>
We are looking for a vector \( \vec{u} \) that can be written as \( t\vec{a}+\vec{b} \) for some \(t\). Since \( \vec{u} \) is
perpendicular to \(\vec{c}\) we must have \( \vec{u}\cdot\vec{c} = 0 \).
</p>

\begin{align}
2(6+7t) - 3(6+8t) + 4(9+10t) &= 0 \\
t&=-1
\end{align}

So \( \vec{u}=i+2j+k \).  A unit vector along \( \vec{u} \) is \(\frac{1}{\sqrt{6}} (i+2j+k) \).


</details>




---

### Find a curve given the tangent
{: .d-inline-block}

B2, 2013
{: .label}


<p>
A curve \(C\) has the property that the slope of the tangent at any given point \((x, y)\) on \(C\) is \(\frac{x^{2}+y^{2}}{2 x y}\)
</p>
<p>
a) Find the general equation for such a curve. You may find it useful to substitute \(z=\frac{y}{x}\).
</p>

<p>
b) Specify all possible shapes of the curves in this family. In particular, could an ellipse be one of the shapes?
</p>

<details><summary>Solution</summary>

<p>
The given property of the curve \(C\) can be expressed as a differential equation:<br>
</p>

<p>
\[\frac{d y}{d x}=\frac{x^{2}+y^{2}}{2 x y}=\frac{1}{2}\left(\frac{x}{y}+\frac{y}{x}\right)\]
</p>


<p>
It is convenient to let \(z=y / x,\) so the equation becomes \(\frac{d y}{d x}=\frac{1}{2}\left(\frac{1}{z}+z\right).\)
</p>

<p>
To get this in terms of only \(x\) and \(z,\) differentiate \(z=y / x\) with respect to \(x\) to get:
\[\frac{d z}{d x}=\frac{1}{x} \frac{d y}{d x}-\frac{y}{x^{2}}=\frac{1}{x}\left(\frac{d y}{d x}-z\right)=\frac{1}{x}\left(\frac{1}{2}\left(\frac{1}{z}+z\right)-z\right)=\frac{1}{x} \frac{1-z^{2}}{2 z}\]
</p>

<p>
Separating the variables and integrating, we get:

\begin{align}
\int \frac{d x}{x}&=\int \frac{2 z d z}{1-z^{2}}\\
\log |x|&=-\log \left|1-z^{2}\right|+ \text{some constant}\\
\log \left|1-z^{2}\right|&=-\log |x|+K=\log |x|^{-1}+K \\
1-z^{2}&=\pm \frac{e^{K}}{x}=\frac{c}{x}
\end{align}

<br>
where \(c\) is a nonzero constant. Substituting \(z=y / x,\) we get \(1-\frac{y^{2}}{x^{2}}=\frac{c}{x},\) i.e., \(x^{2}-y^{2}=c x\).
</p>

<p>
To get the shape of the curve, complete the square to get \(\left(x-\frac{c}{2}\right)^{2}-y^{2}=\frac{c^{2}}{4},\) which is a hyperbola when \(c \neq 0\). It could also represent two straight lines \(y=\pm x\), when \(c=0\).
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

#### Reference

_This problem appears in Chap.~2, Problem~7, 103 Problems in trigonometry Titu Andrescu._



---


### Intersecting planes
{: .d-inline-block}

B2, 2017
{: .label}


<p>
Let \(L\) be the line of intersection of the planes \(x+y=0\) and \(y+z=0\).

<ul>
<li>(a) Write the vector equation of \(L\), i.e., find \((a, b, c)\) and \((p, q, r)\) such that
\(L=\{(a, b, c)+\lambda(p, q, r) \mid \lambda\) is a real number. \(\}\) </li>
<li>(b) Find the equation of a plane obtained by rotating \(x+y=0\) about \(L\) by \(45^{\circ}\) </li>
</ul>


</p>

<details><summary>Solution</summary>

<p>
Clearly the line \(L\) passes through the origin. Moreover \(L\) is in the direction perpendicular to the normals to the both the planes.
The direction vector can be obtained by computing the following cross product:
\[
(i+j) \times(j+\hat{k})=i-j+\hat{k}
\]
Hence \(L\) can be written as
\(L=\{(0,0,0)+\lambda(1,-1,1) \mid \lambda\) is a real number \(\}\).
First, note that the equation of any plane that contains the line \(L\) is given by
\[
x+(1+\lambda) y+\lambda z=0
\]
Second, note that one can rotate the plane \(x+y=0\) in either clockwise or in anticlockwise direction.
Consequently there are two such planes. The normal of one of the planes makes an angle of \(45^{\circ}\) with the normal of \(x+y=0\) and the other normal makes an angle of \(135^{\circ}\).
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




