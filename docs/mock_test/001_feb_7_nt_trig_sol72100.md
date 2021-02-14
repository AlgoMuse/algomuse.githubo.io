---
layout: default
title: Mock test 1 Number theory and trigonometry
nav_exclude: true
---


#  MT #1: Number theory & Trigonometry [Solutions]
#### Timings: 10:30-13:30 Hrs &nbsp;&nbsp;  Date: 7 Feb 2021
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

<ol>

<p><li> If three numbers \(p\), \(p+2\) and \(p+4\) are primes. What is the value of \( p \)?</li></p>

<details open><summary>Sol.</summary> \(p=3\).

Let us see why no other value is possible. If \(p>3\), it can be expressed as either \( 3k+1 \) or \( 3k+2 \).

<ul>
<li><i>Case 1: </i> If \(p=3k+1\), then \(p+2 = 3(k+1) \) which is divisible by \(3\).</li>
<li><i>Case 2: </i> If \(p=3k+2\), then \(p+4 = 3(k+2) \) which is again divisible by \(3\).</li>
</ul>

</details>

<p>
<li>List all the numbers between 1 and 1000 that are both divisible by 7 and have exactly six factors.</li>
</p>

<details open markdown="1"><summary>Sol.</summary>

Suppose the prime factorization of \\(n\\) is \\(p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}\\), then \\(n\\) has \\( (a_1+1)(a_2+1)\cdots (a_k+1) \\) factors. If \\(n\\)
has six factors, its prime factorizaton must be of the form \\(p_1p_2^{2}\\) or \\(p_1^5\\).  Since \\(7^5\\) is greater than 1000, we only get numbers of the first kind.
Since \\(n\\) is also divisible by 7, either \\( p_1 \\) or \\(p_2\\) must be 7.


\\(n = a^2\cdot 7\\) | Number || \\(n = a\cdot 7^2\\) | Number
--|---||---|--
\\(2^2 \cdot 7\\) | \\(28\\) || \\(2 \cdot 7^2\\) | \\(98\\)
\\(3^2 \cdot 7\\) | \\(63\\) || \\(3 \cdot 7^2\\) | \\(147\\)
\\(5^2 \cdot 7\\) | \\(175\\) || \\(5 \cdot 7^2\\) | \\(245\\)
\\(11^2 \cdot 7\\) | \\(847\\) || \\(11 \cdot 7^2\\) | \\(539\\)
 | || \\(13 \cdot 7^2\\) | \\(637\\)
 | || \\(17 \cdot 7^2\\) | \\(833\\)
 | || \\(19 \cdot 7^2\\) | \\(931\\)


<br>
<i><b>Comment</b>. It was tedious to calculate these numbers. Must have chosen a smaller divisor like 3.</i>

</details>


<p> <li> Let \(x\)  be a real number such that \( \sec x-\tan x=1/3 \). Evaluate \( \sec x+\tan x \).</li> </p>


<details open><summary>Sol.</summary>

\begin{align}
\sec^2 x - \tan^2 x &= 1  \\
(\sec x - \tan x)(\sec x+\tan x) &= 1  \\
(\sec x + \tan x) &= 3
\end{align}


</details>



<p>
<li>Consider the two numbers \(a\) and \(b\) whose prime factorizations are as follows:

\[ a = 2\cdot 3\cdot 5^2 \cdot 7^3 \cdot 17^5 \cdot 23 \]
\[ b = 2\cdot 3^2\cdot 5 \cdot 7^3 \cdot 11 \cdot 17 \]
</li>

<ol>
<li>Write the prime factorization of the GCD of \(a\) and \(b\). [2 marks]</li>
<li>Write the prime factorization of the LCM of \(a\) and \(b\). [2 marks]</li>
</ol>

</p>

<details open><summary>Sol.</summary>

\begin{align}
\text{gcd}(a,b) &= 2\cdot 3\cdot 5 \cdot 7^3 \cdot 17 \\
\text{lcm}(a,b) &= 2\cdot 3^2\cdot 5^2 \cdot 7^3 \cdot 11 \cdot 17^5 \cdot 23
\end{align}


</details>






<p><li> Imagine a rectangular carrom board \(ABCD\) with \(AB=17 \) cm and \(BC=16 \) cm.  Assume the striker to be a point moving with no friction. The angle of reflection is equal to the angle of incidence. The striker is shot from point \(A\)
at an angle \(\alpha\). It bounces off the edges twice and ends up at corner \(C\) as shown below. What is the value of \(\tan \alpha\)?
</li></p>

<p style="text-align:center">
<img src="/assets/images/two_reflect.png"/>
</p>


<details open><summary>Sol.</summary>

Proof via unfolding:


<p style="text-align:center">
<img src="/assets/images/two_reflect_sol.png"/>
</p>

So, \( \tan \alpha = \frac{BC}{3AB} = \frac{16}{51} \).<br>


<br>
<i>Problem source:</i> Playing a game of billiard with Fibonacci <a href="https://arxiv.org/pdf/1906.01911.pdf">[pdf]</a>.

