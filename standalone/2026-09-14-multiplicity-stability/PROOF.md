# Multiplicity-sensitive stability: a quantitative simple-or-central improvement

Date: 2026-09-14. **Status: proposed proof, requiring independent mathematical review.**

This is an asymptotic zero-count deduction, not an RH criterion. It uses the
published unconditional BGST pair-correlation theorem, Lamzouri's exact
unweighting argument, and the seven-point inequality already independently
reconstructed in this repository. The seven-point computation is an explicit
import and was not rerun in this pass. No RH, zero simplicity, unbounded
positivity conjecture, or new uniform arithmetic estimate is assumed.

Let N(T) count all nontrivial zeta zeros with 0 < Im rho <= T, with
multiplicity. Let N_0(T) count the central zeros with multiplicity, N_s(T)
count the simple zeros, and N_{s union 0}(T) count zeros which are simple OR
central, with multiplicity. Define

    B(T) = N(T) - N_{s union 0}(T).

Thus B counts precisely the off-critical zeros of multiplicity at least two,
with their full multiplicities. In particular a simple off-critical zero is
NOT excluded by a bound for B.

## Statement

Put

    A = 1/2 + cot(1/sqrt(2))/sqrt(2),
    d = 969/256000,
    b = 51/25600,
    h = 2 + sqrt(255031/128000),
    U = 1 - 4(A-1-d+b)/h^2.                                  (1)

On the imported seven-point certificate stated in Section 3, the following
complete deduction gives

    liminf N_{s union 0}(T)/N(T) >= U
      = 0.888059653174364568859397107720... > 0.88805965.       (2)

Equivalently limsup B(T)/N(T) <= 0.111940346825635431140602892280... .
Lamzouri's v2 Theorem 1.1 gives the comparison constant

    U_L = 1 - (6-4sqrt(2))(A-1)
        = 0.887620008173354339866075859447... .                 (3)

The improvement U-U_L is greater than 0.00043964 in proportion. This is NOT
an 88.8 percent critical-line bound. It is not a proof of RH, and it is not
claimed to improve the strongest simple-AND-central draft bound.

A second deduction from the same imported seven-point inequality is

    liminf [N_s(T)+N_0(T)]/[2N(T)]
      >= 0.836522920638539116521657346524... .                  (4)

The comparison value in Lamzouri's v2 is (3-A)/2 =
0.8362503518397058... . Formula (4) is an average, not a separate lower bound
of that size for each of its two terms.

## 1. The free-threshold stability inequality

This retains the stability term of L-105210, but does not fix its scalar
threshold at 2. For h >= 1 define the convex nonnegative function

    Psi_h(t) = (t-1)^2 - (t-h)_+^2,    t >= 0,                (5)
    D_h(G) = tr Psi_h(G),
    d(h) = 2h-1-h^2/2.

Convexity follows directly: below h its second derivative is 2, above h it
is zero, and both first derivatives at h equal 2(h-1). The minimum is zero
at t=1. Let V have r columns of norm exactly one in a finite-dimensional
complex Hilbert space; put P=VV*, M=V*V. Let Q be Hermitian and let b_+ be
its positive index. Then

    ||P+Q||_HS^2 >= 2h tr(P+Q) - h^2 b_+
                    - (2h-1)r + D_h(M).                     (6)

**Proof.** Write Q=Q_+-Q_- with orthogonal positive and negative parts.
The discarded cross term is 2 tr(P Q_+) >= 0. Consequently

    ||P+Q||^2 >= ||P-Q_-||^2 + ||Q_+||^2.

The scalar inequality x^2 >= 2hx-h^2 gives
||Q_+||^2 >= 2h tr Q_+ - h^2 b_+. Von Neumann's trace inequality, followed
by scalar minimization over the nonnegative eigenvalues of Q_-, gives

    ||P-Q_-||^2 + 2h tr Q_- >= sum_i f_h(lambda_i),
    f_h(t) = min_{v>=0} [(t-v)^2+2hv]
           = t^2-(t-h)_+^2.

The nonzero spectra of P and M agree, f_h(0)=0, and tr M=r. Including all
r eigenvalues of M, also when M is singular, the last sum is r+D_h(M).
Combining proves (6). The finite-rank version on an infinite Hilbert space
is obtained by restricting to the finite span of the ranges. QED.

No priority is claimed for spectral minimization or this general type of
rank inequality. The useful change is to keep h free while pricing multiple
nonreal zeros, and then retain a local Gram defect instead of dropping it.

