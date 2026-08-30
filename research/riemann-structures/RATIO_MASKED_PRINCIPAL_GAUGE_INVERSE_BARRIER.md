# The ratio-masked principal gauge can have a power-sized true inverse

Status: proposed cofinal operator obstruction with an exact finite source
adapter and bounded replay. No RH or native full-moment counterexample.

Scope: the coefficient-recombined squarefree-core gauge and principal weighted
record norm of `PHASE_PROTECTED_PRINCIPAL_GAUGE_TRANSFER.md`, at tau=1/2, with a
global maximum physical horizon and the literal ratio-eight mask. Every record
in the constructed interval is Boolean balanced at the same frozen cutoff,
has clean fixed owners, fixed least phases, and small enough common core. The
interval spans multiple physical dyadic shells. It is not contained in one
unchanged narrow output shell, and is not asserted to be the complete actual
balanced-source coefficient vector or its literal gamma-diagonal resolution.

Exact sources: L-102706 gauge, L-106080 Boolean row, L-106090/L-106120 native
incidence, L-106121/T-106140 diagonal weight, and the frozen protected-transfer
note. The producer authenticates these fixed Git blobs. The Segre-poset
combinatorics are classical; the source gauge, mask, weight and balanced-row
embedding below are the contribution.

What was actually run: a fixed m=3 prime-certified panel, exact matrix inverse,
complete small Boolean allocations, and bounded combinatorial controls are
supplied. The exact-SHA review records execution. The asymptotic claim is
proved, not extrapolated from that small panel.

Smallest remaining gap to a conclusion-facing use: this is an instantaneous
coefficient-record inverse, not a bound or lower bound for the complete
integrated family. The source connection cancellation from
`NATIVE_PHASE_LEAKAGE_CONNECTION_CANCELLATION.md` remains valid.

## 1. Statement and why the physical weight matters

Let A_H be the true fixed-phase gauge compression from PPT, now compressed
also to 1/8<N/M<8, and retain all records up to N,M<=H. Work in the norm with

\[
 w=g^2\ell\rho c_\ell c_\rho,\qquad c_q=(q+1)/(q-1).
\]

The matrix is triangular with diagonal one, hence has a true finite inverse.

**RMI-1.** For a cofinal sequence H there are legal clean fixed-owner,
fixed-phase Boolean-balanced record intervals such that

\[
 \|A_H^{-1}\|_{w\to w}\ \ge H^{1/12-o(1)}.                    \tag{1}
\]

The forward matrix still has the subpower bound proved in PPT. Thus the
absolute Schur estimate after an entry deletion does not prove an analogous
bound for the newly inverted matrix.

This is not factorial growth stripped of source amplitude. Every insertion
in this interval moves an opposite residual prime into the common core. Its
raw gauge coefficient a_tau/p is multiplied by the principal norm-weight
ratio g_new/g_old=p. The weighted coefficient is **exactly a_tau**, so the
inverse entry at tau=1/2 is

\[
 \mu_m\,16^{-2m}.                                             \tag{2}
\]

Its factorial growth beats the remaining 16^(-2m) activity. Unit label and
Mellin phases factor by endpoints and do not change its modulus.

## 2. Prime windows and the complete source interval

Fix ell=5,rho=13, owners P=31*37,Q=11*17. For large L put

\[
 m=\left\lfloor{1\over100}\sqrt{L/\log L}\right\rfloor.
\]

There exist 2m distinct primes r_1,...,r_m,s_1,...,s_m in one interval

\[
 [q,q(1+1/(100m))],\qquad L\le q\le2L.                       \tag{3}
\]

Only ordinary PNT is needed. Partition [L,2L] into 100m equal bins. If every
bin contained fewer than 2m primes, their total would be <200m^2, whereas
PNT gives at least L/(2 log L) primes for large L. Since
200m^2<=L/(50 log L), some bin suffices; its relative width is at most
1/(100m). No uniform shrinking-window PNT is invoked.

Put T=product_i r_i s_i. Ordinary fixed-relative-interval PNT also supplies
four distinct background primes in the following disjoint windows:

\[
 1000T<A<1050T,\quad1050T<B<1100T,
\]
\[
 1100T<C<1150T,\quad1150T<D<1200T.                            \tag{4}
\]

