# Canonical conductor reselection can turn a small gauge coefficient into a power loss

Status: **an exact source-operator obstruction to uniform subpower gauge
transfer in the canonical principal weight**.

This is not a lower bound for the complete principal moment of T-106140.
It tests a proposed uniform operator estimate on its clean source-record
geometry, using the actual Euler/half-divisor gauge coefficient. The example
uses a direct sum of input and output physical shells on one finite horizon;
it does not fit both physical products into one unchanged width-eight shell.
Every individual interaction obeys the native ratio-eight condition.

Sources: L-102706 at ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc;
L-106080/090/120/121 and T-106140 at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b. The canonical equal-pair owner
coordinate and the two reduced-core phase primes are distinct source labels.

## 1. The exact principal weight on a clean record

A record has physical products

\[
 N=P a^2=P g^2c^2,\qquad M=Q b^2=Q g^2d^2,
 \quad g=(a,b),\quad(c,d)=1,\quad c,d>1,
\]

with all owner/core cleanliness conditions retained. Put

\[
 \ell=P^-(c),\quad\rho=P^-(d),\quad
 c_q={q+1\over q-1},\qquad
 w(g,\ell,\rho)=g^2\ell\rho c_\ell c_\rho.       \tag{1}
\]

This is exactly the weight of a literal atomic term in the principal diagonal
T-106140.9. For a coefficient function z(t), its contribution is
w integral |kappa_hat(t)|^2 |z(t)|^2 dt/(2pi).
All quadratic classes are retained; changing a phase prime may move a record
to a different class, which is not discarded.

For the source gauge at parameter tau, the local coefficient is

\[
 [x_p^2]g_\tau=-\tau(1-\tau)/4.
\]

Since x_p^2=p^-1 exp(-2i theta_p)U_(p^2), its actual physical coefficient
on a left square insertion is

\[
 b_p(\tau)=-{\tau(1-\tau)\over4p}.             \tag{2}
\]

The phase has modulus one. The gauge acting on both source sides still has
this exact matrix entry when the right side uses its constant term.

## 2. PSG-1: the selector cocycle of one insertion

Suppose p divides d but not a or the owners, and d/p>1. Inserting p^2 on the
left produces

\[
 a'=pa,\quad b'=b,\quad
 g'=pg,\quad c'=c,\quad d'=d/p,
 \quad\rho'=P^-(d/p),\quad\ell'=\ell.          \tag{3}
\]

The canonical common core and least phase prime must be recomputed: keeping
the old rho when it has become common would violate the clean phase
condition. Equations (1)--(3) give the exact weighted matrix-entry square

