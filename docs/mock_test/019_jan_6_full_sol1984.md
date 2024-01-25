---
layout: default
title: Mock test 1 Full-syllabus test
nav_exclude: true
---


#  Mock test #1 '24: Solutions

#### Timings: 14:00-17:00 Hrs &nbsp;&nbsp;  Date: 6 Jan 2024
{: .fs-3 .text-grey-004 }

---


## Part A: Short-answer type questions

**Submission file:** Write answers to all the ten questions on a single sheet of paper. Email a picture of your answer sheet. Name the file as PartA.jpg or PartA.png.
{: .fs-3 }

**For this part, answers must be written without any explanation.**

<ol>

<li>We have a supply of ice-creams, each of which has two properties: the flavour can be strawberry or vanilla and the cone can be colored brown or green. Half of the ice-creams have a strawberry flavour and the other half have vanilla flavour. Also, \(\frac{4}{9}\) of the strawberry ice-creams have brown cones and \(\frac{2}{3}\) of the vanilla ice-creams have green cones.
What fraction of the green cones are strawberry flavoured?

<ol>
<li>2/3</li>
<li>6/11</li>
<li>5/6</li>
<li>5/11</li>
<li>1/3</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (d).<br>
We denote the values of each property: \(S\) for strawberry, \(V\) for vanilla, \(B\) for brown, and \(G\) for green.
We want to find \(P(S \mid G)\), the probability that an ice-cream is strawberry given that it is square. We have

\begin{align*}
P(S \mid G) & =\frac{P(S, G)}{P(G)} & & \\
& =\frac{P(S, G)}{P(S, G)+P(V, G)} & & \\
& =\frac{P(G \mid S) P(S)}{P(G \mid S) P(S)+P(G \mid V) P(V)} & &  \\
& =\frac{(1-P(B \mid S)) P(S)}{(1-P(B \mid S)) P(S)+P(G \mid V) P(V)} & &  \\
& =\frac{\left(1-\frac{4}{9}\right)\left(\frac{1}{2}\right)}{\left(1-\frac{4}{9}\right)\left(\frac{1}{2}\right)+\left(\frac{2}{3}\right)\left(\frac{1}{2}\right)} & \\
& =\frac{5}{11} 
\end{align*}


<i>Source: SMT 2023</i>.
</details>



<li>
Suppose \(f: \mathbb{R} \rightarrow \mathbb{R}\) is an odd and differentiable function.
Then for every \(x_{0} \in \mathbb{R}, f^{\prime}\left(-x_{0}\right)\) is equal to:
</li>

<ol>
<li>\(f^{\prime}\left(x_{0}\right)\)</li>
<li>\(-f^{\prime}\left(x_{0}\right)\)</li>
<li>0</li>
<li>-1</li>
<li>None of these.</li>
</ol>

<details open><summary>Sol.</summary>
<b>Ans.</b> (a). \(f(x) = -f(-x) \implies f^{\prime}(x) = f^{\prime}(-x)\). <br>
</details>



<li>
We have six hidden numbers \(a_1,a_2,\ldots,a_6\). The are 64 possible subsets of these six numbers. The sum of the elements in each of these 64 subsets is given in the list \(S\) below. 
<p style="text-align:center">
<img src="/assets/images/mt19_subset.png"/>
</p>
What is the value of the sum \(a_1+a_2+a_3+a_4+a_5+a_6\)?

<ol>
<li>-4</li>
<li>-5</li>
<li>-6</li>
<li>-7</li>
</ol>

</li>


<details open><summary>Sol.</summary>
<b>Ans:</b> (b). The positive (resp. negative) numbers in the list \(a_1,\ldots,a_6\) add to the highest (resp. smallest) element in \(S\).
</details>



<li>
Suppose \(p\) be an odd prime. Let \(N\) denote the second smallest multiple of \(p\) that is a perfect cube.
How many positive factors does \(N\) have?<br>


<ol>
<li> 10 </li>
<li> 12 </li>
<li> 16 </li>
<li> 20 </li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (c) <br>
Since \(p\) is an odd prime, the second smallest multiple of \(p\) that is a perfect cube is \(2^3·p^3 = 8p^3\).
The number of positive factors is therefore (3 + 1)(3 + 1).
</details>


