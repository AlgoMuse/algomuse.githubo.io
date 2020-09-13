---
layout: default
title: Probability
nav_order: 81
---



# Probability


### Squares on a chessboard
{: .d-inline-block}

A5, 2019
{: .label}

<p>
You are given an \(8 \times 8\) chessboard. If two distinct squares are chosen uniformly at random find the probability that two rooks placed on these squares attack each other. Recall that a rook can move either horizontally or vertically, in a straight line.
</p>

<details><summary>Solution</summary>

<p>
\(2/9\)
</p>

</details>


---






### Tinku's chocolate
{: .d-inline-block}



A5, 2012
{: .label}

<p>
a) \(n\) identical chocolates are to be distributed among the \(k\) students in Tinku's class. Find the probability that Tinku gets at least one chocolate, assuming that the \(n\) chocolates are handed out one by one in \(n\) independent steps. At each step, one chocolate is given to a randomly chosen student, with each student having equal chance to receive it.
</p>

<p>
b) Solve the same problem assuming instead that all distributions are equally likely. You are given that the number of such distributions is \(\left(\begin{array}{c}n+k-1 \\ k-1\end{array}\right) .\)
</p>

<p>
The chocolates are considered interchangeable but students are considered different.
</p>


<details><summary>Solution</summary>
<p>
(a) The probability of Tinku not getting a chocolate in one step is \(1-\frac{1}{k}\).
</p>

<p>
\begin{align}
\mathrm{P}(\text { Tinku gets at least one chocolate })&=1-\mathrm{P}(\text { Tinku gets none }) \\
&=1-\left(1-\frac{1}{k}\right)^{n}
\end{align}
</p>


<p>
Sol 1. (b) There are \(\left(\begin{array}{c}(n-1)+k-1 \\ k-1\end{array}\right)\) distributions in which Tinku gets at least a chocolate: give Tinku a chocolate and then use the given formula to find number of distributions of the remaining \(n-1\) chocolates among \(k\) students. So the answer is \(\left(\begin{array}{c}(n-1)+k-1 \\ k-1\end{array}\right) /\left(\begin{array}{c}n+k-1 \\ k-1\end{array}\right)=\frac{n}{n+k-1} \)
</p>

<br>

<p>
Sol 2. (b) The number of distributions in which Tinku gets no chocolate \(=\) number of distributions of \(n\) chocolates among the remaining \(k-1\) students \(=\left(\begin{array}{c}n+k-2 \\ k-2\end{array}\right) .\) So the desired probability is \(1-\left(\begin{array}{c}n+k-2 \\ k-2\end{array}\right) /\left(\begin{array}{c}n+k-1 \\ k-1\end{array}\right)=\frac{n}{n+k-1}\)
</p>

</details>
---


### Sampling a quadratic
{: .d-inline-block}

A8, 2013
{: .label}

<p>
Consider the quadratic equation \(x^{2}+b x+c=0\), where \(b\) and \(c\) are chosen randomly from the interval [0,1] with the
probability uniformly distributed over all pairs \((b, c)\).
</p>

<p>
Let \(p(b)=\) the probability that the given equation has a real solution for given (fixed) value of b.
</p>

<p>
Complete the sentences below.
</p>

<p>
(a) The equation \(x^{2}+b x+c=0\) has a real solution if and only if \(b^{2}-4 c\) is
</p>

<p>
(b) The value of \(p\left(\frac{1}{2}\right),\) i.e., the probability that \(x^{2}+\frac{x}{2}+c=0\) has a real solution is
</p>

<p>
(c) As a function of \(b,\) is \(p(b)\) increasing, decreasing or constant?
</p>

<p>
(d) As \(b\) and \(c\) both vary, what is the probability that \(x^{2}+b x+c=0\) has a real solution?
</p>

<details><summary>Solution</summary>
<p>
(a) The equation \(x^{2}+b x+c=0\) has a real solution if and only if \(b^{2}-4 c\) is \(\geq 0\)
</p>

<p>
(b) The value of \(p\left(\frac{1}{2}\right),\) i.e., the probability that \(x^{2}+\frac{x}{2}+c=0\) has a real solution is \(\frac{1}{16}\).
There is a real root when \(b^{2}-4 c=\frac{1}{4}-4 c \geq 0,\) i.e., \(0 \leq c \leq \frac{1}{16}\) which is \(\frac{1}{16}\)
fraction of the interval [0,1] over which \(c\) ranges.
</p>


<p>
(c) Increasing. This is because \(b^{2}-4 c \geq 0\) if and only if \(0 \leq c \leq \frac{b^{2}}{4}\).<br>
So \(p(b)=\frac{b^{2}}{4},\) which is increasing for \(0 \leq b \leq 1\)
</p>


