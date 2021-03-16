---
layout: default
title: Mock test 4
nav_exclude: true
---


#  MT #4: Limits and derivatives
#### Timings: 17:00-20:00 Hrs &nbsp;&nbsp;  Date: 10 March 2021
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

<ol>


<p>
<li>
Suppose \(p(x)\) and \(q(x)\) are polynomials such that:
\[ p(x) = (x-1)q(x) \]

If \( p^{\prime}(1)=1\), what is the value of \( q(1) \)?
</li>
</p>


<details open><summary>Sol.</summary>

\begin{align*}
p^{\prime}(x) &= q(x) + q^{\prime}(x)(x-1) \\
p^{\prime}(1) &= q(1) \\
q(1) &= 1
\end{align*}

</details>

<p>
<li>Let \(D_1\) denote the set of positive one-digit numbers, \(D_3\) the set of three digit numbers and in general \(D_n\) the set of \(n\)-digit numbers.
Consider the following sum for any odd \(n\):

\[ S_{n} = \sum_{k_1\in D_1} \frac{1}{k_1} + \sum_{k_3\in D_3} \frac{1}{k_3} + \sum_{k_5\in D_5} \frac{1}{k_5} + \cdots + \sum_{k_n\in D_n} \frac{1}{k_n} \]

As \(n\) tends to infinity, to what value does \(S_n\) tend to?


</li>
</p>


<details open><summary>Sol.</summary>
<p>
There are \(9\times 10^{d-1}\) \(d\)-digit numbers. The largest number among them is \(10^{d}-1\). Consider the summand for the \(d\)-digit numbers:<br>

\[ \sum_{k_d \in D_d} \frac{1}{k_d}  > \frac{9\times 10^{d-1}}{10^d-1} > \frac{9\times 10^{d-1}}{10^d} = \frac{9}{10} \]

Since each summand is greater than \(9/10\), the sum \(S_n\) diverges to \(\infty\).
</p>

</details>



<p>
<li>
Consider the function \(f: \mathbb{R} \rightarrow \mathbb{R}\) given by \( f(x)=(x-1)|(x-1)(x-2)|\). The function \(f\) is
<ol>
<li> differentiable at \(x=1\) and \(x=2\).</li>
<li> differentiable at \(x=1\) but not at \(x=2\).</li>
<li> differentiable at \(x=2\) but not at \(x=1\).</li>
<li> neither differentiable at \(x=1\) nor at \(x=2\).</li>
</ol>
</li>
Pick the right option.
</p>


<details open><summary>Sol.</summary>

<b>Ans: (b)</b><br>

Let us apply the definition:<br>

\[ \lim_{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}= |(x-1)(x-2)| = \lim_{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1} =  0 \]
\[ \lim_{x \rightarrow 2^{+}} \frac{f(x)-f(2)}{x-2} = (x-1)^2 = 1 \]
\[ \lim_{x \rightarrow 2^{-}} \frac{f(x)-f(2)}{x-2} = -(x-1)^2 = -1 \]

So the given function is differentiable at 1 but not differentiable at 2.

</details>




<p>
<li>What is the smallest value of \(n\) for which the following limit exists?</li>

\[ \lim_{x \rightarrow 0} \frac{\sin^{n}x}{\cos^{4}x(1-\cos x)^{3}} \]

</p>

<details open><summary>Sol.</summary>

First, note that the \(\cos^{4}x\) in the denominator converges to 1 always.
The Taylor series expansions of \(\sin x\) and \(1-\cos x\) to first order are \(x\) and

\(\frac{x^{2}}{2}\), respectively. That means that:<br>

\[ \lim_{x \rightarrow 0} \frac{\sin ^{n} x}{\cos ^{2} x(1-\cos x)^{3}}=\lim_{x \rightarrow 0} \frac{x^{n}}{\left(x^{2} / 2\right)^{3}} \]

The limit exists exactly when the exponent of \(x\) in the numerator is at least the exponent of \(x\) in the denominator, so \(n\) must be at least 6.

<br>

<i>Problem source: SMT 2019.</i>

</details>



<p>

