# L-34410 — Fourfold odd-Jordan parameter scaling is a positive product-carry lift

Claim ID: `L-34410`  
Title: The parameter change `tau -> 4 tau` factors into four positive shifted Jordan stages; its row partition is an exact tuple-carry polynomial whose second jet emits the complete sixteenfold Selberg ledger  
Status: **PROPOSED COMPLETE EXACT ALL-ORDER FACTORIZATION AND SECOND-JET THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: positive odd-prime Jordan deformation; finite Dirichlet convolution; atomized carry rows  
Scope: exact denominator lift for the scale-four relative Jordan path; no scalar factorization, dissipative recurrence, or RH conclusion

## 1. General Jordan cocycle

Let `A(s)` be a Dirichlet series for which

\[
J_\tau(s)=\frac{A(s-\tau)}{A(s)}
\]

is defined.  For every positive integer `m`, telescoping gives

\[
\boxed{
J_{m\tau}(s)
=\prod_{r=0}^{m-1}J_\tau(s-r\tau).
}
\tag{L-34410.1}
\]

If `j_tau(n)` is the coefficient sequence of `J_tau`, then shifting the Dirichlet variable multiplies coefficients by a power:

\[
J_\tau(s-r\tau)
\longleftrightarrow
\operatorname{id}^{r\tau}j_\tau.
\]

Therefore (L-34410.1) is the exact coefficient identity

