---
layout: default
title: Home
nav_order: 1
description: "In-depth solutions to all CMI entrance exam questions."
permalink: /
last_modified_date: 2020-04-27T17:54:08+0000

---


# CMI Tomato

This website is for class XI and XII students who wish to pursue B.Sc. at Chennai Mathematical Institute.
{: .fs-5 .fw-300 }

---


#### What's new?
{: .fs-4}

 - CMI 2021 question paper with solutions.

---


## CMI Entrance Exam 2021: Solutions


### Part-A : Multiple-choice questions

**For each question pick all the options that are true. More than one option may be true.**

<p>
<b>A1.</b> Consider the following equations:
\begin{align*}
\log_{2021} a &= 2022 -a \\
2021^b &= 2022-b
\end{align*}

(a) There is a unique \(a\) that satisfies the first equation.<br>
(b) There is a unique \(b\) that satisfies the second equation.<br>
(c) There exists a solution for both the equations such that \(a=b\).<br>
(d) There exists a solution for both the equations such that \(a+b\) is an integer.

</p>


<details><summary>Solution</summary>
(a) True. \(f(a)=\log_{2021} a + a - 2022\) is an increasing function in \(a\). So \(a=2021\) is the only solution.<br>
(b) True. \(g(b)=2021^b + b - 2022\) is an increasing function in \(b\). So \(b=1\) is the only solution.<br>
(c) False. Follows from above.<br>
(d) True. Since, \(2021+1\) is an integer.<br>
</details>




<p>
<b>A2.</b> If \(p\) is a prime number, which of the following are true?<br>

(a) For every prime \(p\), \(p^2-p\) is divisible by 3. <br>
(b) For every prime \(p>3\), exactly \(p-1\) or \(p+1\) is divisible by 6.<br>
(c) For every prime \(p>3\), \(p^2-1\) is divisible by 24.<br>
(d) For every prime \(p>3\), one of \(p+1\),\(p+3\) and \(p+5\) is divisible by 8.
</p>


<details><summary>Solution</summary>
(a) False. \(5^2-5\) is not divisible by 3.<br>
(b) True. Both 3 and 2 must be factors of either \(p-1\) or \(p+1\). Since \(p\) is an odd prime, it is not divisible by 3. So either \(p-1\) or \(p+1\) is divisible by 3. But \(p-1\) and \(p+1\) are both even.<br>
(c) True. \(p\) is either \(4k+1\) or \(4k+3\). So \(p^2-1\) has 8 and 3 as factors.<br>
(d) False. Put \(p=17\). <br>
</details>




<p>
<b>A3.</b> \(ABC\) is a triangle such that \(AB=1\) cm and \(\angle ABC = 20.21^{\circ}\). Let \(N(x)\) denote the number of non-congruent triangles
such that \(BC=x\) cm, where \(x\) is a positive real number.  There exists an \(x\) such that:<br>
(a)  \(N(x)=0\).<br>
(b)  \(N(x)=1\).<br>
(c)  \(N(x)=2\).<br>
(d)  \(N(x)=3\).<br>
</p>


<details><summary>Solution</summary>
(a) True.<br>
(b) True.<br>
(c) True.<br>
(d) False. <br>

<i>Explanation. </i> Consider the line \(l\) that passes through \(A\) at an angle \(20.21^\circ\) to \(AB\). Let the length
of the shortest distance from \(l\) to \(B\) be \(d\). If \(x< d\) there is no solution. If \(x=d\) there is
exactly one solution. If \(1>x>d\), there are two solutions.<br>

</details>



<p>
<b>A4.</b> Suppose \( f(x) = x^3 + ax^2 + bx +c \) with \(a,b,c\) being integers. Let \(p,q,r\) denote the roots of \(f\), possible complex.<br>

(a) If \(f(1)=2021\), then \(f(x)=(x-1)(x^2+sx+t) + 2021\) such that \(s\) and \(t\) are integers.<br>
(b) There exists \(f(x)\) with \(c=2021\) and \(p=2\).<br>
(c) There exists \(f(x)\) with \(r=1/2\).<br>
(d) \(p^2+q^2+r^2\) does not depend of \(c\).<br>

</p>


<details><summary>Solution</summary>
(a) True. Compare the coefficients. \(t-1\) and \(t-s\) must be integers.<br>
(b) False. Odd-Even argument.<br>
(c) False. Implies that \(1+2a+4b+8c=0\) which can't be the case.<br>
(d) True. \(p^2+q^2+r^2=(p+q+r)^2-2(pq+qr+rp)= a^2-2b\).
</details>



<p>
<b>A5.</b> For a complex number \(z\) let \( P(z): \{z^k: k \in \{1,2,3,\ldots\} \} \).<br>

(a) For every natural number \(n\) there exits a \(z\) such that \(P(z)=n\).<br>
(b) There exits a unique \(z\) such that \(P(z)=3\).<br>
(c) If \(|z|\neq 1\) and \(|z|\neq 0\) then \(P(z)\) is an infinite set.<br>
(d) \(P(e^i)\) has infinite elements.<br>
</p>

<details><summary>Solution</summary>
(a) True. Pick \(z=e^{\frac{2\pi i}{n}}\).<br>
(b) False. Both \(\omega\) and \(\omega^2\) work.<br>
(c) True. If \(z=re^{i\theta}\), then every number in \(P\) has a different length.<br>
(d) True. If \(e^{ia}=e^{ib}\) for some powers \(a,b\) with \(a> b\), then \(a=2k\pi+b\) for some natural number \(k\). But this would imply that \(\pi\) is rational.<br>
</details>



