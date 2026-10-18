# Can the new Gauss estimate improve the inverse recursion?

**PROPOSED audit.** All references are to the exact primary sources pinned
in NOTES.md and SYNCHRONIZED_LOG_MARK.md. The conclusions below concern
what their stated positive estimates yield, not a lower bound for the
actual correlated arithmetic vector.

The new cumulative logarithmic mark uses the all-length prescribed Gauss
mean (I) and the positive fourth-label mean (II). Feeding (I) back into an
inverse mean does not produce a better self-improving exponent by itself.
Even in the clean coprime sector, Poisson on the normalized inverse mean
at row length U and column length D introduces dual row length

    H=D^2/U

and prefactor U/D in front of the normalized C_-1 Gauss norm. Input (I)
then charges

    (U/D) H = D.

Including the original diagonal gives U+D. Moving punctures and shared
factors cannot be discarded; we are giving the most favorable clean-sector
budget, not asserting a new general inverse theorem from this calculation.
It leaves the row-size range U>=D unchanged. The source's sixth-power
amplification therefore still yields the exponent

    e(r)=max(1,(1+5r)/6),  D=U^r,

rather than a smaller long-column exponent. The Gauss theorem itself was
proved using that inverse framework, but this audit is stronger than
merely calling feedback circular: its available numerical self-map does
not improve the threshold.

The existing inverse-witness count is already better than the earliest
base envelope in part of the parameter range. For t in [1,3/2], the actual
inverse witness has r in [t-1/2,t], up to prescribed losses. For delta<=5/6
the endpoint maximum obtained from e(r)-delta r is

    max(1-delta(t-1/2), 1/6+(5/6-delta)t).

Balancing endpoints gives t=1+3delta/5 (when it is in the allowed interval)
and count exponent 1-delta/2-3delta^2/5. This is an existing deduction
from the pinned source, not a new consequence of this packet's Gauss norm.
The source's refined witness counts also use the plain witness and
independent prime amplitudes. They must not be replaced by an older,
weaker base envelope when assessing the existing benchmark.

There is an explicit quantitative target for a genuinely better high
estimate. With low row-size cost max(x,y)/2 and no independent prime boost,
let B be a proposed boundary, delta=2B-1 and r_B=6B-5. Section 6 of
SYNCHRONIZED_LOG_MARK.md gives the necessary top-bin condition

    R(delta) < B*r_B/(1-r_B)-B+2/3.                    (1)

For the reported Liu v2 boundary B=0.874957019420098946 this requires

    delta = 0.749914038840197892,
    R(delta) < 0.0829609925588541068253104488... .      (2)

The optimized inverse-only count just described is
0.2876203411901303544858710261..., and its balanced t is
1.4499484233041187352. At the admissible witness corner r=1,m=1/2,
the stated inverse second-moment and plain fourth-moment estimates each
retain the positive row term U, while their respective witness spikes
are both U^delta. Their separate Markov bounds therefore supply only
R=1-delta=0.250085961159802108 at that corner. Removing that positive
term would itself require a new signed or restricted arithmetic estimate;
it cannot follow from applying the same positive upper bound again.

A mixed estimate is a specific possible escape. At this corner the
ACTUAL matched product has witness spike

    |M_u S_u|^2 >= U^(3delta/2-epsilon).

Consequently a complete mean bound U^(A+epsilon) for this correlated
vector would yield R<=A-3delta/2. The threshold (2) asks for

    A < 1.2078320508191509448253104488... .             (3)

The more ambitious row-size mean A=1 would be sufficient at that corner.
This is only one necessary witness cell; a complete boundary improvement
must cover every actual r,m and all profile, height, powerful-row and
nonunit-mask sectors. The actual convolution coefficient is

    sum_(dn=a) mu(d) nu(a) W_M(Nd/D) W_S(Nn/N),

with the same row character and same norm height in both profiles. No
coprimality of d,n is allowed. The easy identity mu*1=delta does not apply
inside one dyadic corner. For D>N its product support has large squarefree
core, rather than consisting of pure-power columns. The rational component
of this sprint is separately investigating this full vector.

In a clean all-four-pairwise-coprime squarefree sector, row Poisson exposes
a coherent label sum of the form

    (U/(DN)) sum_h |sum_(n~N) gamma_1(n)/sqrt(Nn)
                      chi_n(h)^(sign) S_(h,n)(D)|^2,              (4)

up to the exact fixed ray phases and its one common smooth kernel.
Here S is the prescribed C_-1 Gauss core with fourth-power label n,
and the dual h scale is D^2N^2/U. The sign and full shared-factor
extensions must be retained when converting (4) into a theorem.
In particular (4) is only a mapping of the two separated column phases,
NOT an equality to a complete positive square in the clean sector:
pairwise coprimality excludes the collisions d_1=d_2 or n_1=n_2.
Completing that square requires all corresponding collision and zero-mask
subtractions. The added dual diagonal can cost DN, already U^(3/2) at
the corner, so it must not be silently absorbed into a row-size bound.
Applying Cauchy over labels and only their positive mean (II) is too
expensive at D=U,N=U^(1/2). The relevant coefficient gamma_1(n) is
arithmetically prescribed, and its coherent correlation with that label
is exactly what a useful new theorem would have to exploit.

Finally, gamma_1 at squarefree composite arguments is not simply a
nonzero-angular cubic Gauss coefficient. The exact global relation is

    gamma_1(n)=mu(n)alpha(n)G(n) conjugate(gamma_2(n)).

The global mu(n) cannot be replaced by a single prime minus sign, or
treated as an arbitrary harmless column multiplier in (I). This is a
precise reason the unmarked Gauss theorem does not already estimate the
coherent label vector (4).