\[
 \boxed{
 |b_p(\tau)|^2{w(g',\ell',\rho')\over w(g,\ell,\rho)}
 ={\tau^2(1-\tau)^2\over16}
       {\rho'c_{\rho'}\over\rho c_\rho}.}       \tag{4}
\]

The factor p^-2 has cancelled the common-core weight gain p^2. If p>rho,
then rho'=rho and there is no conductor jump. If p=rho, the next prime in
d can be arbitrarily larger. This is the specific transition that a uniform
weighted gauge estimate must pay.

This is also compatible with the source coefficient normalization. If
z=gamma/(g^2cd sqrt(PQ)), then after insertion the denominator increases by p.
After stripping the displayed unit label phase, gamma is multiplied only by
-tau(1-tau)/4. If that phase is retained inside gamma, multiply also by
exp(-2i theta_p). The allowed subpower bound on its modulus remains intact;
it does not control the ratio of the principal weights.
The square insertion is retained as gauge provenance, with the original owner
history and share. It is not silently identified with a newly reallocated
equal-pair occurrence. A different reallocation needs its own exact adapter.

## 3. PSG-2: legal source records with a power-size transition

Fix P=11*13=143, Q=17*19=323, and choose four distinct primes in the disjoint
fixed windows

\[
 \begin{aligned}
 A&\in(T,1.01T),&B&\in(1.02T,1.03T),\\
 C&\in(1.20T,1.21T),&D&\in(1.22T,1.23T).
 \end{aligned}                                  \tag{5}
\]

Let a=5AB, b=3CD. Initially g=1, c=5AB, d=3CD, ell=5, rho=3. Insert3^2
on the left. The new record has g'=3, c'=5AB, d'=CD and rho'=C. All primes
are distinct apart from the intended common3; none is67. Both records have
two nontrivial reduced cores, four distinct owner primes, and clean opposite
owner/core incidence. The canonical equal-pair gauge permits these owners;
no minimum-owner or largest-owner gauge is silently substituted.

The physical ratios are

\[
 {N\over M}={3575\over2907}\left({AB\over CD}\right)^2,
 \qquad {N'\over M}=9{N\over M}.                \tag{6}
\]

The endpoint bounds in (5) place N/M strictly between1/2 and2/3, and N'/M
strictly between9/2 and6. Thus both interactions satisfy ratio-eight physical
comparability with room to spare. They occupy different shell blocks:
N'/N=9 prevents a common multiplicative-width-eight window. The complete
finite-horizon direct sum retains both legitimate blocks and their shell tags.

Take H=40000 T^4; every displayed product is below H. For sufficiently large
T, the dyadic Vaughan cutoffs comparable to H^(1/6) are below all four large
primes and above15. Hence both original three-prime cores have exactly two
balanced histories of coefficient-1, and the new left four-prime core has
exactly two balanced histories of coefficient+1. These are live Boolean
records, not formally convenient core values with zero balanced coefficient.
This support check does not identify the transported gauge-history coefficient
with the complete new Boolean coefficient; those source labels remain distinct.
The bounded replay checks the literal allocations. The prime number theorem
in fixed proportional intervals supplies such records for all sufficiently
large T; only this classical existence theorem is imported.
For a primary author reference see
[Kedlaya, Theorem4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html),
with the modulus fixed (ordinary prime counting suffices here).

The weights are exactly

\[
 w_0=45,\qquad w_1={135\over2}C c_C.            \tag{7}
\]

At tau=1/2 the actual gauge entry is-1/48. Therefore

\[
 \boxed{|b_3(1/2)|^2w_1/w_0={C c_C\over1536}.}  \tag{8}
\]

The source operator on this direct sum of clean weighted records consequently
has norm at least sqrt(C c_C/1536)=Omega(H^(1/8)). No bound H^o(1) can hold
uniformly for this canonically reselected weighted gauge operator.
This is a statement about the proposed operator norm, not the value of the
operator on the complete unprojected source vector.

For a declared Lebesgue parameter norm, a constant input coefficient gives
the equally exact squared ratio C c_C/2880. The phenomenon is not restricted
to a single parameter point. It also occurs for the literal bilateral Euler
coefficient path f(tau)=tau^4(1-tau)^6 of these two mixed monomials. Its squared
ratio is

\[
 {C c_C\over96}{B(11,15)\over B(9,13)}
       ={91C c_C\over161920}.                   \tag{9}
\]

These parameter measures are explicitly declared; they are not silently
identified with the complete T-106140 history diagonal convention.

## 4. The Mellin observation does not remove this diagonal loss

The insertion changes the Mellin phase by9^(-it). It has modulus one. Thus
the weighted entry ratios above remain exact after integration against the
same native measure |kappa_hat(t)|^2 dt/(2pi), for every nonzero input
coefficient function in that space. For a single unphased atom the common
factor is Gamma(0), which cancels from the ratio.

This argument concerns the principal atomic norm before any off-atomic
interference. It does not assert that the old and new physical cross-Gram
entries are equal, or that their signed observations have a common positive
lower bound. Their ratio phases differ and their shell tags remain distinct.

## 5. What an admissible repair must retain

If the source gauge is applied before canonical phase extraction, its output
must carry enough ancestry to reconstruct (3) and the exact weight cocycle
(4). Keeping the ancestral phase labels can postpone the conductor jump;
it cannot make that jump free when the output is finally placed in the
canonical principal moment. The large factor is localized to removing the
old least reduced-core prime, and may need a separate renewal/selector estimate.

The unamplified gauge and its first-jet norm remain polylogarithmically
controlled, as proved in the separate gauge-connection packet. This example
explains why that result alone does not transfer to the principal weight.
It also shows why retaining the gamma bound, common-core identity, and
phase labels separately is insufficient for such a transfer.

No claim is made that the actual fully recombined principal vector realizes
this operator norm. Other input records can interfere at an output, the
connection term must still be included when differentiating a gauge, and the
complete carrier/renewal assembly may exploit structure absent from a uniform
operator estimate. The open T-106140 bound has not been disproved. The ruled
out shortcut is a source-blind subpower gauge-transfer inequality after
recomputing the principal conductor weight.
