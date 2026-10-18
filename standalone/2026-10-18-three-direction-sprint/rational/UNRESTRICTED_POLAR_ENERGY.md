# True-weight principal-coordinate energy for unrestricted numerator labels

**PROPOSED source-qualified theorem.** This extends
`ALL_SIXFREE_POLAR_ENERGY.md` to EVERY good numerator label R, including
all sixth-power replicas. It concerns the exact Type-I principal
coordinates in the BASE fixed section. It does not estimate their
nonconstant Type-I or adjoint contour remainders, and does not assert
that a short collection of coordinates is a complete row frame.

The reciprocal, growing-Gram, TWO-PLAIN and common-profile inputs are
those pinned in `ANNULAR_PROFILE_DEBIAS.md`. The base section's full
residue periodicity and cusp-density formula are the explicitly
imported ones in `../eisenstein/RESIDUE_VALUATIONS.md`. In particular
we do not assume that the PRIMITIVE residue itself is invariant when
a new sixth-power prime is inserted.

Write e_p=ord_p R=6*k_p+r_p, 0<=r_p<=5. Put

    R_red=product_p p^(r_p),  r=rad R,
    v(r)=product_(p|R) (Np)^2/((Np)^2+Np-1).

The radical includes primes of valuation a POSITIVE multiple of six,
even when those primes are absent from R_red.

## 1. Exact local principal factor with every valuation retained

For any good modulus A, the base full-residue cusp-density calculation
gives

    Delta(A)=1/NA sum_(t^6|A) phi(t^6)/(Nt)^5.

At p^e, the exact telescoping sum is q^(floor(e/6)), q=Np, so

    Delta(p^e)=q^(-e+floor(e/6)).                      (1)

The primitive weight w=1*h, h(p)=-1/(q+1), changes this density by
the factor v(rad A), times the fixed global scalar Z_S. This is
because inserting the squarefree divisor h changes no existing
prime valuation in the least common multiple; absent primes give
their usual convergent factors.

For squarefree a, equation (1) therefore gives

    Delta(aR)= (Na NR)^(-1) product_p q^(k_p)
                               product_(p|a,r_p=5)q. (2)

When r_p=0 and e_p>0 there is no extra q upon inserting p|a;
this case must not be confused with p absent from R. Combine (2)
with the shared-prime primitive factor
v(rad(aR))=v(a)v(r)/v((a,r)). The exact principal scalar for the
modified annular head is

    L_R=sum_(g|r)c_R(g)F_g,
    c_R(g)=product_(p|g)c_(r_p)(p),
    c_j(p)=1/q-1/q^2 for j in {0,1,2,3,4},
    c_5(p)=q-1/q.                                    (3)

Here F_g is the SAME omitted response from `ALL_LABEL_POLAR_TAIL.md`.
The outer principal factor is now

    X^(5/6) (NR_red)^(-1/6) v(r) Phihat(5/6).          (4)

Indeed the factor product q^(k_p) in (2) converts
(NR)^(-1/6) exactly to (NR_red)^(-1/6). It does NOT remove v(r)
at a new sixth-power prime. Equations (1)--(4) reconstruct all local
weights before asserting any periodicity shortcut for a primitive
series.

## 2. Weighted counting includes all sixth-power replicas

The complete positive elementary count is

    sum_(NR<=Z) (NR_red)^(-1/3) << Z^(2/3).            (5)

To prove it, uniquely write R=t^6 R_red, with R_red sixth-free and
NO coprimality condition between t and R_red. The inner sixth-free
count is at most the unrestricted ideal sum through Z/(Nt)^6,
weighted by norm^(-1/3), hence at most
(Z/(Nt)^6)^(2/3). The complete t sum is sum_t (Nt)^(-4)<infinity.
This proves (5), with all repeated primes retained.

For a fixed squarefree g, fix the FULL positive exponents e>=1 at
its primes. Their local principal weights in (3) have the exact
summable resource

    sum_(e>=1) |c_(e mod 6)(p)|^2 q^(-2*e/3-(e mod 6)/3)
                                                    << q^(-3). (6)