<p>
(d) This is the fraction of the area of the unit square \([0,1] \times[0,1]\) that is occupied by the region \(b^{2}-4 c \geq 0,\) i.e., it is the area under the parabola \(c=\frac{b^{2}}{4}\) from \(b=0\) to \(b=1\) which is \(\int_{0}^{1} \frac{b^{2}}{4} d b=\frac{1}{12}\)
</p>

</details>

---

### Conditional probability
{:b .d-inline-block}

A11, 2015
{: .label}

<p>
There are four distinct balls labelled 1,2,3,4 and four distinct bins labelled \(\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D} .\) The balls are picked up in order and placed into one of the four bins at random. Let \(E_{i}\) denote the event that the first \(i\) balls go into distinct bins. Calculate the following probabilities.
Notation: \(\operatorname{Pr}[X]=\) the probability of event \(X\) taking place. \(\operatorname{Pr}[X \mid Y]=\) the probability of event \(X\) taking place, given that event \(Y\) has taken place.
</p>

<details><summary>Solution</summary>

<p>
(i) \(\operatorname{Pr}\left[E_{4}\right]=\frac{4 !}{4^{4}}=\frac{3}{32}\)
(ii) \(\operatorname{Pr}\left[E_{4} \mid E_{3}\right]=\frac{1}{4}\)
(iii) \(\operatorname{Pr}\left[E_{4} \mid E_{2}\right]=\frac{24}{4^{2}}=\frac{1}{8}\)
(iv) \(\operatorname{Pr}\left[E_{3} \mid E_{4}\right]=1\)
</p>


</details>

---



### Vertex in a polygon
{: .d-inline-block}

A5, 2014
{: .label}

<p>
A regular 100-sided polygon is inscribed in a circle. Suppose three of the 100 vertices are chosen at random, all such combinations being equally likely. Find the probability that the three chosen points form vertices of a right angled triangle.
</p>


<details><summary>Solution</summary>

<p>
\(1/33\)
</p>

</details>

---




### Test preparation
{: .d-inline-block}

B1, 2016
{: .label}



<p>
Out of the 14 students taking a test, 5 are well prepared, 6 are adequately prepared and 3 are poorly prepared. There are 10 questions on the test paper. A well prepared student can answer 9 questions correctly, an adequately prepared student can answer 6 questions correctly and a poorly prepared student can answer only 3 questions correctly.
</p>

<p>
(a) If a randomly chosen student is asked two distinct randomly chosen questions from the test, what is the probability that the student will answer both questions correctly?
</p>

<p>
(b) Now suppose that a student was chosen at random and asked two randomly chosen questions from the exam, and moreover did answer both questions correctly. Find the probability that the chosen student was well prepared.
</p>

<p>
Express your answers as irreducible fractions.
</p>


<details>

<summary>Solution</summary>

<p>
(a) The probability that a randomly chosen student is well prepared is \(5 / 14\) The probability of a well prepared student answering two randomly chosen questions correctly is \(\left(\begin{array}{l}9 \\ 2\end{array}\right) /\left(\begin{array}{l}10 \\ 2\end{array}\right) .\) So the probability that a randomly chosen student is well prepared AND answers two randomly chosen questions correctly is \(\frac{5}{14} \times \frac{\left(\frac{9}{20}\right)}{(10)}=\frac{2}{7} .\) A student belongs to exactly one of the three preparedness categories, so the desired probability is obtained by adding \(\frac{2}{7}\) with the results of parallel calculations for the other two categories. We get
</p>

<p>
Let \(P(W),P(M)\) and \(P(K)\) denote the probability that the student is well prepared, moderately prepared and poorly prepared, respectively.
</p>

<p>
\[
P(\text { both answers correct })=
P(\text { W }) \frac{\left(\begin{array}{l}
9 \\
2
\end{array}\right)}{\left(\begin{array}{c}
10 \\
2
\end{array}\right)}+P(\text { M }) \frac{\left(\begin{array}{c}
6 \\
2
\end{array}\right)}{\left(\begin{array}{c}
10 \\
2
\end{array}\right)}+P(\text { K }) \frac{\left(\begin{array}{c}
3 \\
2
\end{array}\right)}{\left(\begin{array}{c}
10 \\
2
\end{array}\right)}
\]

which equals

\[
\frac{5}{14} \times \frac{36}{45}+\frac{6}{14} \times \frac{15}{45}+\frac{3}{14} \times \frac{3}{45}=\frac{31}{70}
\]

</p>

<p>
(b) The probability that a randomly chosen student was well prepared given that he answered both questions correctly is
</p>

<p>
\begin{align}
P(\text { well prepared | both correct })&=\frac{P(\text { well prepared and both correct })}{P(\text { both correct })}\\
&=\frac{2 / 7}{31 / 70}=\frac{20}{31}
\end{align}
</p>

</details>

