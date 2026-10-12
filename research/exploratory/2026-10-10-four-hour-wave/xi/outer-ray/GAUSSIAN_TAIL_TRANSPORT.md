# Absorb the benign quadratic tail before pricing the residual

Status: proposed analytic extension of the finite-census complement theorem.
Scope: a complete simple real-zero census through `R`, a complete classical
strip outside that census, and protected compact domains `|z|<=B<R`.
The resulting native companion sector is finite-domain and conditional on
explicit finite Gaussian-family margins. No cofinal/RH conclusion is made.
Dependencies: (C1)--(C4), the same source-qualified complete counting input,
elementary paired-product algebra, real polynomial interlacing and the exact
full multiplier transport formulas. The Gaussian base is an auxiliary
Laguerre--Pólya function; its inverse Fourier source is not asserted positive.

## 1. The exact quadratic coefficient of the complete tail is benign

Keep the complete factorization `Xi=P_R p_R` from
[FINITE_CENSUS_COMPLEMENT.md](FINITE_CENSUS_COMPLEMENT.md), and suppose the
complete zero strip is `|Im rho|<=A<R`. Write the tail representative as
`rho=gamma+i eta` with `gamma>R` and `|eta|<=A`, and define

\[
a_1=\sum_{\gamma>R}m_\rho\rho^{-2}.
\tag{G1}
\]

Absolute convergence permits grouping conjugate terms. Each real tail pair
contributes positively. Each nonreal conjugate block contributes

\[
\rho^{-2}+\overline\rho^{-2}
 =\frac{2(\gamma^2-\eta^2)}{(\gamma^2+\eta^2)^2}>0.
\tag{G2}
\]

Consequently `a_1` is real, `0<=a_1<=S_R<=S`. No real-rootedness of the tail
was assumed: `gamma>R>A` is enough for this sign. For actual Xi the tail is
infinite, so `a_1>0`, but including zero in its protected parameter interval
is convenient and safe.

The exact native decomposition is

\[
\Xi(z)=G_{a_1}(z)q(z),\qquad
G_a(z)=e^{-az^2}P_R(z),\qquad q(z)=e^{a_1z^2}p_R(z).
\tag{G3}
\]

On `|z|<R`, choose `h=log q` with `h(0)=0`. Its Taylor series starts at
degree four: the quadratic tail term has been absorbed exactly, rather
than approximated or omitted.

## 2. The complete residual has two extra powers of the cutoff

From the paired product,

\[
h'(z)=-2z^3\sum_{\gamma>R}
                 \frac{m_\rho}{\rho^2(\rho^2-z^2)},
\tag{G4}
\]

\[
h''(z)=-2z^2\sum_{\gamma>R}
                 \frac{m_\rho(3\rho^2-z^2)}
                      {\rho^2(\rho^2-z^2)^2}.
\tag{G5}
\]

Thus on `|z|<=B<R`, valid complete-tail bounds are

\[
|h'|\le J_1:=\frac{2B^3 S}{R^2(1-B^2/R^2)},
\quad
|h''|\le J_2:=
\frac{2B^2(3+B^2/R^2)S}{R^2(1-B^2/R^2)^2},
\tag{G6}
\]

\[
|q'/q|\le J_1,\qquad |q''/q|\le J_1^2+J_2.
\tag{G7}
\]

For example, (G4) is bounded using
`sum m|rho|^-4<=S/R^2` and `|rho^2-z^2|>=|rho|^2-B^2`.
For (G5), extract `2B^2`, bound its remaining numerator by
`3|rho|^2+B^2`, and use the same fourth-power sum. Every tail block is still
included. Compared with (C5)/(C7), the first two residual bounds gain the
displayed factor `R^-2` for fixed `B`; the quadratic effect remains present
in the auxiliary base parameter `a_1`.

For higher derivatives, use (C6)--(C7) unchanged after `k>=3`, since the
absorbed quadratic has zero derivatives at those orders. Feeding those
bounds together with `J_1,J_2` into the Bell recursion (C8) gives full
`q^(k)/q` bounds for the all-fixed-order Leibniz transport law.

## 3. Every Gaussian base has a strict companion sector, including its real boundary

Let `P=P_R` have its paired simple real roots and positive value `P(0)`.
For each `a>=0`, fix `0<=r<deg P` and `lambda>0`, and put