</details>



<p><li>How many ordered pairs of integers \( (x,y) \) satisfy the equation \( \frac{x}{20} = \frac{20}{y} \)?</li></p>

<details open><summary>Sol.</summary>


\[ x\cdot y = 400 = 2^4\cdot 5^2 \]

There are 15 factors of 400. If \(f\) is a factor, then \( (f,400/f) \) and \( (-f,-400/f) \) are two solutions. So there are 30 ordered pairs that satisfy
the equation.



</details>


<p>
<li> Count the number of ordered pairs \( (a,b) \)  that satisfy two conditions:

<ul>
<li>\(a\) and \(b\) are relatively prime positive integers</li>
<li>The product of \(a\) and \(b\) is \(10!\)</li>
</ul>
</li>
</p>


<details open><summary>Sol.</summary>

Given: \( a\cdot b = 10! \)

This is similar to the previous problem. The difference here is that since \( a \) and \( b \) are relatively prime they do not
share any common factors. 10! has 2, 3, 5 and 7 as its prime factors. So there are 16 choices.


</details>






<p><li>Find the remainder when \(2021^{2021}\) is divided by 7.</li></p>

<details open><summary>Sol.</summary>

Ans: 3.<br>

By Fermat's little theorem,  \( a^{p-1} \equiv 1 \pmod{p} \), if \(p\) is prime and \( (p,a) = 1\). <br>

For some integer \(k\), \(2021=6k+5\). We derive a sequence of equivalences:

\begin{align}
2021^{2021} \equiv 2021^{6k+5} \equiv 2021^5 \equiv 5^5 \equiv 25\times 25\times 5 \equiv 4\times 4\times 5 \equiv 3  \pmod{7}
\end{align}



</details>



<p><li>Identify the irrational numbers among the three numbers given below.</li></p>




<p>
<ol>
<li>\( \frac{2 \log (3)}{\log (2)+2 \log (3)} \) </li>
<li>\( \frac{\log 14}{\log 18} \) </li>
<li>\( \sqrt{3} + \sqrt{7} + \sqrt{17} - \sqrt{11}\) </li>
</ol>
</p>

<details open><summary>Sol.</summary>
Ans: All three of them are irrational. <br><br>



\( \frac{2 \log (3)}{\log (2)+2 \log (3)} = \frac{\log 9}{\log 18} \)


<p>
To see why (a) and (b) are irrational, see the solution to  <a href="/docs/number_theory/irrationality/#rationality-preserving-operations">A11, 2010</a>.  For (c), refer to the solution to <a href="/docs/number_theory/irrationality/#irrational-fraction">A3, 2012</a>.
</p>




</details>







<p><li>Consider the functions \(f_i\) given below:</li></p>


\begin{align}
f_{1}=(\tan \theta)^{\tan \theta} & \;\; f_{2}=(\tan \theta)^{\cot \theta} \\
f_{3}=(\cot \theta)^{\tan \theta} & \;\; f_{4}=(\cot \theta)^{\cot \theta}
\end{align}

<p>
Identify the function whose value is greater than others in the domain \(\theta \in \left(0,\pi/4\right) \).
</p>

<details open><summary>Sol.</summary>


<h4>Problem source</h4>

<img src="/assets/images/titu.png" style="float:left;margin-right:20px;margin-top:10px;"/>

<p>
<i>This problem and the third one are from the Andreescu & Feng <a href="https://mathematicalolympiads.files.wordpress.com/2012/08/103-trigonometry-problems-titu-andreescu-zuming-feng.pdf"> [pdf]</a>. The solution is reproduced below.
The book is a good source of problems in trigonometry. Problem <a href="http://localhost:4000/docs/geometry/coordinate_system/#mix-a-sin-and-a-circle">B4, 2014</a> directly came from this collection.</i>
</p>


<p>
For \( a>1 \) the function \( y=a^{x} \)  is an increasing function.
For \( 0^{\circ}< \theta<\pi/4,\cot \theta>1>\tan \theta>0 \). Thus \( f_{3}< f_{4} \).
For \( a<1 \), the function \( y=a^{x} \) is a decreasing function. Thus \( f_{1}> f_{2} \).
Again, by \( \cot \theta>1>\tan \theta>0 \),  we have \( f_{1}<1< f_{3} \). Hence \( f_{4}> f_{3}> f_{1}> f_{2} \).
</p>

</details>

</ol>

<br>

---





## Part B: Subjective questions

<p>
<b>B1</b>. Suppose \(x\) is an integer. What are the possible values of \( x^{65} \pmod{131} \) and why?
</p>


<details open><summary>Sol.</summary>

\(x = 0\) is an obvious solution. Since 131 is a prime, if \( x\neq 0\), by Fermat's little theorem:


\begin{align}
(x^{65})^2  & \equiv  1 \pmod{131}  \\
(x^{65})^2 - 1  & \equiv  0 \pmod{131} \;\;\;\; \text{ Subtracting 1 from both sides } \\
(x^{65} - 1)(x^{65}+1)  & \equiv  0 \pmod{131} \\
x^{65} = 1 \mbox{ or } -1
\end{align}


