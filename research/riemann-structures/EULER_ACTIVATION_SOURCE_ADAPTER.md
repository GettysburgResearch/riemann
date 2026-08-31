# An exact Euler source adapter and its cancelling activation complement

Status: **exact finite-horizon source identity, including the explicit
complement of the completed Boolean owner coefficient**.

This supplies a coefficient-level binding that was absent from the restricted
Boolean block. It also closes that block's naive promotion to a lower bound
for the corresponding complete raw Euler source: the complementary activation
terms cancel at the very same physical Mellin labels. It does not identify
every completed retained mask, principal weight, or Wick diagonal with the
Euler derivative-site resolution.

Sources: L-102706/709/741/746 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc; L-106080 at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b; the frozen subcritical observed
Boolean block at1623f1924c62035918a94bcacf2ccad7d3bb6cf7. The old block's
statement and artifacts are unchanged.

## 1. Keep the actual path and its derivative-site labels

On a finite labelled horizon take the exact native Euler path

\[
 E_t=\prod_j e_t(x_j),\qquad
 e_t(x)=1-tx-(1-t)x^2,\quad 0\le t\le1.          \tag{1}
\]

Thus E_1=E=product(1-x_j), E_0=S=product(1-x_j^2), and
E-S=integral_0^1 dE_t/dt dt. Every source partition in this note is independent
of t. A derivative-site label j records which factor is differentiated.

Fix distinct physical primes p,q and a squarefree core a, with
(a,pq)=1 and k=omega(a)>=1. Put P=pq and N=Pa^2, and assume this monomial is
inside the chosen finite horizon. Denote its formal labelled monomial by

\[
m_{P,a}=x_px_q\prod_{r\mid a}x_r^2.            \tag{2}
\]

The source's two labelled copies of67 remain separate. This statement fixes
one labelled monomial, with any unused copy contributing its constant term.
For an assertion about the complete physical coefficient after label collapse,
exclude67 from P a, as in the subcritical block, or retain its other labelled
aliases explicitly. Two distinct67 labels in E can realize the physical
square67^2 even though E has no squared individual label.

Its two unsquared labels are the owner slots. All unused prime factors
contribute their constant term1. The coefficient of (2) in E_t is

\[
 [m_{P,a}]E_t=\mu(a)t^2(1-t)^k.                 \tag{3}
\]

Separate the derivative sites into the two owner slots and the k core slots.
This is a source-label projection of the explicitly expanded Euler derivative,
not an assertion that those sectors are separate endpoint defects.

## 2. EA-1: the owner coefficient and its actual source complement

The respective coefficient densities in dE_t/dt are

\[
 o_k(t)=2\mu(a)t(1-t)^k,
 \qquad c_k(t)=-k\mu(a)t^2(1-t)^{k-1}.           \tag{4}
\]

Each owner site contributes half of o_k, and each core site contributes c_k/k.
Integrating the elementary beta polynomials gives

\[
 \boxed{
 O_{P,a}={\mu(a)\over\binom{k+2}{2}},\qquad
 C_{P,a}=-{\mu(a)\over\binom{k+2}{2}},\qquad
 O_{P,a}+C_{P,a}=0.}                             \tag{5}
\]

Indeed integral t(1-t)^k dt=1/((k+1)(k+2)), while integral
t^2(1-t)^(k-1) dt=2/(k(k+1)(k+2)). This proves every sign and coefficient
in (5). It also follows from (3), which vanishes at both endpoints when k>=1.

The owner coefficient in (5) is precisely the **complete Boolean equal-pair
coefficient**: the full squarefree core coefficient is mu(a), and the occurrence
has k+2 labels, with equal share1/binom(k+2,2). The identification includes
the sign and normalization. It is a binding to the owner-activation projection
of (1), not merely a comparison with an unrelated scalar sequence.

The complement C is explicit and belongs to the same original Euler
homotopy. It is not an unspecified remainder or a bound obtained by Cauchy.
It has the same labelled monomial, hence the same physical integer and
primitive phase, as O. No completion or re-completion moves its Mellin ratio.

The assumption k>=1 is essential. At k=0 the semiprime monomial has endpoint
coefficient1; there is no core activation to cancel it. The empty-core
terminal sector is not deleted by this theorem.

## 3. EA-2: physical realization and the complete mixed sector

The frozen physical substitution is

\[
 x_r=r^{-1/2}e^{-i\vartheta_r}U_r.
\]

Consequently (2) has the common realization

\[
 N^{-1/2}\exp\left(-i\vartheta_p-i\vartheta_q
                    -2i\sum_{r\mid a}\vartheta_r\right)U_N. \tag{6}
\]

Multiplying (5) by (6) proves cancellation coefficientwise in every primitive
phase. Applying any common linear physical observation, including the fixed
Mellin kernel, preserves that cancellation. The same is true after a fixed
mask depending only on the common physical monomial and retained pair/core
data. A mask distinguishing activation types or depending on t does not
have this property merely because it shares an endpoint label.

In fact the entire raw mixed labelled semiprime-square sector of E-S vanishes:
E contains no squared prime labels and S contains no odd prime labels. The
same sector vanishes in the raw carrier-quotiented remainder of L-102741.
To see the latter directly, write

\[
 RS=\prod_r(1-x_r)e^{x_r},\qquad
 \mathcal P_W=-RS\sum_rx_r,\qquad
 \mathcal D_{\ge2}=(E-S)-\mathcal P_W.            \tag{7}
\]

Each local factor (1-x)e^x has degree-one coefficient0. The linear sum in
P_W can supply at most one of the two odd owner labels in (2), leaving the
other degree-one coefficient zero. Thus the coefficient of P_W, and hence
of D_ge2, is zero at every (2). This statement is about these raw monomial
coordinates; a completion chart need not preserve them.

