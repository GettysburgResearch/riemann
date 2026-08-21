# L-19847 — Generic low-prolate surjectivity without quantitative conditioning

Claim ID: `L-19847`  
Status: **PROPOSED COMPLETE ALGEBRAIC SOURCE-FRAME REPAIR**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: analytic dependence of finite prolate eigenspaces on support; fixed-packet prolate-to-Hermite convergence with Mellin derivatives; Hermite Mellin/Meixner--Pollaczek formula; Mellin factorization of `E`  
Scope: replaces the false/overstrong complete `sigma_min` requirement by the three inputs actually used in `L-19846`: generic surjectivity, an upper map bound, and target-line nondegeneracy

## 1. Statement

Let

\[
 m_\lambda=O((\log\lambda)^2)
 \tag{L-19847.1}
\]

and let `U_lambda` be the exact signed low-prolate source packet after the two
source constraints

\[
 f(0)=0,
 \qquad
 \int f=0.
 \tag{L-19847.2}
\]

Let `V_lambda` be the complete finite CCM space of the same dimension, including
both Fourier-sign sectors, and let

\[
 S_\lambda
 =P_{N_\lambda}\Sigma_{\mu_\lambda}E
 \bigm|_{U_\lambda}.
 \tag{L-19847.3}
\]

Then:

1. the set of supports at which `S_lambda` is singular is locally discrete,
   apart from the explicitly countable exact zeta-cycle supports;
2. on every compact support block,
   
   \[
   S_\lambda^*H_\lambda S_\lambda
   \preceq(\log\lambda)^C G_\lambda;
   \tag{L-19847.4}
   \]
3. for the signed target vector `u_lambda` of `L-19823`,
   
   \[
   \|S_\lambda u_\lambda\|_{H_\lambda}^2
   \ge c\|u_\lambda\|_{G_\lambda}^2
   \tag{L-19847.5}
   \]
   on a relative-`1-o(1)` subset of every sufficiently large block.

Consequently the hypotheses (L-19846.8)--(L-19846.9) hold with

\[
 K_\lambda=(\log\lambda)^C,
 \qquad
 k_\lambda\ge c,
 \tag{L-19847.6}
\]

while no lower singular-value estimate for the complete map is asserted or
needed.

## 2. Mellin evaluation matrix

Choose any analytic exact-constraint basis

\[
 p_{1,\lambda},\ldots,p_{m,\lambda}
 \tag{L-19847.7}
\]

of `U_lambda`. Put

\[
 F_j(\lambda,z)=\mathcal M p_{j,\lambda}(z).
 \tag{L-19847.8}
\]

The finite Fourier nodes are

\[
 z_k(\lambda)=\frac{2\pi k}{\ell_\lambda},
 \qquad
 \ell_\lambda\asymp\log\lambda.
 \tag{L-19847.9}
\]

After fixed real/signed changes of basis, the matrix of `S_lambda` is

\[
 \mathsf S_\lambda
 =\operatorname{diag}
 \left(
 \zeta\!\left(\frac12-iz_k(\lambda)\right)
 \right)
 \mathsf F_\lambda,
 \qquad
 (\mathsf F_\lambda)_{kj}
 =F_j(\lambda,z_k(\lambda)).
 \tag{L-19847.10}
\]

The zeta diagonal is nonsingular away from the exact cycle supports. It remains
to prove that

\[
 \Delta_m(\lambda):=\det\mathsf F_\lambda
 \tag{L-19847.11}
\]

is not identically zero.

## 3. Analyticity and nonidentity

For a fixed packet size `m`, the simple parity-separated prolate eigenspaces and
the two exact anchor repairs depend real-analytically on `lambda` away from
finite eigenvalue crossings. Within a parity sector there are no crossings; a
fixed analytic basis may therefore be chosen. Mellin integration is analytic in
the support and in `z` on the required strip. Hence `Delta_m(lambda)` is
real-analytic.

To show it is not identically zero, keep `m` fixed and send `lambda->infinity`.
The prolate packet converges with all fixed Mellin derivatives on compact
`z`-sets to the corresponding constrained even-Hermite packet. Since
`ell_lambda->infinity`, the nodes in (L-19847.9) coalesce at zero. The confluent
alternant formula gives

\[
 \det(F_j(\lambda,z_k))
 =
 \frac{W(F_{1,\lambda},\ldots,F_{m,\lambda})(0)}
      {\prod_{r=0}^{m-1}r!}
 \prod_{a<b}(z_b-z_a)
 [1+o(1)].
 \tag{L-19847.12}
\]

For the Hermite limit,

