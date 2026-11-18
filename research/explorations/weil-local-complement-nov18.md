# Excluding the exterior zero contribution to a local arithmetic matrix

**Status.** Proposed two-sided localization refinement of the [Gaussian matrix criterion](weil-gaussian-nov18.md). The controlling constants are absolute and unevaluated. No sign assertion for the arithmetic matrices is assumed.

Use the preceding parameters $X,H,S,L$, and let $h=\sqrt{H/X}$, $B=\sqrt{XH}$, so $hB=H$. Prescribe an absolute target exponent $a>0$. We modify only the common cutoff of the trial modes. There are constants $C,C',D$ such that the resulting **same** matrix $A$ has these two properties for all sufficiently large $X$ and sufficiently small $H/X$.

1. A defect within $|T-X|\le B$ of displacement $\delta\ge d$ gives $\lambda_{\min}(A)\le-e^{-C_0H}$. One can take $C_0$ independent of $a$.
2. If all zeta zeros with $|T-X|\le DB$ have displacement at most $\epsilon$, where $0\le\epsilon\le1/2$, then
$$
 \lambda_{\min}(A)\ge -e^{-aH}
 -C_D \epsilon^2 e^{2\epsilon L}L^3 B\log X.
$$
In particular, if this enlarged local zero census is entirely on the line, the matrix is bounded below by $-e^{-aH}I$, regardless of every exterior zero. One can choose $a>C_0+1$ for a gap between this range and the guaranteed interior-defect signature.

## Cutoff with two controlled tails

Let $m=\lceil H\rceil$. Convolve the indicator of $[-L+h/2,L-h/2]$ with $m$ independent uniform probability densities on $[-h/(8m),h/(8m)]$, and with one fixed smooth nonnegative even probability bump rescaled to $[-h/8,h/8]$. The result $\chi$ is smooth, is equal to one on $[-L+3h/4,L-3h/4]$, and vanishes outside $[-L+h/4,L-h/4]$. Its derivatives through order two are $O_j(h^{-j})$ by differentiating the last probability bump in $L^1$. It still satisfies $0\le\chi\le1$.

This replaces $x_0=L-2/S$ by $x_0=L-3h/4$ in the physical-tail proof. The corresponding $b=\pi\sin(2h)Se^{-3h/2}$ differs from the former one by $O(h^2X)=O(H)$ once $H/X$ is sufficiently small after fixing $C$, since then $S\ll X$. The slack from $C\sqrt{XH}$ absorbs this loss. All other truncation and coefficient estimates in the Gaussian proof remain valid. The constants for this first part and its coefficient norm are fixed before choosing the larger exterior band $D$ in the next part.

For complex $z$ in $|\Im z|\le1/2$ the interval-average transforms give the bound
$$
 |\widehat\chi(z)|\le 2Le^{L/2}\min\left(1,{8m\over h|z|}\right)^m.
$$
Indeed each box transform is $\sin(hz/(8m))/(hz/(8m))$, bounded both by its averaged absolute value and by $e^{h|\Im z|/(8m)}/(h|z|/(8m))$. The exponential weights for all factors multiply to at most $e^{L/2}$.

## Exterior estimate

For an ordinate $z$ with $v=|\Re z-X|>DB$ and any retained frequency $t_k=k\pi/L$, taking $D>2C'$ gives $|z-t_k|\ge v/2$. Since $m\le2H$, the last factor in the transform of $g_k$ is bounded by $(32 B/v)^m$. For any prescribed $a'>0$ choose a large fixed $D$ so that, for all large $X$,
$$
 (32 B/v)^m\ll e^{-a'H}(B/v)^2,\qquad v>DB .
$$
The polynomial factor ensures summability over the entire exterior. The local Riemann–von Mangoldt bound in intervals of length one gives
$$
 \sum_{z\in\Gamma:\,|\Re z-X|>DB}(B/|\Re z-X|)^4
 \ll_D B\log(2+X+B).
$$
This follows by dyadically grouping distances and bounding the number in each interval of length $r\ge1$ by $O(r\log(2+X+r))$. Both positive and negative ordinates are included.

For $g=\sum a_k g_k$ with coefficient norm one, Cauchy–Schwarz and the preceding estimates give
$$
 \sum_{\mathrm{ext}}|\widehat g(z)|^2
 \le \sum_{k\in J}\sum_{\mathrm{ext}} |\widehat g_k(z)|^2
 \ll_D |J| L e^L B\log(2+X+B)e^{-2a'H}.
$$
The factor outside the exponential is polynomial in $X$, with $H\ge\log X$. As $D$ is fixed after $a'$, its implicit multiplicative constant is absorbed by a sufficiently large $X$. Thus choosing $a'$ large establishes the desired bound $e^{-aH}$. Conjugation preserves the exterior, so the absolute value of its Weil contribution is bounded by this same number.

## Interior estimate

For each conjugate pair $z=t+iy,\bar z=t-iy$ write $v_\pm=\widehat g(t\pm iy)$, $p=(v_++v_-)/2$, $q=(v_+-v_-)/2$. The sum for the pair is $2|p|^2-2|q|^2$. If $|y|\le\epsilon$ then $|q|\le\epsilon\sup_{|\Im u|\le\epsilon}|\widehat g'(t+i\Im u)|$. The cutoff multiplication is a contraction in $L^2$, and the uncut normalized exponentials are orthonormal on $[-L,L]$, hence $\|g\|_2\le1$. Consequently
$$
 |\widehat g'(t+iy')|\le L(2L)^{1/2} e^{\epsilon L},\qquad |y'|\le\epsilon.
$$
All real ordinates contribute nonnegatively. Counting at most $O_D(B\log X)$ ordinates in the enlarged window and adding the exterior estimate proves the theorem.

**Arithmetic interpretation.** A certified local zero census now bounds the contribution to the full signed form on this subspace. In the other direction a computed eigenvalue below the stated lower bound forces an off-line ordinate within the enlarged local band at displacement exceeding $\epsilon$. Neither direction requires a hypothesis about unseen zeros outside that band.
