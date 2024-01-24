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

<li>
Suppose \(a_i\) and \(b_i\) are real numbers such that \(\sum_1^\infty a_i^2\) and \(\sum_1^\infty b_i^2\) converge. Which of these statements is true?

<ol>
<li>The sequence \(\sum_1^\infty |a_i-b_i| \) converges. </li>
<li>The sequence \(\sum_1^\infty |a_i-b_i|^{2} \) converges. </li>
<li>The sequence \(\sum_1^\infty (a_i-b_i)^2 \) converges. </li>
<li>The sequence \(\sum_1^\infty (a_i-b_i)^3 \) converges. </li>
</ol>
</li>

<details open><summary>Sol.</summary>
<b>Ans.</b> (b), (c) and (d).<br>

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
<p>
Suppose \( S=\{1,2,3,4,5\} \).  Find the number of pairs \( (A,B) \)
that can be formed such that \(A \subseteq S\) and \(B\subset A\).
</p>
</li>

<details open><summary>Sol.</summary>
Consider the pairs where \(A \subseteq S\) and \(B\subseteq A\). Each element in \(S\) has three choices:<br>
(i) It can be in \(B\)<br>
(i) It can be in \(A\setminus B\)<br>
(iii) It can be in \(S\setminus A\)<br>
Hence, there are \(3^5\) such pairs. From this we subtract the number of pairs where \(B=A\). There are \( 2^5 \) of 
these. Hence, the required number is \( 3^5 - 2^5 = 211 \).<br>

<i>Source: Slight variation of an ISI Tomato problem.</i>
</details>


<li>
<p>If \(a+b+c=0\), then the quadratic equation \(3 a x^{2}+2 b x+c=0\) has<br>
(a) at least one root in \((0,1)\) <br>
(b) one root in \((1,2)\) and the other in \((-1,0)\) <br>
(c) both imaginary roots <br>
(d) a repeated root<br>
</p>
</li>

<details><summary>Solution</summary>

(a)
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


<li>
<p> The number of continuous functions \(f: \mathbb{R} \rightarrow \mathbb{R}\) satisfying \((f(x))^{2}=x f(x)\) is ________<br>
</p>
</li>


<details><summary>Solution</summary>
Ans: 4<br>

 \(f(x) = 0\) is an obvious solution. If \(f(x) = 0\) for some \(x>0\),
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











</ol>



## Part B: Subjective questions

**Submission files:** Each question in this part must be answered on a page of its own. Name the files as B1.jpg, B2.jpg, etc. In case you have multiple files
for the same question, say B4, name the corresponding files as B4-1.jpg, B4-2.jpg, etc.
{: .fs-3 }


**Clearly explain your entire reasoning.** No credit will be given without reasoning. Partial solutions may get partial credit.


---


