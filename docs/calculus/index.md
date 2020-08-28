---
layout: default
title: Calculus
nav_order: 51
has_children: true
---


# Calculus



### Vanilla application of L'Hospital
{: .d-inline-block }

A3, 2010
{: label .label-blue}

Evaluation the limit:

\\[ \lim_{x \rightarrow 1}\left(\frac{n- \displaystyle \sum_{k=1}^n x^{k}}{1-x}\right) \\]


<details><summary>Solution</summary>

We apply the L'Hospital's rule and differentiate both the numerator and the denominator.

\begin{array}{rl}
 \lim_{x\rightarrow 1}&\displaystyle \frac{-n x^{n-1}-(n-1) x^{n-2}-\cdots-x-1}{-1}  \\
 \lim_{x\rightarrow 1}&\displaystyle \frac{n(n-1)}{2}
\end{array}


</details>

---


### L'Hospital again
{: .d-inline-block}

A4, 2012
{: .label}


<p>
Prove the following limit.
</p>

<p>
\[ \lim_{x \rightarrow \infty} \frac{x^{100} \ln (x)}{e^{x} \arctan \left(\frac{\pi}{3}+\sin x\right)}=0 \]
</p>

<details><summary>Solution</summary>

<p>
For some positive constant \(k\) we can ensure that \(\arctan \left(\frac{\pi}{3}+\sin x\right)> k\) for any \(x\).

For example, \(k=\arctan(0.0001)\) will work. This is because \(\pi>3.142, \sin (x) \geq-1\) and \(\arctan\) is an increasing function.
</p>

<p>
Further, \(\ln (x)< x\) for \(x> 0\). So the given ratio must lie between 0 and \(x^{101} / c e^{x} \). If we apply the L'Hospital's rule 102 times, we get the result.
</p>


</details>


---

### Limit of \\(x^{x^{x}}\\)
{: .d-inline-block }

B1a, 2017
{: .label }

<p>
(a) Evaluate \( \lim_{x \rightarrow 0^{+}}\left(x^{x^{x}}-x^{x}\right) \)
</p>


<details><summary>Solution</summary>

<p>
First consider the limit
\[
\begin{align}
\lim_{x \rightarrow 0^{+}} x^{x}  \\
&=\lim_{x \rightarrow 0^{+}}\left(e^{x\log x}\right) \\
&=\lim_{x \rightarrow 0^{+}}\left(e^{\frac{\log x}{1 / x}}\right)
\end{align}
\]
</p>


<p>Now consider just the exponent:
\[
\begin{align}
\lim_{x \rightarrow 0^{+}} \frac{\log x}{1 / x} \\
&=\lim_{x \rightarrow 0} \frac{1 / x}{-1 / x^{2}} \\
&=0
\end{align}
\]
substituting the value 0 from (2) in equation (1) we get that the limit is 1.
</p>


<p>
Now
\[
\begin{align}
\lim_{x \rightarrow 0^{+}}\left(x^{x^{x}}-x^{x}\right) \\
&=\lim_{x \rightarrow 0^{+}} x^{x^{x}}-\lim_{x \rightarrow 0^{+}} x^{x} \\
&=\lim_{x \rightarrow 0^{+}} x^{\lim_{x \rightarrow 0^{+}} x^{x}}-\lim_{x \rightarrow 0^{+}} x^{x} \\
&=0-1 \\
&=-1
\end{align}
\]
</p>

</details>


---

### Strange question
{: .d-inline-block}


B3, 2017
{: .label }

<p>
Suppose \(p(x)\) be a polynomial of degree strictly less than hundred and such that  \(x^{3}-x\) is not one of its factors. If
\[ \frac{d^{100}}{d x^{100}}\left(\frac{p(x)}{x^{3}-x}\right)=\frac{f(x)}{g(x)} \]
for some polynomials \(f(x)\) and \(g(x)\) then find the smallest possible degree of \(f(x)\).
</p>

<details><summary>Solution</summary>
<p>
Put \(p(x)=x^2-1\), then

\begin{align}
\frac{d^{100}}{d x^{100}}\left(\frac{p(x)}{x^{3}-x}\right)=\frac{d^{100}}{d x^{100}}\left(\frac{1}{x}\right) = \frac{-100!}{x^{100}}
\end{align}

Hence, \(f(x)\) can have degree 0.
</p>

<p>
<i><b>Comment.</b> The official solution has something elaborate which I could not make sense of</i>.
</p>

</details>




---

### Inflection point
{: .d-inline-block}

A6, 2017
{: .label}


<p>Let \(g\) be a function such that all its derivatives exist. <br>

We say \(g\) has an inflection point at \(x_{0}\) if the second derivative \(g^{\prime \prime}\) changes sign at \(x_{0}\) i.e., if \(g^{\prime \prime}\left(x_{0}-\epsilon\right) \times g^{\prime \prime}\left(x_{0}+\epsilon\right)<0\) for all small enough positive \(\epsilon\).</p>

<p>(a) Find all values \(x_{0}\) at which \(g(x) = x^{4}(x-10)\) has an inflection point.</p>

<p>(b) If \(g^{\prime \prime}\left(x_{0}\right)=0\) then \(g\) has an inflection point at \(x_{0}\). Is this true? </p>

<p>(c) If \(g\) has an inflection point at \(x_{0}\) then \(g^{\prime \prime}\left(x_{0}\right)=0.\). Is this true? </p>


<details><summary>Solution</summary>

<p>(a) \(g^{\prime \prime}(x)=20 x^{3}-120 x^{2}=20 x^{2}(x-6)\) and this changes sign only at \(x=6 .\) </p>

<p>(b) is false. Consider the function above: \(g^{\prime \prime}(0)=0\) but \(g^{\prime \prime}\) does not change sign at \(x=0\). </p>

<p>(c) is true due to continuity. The function \(g\) is continous since it is differentiable.</p>

</details>

---

### Absolute integrals
{: .d-inline-block}

A7, 2017
{: .label}

<p>Evaluate: </p>

<p>(a) \(\int_{-3}^{3}\left|3 x^{2}-3\right| d x\)</p>

<p>(b) \(f^{\prime}(1)\) where \(f(t)=\int_{0}^{t}\left|3 x^{2}-3\right| d x\)</p>

<details><summary>Solution</summary>

 <p>(a) Due to symmetry, we can double the integral from 0 to 3. So the value is \(2I\), where:</p>

<p>
\begin{align}
I &=\int_{0}^{1} (3-3x^{2}) \text{d}x  +  \int_{1}^{3} (3 x^{2}-3) \text{d}x  \\
  &=\left. 3x-x^3 \right\rvert_{0}^1  +  \left. (x^{3}-3x)\right\rvert_{1}^3  \\
  &=2 + 20 \\
  &=22\\