So the possible values of \(x\) are \( 0,1,130 \).


</details>


---

<p>
<b>B2</b>. A coordinate grid is made up of horizontal and vertical lines of the form \(x=k\) and \(y=k\), where \(k\in \mathbb{Z}\).
Consider a line segment OA where O is the origin and A is the point \(  (10,4) \). Notice that this line segment passes through the
interior of 12 cells. In the figure below, the shaded cells are the ones through which the line passes.
</p>


<p style="text-align:center">
<img src="/assets/images/mt_1_grid.jpg"/>
</p>


<p>
Suppose a line segment is drawn from the origin O to the point B at \( (48,54) \). How many cells would would OB pass through?
</p>


<details open><summary>Sol.</summary>

OB intersects the vertical grid lines 48 times and the horizontal grid lines 54 times (not counting the origin). Among these
there are \( gcd(48,54) = 6 \) common points.

Each shaded cell can be uniquely identified by the point at which OB exits the cell. Notice that there is a one-to-one correspondence between
the shaded cells (exit points) and the intersection points.  So there are \( 48+54-6 = 96 \) shaded cells.

</details>




---

<p><b>B3</b>. Suppose \( f(x)=\cos^{-1}(\cos (\pi x)) \). Find the value of \( f(2.6) \).</p>



<details open><summary>Sol.</summary>


\begin{align}
f(x)&=\cos ^{-1}(\cos (\pi x)) \\
f(2.6)&= \cos ^{-1}(\cos (2.6 \pi)) \\
&=\cos ^{-1}\left(\cos \left(2 \pi+\frac{3}{5} \pi\right)\right) \\
&=\cos ^{-1}\left(\cos \left(\frac{3}{5} \pi\right)\right) \\
&=\frac{3}{5} \pi
\end{align}



</details>

---


<p>
<b>B4</b>. Find five unique positive integers \( b_{1}, b_{2}, \cdots, b_{5} \geq 2 \) such that:

\[ \Large \frac{125}{76}=b_{1}-\frac{1}{b_{2}-\frac{1}{b_{3}- \frac{1}{b_4 - \frac{1}{b_5} }  }} \]
</p>


<p>
You may find the following fact useful:
</p>

<p>
Let \(q\) and \(n\) be relatively prime positive integers such that \( 1 < q < n \).
There exist unique integers \( k, r \) such that \( n=kq-r, 0 \leq r< q \).
</p>

<details open><summary>Sol.</summary>
\begin{align}
\frac{125}{76} &=\frac{76 \times 2-27}{76}  \\
&=2-\frac{27}{76}  \\
&=2-\frac{1}{\frac{76}{27}} \\
&=2-\frac{1}{\frac{27 \times 3-5}{27}}  \\
&=2-\frac{1}{3-\frac{1}{\frac{27}{5}}} \\
&=2-\frac{1}{3-\frac{1}{6-\frac{1}{\frac{15}{3}}}} \\
&=2-\frac{1}{3-\frac{1}{6-\frac{1}{2-\frac{1}{3}}}}
\end{align}
</details>





---


<p>
<b>B5</b>. Find all the positive integer solutions to the following equation:
\[ xyz-xy-yz-xz+x+y+z=52 \]

Express the solutions as triplets \( (x,y,z) \).
</p>


<details open><summary>Sol.</summary>

<p>
\begin{align*}
xyz-xy-yz-xz+x+y+z-1&=51 \\
(x-1)(y-1)(z-1) &= 51
\end{align*}

The LHS is a product of three numbers. It may either be \( 1 \times 1 \times 51 \) or \(1\times 3\times 17\).


So \( (x,y,z) = (2,2,52) \mbox{ or } (2,4,18) \) or any permutation of the two triplets.


</p>


</details>

---





<p>
<b>B6</b>. Prove that there are no integers \(x>0\) and \(n>1\) such that  \( x(x+1) = 2442^n \).
</p>


<p>
<i>Problem source: Nick's mathematical puzzles <a href="http://www.qbyte.org/puzzles/p065s.html">link</a></i>. <br><br>

The result holds for any \(y^n\) in the RHS.


Suppose the prime factorization of \(y\) is \(p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}\).

Since \(x\) and \(x+1\) are relatively prime, they do not share any common factors. So for any \(p_i\),
either \(p_i^{a_in} | x\) or \(p_i^{a_in}| (x+1)\) but not both. This means that \(x=r^n\) for some \(r\) and \( (x+1) \) = \(s^n\) for some \(s>r\).

Thus we have the relation:

\[ s^n - r^n = 1  \]

But the LHS is always \( \geq 3 \) for \( n> 1\). Thus we have a contradiction.




</p>

<!--

### Practice problems on number theory

<a href="http://math.northwestern.edu/putnam/training-numth.pdf">Putnam training</a>

-->


<!--
Please note: There was a typo in the last problem B6 earlier. It's 2442 not 2021.
{: .bg-red-000 .p-6 }
-->