<p>
<b>A6.</b> A real number \(r\) is called a stationary point if \(f^\prime(r)=0\) where \(f(x)\) is a degree \(d\) polynomial.<br>

(a) If \(d=2022\), then \(f\) has at least one stationary point.<br>
(b) If \(f\) has 2021 distinct real roots, then there are at least 2020 stationary points.<br>
(c) If \(f\) has 2021 distinct real roots, then there are at most 2020 stationary points.<br>
(d) If \(r\) is a stationary point and \(f^{\prime\prime}(r)=0\), then \( (r,f(r)) \) is neither a local minima nor a local maxima.<br>
</p>

<details><summary>Solution</summary>
(a) True. \(f^\prime\) has odd degree, so there is one real root.<br>
(b) True. If \(r_1 < r_2 \ldots < r_{2021}\) are the roots, then there is a stationary point between \(r_i\) and \(r_{i+1}\).<br>
(c) False. \(f\) can have any  number of stationary points without have a single real root.<br>
(d) False. \(f(x) = x^4\) is a counterexample.<br>
</details>

<p>
<b>A7.</b> \(a,b,c\) are distinct positive constants. Consider the system of equations:

\begin{align*}
ax + by &= \sqrt{2}\\
bx + cy &= \sqrt{3}
\end{align*}

(a) There exist \(a,b,c\) such that such that the system has infinite solutions.<br>
(b) There exist \(a,b,c\) such that such that the system has exactly one solution.<br>
(c) If the system has no solution, it means that \(2b < a+c\).<br>
(d) If \(2b< a+c\), then the system has no solution.<br>
</p>


<details><summary>Solution</summary>
(a) True. Pick \(a=2/3,b=\sqrt{2/3}\) and \(c=1\). Both the equations become equal.<br>
(b) True. Pick \(a=2,b=1\) and \(c=1\).<br>
(c) True. There is no solution if \(b^2-ac=0\) and \(b/c\neq \sqrt{2/3}\). The first condition implies that \(2b\leq a+c\).<br>
(d) False. Pick values given in (b).<br>
</details>




<p><b>A8.</b> Let \(\vec{v}_n\) denote a vector for \(n\in \mathbb{N}\). We define \(\vec{v}_{n+2} = \vec{v}_{n}\times \vec{v}_{n+1}\), where \(\times\) denotes the cross-product. Let \(\mathbb{0}\) denote
the zero vector. \(\vec{v}_{n}\) maybe the zero vector too. Define sets \(S\) and \(T\) as follows:

\[ S = \{ v_n : n\in \mathbb{N} \} \]
\[ U = \{ \frac{\vec{v}_n}{|\vec{v}_n|} : n \in \mathbb{N} \text{ and } \vec{v}_n \neq \mathbb{0} \} \]

(a) There exists \(\vec{v}_1\) and \( \vec{v}_2 \) such that \( |S| =2 \).<br>
(b) There exists \(\vec{v}_1\) and \( \vec{v}_2 \) such that \( |S| =3 \).<br>
(c) There exists \(\vec{v}_1\) and \( \vec{v}_2 \) such that \( |S| =4 \).<br>
(d) If  \(\vec{v}_1\) and \( \vec{v}_2 \) exist such that \( |S| = \infty \), then \(|U|=\infty\).<br>
</p>


<details><summary>Solution</summary>
(a) True. Pick \(\mathbb{1}\) and \(\mathbb{0}\).<br>
(b) True. Pick \(\vec{v_1} = \vec{i}\) and \(\vec{v_2}=\vec{j}\).<br>
(c) False. They would have to be unit vectors. Additionally, \(\vec{v_1},\vec{v_2},\vec{v_3}\) and  \(\vec{v_2},\vec{v_3},\vec{v_4}\) both must be mutually orthogonal. But this implies that \(\vec{v_3}=\vec{v_1}\).<br>
(d) False. Pick \(\vec{v_1} = 2\vec{i}\) and \(\vec{v_2}=3\vec{j}\). \(|S|=\infty\) but \(|U|=3\).<br>
</details>




<p><b>A9.</b> Let \(f\) and \(g\) be function defined as follows:<br>

\[ f(x) = \frac{x}{x+\sin x} \]

\[ g(x) = \frac{x^4+x^6}{e^x-1-x^2} \]

(a) \(\lim_{x\rightarrow 0} f(x) = 1/2\)<br>
(b) \(\lim_{x\rightarrow \infty} f(x)\) does not exist.<br>
(c) \(\lim_{x\rightarrow \infty} g(x) \) is finite.<br>
(d) \(\lim_{x\rightarrow 0} g(x) = 720 \).<br>

</p>

<details><summary>Solution</summary>
(a) True. \(\sin x \approx x\) as \(x\rightarrow 0\).<br>
(b) False. The limit is 1.<br>
(c) True. Numerator is polynomial, while the denominator is exponential.<br>
(d) False. The limit is zero. (L'Hosptial's rule is not applicable).
</details>



<p><b>A10.</b> Let \(f(x) = \arctan(x) \) and \(g(v) = \int_0^{v} f(x) dx \) for \(v>0\).<br>


(a) \(f(1)=\pi/4\)<br>
(b) \(f(1)+f(2)+f(3)=\pi\) <br>
(c) \(g(v)\) is an increasing function.<br>
(d) \(g(v)\) is an odd function.<br>
</p>