\end{align}


Hence, \(\int_{-3}^{3}\left|3 x^{2}-3\right| d x = 44 \).

</p>

<p></p>

<p>(b) \(\left|3 x^{2}-3\right|\) is a continuous function so by the fundamental theorem of calculus, \(f^{\prime}(1)=\) \(\left|3 \times 1^{2}-3\right|=0\)</p>


</details>


---


### Convergence of \\(e^{\text{quadratic}}\\)
{: .d-inline-block}


A2, 2014
{: .label}


<p>
Consider the intergal \(I=\int_{1}^{\infty} e^{a x^{2}+b x+c} d x,\) where \(a, b, c\) are constants. Some combinations of values for these constants are given below and you have to decide in each case whether the integral \(I\) converges.
</p>

<p>(A) \(I\) converges for \(a=-1 \quad b=10 \quad c=100\)</p>
<p>(B) \(I\) converges for \(a=1 \quad b=-10 \quad c=-100\)</p>
<p>(C) \(I\) converges for \(a=0 \quad b=-1 \quad c=100\)</p>
<p>(D) \(I\) converges for \(a=0 \quad b=0 \quad c=-100\)</p>

<details><summary>Solution</summary>
TFTF
</details>

---


### Differentiability I
{: .d-inline-block}

A3, 2014
{: .label}

<p>Given a real number \(x,\) define \(g(x)=x^{2} e^{x}\) if \(x \geq 0\) and \(g(x)=x e^{-x}\) if \(x<0\)</p>
<p>(A) The function \(g\) is continuous everywhere.</p>
<p>(B) The function \(g\) is differentiable everywhere.</p>
<p>(C) The function \(g\) is one-to-one.</p>
<p>(D) The range of \(g\) is the set of all real numbers.</p>

<details><summary>Solution</summary>
TFTT
</details>

---

### Longest diagonal in a box
{: .d-inline-block}

A12, 2014
{: .label}

<p>The total length of all 12 sides of a rectangular box is \(60 .\) (i) Write the possible values of the volume of the box. Your answer should be an interval. Now suppose in addition that the surface area of the box is given to be \(56 .\) Find, if you can, (ii) the length of the longest diagonal of the box (iii) the volume of the box.</p>

<details><summary>Solution</summary>
\((0,125], 13,\) not possible to decide
</details>


---


### Differentiable piece function
{: .d-inline-block}

A5, 2011
{: .label}


<p>
A function \(f\) is defined by \(f(x)=e^{x}\) if \(x<1\) and \(f(x)=\log_{e}(x)+a x^{2}+b x\) if \(x \geq 1\). Here \(a\) and \(b\) are unknown real numbers. Can \(f\) be differentiable at \(x=1 ?\)
</p>

- [ ] \\(f\;\\) is not differentiable at \\(\;x=1\;\\) for any \\(\;a\;\\) and \\(\;b\\).
- [ ] There exist unique numbers \\(\; a \;\\) and \\(\; b \;\\) for which \\(\;f\;\\) is differentiable at \\(\;x=1\\).
- [ ] \\(f\;\\) is differentiable at \\(\; x=1\;\\) whenever \\(\; a+b=e\\).
- [ ] \\(f\;\\) is differentiable at \\(\; x=1\;\\) regardless of the values of \\(\; a\\) and \\(\; b\\).

<details><summary>Solution</summary>

<p>
Option (B). There are unique values of \(a\) and \(b\) for which \(f\) is differentiable at \(x=1\).
</p>


<p>
For the function to be continuous at \(x=1\), we must have \( a+b = e \). For the function to be differentiable:
</p>

<p>
\[ e^x = \frac{1}{x} + 2ax + b \;\;\;\text{ at }\; x=1 \]
</p>

<p>
This means at \( x= 1\), we must have \( a=-1\) and \( b=e+1 \) for the function to be differentiable.
</p>



</details>

---

### Only one real root
{: .d-inline-block }

A8, 2011
{: label .label-blue}


<p>
Suppose \(f(x) = x^3 + x^2 + cx + d\), where \(c\) and \(d\) are real numbers. Prove that if \(c>1/3\),
then \(f\) has exactly one real root.
</p>


*Requires algebra too*.

<details><summary>Solution</summary>