The [prime number theorem](https://kskedlaya.org/ant/chap-primes-in-ap.html)
is the only imported prime-distribution input. All primes avoid 67 and the
fixed owners/phases for large L.

For subsets I,J of {1,...,m}, use cores

\[
 a_{I,J}=5AB\left(\prod_i r_i\right)\left(\prod_{i\in I}s_i\right),
\]
\[
 b_{I,J}=13CD\left(\prod_i s_i\right)\left(\prod_{j\in J}r_j\right).
                                                               \tag{5}
\]

Only I affects a and only J affects b. The common core is

\[
 g_{I,J}=\prod_{i\in I}s_i\prod_{j\in J}r_j\le T.
\]

The mandatory 5 and 13 remain the least exclusive primes throughout; all
background and variable primes are larger. Owners and core supports are
clean. The background primes stay exclusive, rather than creating a large
common core.

Choose

\[
 H=31603(CDT)^2,\qquad U=\lfloor H^{1/6}\rfloor.               \tag{6}
\]

All physical N=P a^2 and M=Q b^2 lie below H, because
25P=28675<31603=169Q and AB<CD. The elementary bounds

\[
 500T<H^{1/6}<672T
\]

follow from 5<31603^(1/6)<6 and
100^3<1265000<CD/T^2<1380000<112^3. In particular

\[
 13T<U<\min(A,B,C,D),\qquad g\le T<U^2/4.                    \tag{7}
\]

The same inequalities hold if the cutoff is rounded down to the next dyadic
power. Thus the example does not hide in a discarded very-large-common-core
sector.

**RMI-2 (complete Boolean support).** Every core in (5) has precisely two
nonzero balanced histories at cutoff U. On the left these are (A,B,s) and
(B,A,s), where s=a/(AB), and the balanced coefficient is 2mu(s). The analogous
right histories are (C,D,s') and swap.

Proof. Every divisor of s is at most 13T<U. With the frozen convention
a_U=epsilon-mu_U*1, a_U vanishes on every entirely small group, including the
empty group. For a group consisting of at least one of its two large primes
and a small part t, the truncated divisor sum is sum_(d|t)mu(d), so a_U=-1
if t=1 and zero otherwise. A nonzero product of the two a_U factors must
therefore put one distinct large prime in each, and no small prime in either.
All small primes belong to the third mu factor. These are exactly the two
claimed histories, including all allocations involving 1 and both large
primes in the same group. The Boolean row is nonzero at every interval
record. This is a support statement, not a replacement of transported owner
shares by freshly allocated shares.

## 3. The physical ratio mask is exactly the balanced Boolean poset

Write

\[
 c_0={28675\over31603}\left({AB\over CD}\right)^2.
\]

The windows imply 1/2<c_0<1. Factoring each variable prime as q times a
number in [1,1+1/(100m)] gives

\[
 {N_{I,J}\over M_{I,J}}
  =c_0 q^{2(|I|-|J|)}E_{I,J},\qquad 1/2<E_{I,J}<2.            \tag{8}
\]

For example the absolute log of E is at most
4m log(1+1/(100m))<1/25<log 2. If |I|=|J|, (8) belongs to (1/4,2), hence
passes the ratio mask. If the ranks differ, q>100 makes the ratio either
greater than 8 or smaller than 1/8. Therefore precisely the states

\[
 \mathcal S_m=\{(I,J):|I|=|J|\}
\]

remain. Order is inclusion in both coordinates. This is the Segre square of
the Boolean lattice, whose rank-j size is binom(m,j)^2.

All transitions between these states insert only an opposite residual prime.
After conjugation by sqrt(w), the forward entry from (I,J) to (I',J') is
a_tau^(|I'\I|+|J'\J|) times a common endpoint phase whenever both inclusions
hold, and is zero otherwise. This is a diagonally weighted zeta matrix.
Its inverse has the corresponding poset Möbius coefficients.

Crucially, this is an entry of the **full** triangular protected,
horizon-plus-ratio inverse. Any path from the bottom record to the top record
can only add the variable primes displayed in (5). It cannot add an outside
prime, make an exclusive background common, or remove any original support
and still reach the top. Thus no outside record changes this interval's
Möbius coefficient.

## 4. Elementary factorial lower bound, including all gauge activity

Let mu_m be the bottom-to-top Möbius number of S_m. The interval below a
rank-j state is S_j, so

\[
 \mu_0=1,\qquad
 \mu_m=-\sum_{j=0}^{m-1}\binom mj^2\mu_j.                    \tag{9}
\]

The first values are 1,-1,3,-19,211. Its standard interpretation is

\[
 \mu_m=(-1)^m C_m,
\]

where C_m counts ordered pairs of permutations of m letters having no common
ascent. This is classical, for example [Li and Sundaram, Proposition
2.5](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/151.pdf). Here is a
complete elementary proof of the part used.

Inclusion-exclusion over positions where both permutations ascend gives a
sum over compositions m=l_1+...+l_r. A specified common-ascent block of size
l has l! possible relative orders, exactly one increasing order. Hence

\[
 C_m=\sum_{l_1+\cdots+l_r=m}
       (-1)^{m-r}{(m!)^2\over\prod_i(l_i!)^2}.                \tag{10}
\]

Expanding the reciprocal of sum_(j>=0)z^j/(j!)^2 shows that (9), divided by
(m!)^2, has the same composition sum with sign (-1)^r. This proves the
identity, without importing Bessel zero asymptotics.

Require the first permutation to descend at every odd position and the
second to descend at every even position. These constraints exclude a common
ascent everywhere. Within each permutation the constrained adjacent pairs
are disjoint, so exactly half of their orders are allowed independently.
Consequently

\[
 {(m!)^2\over2^{m-1}}\le C_m\le(m!)^2.                       \tag{11}
\]

At tau=1/2, |a_tau|=1/16. The logarithm of the weighted inverse entry (2) is
therefore

\[
 \log(C_m16^{-2m})=2m\log m+O(m).                            \tag{12}
\]

There is no missing product of reciprocal primes in (12): (2) was derived
after the exact principal weight conjugation, not by discarding it.

Since m is as chosen above, log L=2log m+O(log log m). Equations (3)--(6)
give log T=2m log L+O(m) and log H=6log T+O(1). Combining with (12) proves

\[
 C_m16^{-2m}=H^{1/12+o(1)},
\]

which implies RMI-1. The same lower bound holds in the weighted record
Hilbert space integrated against the native Mellin measure: a single input
column and its output have a common endpoint unit phase, and the common
positive mass Gamma(0) cancels from their norm ratio.

## 5. Exact limits: one fixed narrow shell behaves differently

If each physical coordinate is restricted to one unchanged interval of
multiplicative width strictly less than 9, every nonidentity odd-prime square
insertion leaves that interval. On the purely odd squarefree gauge sector,
compression to that same narrow two-coordinate shell is therefore the
identity. If prime 2 is permitted, its square shift needs separate treatment.

The constructed Segre interval crosses many such shells. It proves a real
obstruction to inverting the **global** protected gauge after imposing the
coupled ratio mask; it does not prove an obstruction to an unchanged-shell
identity map or to the original fixed-Y principal moment.

Likewise a legal Boolean support and an operator-norm lower bound do not
identify the normalized worst input column with the complete canonical
source vector. Absolute source amplitudes may be small, and homotopy
integration with the full connection may cancel it. No contradiction to the
paid native diagonal, no full family lower bound, and no RH conclusion follows.

## 6. Bounded replay and next interface

The fixed m=3 panel has 64 interval records and exactly 20 ratio-admissible
records. Six small primes are checked by complete trial division. Four large
background primes carry explicit Proth certificates; the checker proves the
certificate conditions and never accepts a probable-prime flag. It checks
all 64 native selectors, physical bounds, common cores and Boolean support
inequalities. It enumerates complete Boolean allocations at the two endpoints
on both sides, and directly inverts the 20x20 weighted gauge matrix.

Independent controls compare (9) with explicit permutation-pair counts at
small m and verify the elementary factorial lower bound at bounded m. The
finite matrix entry -19/16^6 is small; the cofinal theorem, not this fixture,
asserts eventual power growth. No large matrix, prime sweep, or fitted
asymptotic is used.

The primality implication is elementary: if n=k*2^s+1 with k odd and k<2^s
has a witness a^((n-1)/2)=-1 modulo n, every prime divisor of n is 1 modulo
2^s. A composite n would consequently be at least (2^s+1)^2, contradicting
n<2^(2s)+1. The published certificates include k,s,a and are replayed with
exact modular exponentiation.

Together with PPT and PLC this isolates the actual choices: keep the
unmasked finite-horizon inverse, transport shell boundaries explicitly, or
retain and recombine the source connection before seeking an integrated
estimate. A subpower inverse after arbitrary physical masking is no longer
an available shortcut.