<details><summary>Solution</summary>

<p>
(a) True.<br>
(b) True. <br>

Let \( \arctan(1)=x ; \arctan (2)=y ;\) and \(\arctan (3)=z\).<br>

\[\tan (x+y)=\frac{\tan x+\tan y}{1-\tan x \cdot \tan y}=\frac{1+2}{1-2}=-3\]

Put \(u = x+y\) and evaluate:
\[\tan (z+u)=\frac{\tan z+\tan u}{1-\tan z \cdot \tan u}=\frac{-3+3}{1-9}=0\]

So \( tan( x+y+z ) = 0\).  Hence, \(\arctan (1)+\arctan (2)+\arctan (3)=x+y+z=\pi\).

<br>
(c) True. Since \(g^\prime(v)=\arctan(v) > 0\) for \(v> 0\).<br>
(d) Not sure since \(g\) is not defined for \(v < 0\).<br>

</p>

</details>





### Part-B: Subjective questions


---

<p>
<b>B1. (a)</b> \(f\) is a function defined on the domain \(S\) and codomain \(T\) and \(g\) is a function defined on the domain \(T\) and codomain \(U\).
Fill in the blanks with with one of the four options.<br>

If \(g\circ f\) is one-one then, \(f\) is \(\underline{.......}\)  and \(g\) is \(\underline{......}\).<br>
If \(g\circ f\) is onto then, \(f\) is \(\underline{.......}\)  and \(g\) is \(\underline{......}\).<br>

<br>
Options:<br>

A: One-one and onto.<br>
B: One-one but need not to be onto.<br>
C: Onto but need not to be one-one.<br>
D: Need not to be one-one and need not be onto.<br>


<br>

<details><summary>Answer</summary>
B-D-D-C.
</details>
<br>



<b>B1. (b)</b> \(ABCD\) is a square. Point \(X\) lies on a circle with \(AY\) as the diameter. Points \(X\) and \(Y\) lie on the sides of the
square such that \(AX=4\) cm and \(AY=5\) cm. What is the area of the square \(ABCD\)?<br>

<p style="text-align:center">
<img src="/assets/images/cmi_2021_square.png"/>
</p>

</p>

<details><summary>Solution</summary>
\begin{align*}
\angle DAX &= \angle CXY\\
\implies \Delta DAX &\sim \Delta CXY \\
\frac{XY}{AX} &= \frac{XC}{AD} \\
\frac{3}{4} &= \frac{XC}{AD} \\
XC &= \frac{3}{4} AD \\
DX &= CD-CX = \frac{1}{4}AD\\
AD^2+DX^2 &= 4^2\\
AD^2+\frac{AD^2}{16} &= 16\\
AD &= \frac{16}{\sqrt{17}}\\
\text{Area of the square} &= \frac{256}{17}
\end{align*}


<i>Problem source: <a href=" https://www.youtube.com/watch?v=aQsb5jfqSYo">Presh Talwalkar's channel</a>.</i>

</details>


---
<p>
<b>B2 (a).</b> A mother and two daughters have a fair coin and play a game as follows. First, the mother tosses the coin.<br>

<i>Case I:</i> If the coin lands heads, then both the daughters win.<br>
<i>Case II:</i> If the coin lands tails, then each daughter rolls a fair die independently. The first daughter wins if her die comes up 5 or 6. The second
daughter wins if her die comes up 5 or 6. <br>

A game is played.<br>

<ol>
<li> What is the probability that the second daughter has lost given that the first daughter has lost?</li>
<li> What is the probability that the second daughter won given that the first daugher has won?</li>
</ol>

</p>

<details><summary>Solution</summary>

<ol>
<li>Since the outcome of the toss was tails, the second daugther lost since the die came up 1,2,3 or 4. Hence, required probability is 2/3.</li>

<li>
Let \(A\) the event that the second daughter won and \(B\) be the event that the first daughter won.<br>

\[ P(A \mid B)=\frac{P(A \cap B)}{P(B)} \]


\begin{align*}
P(A \cap B)&=P(A \cap B \mid H) P(H)+P(A \cap B \mid T) P(T) \\
&=1\cdot \frac{1}{2} + \frac{1}{9}\cdot \frac{1}{2} \\
&=\frac{5}{9}
\end{align*}

\begin{align*}
P(B)&=P(B \mid H) P(H)+P(B \mid T) P(T) \\
&=1\cdot \frac{1}{2} + \frac{1}{3}\cdot \frac{1}{2} \\
&=\frac{2}{3}
\end{align*}

\[ P(A \mid B)=\frac{P(A \cap B)}{P(B)} = \frac{5/9}{2/3} = \frac{5}{6} \]

</li>
</ol>

</details>



<p>
<b>B2 (b)</b> Prove or disprove:<br>
(i) \( 2^{40} > 20! \)<br>
(ii) \( 1-1/x \leq \ln x \leq x-1 \) for all \(x>0\)<br>
</p>

<details><summary>Solution</summary>

(i) False.<br>

\begin{align*}
20! &> 2\times3\times4\times5\times6\times 7\times 8\times8\times 8\ldots (\text{13 times}) \\
20! &> 2\times3\times4\times5\times6\times 7\times (2^{3})^{13} \\
20! &> 2^{40}
\end{align*}

<br><i>Comment:</i> A similar problem was asked in <a href="/docs/mock_test/006_apr_1_full/">mock test #6</a> (Problem B2).<br><br>


(ii) True.<br>

Let us prove the left hand side inequality.