<p>
Since the function has odd degree as the highest power, it has at least one
real root. To show that the function has exactly one real root
we have to show, that it is monotonic in the whole \(\mathbb{R}\).
This can be done by showing that \(f'(x)\) is always positive when \(c>1/3\).
</p>

<p>
\[ f'(x) = 3x^2+2x+c \]
</p>

<p>
The discriminant of the above quadratic, \(2^2-4\cdot3\cdot c\), is negative when \(c>1/3\).
Hence, \(f'(x)\) is always positive in \(\mathbb{R}\).
</p>

</details>

---
### Rolle's theorem I
{: .d-inline-block }

A2, 2012
{: .label}


<p>
A differentiable function \(f: \mathbb{R} \rightarrow \mathbb{R}\) has the following values: \(f(1)=2, f(2)=4\) and \(f(3)=1 \).
Show that \(f^{\prime}(x)=0\) for some \(x\).
</p>

<details><summary>Solution</summary>

<p>
Since \(f\) is differentiable, it must be continuous. By continuity, there is \(a \in(2,3)\) with \(f(a)=2=f(1)\).
Rolle's theorem says that there is \(x \in(1, a)\) with \(f^{\prime}(x)=0\).
</p>

</details>

---

### Rolle's theorem II
{: .d-inline-block }

A9, 2011
{: label .label-blue}

<p>
A real-valued function \(f(x)\) defined on a closed interval \([a,b]\) has the property
that \(f(a)=f(b)=0\) and \(f(x)=f'(x)+f^{\prime\prime}(x)\) for all \(x\) in \([a,b]\). Show that \(f(x)=0\) for
all \(x\) in \([a,b]\).
</p>

<details><summary>Solution</summary>

<p>
If \(f(x)\) is not constant, then it must attain a local maxima or minima at some value \(c\in[a,b]\).
</p>

<p>
From the condition specified:
</p>

<p>
\begin{equation}
f(c)=f'(c)+f^{\prime\prime}(c)
\label{eq:rolle}
\tag{1}
\end{equation}
</p>


<p>
If \(f(c)\) is the local maxima, then \(f(c)>0\), \(f'(c)=0\) and
\(f^{\prime\prime}(c)<0\). But Eq.\(\eqref{eq:rolle}\) does not hold in that case. A similar argument holds for local minima. Hence, \(f(x)\) is zero in the interval \([a,b]\).
</p>



</details>

---


### A simple substitution
{: .d-inline-block }

A2, 2019
{: label .label-blue}


<p>
Let \(f\) be a real valued continuous function defined on \(\mathbb{R}\) satisfying
\(f^{\prime}\left(\tan ^{2} \theta\right)=\cos 2 \theta+\tan \theta \sin 2 \theta,\) for all real numbers \(\theta\)
If \(f(0)=-\cos \frac{\pi}{12}\) then find \(f(1)\)
</p>

<details><summary>Solution</summary>

<p>
Substitute \(t=\tan^{2} \theta \). Then we have
</p>

<p>
\begin{align}
f'(\tan^2\theta) & = \cos 2\theta(1+\tan \theta \tan 2\theta ) \\
f'(\tan^2\theta) & = \frac{1-\tan^2\theta}{1+\tan^2\theta} \left( 1 + \frac{2\tan^2\theta}{1-\tan^2\theta} \right) \\
f'(t) & = \frac{1-t}{1+t} \left( 1 + \frac{2t}{1-t} \right) \quad\text{ where } t=\tan^2 \theta \\
f'(t) & = 1 \\
f(t) & = t + constant
\end{align}
</p>


<p>
Hence the answer is \(1-\cos \frac{\pi}{12}\).
</p>

</details>

---

### Application of Rolle's theorem
{: .d-inline-block }


A7, 2014
{: .label}

<p>
Let \(f(x)=(x-a)(x-b)^{3}(x-c)^{5}(x-d)^{7},\) where \(a, b, c, d\) are real numbers with \( a < b < c < d \).
Thus \(f(x)\) has 16 real roots counting multiplicities and among them 4 are distinct from each other.
Consider \(f^{\prime}(x),\) i.e. the derivative of \(f(x)\). Find the following quantities:<br>

(i) the number of real roots of \(f^{\prime}(x),\) counting multiplicities.  <br>

(ii) the number of distinct real roots of \(f^{\prime}(x)\).<br>
</p>

<details><summary>Solution</summary>

<p>
15,6
</p>


</details>

---

### Smallest prime factor function
{: .d-inline-block }

A9, 2017
{: .label}

<p>
Let \(f\) be a continuous function from \(\mathbb{R}\) to \(\mathbb{R}\) (where \(\mathbb{R}\) is the set of all real numbers) that satisfies the following property: <br>
</p>

<p>
For every natural number \(n\)
</p>

<p>
\[ f(n)= \text{the smallest prime factor of }n \]
</p>


<p>
For example, \(f(12)=2, f(105)=3 .\) Calculate the following.
</p>

<p>
(a) \(\lim_{x \rightarrow \infty} f(x)\)
</p>

<p>
(b) The number of solutions to the equation \(f(x)=2016\)
</p>

<details><summary>Solution</summary>

<p>
(a) \(f(x)\) will take value 2 for all even \(x\). At the same time, primes provide an increasing infinite sequence of positive integers for which \(f(x)=x .\) Thus \(\lim_{x \rightarrow \infty} f(x)\) does not exist.
</p>

<p>
(b) By intermediate value theorem, for each prime \(p> 2016\) there is an \(x\) between \(p\) and \(p+1\) such that \(f(x)=2016\)
</p>

</details>

---

### Monotonic again
{: .d-inline-block}

B1c, 2017
{: label .label-blue}


<p>
Find the number of solutions to \(e^{x}=\frac{x}{2017}+1\)
</p>

<details><summary>Solution</summary>

<p>
This problem is similar to the last one. We need to show that the function is monotonic in some interval.
</p>

<p>
Consider the function:
\begin{align}
f(x)&=  e^x -\frac{x}{2017} - 1 \\
f'(x)&=  e^x -\frac{1}{2017}
\end{align}
</p>


<p>
The derivative is positive when \(x> x_0=-\log 2017\).
</p>

<p>
<ul>
<li>We have \(f(x_0)< 0\) and \( f(-\infty)>0 \) so there is one solution in the interval \((-\infty,x_0)\).</li>
<li>\( x = 0 \) is another solution.</li>
</ul>
</p>

<p>
Hence, there are two solutions to the equation.
</p>


</details>

---

### A perplexing integral
{: .d-inline-block}

B5, 2017
{: label .label-blue}



<p>
Prove that \(\int_{1}^{b} a^{\log_{b} x} d x>\ln b\) where \(a, b>0, b \neq 1\).
</p>


<details open><summary>No solution</summary>
<p>
There is a mistake in this problem. The above statement is not true. See <a href="https://math.stackexchange.com/questions/2182860/proving-the-inequality-int-1b-a-log-bxdx-ln-b">this discussion</a> on Math Stack Exchange for details.
</p>
</details>



---

### Riemann sum
{: .d-inline-block}

B4, 2012
{: .label}

<p>
Define
\[
x=\sum_{i=1}^{10} \frac{1}{10 \sqrt{3}} \frac{1}{1+\left(\frac{i}{10 \sqrt{3}}\right)^{2}}
\]


\[
y=\sum_{i=0}^{9} \frac{1}{10 \sqrt{3}} \frac{1}{1+\left(\frac{i}{10 \sqrt{3}}\right)^{2}}
\]

</p>

<p>
Prove the two inequalities:
</p>

<p>
(a) \(x<\frac{\pi}{6}<y\)
</p>

<p>
</p>

<p>
(b) \(\frac{x+y}{2}<\frac{\pi}{6}\)
</p>

<p>
Hint: Connect the sums to an integral.
</p>


<details open><summary>Solution (a)</summary>
<p>
a) Let \(f(t)=1 /\left(1+t^{2}\right) .\) Then \(y\) and \(x\) are respectively the left and right hand Riemann sums for \(f\) over the interval \(\left[0, \frac{1}{\sqrt{3}}\right]\) using 10 equal parts, each of width \(1 / 10 \sqrt{3} .\) since \(f\) is a positive decreasing function, \(y\) must be greater than the area under \(f\) over the given interval and
\(x\) must be lesser than the area. The area under \(f\) over \(\left[0, \frac{1}{\sqrt{3}}\right]\) is:
</p>

<p>
\[\int_{0}^{1 / \sqrt{3}} f(t) d t=\lvert \tan^{-1}(t)\rvert_{0}^{1 / \sqrt{3}}=\frac{\pi}{6}\]
</p>

<p>
This implies that \(x< \frac{\pi}{6}< y\).
</p>

</details>

<p>
</p>


<details open><summary>Solution (b)</summary>

<p>
b) \(\frac{x+y}{2}\) can be interpreted as the sum of areas of 10 trapezoids as follows. Dividing
\(\left[0, \frac{1}{\sqrt{3}}\right]\) into 10 equal parts, let the \(i\)th subinterval be \(\left[x_{i}, x_{i+1}\right]\)
with \(i=0,1, \ldots, 10 .\) Then the \(i\) -th trapezoid has base \(\left[x_{i}, x_{i+1}\right]\) and it has two vertical sides,
the left one of height \(f\left(x_{i}\right)\) and the right one of height \(f\left(x_{i+1}\right)\).
</p>

<p style="text-align:center;"><img src="/assets/images/trapezoid_B4_2012.png" width="250px"></p>


<p><i>Claim</i>: The function \(f\) is concave </p>

<p>
<i>Proof:</i>
In the interval \(\left(0, \frac{1}{\sqrt{3}}\right)\), we have \(f^{\prime \prime}(t)=\frac{6 t^{2}-2}{\left(1+t^{2}\right)^{3}}<0\). \(\square\).
</p>


<p>
Since \(f\) is concave, the total area of trapezoids is less than the area under \(f\).
</p>



</details>





---










<!--

<table>
<tr>
<td>
<div class="card">
  <img src="https://thumbs-prod.si-cdn.com/sAw6gPjQpCHoRAaYGna1Nof5xQU=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/7c/a4/7ca4762d-8448-40ef-8680-6739305f266c/agnesi-wr.jpg" alt="Avatar" style="width:300px">
  <div class="container">
    <h4><b>Angei</b></h4>
    <p>Mathematician</p>
  </div>
</div>
</td>
<td>
<div class="card">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Gottfried_Wilhelm_Leibniz.jpg" alt="Avatar" style="width:300px">
  <div class="container">
    <h4><b>Leibniz</b></h4>
    <p>Interior Designer</p>
  </div>
</div>
</td>
</tr>
</table>


-->




### Vanilla integrals
{: .d-inline-block}

A6, 2013
{: .label}


<p>
Compute the integrals below, whenever possible. If it does not exist, say so.
</p>

<p>
The notation \([x]\) denotes the integer part of \(x\).
</p>

<p>
<ul>
<li>(a) \(\int_{1}^{4} x^{2} d x\). </li>
<li>(b) \(\int_{1}^{3}[x]^{2} d x\). </li>
<li>(c) \(\int_{1}^{2}\left[x^{2}\right] d x\). </li>
<li>(d) \(\int_{-1}^{1} \frac{1}{x^{2}} d x\).</li>
</ul>
</p>


<details><summary>Solution</summary>

<p>
a) \(\int_{1}^{4} x^{2} d x=\frac{x^{3}}{3}\rvert_{1} ^{4}=21\) using the fundamental theorem of calculus.
</p>

<p>
b) \(\int_{1}^{3}[x]^{2} d x=1\left(1^{2}\right)+1\left(2^{2}\right)=5=\) area under the piecewise constant function \([x]^{2}\)
</p>

<p>
c) \(\int_{1}^{2}\left[x^{2}\right] d x=1(\sqrt{2}-1)+2(\sqrt{3}-\sqrt{2})+3(2-\sqrt{3})=5-\sqrt{2}-\sqrt{3}\) since the function \([x]^{2}\) is constant on intervals \([1, \sqrt{2}),[\sqrt{2}, \sqrt{3}),[\sqrt{3}, 2)\). It takes the values 1,2 and 3 on these intervals, respectively.
</p>


