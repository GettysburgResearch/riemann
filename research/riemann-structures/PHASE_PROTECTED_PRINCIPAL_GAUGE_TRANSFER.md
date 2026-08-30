# Phase-protected principal gauge transport and its true inverse

Status: proposed theorem with an exact bounded replay; no RH conclusion.

Scope: the coefficient-recombined, squarefree-core sector of the frozen native
prime-square gauge, with fixed clean owner pairs and fixed canonical phase
primes. This gives a positive principal-weighted operator theorem. It does not
identify this record resolution with every literal carrier/history atom in
T-106140. The off-sector selector transition in
`PRINCIPAL_SELECTOR_GAUGE_OBSTRUCTION.md` is deliberately not discarded from the
full problem.

Exact sources: the producer authenticates the old L-102706 gauge, the FAMILY
L-106090/L-106120/L-106121/T-106140 source, and the frozen gauge-connection and
principal-selector notes, by commit and Git blob. All local coefficients below
come from that gauge, not from a newly chosen norm-preserving operator.

What was actually run: a bounded exact-rational producer and regression suite
are supplied; their run status belongs to the exact-SHA review. The proof of the
uniform horizon bound is analytic, not inferred from the 24-record fixture.

Smallest remaining gap: a norm-controlled adapter from the complete retained
native source, including off-sector selector changes and its actual diagonal
measure, to this protected coefficient-record resolution.

## 1. The declared source resolution and weighted Hilbert space

Fix disjoint squarefree two-prime owners P,Q and distinct odd primes ell,rho,
all avoiding the duplicated physical label 67. Retain the owner slots and all
spectator source labels. For squarefree cores a,b, disjoint from P Q and 67, set

    N=P a^2, M=Q b^2, g=gcd(a,b), c=a/g, d=b/g,
    least(c)=ell, least(d)=rho.

Both reduced cores are nontrivial. Use the actual principal diagonal weight

\[
 w(a,b)=g^2\ell\rho c_\ell c_\rho,
 \qquad c_q=(q+1)/(q-1).                                      \tag{1}
\]

For each finite physical horizon H, take the record Hilbert space with
N,M <= H and squared norm sum w(a,b)|z_(a,b)|^2. This is the diagonal record
norm, not a claim about a physical-product quotient or a recombined family
square. An arbitrary fixed spectator Hilbert space may be tensored on.

The native local gauge has zero linear coefficient and quadratic coefficient

\[
 [x_p^2]g_\tau=-\tau(1-\tau)/4=:a_\tau,
 \quad 0\le\tau\le1.                                         \tag{2}
\]

Its physical square insertion coefficient is a_tau/p, with the primitive
label phase and the Mellin translation p^(-2it) retained as unit factors.
First form the local gauge product, then apply the **linear coefficient
projection** retaining core exponents 0 or 2 on each side. This combines equal
local coefficient histories; it is not an algebra quotient killing x_p while
keeping x_p^2, and is not an assertion about a counting measure on Taylor words.
All the results below use this specified resolution.

Let L,R insert a missing core prime on the indicated side. Before weighting,
the two-sided local operator is

\[
 (I+(a_\tau/p)L)(I+(a_\tau/p)R), \qquad L^2=R^2=0.              \tag{3}
\]

Conjugation by sqrt(w), whose local common-prime multiplier is p, gives, in
the state order 00,10,01,11, the nonidentity entries

\[
 00\to10,01:\ a_\tau/p;\qquad
 00\to11:\ a_\tau^2/p;\qquad
 10,01\to11:\ a_\tau.                                        \tag{4}
\]

With different unit phases on the two sides, use a_L,a_R in (4) and a_L a_R
in its quadratic entry. All cancellations and absolute estimates below remain
valid. These phases are independent of the homotopy parameter tau.

## 2. Fixed phases factor locally, but inversion changes

Assume ell<rho; interchange left/right otherwise. The fixed-phase projection
has these exact local allowed states:

| Prime | Allowed core states |
| --- | --- |
| p divides P Q, or p=67 | 00 |
| p=ell | 10 |
| p=rho | 01 |
| p<ell, otherwise | 00,11 |
| ell<p<rho, otherwise | 00,10,11 |
| p>rho, otherwise | 00,10,01,11 |

Indeed an exclusive left prime cannot lie below ell, an exclusive right prime
cannot lie below rho, and the two least primes must occur exclusively on their
declared sides. Common primes do not affect either selector. Thus the
protected operator A_tau=P_phase G_tau P_phase is a product of precisely these
compressed local blocks.

**PPT-1 (true protected inverse).** On every finite alphabet and downward
physical horizon, A_tau is invertible. Its local inverse has diagonal one and:

* below ell, the sole corner 00->11 is **-a_tau^2/p**;
* between ell and rho, the edges 00->10 and 10->11 are -a_tau/p and -a_tau,
  while the direct corner 00->11 is **zero**;
* above rho, replace a_tau by -a_tau in the full four-state block, leaving its
  quadratic corner +a_tau^2/p;
* mandatory one-state blocks are the identity.

Proof. In the two-state block, invert I+T by I-T. In the three-state block,
the square of the two-edge nilpotent part contributes a_tau^2/p, cancelling
the direct corner in I-T+T^2. In the four-state block, (3) has inverse
(I-(a_tau/p)R)(I-(a_tau/p)L); weight conjugation gives the displayed result.
Tensor the local inverses. Every nonzero transition only adds core primes, so
every intermediate physical pair lies below its final pair. Therefore the
restriction to N,M<=H still preserves both inverse identities. This is a
finite nilpotent polynomial inverse, not an untruncated formal-series claim.

In particular,

\[
 (P_{\rm phase}G_\tau P_{\rm phase})^{-1}
 \ne P_{\rm phase}G_\tau^{-1}P_{\rm phase}                    \tag{5}
\]

in general. The negative low-prime corner already proves (5). This is the
required return-path correction to phase protection.

## 3. A uniform subpower principal-weighted bound

Put

\[
 A=1/16,\quad B=2A+A^2=33/256,\quad
 F=1+B=289/256,\quad K(H)=\max_{n\le H}\omega(n),
\]
\[
 \mathcal B_H=F^{K(H)}\prod_{p\le H}(1+B/p).                  \tag{6}
\]

**PPT-2 (protected weighted transfer).** Uniformly in all clean fixed owners,
phase primes, finite alphabets, primitive unit phases and tau in [0,1],

\[
 \|A_\tau\|_{w\to w},\ \|A_\tau^{-1}\|_{w\to w}
 \le\mathcal B_H=H^{o(1)}.                                   \tag{7}
\]

The same upper bound holds after any entrywise deletion from either matrix
separately; this last assertion does not identify the two deleted matrices as
inverses.

Proof. In the weighted coordinates (4), every local absolute row or column
sum of the forward block or its **true** protected inverse is bounded by F
when the corresponding input or output contains that prime. A column with
state 00 instead has sum at most

    1+2A/p+A^2/p = 1+B/p.

A row with state 00 has sum one. The smaller protected blocks and their true
inverses only improve these estimates. In a fixed record, the number of
occupied primes is at most omega(ab). Since ab<=H/sqrt(PQ)<=H, this is at most
K(H). Multiplying the local majorants gives both the maximum row and the
maximum column bound (6). Horizon restrictions and entrywise masks only
delete terms from these absolute sums. The Schur test proves (7).

For completeness, n with k distinct prime divisors is at least k!, so
K(H)<=(1+o(1))log H/log log H by the elementary factorial estimate. The
classical prime harmonic estimate sum_(p<=H)1/p=log log H+O(1), also used in
the frozen native gauge estimate, gives

\[
 \log\mathcal B_H\le(\log F+o(1)){\log H\over\log\log H}
       +B\log\log H+O(1)=o(\log H).                          \tag{8}
\]

The o(1) here is independent of ell,rho,P,Q. This does not assert a
polylogarithmic bound: the occupied-prime factor F^K(H) was retained.