\[
H=G_a^{(r)},\qquad E_a=H-i\lambda H',\qquad W_a=iE_a/E_a'.
\tag{G8}
\]

**Lemma.** Both companions are nowhere zero on `Im z<=0`, and
`Re W_a>0` there. The assertions hold for every fixed `a,r,lambda` in the
stated range.

For the open lower half-plane, approximate `G_a` by
`P(z)(1-az^2/n)^n` when `a>0`; these are real-rooted polynomials and converge
with every fixed derivative locally uniformly. For `a=0` use `P` itself.
The polynomial companion proof, Hurwitz and harmonic strictness from the
outer theorem apply without a Fourier-source premise: on the imaginary axis
`G_a(-iy)=e^(ay^2)P(-iy)` has strictly positive even power-series coefficients.
Its every fixed derivative through the stated range is strictly positive in
the real variable `y>0`. Therefore the same `i^r A_r` anchors exclude zero
limits and make the logarithmic-derivative sign strict.

The boundary proof is also elementary. Write

\[
G_a^{(j)}(z)=e^{-az^2}Q_j(z),\qquad
Q_0=P,\qquad Q_{j+1}=Q_j'-2azQ_j.
\tag{G9}
\]

For `a=0`, Rolle gives simple real roots for every nonconstant `Q_j` in the
needed range. For `a>0`, if `Q_j` has simple real roots `alpha_k`, then

\[
Q_{j+1}/Q_j=\sum_k(z-\alpha_k)^{-1}-2az.
\tag{G10}
\]

On each interval between roots the real expression decreases strictly from
`+infinity` to `-infinity`. On the two exterior intervals it likewise has
exactly one zero, by its limits at the pole and at infinity. Thus it has
exactly `deg Q_j+1` distinct simple real zeros, equal to the degree of
`Q_{j+1}`. Induction proves the assertion for all `j` when `a>0`.

Consequently `H,H'` never have a common real zero, and neither do `H',H''`.
If `H'` is a nonzero constant, this last assertion is immediate. Both
companions are therefore nonzero on the boundary. Off the roots of `H`,

\[
H'^2-HH''=H^2\left[2a+\sum_{\alpha\in Z(Q_r)}(x-\alpha)^{-2}\right]>0,
\tag{G11}
\]

and at a root it equals `H'^2>0`. The real-boundary formula (C11) makes
`Re W_a>0`, completing the proof. The Gaussian order-two base is handled
by its real-rooted polynomial approximants; applying the order-below-two
Fourier theorem to it directly would be unjustified.

Joint continuity now gives strictly positive protected margins on any
compact `D in {Im z<=0}` for the **whole finite parameter family**
`0<=a<=S`, with `r,lambda` fixed. A directed certificate must enclose that
parameter interval as well as the full complex domain; choosing a fitted
value for the unknown `a_1` would lose the native source binding.

## 4. Explicit order-zero acceptance predicate

For `r=0`, suppose a finite certificate proves on each protected compact
box, uniformly for all `a in[0,S]`,

\[
|W_a|\le M,\qquad
\operatorname{Re}W_a/|W_a|\ge\tau>0.
\tag{G12}
\]

The same closed lower-half-plane disk bound for `H/E_a` holds by continuity.
Apply the exact single-base multiplier identity to `Xi=qG_(a_1)`, now with

\[
\alpha=\lambda J_1,\qquad
\beta=M[2J_1+\lambda(J_1^2+J_2)].
\tag{G13}
\]

The strict finite predicate

\[
\boxed{\alpha+(1+\tau)\beta<\tau}
\tag{G14}
\]

proves both actual companions nonzero and their quotient in the strict right
half-plane on that box. Its proof is exactly (C14)--(C17), applied to the
**actual** unknown coefficient `a_1` inside the fully protected family.

For higher fixed orders, use the full original-function Leibniz formulas
with `F=G_(a_1)` and `p=q`, together with the corresponding complete Bell
bounds and finite Gaussian-family derivative/denominator margins. The
single-base order-zero formula alone is not a higher-order transport theorem.

This absorbs a known benign part of the complete source tail and prices the
remaining part. It does not improve the primitive real-zero census or
produce an unbounded protected domain. Hidden nonreal zeros above `R` remain
permitted, and their effect has been retained in the residual budget.
