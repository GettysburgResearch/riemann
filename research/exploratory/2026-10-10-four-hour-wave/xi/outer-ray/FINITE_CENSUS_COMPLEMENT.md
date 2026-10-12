# A complete finite census can protect a finite part of the remaining slab

Status: proposed locality/complement theorem; independent review pending.
Scope: conditional finite-domain companion positivity for actual Xi. The
finite zero census is an explicit primitive input, and the complete infinite
tail is bounded separately. There is no cofinal or RH conclusion.
Dependencies: the actual complete paired product from [THEOREM.md](THEOREM.md),
an authenticated complete simple real-zero census through a stated ordinate,
the actual complete counting bound in
[COARSE_ZERO_COUNT.md](../../heights/COARSE_ZERO_COUNT.md), polynomial
Gauss--Lucas/Rolle and the exact multiplier transport algebra.
What was actually run: the companion proof's finite rational controls; any
additional directed native certificate is separately labeled and must state
its primitive census/count contracts. No census is inferred from a selected
list of zero candidates.
Smallest remaining gap: a uniformly effective version of the protected
polynomial margin and tail budget as the domain grows without bound.

## 1. Primitive complete census and complete tail

Use `Xi(z)=xi(1/2+iz)` and write each opposite pair using its representative
`rho=gamma+i eta`, `gamma>0`, with multiplicity. The classical strip gives
`|eta|<1/2`. Fix `R>=1024`. Assume a **complete** native census proves that
every actual zero with `0<gamma<=R` is real in the Xi coordinate and simple.
Call their positive ordinates `gamma_1,...,gamma_n`. This premise includes
completeness and multiplicities, not merely the existence of these roots.

The exact factorization is

\[
\Xi(z)=P_R(z)p_R(z),\qquad
P_R(z)=\Xi(0)\prod_{j=1}^n(1-z^2/\gamma_j^2),
\tag{C1}
\]

\[
p_R(z)=\prod_{\gamma>R}(1-z^2/\rho^2)^{m_\rho}.
\tag{C2}
\]

Every tail zero has `|rho|>R`, so `p_R` is holomorphic and nowhere zero on
`|z|<R`. The product is the complete actual tail; no zeros off the critical
line are assumed absent above `R`.

Let `N_+(t)` count all actual positive-ordinate zeros with multiplicity, and
suppose the source-qualified bound

\[
N_+(t)\le t\log t\quad(t\ge R)
\tag{C3}
\]

is supplied. The cited wave's coarse count proves (C3) for `R>=1024`, using
actual theta source, classical strip, Jensen/Gamma and its explicitly stated
directed primitive input `xi(1/2)>=1/4`. Those dependencies are inherited;
this packet does not replace them with a synthetic count.

Partial summation, with the convention that the census includes zeros at `R`,
gives

\[
S_R:=\sum_{\gamma>R}\frac{m_\rho}{|\rho|^2}
\le\sum_{\gamma>R}\frac{m_\rho}{\gamma^2}
 =-\frac{N_+(R)}{R^2}
   +2\int_R^\infty\frac{N_+(t)}{t^3}\,dt
\le\frac{2(\log R+1)}R.
\tag{C4}
\]

The complete-count bound makes the endpoint at infinity vanish. Retaining
the negative endpoint gives the optional smaller bound
`2(log R+1)/R-N_+(R)/R^2`. Dropping it as in (C4) is safe; silently changing
the endpoint convention is not.

## 2. Full tail multiplier derivative bounds

Let a compact domain `D` lie in `|z|<=B<R`, and let `S` be any proved upper
bound on `S_R`, such as (C4). Choose the analytic logarithm `ell=log p_R`
with `ell(0)=0`. Paired differentiation gives

\[
\ell'(z)=-\sum_{\gamma>R}\frac{2m_\rho z}{\rho^2-z^2},
\qquad
|\ell'|\le M_1:=\frac{2BS}{1-B^2/R^2}.
\tag{C5}
\]

For every fixed `k>=2`, the derivative of each paired factor is

\[
\frac{d^k}{dz^k}\log(1-z^2/\rho^2)
 =-(k-1)!\left[(\rho-z)^{-k}+(-1)^k(\rho+z)^{-k}\right].
\tag{C6}
\]

Consequently

\[
|\ell^{(k)}|\le
M_k:=\frac{2(k-1)!R^{2-k}S}{(1-B/R)^k}
\quad(k\ge2).
\tag{C7}
\]

For `k=1` the cancellation in (C5) is essential: bounding the unpaired
reciprocals by `sum 1/|rho|` would lose convergence. All differentiated paired
series are locally uniformly absolutely convergent on `|z|<R`.

Define `L_0=1` and recursively

\[
L_{a+1}=\sum_{j=0}^a\binom aj L_{a-j}M_{j+1}
\quad(a\ge0).
\tag{C8}
\]

Leibniz applied to `p_R'=p_R ell'` proves

\[
|p_R^{(k)}/p_R|\le L_k\quad(z\in\mathcal D).
\tag{C9}
\]

