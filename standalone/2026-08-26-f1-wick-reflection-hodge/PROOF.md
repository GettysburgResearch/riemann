# Standalone proof — F1 Boolean/Wick configuration square and reflection-Hodge frontier

## Frozen packet

```text
F1 parent:
  PR #730
  d385097bfcd19ab6f9015b522eacd5b97bc7e1b5

Boolean parent:
  PR #719
  4146f81e7237d41e2e4a0cb1737511266683e980

half-source / reflection parent:
  PR #751
  356fbf29e958e2ea067bfe5ef912b1f68d0334c6
```

The classical Riemann Hypothesis is not assumed and is not proved here.

## Theorem A — Chow equals Boolean/Wick

For a finite labelled prime set,

\[
\mathscr C=\mathbf Q[h_p]/(h_p^2).
\]

The monomial identity

\[
h_Ah_B=\mathbf1_{A\cap B=\varnothing}h_{A\cup B}
\]

is exactly disjoint-support convolution.  Therefore

\[
\left[\prod_p(1-h_p/2)\right]^2=\prod_p(1-h_p),
\]

and the Boolean half-source identity \(h\star h=\mu_{\rm sf}\) is an ordinary
square in \(\mathscr C\).

## Theorem B — the canonical pair owner is the incidence Green

For a degree-\(k\) monomial, pair marking followed by recombination counts
every unordered pair:

\[
m_2\delta_2=\binom{k}{2}I.
\]

Hence

\[
\mathcal G_2=\delta_2\binom N2^{-1}
\]

is a right inverse.  The Beta identity

\[
2\int_0^1(1-\theta)\theta^{k-2}\,d\theta
=\binom{k}{2}^{-1}
\]

realizes it exactly.

Among all pair allocations summing to \(c\), Cauchy gives minimum squared norm
\(|c|^2/\binom{k}{2}\), uniquely at the equal allocation.

Let \(B\) be the unsigned vertex-edge incidence matrix of \(K_k\).  Since

\[
BB^T=(k-2)I+J,
\]

pair space splits orthogonally into constant, zero-sum star, and
\(\ker B\) primitive components.  The equal allocation is constant.  For one
edge delta, direct inversion of \(BB^T\) gives squared components

\[
\binom{k}{2}^{-1},\qquad \frac2k,\qquad\frac{k-3}{k-1}.
\]

Thus the concentrated owner creates the star and primitive debts.

## Theorem C — open configuration square plus diagonal strata

Put

\[
\mathfrak G_{U,\theta}=\Pi\star T_\theta\mathfrak f_U.
\]

Theorem B gives

\[
\mathfrak B_U^{\rm eq}
=\int_0^1(1-\theta)\mathfrak G_{U,\theta}^2\,d\theta.
\]

The square is taken in the square-zero Chow algebra, so its two supports are
disjoint.  Physical realization gives the Wick–Mellin square
\(\mathcal J_U^\diamond\).

Ordinary multiplication partitions into disjoint and intersecting support
pairs.  Therefore

\[
\mathcal J_U=\mathcal J_U^\diamond+\mathcal C_U.
\]

A shared prime has exponent \(2\), \(3\), or \(4\), according to whether it is
owner/owner, owner/core, or core/core.  The frozen parent closes these
repeated/higher-prime-power strata after the fixed observation.

## Theorem D — reflection Hodge signature

For the ordinary half-field, reflection \(R_xf(u)=f(x-u)\) is a self-adjoint
involution.  Its projections satisfy

\[
\mathcal E_U+\mathcal O_U=\mathcal N_U,
\qquad
\mathcal J_U=\mathcal E_U-\mathcal O_U.
\]

Because

\[
\mathcal D_{\rm out}
=\frac12D(D-1)(5D+3/2)(2D-1)
\]

contains \(D\),

\[
\mathcal D_{\rm out}\mathcal J_U
=-2\mathcal D_{\rm out}\mathcal O_U.
\]

Also

\[
\mathcal O_U(x)
=\frac14\int_0^1(1-\theta)\int
 |f_\theta(u)-f_\theta(x-u)|^2\,du\,d\theta.
\]

Thus the remaining current is the differential variation of a nonnegative
anti-invariant Hodge energy.

For a frozen finite source block,
\(q_U=\mathcal O_U-\mathcal N_U/2=-\mathcal J_U/2\) is compactly supported.
Hence

\[
\nu_U=\mathcal D_{\rm out}q_U
\]

has total mass zero.  Its positive and negative Jordan masses are equal and
each is half its total variation.  At the four roots

\[
0,\ 1,\ -3/10,\ 1/2
\]

of the detector polynomial, compact integration by parts gives the four
vanishing exponential moments.

Therefore the frozen reflection premise is exactly

\[
\|\nu_U\|_{\rm TV}=Y^{o(1)}.
\]

## Theorem E — TP3 fails

Let \(t=2^{1/8}\), and use the ordered points

\[
u=(5L/4,3L/2,2L),\qquad x=(0,L/4,L/2).
\]

The exact half-kernel matrix has determinant

\[
-8t^4(t-1)^3(t+1)(t^4+1)<0.
\]

Thus the kernel is `TP2` but not `TP3`.

## Implication frontier

Define `F1VAR105460` to be the subpower total-variation estimate in Theorem D.
Then, at the frozen source and boundary convention,

```text
F1VAR105460
  <=> REFSIG106150
  <=> SFSC106150
  -> WKSFSC106150
  -> BCI102990
  -> RH.
```

Only the identities and reductions before the first premise are proved in this
packet.  `F1VAR105460`, `BCI102990`, and RH remain open.
