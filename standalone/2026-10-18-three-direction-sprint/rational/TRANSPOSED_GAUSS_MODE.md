# Flat row probes already pay the known transposed sextic Gauss mode

**PROPOSED, source-qualified component theorem.** The proof uses the pinned
OpenAI unmarked inverse moment at its precise boundary length and the
elementary complete small-conductor estimate proved in this packet.
Direct Cauchy already bounds the actual mixed detector's overlap with
the induced bad COLUMN from the known transposed sextic Gauss witness.
It does not bound the whole mixed mean or prove a zeta improvement.
Sections 2--3 give an optional exact reflection check, not an additional
arithmetic saving or the cause of the bound.

## 1. The row-side pairing and the exact source interface

Work over E=Q(omega) with the fixed arithmetic data of the source. Let
u range over squarefree good primary rows with Nu≈U, in any fixed ray
slice. The original mixed polynomial is

    f_u=M_u(D;W_M) S_u(N;W_S),
    D=U,   N=U^(1/2),                                  (1)

with the SAME finite twist, orientation, height, and original zero
extensions in the two factors. All d,n and all shared-prime cases in
their product remain present. We first take orientation +; conjugating
the entire construction gives the other orientation.

The only deep source moment used here is

    sum_(u sixth-power-free, Nu≈U) |M_u(U;W)|^2
                          <<_epsilon U^(1+epsilon).     (2)

This is the pinned source's `inverse-amplification` lemma,
`eq:amplified-note`, with exponent `e(r)=max(1,(1+5r)/6)` at r=1,
around lines 12360--12480 of
`../eisenstein/_source-original-quasi.tex`. It permits the stated fixed
finite twists and smooth profiles, with polynomial height cost and
rowwise smooth test parameters. It does not require a strict D<U
margin. Squarefree rows are a positive subset of those in (2).
This packet does not reprove the source's inverse-moment recursion.

Let a_u be ANY row multiplier with |a_u|<=C, supported on this squarefree
row annulus. It may contain a fixed smooth radial weight, a ray slice,
moving residue-character twists, and additional coprimality masks.
No multiplicativity of a_u is needed. Define the raw row pairing

    B=U^(-1/2) sum_u a_u conjugate(gamma_1(u)) f_u.      (3)

Then

    |B|^2 <<_epsilon U^(1+epsilon)(1+T)^A,              (4)

Here T bounds the norm-twist heights and A is a fixed seminorm order.
As in the source, choosing its height cutoff T<=U^tau after A makes
this `U^(1+epsilon)` after reducing the preliminary losses.
The constant in this raw estimate is independent of the twists and
masks inside a_u. Uniformly normalizing an arbitrarily deleted row
vector would additionally require its actual norm; no lower norm is
assumed for an arbitrary mask.

The shortest proof uses the ORIGINAL plain polynomial. The elementary
all-element plain mean (8), at N=U^(1/2), gives `sum_u|S_u|^2<<U^(1+epsilon)`.
Thus for every row multiplier with absolute value at most C,

    |B|^2 <= C/U * (sum_u |M_u|^2)(sum_u |S_u|^2),

and (2) proves (4). This holds for every flat row probe, regardless of
its phase. It is a consequence of existing second moments; it does not
prove a new correlated second moment of the product.

## 2. Optional exact reflection check

Fix the finitely many row/column ray classes required by reciprocity.
The character in S_u is a fixed finite twist of the primitive sextic
character modulo u, with its original fixed-S deletions retained.
For squarefree good u its primitive conductor norm is

    Q_u=c_sector*Nu,

where c_sector is fixed within the finite sector. Its normalized Gauss
root has the exact form

    epsilon(psi_u)=gamma_1(u)*b_u,   |b_u|=1,           (5)

where b_u retains the fixed local, supplementary, unit, and finite-ray
phases. These phases may depend on u. They need not be declared constant:
after the cancellation below they are bounded ROW multipliers.

Primitive GL1 Poisson at the central normalization gives

    N^(-1/2) sum_n psi_u^*(n) W(Nn/N)
      =epsilon(psi_u) H_u^(-1/2)
            sum_h conjugate(psi_u^*(h)) Wdot(Nh/H_u),
    H_u=C_u/N≈U^(1/2),
    C_u=3Q_u/(2pi)^2.                                  (6)