\[
 \mathcal Mh_{2n}(z)
 =c_n\Gamma(1/4+iz/2)
 P_n^{(1/4)}(z/2;\pi/2).
 \tag{L-19847.13}
\]

After the two constraint anchors, the remaining polynomial degrees are still
distinct. Their Wronskian equals the product of nonzero leading coefficients,
times a nonzero power of `Gamma(1/4)`. Therefore

\[
 W(F_{1,\infty},\ldots,F_{m,\infty})(0)\ne0.
 \tag{L-19847.14}
\]

Equations (L-19847.12)--(L-19847.14) show that `Delta_m` is nonzero for all
sufficiently large support when `m` is fixed. In particular it is not the zero
analytic function.

Its zeros are locally discrete. Repeating this for the countable packet sizes
used by the cofinal construction yields a countable exceptional support set.
This proves generic exact surjectivity. The determinant may be extremely small;
`R-19843` explains why this is expected and harmless for the quotient-energy
argument.

## 4. Upper map bound

Mellin Plancherel and the Meixner--Pollaczek Christoffel--Darboux estimate give,
for the Hermite packet,

\[
 \sup_{|t|\le C\log\lambda}
 \sum_{j\le m_\lambda}
 |\mathcal Mh_{2j}(t)|^2
 \le(\log\lambda)^C.
 \tag{L-19847.15}
\]

The uniform low-mode prolate-to-Hermite theorem transfers this estimate to
`p_(j,lambda)` for `j=O((log lambda)^2)`. The zeta convexity bound on the same
ordinate window is polynomial in `log lambda`. Summing the sample grid with its
natural Fourier normalization gives

\[
 \|\mathsf S_\lambda c\|_{H_\lambda}^2
 \le(\log\lambda)^C\|c\|_{G_\lambda}^2,
 \tag{L-19847.16}
\]

which is (L-19847.4).

This argument uses only an analysis bound. The exponentially small sampling
directions of `R-19843` affect the inverse, not (L-19847.16).

## 5. Target-line nondegeneracy

The signed target vector uses only the fixed modes `0,2,4,6` up to coefficients
whose ratios converge. Its Mellin transform therefore converges locally
uniformly to one fixed nonzero Hermite-Mellin function

\[
 F_*(t)\not\equiv0.
 \tag{L-19847.17}
\]

Choose a compact real interval `I` on which

\[
 |\zeta(1/2-it)F_*(t)|\ge2c_0
 \tag{L-19847.18}
\]

except at finitely many points, and then choose a positive-length closed
subinterval avoiding them. Local uniform convergence gives

\[
 |\zeta(1/2-it)\mathcal Mu_\lambda(t)|\ge c_0
 \tag{L-19847.19}
\]

there for all large `lambda`.

The Fourier grid has spacing `asymp1/log lambda`, so its naturally normalized
Riemann sum over that subinterval is bounded below by a fixed constant. This
proves (L-19847.5). Exact cycle supports form a countable set and are removed.

## 6. Positive-measure compatibility

The singular set from Section 3 and the exact zeta cycles have measure zero.
The endpoint, alias, and local-Weyl theorems remove `o(1)` relative measure in
each large block. Their intersection with the nonsingular and target-
nondegenerate supports therefore has positive measure.

At such a support:

```text
S_lambda is exactly onto;
S_lambda may be arbitrarily ill-conditioned;
its upper norm is polylogarithmic;
the target image has a fixed lower norm.
```

These are precisely the source-map facts used by `L-19846`.

## 7. Adversarial comparison with the review

The reviewer was correct that qualitative surjectivity does not provide a
controlled right inverse. The additional conclusion drawn in the review -- that
a controlled complete right inverse is therefore required -- is not correct.
`L-19846` shows that complete inverse conditioning is the wrong min--max
quantity.

`R-19843` and this theorem are compatible:

- generic determinant nonzero: **yes**;
- smallest singular value superalgebraically small: **also yes**;
- quotient-energy target/gap transfer: unaffected by that small singular value.

## 8. Exact proof boundary

The most load-bearing analytic inputs are the growing Christoffel bound
(L-19847.15) and the fixed-packet Mellin-derivative convergence used in the
confluent determinant. The determinant argument needs only fixed `m` to prove
nonidentity; no uniform determinant lower bound is used.

This lemma closes the source-map part of the common-frame compatibility. It does
not by itself prove that the **complete source tail** has only one direction
below the `d_6` scale; that is supplied for the declared low packet by
`L-19841/L-19844/L-19845`.

No RH conclusion is claimed by this lemma alone.
