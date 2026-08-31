# Independent review: completed period and theta-source flag positivity

Verdict: **PASS** on exact science
`fdd349dcf6ba1b104e27866ae66b4c89752d5f05`, immediate parent
`8cf1538b336acd2b60faba2d7129edba3676932c`, authoring base
`ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf`.
This is a non-author review of the complete five-file packet. Neither the
proof nor its finite controls were authored or edited by this reviewer.
The result is accepted in its written fixed-source scope, not on the strength
of finite tests alone. No actionable mathematical or release-contract gap
was found. This separate review changes no scientific source.

## 1. Actual theta source and global completion

I read the complete frozen proof, producer, test, manifest and fixture, the
literal RQ and CF parent notes, the full FI theorem and its independent
audit, and all three preregistration/design versions. Their roles differ:
RQ/CF supply the actual modular period and Fourier normalization; FI and
its accepted audit supply the genuine poles of the old period quotient;
the new MP source construction has a direct proof independent of FI's
deeper simultaneous automorphic-value imports.

MP1--MP5 have the correct normalization. The lattice
`((mx+n)/sqrt(y),m sqrt(y))` has covolume one and its dual is a rotation.
Poisson summation therefore has factor `t^-1`, not `t^-1/2`. The theta
integral has the factor `1/2`, and its constant/vacuum contribution is the
Petersson matrix G. Thus

`B(t)=t^-1 B(1/t)+(t^-1-1)G/2`,
`H(t)=G+2B(t)=t^-1 H(1/t)`.

The source is intrinsic under modular lattice rotations. A fixed-t theta
sum has at most polynomial cusp growth, locally uniformly for positive t;
cusp forms pay integrability. Every nonzero vector has strictly positive
B(t)-norm. Monotonicity in t and the finite Mellin moments for every real
exponent greater than one imply rapid decay: integrating on `[t/2,t]`
bounds `tr B(t)` by a constant times `t^-A`. This is an all-exponent proof,
not extrapolation from sampled theta values. Tonelli first applies to
nonnegative diagonal forms; polarization and absolute domination then
justify the complex-variable period identity.

I used the PDF skill to read and visually inspect Zagier's printed pages
275--277, including equations 2, 4, 6 and 7, in
[Eisenstein series and the Riemann zeta-function](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf).
The downloaded PDF SHA256 was
`bd42ed6dfc76fa87f71334e7cc7dbb9f86e21e6717c1b23a89625114a8efe907`.
This primary passage agrees with the half-factor, theta reciprocity,
completed Eisenstein normalization and invariant measure. The remote PDF
is a personally checked analytic input, not part of the producer's offline
Git-byte contract.

For a fixed proper W, the quotient-metric construction is sound. In
G-orthonormal coordinates with W trailing, writing `R=2B` gives

`2C_W=R11-R12(I+R22)^(-1)R21`
`     =min_u {R[(c,u)]+||u||^2}`

as quadratic forms on the quotient. Positive definiteness in finite
dimension gives strict positivity; using u=0 gives `2C_W<=R11` and pays
the rapid-decay bound. Quotient metrics are homogeneous, so the homogeneous
H-law gives exactly the stated affine C-law. No commutation of B and G,
no Schur-through-integral identity, and no complex minimization are used.

Splitting the Mellin integral at one independently gives

`L_W(s)=G_Q/[2s(s-1)]`
`       + integral_1^infinity (t^(s-1)+t^(-s)) C_W(t) dt`.

The integral is entire by local uniform domination using arbitrary rapid
decay. This proves the complete reflection, Schwarz symmetry and precisely
the nonzero matrix residues `-G_Q/2,+G_Q/2` at zero and one. Multiplication
by `s(s-1)` has endpoint value `G_Q/2`. There is no hidden assertion that
individual matrix entries all have nonzero residues or that a determinant
has pole order one. The pointwise vacuum subtraction, rather than separate
divergent vacuum Mellin integrals, is essential and correctly retained.

## 2. What positivity proves, and what it does not

For the conjugate-linear-first convention, the feature vector is
`sum_j t^(conjugate(z_j)) v_j`. Its positive quadratic form integrated
against `B(t) dt/t` or `C_W(t) dt/t` gives precisely the matrix kernel
`I(z+conjugate(w))` or `L_W(z+conjugate(w))`. All real parts of the sums
exceed one in the specified half-plane, so Cauchy--Schwarz and the Mellin
domain pay convergence. This is kernel positivity, not pointwise Hermitian
positivity of the value at a nonreal parameter.

The comparison to the old actual weight-24 quotient is valid. FI gives a
genuine pole `a+ib`, a>1. Taking the two kernel arguments with common real
part a/2 and imaginary parts near +/-b/2 keeps diagonal entries equal to
the positive finite `Q_period(a)`, while the off-diagonal entry is unbounded.
The two-by-two kernel inequality fails nearby. The new family has no such
pole, so equality of the two constructions for the canonical weight-24
flag is impossible. FI's automorphic inputs are retained as the accepted
frozen theorem/audit dependency; they are not falsely machine-certified
or claimed to have been re-proved by this MP finite helper.