<li>We have a tape that is wound as a spool around axle \(A\). There is an axle \(B\) that
winds the tape around itself at constant speed. In other words, a fixed length of tape is transfered in one minute from spool \(A\) to \(B\). Let the instantaneous radius
of the spool \(A\) be \(r\). Intially, at \(t=0\) minutes, \(r=R \) cm. At \(t=50\) minutes, \(r=0\) cm. <b>Qualitatively</b>, sketch the value of \(r\) as a function of time.</li>

<p style="text-align:center">
<img src="/assets/images/spool.png"/>
</p>

<br>

<details open><summary>Sol.</summary>

The radius decreases rapidly as time approaches 50 minutes.<br>

<p style="text-align:center">
<img src="/assets/images/spool_graph_sol.png"/>
</p>

</details>



</p>





<p>
<li>
Let  \(f_{0}(x)=(\sqrt[3]{e})^{x}\).  For \(n\geq 0\), we define \(f_{n+1}(x)=f_{n}^{\prime}(x)\). Compute \( \sum_{i=0}^{\infty} f_{i}(1) \).
</li>

<details open><summary>Sol.</summary>

 \(\sqrt[3]{e}^x = e^{x / 3}\). Then, we can see by induction that \( f_{n}(x)=\frac{1}{3^{n}} e^{x / 3}\)  and
hence the infinite sum is a geometric series with ratio \( \frac{1}{3} \).

\[ \sum_{i=0}^{\infty} f_{i}(1)=\sum_{i=0}^{\infty} \frac{1}{3^{i}} e^{1 / 3}=\frac{3\sqrt[3]{e}}{2} \]


</details>




</p>


<p>
<li>
Alice and Bob are standing on a playground and Alice is 400m directly East of Bob. Alice starts to walk North at a rate of 3 m/sec, while Bob
starts to walk South at the same time at a rate of 7 m/sec. After 30 seconds, at what rate is the distance between Alice and Bob changing?
</li>
</p>

<details open><summary>Sol.</summary>

We can model the rate of change as a right-angle triangle with
base \(x=400\) m and height \(y\) increasing at a rate of 10 m/sec. After 30 seconds, we will have \(y=300\) m.

Let \(z\) denote the distance between Alice and Bob, then \(z\) is the hypotenuse of the right triangle.
Thus, the distance between Alice and Bob after 30 seconds is \(z=500\) m.

\begin{align*}
z^{2}&=x^{2}+y^{2}\\
2 z \cdot z^{\prime}&=2 x \cdot x^{\prime}+2 y \cdot y^{\prime}
\end{align*}



Plugging in our values, we get \(2 \cdot 500 z^{\prime}=2 \cdot 400 \cdot 0+2 \cdot 300 \cdot 10\), which gives us \(z^{\prime}=6\) m per second.

</details>


<p>
<li>Suppose \(p(x) = x^3 + x^2 + 2x + k\). Which of the following statements is true?</li>

<ol>
<li>\( p(x) \) has exactly one real root for any value of \(k\).</li>
<li> For some real number \(k\), \(p(x)\) has more than one real root.</li>
</ol>

</p>

<details open><summary>Sol.</summary>
\[ p^{\prime}(x) = 3x^2 + 2x + 2 > 0 \; \text{for every }\; x\]
Hence, the function is monotone. Since the polynomial is cubic it has exactly one real root.
</details>

<p>
<li>Calculate the value of the infinite series:</li>

\[ \sum_{k=1}^{\infty} \frac{1}{2 k^{2}-k} \]
</p>

<details open><summary>Sol.</summary>


Rewrite the general term as:

\[ \frac{1}{2 k^{2}-k}=\frac{2}{2 k-1}-\frac{2}{2 k} \]

Therefore,
\begin{align*}
\sum_{k=1}^{\infty} \frac{1}{2 k^{2}-k} & =2 \sum_{k=1}^{\infty}\left(\frac{1}{2 k-1}-\frac{1}{2 k}\right) \\
& =2\left(1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots\right)\\
&=2 \ln 2
\end{align*}

</details>


<p>
<li>Evaluate:
\[ \lim_{n \rightarrow \infty} 4^{n}\left(1-\cos \left(\pi / 2^{n+1}\right) \right) \]

</li>
</p>
<details open><summary>Sol.</summary>

<b>Ans.</b> \(\frac{\pi^2}{8}\).<br>

Using the Taylor series expansion, we have:<br>