<p>
d) \(\int_{-1}^{1} \frac{1}{x^{2}} d x=2 \lim_{t \rightarrow 0^{+}} \int_{t}^{1} \frac{1}{x^{2}} d x=2 \lim_{t \rightarrow 0^{+}}\left(-1+\frac{1}{t}\right)=\infty .\) The fundamental theorem
does not apply over the interval [-1,1] because \(\frac{1}{x^{2}}\) goes to \(\infty\) in the interval. So the integral does not exist.
</p>

</details>

---



### Asymptotes of a function
{: .d-inline-block}

A10, 2013
{: .label}


<p>
Let
</p>

<p>
\[ f(x)=\frac{x^{4}}{(x-1)(x-2) \cdots(x-n)} \]
</p>

<p>
where the denominator is a product of \(n\) factors, \(n\) being a positive integer. It is also given that the X-axis is a horizontal asymptote for the graph of \(f\). Answer these four questions.
<br>
(i) How many vertical asymptotes does the graph of \(f\) have?
<br>
(a) \(n\)<br>
(b) less than \(n\)<br>
(c) more than \(n\)<br>
(d) impossible to decide <br>
<br>

(ii) What can you deduce about the value of \(n ?\)
<br>
(a) \(n<4\)<br>
(b) \(n=4\)<br>
(c) \(n>4\)<br>
(d) impossible to decide
<br>
<br>
(iii) As one travels along the graph of \(f\) from left to right, at which of the following points is the sign of \(f(x)\) guaranteed to change from positive to negative?
<br>
(a) \(x=0\) <br>
(b) \(x=1\) <br>
(c) \(x=n-1\) <br>
(d) \(x=n\) <br>
<br>
<br>
(iv) How many inflection points does the graph of \(f\) have in the region \(x<0 ?\)
<br>
(a) none <br>
(b) 1 <br>
(c)  more than \(1 \quad\) <br>
(d) impossible to decide.<br>


(It is better to sketch than calculate).
</p>

<details><summary>Solution</summary>

<p>
(i) \(n\) at \(x=1,2, \ldots, n\).
</p>

<p>
(ii) \(n>4,\) because \(\lim_{x \rightarrow \pm \infty} f(x)=0\) and for this to happen, the degree of the denominator of \(f(x)\) must be greater than that of the numerator.
</p>

<p>
(iii) \(x=n-1,\) because \(f(x)\) is positive for \(x> n\) and \(f(x)\) changes sign precisely when it passes through \(x=1,2 \ldots, n .\) Note that the sign of \(f(x)\) for \(x<0\) and for \(x \in(0,1)\) depends on the parity of \(n\)
</p>

<p>
(iv) More than \(1 .\) Note that \(f(x)=0\) only at \(x=0,\) with multiplicity \(4 .\) Without loss of generality, let \(n\) be even.
Now \(f(x)> 0\) for \(x<1\) except at \(x=0\) and \(f\) has all derivatives for \(x<1\).
Due to the multiple root at \(x=0,\) the graph of \(f\) must be concave up, that is \(f^{\prime \prime}(x)> 0\) ) near \(x=0\).
Further, as \(x \rightarrow-\infty,\) the values of \(f(x)\) stay positive and \(\rightarrow 0\).
</p>

