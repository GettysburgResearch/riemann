# Prime-side heat continuation: all orders to t=1/10 and a growing-time region

**RH and unrestricted mixed positivity remain UNPROVED.** This packet contains
proposed complete proofs of the stated inequalities, exact source identities,
and a recorded unsuccessful attempt at the remaining global estimate.
Independent mathematical/code review and external novelty assessment are pending.

Scientific base: PR #790 at 401196451ef1b51e5ff4d84dd23bd75bbf9215a1.
New files only under prime-heat-pass3/. The original, mixed-differences-pass2,
quadratic-wedge-pass3, and newly published pass2 packets are preserved.

## What is proved here

Keep A=rho(1-rho), S(t)=sum_(Im rho>0) exp(-At), and D_m=(-1)^m S^(m),
with multiplicities. The inherited mixed inequality has the exact form

    H_(a,b)(v)=v^(a+1)/(a+b)! integral_0^infinity
                              t^(a+b)e^(-vt)D_b(t)dt.

The new method is the prime-side explicit formula for

    F_(m,t)(z)=(z^2+1/4)^m exp(-t(z^2+1/4)),   I=integral_R F(x)dx.

For m>=1 the endpoint terms vanish exactly, and

    4pi D_m = integral_R F(x)[Re psi(1/4+ix/2)-log pi]dx
                   -2 sum_(n>=2) Lambda(n)/sqrt(n) Fhat(log n).

No RH-conditional explicit-formula input is used. A finite Gamma-polynomial
estimate bounds the shifted Fourier contour uniformly in m, while an exact
positive Gamma mixture controls the archimedean part.

**ASTRA-PH-01:** for m>=1 and 0<t<=1/10,

    D_m(t) > I/(4pi) [log sqrt(m/t)-15].

**ASTRA-PH-02:** combining this with the preserved pass2 analytic theorem and
its published zero-verification input gives

    D_m(t)>0, every m>=0 and 0<t<=1/10;
    H_(a,b)(v)>0, every a>=0, v>0 and 0<=b<=10^22.

The first is an unbounded-order theorem on one common time interval. The
second is all-time but FINITE in mixed depth. The 10^22 range is a parameter
comparison, not an enumeration. This corollary imports the full established
Platt--Trudgian verified height 3*10^12; that computation was not rerun.
Its dependence on pass2's proposed analytic proof is retained explicitly.

**ASTRA-PH-03:** without any finite zero verification, for m>=40t and m>=1,

    D_m(t) > I/(4pi)
            [log sqrt(m/t)-7-130(t+1)^2 exp(t/2)].

It follows that for every epsilon in (0,2), all sufficiently large m obey

    D_m(t)>0 for EVERY 0<t<=(2-epsilon)log log m.

Thus the common time window can itself grow with order. The number 2 is the
coefficient of a proved region, not a sharp obstruction or a universal limit.

**ASTRA-PH-04:** at every fixed t>0, with r=sqrt(m/t),

    D_m/I = (1/(4pi))[log(r/(2pi))-2 C_t(r)+o_t(1)],
    C_t(r)=sum_(n>=2) Lambda(n)/sqrt(n)
                  exp(-(log n)^2/(8t))cos(r log n).

The error is NOT claimed uniform as t grows. A complete Hermite-polynomial
formula for each finite-order prime kernel is supplied, including its signs.

**ASTRA-PH-05:** the full prime/gamma comparison for every m>=1,t>0 is an
exact RH-equivalent endpoint. Its proof is a conditional implication, not a
proof that the arithmetic comparison holds everywhere.

## What the attempted closure does not establish

The prime majorant used here is of size (t+1)^2 exp(t/2), while the available
archimedean reserve is logarithmic in sqrt(m/t). Their comparison does not
control all intermediate scales. Replacing the prime kernel by its absolute
value loses precisely the signed arithmetic needed beyond this region.

Any remaining heat-sign failure must have m>10^22, t>1/10, avoid the positive
bracket above, and precede the inherited late-time threshold T_m(3*10^12).
This is still an infinite region. Taking a finite verified height to infinity,
or applying the fixed-t asymptotic in an unproved joint limit, is not allowed.
There is no claim here of an end-to-end unconditional RH proof.

## Review and execution

Read PROOF.md, then SOURCES_REVIEW.md. The exact checker is deliberately
separate from the analytic proofs:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    sha256sum -c SHA256SUMS

17,142 finite exact rational checks passed in each mode, with byte-identical
results. Four altered-output tests were rejected, including altered RH and
machine-proof flags. These controls authenticate finite constants, Gamma
coefficients, contour algebra, endpoint normalization, Hermite expansions and
mixed-integral factors. They do not prove the infinite analytic statements.
No Lean build, independent referee acceptance, external priority, or full
zero verification is claimed. See VALIDATION.md for executed boundaries.