<li>
There are \(n\) cards. Alice and Bob play, alternately, the following game. Alice starts the game by removing
one card. In each subsequent move the current player can remove any quantity of cards,
from \(1\) card to \(t+1\) cards, where \(t\) is the number of cards removed by the opponent in the previous move. The winner is the player who removes the last card.
The possible values of \(n\) for which Alice has the winning strategy are:

<ol>
<li> \( n=0\mod 5\) </li>
<li> \( n=1\mod 5\) </li>
<li> \( n=2\mod 5\) </li>
<li> \( n=3\mod 5\) </li>
<li>\( n=4\mod 5\) </li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans</b>. (b) and (e). <br>
Each case can be checked explicitly.
</details>

<li>
Suppose \(a_i\) and \(b_i\) are real numbers such that \(\sum_1^\infty a_i^2\) and \(\sum_1^\infty b_i^2\) converge. Which of these statements is true?

<ol>
<li> The sequence \(\sum_1^\infty |a_i-b_i| \) converges.</li>
<li> The sequence \(\sum_1^\infty |a_i-b_i|^{2} \) converges.</li>
<li> The sequence \(\sum_1^\infty (a_i-b_i)^2 \) converges.</li>
<li> The sequence \(\sum_1^\infty (a_i-b_i)^3 \) converges.</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans</b> (b),(c) and (d).<br>

(a) is not true if \(a_i=1/i\) and \(b_i=0\).<br>

\[ 0 \leq (a_i-b_i)^2 = 2a_i^2 + 2b_i^2-(a_i+b_i)^2 \leq 2a_i^2 + 2b_i^2 \]

(c) and (d): Since \(\sum a_i^2 \) and \(\sum b_i^2\) are absolutely convergent, \(\sum 2a_i^2+2b_i^2 \)
is also convergent.
<br>
For sufficiently large \(i\), \(|a_i-b_i|<1\) so \( |a_i-b_i|^3 \leq |a_i-b_i|^2 \). Since \( (a_i-b_i)^3 \)
is absolutely convergent it is convergent.


<br><i>Why is (b) not true?</i>

<br><b>Proposition.</b> The sum \( \sum_{i=1}^\infty 1/n^p \) converges if \( p > 1\) and diverges when \( 0 \leq p \leq 1\).
<br><i>Proof.</i> See the following article for proofs of both assertions: Cohen and Knight, Convergence and divergence of \( \sum_{i=1}^\infty 1/n^p \) [<a href="https://www.jstor.org/stable/2690283">paper</a>].<br>

<a href="https://math.stackexchange.com/questions/29450/self-contained-proof-that-sum-limits-n-1-infty-frac1np-converges-for">Alternate proof</a> on stack exchange.


<br>

(b) is not true if we we pick \(a_i = 1/i^{0.6} \) and \(b_i=0\) and invoke the above proposition. 
</details>








<li>
If \(a+b+c=0\), then the quadratic equation \(3 a x^{2}+2 b x+c=0\) has \(\\\).

<ol>
<li>at least one root in \((0,1)\).</li>
<li>one root in \((1,2)\) and the other in \((-1,0)\). </li>
<li>both imaginary roots.</li>
<li>a repeated root.</li>
</ol>

</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (a) <br>

\begin{align*}
\mbox{Let }   f’ (x) &= 3ax^2 + 2bx + c \\
f (x) &= ax^3 + bx + cx + d\\
f (0)  &= d\\
f (1)  &= a + b + c + d \\
\end{align*}

