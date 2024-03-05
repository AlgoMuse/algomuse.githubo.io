---
layout: default
title: Mock test 3 Full-syllabus test
nav_exclude: true
---


#  Mock test #3 '24: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 10 Feb 2024
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg or PartA.png.
{: .fs-3 }

**For this part, answers must be written without any explanation.**

<ol>

<li>
What is the least positive integer \(m\) such that \(m\cdot2!\cdot3!\cdot4!\cdot5!...16!\) is a perfect square?

<ol>
<li>30</li>
<li>70</li>
<li>140</li>
<li>300</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (b) 
<i>Source: AMC '23. Solution due to Technodoggo (AoPS).</i>
Consider 2 - there are odd number of 2's in \(2 ! \cdot 3 ! \cdot 4 ! \cdot 5 ! \ldots 16\) ! (We're not counting 32 's in 8,23 's in 9 , etc).
There are even number of 3s in ... etc. So, we can reduce our original expression to
        \[
\begin{align*}
m \cdot 2 \cdot 4 \cdot 6 \cdot 8 \cdot 10 \cdot 12 \cdot 14 \cdot 16 & \equiv m \cdot 2^8 \cdot(1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 \cdot 8) \\
& \equiv m \cdot 2 \cdot 3 \cdot(2 \cdot 2) \cdot 5 \cdot(2 \cdot 3) \cdot 7 \cdot(2 \cdot 2 \cdot 2) \\
& \equiv m \cdot 2 \cdot 5 \cdot 7 \\
m & =2 \cdot 5 \cdot 7=70
\end{align*}
        \]
</details>



<li>
Let \(h\) be a function defined for all \(x \in(0,1)\) as
\[ h(x)=\frac{x^4}{(1-x)^6} \]
</li>

<ol>
<li> \(h\) is a strictly decreasing function.  </li>
<li> \(h\) is a strictly increasing function.  </li>
<li> \(h\) is unimodal.                        </li>
<li> \(h\) is discontinous at a few points.    </li>
</ol>

<details open><summary>Sol.</summary>
Ans. (b)
</details>


<li>
Each of 1001 balls is randomly placed into one of 3 bins.
Which of the following is closest to the probability that each of the bins will contain an odd number of balls?


<ol>
<li>1/2</li>
<li>3/8</li>
<li>1/4</li>
<li>2/7</li>
</ol>

</li>


<details open><summary>Sol.</summary>
<b>Ans.</b> (c).<br>
Having 2 bins with an odd number of balls means the 3rd bin also has an odd number.
The probability of the first bin having an odd number of balls is \(\frac{1}{2}\), since even and odd have roughly the same probability.
The probability of the second bin having an odd number of balls is also \(\frac{1}{2}\) for the same reason.
If both of these bins have an odd number of balls, the number of balls remaining for the third bin is also odd. Therefore the probability is \(\frac{1}{2} \cdot \frac{1}{2}=(\mathbf{E}) \frac{1}{4}\).
<br><i>Solution due to Yash. Source: AoPS.</i>
</details>


<li>
The value of \(\int_a^b \sin x d x\) is EXP for some real number \(c\) such that \(a \leq c \leq b\), where EXP is

<ol>
<li>  \((b-a) \sin c\)      </li>
<li>  \((b-a) \cos c\)      </li>
<li>  \(\frac{\sin c}{b-a}\)</li>
<li>  \(\frac{\cos c}{b-a}\)</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (a) <br>
Since the function \(f(x)=\sin x\) is continuous in \([a, b]\), by the mean-value theorem there is \(c \in[a, b]\) such that the integral \(=(b-a) f(c)\).<br>
<i>Source: MMC 2015.</i>
</details>


<li>
Let \(f:\mathbb{R} \rightarrow \mathbb{R}\) be a periodic function with period \(T\). 
We say that a chord of length \(l\) if \(f(x_0) = f(x_0+l)\) for some \(x_0 \in \mathbb{R}\). 
Pick the most general statement that is true among the following options:


<ol>
<li>  There exists a chord of length \(T/2\).</li>
<li>  There exists a chord of any length less than or equal to \(T\).</li>
<li>  There exists a chord of any arbitrary length.</li>
</ol>
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (c) <br>
\(f(x)\). In other words, we must show that the function \(g(x)=f(x+T / 2)-f(x)\) has a root-that is, \(g(x)=0\) for a certain \(x\).