Here C_u is the conductor SCALE in the pinned source's normalization;
Q_u/N alone is only a comparable scale. Wdot is normalized accordingly,
including the fixed field constants. It is the exact GL1 transform of W,
smooth and rapidly
decreasing at infinity, with its bounded-end behavior included. The
fixed missing Euler factors produce finitely many terms of the same
form at fixed rescaled lengths. No zero factor at a shared prime is
divided out. In particular the row character remains zero at primes
of u on both sides.

If a dual sum includes primes of the fixed set S, retain all their
powers. Writing h=h_S*h_good gives an absolutely summable normalized
coefficient mass `sum_(h_S S-supported)(Nh_S)^(-1/2)<infinity`.
Their phases become bounded row factors. This is an optional completion,
not an instruction to delete those indices.

Let T_u denote the sum of the complete dual terms after removing the
factor gamma_1(u). Equations (5)--(6), including fixed deletion terms,
give exactly

    conjugate(gamma_1(u)) S_u(N;W_S)=T_u,
    sum_(u squarefree,Nu≈U) |T_u|^2
                           <<_epsilon U^(1+epsilon).   (7)

The second assertion is justified in Section 3. Inserting the FIRST,
exact identity into (3), then applying Cauchy to the full row sum, gives

    |B|^2 <= C/U * (sum_u |M_u|^2)(sum_u |T_u|^2).

Now (2) and (7) give the same bound (4). This is a consistency check on
the actual transposed orientation. The direct original-factor proof
above is shorter and already has the same strength at this corner.

## 3. The complete dual plain norm, including its tails

For an annular plain polynomial of length H with bounded coefficients,
the all-element smooth row mean satisfies

    sum_(Nu≈U) |H^(-1/2) sum_(Nh≈H) b_h chi_h(u)|^2
                         <<_epsilon (UH)^epsilon(U+H^2). (8)

Every power of h is allowed. One proof is precisely
`MIXED_CONDUCTOR_SECTOR.md`, Sections 2--3, applied to the coefficient
vector `b_h/sqrt(H)`. Its primitive pair conductor is at most O(H^2).
The principal pairs cost U; all nonprincipal pairs cost O(H^2), with
their complete shared-prime zero masks. That proof only uses the bound
on the coefficients, so fixed local coefficient sectors cause no loss.
For this auxiliary POSITIVE norm, enlarging squarefree rows to all
element rows before expansion is legitimate.

Use a smooth dyadic partition of the exact transformed sum in (6),
with H_0=U^(1/2). At each dyadic H it is an H-centrally-normalized
plain polynomial multiplied by `sqrt(H/H_0)`. Its profile has uniform
size O(1) for H<=H_0, and O_A((H/H_0)^(-A)) for H>=H_0.
The same bounds hold for the finitely many derivatives invoked in
common parameter separation. Hence Minkowski and (8) give the full
root norm bound

    C_epsilon sum_(H dyadic,nonempty)
        sqrt(H/H_0) min(1,(H/H_0)^(-A))
                            [sqrt(U)+H]*(UH)^epsilon
                      <<_epsilon U^(1/2+epsilon),     (9)

by taking A sufficiently large. The H<=H_0 part is a convergent
geometric sum toward H_0; the H>=H_0 part is another convergent
geometric sum. Empty subunit annuli contribute zero. Thus the entire
infinite dual tail is paid, not truncated at its nominal scale.

The actual H_u/H_0 is a smooth bounded positive function of Nu/U and
the fixed sector. A common parameter Sobolev/Fourier separation on
that compact interval gives (9) with uniform seminorms. It does not
permit independent arbitrary arithmetic coefficients in each row.
The original height has a fixed polynomial cost in these bounds;
as in the source, its small power cutoff is chosen after that order.
This proves the second assertion in (7).

## 4. Which transposed bad mode has actually been controlled

Let T have rows u in the U annulus and columns A in a fixed annular
envelope of L=DN=U^(3/2), large enough to contain every original
product in (1), and entries

    T_(u,A)=chi_A(u).