MP14 is an exact nonnegative integral of the cross-density square. For
weight24 and a line W, equality would make that cross density vanish
identically, and hence make the period diagonal in one fixed basis.
The three distinct Fourier directions in RQ rule this out. The strict
comparison is not a general irreducibility assertion for arbitrary weights.

The logarithmic block-moment argument is correct. Inside the convergence
domain all logarithmic moments are dominated by slightly shifted powers.
The variance Schur complement is the minimum of the integrated norm of
`(log t)v-u`. An everywhere positive-definite density on a continuum cannot
annihilate this expression for a nonzero v, proving strict variance for I
and L_W. For the uncompleted weight24 Dirichlet Gram, the four stacked
coefficient/logarithm rows alone have positive determinant

`L2 [211312800 L3+1159692288(L3-L2)]`.

Thus they form a strictly positive sub-Gram of the full convergent sum.
This is a legitimate finite-rank sufficient proof of strict variance,
not a finite-sample inference about the full family. The rational proxy
frequencies in the separate controls are explicitly not native logarithms.

MP2 permits any fixed nonzero J, including non-Hermitian, indefinite and
singular matrices. Finitely many Fourier coefficient rows span the fixed
space; their contribution bounds D(sigma) below by `N^-sigma D0`.
The literal double-gamma completion grows faster than that exponential
decays, so the least eigenvalue of I(sigma) tends to infinity. Inverting
`I J I=J` gives the stated norm contradiction. No changed completion or
parameter-dependent metric is excluded by this argument.

For MP3, choosing a sufficiently right fixed line makes the normalized
Dirichlet tail and the zeta(2s) correction uniformly smaller than one half.
The phase derivative of the leading double-gamma term is exactly the sum
of the two real digammas minus `log(4pi^2 n0)`. The
[DLMF expansions 5.11.1--5.11.3](https://dlmf.nist.gov/5.11)
apply in this sector and yield eventual increase through all phase
quadrants. At the successive multiples of pi/2, `Re(1+r)>1/2` protects the
alternating indicated component. The Herglotz/positive-real exclusions
therefore concern the literal period, not every possible scattering object.

## 3. Independent finite reconstruction

The accompanying standard-library helper imports neither scientific
producer nor test module. It authenticates all five science files directly
against frozen Git bytes and resident LF hashes, the seven literal source
pins, the four artifact hashes and the payload seal. Its separate routes are:

- Native coefficients from `(E4^3-E6^2)/1728`, followed by the Miller shear.
  Expanding along the two unit-pivot rows gives the formal logarithmic
  determinant coefficients without numerical logarithms.
- All 48 derivatives from truncated Taylor composition `F(q exp(h))`, whose
  r-th coefficient times r! is `(q d/dq)^r F`. This uses neither the producer's
  rational-numerator recurrence nor the test's Stirling-number route.
- Exact Gaussian-rational matrices, recursive determinant expansion and
  cofactor inverses. Source quotients are independently recovered as the
  inverse of the restricted inverse metric, rather than the producer's
  direct block-elimination formula.
- Complete feature moment, regression-residual, congruence and principal-
  minor reconstruction for all three declared systems and all twelve
  reciprocal pairs. Both vacuum and H are transformed under nonunitary
  flag-preserving congruence.

All comparisons pass normally and under `-O`. All 12 negative derivative
cells are retained; the first is `r=7,q=1/3`, value `-3311/12288`.
The post-scout kernel determinant is `-81/8808800`, with pivots
`91/90,1189/89180,-5103/7481188`. The finite variance determinants are
`0,45309363075729/8557913953170404494528,0`; the two singular examples
are not relabelled strictly positive. These are algebraic reciprocal pairs,
not one globally specified synthetic theta function or actual theta samples.

The frozen 36-test suite passed normal **49.433 s** and optimized
**47.721 s**. Both producer checks and all four LF-exact fixture/source
emits passed. A fresh independent terminal attack set obtained **24 genuine
rejections in each mode**, including fourteen independently resealed value,
coverage, native-row, proxy, vacuum, flag, scope, source and artifact mutations;
five malformed/type JSON cases; four scalar/matrix/range cases; and literal
frozen-source byte corruption. The checker reconstructs primitive arithmetic
after authentication, not merely a self-consistent supplied payload.

Ruff lint/format, the full authoring-base-to-science whitespace check and
the exact five-file scientific delta pass. The science fixture LF SHA256 is
`021b0bd08e96fa4a58dfac352f4833ef86587ea273e6d656bcda8c19bf789689`;
its payload seal is
`c2468ac8f9556399dfbcd2ae4be8fc347c6cb75fbab206f1f63a99fe92cbf7b0`.

## 4. Accepted scope and open questions

The substantive constructive result is a source-defined, Petersson-polarized
theta-flag family with global completion, endpoint residues and a positive
Mellin feature kernel. The earlier period quotients and their additional
poles remain different, valid objects. Classical Poisson, quotient-form,
Mellin and matrix-moment machinery is credited.

No Euler product, ordinary Dirichlet series, motive, preferred Hecke flag,
canonical automorphic representation, exhaustive novelty claim, nontrivial
zero localization, RH or GRH follows. The finite helper proves none of the
analytic continuation or infinite positivity assertions mechanically; those
were reviewed in the written proof. Only these two review files are added.
There was no push, PR change, main/front edit, or frozen-source modification.