In particular `L_1=M_1` and `L_2=M_1^2+M_2`. These bounds retain the entire
spectral tail and are valid even if every tail block permitted by the strip
contains nonreal zeros.

## 3. A finite polynomial has a strict margin on the closed lower half-plane

Fix `0<=r<deg P_R` and `lambda>0`. Let

\[
H=P_R^{(r)},\qquad E_P=H-i\lambda H',\qquad W_P=iE_P/E_P'.
\tag{C10}
\]

The simple real roots of `P_R` and Rolle imply that every nonconstant
derivative through this range has simple real roots. The polynomial
companion argument gives nonzero `E_P,E_P'` and `Re W_P>0` in `Im z<0`.
At every real point,

\[
\operatorname{Re}W_P(x)
 =\frac{\lambda[H'(x)^2-H(x)H''(x)]}
              {H'(x)^2+\lambda^2H''(x)^2}>0.
\tag{C11}
\]

The denominator is positive: `H'` has simple real roots when nonconstant,
and is a nonzero constant otherwise. For the numerator, off the roots of
`H`, its divided form is `H(x)^2 sum_j 1/(x-alpha_j)^2>0`; at a simple root
it is `H'(x)^2>0`. Thus both companions are nonzero also on the real boundary.

On any compact `D` in `Im z<=0`, define the **finite polynomial** margins

\[
c_0=\min_{\mathcal D}|E_P|>0,\quad
c_1=\min_{\mathcal D}|E_P'|>0,\quad
\tau=\min_{\mathcal D}\frac{\operatorname{Re}W_P}{|W_P|}>0,
\quad
V_j=\max_{\mathcal D}|P_R^{(j)}|.
\tag{C12}
\]

The strict statements above and compactness justify these definitions. A
computational certificate must prove explicit bounds for them; sampling does
not certify the compact domain. Coefficient or root enclosures must come from
the authenticated native census, not a fitted polynomial.

## 4. Exact finite acceptance predicate for actual Xi in the slab

Use (C8)--(C9) through `k=r+2`, put `S_0=0`, and define

\[
S_j=\sum_{k=1}^j\binom jk L_kV_{j-k},\quad
\alpha=\frac{S_r+\lambda S_{r+1}}{c_0},\quad
\beta=\frac{S_{r+1}+\lambda S_{r+2}}{c_1}.
\tag{C13}
\]

If the explicit finite predicate

\[
\boxed{\alpha+(1+\tau)\beta<\tau}
\tag{C14}
\]

holds, then the actual companions satisfy

\[
E_{r,\lambda}[\Xi]\ne0,\qquad E_{r,\lambda}'[\Xi]\ne0,
\qquad \operatorname{Re}\frac{iE_{r,\lambda}[\Xi]}
                                   {E_{r,\lambda}'[\Xi]}>0
\quad\text{on the entire }\mathcal D.
\tag{C15}
\]

**Proof.** Apply the full original-function Leibniz identities (T20)--(T21)
to `F=P_R`, `p=p_R`. They give
`E[Xi]=p_R E_P(1+n)` and `E'[Xi]=p_R E_P'(1+d)`, with
`|n|<=alpha`, `|d|<=beta`. Condition (C14) implies `alpha<1`, `beta<1` and
`(alpha+beta)/(1-beta)<tau`. Thus neither actual companion vanishes, and

\[
\operatorname{Re}W[\Xi]
\ge\operatorname{Re}W_P
       -|W_P|\frac{\alpha+\beta}{1-\beta}
\ge|W_P|\left[\tau-\frac{\alpha+\beta}{1-\beta}\right]>0.
\tag{C16}
\]

This uses the complete tail, not a locality assumption about the logarithmic
derivative. It can apply to compact domains touching `y=0`, or lying wholly
inside `0<=y<=1/2`, provided their finite predicate is actually proved.

For `r=0`, the cheaper single-base estimate is available. If a finite
certificate proves `|W_P|<=M` and `Re W_P/|W_P|>=tau`, then valid choices are

\[
\alpha=\lambda M_1,
\qquad\beta=M(2M_1+\lambda(M_1^2+M_2)).
\tag{C17}
\]

The disk `|H/E_P-1/2|<=1/2` on the closed lower half-plane, by continuity
from its interior, and (T14)--(T16) prove (C17). Testing (C14) with (C17)
avoids evaluating `P_R` itself or its potentially very large constant.

## 5. What a successful finite certificate would and would not settle

This is a genuine forward continuation route: it replaces an assumed actual
slab denominator by a finite real-rooted polynomial margin and a complete
tail budget. It gives a precise sufficient finite predicate that can fail
honestly. The actual source is bound through its exact complete product and
the primitive census/count, rather than through source positivity alone.

Even successful certification at a fixed `R,D,r,lambda` gives only (C15) on
that domain. The tail estimates become weaker when `B` approaches `R`, and
the finite polynomial margin need not remain uniformly positive as the
domain or order grows. Finite success is compatible with a hidden off-real
quartet farther up the tail. A complete cofinal theorem, with its source and
coverage inputs, would be a new claim requiring a new proof and review.
