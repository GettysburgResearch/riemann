# A shorter finite Li detection horizon

In the notation of the [angular Li converse](li-angular-converse-nov18.md), let $a=\max_\rho\log|1-1/\rho|>0$ and $\ell=\log(2/a)$. Then some $\lambda_n<0$ with
$$
 n\ll a^{-1}\ell\log(2+\ell).
$$
The improvement replaces the second full logarithm by an iterated one. We use the angular localization and infinite-tail estimates in the linked note, with the following replacement for its Fejér detection step.

Write $D=\lceil1/a\rceil$, $m=\max(1,\lfloor D/100\rfloor)$, $J=\lceil C\ell\log(2+\ell)\rceil$, $j_0=J$, and
$$
 P(w)=\left(D^{-1}\sum_{r=0}^{D-1}w^r\right)^J .
$$
By the known first zero, $a\le1/(2\cdot14^2)$, so $D\ge392$ and $D/m$ is bounded by an absolute constant. On $|w|\le1$ we have $|P|\le1$. Also $|P(w)|\le q^J$ whenever the angular distance to zero is greater than $4/D$, for some absolute $q<1$. Indeed $|1-w^D|\le2$, and $|1-w|\ge\sin(4/D)$ for angles from $4/D$ to $\pi/2$, and at least 1 beyond; $2/(D\sin(4/D))<0.51$ here.

Select an extremal angle $\theta_*$ and let $w_\rho=e^{-a-i\theta_*}(1-1/\rho)$. From the low zeros $|\gamma|\le a^{-1/2}$ take those within $4/D$ of the centered angle zero. Their number $k$ counted with multiplicities is $1\le k\le C_1\ell$ by the angular-cell count. For these zeros set $v=w_\rho^m$, $b=P(w_\rho)v^{j_0}$. One target has $v=b=1$. All satisfy $|v|,|b|\le1$ and
$$
 |b-1|\le C_2(J+j_0)|v-1|.
$$
In fact $|1-P(w)|\le JD|1-w|$ by its positive normalized coefficients. On this cluster $w=\exp(-u+i\theta)$ with $0\le u\le2a$, $|\theta|\le4/D$. Thus $m|-u+i\theta|<1/10$ and $|1-w|\ll |1-w^m|/m$ by the exponential Taylor estimate, uniformly. Finally $|1-v^{j_0}|\le j_0|1-v|$.

Put $S_n=\sum_{\rm cluster} b v^n$. Choose $r\in[1/2,1)$ with $(1-r)^{-1}=10(1+C_2)k(1+J+j_0)$. The function $\sum b/(1-rv)$ has real part at least $(1-r)^{-1}-2C_2 k(J+j_0)$, because one unweighted term is $(1-r)^{-1}$, all the others have positive real part, and $|1-v|/|1-rv|\le2$ for $|v|\le1$. Hence it has modulus at least $1/(2(1-r))$. As a generating function at $r$, its denominator $\prod(1-rv)$ has modulus at least $(1-r)^k$ and its numerator is a polynomial of degree $<k$. The first $k$ coefficients of this numerator are the convolution of $S_0,\ldots,S_{k-1}$ with coefficients of a denominator of $\ell^1$ norm at most $2^k$. It follows that for some $0\le n<k$,
$$
 |S_n|\ge (1-r)^{k-1}/(2k\,2^k).
 \tag{1}
$$
For the present choices this exceeds $\exp[-C_3(1+\log(2+C))\ell\log(2+\ell)]$ with an absolute $C_3$ independent of $C$.

Use $T(z)=z^{m(j_0+n)}P(z)$ for this index. The centered sum over low zeros of $T(w_\rho)$ differs from $S_n$ by $O(a^{-1/2}\ell q^J)$. The uncentered sum of $T(e^{-a}(1-1/\rho))$ over the same low zeros is $O(a^{-1/2}\ell q^J)$ since their angular distances to zero are $\gg\sqrt a$, and in fact exceed $4/D$: from the exact arctangent formula and $|\gamma|\ge14$, $|\theta|\ge 0.99/|\gamma|\ge0.99\sqrt a>4/D$. The real polynomial
$$
 Q(z)=T(z)+\tfrac12\big(e^{i\phi}T(e^{-i\theta_*}z)+e^{-i\phi}T(e^{i\theta_*}z)\big)
$$
has coefficient weights $t_j(1+\cos(\phi-j\theta_*))\ge0$ summing to at most two, where $T=\sum t_jz^j$. Conjugate symmetry and a choice of $\phi$ realize $|S_n|$ as the positive desired term in the low sum, to the errors just bounded.

All nonzero coefficients of $Q$ have indices between $N_-=m j_0$ and $N_+=m(j_0+k)+DJ$. Middle and infinite-tail subtraction estimates from §4 of the linked proof apply with these endpoints and total weight two. In detail, for $Y=(N_++2/a)^2$ the middle contribution is $\ll e^{-aN_-/2}Y\log(2Y)$, all subtractions through $Y$ are $\ll e^{-aN_-}Y\log(2Y)$, and the remaining real Li tail is $\ll e^{-aN_-}N_+^2\log(2Y)/Y$. Here $am$ is bounded below by a fixed positive absolute constant. Thus all errors are at most a polynomial in $1/a,C,J$ times $\exp(-cC\ell\log(2+\ell))$. Increasing $C$, which dominates the $\log(2+C)$ dependence in (1), makes them together strictly less than $|S_n|$, uniformly over the stated range of $a$. Consequently the nonnegative weighted Li sum is negative, forcing a negative coefficient at an index at most $N_+$. This proves the asserted horizon.