The coefficient vector c_A is the COMPLETE convolution in (1), so
`(Tc)_u=f_u` exactly. Powerful A and shared d,n primes are included.

Xu--Sang's explicit coefficient vector for the TRANSPOSED matrix has

    lambda_u=U^(-1) W(Nu/U)(Nu/U)^(-1/2)
                    conjugate(gamma_1(u))*eta(u),       (10)

with its squarefree, fixed-good-prime, and fixed-ray restrictions.
Their Section 5.5 gives this formula; Section 6 changes vectors only
in the later squarefree-row transfer, which we do not invoke here.
The relevant row probe for T* is

    alpha=sqrt(U)*conjugate(lambda),

up to a fixed normalization constant. In particular

    <Tc,alpha>=sqrt(U) sum_u lambda_u f_u,

which has the conjugate-gamma weight in (3). Conjugating lambda the
wrong way here would fail to cancel the root in (6).

The fixed reciprocity sign is constant on each chosen pair of ray
classes and is absorbed in the corresponding bounded row multiplier.
Equivalently, for a fixed row ray class it is a unit phase on the
transposed output classes, preserving their norm.

Let `v=T*alpha`, with ALL columns in that envelope. The known
unrestricted-row lower construction at lengths A=L, B=U applies
because, for any fixed `0<delta<1/22`,

    U^(16/11+delta) <= L=U^(3/2) <= U^(2-delta).

The source row profile can be chosen within this annular column
envelope. This particular lower construction sums unrestricted ideal
rows A, which are precisely the unrestricted columns allowed in v.
No claim that its squarefree A subset retains the same lower bound
is needed or inferred; the later squarefree-row transfer may change
the vector and is not used.
For the specified fixed-data nonzero vector, `||alpha||_2≈1` and

    ||v||_2^2 >>_epsilon L^(5/6)U^(1/3)U^(-epsilon)
                           =U^(19/12-epsilon).        (11)

Our actual overlap estimate is

    |<c,v>|^2=|<Tc,alpha>|^2 <<_epsilon U^(1+epsilon).

Consequently the unit-normalized induced COLUMN mode has overlap

    |<c,v/||v||>|^2 <<_epsilon U^(-7/12+epsilon).        (12)

This controls the actual induced Gauss-character-average mode, rather
than identifying it with bare gamma_1(A). The same RAW pairing bound
holds with any further bounded row multipliers in (10), including
moving numerator-character twists and zero masks. A lower bound such
as (11) for a heavily modified vector requires its own hypothesis;
it is not inherited automatically.

## 5. What remains before an improving mean can follow

The generic sextic operator can still have other bad directions.
Neither the lower-bound construction nor (12) supplies a decomposition
of its positive quadratic form into these modes plus a paid remainder.
Thus (4) and (12) do not imply `sum_u|M_u S_u|^2<<U^(1+epsilon)`.
They remove one actual, quantitatively large obstruction for this
specific mixed vector and its bounded row-probe family, using its
already available individual second moments. This is not a new full
mixed-moment saving.

The complete actual-row small-conductor form is separately paid in
`ACTUAL_SIXTHFREE_SECTOR.md` by `U^(13/12+epsilon)` at cutoff Q=U.
The remaining large-conductor signed form still needs an estimate.
An upper exponent below about 1.20783 at this corner would be useful
for the source's reported working boundary, but the entire witness
length consumer must also be checked before asserting a new boundary.

Primary interfaces: the source inverse-amplification statement was
read directly in its saved TeX; the primitive normalized Poisson
formula is also [Blomer--Goldmakher--Louvel, arXiv:1112.1650v1,
Lemma 2.2](https://arxiv.org/pdf/1112.1650), PDF page 6.
The exact explicit bad vector and its range are
[Xu--Sang, arXiv:2610.17675v1, Sections 3 and 5.5](https://arxiv.org/html/2610.17675v1#S5.SS5).
Both primary external sources were read directly. The Eisenstein
teammate independently reconstructed the root cancellation, actual
boundary inverse exponent, and fixed-mask completion before this draft.
This is internal component feedback, not final-SHA acceptance.