\begin{align*}
f(x) &:= \ln x - 1 + 1/x\\
f^\prime(x) &= 1/x(1 - 1/x)\\
\end{align*}

\(f^\prime < 0 \)  for \(x\in(0,1)\) and \(>0\) for \(x\in(1,\infty)\). This means
\(f\) is decreasing in the interval \( (0,1)\) and increasing in the interval \( (1,\infty) \). It reaches the minimum at \(x=1\) which is zero.
Hence \(f(x)\geq 0\) for all \(x > 0\).<br>


The right hand side inequality can be proved similarly.

\begin{align*}
g(x) &:= x - 1 - \ln x\\
g^\prime(x) &= 1 - 1/x
\end{align*}

Again, \( g(x) \) attains its minima of zero at \(x=1\).



</details>




---

<p>
<b>B3.</b> You have to form a 7 letter password using 10 digits and 26 letters. Only lower case letters as allowed. For example, 01x01xb, 11bcaa0, etc. are valid passwords.
<ol>
<li>How many passwords can you make with 26 letters and 10 digits?</li>
<li>How many passwords have atleast one alphabet and atleast one digit?</li>
<li>How many passwords are there with at least one consonant and atleast one vowel and atleast one digit? Note that there are 5 vowels and 21 consonants.</li>
<li>Suppose there are 12 additional special characters. How many passwords are there with atleast one vowel, one consonant, one digit and one special character?</li>
</ol>

<!--
<br><i>Reference: <a href="https://math.stackexchange.com/questions/739874/how-many-possible-combinations-in-8-character-password">Math Stack Exchange.</a></i>
-->


</p>


<details><summary>Solution</summary>
<ol>
<li> \(36^{7}\).</li>
<li> \(36^{7} - 26^7 - 10^7 \).</li>

<li> Let \(V=5,C=21,D=10\) and \(S=12\). <br>
<i>Notation.</i> Let \(P(x_1,\ldots,x_k)\) denote the number \( (x_1+x_2+\ldots+x_k)^7 \) where \( x_i \in \{V,C,D,S\} \).<br>

By principle of inclusion/exclusion the answer is:

\[ P(VCD) - \{P(VC)+P(VD)+P(CD)\} + P(V) + P(C) + P(D) \]
</li>

<li>
\begin{align*}
 P(VCDS) &- \{ P(VCD) + P(CDS) + P(VCS) + P(VDS)  \} \\
         &+\{ P(VC)+P(VD)+P(VS)+P(CD)+P(CS)+P(DS)\}\\
         &- \{ P(V) + P(C) + P(D) + P(S) \}
\end{align*}


</li>

</ol>

</details>




---


<p>
<b>B4.</b> Show that there is no polynomial \(p(x)\) such that \(\cos \theta = p(\sin \theta)\) for every \(\theta\).

<details><summary>Solution</summary>
Put \( \theta = 0 \) and \(\theta = \pi\). Then \(p(0) = 1 \) and \(p(0)=-1\) which cannot be the case.
</details>
</p>



---

<p>
<b>B5.</b> Function \(f(x)\) is defined as \(f(0)=0\) and for \(x> 0\) as
\[ f(x) = \lim_{L\rightarrow \infty} \int_{1/x}^{L} \frac{1}{t^2} \cos(t) dt \]

