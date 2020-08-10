---
layout: default
title: Calculus
nav_order: 4
---


# Calculus



### Vanilla application of L'Hospital
{: .d-inline-block }

A3, 2011
{: label .label-blue}

Evaluation the limit:

\\[ \lim_{x \rightarrow 1}\left(\frac{n- \displaystyle \sum_{k=1}^n x^{k}}{1-x}\right) \\]


#### Solution

We apply the L'Hospital's rule and differentiate both the numerator and the denominator.

\begin{array}{rl}
 \lim_{x\rightarrow 1}&\displaystyle \frac{-n x^{n-1}-(n-1) x^{n-2}-\cdots-x-1}{-1}  \\\\\\\\
 \lim_{x\rightarrow 1}&\displaystyle \frac{n(n-1)}{2}
\end{array}




### Only one real root
{: .d-inline-block }

A8, 2011
{: label .label-blue}


Suppose \\(f(x) = x^3 + x^2 + cx + d\\), where \\(c\\) and \\(d\\) are real numbers. Prove that if \\(c>1/3\\),
then \\(f\\) has exactly one real root.


*Requires algebra too*.

#### Solution

Since the function has odd degree as the highest power, it has at least one
real root. To show that the function has exactly one real root
we have to show, that it is monotonic in the whole \\(\mathbb{R}\\).
This can be done by showing that \\(f'(x)\\) is always positive when \\(c>1/3\\).

\\[ f'(x) = 3x^2+2x+c \\]

The discriminant of the above quadratic, \\(2^2-4\cdot3\cdot c\\), is negative when \\(c>1/3\\).
Hence, \\(f'(x)\\) is always positive in \\(\mathbb{R}\\).


### Rolle's theorem
{: .d-inline-block }

A9, 2011
{: label .label-blue}

A real-valued function \\(f(x)\\) defined on a closed interval \\([a,b]\\) has the property
that \\(f(a)=f(b)=0\\) and \\(f(x)=f'(x)+f^{\prime\prime}(x)\\) for all \\(x\\) in \\([a,b]\\). Show that \\(f(x)=0\\) for
all \\(x\\) in \\([a,b]\\).

#### Solution

If \\(f(x)\\) is not constant, then it must attain a local maxima or minima at some value \\(c\in[a,b]\\).
From the condition specified:
\begin{equation}
f(c)=f'(c)+f^{\prime\prime}(c)
\label{eq:rolle}
\tag{1}
\end{equation}



If \\(f(c)\\) is the local maxima, then \\(f(c)>0\\), \\(f'(c)=0\\) and
\\(f^{\prime\prime}(c)<0\\). But Eq.\\(\eqref{eq:rolle}\\) does not hold in that case. A similar argument holds for local minima. Hence, \\(f(x)\\) is zero in the interval \\([a,b]\\).



---


### A simple substitution
{: .d-inline-block }

A2, 2011
{: label .label-blue}



Let \\(f\\) be a real valued continuous function defined on \\(\mathbb{R}\\) satisfying
\\(f^{\prime}\left(\tan ^{2} \theta\right)=\cos 2 \theta+\tan \theta \sin 2 \theta,\\) for all real numbers \\(\theta\\)
If \\(f(0)=-\cos \frac{\pi}{12}\\) then find \\(f(1)\\)

#### Solution

Substitute \\(t=\tan^{2} \theta \\). Then we have
\begin{align}
f'(\tan^2\theta) & = \cos 2\theta(1+\tan \theta \tan 2\theta ) \\\\\\\\
f'(\tan^2\theta) & = \frac{1-\tan^2\theta}{1+\tan^2\theta} \left( 1 + \frac{2\tan^2\theta}{1-\tan^2\theta} \right) \\\\\\\\
f'(t) & = \frac{1-t}{1+t} \left( 1 + \frac{2t}{1-t} \right) \quad\text{ where } t=\tan^2 \theta \\\\\\\\
f'(t) & = 1 \\\\\\\
f(t) & = t + constant
\end{align}



Hence the answer is \\(1-\cos \frac{\pi}{12}\\).






<!--

<table>
<tr>
<td>
<div class="card">
  <img src="https://thumbs-prod.si-cdn.com/sAw6gPjQpCHoRAaYGna1Nof5xQU=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/7c/a4/7ca4762d-8448-40ef-8680-6739305f266c/agnesi-wr.jpg" alt="Avatar" style="width:300px">
  <div class="container">
    <h4><b>Angei</b></h4>
    <p>Mathematician</p>
  </div>
</div>
</td>
<td>
<div class="card">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Gottfried_Wilhelm_Leibniz.jpg" alt="Avatar" style="width:300px">
  <div class="container">
    <h4><b>Leibniz</b></h4>
    <p>Interior Designer</p>
  </div>
</div>
</td>
</tr>
</table>



-->