Since we are given that \(a + b + c = 0\), \(f (1) = d\) and \(f(0) = f (1)\).
Rolle’s theorem can be applied in the interval \((0, 1)\). \(f'(c) = 0\) for some \(0 < c < 1\).
There will be at least one root of the equation \(3ax^2 + 2bx + c = 0\) in the interval \((0, 1)\).

</details>


<li> Suppose \( S=\{1,2,3,4,5\} \).  Find the number of pairs \( (A,B) \)
that can be formed such that \(A \subseteq S\) and \(B\subset A\).
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> 211.<br>

Consider the pairs where \(A \subseteq S\) and \(B\subseteq A\). Each element in \(S\) has three choices:<br>
(i) It can be in \(B\)<br>
(i) It can be in \(A\setminus B\)<br>
(iii) It can be in \(S\setminus A\)<br>
Hence, there are \(3^5\) such pairs. From this we subtract the number of pairs where \(B=A\). There are \( 2^5 \) of 
these. Hence, the required number is \( 3^5 - 2^5 = 211 \).<br>

<i>Source: Slight variation of an ISI Tomato problem.</i>
</details>




<li>
The number of continuous functions \(f: \mathbb{R} \rightarrow \mathbb{R}\) satisfying \((f(x))^{2}=x f(x)\) is:
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> 4<br>


 \(f(x) = 0\) and \(f(x)=x\) are obvious solutions. If \(f(x) = 0\) for some \(x>0\),
 it implies that \(f\) is always zero in the positive reals. Similarly for negative reals. We get four functions:
<br>
<p>
  <ul>
     <li> \(f = id\)</li>
     <li> \(f = id\) on \(R^+\) and \(f = 0\) on \(R^-\)</li>
     <li> \(f = id\) on \(R^-\) and \(f = 0\) on \(R^+\)</li>
     <li> \(f = 0\)</li>
  </ul>
</p>
<br>
  Here is an another approach. If \(f(x)\) is not 0, then cancelling \(f(x)\) on both sides yields \(f(x) = x\) so if \(f(x) = x\)
 for any \(x > 0\) if \(f(x)\) is 0 anywhere \(> 0\), say at \(y\), wlog \(0< y < x\), then somewhere on \([x,y], g(z) := f(z)-z\) will take values not equal to \(z\) or 0 by IVT
hence on \((0, \inf)\), the function is either identically \(f(x) = x\) or \(f(x) = 0\) similarly for \(x < 0\) and clearly \(f(0) = 0\) in either case
so the 4 possible solutions are made by combining the 2 cases for the positive and negative value solutions in \(2\times2 = 4\) ways, and it's easy to check that all these four
are continuous solutions.<br><br>

</details>

<li>
If \(x\) and \(y\) are positive integers that satisfy \(43 x+47 y=2023\), compute the minimum possible value of \(x+y\).
</li>

<details open><summary>Sol.</summary>
Ans: 45<br>
Taking modulo 43 , one notices that \(47 \equiv 4(\bmod 43)\) and \(2023 \equiv 2(\bmod 43)\). We rewrite \(43 x+47 y \equiv 4 y \equiv 2(\bmod 43)\). The least \(y\) for which this holds is \(y=22\), and computing, \(23 \cdot 43+22 \cdot 47=2023\). It is impossible to have other positive integer pair solutions because all solutions are given by the form \((x, y)=(23+47 k, 22-43 k)\) for integers \(k\). Therefore, the minimal value is \(23+22=45\).
</details>

</ol>


## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---


<p><b>B1.</b> 

There are \(n \ge 3\) positive real numbers \(a_1, a_2, \dots, a_n\). For each \(1 \le i \le n\) we let \(b_i = \frac{a_{i-1} + a_{i+1}}{a_i}\). 
Here we define \(a_0\) to be \(a_n\) and \(a_{n+1}\) to be \(a_1\). 
Assume that for all \(i\) and \(j\) in the range \(1\) to \(n\), 
we have \(a_i \le a_j\) if and only if \(b_i \le b_j\). Prove that \(a_1 = a_2 = \dots = a_n\).
</p>

<details><summary>Sol.</summary>

<i>Solution 1</i>. Let \(m=\min(a_1,\ldots,a_n)\) and \(M=\max(a_1,\ldots,a_n)\).
Assume for the sake of contradiction that \(M>m\).
Then, there must exist an index \(i\) such that \(a_i=m\) and \(\max(a_{i-1},a_{i+1})>m\), giving \(b_i>2\). 
Similarly, there must exist an index \(j\) such that \(a_j=M\) and \(\min(a_{j-1},a_{j+1}) < M\), giving \(b_j < 2\).
This means \(a_i< a_j\) and \(b_i>2>b_j\), a contradiction. Therefore, we have \(M=m\), so \(a_1=\cdots=a_n\).<br>

<i>Source: EGMO '23. Solution due to CyclicISLscelesTrapezoid (AoPS).</i><br>

<i>Solution 2</i>. See Rudolf Emil Kalman's <a href="/assets/images/mock_test_19/Rudolf_Emil_Kalman/B1.jpg">solution</a>.

</details>

---

<p><b>B2</b>. Suppose \(ABC\) is an equilateral triangle with side length 7 cm. We draw the circumcircle of the triangle as shown below.
Find a point \(D\) on the arc \(BC\) such that the distances \(AD,BD\) and \(CD\) are all integers. Write down 
the values of the three distances for your choice of the point \(D\).
</p>

<p style="text-align:center">
<img src="/assets/images/integer_distances.png"/>
</p>

<details><summary>Sol.</summary>
On the circumcircle of the triangle ABC, pick the point D, which is 3 cm from B. 

We need to find the lengths of \(AD\) and \(CD\). Let's find the length of \(AD\)
by using the cosine formula for triangle \(ADB\). We know that \(\angle ADB=60^\circ\) by subtended angles. 

\begin{align*}
7^2 &= AD^2 + 3^2 - 2\cdot AD\cdot 3\cdot \cos 60^\circ\\ 
AD^2 -3 AD - 40 &= 0\\ 
(AD -8)(AD+5)& \Rightarrow AD=8
\end{align*}

 
Let's find the length of \(CD\) by applying the cosine formula to the triangle \(CDB\). Notice that 

\begin{align*}
\angle CDB &= 120^\circ \\
CB^2 &= CD^2 + 3^2 - 2\cdot CD\cdot 3\cdot \cos 120^\circ \\
CD^2 + 3CD - 40 &= 0 \\
(CD+8)(CD-5) \Rightarrow CD &= 5 
\end{align*}

</details>



---


<p><b>B3.</b>
Show that there does not exist a function \(f:(0, \infty) \rightarrow(0, \infty)\) such that \(f^{\prime \prime}(x) \leq 0\) for all \(x\) and \(f^{\prime}\left(x_0\right) < 0\) for some \(x_0\).
</p>

<details><summary>Sol.</summary>
Suppose there exists a function \(f:(0, \infty) \rightarrow(0, \infty)\) such that \(f^{\prime \prime}(x) \leq 0\) for all \(x\) and \(f^{\prime}\left(x_0\right)<0\) for some \(x_0\). Thus \(f^{\prime}\) is a decreasing function. Define \(g(x)=f(x)-f\left(x_0\right)-f^{\prime}\left(x_0\right)\left(x-x_0\right)\).
Note that \(g\left(x_0\right)=0\) and \(g^{\prime}(x)=f^{\prime}(x)-f^{\prime}\left(x_0\right)<0\) for all \(x>x_0\). Since \(g\) is a decreasing function on \(\left(x_0, \infty\right)\), we get \(g(x) \leq 0\) for all \(x>x_0\). Now \(f^{\prime}\left(x_0\right)<0\) implies, there exists \(x_1>x_0\) such that \(f\left(x_1\right)<0\).
</details>

---



<p><b>B4.</b>
Let \(\mathcal{P_n}\) denote the collection of polynomials of degree \(n\) such that the polynomial and all its derivatives have integer roots. <br>

(a) Find a polynomial in \(\mathcal{P_2}\) having at least two distinct roots.<br>
(b) Find a polynomial in \(\mathcal{P_3}\) having at least two distinct roots.<br>
(c) For any polynomial \(P\) in \(\mathcal{P_n}\), show that the arithmetic mean of all roots of \(P\) is also an integer.<br>

Show that there does not exist a function \(f:(0, \infty) \rightarrow(0, \infty)\) such that \(f^{\prime \prime}(x) \leq 0\) for all \(x\) and \(f^{\prime}\left(x_0\right) < 0\) for some \(x_0\).
</p>

<details><summary>Sol.</summary>
i) Let \(f=(x-\alpha)(x-\beta)\); then \(f^{\prime}=(x-\alpha)+(x-\beta)=2 x-(\alpha+\beta)\). Thus the condition is \(\alpha+\beta\) must be even. <br>

