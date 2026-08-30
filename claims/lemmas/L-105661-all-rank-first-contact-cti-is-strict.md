# L-105661 — All-rank CTI is strict at first contact

**Claim ID:** `L-105661`  
**Status:** proved exact local analytic theorem  
**Date:** 2026-08-31

Let `G_s` be a finite positive Cauchy Gram, with confluent derivative blocks
allowed, and define

\[
\mathcal O_H=\operatorname{tr}(G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H}),\qquad
\mathcal T_H=\operatorname{tr}(G_0^{-1}G_H).
\]

There exists `H_0>0` such that

\[
\boxed{\mathcal O_H>\mathcal T_H\quad(0<H<H_0).}\tag{1}
\]

Put `G=G_0`,

\[
M=-G'_0=[(\overline\lambda_i+\lambda_j)^{-2}],\qquad
N=G''_0=[2(\overline\lambda_i+\lambda_j)^{-3}],
\]

and `A=G^{-1/2}MG^{-1/2}`, `B=G^{-1/2}NG^{-1/2}`. The block matrix
`[[G,M],[M,N]]` is the Gram of packet functions and their products with
`xi`; hence `B-A^2>=0`. Direct matrix expansion gives

\[
\mathcal T_H=n-H\operatorname{tr}A+\frac{H^2}{2}\operatorname{tr}B+O(H^3),
\]

\[
\mathcal O_H=n-4H^2\operatorname{tr}(B-A^2)+O(H^3).
\]

Thus the current reserve is linearly positive at contact while the complete
nonorthogonal phase defect is quadratically soft. Since `tr A>0`, (1) follows.
No separation hypothesis is used.