<p>
Therefore, as one traces the graph from from the origin to the left, it must become concave down at least
once and eventually concave up again so as to approach the X-axis from above.
</p>

</details>

---

### Span of the a function
{: .d-inline-block}

B5, 2013
{: .label}


<p>
Consider the function \(f(x)=a x+\frac{1}{x+1},\) where \(a\) is a positive constant. Let \(M=\) the largest value of \(f(x)\) and \(N=\)
the smallest value of \(f(x)\) for \(x \in[0,1] .\) Show that \(M-N>\frac{1}{12}\) for any \(a>0\).
</p>


<details><summary>Solution</summary>


<p>
We have \(f(0)=1, f(1)=a+\frac{1}{2}\) and \(f^{\prime}(x)=a-\frac{1}{(x+1)^{2}}\) Over the interval \([0,1],\) the value of \(f^{\prime}(x)\) increases from \(a-1\) at \(x=0\) to \(a-\frac{1}{4}\) at \(x=1\)o
</p>

<p>
What happens to the sign of \(f^{\prime}(x)\)? We do a case by case analysis.
</p>

<p>
<b>Case 1</b>. Suppose \(a \leq 1 / 4 .\) Because \(1 /(x+1)^{2} \geq 1 / 4\) on the interval \([0,1], f^{\prime}(x) \leq 0,\) so the maximum is at 0 and the minimum is at \(x=1\). So the difference is \(1-(1 / 2+a)=\) \(1 / 2-a \geq 1 / 4 \geq 1 / 12\)
</p>


<p> </p>

<p>
<b>Case 2.</b> Suppose \(a \geq 1\). Then \(f^{\prime}(x) \geq 0\) on the interval [0,1] , so maximum is at 1 and minimum at
0. We get \(a+1 / 2-1=a-1 / 2 \geq 1 / 2 \geq 1 / 12\)
</p>

<p> </p>
<p>
<b>Case 3.</b> Suppose \(1 / 4 \leq a \leq 1 .\) Now \(f^{\prime}(x)=0\) at \(\tilde{x}=\frac{1}{\sqrt{a}}-1 .\) For this range of \(a, \tilde{x} \in[0,1]\) In the interval \([0, \tilde{x}], f^{\prime}(x) \leq 0\) and in the interval \([\tilde{x}, 1], f^{\prime}(x) \geq 0 .\) Now we make two sub-cases depending on the endpoint at which the maximum occurs.
</p>

<p> </p>
<p>
<b>Case 3a.</b> Suppose \(1 / 4 \leq a \leq 1 / 2\). Then \(f(0) \geq f(1)\). So minimum is at \(\tilde{x},\) maximum is at \(x=0 . f(\tilde{x})=\sqrt{a}-a+\sqrt{a}=2 \sqrt{a}-a\). So the difference between maximum and minimum is \(1+a-2 \sqrt{a}=(1-\sqrt{a})^{2}\). This is smallest when \(\sqrt{a}\) is closest to 1 and so \((1-\sqrt{a})^{2} \geq(1-1 / \sqrt{2})^{2}=3 / 2-\sqrt{2} .\) This is bigger than \(1 / 12\) since \(\left(\frac{3}{2}-\frac{1}{12}\right)=17 / 12\) and
\(17^{2}=289 \geq 2 \times 12^{2}\)
</p>

<p> </p>

<p>
<b>Case 3b.</b> Suppose \(1 / 2 \leq a \leq 1\). Now \(f(1) \geq f(0)\). Max is at 1 and minimum is at \(\tilde{x}\). The difference is \(a+1 / 2-\sqrt{a}+a-\sqrt{a}=2 a-2 \sqrt{a}+1 / 2=\left(\sqrt{2 a}-\frac{1}{\sqrt{2}}\right)^{2} .\) By a calculation
similar to the above it is bigger than \(1 / 12\).
</p>


</details>


---


### Differentiability Challenge
{: .d-inline-block}

B4, 2014
{: .label}

<p>(i) Let \(f\) be continuous on [-1,1] and differentiable at \(0 .\) For \(x \neq 0,\) define a function \(g\) by \(g(x)=\frac{f(x)-f(0)}{x} .\) Can \(g(0)\) be defined so that the extended function \(g\) is continuous at \(0 ?\)</p>

<p>(ii) For \(f\) as in part (i), show that the following limit exists.</p>

<p>\[ \lim_{r \rightarrow 0^{+}}\left(\int_{-1}^{-r} \frac{f(x)}{x} d x+\int_{r}^{1} \frac{f(x)}{x} d x\right) \]</p>

<p>(iii) Give an example showing that without the hypothesis of \(f\) being differentiable at \(0,\) the conclusion in (ii) need not hold.</p>

<details><summary>Solution (i)</summary>


<p>(i) Yes. We must define \(g(0)=\lim_{x \rightarrow 0} g(x)=f^{\prime}(0),\) which exists by hypothesis.</p>

</details>

<p></p>

<details><summary>Solution (ii)</summary>
<p>(ii) Consider \(\int_{-1}^{-r} g(x) d x=\int_{-1}^{-r} \frac{f(x)}{x} d x-\int_{-1}^{-r} \frac{f(0)}{x} d x=\int_{-1}^{-r} \frac{f(x)}{x} d x-f(0) \ln r . \quad\) Similarly</p>

<p>\[\int_{r}^{1} g(x) d x=\int_{r}^{1} \frac{f(x)}{x} d x-\int_{r}^{1} \frac{f(0)}{x} d x=\int_{r}^{1} \frac{f(x)}{x} d x+f(0) \ln r\]</p>

<p>Thus the expression inside the given limit is equal to \(\int_{-1}^{-r} g(x) d x+\int_{r}^{1} g(x) d x,\) as \(\pm f(0) \ln r\) cancels out.</p>

<p>Applying the fundamental theorem of calculus to the continuous function \(g,\) we get an antiderivative \(G\) of \(g,\) where \(G\) is defined on [-1,1] by \(G(t)=\int_{-1}^{t} g(x) d x .\) So the given</p>

<p>

\begin{align}
\text { limit }&=\lim_{r \rightarrow 0^{+}}\left(\int_{-1}^{-r} g(x) d x+\int_{r}^{1} g(x) d x\right) \\
&=\lim_{r \rightarrow 0^{+}}(G(-r)-G(-1)+G(1)-G(r)) \\
&=G(0)-0+G(1)-G(0)\\
&=G(1)
\end{align}