ii) Let \(f=(x-\alpha)(x-\beta)(x-\gamma)\)

Then \(f^{\prime}=(x-\alpha)(x-\beta)+(x-\alpha)(x-\gamma)+(x-\beta)(x-\gamma)\)

Let \(f=(x-\alpha)^{2}(x-\gamma)\). Then \(f^{\prime}=(x-\alpha)^{2}+2(x-\alpha)(x-\beta)\)

\begin{align*}
f^{\prime \prime}&=2(x-\alpha)+2(x-\alpha)+2(x-\beta)=4(x-\alpha)+2(x-\beta)\\
&=6 x-4 \alpha-2 \beta\\
f^{\prime \prime}&=0 \mbox{if }x=\frac{4 \alpha+2 \beta}{6}
\end{align*}

So \(6 \mid 4 \alpha+2 \beta\). Put \(\beta=1\) and \(\alpha=4\). We can take \(f(x)=(x-4)^{2}(x-1)\).<br>

iii) Let \(p(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\ldots+a_{1} x+a_{0} \in P_{n}\). Let the roots of \(p(x)\) be \(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{n}\)

Now \(p^{\prime}(x)=n a_{n} x^{n-1}+(n-1) a_{n-1} x^{n-2}+\ldots+a_{1}\).

\(p^{\prime \prime}(x)=n(n-1) a_{n} x^{n-2}+(n-1)(n-2) a_{n-1} x^{n-3}+\ldots+2 a_{2}\) and so on.

\(p^{(n-1)}(x)=n ! a_{n} x+(n-1) ! a_{n-1}\)

Since \(p^{(n-1)}(x)\) has integer roots, it is equal to \(\frac{-(n-1) ! a_{n-1}}{n ! a_{n}}\) \(\frac{\sum_{i=1}^{n} \alpha_{i}}{n}=\frac{-(n-1) a_{n-1}}{n a_{n}}\) is thus an integer.


<br><i>Source: Madhava 2021</i>
</details>



---


<p><b>B5.</b>
There is a \(n\times n\) board in which \( (n-1)^2 \) identical coins are kept as follows. Each cell has a coin, except for the last row and the last column of cells.
The cell in the \(i\)th row and the \(j\)th column is indexed by \( (i,j) \). The initial configuration of the board with \(n=6\) is shown below. The sixth row and the sixth column are empty.
</p>

<p style="text-align:center">
<img src="/assets/images/mt19_board.png"/>
</p>

<p>We can move a coin placed on cell \( (i,j) \) to the cell \( (i+1,j+1) \) if \( 1 \leq i,j \leq n-1 \) and the cells at \( (i,j+1), (i+1,j) \) and \( (i+1,j+1) \) are
empty. How many configurations of the board can we get by a sequence of valid moves? A sequence can have any number of moves, including zero.
</p>

<details><summary>Sol.</summary>
The trick is to look at the path of empty cells. There is a 1-1 correspondence between the paths 
that go from the top left corner to bottom right corner and the coin configurations. The paths are
such that each step either goes right or down. There are \( \binom{2n-2}{n-1} \) such paths. <br>


To see the correspondence, we work backwards. Ending at a given path, if this path is not the initial path,
then it contains at least one sequence of squares of the form \( (i,j)\rightarrow (i,j−1) \rightarrow (i+1,j−1)\).
In this case the square \( (i+1,j) \) must be occupied, so we can undo a move by replacing this sequence with
\( (i,j)\rightarrow (i+1,j) \rightarrow (i+1,j−1) \).
</details>



---

<p><b>B6.</b>
Let \(p,q\) and \(r\) be prime numbers. Let \(S\) be the set of all ordered triples \((p,q,r)\) such 
that \(q^2 - 4pr = a^2\) for some integer \(a\).  <br>

(a) Give an example of a valid triple.<br>

(b) Show that the prime number 3 appears in at most six triples in \( S \).<br>
</p>

<details><summary>Sol.</summary>

(a) \( (2,5,3),(2,7,5),(2,11,5), \) etc.<br>

(b) 

<b>Lemma 1.</b> Either \(p\) or \(r\) is 2.<br>
<i>Proof.</i> Since \(4pr \geq 16\) and \(a^2 \leq 0\), we must have \(q\geq 5\). Since \(q\) is odd \(a\)
must also be odd. \(q^2 \equiv a^2 \equiv 1 (\mod 8) \implies 4pr \equiv 0 (\mod 8) \). \( \;\;\; \square \).<br> 

<b>Lemma 2.</b> If \(r=2\), then \(q \in \{2p+1,p+2\}\).<br>
If \(r=2\), \(8p = (q+a)(q-a)\). Both the factors \( q+a \) and \(q-a\) must be positive (since they have the same sign and add up to a positive number \(2q\)).
Also, both the factors must be even since \(q\) and \(a\) have the same parity. So \( (q\pm a) \in \{2,4,2p,4p\} \). Hence, \( 2q \in \{4p+2,2p+4\} \).

<br><b>Corollary 2.</b> If \(p=2\), then \(q \in \{2r+1,r+2\}\).<br>

The above observations mean that a prime \(x\) occurs at most twice as many times as there are prime numbers in the list
\[ 2x+1, x+2, (x-1)/2, x-2 \]. If \(x=3\), \(x-2\) is not a prime.


<br><i>Source: Putnam 2011, B2.</i> 
</details>



