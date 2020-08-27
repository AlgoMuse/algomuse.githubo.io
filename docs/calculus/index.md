---
layout: default
title: Calculus
nav_order: 92
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

B1, 2017
{: label .label-blue}


<p>
Find the number of solutions to \(e^{x}=\frac{x}{2017}+1\)
</p>

<details><summary>Solution</summary>

<p>
This problem is similar to the last one. We need to show that the function is monotonic in some interval.
Consider the function:
\begin{align}
f(x)&=  e^x -\frac{x}{2017} - 1 \\
f'(x)&=  e^x -\frac{1}{2017}
\end{align}


The derivative is positive when \(x> x_0=-\log 2017\).

<ul>
<li>We have \(f(x_0)< 0\) and \( f(-\infty)>0 \) so there is one solution in the interval \((-\infty,x_0)\).</li>
<li>\( x = 0 \) is another solution.</li>
</ul>

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

Sol.


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

Sol.

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
<b>Case 3.</b> Suppose \(1 / 4 \leq a \leq 1 .\) Now \(f^{\prime}(x)=0\) at \(\tilde{x}=\frac{1}{\sqrt{a}}-1 .\) For this range of \(a, \tilde{x} \in[0,1]\) In the interval \([0, \tilde{x}], f^{\prime}(x) \leq 0\) and in the interval \([\tilde{x}, 1], f^{\prime}(x) \geq 0 .\) Now we make two sub-cases depending on at which endpoint the maximum occurs.
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
