Let's take an arbitrary number \(a\). If \(g(a)=0\), we're all done. So we'll assume that \(g(a)\) is nonzero.
To be definite, let's suppose \(g(a)<0\). Let \(b=a+T / 2\). We can easily compute \(g(b)\) :

\begin{align*}
g(b) & =g(a+T / 2) \\
& =f(a+T / 2+T / 2)-f(a+T / 2) \\
& =f(a+T)-f(a+T / 2) \\
& =f(a)-f(a+T / 2) \\
& =-g(a) .
\end{align*}

Therefore, \(g(b)>0\).
The function \(g(x)\) is continuous, since it's the difference of continuous functions. So once again we can use the intermediate value theorem, which implies that there is a number \(x\) between \(a\) and \(b\) such that \(g(x)=0\).

The statement about horizontal chords of graphs of continuous periodic functions can be considerably strengthened: The graph of such a function has a horizontal chord of arbitrary length.
<i>Source: Quantum P2.</i>
</details>


<li>
Define the function \(f: \mathbb{R} \rightarrow \mathbb{R}\) as:
\[ f(x)= \begin{cases}x^2 & \text { if } x \text { is rational } \\ x^3 & \text { if } x \text { is irrational }\end{cases}
\]

<ol>
<li>  \(f\) is continuous at 0.</li>
<li>  \(f\) is continuous at 1.</li>
<li>  \(f\) is continuous at -1.</li>
<li>  \(f\) is continuous at more than three points.</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (a) and (b) <br>
<i>Source: MMC '15.</i>
</details>



<li>
Suppose \(a, b\), and \(c\) are positive integers such that
\[ \frac{a}{14}+\frac{b}{15}=\frac{c}{210} \]
Which of the following statements are necessarily true?
</li>

<ol>
<li> If \(\operatorname{gcd}(a, 14)=1\) or \(\operatorname{gcd}(b, 15)=1\) or both, then \(\operatorname{gcd}(c, 210)=1\).  </li>
<li> If \(\operatorname{gcd}(c, 210)=1\), then \(\operatorname{gcd}(a, 14)=1\) or \(\operatorname{gcd}(b, 15)=1\) or both.  </li>
<li> We have \(\mbox{gcd}(c, 210)=1\) if and only if \(\mbox{gcd}(a, 14) = 1\) and \(\mbox{gcd}(b, 15)=1\). </li>
</ol>

<details open><summary>Sol.</summary>
<b>Ans.</b> (b) and (c) <br>
<i>Source: AMC '23. Solution due to Technodoggo (AoPS).</i> We look at each of the conditions.
A counterexample to the first condition is \(a=3\) and \(b=5\). The corresponding value of \(c\) is \(17 \cdot 15=255\).
Clearly, \(\operatorname{gcd}(3,14)=1\) and \(\operatorname{gcd}(5,15)=5\), so condition \(I\) would imply that \(\operatorname{gcd}(c, 210)=1\).
However, \(\operatorname{gcd}(255,210)\) is clearly not 1 (they share a common factor of 5 ).
We look at the second statement's contrapositive to prove it.
The contrapositive states that if \(\operatorname{gcd}(a, 14) \neq 1\) and \(\operatorname{gcd}(b, 15) \neq 1\),
then \(\operatorname{gcd}(c, 210) \neq 1\).
In other words, if \(a\) shares some common factor that is not 1 with 14 and \(b\) shares some common factor that is not 1 with 15, then \(c\) also shares a common factor with 210.
Let's say that \(a=a^{\prime} \cdot n\), where \(a^{\prime}\) is a factor of 14 not equal to 1.
So \(a^{\prime}\) is the common factor.
We can rewrite the given equation as \(15 a+14 b=c \Longrightarrow 15\left(a^{\prime} n\right)+14 b=c\). We can express 14 as \(a^{\prime} \cdot n^{\prime}\), for some positive integer \(n^{\prime}\) (this \(n^{\prime}\) can be 1). We can factor \(a^{\prime}\) out to get \(a^{\prime}\left(15 n+14 n^{\prime}\right)=c\).
We know that all values in this equation are integers, so \(c\) must be divisible by \(a^{\prime}\). Since \(a^{\prime}\) is a factor of \(14, a^{\prime}\) must also be a factor of 210 , a multiple of 14 . Therefore, we know that \(c\) shares a common factor with 210 (which is \(a^{\prime}\) ), so \(\operatorname{gcd}(c, 210) \neq 1\). This is what \(I I\) states, so therefore \(I I\) is true.
</details>