## 2. Exact finite zero-side operator and multiplicity accounting

Let eta be a real even compactly supported L2 function, integral eta^2=1,
and let K be the Fourier transform of eta^2 with convention exp(-2 pi i z u).
Let Z be any finite conjugation-invariant complex multiset. All its sums
below retain analytic multiplicities. Define

    f_z(u) = eta(u) exp(-2 pi i z u),
    T = sum_{z in Z} f_z tensor f_bar(z)^*,
    C(Z) = sum_{z,s in Z} K(z-s)^2.                           (7)

Here u tensor v* sends a vector w to <w,v>u, with the inner product linear
in its first entry. T is self-adjoint, by conjugation invariance. Direct
rank-one multiplication and evenness of K give

    tr T = |Z| =: N,        ||T||_HS^2 = C(Z).                (8)

Indeed <f_z,f_bar(z)>=K(0)=1, and the two factors in a pair contribution to
tr T^2 are K(z-s) and K(s-z). The latter are equal, not complex conjugates.
Thus the last sum is nonnegative as a WHOLE; no sign of an individual
complex term is assumed. This is Lamzouri's finite Hilbert-space mechanism
in operator notation, not a new spectral realization of zeta.

For a nonreal conjugate pair write f_z=g+ih and f_bar(z)=g-ih. Its contribution
is 2m(g tensor g* - h tensor h*), so it has positive index at most one.
Let R be the number of real elements, with multiplicity, and put into P
ALL their rank-one terms, including repeated copies. They have unit norm.
If B is the total multiplicity of nonreal elements of multiplicity >=2,
the remaining operator Q has

    n_+(Q) <= (N-R)/2 - B/4.                                 (9)

To see this, a simple nonreal pair has mass 2 and costs at most one positive
direction. A pair of multiplicity m>=2 has mass 2m and costs at most one,
which is at most m/2. Sum these inequalities. No independence of the vectors
or separation of zero ordinates is needed.

Apply (6) and (8)-(9), with M the Gram of ALL real elements:

    C(Z) >= [d(h)+1]N - d(h)R + (h^2/4)B + D_h(M).          (10)

Repeated central zeros are legitimate repeated Gram columns. The local gap
certificate below allows zero gaps, so they are never silently removed.

There is a second useful version. If P includes only the S simple real
columns, and the other real zeros are moved to Q, then still

    n_+(Q) <= (N-S)/2 - B/4.                                 (11)

A distinct multiple real zero costs one positive direction and has mass at
least two. Thus (10) also holds with R replaced by S and its corresponding
simple-real Gram. At h=2 this gives

    S-B >= 2N-C(Z)+D_2(M_simple).                            (12)

Exactly N_s+N_0=N+S-B; this identity will produce (4).

## 3. The imported gap inequality and a finite spectral cap

The ONLY continuum numerical premise for (2) and (4) is the previously
certified Montgomery--Taylor inequality. Define

    f_0(u) = cos(sqrt(2)u)/[sqrt(2)sin(1/sqrt(2))], |u|<=1/2,
             0 outside;
    K_0 = Fourier f_0,       w_0(x)=K_0(x)^2.

For every six nonnegative real gaps, with y_0=0 and y_j=sum_{i<=j}g_i,

    p sum_{i=1}^6 g_i
      + sum_{s=1}^6 [2/(7-s)] sum_{i=0}^{6-s} w_0(y_{i+s}-y_i)
      >= epsilon,
    p=1/3000, epsilon=19/5000.                              (13)

The indexing in (13) needs the inner sum i=0,...,6-s, inclusive: these are
7-s pairs at each separation s. The original source and this repository's
independent 713,315-node reconstruction are pinned in Section 8. They are
explicit mathematical/computational imports, NOT newly executed tests.

Here is the spectral lemma needed to use a higher h. For any PSD m by m
matrix G of trace m, put E=tr(G-I)^2 and a=h-1. Then, for m>=2,

    D_h(G) >= min(E, theta),       theta=m a^2/(m-1).        (14)

**Proof.** If no eigenvalue exceeds h, D_h=E. Otherwise let the largest
eigenvalue be 1+x, x>=a. Trace and nonnegativity give 0<=x<=m-1. Jensen's
inequality applied to the remaining m-1 eigenvalues, whose mean is
1-x/(m-1)<=1, gives

    D_h >= 2ax-a^2 + x^2/(m-1)
         >= a^2+a^2/(m-1)=theta.