<ol>
<li>Show that \(f(x)\) is well-defined.</li>
<li>Find \(f'(1/\pi)\). Clearly state what result you are using.</li>
<li>Find \( \lim_{h\rightarrow 0^+} \frac{f(h)-f(0)}{h} \). </li>
</ol>

</p>


<details><summary>Solution</summary>
<ol>
<li>

We split the function into three parts:

\(A\) is the interval before the first time the function touches zero. \(B\) is the part  of the
function that is positive for \(x>\pi/2\) and \(C\) is the part of the function that is negative. We show that
each of these intergrals converge.


<p style="text-align:center">
<img src="/assets/images/cmi_2021_damp.png"/>
</p>

\begin{align*}
A:&\int_{1/x}^{\pi/2} \frac{\cos t}{t^2} dt\\
B:& \sum_{k=0}^{n} \int_{(2k+1)\pi/2}^{(2k+3)\pi/2} \frac{\cos t}{t^2} dt\\
C:& \sum_{k=0}^{n} \int_{(2k+3)\pi/2}^{(2k+5)\pi/2} \frac{\cos t}{t^2} dt\\
\end{align*}

\(A\) is a proper integral and hence well-defined for a given \(x\). \(B\) and \(C\) are dominated by
the integrals \( \int_{\pi/2}^{\infty} \frac{1}{t^2}\) and \( -\int_{\pi/2}^{\infty} \frac{1}{t^2} dt \),
respectively and hence they converge.
</li>

<li> \( \displaystyle f^\prime(1/\pi) = -\pi^2\cos(1/\pi) \) using Leibniz rule.</li>

<li> \(  f^\prime(h) = -\frac{1}{h^2}\;\; \text{ as } h\rightarrow 0^+ \).</li>

</ol>

</details>


---

<p>
<b>B6.</b>  You and your friend are playing a game where there are 2 stacks of cards:<br>

Stack A has \(n\) cards and each card has a number from the set \( \{1,2,...,m\} \).<br>
Stack B has \(m\) cards and each card has a number from the set \( \{1,2,...,n\} \).<br>

You start with \(t_0=0\) and note down the following sequence \(t_1,t_2,t_3,\ldots\). The game proceeds in steps as follows:<br>

If \(t_j \leq 0\), pick out the topmost card from stack A and set \[t_{j+1}=t_j + \text{number on the topmost card drawn from Stack A}\]

If \(t_j> 0\), pick out the topmost card from stack B and set \[t_{j+1}=t_j - \text{number on the topmost card drawn from stack B}\]

The game ends when a player has to draw a card from an empty stack. <br>

Prove that<br>
<ol>
<li> \(1-n \leq t_j \leq m \) for all \(j\)</li>
<li>There exists distinct indices \(i\) and \(j\) such that \(t_i=t_j\)</li>
<li>Prove that there exists a non empty subset in stack A and another in B such that the sum of the numbers on those cards are equal.</li>
</ol>
</p>


<details><summary>Solution</summary>
<ol>
<li>If \(t_j\leq 0\), a card from A is removed. The maximum value of a card in A is
\(m\) so \(t_j\) can at most be \(m\). Similarly, a card from B is subtracted
when the value of \(t_j \geq 1\). Hence, the smallest value it can take is \(1-n\).</li>

<li> From (1) we see that the \(t\)-sequence can take at most \(n\) distinct
non-positive values and at most \(m\) distinct positive values.  We consider two ways in which the game can end:<br><br>

<i>Case 1: Cards in stack B are empty.</i><br>
Suppose the game ended after using up \(m\) cards from B and \(p\leq n\) cards from A.
Since the game has ended the value of \(t_{m+p}\) must be positive.  In addition, the value of \(t\) before
every card in B was added must have been positive (by the game's rule).
So the sequence \(t_1,t_2,t_3,\ldots,t_{m+p}\) contains \(m+1\) positive numbers. But since the sequence
contains \(m\) distinct positive numbers, two \(t\)s must have the same value by pigeon-hole principle.

<br><br>
<i>Case 2:  Cards in stack A are empty. </i><br>
We use a similar argument. Suppose the game ended after using up \(n\) cards from A and \(p\leq n\) cards from B.
Since the game has ended the value of \(t_{n+p}\) must be non-positive.
In addition, the value of \(t\) before every card in A was added must have been non-positive.
So the sequence \(t_0,t_1,t_2,t_3,\ldots,t_{m+p}\) contains \(n+1\) non-positive numbers.
But since the sequence contains \(n\) distinct non-positive numbers, two \(t\)s must have the same value by pigeon-hole principle.

</li>
<li>From (2), some \(t_i=t_j\). The sequence of cards added between \(t_i\) and \(t_j\) sums to zero. So some proper subset
of \(A\) and \(B\) have equal sums.</li>
</ol>
</details>





---

<!--

#### What you get on this site
{: .fs-4}

- In-depth solutions to previous CMI entrance exam questions. This includes questions from 2010 and 2011 for which official solutions are not given.

- Topic-wise classification of all problems ordered by increasing difficulty. This helps you to specialize in a topic.

- Mock tests
{: .fs-4 .fw-300 }



-->

<div id="palette1">
<h2>Browse previous years' problems</h2>

<br>

  <div class="palette">
      <div class="palette-keys">


<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#an-easy-problem';" onmouseover = "display('A1_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#parity-of-a-polynomial';" onmouseover = "display('A2_2010')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#vanilla-application-of-lhospital';" onmouseover = "display('A3_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#progression-of-squares';" onmouseover = "display('A4_2010')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#fermats-little-theorem';" onmouseover = "display('A5_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#easy-induction';" onmouseover = "display('A6_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#symmetric-log-reciprocals';" onmouseover = "display('A7_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#pigeon-hole-principle';" onmouseover = "display('A8_2010')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#repeated-roots';" onmouseover = "display('A9_2010')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#trignometric-triangle-inequality';" onmouseover = "display('A10_2010')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#rationality-preserving-operations';" onmouseover = "display('A11_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#rhombus-within-a-triangle';" onmouseover = "display('A12_2010')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#power-of-a-complex-number';" onmouseover = "display('A13_2010')"></button>
<button class="button white"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#pigeon-hole-principle';" onmouseover = "display('B1_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#midpoint-of-a-median';" onmouseover = "display('B2_2010')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#just-count';" onmouseover = "display('B3_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#rational-triangle';" onmouseover = "display('B4_2010')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#a-perplexing-integral';" onmouseover = "display('B5_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#intersecting-circles';" onmouseover = "display('B6_2010')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#line-passing-through-an-ap';" onmouseover = "display('B7_2010')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#letter-arrangement';" onmouseover = "display('A1_2011')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#a-chord-within-a-rectangle';" onmouseover = "display('A2_2011')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#intersection-of-a-line-and-periodic-function-ii';" onmouseover = "display('A3_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#am-gm-inequality';" onmouseover = "display('A4_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#differentiable-piece-function';" onmouseover = "display('A5_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#roots-of-a-quadratic';" onmouseover = "display('A6_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#01-polynomial';" onmouseover = "display('A7_2011')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#handshake-party';" onmouseover = "display('B1_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#largest-coefficient';" onmouseover = "display('B2_2011')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#six-consecutive-numbers';" onmouseover = "display('B3_2011')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#serendipitous-sum';" onmouseover = "display('B4_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#degree-constraint-on-the-polynomial';" onmouseover = "display('B5_2011')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#impossible-solid';" onmouseover = "display('B6_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#volume-of-a-cave';" onmouseover = "display('B7_2011')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#only-one-real-root';" onmouseover = "display('B8_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-ii';" onmouseover = "display('B9_2011')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#two-variables-one-equation';" onmouseover = "display('B10_2011')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#surjective-if-and-only-if-injective';" onmouseover = "display('B11_2011')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#an-old-russian-problem';" onmouseover = "display('B12_2011')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#intersection-of-a-line-and-periodic-function-i';" onmouseover = "display('A1_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-i';" onmouseover = "display('A2_2012')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#irrational-fraction';" onmouseover = "display('A3_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#lhospital-again';" onmouseover = "display('A4_2012')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#tinkus-chocolate';" onmouseover = "display('A5_2012')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-a-rational-polynomial-with-a-given-a-root';" onmouseover = "display('B1_2012')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#midpoints-of-a-quadrilateral';" onmouseover = "display('B2_2012')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#intersection-family';" onmouseover = "display('B3_2012')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#riemann-sum';" onmouseover = "display('B4_2012')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#trigonometric-values-via-complex-numbers';" onmouseover = "display('B5_2012')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#matching-pairs-of-points';" onmouseover = "display('B6_2012')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#pigeon-hole-on-pairs';" onmouseover = "display('B7_2012')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomial-that-gives-only-prime-powers';" onmouseover = "display('B8_2012')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#function-composition';" onmouseover = "display('B9_2012')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#one-to-one-i';" onmouseover = "display('A1_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#continuity';" onmouseover = "display('A2_2013')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#circumcenter-and-orthocenter';" onmouseover = "display('A3_2013')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#sum-of-squares-polynomial';" onmouseover = "display('A4_2013')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#seating-boys-and-girls';" onmouseover = "display('A5_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#vanilla-integrals';" onmouseover = "display('A6_2013')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#complex-triangle';" onmouseover = "display('A7_2013')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#sampling-a-quadratic';" onmouseover = "display('A8_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#rolles-theorem-iii';" onmouseover = "display('A9_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#asymptotes-of-a-function';" onmouseover = "display('A10_2013')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#isoceles-triangle';" onmouseover = "display('B1_2013')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#find-a-curve-given-the-tangent';" onmouseover = "display('B2_2013')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#prime-factorization-and-perfect-squares-again';" onmouseover = "display('B3_2013')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomials-that-exponentiate';" onmouseover = "display('B4_2013')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#span-of-the-a-function';" onmouseover = "display('B5_2013')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#difference-equations-iii';" onmouseover = "display('B6_2013')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#summations';" onmouseover = "display('A1_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#convergence-of-etextquadratic';" onmouseover = "display('A2_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#differentiability-i';" onmouseover = "display('A3_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#tangent-to-a-cubic';" onmouseover = "display('A4_2014')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#vertex-in-a-polygon';" onmouseover = "display('A5_2014')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#prime-factorization-and-divisibility';" onmouseover = "display('A6_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#application-of-rolle's-theorem';" onmouseover = "display('A7_2014')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-the-remainders';" onmouseover = "display('A8_2014')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#maximum-and-minimum-of-an-average';" onmouseover = "display('A9_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#triangle-construction';" onmouseover = "display('A10_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#cyclic-polygon';" onmouseover = "display('A11_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#longest-diagonal-in-a-box';" onmouseover = "display('A12_2014')"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#mix-a-sin-and-a-circle';" onmouseover = "display('B1_2014')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/irrationality/#a-polynomial-integer';" onmouseover = "display('B2_2014')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-number-of-functions';" onmouseover = "display('B3_2014')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#differentiability-challenge';" onmouseover = "display('B4_2014')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#difference-equations';" onmouseover = "display('B5_2014')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#quadrilateral-with-circles';" onmouseover = "display('B6_2014')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#charity';" onmouseover = "display('A1_2015')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#ordered-binary-strings';" onmouseover = "display('A2_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#magic-number';" onmouseover = "display('A3_2015')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#double-derivatives';" onmouseover = "display('A4_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#polynomial-with-positive-coefficients';" onmouseover = "display('A5_2015')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#circles-with-pythagoras';" onmouseover = "display('A6_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#coefficient-ratio';" onmouseover = "display('A7_2015')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#number-plates';" onmouseover = "display('A8_2015')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#a-saw-tooth-function';" onmouseover = "display('A9_2015')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#roots-of-unity-i';" onmouseover = "display('A10_2015')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#conditional-probability';" onmouseover = "display('A11_2015')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#polynomial-and-limits';" onmouseover = "display('B1_2015')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/binomial/#points-on-a-sphere';" onmouseover = "display('B2_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#when-is-a2-a-divisible-by-10000';" onmouseover = "display('B3_2015')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#slowing-slope-changing-function';" onmouseover = "display('B4_2015')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#euclidean-algorithm';" onmouseover = "display('B5_2015')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#straight-edge-with-circle';" onmouseover = "display('B6_2015')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#logical-puzzle';" onmouseover = "display('A1_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#gdp-vs-per-capita-gdp';" onmouseover = "display('A2_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#totient-function';" onmouseover = "display('A3_2016')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-steps';" onmouseover = "display('A4_2016')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#use-of-telescoping';" onmouseover = "display('A5_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#irrationality-and-continuity';" onmouseover = "display('A6_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#gcd-application';" onmouseover = "display('A7_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#integer-valued-polynomials';" onmouseover = "display('A8_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#continuity-on-tangents-and-secants';" onmouseover = "display('A9_2016')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#triangle-with-segments';" onmouseover = "display('A10_2016')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button probability" onclick="location.href='/docs/probability/#test-preparation';" onmouseover = "display('B1_2016')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#circle-touching-a-parabola';" onmouseover = "display('B2_2016')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#definite-integral';" onmouseover = "display('B3_2016')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#pairwise-sums-of-a-set';" onmouseover = "display('B4_2016')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#given-the-remainders-find-the-polynomials';" onmouseover = "display('B5_2016')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#primes-in-an-algebraic-equation-';" onmouseover = "display('B6_2016')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#circle-inside-a-triangle-inside-a-circle';" onmouseover = "display('A1_2017')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#distribute-oranges-in-boxes';" onmouseover = "display('A2_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#sweep-volume';" onmouseover = "display('A3_2017')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#sample-a-divisor';" onmouseover = "display('A4_2017')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#roots-of-a-quartic-polynomial';" onmouseover = "display('A5_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#inflection-point';" onmouseover = "display('A6_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#absolute-integrals';" onmouseover = "display('A7_2017')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solutions-to-simultaneous-equations';" onmouseover = "display('A8_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#smallest-prime-factor-function';" onmouseover = "display('A9_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#continuity-of-two-functions';" onmouseover = "display('A10_2017')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#roots-of-unity-to-rescue';" onmouseover = "display('B1_2017')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#intersecting-planes';" onmouseover = "display('B2_2017')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#strange-question';" onmouseover = "display('B3_2017')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#perfect-square-in-a-sequence';" onmouseover = "display('B4_2017')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#coloring-integers';" onmouseover = "display('B5_2017')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#square-inside-a-hexagon';" onmouseover = "display('B6_2017')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#progression-of-circles';" onmouseover = "display('A1_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#integers-in-a-function-range';" onmouseover = "display('A2_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solving-a-cubic-root-equation';" onmouseover = "display('A3_2018')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#a-routine-substitution';" onmouseover = "display('A4_2018')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#difference-of-squares';" onmouseover = "display('A5_2018')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#counting-roots-in-a-quadrant';" onmouseover = "display('A6_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#find-the-possible-coefficients-given-the-roots';" onmouseover = "display('A7_2018')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#non-congruent-triangles-with-fixed-perimeter';" onmouseover = "display('A8_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#recursive-polynomial';" onmouseover = "display('A9_2018')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#repeated-saw-tooth';" onmouseover = "display('A10_2018')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#smart-induction';" onmouseover = "display('B1_2018')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/solvability/#solve-pxqx--1';" onmouseover = "display('B2_2018')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#function-on-integers';" onmouseover = "display('B3_2018')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/triangles/#segments-inside-a-triangle';" onmouseover = "display('B4_2018')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#combinations-with-gaps';" onmouseover = "display('B5_2018')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/gcd/#carrom-board-math';" onmouseover = "display('B6_2018')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#number-of-divisors';" onmouseover = "display('A1_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#a-simple-substitution';" onmouseover = "display('A2_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#maximize-area-of-a-rectangle';" onmouseover = "display('A3_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#sum-of-a-finite-series';" onmouseover = "display('A4_2019')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#squares-on-a-chessboard';" onmouseover = "display('A5_2019')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#is-a-square';" onmouseover = "display('A6_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#broken-calculator';" onmouseover = "display('A7_2019')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#first-ascent';" onmouseover = "display('A8_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#limit-of-a-log-of-an-exponent';" onmouseover = "display('A9_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#continuity-based-on-integral-conditions';" onmouseover = "display('A10_2019')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#count-the-number-of-functions-ii';" onmouseover = "display('B1_2019')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#counting-the-roots-outside-a-disk';" onmouseover = "display('B2_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#routine-definite-integral-in-disguise';" onmouseover = "display('B3_2019')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#interior-point-in-a-parallelogram';" onmouseover = "display('B4_2019')"></button>
<button class="button trigonometry" onclick="location.href='/docs/trigonometry/#geometric-interpretation-of-algebraic-expressions';" onmouseover = "display('B5_2019')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#leibniz-rule';" onmouseover = "display('B6_2019')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#counting-students';" onmouseover = "display('A1_2020')"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/coordinate_system/#vector-perpendicular-to-a-plane';" onmouseover = "display('A2_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/integrals/#absolute-integrals-ii';" onmouseover = "display('A3_2020')"></button>
<button class="button probability" onclick="location.href='/docs/probability/#yet-another-dice-roll';" onmouseover = "display('A4_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#asymptotes';" onmouseover = "display('A5_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#concave-function';" onmouseover = "display('A6_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#guess-the-polynomial';" onmouseover = "display('A7_2020')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/prime_factorization/#number-of-divisors-ii';" onmouseover = "display('A8_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#binomial-polynomial';" onmouseover = "display('A9_2020')"></button>
<button class="button numbers" onclick="location.href='/docs/number_theory/modulo_arithmetic/#chinese-remainder-theorem';" onmouseover = "display('A10_2020')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button white"></button>
<button class="button geometry" onclick="location.href='/docs/geometry/circles/#cyclic-trapezoids';" onmouseover = "display('B1_2020')"></button>
<button class="button complex" onclick="location.href='/docs/complex_numbers/#complex-polygon';" onmouseover = "display('B2_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/derivatives/#spider-walk';" onmouseover = "display('B3_2020')"></button>
<button class="button calculus" onclick="location.href='/docs/calculus/limits/#constrained-function';" onmouseover = "display('B4_2020')"></button>
<button class="button algebra" onclick="location.href='/docs/algebra/polynomials/#dependent-roots';" onmouseover = "display('B5_2020')"></button>
<button class="button combinatorics" onclick="location.href='/docs/combinatorics/#counting-relations';" onmouseover = "display('B6_2020')"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>
<button class="button blank"></button>


      </div>
  </div>

<p>


    <div style="min-height:250px" id="thetext">

<i>Hover on the cell to see the problem. Click on it to navigate to the solution.</i><br>

<button class="button algebra"></button> Algebra <br>
<button class="button geometry"></button> Geometry <br>
<button class="button numbers"></button> Number theory <br>
<button class="button calculus"></button> Calculus<br>
<button class="button combinatorics"></button> Combinatorics <br>
<button class="button probability"></button> Probability <br>
<button class="button complex"></button> Complex numbers <br>
<button class="button trigonometry"></button> Trigonometry<br>

    </div>
</p>

</div>


<hr>





## CMI entrance exam cutoff

The cutoff has been around 35% for the objective section and 40-50% overall. The objective section is used for screening.<br>

CMI does not publish the cutoff marks but they have responded to individual requests in the past.
The scores shown below were shared by former students who were privy to this data.
<br>

<!--
[Subhayan Saha](https://www.quora.com/profile/Subhayan-Saha)
-->


The cutoff marks for the year 2020 are given below. The marks are out of 94 instead of 100 since one question had a mistake.

Type | General |  Reserved
-----|------|----
With scholarship| 54/94 | 44/94
Without scholarship| 48/94 | 40/94
Waiting list| 45/94 | 38/94


The cutoff marks for the previous years are given below.




| Year | Objective | Overall | Vetted by
|---|--|--|
2016 | 14/40 | 62/124 | Sayantani Bhattacharya [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/Why-there-is-no-interview-for-cmi-bsc-this-year)
2017 | 15/40 | 60/125 | Abhiroop Sanyal
2018 | 15/40 | 50/125 |  -
2019 | 20/40 | 52/100  | Ankush Agarwal
2020 | 20/40 | 48/94  | CMI Office




## Preparation tips and interview experiences (pre-2016)


<!--
http://services.artofproblemsolving.com/download.php?id=YXR0YWNobWVudHMvMS8yLzgwZWIwOGVmNzE5YjU1ZjRkMjE5MzI4NTgwMDRmNjZmNTVmYzdlLnBkZg==&rn=TXkgaW50ZXJ2aWV3IGV4cGVyaWVuY2UucGRm
-->

- _2015 Interview experience_ by Sanjay M who posted this on AoPS. [[pdf]](/assets/images/sanjay_interview.pdf)
- _Why I joined CMI_  by Vipul Naik who joined CMI despite getting JEE AIR-154. [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://vipulnaik.com/undergraduate-institution-selection/)
- _How to prepare for CMI_ by Sai Krishna who joined CMI in 2013. [[pdf]](https://www.cmi.ac.in/~saikrishnac/files/how-to-prepare-for-cmi.pdf)
- _CMI entrance exam preparation experience_  by Ankita Sarkar who joined CMI in 2015. [<i style="font-size:14px" class="fa">&#xf08e;</i>](https://www.quora.com/How-did-Ankita-Sarkar-prepare-for-CMI-Entrance-exam-What-books-did-she-use)


Starting from 2016, admissions are based only on the written test and there is no interview.

---

<img src="/assets/images/manjul_bhargava.png" style="float:left;margin-right:20px;width=50px"/>

<q>When universities in the United States are looking to recruit mathematics students
from India, one of the first places they look for applications is from CMI, if not the first place. Universities that are able to get CMI students are always very proud.</q>
{: .fs-4 .fw-300 }





Manjul Bhargava
{: .fs-4 .fw-300 }

[Source](https://www.youtube.com/watch?v=FsdZLme1fj0&t=2870s)
{: .fs-1 .fw-400  }

---


## Admission rate

Acceptance offers are sent to around 90 candidates and about half of them enroll. This is the reason why the number varies from year to year. Approximate numbers are given below.

| Year | # Test-takers | # Offers | # Students enrolled
|-----|----|--|
2015 | 4000 | 70 | 40
2016 | 4000 | 90 | 44
2017 | 4000 | 90 | 45
2018 | 5000 | 95 | 48
2019 | 5500 | 100 | 61

---


## All-in-one book
<br>

<img src="/assets/images/cmi_tomato_cover.jpg" style="float:left;margin-right:20px;margin-top:0px;border-radius:1%"/>

The content of this website is available as an e-book in PDF format. You will have a permanent copy of the solutions which may be handy just in case the site
goes down.
{: .fs-4 .fw-300 }


<a href="https://gum.co/kBekW">Buy the book on Gumroad</a>


<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>




<!--
https://promys-india.org/resources/reading-list/
-->

---



#### About the author

This website is maintained by  Balasundar M, a teacher who has more than 15 years of experience in the industry and academia. He enjoys solving
olympiad-type problems over coffee.
{: .fs-3 .fw-300 }

If you have a more elegant solution to any problem than the one presented, feel free to email him at <code>mbalasundar08</code> [at] <code>gmail.com.</code>
{: .fs-3 .fw-300 }

---

#### Legal information

The contents of this website are hosted in accordance with principles of [fair use](https://www.copyright.gov/fls/fl102.html).
You agree to email me about any possible infringement of copyright law before taking legal action.
{: .fs-3 .fw-300 }

<!--
M. Balasundar is a participant in the Amazon Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to amazon.in.
{: .fs-3 .fw-300 }
-->




