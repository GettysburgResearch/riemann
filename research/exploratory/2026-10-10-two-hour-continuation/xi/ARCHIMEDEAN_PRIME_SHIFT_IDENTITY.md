# Exact shifted logarithmic moments from Gamma and positive prime coefficients

Status: proposed complete source identity and finite directed tail envelope.
Scope: actual Xi, each fixed integer order, an imaginary-axis shift t>1/2,
and the absolutely convergent Euler half-plane. No all-order sign or cofinal
census theorem is inferred from the positivity of the prime coefficients.
Exact dependencies: the literal completed-zeta formula, its functional
equation, the absolutely convergent Euler logarithm for Re s>1, and
[SHIFTED_COMPLETE_MOMENTS_V2.md](SHIFTED_COMPLETE_MOMENTS_V2.md).
What was actually run: analytic derivation; no additional native high-order
experiment is claimed by this document.
Smallest remaining gap: a source inequality controlling the complete
Gamma-minus-prime coefficients after real-root subtraction, uniformly enough
to make count-free exclusion guards pass cofinally.

## AP1. Literal actual-source decomposition

Fix t>1/2 and write

\[
 s(w)=\tfrac12+\sqrt{t^2-w},\qquad s_0=\tfrac12+t>1,
 \quad r_t(w)=t-\sqrt{t^2-w},
\]

where the square root is positive at w=0. Set

\[
 A(s)=\frac{s(s-1)}2\,\pi^{-s/2}\Gamma(s/2),\qquad
 G_k(t)=-k[w^k]\log A(s(w)),\qquad
 P_k(t)=k[w^k]\log\zeta(s(w)).
 \tag{AP1}
\]

All logarithms take their real branches at the positive expansion center.
Their constant terms are irrelevant to the displayed coefficients. For
each fixed integer k>=1, the complete shifted logarithmic moment is exactly

\[
 C_k(t)=G_k(t)-P_k(t).
 \tag{AP2}
\]

Indeed xi(s)=A(s)zeta(s), and functional symmetry identifies
`Xi(i sqrt(t^2-w))=xi(s(w))`. Applying `-k[w^k]` gives AP2 with precisely
the sign shown. The complete even product then identifies C_k with the
multiplicity-preserving sum of `(rho^2+t^2)^(-k)`. No finite zero census
is involved in this identity.

## AP2. Positive prime coefficients at every fixed order

The exact Taylor coefficients of the shift are

\[
 r_t(w)=\sum_{h\ge1}d_h(t)w^h,\qquad
 d_h(t)=\frac{\binom{2h}{h}}{4^h(2h-1)}t^{1-2h}>0.
 \tag{AP3}
\]

For q>0 define `E_k(q,t)=[w^k]exp(q*r_t(w))`. Differentiating this
exponential gives the finite exact recurrence

\[
 E_0(q,t)=1,\qquad
 E_k(q,t)=\frac{q}{k}\sum_{h=1}^k h\,d_h(t)E_{k-h}(q,t)>0.
 \tag{AP4}
\]

For Re s>1 the absolutely convergent Euler logarithm is

\[
 \log\zeta(s)=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-s},
\]

where the coefficient is 1/m at n=p^m and zero otherwise. Consequently

\[
 P_k(t)=k\sum_{n\ge2}\frac{\Lambda(n)}{\log n}
              n^{-s_0}E_k(\log n,t)>0.
 \tag{AP5}
\]

This is a statement about a complete literal prime-source coefficient,
not the positivity of the complete moment C_k. The prime term enters C_k
with a MINUS sign.

To justify coefficient extraction, choose any radius
`0<r<t^2-1/4`. Since AP3 has nonnegative coefficients,
`Re s(w)>=s_0-|r_t(w)|>=1/2+sqrt(t^2-r)=:sigma_r>1` for |w|<=r.
The Euler logarithm therefore converges absolutely and uniformly on that
disk. The identity and termwise coefficient extraction are valid there.
Every summand in AP5 is nonnegative, so monotone convergence also preserves
the sign of the full coefficient sum.