If E<theta, the presence of an eigenvalue above h is also impossible by
Cauchy: E>=m x^2/(m-1)>theta. This proves (14). QED.

Consequently, whenever q<=theta, E+P>=q and P>=0 imply

    D_h(G)+P >= q.                                         (15)

This is a genuine all-vector finite-matrix inequality, not a numerical
check of a selected matrix. It does not assert D_h>=E at arbitrary energy.

## 4. Exact gap charges, pinching, and endpoints

It is convenient to state the counting for k gaps. Suppose a (k+1)-point
inequality has nonnegative pair coefficients whose sum at each fixed index
separation is at most 2, pressure p, and lower bound epsilon. Formula (13)
has k=6 and equality in every pair capacity.

For m ordered points (repetitions allowed), sum all m-k contained local
inequalities. Each global pair uses only a subset of one separation's
coefficient array, so its aggregate coefficient is <=2. With

    E_m=2 sum_{i<j} K(y_i-y_j)^2,
    L_k(B)=sum_{j=1}^{m-k} (y_{j+k}-y_j),
    q=epsilon(m-k),

one obtains E_m+p L_k(B)>=q. If q<=m(h-1)^2/(m-1), (15) gives

    D_h(G_B)+p L_k(B)>=q.                                  (16)

This retains the actual boundary gap multiplicities. Replacing L_k by
k times the entire block span and then averaging loses useful boundary
information. The exact window-in-block refinement is ALREADY present in
the external tawanerguo/trmdy work; it is not claimed new here.

For a full n by n Gram M, partition its ordered columns into consecutive
m-blocks with each of the m possible offsets, retaining leftover columns
as a residual block. Convex trace pinching gives D_h(M) at least the sum
of D_h over a partition. One proof is that pinching is an average of
unitary conjugations and trace of a convex scalar function is convex.
The residual block costs >=0 because Psi_h>=0.

Across all offsets, every full consecutive m-block appears exactly once.
There are n-m+1 of them if n>=m. Each fixed (k+1)-window is contained in at
most m-k such blocks, and each elementary gap belongs to at most k local
windows. Thus

    sum_{all m-blocks} L_k(B) <= k(m-k) span(y).

It follows that, with

    d=epsilon(m-k)/m,       b=p k(m-k)/m,

    D_h(M) >= d n - b span(y) - q(m-1)/m.                   (17)

This also holds for n<m: its right side is then nonpositive. Set span=0
when n<=1. Every endpoint and every repeated point is included. The last
term is a fixed additive constant, not an unpriced boundary error.

If 0<d<1, choose

    h=2+sqrt(2-2d),       so d(h)=d.                        (18)

Combining (10) and (17) cancels the real-zero count exactly and gives the
finite-multiset statement

    B <= (4/h^2)[ C(Z)-(1+d)N+b span(real Z)+q(m-1)/m ].    (19)

THIS cancellation is the new use of the retained defect. A fixed h=2 is
adapted to simple-real counting, not to the simple-OR-real objective. The
new proof does not infer a sign for any unknown individual zero.

## 5. Passing to the actual zeta zeros: two fixed tests, not a moving-test assumption

The analytic input is the unconditional BGST theorem in the following
form (Lamzouri v2, Lemma 3.1, citing BGST Lemma 5). For real even f in L1,
supported in [-1,1] and Lipschitz at zero,

    sum_{rho,rho': 0<gamma,gamma'<=T}
      fhat(i(rho-rho') log T/(2pi)) 4/[4-(rho-rho')^2]
      = [f(0)+2 integral_0^1 u f(u)du+O_f(1/sqrt(log T))]
           T log T/(2pi).                                 (20)

All zeros and multiplicities enter this theorem; it assumes no RH. We
import (20), not a new estimate for its error term.

For fixed real even eta in C_c^infinity(-1/2,1/2), integral eta^2=1, put
v=eta^2, K=vhat and U=v*v. Then U and U'' are both fixed real even smooth
functions supported in [-1,1]. The exact identity

    [ Uhat(z) - U''hat(z)/(4(log T)^2) ]
       = [1+pi^2 z^2/(log T)^2] K(z)^2                      (21)

cancels the rational weight in (20). Apply (20) SEPARATELY to U and U''.
There is no unsupported uniformity assertion for a T-dependent test. By
Riemann--von Mangoldt the resulting unweighted identity is

    C(Z_T) = [A(v)+o_eta(1)] N(T),
    A(v)= integral v(u)^2 du
            + integral integral |u-v'| v(u)v(v') du dv',
    Z_T={-i(rho-1/2) log T/(2pi): 0<gamma<=T}.               (22)