\begin{align*}
4^{n}\left(1-\cos \left(\pi / 2^{n+1}\right)\right) &=4^{n}\left(1-\left(1-1 \frac{\left(\frac{\pi}{2^{n+1}}\right)^{2}}{2 !}+\frac{\left(\frac{\pi}{2^{n+1}}\right)^{4}}{4 !}-\ldots\right)\right) \\
&=\frac{\pi^2}{8} + \text{terms having } 4^n \text{ in the denominator}
\end{align*}

</details>



</ol>



## Part B: Subjective questions

<p>
<li> <b>B1.</b> Consider an axis-parallel rectangle with its bottom-left corner at the origin and top-right corner on the curve \(y=-\ln 3x\). What is the maximum area
that can be attained by any such rectangle?</li>

<p style="text-align:center">
<img src="/assets/images/mt4_max_rect.png"/>
</p>

<i>Problem source: SMT</i><br>

</p>


<details open><summary>Sol.</summary>
The area of the rectangle is \(x y=-x \ln (3 x)\).
The maximum occurs when \( (x y)^{\prime}=0,\) or \(-\ln (3 x)-1=0\). Hence \(x=e^{-1} / 3\) and \(y=1\). So, the maximum area is \(1/3e\).
</details>




<p>
<b>B2.</b> A fractal region is constructed as follows. Initially, a unit square is added at \(t=1 s\).
At each subsequent time step \(t\), new squares of size \(s_t\) are added to the region as follows.
<br>
<br>


For each square \(S\) that was added at time step \(t-1\):
<ul>
<li>Add a square with side length \(s_t = s_{t-1}/2\) to each of the free corners of \(S\).</li>
</ul>

The figure below shows the region after the third time step. Squares of the same shade were added at the same time step. As \(t\) tends to infinity, what value does the area of the region approach?

<p style="text-align:center">
<img src="/assets/images/square_fractal.png"/>
</p>


</p>


<details open><summary>Sol.</summary>
Suppose the area of the squares added at time \(t>2\)s is \(A\). The area of the squares added at time \(t+1\) is \(3A/4\). For \(t\leq 2\), \(A=1\), hence
the total area of the fractal region is:

\begin{align*}
&=1 + 1 + \frac{3}{4} + \frac{3^2}{4^2} + \ldots \\
&=1 +  \left( \frac{1}{1-3/4} \right) \\
&=5 \text{ sq. units}
\end{align*}



</details>



<p><b>B3.</b> Let \(x_{0}=1\) and
\[ x_{n}=\frac{3+2 x_{n-1}}{3+x_{n-1}} \]
for \(n=1,2, \ldots .\)<br>

(a) Prove that the sequence converges, that is, \( \lim_{n \rightarrow \infty} x_{n} \) exists. [6 marks]<br>

(b) Find the value of the above limit. [4 marks]

<br>
<i>Problem source: Berkeley problems in mathematics.</i>
<br>
</p>



<details open><summary>Sol.</summary>

(a)

\begin{aligned}
x_{n+1}-x_{n} &=\frac{3+2 x_{n}}{3+x_{n}}-\frac{3+2 x_{n-1}}{3+x_{n-1}} \\
&=\frac{3\left(x_{n}-x_{n-1}\right)}{\left(3+x_{n}\right)\left(3+x_{n+1}\right)}
\end{aligned}


Since \(x_n\geq 1\) for all \(n\) we have \( \left|x_{n+1}-x_{n}\right| \leq \frac{1}{3}\left|x_{n}-x_{n-1}\right|\).

Iteration gives<br>

\[ \left|x_{n+1}-x_{n}\right| \leq 3^{-n}\left|x_{1}-x_{0}\right|=\frac{1}{3^{n} \cdot 4} \]

The series \( \sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right) \) of positive terms,
is dominated by the convergent series \( \frac{1}{4} \sum_{n=1}^{\infty} 3^{-n} \)
and so converges.<br>

We have \( \sum_{n=1}^{\infty}\left(x_{n+1}-x_{n}\right)=\lim_{n \rightarrow \infty} x_{n}-x_{1}\)  and we are done.


<br>

(b) Let the limit be \(L\).

\begin{align*}
L &= \frac{3+2L}{3+L} \\
L^2 + L - 3 &= 0 \\
L &= \frac{1}{2}(-1+\sqrt{13})
\end{align*}