<li>
A rectangle is partitioned into \(5\) regions as shown. Each region is to be painted a solid color. The five available
colors are red, orange, yellow, blue, or green. Regions that touch are painted different colors,
and colors can be used more than once. How many different colorings are possible?
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> 540. <br>
The top left rectangle can be \(5\) possible colors. Then the bottom left region can only be \(4\) possible colors, and the bottom middle can only be \(3\) colors since it is next to the top left and bottom left. Similarly, we have \(3\) choices for the top right and \(3\) choices for the bottom right, which gives us a total of \(5\cdot 4 \cdot 3 \cdot 3 \cdot 3 = 540\).
</details>


<li>
Find the remainder when \(f\left(x^3\right)\) is divided by \(f(x)\) where \(f(x)=1+x+x^2\).
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> 3. <br>
Let \(f(x)=1+x+x^2\). Then \((x-1) f(x)=x^3-1\). Therefore \(f(x) \mid\left(x^3-1\right)\).
Now \(f\left(x^3\right)=1+x^3+x^6=3-2+x^3+x^6=\left(x^3-1\right)+\left(x^6-1\right)+3\).
Therefore \(f(x) \mid\left[f\left(x^3\right)-3\right]\). Hence the required remainder is 3, since \(f\) being a polynomial of degree 2 , the unique remainder is of the form \(a x+b\).
</details>


<li>
Anil starts with a single \(1 \times 1\) square of chocolate and then adds more rows and columns from there.
Suppose his current bar has dimensions \(w \times h\), where \(w\) denotes the number of columns and \(h\) the number of rows.
It then costs \(w^2\) dollars to add another row and \(h^2\) dollars to add another column.
What is the minimum cost to get his chocolate bar to size \(10 \times 10\)?
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> 284. <br>
The optimal way to add rows and columns to the \(1 \times 1\) chocolate to the \(10 \times 10\) chocolate is to alternate adding rows and columns.
If we do this, then the costs are \(1^2\) for the first row, plus \(2^2\) for the first column, plus \(2^2\) for the second row, plus \(3^2+3^2+4^2+\cdots\).
<i>Claim</i>. The sum of the first \(n\) squares can be calculated as \(\frac{n(n+1)(2 n+1)}{6}\).<br>

<i>Proof:</i> Assume \(w>h\) (more columns than rows).
Adding a column and then a row costs \(h^2+(w+1)^2\).
Adding a row and then a column costs \(w^2+(h+1)^2\).
Since \(w>h\), we have \(h^2+(w+1)^2=h^2+w^2+2 w+1>h^2+w^2+2 h+1=w^2+(h+1)^2\).
Therefore, it's always more optimal to add a row first in this case. We can see that alternating rows and columns is optimal.
The formula for the overall cost to get to \(n \times n\) is \(1^2+\) \(2 \cdot 2^2+2 \cdot 3^2+\cdots+2 \cdot(n-1)^2+n^2\).
Thus, the desired sum is \(\frac{n(n+1)(2 n+1)}{3}-1-n^2\). For \(n=10\) this equals \(\frac{10 \cdot 11 \cdot 21}{3}-1-10^2=284\).
</details>

</ol>


## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---


<p><b>B1.</b> 
Let \(a\) and \(c\) be natural numbers that are coprime. Prove there exists a natural number \(b\) such that \(c^b-1\) is divisible by \(a\).
</p>

<details><summary>Sol.</summary>
Consider \(a+1\) numbers \(c^0-1,c^1-1\), \(\ldots, c^a-1\). Since there are only \(a\) different remainders modulo \(a\),
we can find two of the above numbers giving the same remainders modulo \(a\) (pigeon-hole principle).
If these numbers are \(c^k-1\) and \(c^m-1\) with \(k< m\), then \(\left(c^m-1\right)-\left(c^k-1\right)=c^k\left(c^{m-k}-1\right)\) is divisible by \(a\).
Since \(\mbox{gcd}(a,c)=1\), \(a\) and \(c^k\) have no common factors. Hence, \(c^{m-k}-1\) is divisible by \(a\).

