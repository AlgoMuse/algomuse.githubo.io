---
layout: default
title: Algebra
nav_order: 3
---


# Algebra



### Parity of a polynomial
{: .d-inline-block}

A2, 2010
{: .label .label-blue}


A polynomial \\(f(x)\\) has integer coefficients such that \\( f(0)\\) and \\( f(1)\\) are both odd numbers.
Prove that \\( f(x) = 0 \\) has no integer solutions.

#### Solution

Suppose \\(f(x)=c_{n} x^{n}+c_{n-1} x^{n-1}+\cdots+c_{0}\\)

Since \\( f(0) \\) and \\( f(1) \\) are odd numbers, \\(c_0\\) is odd and

\\[ \text{Parity of } \sum_{i=1}^n c_i \text{ is even}\\]


Suppose \\(f(x)\\) has an integer root \\(r\\). Let us see what happens to the parity of \\( f(r) \\).

\begin{align}
\text{Parity of }f(r) &= \text{Parity of }r \times \text{Parity of} \sum_{i=1}^n c_i  + \text{Parity of }c_0 \\\\\\\\
\text{Parity of }f(r) &= \text{odd}
\end{align}

Since \\( f(r) \\) is an odd number \\(r\\) cannot be a root of the polynomial.

---


### Binomial expansion
{: .d-inline-block}

B2, 2011
{: label .label-blue}

Show that the power of \\(x\\) with the largest coefficient in the polynomial \\(\displaystyle (1 + 2x/3)^{20}\\) is 8. In other words, if
we write the given polynomial as \\( \sum_i a_ix^i\\) then the largest coefficient \\(a_i\\) is \\(a_8\\).


#### Solution

The co-efficient \\( a_i = \binom{20}{i} \left(\frac{2}{3}\right)^i \\). Consider the ratio of two consecutive terms: \\( a_{i+1}/a_i \\).

\begin{align}
\text{ratio } &= \frac{2}{3} \times \left(  \frac{20!}{20-i-1!i+1!}/\frac{20!}{20-i!i!} \right) \\\\\\\\
&\\\\\\\\
  &= \frac{2}{3} \cdot \frac{20-i!i!}{20-i-1!i+1!} = \frac{2(20-i)}{3(i+1)}
\end{align}


The ratio \\( a_{i+1}/a_i > 1\\) upto \\(i\leq 7\\) and strictly less than 1 for \\(i>7\\). Hence, the sequence of co-efficients is bitonic with the peak occuring at \\(a_8\\).

---

### AM-GM inequality
{: .d-inline-block}

A4, 2011
{: label .label-blue}

Given positive real numbers \\( a_1, a_2, \ldots , a_{2011} \\) whose product \\(a_1 a_2 \cdots a_{2011}=1\\),
what can you say about their sum \\( S = a_1 + a_2 + · · · + a_{2011} \\)?

- [ ] \\( S\; \\) can be any positive number.
- [ ] \\( 1 \leq S \leq 2011\\).
- [x] \\( 2011 \leq  S \text{ and }  S\;\\) is unbounded above.
- [ ] \\( 2011 \leq  S \text{ and }  S\;\\) is bounded above.

*Explanation*. The first inequality follows from AM-GM inequality. To see why \\(S\\) is unbounded, set
\\( a_1=n \\), \\(a_2=1/n\\) and the rest of \\( a_is\\) to 1. The sum \\(S>n\\) for any \\(n\\).


---

### Roots of a quadratic
{: .d-inline-block}

A6, 2011
{: label .label-blue}


*Explanation*. (B) Let \\(p\\) and \\(q\\) be the roots of the equation. The condition in the problem implies that both are real and non-zero. We know that \\(p+q=-b\\) and \\(pq=c\\).
If one root is rational and the other is irrational, then both \\(b\\) and \\(c\\) must be irrational. If both the roots are rational, then both \\(b\\) and \\(c\\) must be rational. Hence, both \\(p\\) and \\(q\\) must be irrational.




### Polynomial factorization
{: .d-inline-block}

B5, 2011
{: label .label-blue}

It is given that the complex number \\(i−3\\) is a root of the polynomial \\(3x^4+10x^3+Ax^2+Bx−30\\),
where \\(A\\) and \\(B\\) are unknown real numbers.  Find the other roots.

#### Solution

Complex roots come in conjugates, so \\(-i-3\\) must also be a root. So \\( (x-i+3)(x+i+3) = (x^2+6x+10) \\) must be a factor. The given
polynomial can writen as
\\[ (x^2+6x+10)(ax^2+bx+c) \\]

By comparing the co-efficients, \\(a=3,b=-8,\text{and }c=-3\\). Hence the polynomial is:

\\[ (x^2+6x+10)(3x^2-8x-3) \\]
\\[ (x^2+6x+10)(x-3)(3x+1) \\]

Hence the other roots are 3 and -1/3.


---


### Only one real root
{: .d-inline-block}

B8, 2011
{: label .label-blue}




Suppose \\(f(x) = x^3 + x^2 + cx + d\\), where \\(c\\) and \\(d\\) are real numbers. Prove that if \\(c>1/3\\),
then \\(f\\) has exactly one real root.

*Requires calculus too*.

#### Solution

Since the function has odd degree as the highest power, it has at least one
real root. To show that the function has exactly one real root
we have to show, that it is monotonic in the whole \\(\mathbb{R}\\).
This can be done by showing that \\(f'(x)\\) is always positive when \\(c>1/3\\).

\\[ f'(x) = 3x^2+2x+c \\]

The discriminant of the above quadratic, \\(2^2-4\cdot3\cdot c\\), is negative when \\(c>1/3\\).
Hence, \\(f'(x)\\) is always positive in \\(\mathbb{R}\\).


---