<br>
We have used the fundamental theorem to evaluate the integrals and the fact that \(G\) is differentiable.
</p>

</details>

<p></p>

<details><summary>Solution (iii)</summary>
<p>(iii) Define \(f(x)=\frac{1}{-\ln \frac{x}{2}}\) for \(x \in(0,1], f(x)=\frac{1}{\ln \left|\frac{1}{2}\right|}\) for \(x \in[-1,0),\) and \(f(0)=0 .\) Verify that this works: \(f\) is continuous at 0 and so on \([-1,1] .\) It is not differentiable at 0 as the relevant limit is \(+\infty .\) The two integrals in the desired limit are equal (because \(f\) is an odd function, so \(\frac{f(x)}{x}\) is even \()\) and each integral is \(+\infty\) as it amounts to \(\lim_{t \rightarrow 0^{+}} \ln |\ln t| .\) Can you see how one might think of such \(f ?\) E.g., check that choices like \(|x|\) or even \(x^{\frac{1}{3}}\) do not work. Compare the behaviour of these functions at \(x=0\) with that of chosen \(f .\)</p>

</details>

---



### Double derivatives
{: .d-inline-block}

A4, 2015
{: .label}

<p>Let \(A, B\) and \(C\) be unknown constants. Consider the function \(f(x)\) defined by</p>

<p>
\begin{align}
f(x) &=A x^{2}+B x+C \text { when } x \leq 0 \\
&=\ln (5 x+1) \text { when } x>0
\end{align}
</p>

<p>Write the values of the constants \(A, B\) and \(C\) such that \(f^{\prime \prime}(x),\) i.e., the double derivative of \(f,\) exists for all real \(x .\) If this is not possible, write "not possible". If some of the constants cannot be uniquely determined, write "not unique" for each such constant.</p>


<details><summary>Solution</summary>

<p>The only problem is at \(x=0 .\) For continuity, \(\ln (0+1)=C\).</p>

<p>For \(f^{\prime}(0)\) to exist, \(f\) must be continuous and the left and right derivatives of \(f\) at \(x=0\) (which are easily seen to exist) must match, that is \(5=B\).</p>

<p>For \(f^{\prime \prime}(0)\) to exist, \(f^{\prime}(0)\) must exist and left and right derivatives of \(f^{\prime}\) at \(x=0\) must match, i.e. \(2 A=-5^{2} .\) So \(A=-\frac{25}{2}, B=5, C=0\).</p>

</details>

---

###  Polynomial and limits
{: .d-inline-block}

B1, 2015
{: .label}

<p>1. Carefully solve the following series of questions. If you cannot solve an earlier part, you may still assume the result in it to solve a later part.</p>
<p>(a) For any polynomial \(p(t),\) the limit \(\lim_{t \rightarrow \infty} \frac{p(t)}{e^{t}}\) is independent of the polynomial \(p .\) Justify this statement and find the value of the limit.</p>
<p>(b) Consider the function defined by</p>

<p>
\begin{align}
q(x) &=e^{-1 / x} \text { when } x>0 \\
&=0 \text { when } x=0 \\
&=e^{1 / x} \text { when } x<0
\end{align}
</p>

<p>Show that \(q^{\prime}(0)\) exists and find its value. Why is it enough to calculate the relevant limit from only one side?</p>
<p>(c) Now for any positive integer \(n,\) show that \(q^{(n)}(0)\) exists and find its value. Here \(q(x)\) is the function in part (b) and \(q^{(n)}(0)\) denotes its \(n\) -th derivative at \(x=0\). Answer: (a) If \(p(t)\) is constant, then the limit \(=0 .\) Otherwise we get a form \(\frac{\pm \infty}{\infty} .\) Using L'Hospital's rule, we get \(\lim_{t \rightarrow \infty} \frac{p(t)}{e^{t}}=\lim_{t \rightarrow \infty} \frac{p^{\prime}(t)}{e^{t}}=0\) by induction on the degree of \(t\) (or apply
L'Hospital's rule repeatedly).</p>

<details><summary>Solution</summary>

 <p>(a) If \(p(t)\) is constant, then the limit \(=0 .\) Otherwise we get a form \(\frac{\pm \infty}{\infty}\). Using L'Hospital's rule, we get \(\lim_{t \rightarrow \infty} \frac{p(t)}{e^{t}}=\lim_{t \rightarrow \infty} \frac{p^{\prime}(t)}{e^{t}}=0\) by induction on the degree of \(t\) (or apply
L'Hospital's rule repeatedly).</p>


<p>(b) The right side derivative \(=\lim_{h \rightarrow 0^{+}} \frac{q(h)-q(0)}{h}=\lim_{h \rightarrow 0^{+}} \frac{e^{-1 / h}}{h}=\lim_{h \rightarrow 0^{+}} \frac{1 / h}{e^{1 / h}}=\lim_{t \rightarrow+\infty} \frac{t}{e^{t}} \cdot\) (Let \(t=1 / h .\) As \(\left.h \rightarrow 0^{+}, t \rightarrow+\infty .\right)\) This limit is \(0,\) e.g. by part \((\mathrm{a})\) Now \(q\) is an even function, so letting \(k=-h,\) the left side derivative \(=\lim_{h \rightarrow 0^{-}} \frac{q(h)-q(0)}{h}=\) \(\lim_{k \rightarrow 0^{+}} \frac{q(-k)}{-k}=\lim_{k \rightarrow 0^{+}} \frac{q(k)}{-k} .\) Using the earlier calculation this also equals \(-0=0\) Note: It is wrong to argue that \(q^{\prime}(0)=\lim_{x \rightarrow 0} q^{\prime}(x)\) because to do so, we first need to know that \(q^{\prime}\) is continuous at \(0,\) but we have not even shown that \(q^{\prime}(0)\) exists! For the same reason it is wrong to argue below that \(q^{(n)}(0)=\lim_{x \rightarrow 0} q^{(n)}(x)\)</p>