\[
\boxed{
j_{m\tau}
=j_\tau*
 (\operatorname{id}^{\tau}j_\tau)*\cdots*
 (\operatorname{id}^{(m-1)\tau}j_\tau).
}
\tag{L-34410.2}

For the odd-prime Jordan system of PR #345/#346,

\[
J_{{\rm odd},\tau}(n)\ge0
\qquad(n\ge1,\ \tau\ge0),
\]

and multiplication by `n^(r tau)` preserves coefficientwise nonnegativity.  Thus the troublesome parameter `4 tau` is an exact **four-stage positive convolution cascade**:

\[
\boxed{
J_{{\rm odd},4\tau}
=J_{{\rm odd},\tau}*
 (\operatorname{id}^{\tau}J_{{\rm odd},\tau})*
 (\operatorname{id}^{2\tau}J_{{\rm odd},\tau})*
 (\operatorname{id}^{3\tau}J_{{\rm odd},\tau}).
}
\tag{L-34410.3}

No asymptotic approximation or interpolation in the parameter is involved.

## 2. Exact product-carry partition

For one integer row `e=(n,j)`, put

\[
\chi_e(q)
=\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}q\right\rfloor
\in\{0,1\}.
\]

For a finite row and a sequence `f` define

\[
\mathcal F_e(f)=1+\sum_{q\le n}f(q)\chi_e(q).
\tag{L-34410.4}
\]

Let `f_0,...,f_(m-1)` satisfy `f_r(1)=1`.  Expanding the ordered Dirichlet convolution tuple by tuple gives

\[
\boxed{
\begin{aligned}
\mathcal F_e(f_0*\cdots*f_{m-1})
={}&1\\
&+\sum_{\varnothing\ne S\subseteq\{0,\ldots,m-1\}}
 \sum_{\substack{a_r>1\\r\in S}}
 \chi_e\!\left(\prod_{r\in S}a_r\right)
 \prod_{r\in S}f_r(a_r).
\end{aligned}}
\tag{L-34410.5}

Only tuples whose product is at most `n` can contribute.  When all `f_r` are nonnegative, every term in (L-34410.5) is nonnegative.

Applying (L-34410.5) to the four factors of (L-34410.3) gives an exact finite positive proof object for the denominator

\[
F_e^{\rm odd}(4\tau)
=1+\mathcal L_e(J_{{\rm odd},4\tau})
\]

in the relative Jordan ratio.  The denominator is therefore not an opaque rescaled scalar row: it is a complete four-layer product-carry state.

## 3. Exact first two stage jets

Write

\[
J_{{\rm odd},\tau}
=\varepsilon
 +\tau\Lambda_{\rm odd}
 +\frac{\tau^2}{2}C_{\rm odd}
 +O(\tau^3),
\]

where

\[
C_{\rm odd}
=\Lambda_{\rm odd}\log
 +\Lambda_{\rm odd}*\Lambda_{\rm odd}.
\]

For the `r`th shifted factor

\[
f_r(\tau)
=\operatorname{id}^{r\tau}J_{{\rm odd},\tau},
\]

one has exactly

\[
\boxed{f_r(0)=\varepsilon,}
\tag{L-34410.6}
\]

\[
\boxed{f_r'(0)=\Lambda_{\rm odd},}
\tag{L-34410.7}
\]

and

\[
\boxed{
f_r''(0)
=C_{\rm odd}+2r\,\Lambda_{\rm odd}\log.
}
\tag{L-34410.8}

The extra term is the exact derivative of the coefficient multiplier `n^(r tau)`.

## 4. Complete sixteenfold second-jet ledger

Let

\[
P_e=\mathcal L_e(\Lambda_{\rm odd}),
\qquad
S_e=\mathcal L_e(C_{\rm odd}).
\]

Differentiate the four-stage tuple partition.  Singleton stages give

\[
\sum_{r=0}^{3}\mathcal L_e(f_r''(0))
=4S_e
 +12\mathcal L_e(\Lambda_{\rm odd}\log).
\tag{L-34410.9}
\]

Every ordered pair of distinct stages contributes twice the product-carry coefficient. There are six unordered pairs, hence

\[
2\sum_{0\le r<s\le3}
 \mathcal L_e(\Lambda_{\rm odd}*\Lambda_{\rm odd})
=12\mathcal L_e(\Lambda_{\rm odd}*\Lambda_{\rm odd}).
\tag{L-34410.10}
\]

Combining (L-34410.9)--(L-34410.10),

\[
\begin{aligned}
\frac{d^2}{d\tau^2}
 F_e^{\rm odd}(4\tau)\bigg|_{\tau=0}
={}&4S_e\\
&+12\mathcal L_e(\Lambda_{\rm odd}\log)\\
&+12\mathcal L_e(\Lambda_{\rm odd}*\Lambda_{\rm odd})\\
={}&\boxed{16S_e}.
\end{aligned}
\tag{L-34410.11}

Likewise

\[
\boxed{
\frac{d}{d\tau}F_e^{\rm odd}(4\tau)\bigg|_{0}
=4P_e.
}
\tag{L-34410.12}

Thus the factor `16` in the relative curvature is not a formal parameter convention.  It consists exactly of

```text
four individual second-current stages;
twelve shifted logarithmic drifts;
twelve ordered pair-carry collisions.
```

The last two lines recombine into twelve additional complete Selberg sources.  No collision term may be deleted before the relative curvature is formed.

## 5. The source-convolved lift

Let

\[
K_{0,\tau}=\mu*J_{{\rm odd},\tau}.
\]

Attaching the Möbius source to the first stage of (L-34410.3) gives the exact all-order factorization

\[
\boxed{
K_{0,4\tau}
=K_{0,\tau}*
 (\operatorname{id}^{\tau}J_{{\rm odd},\tau})*
 (\operatorname{id}^{2\tau}J_{{\rm odd},\tau})*
 (\operatorname{id}^{3\tau}J_{{\rm odd},\tau}).
}
\tag{L-34410.13}

The final three stages are coefficientwise nonnegative.  Equation (L-34410.13) is the source-complete four-stage denominator coordinate needed by any independent-frequency reflected proof.  The initial Möbius source remains signed and must stay attached to its full tuple ledger.

## 6. Exact scalarization firewall

The positive coefficient factorization does **not** imply

\[
F_e^{\rm odd}(4\tau)
=F_e^{\rm odd}(\tau)^4.
\]

Take the row

\[
e=(8,4).
\]

Because the coefficient of `1*J_odd,tau` at `m` is `odd(m)^tau`, direct prefix subtraction gives

\[
\boxed{
F_{(8,4)}^{\rm odd}(\tau)
=5^\tau+7^\tau-1.
}
\tag{L-34410.14}

Therefore

\[
F_{(8,4)}^{\rm odd}(4)
=5^4+7^4-1
=3025,
\]

while

\[
F_{(8,4)}^{\rm odd}(1)^4
=11^4
=14641.
\]

At the carry level the reason is exact:

\[
\chi_{(8,4)}(5)=\chi_{(8,4)}(7)=1,
\qquad
\chi_{(8,4)}(35)=0.
\]

The scalar fourth power contains an independent `5 x 7` cross term, whereas the correct product-carry partition rejects it because the product modulus lies outside the row.  This is the smallest clean manifestation of the collision geometry which a four-stage proof must retain.

## 7. Consequence for the live relative-curvature problem

The parameter-rescaled denominator now has a finite exact positive lift, and its entire first/second jet ledger is explicit.  The remaining problem is no longer to justify the factor `4 tau` or `16S`.

It is to place the numerator row at `4e` and the complete four-stage denominator tuples of (L-34410.5) in one source-bound independent-frequency Gram so that the unmatched product-carry collisions have dissipative sign.

No scalar product of four row partitions can substitute for that Gram.

## 8. Proof boundary

Closed exactly:

1. the general Jordan cocycle factorization;
2. coefficientwise positive four-stage odd-Jordan lift;
3. the complete tuple-carry partition;
4. every first- and second-jet multiplicity;
5. the source-convolved lift;
6. the exact scalarization counterexample.

Open:

1. the common numerator/denominator collision Gram;
2. reflected dissipative orientation of its unmatched terms;
3. a coefficient-one energy recurrence;
4. RH.