The diagram now has a precise outcome. The full integrated Euler derivative
maps to the zero endpoint coefficient at (2). Its owner-activation projection
maps to the nonzero completed Boolean coefficient in (5). Therefore this
projection cannot factor through the endpoint physical-coefficient quotient.
In the two-sector space the relation is (O,C)=(v,-v), with endpoint map
(u,w)->u+w. Retaining the owner coordinate requires the activation-type label;
forgetting that label first destroys it. This is the exact obstruction to the
identity-on-physical-monomials adapter, not an obstruction to every transported
completion gauge.

## 4. EA-3: full Boolean row recombination in the subcritical block

The frozen block has core a=A B ell (or A B rho), with A>U,
B,ell<U, and B ell>U. The only U-small subsets of its three prime labels are
the empty set and the singleton sets B and ell. The exact Boolean Vaughan
identity is

\[
 \mu_{\rm sf}=2\mu_U-\mu_U\star\mu_U\star1_{\rm sf}
                   +a_U\star a_U\star\mu_{\rm sf}.
                                                               \tag{8}
\]

At this core, 2mu_U=0. In mu_U star mu_U star1, the possibilities for B,ell
contribute1-4+2=-1: neither in a truncated slot, exactly one in such a slot,
or in two different truncated slots. Putting both into the same truncated
slot is prohibited by B ell>U. Thus the Type-I coefficient is+1. The two
balanced histories have total coefficient-2, as proved in the old block.
Their complete sum is the native coefficient-1.

At depth5, (5) consequently gives the full-row owner coefficient

\[
 -{1\over10\sqrt N},                            \tag{9}
\]

half the balanced coefficient -1/(5sqrt N). The core-activation complement
is +1/(10sqrt N). These statements are exact for each physical term, not
an estimate for a mask of the globally summed Type-I row.

Keep the old fixed-g bilateral restriction and its exact observation
Gamma(log(N/M)). Its balanced owner-owner block was J_U. Full Boolean row
recombination gives

\[
 J_U^{OO}=J_U/4
 =\Theta(Y^{1/24}/\log^8Y).                     \tag{10}
\]

This preserves the previous signed coefficient-block obstruction to uniform
restriction-stable saving. It does not promote that block to the raw source.
For the explicit Euler activation complement, the four cross pairings are

\[
 (J_U^{OO},J_U^{OC},J_U^{CO},J_U^{CC})
       ={J_U\over4}(1,-1,-1,1),\qquad
 \sum_{X,Y\in\{O,C\}}J_U^{XY}=0.               \tag{11}
\]

Cancellation occurs term by term before summation or observation. Shared g
is retained: this is the sum of the declared fixed-g cross packets, not the
norm of independently summed fields that would add g!=g' terms. Formula (11)
supplies an actual native complement for this coefficient-level Euler lift.
It is not a cancellation theorem for all retained T-106140 source channels.

## 5. EA-4: the source measure and the diagonal do not disappear

There are several different legitimate resolutions; their diagonals must not
be conflated. In the original Euler derivative-site resolution use counting
measure on the k+2 sites and Lebesgue measure dt on [0,1]. At the fixed
physical monomial, the sum of squared real coefficient densities is

\[
 D_{\rm site,time}
 ={1\over N}\left(2B(3,2k+1)+kB(5,2k-1)\right)
 =\boxed{{4\over(2k-1)(2k+1)(2k+3)N}}.           \tag{12}
\]

Integrating each site's coefficient first, then using counting measure on
those k+2 integrated atoms, gives instead

\[
 D_{\rm site}
 ={1\over N}\left({2\over(k+1)^2(k+2)^2}
             +{4\over k(k+1)^2(k+2)^2}\right)
 =\boxed{{2\over k(k+1)^2(k+2)N}}.              \tag{13}
\]

Finally, collapsing all owner sites to O and all core sites to C gives

\[
 D_{O,C}={8\over(k+1)^2(k+2)^2N}.               \tag{14}
\]

At k=3 these are4/(315N),1/(120N),1/(50N), respectively. If the common
physical Mellin measure is applied, each is multiplied by its common mass
Gamma(0). They are exact properties of the stated measures and atomizations.
They are not identities with the four balanced Boolean-history diagonal or
with T-106140's complete principal diagonal.

The complete uncentered field vanishes, but a form centered by any one of
these specified diagonals equals minus that diagonal. Thus linear source
cancellation does not authorize deleting a Wick correction. Transferring a
centered form between these resolutions requires the exact difference of
their diagonals, in addition to the common endpoint identity.

## 6. What has been closed, and what remains

The missing coefficient-level Euler adapter is now explicit, and so is the
complement that invalidates a lower-bound promotion of the subcritical block
through that adapter. This is stronger than observing that a raw monomial
coefficient happens to vanish: it identifies the two source sectors, their
signs, their beta weights, and their unchanged physical observation.

The remaining gate is different. A full retained-label principal/Wick source
adapter must transport the actual regional carrier, endpoint and homotopy
labels, Gauss/principal weights, and its inherited diagonal. Equality of one
completed coefficient with (5) does not establish equality of that entire
assembly. Nor does the subcritical global Type-I estimate apply to arbitrary
coefficient masks. No RH-facing bound or unrestricted source cancellation is
claimed here.

The bounded companion replay authenticates every imported source, reconstructs
the Euler coefficient polynomials and integrals with exact rationals, checks
all three diagonal conventions, and recombines the complete Boolean rows in
each frozen prime-window fixture. It does not run new prime searches or
approximate the Mellin kernel.
