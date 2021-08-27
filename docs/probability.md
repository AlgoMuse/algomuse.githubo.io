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

### Yet another dice roll
{: .d-inline-block}

A4, 2020
{: .label}

<p>
(i) What is the probability that among \(100\) rolls of a fair die the first \(3\) rolls yield at least one \(4\)?
</p>

<p>
(ii) Calculate the probability that out of the last \(4\) rolls, exactly two are multiples of \(3\).
</p>

<details><summary>Solution</summary>

<p>
(i) The probability that none of the first three rolls have a 4 is \( (5/6)^3 \). So the required probability is \(1 - (5/6)^3\).
</p>

<p></p>

<p>
(ii) Let \(S\) be the number of ways in which four rolls can have exactly two multiples of 3. The required probability \(P\) is then \(S/6^4\).
</p>

<p> Let us calculate \(S\). Two positions can be picked in \( \binom{4}{2} \)
ways. These two positions can have either a 3 or a 6. So the favorable positions can be filled in \( \binom{4}{2}\times 2^2 \) ways. The other two positions can have either 1, 2, 4 or 6. So they
can be filled in \( 4^2\) ways. Hence we have:

\[ P = \frac{  \binom{4}{2}\times 4 \times 4 \times 4  }{6^4} = \frac{2}{3}^3 = \frac{8}{27} \]

</p>

</details>

---

### Coin toss and a dice roll
{: .d-inline-block}

B2a, 2021
{: .label}


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