<p>
(c) We will show by induction on \(n\) that \(q^{(n)}(0)=0 .\) The case \(n=1\) is done. (We can even start the induction at \(n=0\) by interpreting \(q^{(0)}(x)=q(x) .\) ) Assuming that we are done up to \(n\) and to prove the statement for \(n+1,\) we need to calculate \(\lim_{h \rightarrow 0} \frac{q^{(n)}(h)-q^{(n)}(0)}{h}=\) \(\lim_{h \rightarrow 0} \frac{q^{(n)}(h)}{h},\) because \(q^{(n)}(0)=0\) by induction. Therefore it is good to examine \(q^{(n)}(h)\) for \(h \neq 0 .\) This is easy to calculate by the usual rules, but the formulas will be different for positive and negative \(h .\) For \(h \neq 0,\) as \(q\) is even, \(q^{\prime}\) is odd, so \(q^{\prime \prime}\) is even, etc. and in general \(q^{(n)}(h)=(-1)^{n} q^{(n)}(-h) .\) Therefore, just as for part (b), it suffices to show that \(\lim_{h \rightarrow 0^{+}} \frac{q^{(n)}(h)}{h}=0 .\) By another induction, we see easily that for \(h>0, q^{(n)}(h)=p(1 / h) e^{-1 / h}\)
for some polynomial \(p .\left[\right.\) Proof: \(q^{\prime}(h)=\left(\frac{1}{h^{2}}\right) e^{-1 / h} .\) Assuming the result for \(n,\) we have \(q^{(n+1)}(h)=\left[p(1 / h) e^{-1 / h}\right]^{\prime}=-\frac{1}{h^{2}}\left(-p(1 / h)+p^{\prime}(1 / h)\right) e^{-1 / h},\) which has the desired form.
</p>

<p>
So we have \(\lim_{h \rightarrow 0^{+}} \frac{q^{(n)}(h)}{h}=\lim_{h \rightarrow 0^{+}} \frac{p(1 / h) e^{-1 / h}}{h}=\lim_{t \rightarrow \infty} t p(t) e^{-t}=\lim_{t \rightarrow \infty} \frac{t p(t)}{e^{t}}=0\) by part (a). Here we have again substituted \(t=1 / h\)
</p>

</details>

---

### Slowing slope changing function
{: .d-inline-block}

B4, 2015
{: .label}

<p>Let \(f: \mathbb{R} \rightarrow \mathbb{R}\) be a twice differentiable function, where \(\mathbb{R}\) denotes the set of real numbers. Suppose that for all real numbers \(x\) and \(y,\) the function \(f\) satisfies</p>

<p>\[ f^{\prime}(x)-f^{\prime}(y) \leq 3|x-y| \]</p>


<p>(a) Show that for all \(x\) and \(y,\) we must have \(\left|f(x)-f(y)-f^{\prime}(y)(x-y)\right| \leq 1.5(x-y)^{2}\)</p>

<p>(b) Find the largest and smallest possible values for \(f^{\prime \prime}(x)\) under the given conditions.</p>


<details><summary>Solution</summary>

<p>(a) Note that the given inequality stays valid if we take absolute value of the LHS, because we may interchange \(x\) and \(y\) without affecting RHS.</p>

<p>
Fix \(x, y\) and let \(t=x-y .\) For now let \(x \geq y,\) i.e. \(t \geq 0 .\) For \(h \in[0, t],\) the value of \(y+h\) varies between \(y\) and \(x .\) We are given that \(\left|f^{\prime}(y+h)-f^{\prime}(y)\right| \leq 3|h|\). Integrate with respect to \(h\) over the interval \([0, t]\) to get:

\[\int_{0}^{t}\left|f^{\prime}(y+h)-f^{\prime}(y)\right| d h \leq \int_{0}^{t} 3|h| d h=1.5 t^{2}\]

<br>

The following inequality follows from Lemma 1 (proved below).

</p>

<p>
\[\left|\int_{0}^{t} f^{\prime}(y+h)-f^{\prime}(y) d h\right| \leq \int_{0}^{t}\left|f^{\prime}(y+h)-f^{\prime}(y)\right| d h .\]
</p>

<p>
Combining with the previous inequality we have:
\[\left|\int_{0}^{t} f^{\prime}(y+h)-f^{\prime}(y) d h\right| \leq 1.5 t^{2}\]
</p>

<p>
Finally we calculate the LHS.
<br>

\[\left|\int_{0}^{t} f^{\prime}(y+h) d h-\int_{0}^{t} f^{\prime}(y) d h\right|=\left|f(y+t)-f(y)-f^{\prime}(y) t\right|\]

<br>
where the first integral is calculated using the fundamental theorem of calculus and the second one is just the integral of the constant \(f^{\prime}(y) .\) Substituting \(x-y\) for \(t\) gives the desired result.
</p>

<p>The case when \(x\leq y\) is analogous.</p>


<p> (b) We have, for \(x \neq y,\left|\frac{f^{\prime}(x)-f^{\prime}(y)}{x-y}\right| \leq 3,\) so \(-3 \leq \frac{f^{\prime}(x)-f^{\prime}(y)}{x-y} \leq 3 .\) Taking limit as \(y \rightarrow x\)
we get \(-3 \leq f^{\prime \prime}(x) \leq 3 .\) It is easy to provide examples where \(f^{\prime \prime}\) attains the extreme values \(\pm 3,\) e.g. \(f(x)=\pm 1.5 x^{2} .\) These satisfy the hypothesis and have constant \(f^{\prime \prime}=\pm 3\)
</p>



<p><b>Lemma 1.</b>

<p> \[ \left|\int_{a}^{b} f(x) d x\right| \leq \int_{a}^{b}|f(x)| d x \] </p>


<p> <i>Proof.</i><br> </p>

<p> \[ -|f(x)| \leq f(x) \leq|f(x)| \] </p>


<p> for all \(x\); hence </p>

<p>
\[
-\int_{a}^{b}|f(x)| d x \leq \int_{a}^{b} f(x) d x \leq \int_{a}^{b}|f(x)| d x
\]
</p>

<p>
The lemma follows since \(-a \leq x \leq a \implies  |x|\leq a  \) if \(a \geq 0\). \(\quad \square\)
</p>


</p>


</details>

---


### Sweep volume
{: .d-inline-block}

A3, 2017
{: .label}

<p>
Find the volume of the solid obtained when the region bounded by \(y=\sqrt{x}, y=-x\) and the line \(x=4\) is revolved around the \(x\) -axis.
</p>

<p style="text-align:center;"><img src="/assets/images/2017_sweep_volume.svg" width="250px"></p>

<details><summary>Solution</summary>

<p>
From \(x=0\) to \(x=1\) we have \(\sqrt{x} \geq|-x|,\) so from \(x=0\) to \(x=1\) the volume swept out by the curve determines the volume. From \(x=1\) to \(x=4\), the volume swept by the line determines the volume. Hence, we need two integrals.
</p>

<p>
From \(x=0\) and \(x=1\) we calculate volume obtained by revolving the area below \(y=\sqrt{x}\).

\[ \int_{0}^{1} \pi (\sqrt{x})^2 \text{d}x = \left.\frac{\pi x^2}{2} \right\rvert_{0}^{1} = \frac{\pi\cdot 1^2}{2} - \frac{\pi\cdot 0^2}{2} = \frac{\pi}{2} \]


Similarly, from \(x=1\) to \(x=4\) we have \(|-x| \geq \sqrt{x},\) so here we just have to take the volume obtained by the revolving the area below \(y=x\).

\[ \int_{1}^{4} \pi x^2 \text{d}x = \left.\frac{\pi x^3}{3} \right\rvert_{1}^{4} = \frac{64\pi}{3} - \frac{\pi}{3} =  21\pi \]

Thus total volume of the resulting solid: \( 21.5 \pi \).

</p>



</details>





---

### Definite integral
{: .d-inline-block}

B3, 2016
{: .label}


<p>Consider the function \(f(x)=x^{\cos (x)+\sin (x)}\) defined for \(x \geq 0\).</p>
<p>(a) Prove that</p>

<p>\[ 0.4 \leq \int_{0}^{1} f(x) d x \leq 0.5 \]</p>

<p>(b) Suppose the graph of \(f(x)\) is being traced on a computer screen with the uniform speed of \(1 \mathrm{cm}\) per second (i.e., this is how fast the length of the curve is increasing). Show that at the moment the point corresponding to \(x=1\) is being drawn, the \(x\) coordinate is increasing at the rate of</p>

<p>\[ \frac{1}{\sqrt{2+\sin (2)}} \mathrm{cm} \text { per second } \]</p>



<details><summary>Solution</summary>

<p>(a) It is easy to see that for \(0 \leq x \leq 1,\) we have \(1 \leq \cos (x)+\sin (x) \leq \sqrt{2},\) and so</p>

<p>\[ x^{1} \geq x^{\cos (x)+\sin (x)} \geq x^{\sqrt{2}} \]</p>

<p>As all three functions are non-negative in \([0,1],\) we can integrate the inequalities over that interval to get</p>

<p>\[ \frac{1}{2} \geq \int_{0}^{1} f(x) d x \geq \frac{1}{\sqrt{2}+1}>\frac{1}{1.5+1}=0.4 \]</p>

<p>(b) Length of the curve from \(x=0\) to any given \(x\) is \(l(x)=\int_{0}^{x} \sqrt{1+f^{\prime}(u)^{2}} d u\) It is given that \(\frac{d l}{d t}=1 \mathrm{cm} /\) second at all times. One needs to find \(\frac{d x}{d t}\) when \(x=1\)</p>

<p>By chain rule \( \displaystyle \frac{d l}{d t}=\frac{d l}{d x} \frac{d x}{d t} .\)</p>

<p> By the fundamental theorem of calculus:</p>

<p>
\[\frac{d l}{d x}=\sqrt{1+f^{\prime}(x)^{2}}\]
</p>

<p>From Lemma 1, we have \(f^{\prime}(1)=\cos (1)+\sin (1)\).</p>

<p>So at \(x=1\) we have<br></p>

<p>
\[ \frac{d l}{d x}=\sqrt{1+(\cos (1)+\sin (1))^{2}}=\sqrt{2+\sin 2}\]


The statement follows by substituting in the first equation.

</p>


<p><b>Lemma 1:</b> \(f^{\prime}(1) = \sin(1) + \cos(1)\)</p>

<p>\[f^{\prime}(x) = x^{(\cos (x)+\sin (x))-1}(-x \log (x) \sin (x)+x \log (x) \cos (x)+(\cos (x)+\sin (x))) \]
</p>

<p>Substitute \(x=1\) and \(\log (1) = 0\) in the above equation.
</p>


</details>


---

### Continuity of two functions
{: .d-inline-block}

A10, 2017
{: .label}


<p>
Consider the following function:
\[
f(x)=\left\{\begin{array}{ll}
x^{2} \cos \left(\frac{1}{x}\right), & x \neq 0 \\
a, & x=0
\end{array}\right.
\]
</p>

<p>(a) Find the value of \(a\) for which \(f\) is continuous.</p>

<p></p>

<p>(b) \(f^{\prime}(0)\)</p>

<p></p>

<p>(c) \(\lim_{x \rightarrow 0} f^{\prime}(x)\)</p>

<details><summary>Solution</summary>

<p>(a) \(\cos \left(\frac{1}{x}\right)\) is sandwiched between -1 and \(1,\) so \(\lim_{x \rightarrow 0} f(x)=0=a\) makes \(f\) continuous.</p>

<p>(b) Now \(f^{\prime}(0)=\lim_{h \rightarrow 0} \frac{h^{2} \cos \left(\frac{1}{h}\right)-0}{h}=\lim_{h \rightarrow 0} h \cos \left(\frac{1}{h}\right)\) which is similarly 0.</p>

<p>(c) For nonzero \(x,\) calculate \(f^{\prime}(x)=2 x \cos \left(\frac{1}{x}\right)+\sin \left(\frac{1}{x}\right),\) so \(\lim_{x \rightarrow 0} f^{\prime}(x)\) does not exist
\(\operatorname{as} \lim_{x \rightarrow 0} 2 x \cos \left(\frac{1}{x}\right)=0\) and \(\lim_{x \rightarrow 0} \sin \left(\frac{1}{x}\right)\) does not exist.
</p>

</details>



---


### Function with a maximum
{: .d-inline-block}

B1b, 2018
{: .label}


<p>
Suppose \(f\) is a differentiable function defined on a subset \(S\) of \(\mathbb{R}\). Define
\[
f^{\ast}(y):=\max_{x \in S}\{y x-f(x)\}
\]
whenever the above maximum is finite. For the function \(f(x)=-\ln (x),\) determine the set of points for which \(f^{\ast}\) is defined and find an expression for \(f^{\ast}(y)\) involving only \(y\) and constants.
</p>

<details><summary>Solution</summary>
First, note that the function \(f(x)\) is defined only for the positive values of \(x\).

Now if \(y \geq 0\) then the first derivative of \(x y+\ln (x)\) is \(y+\frac{1}{x}\) which is strictly positive for \(x>0 .\) Hence \(x y+\ln (x)\) is an increasing function and consequent ly \(f^{\ast}(y)\)
is not defined. Now if \(y<0\) then \(x=-\frac{1}{y}\) is the only critical point of \(x y+\ln (x)\). Either of the derivative test tells us that it is in fact the maxima. Hence, the domain of \(f^{\ast}(y)\) is \(y<0\) and

\[
f^{\ast}(y)=\ln \left(\frac{-1}{y}\right)-1
\]


</details>