<br><i>Source:</i> Quantum P1 issue (Problem corner). https://static.nsta.org/pdfs/QuantumP1.pdf
</details>

---

<p><b>B2.</b>
Several circles are drawn inside a unit square. Prove that if the sum of their circumferences is equal to 10,
there exists a straight line that intersects at least four circles.
</p>


<details><summary>Sol.</summary>
Project all the circles perpendicularly onto some side \(A B\) of the square (see figure below)
and assume that every line intersects no more than three circles.
Any point of the segment \(A B\) is thus covered by projections of circles no more than three times.
It follows that the length of all projections is less than or equal to 3.
But this length is also equal to the sum of the diameters of all the circles.
Thus, the sum of the circumferences of the circles is less than or equal to \(3 \pi\).
Since \(3 \pi< 10\), this contradicts the original assumption that this sum is equal to 10.
Source: Quantum P1 issue (Problem corner). https://static.nsta.org/pdfs/QuantumP1.pdf
</details>

---

<p><b>B3.</b>
Let \(P_t\) be the point of intersection of the line segment \(L_t\) with the parabola \(y=x^2\).
Define function \(f: \mathbb{R} \rightarrow \mathbb{R}\) as \(f(t)=y\) coordinate of point \(P_t\).
Answer the following with reasoning.<br>

(a) Is \(f\) a bounded function? <br>
(b) Is \(f\) a continuous function?<br>
(c) Find \(\lim_{t \rightarrow \infty} f(t)\).<br>
(d) Is \(f\) differentiable at 0?<br>
</p>

<details><summary>Sol.</summary>
The equation of line \(L_t\) is : \(y=1-\frac{x}{t}\). Thus, \(x-\) coordinate of the point of intersection of \(L_t\) with the parabola \(y=x^2\) satisfy \(1-\frac{x}{t}=x^2\). This gives \(x=-\frac{\frac{1}{t} \pm \sqrt{\frac{1}{t^2}+4}}{2}\) For \(t>0\), we get \(x=\frac{-1+\sqrt{1+4 t^2}}{2 t}=\frac{2 t}{1+\sqrt{4 t^2+1}}\) and thus, \(y=x^2=\frac{4 t^2}{4 t^2+2+2 \sqrt{4 t^2+1}}\).
Hence, \(f(t)=\frac{4 t^2}{4 t^2+2+2 \sqrt{4 t^2+1}}\) for \(t \geq 0\).

Further, as \(g(x)=x^2\) is an even function from \(\mathbb{R}\) to \(\mathbb{R}\), it can be observed by definition of \(f\) that \(f\) is an even function. Hence, for \(t<0\), we get,
\[
f(t)=f(-t)=\frac{4(-t)^2}{4(-t)^2+2+2 \sqrt{4(-t)^2+1}}=\frac{4 t^2}{4 t^2+2+2 \sqrt{4 t^2+1}}
\]

Thus, we get, \(f(t)=\frac{4 t^2}{4 t^2+2+2 \sqrt{4 t^2+1}}\), for all \(t \in \mathbb{R}\).
        <br>

(a) Since, \(4 t^2< 4 t^2+2+2 \sqrt{4 t^2+1}, \forall t \in \mathbb{R}\), we get, \(0 \leq f(t)< 1, \forall t \in \mathbb{R}\). Hence, \(f\) is bounded.
        <br>
(b) By continuity of polynomials, square-root function and algebra of continuous functions, function \(f\) is a continuous function.
            <br>

(c) \(\lim_{t \rightarrow \infty} f(t)=\lim_{t \rightarrow \infty} \frac{4 t^2}{4 t^2+2+2 \sqrt{4 t^2+1}}=\frac{4}{4}=1\).
                <br>

(d) As \(f(0)=0\), Consider \(\lim_{t \rightarrow 0} \frac{f(t)}{t}=\lim_{t \rightarrow 0} \frac{4 t}{4 t^2+2+2 \sqrt{4 t^2+1}}=0\) and hence, \(f\) is differentiable at 0 and \(f^{\prime}(0)=0\).
                    <br>
<i>Source: MMC 2023.</i>
</details>

---



<p><b>B4.</b>
Prove that function \(f:X\rightarrow Y\) is a bijection if and only if it preserves complements,
that is, if and only if \(f(X\setminus A)=Y\setminus f(A)\) for every subset \(A\) of \(X\). 
</p>

