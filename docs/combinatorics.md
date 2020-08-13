---
layout: default
title: Combinatorics
nav_order: 7
---


# Combinatorics


### Serendipitous sum
{:b .d-inline-block}

B4, 2011
{: .label}

Let S be the set of all 5-digit numbers that contain the digits 1,3,5,7 and 9 exactly once (in usual base 10 representation).
Show that the sum of all elements of S is divisible by 11111. Find this sum.


#### Solution

Each number appears in the \\(i\\)th place exactly \\(4!\\) times for
\\(i\in {1,\ldots,5}\\). So the sum of numbers corresponding to each place is

\\[ 4!(1+3+5+7+9) = 4!\times 25 = 600 \\]

The total sum is therefore:


\\[ 10^4\cdot 600 + 10^3\cdot 600 + 10^2\cdot 600 + 10^1\cdot 600 + 600 = 6666600 \\]



---


### Sum of a finite series [2019]

The sum \\( S = 1 + 111 + 11111 + \cdots + \underbrace{11 \cdots 1}_{2k+1} \\)


#### Solution


\begin{align}
9S &= 9 + 999 + 99999 + \cdots + \underbrace{99 \cdots 9}_{2k+1} \\\\\\\\
 &= (10-1) + (1000-1) + \cdots + (100^{2k+1}-1) \\\\\\\\
 &= \frac{10(100^{k+1} - 1)}{99} - (k+1) \\\\\\\\
S&= \frac{ 10^{2k+3} - 99k - 109}{99\times 9}
\end{align}

---

### Impossible solid
{: .d-inline-block}

B6, 2011
{: .label }

Show that there is no solid figure with exactly 11 faces such that each face is a polygon
having an odd number of sides.

#### Solution

Let us add up the number of sides from each face and call this number T.  It is given that there are 11 faces and each face has odd sides, so T is odd. However,
in any solid each side is counted twice since two faces intersect to form a side. So T must be even, which is a contradiction. Hence such a solid cannot exist.


![](/assets/images/dodecahedron.png)




---


### Progression of squares
{: .d-inline-block}

A4, 2010
{: .label }

Show that there is no infinite arithmetic progression consisting of distinct integers all
of which are squares.

#### Solution

Suppose the infinite A.P. is given by

\\[ a_0^2 < a_1^2 < a_3^2 < \cdots \\]

Without loss of generality, assume that \\(a_0>0\\). Let the common difference be \\(d\neq 0\\).

The difference between any two consecutive squares in the A.P. is unbounded, hence at some point \\( a_i^2 - a_{i-1}^2 > d \\).


---





### Give-away problem
{: .d-inline-block}

A1, 2010
{: .label }


The word MATHEMATICS consists of 11 letters. The number of distinct ways to rearrange these letters is.



- [ ] 11!
- [ ] 11!/3
- [ ] 11!/6
- [x] 11!/8