The sign -i instead of i is harmless because K is even. Reflection
rho -> 1-conj(rho) proves conjugation invariance of Z_T. Its real elements
are exactly the central zeros and their real span is at most
T log T/(2pi)=(1+o(1))N(T).

We must also justify using the nonsmooth f_0 of (13). Choose fixed smooth
even cutoffs chi_delta supported in (-1/2,1/2), equal to 1 away from the
endpoints, between 0 and 1. Normalize

    v_delta=chi_delta^2 f_0 / integral chi_delta^2 f_0,
    eta_delta=sqrt(v_delta).

The last expression is the smooth function chi_delta sqrt(f_0) divided by
the positive normalizer. Thus it is admissible in (20)-(22). As delta->0,
v_delta->f_0 in L1 and L2. Put e_delta=||v_delta-f_0||_1. For EVERY real x,

    |K_delta(x)-K_0(x)|<=e_delta,
    |K_delta(x)^2-K_0(x)^2|<=2e_delta.                      (23)

Both kernels have modulus at most one on the real axis. The sum of all
pair coefficients in (13) is 12, so the same gap inequality for K_delta
holds with epsilon_delta=epsilon-24 e_delta and unchanged p. This is
uniform over ALL gaps, not only a compact set of separations.

Use epsilon_delta, d_delta and h_delta in (16)-(19). The numerical cap
condition at delta=0 is STRICT, so it persists for all sufficiently small
delta. First fix delta, let T tend to infinity in (19) using (22), and
only afterward let delta->0. Since A(v_delta)->A(f_0), this proves

    limsup B(T)/N(T) <= (4/h^2)[A(f_0)-1-d+b].              (24)

There is no interchange of an uncontrolled growing-parameter limit.

For completeness A(f_0) equals A in (1). On [-1/2,1/2], define
F(x)=f_0(x)+integral |x-y|f_0(y)dy. Since f_0''=-2f_0,
F''=0; F is even, hence constant. At x=1/2 its value is
f_0(1/2)+1/2=A. Integrating F against f_0, whose integral is one, gives
A(f_0)=A. This is the classical Montgomery--Taylor value, not a new
window optimization.

## 6. Explicit constants and the average-count consequence

For the union theorem choose m=1536, k=6, epsilon=19/5000, p=1/3000. Then

    q=2907/500=5.814,
    d=969/256000,
    b=51/25600,
    h=2+sqrt(255031/128000).

The cap condition has a positive margin:

    m(h-1)^2/(m-1)-q > 0.0052873163417615.                  (25)

Therefore (24) proves (1)-(2). All displayed comparisons are freshly
reconstructed by rational interval arithmetic in verify.py, using integer
square roots and alternating series in x^2=1/2 for cos x and sin x/x.
No zero ordinate or gamma/zeta numerical oracle enters these comparisons.

For the average statement use only SIMPLE central columns in Section 2,
so (12) holds, and choose h=2, m=269, k=6. Write

    d_a=4997/1345000,       b_a=263/134500,
    X=S-B=N_s+N_0-N.

The block target is 4997/5000 < 269/268, so (17) applies. Since S>=X and
d_a>=0, (12) implies

    (1-d_a)X >= 2N-C(Z)-b_a span(simple real Z)-O(1).

Apply the same smooth-window limiting argument. It gives

    liminf (N_s+N_0)/(2N)
       >= (1/2)[1+(2-A-b_a)/(1-d_a)]
        = 0.836522920638539116521657346524... .              (26)

This is not inferred by incorrectly adding marginal density lower bounds;
the multiple-off-line term B is retained until the exact count identity.

### Optional stronger input, NOT needed by the headline theorem

The external trmdy nine-point draft at the source pin in Section 8 states
an admissible window with A(v)<=2-3362285207/5000000000 and a k=8
certificate with epsilon=15211/2500000, p=1/2500 and all separation
capacities equal to 2. If those additional numerical/window inputs are
accepted, the SAME argument with m=963 gives

    liminf N_{s union 0}/N >= 0.8883071710663649185... .      (27)

The cap condition is strict here too. This pass did not reconstruct that
window or replay its large nine-point search. Equation (27) is a clearly
conditional application of their stronger inputs, not an independently
certified headline or a competing priority claim. The original seven-point
premise, not this optional external draft, suffices for (2) and (4).