<details><summary>Sol.</summary>
If \(f\) is a bijection and \(B=X\setminus A\), then \(f\) preserves unions and intersections and \(f(X)=Y\),
so \(f(A)\) and \(f(B)\) are disjoint and have union equal to \(Y\).
Conversely, if \(f\) preserves complements, then setting \(A = \emptyset\), we see that \(f(X)=Y\), so \(f\) is a surjection.
And for every \(x\) we also have that \(f(X\setminus {x})=Y\setminus {f(x)}\).
Therefore, if \(x\) and \(y\) are distinct, then so are \(f(x)\) and \(f(y)\).
So \(f\) is an injection as well.
<br><i>Source: https://twitter.com/wtgowers/status/1755183339844079932</i>
</details>



---


<p><b>B5.</b>
Let \(a_1=1\) and \(a_n=n\left(a_{n-1}+1\right)\) for all \(n \geq 2\). Define:

\[ P_n=\left(1+\frac{1}{a_1}\right) \cdots\left(1+\frac{1}{a_n}\right) \]

Compute \(\lim_{n \rightarrow \infty} P_n\).
</p>


<details><summary>Sol.</summary>
<i>Source: From ISI 2005 Bmath.</i><br>

\[ a_2=2\left(a_1+1\right), a_3=3\left(a_2+1\right)=3+3(2)+3(2)(1), a_4=4\left(a_3+1\right)=4+4(3)+4(3)(2)+4(3)(2)(1), \cdots \]

and it is easy to show by induction that

\[
\begin{align*}
a_n & =n+n(n-1)+n(n-1)(n-2)+\cdots+n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1 \\
& =\frac{n !}{(n-1) !}+\frac{n !}{(n-2) !}+\cdots+\frac{n !}{1 !}+\frac{n !}{0!} 
\end{align*}
\]

Then

\[
\begin{align*}
\lim_{n \rightarrow \infty} P_n & =\lim_{n \rightarrow \infty} \prod_{k=1}^n\left(1+\frac{1}{a_k}\right) \\
& =\lim_{n \rightarrow \infty}\left(\frac{a_1+1}{a_1} \cdot \frac{a_2+1}{a_2} \cdots \frac{a_n+1}{a_n}\right) \\
& =\lim_{n \rightarrow \infty}\left(\frac{a_2}{2 a_1} \cdot \frac{a_3}{3 a_2} \cdots \frac{a_{n+1}}{(n+1) a_n}\right) \\
& =\lim_{n \rightarrow \infty} \frac{a_{n+1}}{(n+1) !} \\
& =\lim_{n \rightarrow \infty}\left(1+\frac{1}{1 !}+\frac{1}{2 !}+\cdots+\frac{1}{n !}\right)=e
\end{align*}
\]
</details>


---

<p><b>B6.</b>
Let \(A B C D\) be a quadrilateral such that the sum of a pair of opposite sides equals the sum of other pair of opposite sides \((A B+C D=A D+B C)\). Prove that the circles inscribed in triangles \(A B C\) and \(A C D\) are tangent to each other.
</p>

<details><summary>Sol.</summary>
We refer to the incircles of the triangles \(ABC\) and \(ADC\)
as the first circle and the second circle, respectively. Let the
first circle (resp. second) touch the side \(AC\) at point \(X\) (resp. \(Y\)).
We need to show that points \(X\) and \(Y\) coincide.

Let \(a_1\) and \(a_2\) denote the lengths of the tangents from vertex
\(A\) to the first and second circle respectively i.e \(|AX|=a_1 \) and \(|AY|=a_2\). Similarly,
define \(c_1\) and \(c_2\) as the lengths |CX| and |CY|, respectively.


Let \(b\) be the length of the tangent from vertex \(B\) to the first
circle.  Let \(d\) be the length of the tangent from vertex \(D\) to
the second circle.

From the constraint given in the problem:
\[
\begin{align*}
AB + CD & =  AD + BC \\
a_1 + b + c_2 + d & = a_2 + d + c_1 + b\\
a_1 + c_2 & = a_2 + c_1\\
a_1 + c_1 - |XY| & = a_1 + |XY| + c_1\\
|XY| & = 0 \\
\end{align*}
\]
</details>