For residues one through four the leading term is at most q^(-3).
For residue five, c_5^2<=q^2 and its first exponent costs q^(-5),
again q^(-3). For residue zero the first positive exponent is SIX,
so it starts at q^(-6). Increasing e by six contributes a factor
q^(-4), giving a convergent geometric series in every branch.

After fixing these g-supported exponents, apply (5) to the remaining
label ideal. Its count supplies Z^(2/3)/(NR0)^(2/3), while the
fixed reduced-prime weight supplies (N(R0)_red)^(-1/3). Thus (6)
gives the COMPLETE unrestricted-label bound

    sum_(NR<=Z,g|rad R) (NR_red)^(-1/3)|c_R(g)|^2
                         <<_epsilon Z^(2/3)(Ng)^(-3+epsilon). (7)

Divisor Cauchy, the exact zeros F_g=0 for Ng<=G, and the same
omitted-response integral as before prove

    sum_(R good,NR<=Z)(NR_red)^(-1/3)|v(r)L_R|^2
       << (1+|kappa|)^A (DGZ)^epsilon
                     Z^(2/3)D^(2*beta-2)G^(-2*beta-2).  (8)

There is no sixth-free restriction on R in (8). Every valuation-zero
residue class at a positive sixth-power exponent, every exponent-five
branch and every common prime of t,R_red is included. Fixed kappa
derivatives obey the same estimate. The original common-profile
Fourier density integrates the polynomial height cost.

The uniform WEIGHTED scalar bound also extends unchanged:

    (NR_red)^(-1/6)|v(r)L_R|
       << (1+|kappa|)^A (DGR)^epsilon
                            D^(beta-1)G^(1/6-beta).   (9)

At each prime in g, (NR_red)^(-1/6)|c_R(g)| contributes at most
q^(1/6) in the residue-five case and at most one otherwise. Therefore
the proof of the weighted scalar estimate in the sixth-free note
applies literally. The UNWEIGHTED uniform scalar estimate is still
not claimed for labels with residue-five primes.

## 3. Actual adjoint normalization for the matched fixed section

Use the exact primitive adjoint of
[rStation paper 10/v2, (7.1)--(7.3)](https://rstation.ai/problems/riemann_hypothesis/papers/10).
Its residue term is U^(1/6)*w_hat(2/3)*rho_prim(nR), on unrestricted
good columns n. Pair it with the normalized common-product-profile
mixed coefficient of product length L=DN. The Type-I principal
MAINTERM in the matched base fixed section is exactly

    M_R=C U^(1/6)L^(1/3)
                      (NR_red)^(-1/6)v(r)L_R.         (10)

The scalar C contains the fixed row and Type-I Mellin values and
local constants. The power L^(1/3) is L^(5/6) from the Type-I
principal mean times L^(-1/2) from the actual mixed coefficient.
Hence (8) yields the source-correct complete bound

    sum_(R good,NR<=K)|M_R|^2
       << (UDGK)^epsilon U^(1/3)L^(2/3)K^(2/3)
                              D^(2*beta-2)G^(-2*beta-2). (11)

At beta=7/8,G=D^(1/5), the COMPLETE mixed-norm comparison costs U,
and (11) is

    << (UDK)^epsilon U^(1/3)D^(-1/3)N^(2/3)K^(2/3).  (12)

At G=U^(4/25)D^(1/5), whose comparison costs U^(6/5), multiply
(12) by U^(-3/5). Across D>=U,N<=sqrt(U), this is at most

    (UDK)^epsilon U^(-4/15)K^(2/3).                  (13)

For example K=U^(2+eta) costs U^(16/15+2*eta/3+epsilon) in these
ACTUAL principal coordinates. All original Fourier/profile parameters
are separated before this family and retain their fixed seminorms.

Equations (10)--(13) are not a full bound for <Ac,v_R>. The entire
nonconstant Type-I residue error and the distinct adjoint contour
remainder remain. The matched fixed-section local formula must be
verified before adding other sections. Any row-frame inverse, its
normalization or a synthesis operator is a separate theorem; none is
assumed here. Thus no full U^(6/5) mixed mean or new zero-free region
follows from this principal-coordinate result alone.