## 7. Scope, checks, and what changed in the research strategy

The preceding HBR30 all-rank theorem at bounded smoothing parameter did
not control unseen off-line zeros: it used verified low zeros and admitted
synthetic off-line divisors. Increasing its parameter without new arithmetic
would not be the result proved here. That route is not used in this proof.

This contribution instead improves a finite, explicitly stated asymptotic
bound concerning the actual zeros, through a source-specific gap constraint
and a proved number-theoretic mean-square input. It still allows all simple
off-critical zeros and density-zero exceptional sets; it is not an RH
completion or a claim that RH is now close.

The exact checker verifies the scalar spectral minimum; noncommuting
rational Hermitian matrix examples; the cap; multiplicity inequalities;
full offset/gap counts; and the final constants. These finite controls are
not a machine proof of the analytic or all-dimension arguments. Normal and
optimized execution use the SAME code. The seven-point continuum search,
BGST theorem, Lean builds, and whole-repository validation were NOT rerun.

The main review questions are (6), the B/4 saving in (9)/(11), use of ALL
real columns with repeated zeros, the cap (14), the exact average (17), and
the order of limits in (20)-(24). A mistake in any of these would invalidate
the new bound. No missing RH-strength estimate is delegated to reviewers.

## 8. Exact sources, attribution, and comparison boundary

1. Y. Lamzouri, arXiv:2609.02882v2, dated 2026-09-08. Theorem 1.1,
   Proposition 2.1 and Section 3 were read, including HTML and the PDF
   statement/pair-correlation pages. The operator identity and removal of
   the pair weight are credited to this source; its comparison for the
   union is (3), not its simple-AND-central constant.
   https://arxiv.org/html/2609.02882v2
2. S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L.
   Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair
   correlation of zeros of the Riemann zeta-function*, Acta Arith. 214
   (2024), 357-376, Lemma 5. Imported in the exact form (20), checked
   against Lamzouri v2 Lemma 3.1; not independently reproved here.
3. `ainta/zeta-simple-zeros@040c5e899e658aed7b56a2a87f501798fe10761d`,
   seven-point certificate. Its distinct independent repository replay is
   `GettysburgResearch/riemann@f99d9e3908dde4865377c75d9ca051c1f545bf4f`,
   `reviews/A/supplement/REPORT.md` Sections S01-S02,
   blob `e1359f93c399c783e01c86d614fa02e86666671a`.
   The statement, arithmetic boundary, coverage account, and block proof
   were read. No new replay of its 713,315-node search is claimed.
4. Riemann PR #731 at `6d440eb6c82d989c046e87e13f9bdabf087f920f`:
   `claims/lemmas/L-105210-stability-enhanced-rank-inertia.md`,
   blob `2ecb7959c1c8eb3bd9169a5cc606630282019bb8`;
   `claims/lemmas/L-106551-280-point-seven-gap-pressure-lift.md`,
   blob `3803c74e27260da1f65531da06cda7c8c376f9af`.
   Both full proofs read. Classical trace convexity, spectral minimization,
   and the original stability improvement are credited, not relabeled.
5. `trmdy/zeta-simple-zeros-673137@1610b97b7895ff34982260f8dcaf04a0f7b82cf7`
   is the common-window/certificate source pinned by Yuhang Shi's paper.
   README, `docs/proof.md` (blob
   `71355b43b37c32e0e1ae7a8997f4fdac36fd6a7a`), and the two-certificate
   mathematical interface were inspected;
   neither large gap run was replayed. The known window-in-frame counting
   improvement is credited to tawanerguo-cn/trmdy. Our initial independent
   rediscovery of that counting refinement was NOT counted as new progress.
6. Y. Shi, `yuhangshi888/zeta-simple-zeros-673316977`, `main.tex` blob
   `a9915c4b09b5fbbba075cfdeb89434c4dd6e11da`, and README blob
   `735a8b69973dba514dd89182b8aa909b803ab4f6`, read for the existing
   two-certificate method and .673316977 simple-AND-central candidate.
   No attempt is made to beat that DIFFERENT statistic by comparing it
   numerically with (2). External draft status and input boundaries remain.

The attribution search was targeted, not an exhaustive originality audit.
The claim is a proposed quantitative improvement over the explicitly
identified Lamzouri-v2 bounds; no accepted world-record or external-referee
verdict is asserted. All earlier research, main, canonical statuses and
formal sources are unchanged.
