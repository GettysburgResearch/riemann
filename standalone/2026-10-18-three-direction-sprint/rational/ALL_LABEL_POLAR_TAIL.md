# Quantitative principal-functional control for every squarefree label

**PROPOSED source-qualified corollary.** This bounds the exact principal
functional for ALL squarefree numerator labels, including those larger
than the response cutoff. It does not identify these functionals with
the entire spectral or Poisson operator. Its nonconstant complement
remains OPEN.

The same bound also applies to the base fixed section's labels whose
nonzero valuations are at most FOUR, as specified in Section 4. It
does NOT apply uniformly to arbitrary sixth-free labels.

Use `ANNULAR_PROFILE_DEBIAS.md`, with the same actual compact annular
Mobius head b_kappa, response cutoff G<=D^(1/2-delta), and modified
coefficients b_new,kappa=b_kappa+t_kappa. For EVERY good squarefree g,
not only those with Ng<=G, define

    F_g(kappa)=sum_(g|a) b_new,kappa(a)v(a)/Na.          (1)

This sum is finite. The exact response equations say F_g=0 whenever
Ng<=G. The proven principal functional from
`../eisenstein/GROWING_RESIDUE_DEBIAS.md`, Section 3, is, apart from
its displayed common scalar and the bounded factor v(R),

    L_R(kappa)=sum_(g|R) c(g)F_g(kappa),
    c(g)=product_(p|g)((Np)^(-1)-(Np)^(-2)),           (2)

for a good squarefree numerator label R. In particular |c(g)|<=1/Ng.
No nonconstant finite Fourier transform is replaced by (2).

For each fixed j and every epsilon we claim, uniformly in every
polynomially bounded good squarefree label R,

    |partial_kappa^j L_R(kappa)|
       <<_epsilon (1+|kappa|)^A
          D^(beta-1)G^(-beta-1)(DGR)^epsilon.          (3)

The height powers in (3) can be integrated against the ORIGINAL
common-profile Fourier density, exactly as in the annular comparison.

## 1. An exact response bound beyond the solved index set

Let B_(g,h) be the positive tail-response expression even when g>G.
Its complete fixed-field ideal count gives the elementary uniform bound

    |B_(g,h)|
      =sum_([g,h]|a)mu(a)^2 W(Na/D)/Na
      << 1/N[g,h].                                   (4)

Indeed the fixed annulus has Na comparable to D. If the sum is nonempty,
N[g,h]<=C D, and there are O(D/N[g,h]) possible quotient ideals.
If that inequality fails the sum is empty. The same estimate follows
for a bounded fixed tail profile of either sign by taking its absolute
value. All bad-prime deletions only remove summands.

Using (4) and the annular infinity resource yields, for any g,

    |sum_(Nh<=G) B_(g,h)partial_kappa^j xi_h(kappa)|
       << (1+|kappa|)^A D^(beta-1)G^(1-beta)(DG)^epsilon
                   /(Ng) * sum_(Nh<=G) N(g,h)/Nh.

The final divisor-harmonic sum is at most (Ng*G)^epsilon. To see this,
expand N(g,h)=sum_(d|g,d|h)phi(d); its inner harmonic sum is
O(log(2G)/Nd), and sum_(d|g)phi(d)/Nd is divisor-bounded. Including
the complete original-head response from the annular Mellin estimate
therefore gives

    |partial_kappa^j F_g(kappa)|
       << (1+|kappa|)^A (DgG)^epsilon
          [D^(beta-1)(Ng)^(-beta)
              +D^(beta-1)G^(1-beta)/(Ng)].             (5)

This is an absolute bound for every omitted response; no uniform
conditioning theorem for an enlarged matrix is being assumed.

## 2. Sum the entire actual principal functional

In (2) every divisor with Ng<=G is EXACTLY zero. For every remaining
divisor multiply (5) by |c(g)|<=1/Ng. Both terms are at most

    (1+|kappa|)^A D^(beta-1)G^(-beta-1)(DgG)^epsilon:

the first uses (Ng)^(-beta-1)<=G^(-beta-1), and the second uses
G^(1-beta)(Ng)^(-2)<=G^(-beta-1). The number of divisors of R is
R^epsilon. This proves (3), with all original shared-prime local
constants in (2) retained. It also covers R with arbitrarily many
small prime factors. No assumption that R itself is at most G enters.
For R<=G the functional is of course exactly zero, a stronger statement.

## 3. Explicit budgets and scope

At beta=7/8 the full functional bound is

    |L_R(kappa)| << (1+|kappa|)^A
                         D^(-1/8)G^(-15/8)(DGR)^epsilon. (6)

Choosing G=D^(1/5), whose complete mixed-norm comparison costs only
U^(1+epsilon), gives D^(-1/2+epsilon). Choosing instead the adaptive
U^(6/5) comparison budget G=U^(4/25)D^(1/5) gives

    |L_R(kappa)| << (1+|kappa|)^A
                         U^(-3/10)D^(-1/2)(UDR)^epsilon. (7)

This holds simultaneously for EVERY squarefree R in any fixed
polynomial range. At D=U it is U^(-4/5+epsilon), and at D=U^(3/2)
it is U^(-21/20+epsilon). It is a bound for the actual scalar
functional (2), not a unit-normalized row or column projection.

The full polar expression in the cited source still contains its
explicit X^(5/6), R^(-1/6), profile Mellin value, and fixed constants.
Those factors must be restored when using (3); they are not silently
bounded by one. Nor does a uniform bound for (2) authorize summing
an unbounded family of allegedly orthogonal modes. Its actual operator
measure, overlaps, nonconstant finite transforms and all continuous
remainders still require a separate full calculation. No full mixed
mean or zero-free improvement follows from this corollary alone.

## 4. Valuations through four, and the genuine exponent-five gate

For the base fixed section only, the exact local calculation in
`../eisenstein/RESIDUE_VALUATIONS.md` gives the polar scalar

    sum_(g|rad R) c_R(g)F_g,
    c_R(g)=product_(p|g)(L_(R,p)-1),
    L_(R,p)=1/v(p)  for 1<=ord_p R<=4,
             Np/v(p) for ord_p R=5.                   (8)

If every nonzero valuation is at most four, (8) is EXACTLY the
coefficient c(g) in (2), since 1/v(p)-1=1/Np-1/(Np)^2.
Repeating the proof over g|rad R establishes (3), (6), and (7)
unchanged for ALL such R, with no radical cutoff. Exact vanishing
holds when N(rad R)<=G, rather than only when NR<=G. The full scalar
outside (8), including (NR)^(-1/6), is still restored separately.
This includes arbitrary fourth-power numerator labels f^4. It uses
the BASE fixed section's local polar formula; no different numerator
filter or growing twist is silently added.

At a prime of valuation FIVE the coefficient L_(R,p)-1 is instead
of order Np, so |c_R(g)|<=1/Ng is FALSE. The exact constraints still
kill labels with N(rad R)<=G, but the quantitative uniform tail
argument of Section 2 no longer applies. No all-sixth-free-label
suppression follows from this corollary. Exponent-five branches,
all operator measures and the full nonpolar covariance remain open.
The distinct `ALL_SIXFREE_POLAR_ENERGY.md` restores the TRUE label
weight and proves weighted scalar and positive coordinate-energy
bounds including exponent five. It does not extend the unweighted
uniform-functional claim in this note or estimate a full operator.