**PPT-3 (the actual homotopy first jet).** For H large enough to contain a
record, both A_tau' and (A_tau^-1)' have operator norm at most
8K(H) B_H. Consequently the field/derivative map

\[
 \binom{f}{f'}\longmapsto
 \begin{pmatrix}A_\tau&0\\A_\tau'&A_\tau\end{pmatrix}
 \binom{f}{f'}                                                \tag{9}
\]

and its inverse have H^o(1) bounds in this weighted record space.

Proof. Each nonzero coefficient of either matrix is a signed monomial in
a_tau, times a rational prime factor and unit phases. Its degree is at most
2K(H). Since |a_tau|<=A and |a_tau'|<=1/4=4A, its derivative is bounded by
8K(H) times the same fixed-A absolute majorant. This argument remains valid
at a_tau=0 and never divides by a_tau. Apply the preceding row/column proof.
The inverse jet is the derivative of the true protected inverse; equivalently
its lower-left block is -A_tau^-1 A_tau' A_tau^-1. Bounding directly by
(A_tau^-1)' avoids an unnecessary extra product of Schur bounds.

The bounds are pointwise in the Mellin variable t, so they integrate against
the frozen nonnegative |kappa-hat(t)|^2 dt measure and any retained probability
measure on spectator labels. They apply to the weighted record diagonal
integral. They do not by themselves bound the norm of the scalar field obtained
by summing records, nor the native principal family square.

## 4. Physical shell masks retain the bound but can destroy inversion

The distinction is visible with actual clean records. Take

    ell=5, rho=13, P=31*37, Q=11*17,
    base cores a=5, b=13, variable primes 3,7,29.

The fixed-phase tensor space has 2*3*4=24 records. Its base physical pair is
(28675,31603), whose ratio is in (1/8,8). Adding 29 to both cores multiplies
both outputs by 841, remains below H=10^8, and preserves the ratio. Adding
29 to only one core violates the ratio-eight condition.

For this two-endpoint transition, the full four-state forward and inverse
corners are each +a_tau^2/29. The two single-side intermediates are the paths
that cancel their sum in the full inverse product. The ratio mask deletes
both intermediates. Thus the corresponding corner of the product of masked
forward and masked full-inverse matrices is

\[
 2a_\tau^2/29\ne0\quad(0<\tau<1).                            \tag{10}
\]

Both individually still obey (7). A separate inversion of a shell-restricted
matrix needs its own path analysis; it is not supplied by an entry deletion
argument. In particular a lower dyadic shell, a physical ratio mask, a Boolean
cutoff, and a source history restriction must not be conflated with the
downward maximum horizon used in PPT-1.

## 5. Replay and exact boundary to the full programme

The producer uses only 24-record rational matrices and a fixed three-prime
alphabet. It constructs the forward matrix twice: directly from raw square
insertions plus the exact g-weight ratio, and from the protected local blocks.
It checks both true inverse identities, the derivative inverse identity,
finite absolute Schur bounds, horizon restriction, the wrong compressed
inverse, and the explicit ratio-mask failure (10). Hostile tests cover unsafe
parameter types, dimension caps, source mutation, and JSON numeric-type
substitution. No numerical singular values or asymptotic experiments are used.

This packet supplies a positive replacement for the failed **uniform
source-blind** gauge shortcut: phase-preserving transport has a uniform
subpower bound, with an exact inverse and its connection term. It also locates
two remaining interfaces rather than declaring them solved:

1. The complete gauge has off-sector blocks that change the least discrepancy
   prime. The frozen selector example gives a power-sized weighted entry
   there. Summing the protected estimates does not control those blocks.
2. The complete native paid diagonal retains Boolean, owner, renewal, carrier,
   endpoint and color data. Our local coefficient recombination must be shown
   bounded in that exact measure, or the measure must be transported with its
   correction. Neither an arbitrary word-counting diagonal nor a scalar
   physical quotient can be substituted for it.

The protected first-jet theorem is therefore a genuine limited-sector source
transport result, not the missing full principal moment estimate and not an
effective-rank or RH theorem.