## AP3. A finite prime-power envelope with an explicit complete tail

Let N>=2 be an integer and define the finite literal prime-power sum

\[
 P_{k,N}(t)=k\sum_{2\le n\le N}\frac{\Lambda(n)}{\log n}
                     n^{-s_0}E_k(\log n,t).
\]

For any radius r as above, positivity of every coefficient implies that
the kth coefficient of the remaining series is at most its value at r
divided by r^k. Using `0<=Lambda(n)/log n<=1` and the elementary integral
bound for the tail of a decreasing power gives

\[
 0\le P_k(t)-P_{k,N}(t)
       \le \frac{k}{r^k}\sum_{n>N}n^{-\sigma_r}
       \le \frac{k}{r^k}\frac{N^{1-\sigma_r}}{\sigma_r-1}.
 \tag{AP6}
\]

The envelope retains the complete prime tail. A finite directed computation
may enclose the Gamma coefficient G_k, all finite prime-power terms and
the AP6 endpoint with convergent interval arithmetic. Primality and exact
prime-power weights must be authenticated in that finite computation;
ordinary decimal evaluations are not directed endpoints.

For a selected real-root inventory, let each actual selected root lie in
the authenticated interval [l_j,u_j]. The full residual moment then satisfies

\[
 T_k(t)\le G_{k,\mathrm{hi}}(t)-P_{k,N,\mathrm{lo}}(t)
                        -\sum_j(u_j^2+t^2)^{-k}.
 \tag{AP7}
\]

The sign of the prime term makes a finite LOWER prime endpoint useful for
the residual UPPER endpoint. A complete lower residual endpoint may instead
use the finite upper prime endpoint plus AP6. Every real-root uncertainty
and every native coefficient uncertainty remains in these interval bounds.
Combining an authenticated AP7 with the global phase guard and strict
exclusion predicate of SM6–SM7 gives a finite count-free census. AP7 alone
does not prove that its upper endpoint is small enough to pass.

## AP4. The cancellation that a separate positive estimate loses

Put `w_1=t^2-1/4>0`. On the chosen square-root branch, s(w_1)=1 and
`s'(w_1)=-1`. Near w_1,

\[
 A(s(w))=(w_1-w)\,a(w),\qquad
 \zeta(s(w))=(w_1-w)^{-1}\,b(w),
 \tag{AP8}
\]

where a and b are analytic and nonzero in a sufficiently small neighborhood.
The elementary s(s-1) factor has its simple zero, while zeta has its
simple pole of residue one. The two logarithmic singularities therefore
cancel exactly in the COMPLETED source:

\[
 \log A(s(w))=\log(w_1-w)+\log a(w),\qquad
 \log\zeta(s(w))=-\log(w_1-w)+\log b(w).
 \tag{AP9}
\]

Their separately displayed singular contributions to both G_k and P_k
are `w_1^(-k)`, with equal sign and size. They cancel in G_k-P_k.
AP9 states the exact local singular-part identity; it does not assert that
these parts alone are an asymptotic estimate for each complete coefficient.
The completed xi is regular and nonzero at s=1. At w=t^2, the square-root
branch point of the separate composition also disappears from completed
xi because the functional equation makes xi(1/2+u) even in u.

Thus the positive Euler coefficient family does identify a literal actual
arithmetic contribution, but treating Gamma and prime envelopes separately
does not automatically preserve the cancellations that govern the complete
zero moments. Proving a useful uniform lower prime contribution together
with a sharp Gamma upper contribution is a substantive source estimate.
The exact theta positivity and the Euler identity do not already prove it.

The universal Hausdorff or Hankel criterion can express the missing
real-spectrum conclusion without simplicity. A cofinal one-occurrence
strict-sign census additionally forces simplicity. This fixed-order
Gamma/prime identity establishes neither global statement.