</details>




<p>
<b>B4.</b> Find the value of the limit:
\[ \lim_{x \rightarrow 0} \frac{1}{x} \ln \left(\frac{e^{x}-1}{x}\right) \]
</p>
<details open><summary>Sol.</summary>

We use the fact that \( \lim_{x\rightarrow 0} \ln (1+x) = x \), we have:


\begin{align*}
\lim_{x \rightarrow 0} \frac{1}{x} \ln \left(\frac{e^{x}-1}{x}\right) &= \lim_{x\rightarrow 0} \frac{1}{x} \left( \frac{e^x-1}{x} - 1   \right) \\
&= \lim_{x\rightarrow 0}  \frac{e^x-1-x}{x^2} \\
&= \lim_{x\rightarrow 0}  \frac{e^x-1-x}{x^2} \\
&= \lim_{x\rightarrow 0}  \frac{e^x-1}{2x} \;\;\;\;\; \text{using L'Hospital} \\
&= \frac{1}{2}\;\;\;\;\;\;\;\; \text{using}\;\; \frac{e^{a}-1}{a} \rightarrow\left(e^{x}\right)^{\prime}(0)=1
\end{align*}



</details>


<p>
<b>B5.</b> A monic polynomial is a polynomial with leading coefficient as 1.  Suppose \(p\) is a monic polynomial with real coefficients.
Let  \( \lim_{x \rightarrow \infty} p^{\prime \prime}(x)=\lim_{x \rightarrow \infty} p\left(\frac{1}{x}\right) \) and \( p(x) \geq p(2) \) for all \( x \in \mathbb{R} \). Find \( p(x) \).
</p>


<details open><summary>Sol.</summary>

\begin{align*}
p(x)&=a_{0}+a_{1} x+a_{2} x^{2}+\cdots+a_{n} x^{n}\\
p^{\prime \prime}(x)&=2 a_{2}+6 a_{3} x+\cdots+n(n-1) a_{n} x^{n-2}\\
p\left(\frac{1}{x}\right)&= a_{0}+a_{1}\left(\frac{1}{x}\right)+\cdots+a_{n}\left(\frac{1}{x}\right)^{n}
\end{align*}

Now \(\lim_{x \rightarrow \infty} p\left(\frac{1}{x}\right)=a_{0}\). Therefore \( \lim_{x \rightarrow \infty} p^{\prime \prime}(x)=a_{0}\).<br>

Hence \(p^{\prime \prime}(x)=2 a_{2}\) and \(a_{3}=a_{4}=\cdots=a_{n}=0\). Hence, \(p\) is a quadratic with leading co-efficient 1.<br>

Now \( \lim_{x \rightarrow \infty} p^{\prime \prime}(x)=\lim_{x \rightarrow \infty} p\left(\frac{1}{x}\right)\)
implies \( a_{0}=2 a_{2}=2\). Also \( p(x) \geq p(2)\) for all \( x \in \mathbb{R}\) implies \(p\) has minimum at \(x=2\).

<br>
Therefore \(p^{\prime}(2)=0\). Hence \( a_{1}+2 a_{2}=0 \) . Therefore \( a_{1}=-4 \). Hence \( p(x)=x^{2}-4 x+2 \).



</details>


<p>
<b>B6.</b> Let \(p(x)\) be a polynomial with only real roots. Show that for every \(x\):
\[ p^{\prime}(x)^2 \geq p(x) p^{\prime\prime}(x) \]

<br>
<i>Problem source: Proofs from the book</i>
<br>
</p>



<details open><summary>Sol.</summary>

The inequality holds trivially if \(x=a_{i}\) is a root of \(p(x)\). Assume then \(x\) is not a root.<br>

The product rule of differentiation yields:

\[ p^{\prime}(x)=\sum_{k=1}^{n} \frac{p(x)}{x-a_{k}}, \quad \text { that is, } \quad \frac{p^{\prime}(x)}{p(x)}=\sum_{k=1}^{n} \frac{1}{x-a_{k}} \]

Differentiating this again we have
\[ \frac{p^{\prime \prime}(x) p(x)-p^{\prime}(x)^{2}}{p(x)^{2}}=-\sum_{k=1}^{n} \frac{1}{\left(x-a_{k}\right)^{2}}<0 \]

</details>



