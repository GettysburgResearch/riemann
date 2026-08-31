# A positive coefficient majorant for the completed primitive current

This refines the uniform tail bound in
`FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md`. It uses exactly the same
finite prime set, all monotone source paths, all ordered records and
original product horizon nm<=H. It does not evaluate a signed observed
tail or claim a cancellation estimate.

Write b_e=[z^e]sqrt(1-z), b_0=1. For e>=1 put

    beta_e=|b_e|=binom(2e,e)/(4^e(2e-1)).               (1)

The absolute local source coefficient is a convex combination of the
two endpoint magnitudes. A COEFFICIENTWISE upper bound is therefore

    alpha_0=1,
    alpha_e=beta_e if e is odd,
    alpha_e=beta_(e/2) if e>=2 is even.                 (2)

The exact absolute schedule-derivative coefficients are

    d_0=0,
    d_e=beta_e if e is odd,
    d_e=beta_(e/2)-beta_e if e>=2 is even.              (3)

All alpha_e are positive and all d_e with e>=1 are positive. Separating
even and odd powers gives their generating functions

    Amax(z)=sum alpha_e z^e
      =2-sqrt(1-z^2)+(sqrt(1+z)-sqrt(1-z))/2,
    D(z)=sum d_e z^e=sqrt(1+z)-sqrt(1-z^2).            (4)

The distinction from the completion note's A(q)=2-sqrt(1-q) matters.
That function bounds the local absolute SUM at a positive evaluation
point. It is not a coefficientwise bound for both endpoint sources.
Formula(2), rather than that smaller aggregate bound, is used for each
individual product cost below.

For a fixed finite set P of primes, form the multivariate nonnegative
series

    G(z)=2 sum_(p in P) D(z_p) Amax(z_p)
                              product_(q!=p) Amax(z_q)^2
        =sum_(k supported on P) g_k z^(v_P(k)).        (5)

If a_n is the actual half-source coefficient, its coefficientwise
absolute bound is product_p alpha_(v_p(n)). The corresponding bound
for its p derivative uses d_(v_p(n)) in that one coordinate. Since
each monotone coordinate has total increment1, the actual factor2 gives

    sum_(nm=k) |2 integral a_m da_n| <= g_k.            (6)

The convolution in(5) includes every allocation of each prime exponent
between n and m and every derivative coordinate. In particular it is
not a squarefree-only census, a chosen ratio mask or a sample of paths.

Set rho_p=p^-1/2. Absolute convergence follows from(4), so

    T_H=G(rho)-sum_(k<=H, k supported on P) g_k/sqrt(k)
       =sum_(k>H) g_k/sqrt(k) >=0.                    (7)

Equations(6)-(7) prove the uniform ORIGINAL-field bound

    sup_(path,t) |F_infinity(t;path)-F_H(t;path)|<=T_H. (8)

The completed field and source measure are those in the completion
theorem. Equal-ratio cancellation is neither used nor dropped from
the underlying field: (8) is obtained by bounding the complete tail
before collecting it.

Let nu0 be the exact original kernel mass and Cphys=C_(1/2) the
smaller aggregate source bound from that theorem. Then

    ||F_infinity-F_H||_(L2(nu)) <=sqrt(nu0) T_H,
    |I_infinity-I_H| <=2 nu0 Cphys T_H,                (9)

uniformly over all paths. The same last bound applies to the difference
of actual global minimum values. One may replace T_H on the right by
min(T_H,C0 H^-1/2), where C0=|P|sqrt2*4^|P|. Both are proved upper
bounds; selecting the smaller one does not select a source or a metric.

For the panel P={2,3,5}, g_k is calculated with exact rational
convolutions of(2)-(3). A complete finite prefix contains only the
costs k=2^a3^b5^c<=H. Its evaluation and the closed total G(rho)
require positive square roots and rational arithmetic, not a large
matrix of physical frequencies. Outward rational intervals give an
upper bound even when the total-minus-prefix subtraction loses digits.
Known positivity may replace a negative interval LOWER endpoint by0;
an upper endpoint below0 would instead be a failed check.

The following tiny coefficients provide independent arithmetic controls:

    g_1=0, g_2=1, g_4=5/4, g_6=2, g_8=1.             (10)

For example [z^2]D Amax=3/8+1/4=5/8, giving g_4=5/4;
the cost6 has contributions from each of its two derivative coordinates.

The registered acquisition below this note measures only the positive
majorant and its rigorous bounds. It does not assert that a bound is
attained, that a finite minimizing path remains optimal at infinity,
or that the fixed-prime primitive has been identified with a retained
post-renewal family. No limit over primes is taken.
