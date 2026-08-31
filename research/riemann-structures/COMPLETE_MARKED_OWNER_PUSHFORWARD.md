# A complete degree-bounded owner pushforward in the marked partition

Status: **exact complete-owner class-count formula and a cofinal marked
partial-Frobenius obstruction for its literal principal Wick observable**.

Scope: a specified polynomial Boolean coefficient projection, with all split
degree-two owners summed, fixed degree-three split common core, degree-one
reduced cores, complete quadratic-class partition, and literal Boolean-history
normal ordering. This is not the complete original carrier/renewal source.

Exact native interfaces: L-106080/106120/106131/T-106140 at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b; the marked partition and projector
interface in FFPS_MARKED_PLACE_SIGNED_DESCENT_GATE0.md at
a30276a5be049749ebb2147f30f000dd5659298b. The coordinating agent's exact
F_25 scout found the nonzero defect below with complete owner coverage and
total-Frobenius controls. The cofinal theorem is proved symbolically, not
extrapolated from those finite values. Final source-authenticated replay and
independent review are recorded separately at the frozen commit.

## 1. Source object before taking any trace

Work over an odd finite field F_q. Let the common core be
g(T)=(T-g_1)(T-g_2)(T-g_3), and the reduced cores be T-lambda and T-rho.
The five roots are distinct. A further fixed root m is omitted from the
coefficient projection; it provides an explicit marked exclusion rather than
silently adding marked-prime copies to the owner sum.

Let C={g_1,g_2,g_3,lambda,rho,m}. The source cover consists of four ordered,
distinct F_q-rational roots a,b,c,e outside C, with
P=(T-a)(T-b), Q=(T-c)(T-e). Its counting measure has the rational weight1/4
for the two free pair swaps. Thus every unordered split P,Q in this degree
block is counted once. The owners are pairwise disjoint and clean with both
cores. This is not the set of rational points of the geometric pair-swap
quotient: that set would also contain Frobenius-swapped nonsplit owner pairs.

Put d=rho-lambda and

\[
 x=d^2P(\rho),\qquad y=d^2Q(\lambda),\qquad
 \tau=\chi_q(P(\rho)),\quad\sigma=\chi_q(Q(\lambda)).
\]

Both residues are nonzero. For each (sigma,tau), let H_(sigma,tau)(x,y) be
the exact number of owner configurations above that pair of residues, and
K_(sigma,tau)=sum_(x,y) H_(sigma,tau)(x,y). The complete additive member is

\[
 S_{\sigma,\tau}(h,k)
 =\sum_{x,y}H_{\sigma,\tau}(x,y)\psi(kx-hy).        \tag{1}
\]

This is the actual finite owner pushforward, not a chart fixing P(rho)=Q(lambda)=1.
Geometrically its defining correspondence is the ordered configuration source
with the two evaluation maps and the two quadratic-class conditions, followed
by compact pushforward of the indicated additive character and the explicit
rational counting weight. No deck-invariant projector is substituted for that
weight. No Betti estimate or partial Frobenius isomorphism is assumed.

## 2. Boolean and literal Wick normalization

Use the polynomial norm and cutoff q<=U<q^2; this contains the native degree
cutoff at physical norm Y=q^10. Each full core g(T)(T-lambda) has four distinct
degree-one labels. Its only balanced histories are the six ordered 2+2
partitions, each of coefficient +1. A one-sided full occurrence has six
labels including its two owners, hence equal-pair share1/15. Each one-sided
history has coefficient 1/(15q^5), and each bilateral history 1/(225q^10).
There are 36 bilateral histories per owner configuration.

Thus a complete principal member is proportional to 36K_(sigma,tau), while
its literal history diagonal is proportional to 36K_(sigma,tau), not
K_(sigma,tau) and not 1296K_(sigma,tau). After the common squared amplitude is
factored out, its principal Wick polynomial is

\[
 J_{\sigma,\tau}=1296K_{\sigma,\tau}^2-36K_{\sigma,\tau}.\tag{2}
\]

The sum of (2) over all four quadratic classes retains the native placement of
the class partition before the family square. Its source-dual principal
prefactor is c_q^2/(225^2 q^12), c_q=(q+1)/(q-1), times the common Mellin
measure mass if that fixed physical observation is applied. At equal norm
q^10 the Mellin ratio is one, so the multiplier is common to the entire fibre.

The invariant projector Pi_0 has coefficient one on its retained deck line.
The reduced cores are distinct linear factors, so their polynomial coprimality
projector is one. Equation (2) performs literal normal ordering explicitly;
these operations are not assumed to preserve an unspecified discarded carrier.

## 3. The marked partial-Frobenius decision

Keep g_i and m over the base field F_p and evaluate over F_(p^2). The left
marked map raises lambda and h to their p-th powers while fixing rho and k;
the right map is symmetric. The omitted common-root parameters remain fixed.
Total Frobenius raises both marked blocks and preserves the source object.

A compatible partial-Frobenius isomorphism for the complete relative object
would preserve its extension-field trace. Therefore a discrepancy in (1),
or in the fully class-summed literal principal polynomial (2) for an object
preserving that observable, is an exact obstruction at this declared scope.
The comparison must stay inside the clean open set at both points; moving a
point onto an excluded diagonal is not used as a witness.

The bounded scout uses F_25=F_5[a]/(a^2-2), common roots0,1,2, and omitted
root3. It enumerates every unordered owner pair from the remaining19 roots,
then every disjoint ordered pair of those owners. Its complete count is
19*18*17*16/4. All additive characters are stored in the exact basis
1,zeta_5,...,zeta_5^3, using 1+zeta_5+...+zeta_5^4=0. No numerical phase is
evaluated. Total-Frobenius agreement is a required positive control.

One collapse is already proved without computation: summing (1) over every
nonzero h,k gives K_(sigma,tau), by the two Ramanujan identities. Summing
K over the four classes gives the constant configuration count. Hence the
completely class-forgotten linear count cannot detect the marked obstruction.
The class-preserving family and its principal Wick observable are the actual
objects under examination.

## 4. MOP-1: the complete owner sum has an exact three-moment formula

Let D=F_q minus C and n=|D|. For z in D put

\[
 u_z=\chi_q(\rho-z),\quad v_z=\chi_q(\lambda-z),\quad
 \alpha=\sum_Du_z,\quad\beta=\sum_Dv_z,\quad
 \omega=\sum_Du_zv_z.
\]

All these signs are nonzero. Define

\[
 \begin{aligned}
 A_n&=n(n-1)(n-2)(n-3),\\
 B_n&=(n-2)(n-3)(\alpha^2-n),\\
 C_n&=(n-2)(n-3)(\beta^2-n),\\
 T_n&=\alpha^2\beta^2-(n-4)(\alpha^2+\beta^2)
       -4\omega\alpha\beta+n^2+2\omega^2-6n.
 \end{aligned}
\]

Then the complete unordered-owner class count is

\[
 \boxed{K_{\sigma,\tau}
 ={A_n+\tau B_n+\sigma C_n+\sigma\tau T_n\over16}.} \tag{3}
\]

To prove (3), temporarily order the two roots inside each owner pair. The two
quadratic-class indicators are (1+tau u_a u_b)/2 and
(1+sigma v_c v_e)/2. The four-distinct ordered count is A_n. The u_a u_b
sum is B_n, since each ordered a!=b has (n-2)(n-3) choices for c,e and
sum_(a!=b)u_a u_b=alpha^2-n. The v_c v_e sum is C_n.

For the mixed sum, condition on ordered a!=b. The sum over the remaining
ordered c,e is (beta-v_a-v_b)^2-(n-2). Use

\[
 \sum_{a\ne b}u_au_b(v_a+v_b)=2(\alpha\omega-\beta),\quad
 \sum_{a\ne b}u_au_bv_av_b=\omega^2-n.
\]

Expansion gives T_n exactly. Dividing by four for the class indicators and
by four for the free owner-pair swaps proves (3). This sums every owner
configuration, including all its cross-disjointness exclusions.

The four sign characters are orthogonal. Consequently the class-summed literal
principal Wick integer has the closed formula

\[
 \boxed{J=\sum_{\sigma,\tau}(1296K_{\sigma,\tau}^2-36K_{\sigma,\tau})
 ={81\over4}(A_n^2+B_n^2+C_n^2+T_n^2)-9A_n.}        \tag{4}
\]

This is not the square of the class-forgotten owner count. That square would
discard precisely the partition under investigation.

### Only finitely many marked character values remain

The complete finite-field character sums give

\[
 \begin{aligned}
 \alpha&=-\sum_{z\in C\setminus\{\rho\}}\chi_q(\rho-z),\\
 \beta&=-\sum_{z\in C\setminus\{\lambda\}}\chi_q(\lambda-z),\\
 \omega&=-1-\sum_{z\in C\setminus\{\lambda,\rho\}}
                   \chi_q((\rho-z)(\lambda-z)).
 \end{aligned}                                    \tag{5}
\]

For the last identity, the complete quadratic sum at two distinct roots is
-1. An elementary proof completes the square and counts the solutions of
s^2-t^2=c!=0: (s-t)(s+t)=c has q-1 solutions, so the corresponding character
sum is (q-1)-q=-1. No square-root estimate or unproved cancellation is used.

## 5. MOP-2: an exact obstruction on a nested cofinal extension tower

Work over F_5, with fixed excluded marks0,1,2,3 and
lambda=a, rho=a+1 in F_25, where a^2=2. Take

\[
 q=25^m,\qquad m\ge1\text{ odd},\qquad n=q-6.
\]

One may take m=3^j to obtain a nested cofinal tower. For z in F_25^*,
chi_(25^m)(z)=chi_25(z)^m, so all signs below remain unchanged for odd m.
The left marked Frobenius is the fixed base-field map lambda->lambda^5=-a;
rho stays a+1. All six excluded marks remain distinct before and after this
map. The witness never leaves the clean open set.

For the four fixed marks z=0,1,2,3, the sign rows are

\[
 (\chi(\rho-z))_z=(+,-,+,-),\qquad
 (\chi(\lambda-z))_z=(-,+,-,-).
\]

These follow from chi_25(x+ya)=chi_5(x^2-2y^2). The second row is unchanged
when lambda is replaced by lambda^5. The crossed sign, however, changes:

\[
 \chi(\rho-\lambda)=1,\qquad
 \chi(\rho-\lambda^5)=\chi(1+2a)=-1,              \tag{6}
\]

since the latter norm is 1-8=3 modulo5. Equations (5) therefore give

\[
 (\alpha,\beta,\omega)=(-1,1,1),\qquad
 (\alpha',\beta',\omega')=(1,3,1).                 \tag{7}
\]

Before the partial map,

\[
 B_n=C_n=(n-2)(n-3)(1-n),\quad T_n=(n-3)(n-5).
\]

After it B_n is unchanged, while

\[
 C'_n=(n-2)(n-3)(9-n),\quad T'_n=(n-3)(n-13).
\]

Substitution into (4) proves

\[
 \boxed{J'-J
 =324(n-3)^2\big((n-2)^2(5-n)-(n-9)\big)<0
 \quad(n\ge19).}                                  \tag{8}
\]

Both bracketed terms have strict negative sign in this range. Thus the
complete owner pushforward, after all four quadratic classes, all36 literal
Boolean histories per configuration, the invariant deck line, polynomial
coprimality, and literal Wick deletion, still has a nonzero marked
partial-Frobenius defect in the principal observable on a cofinal extension
tower. Total Frobenius preserves it by the exact bijection raising every
owner and every marked coordinate to the fifth power.

At q=25, the four classes in order (--),(-+),(+-),(++) are

\[
 (6440,5800,5800,5216)\longmapsto(6296,5672,5944,5344).
\]

Their sum is23256 on both sides, but

\[
 J=176203654560,\quad J'=175867233696,\quad
 J'-J=-336420864.
\]

The bounded complete enumeration authenticates these values independently
of formula (3). Formula (8), not a fitted trend, proves the cofinal statement.

## 6. The actual source parent and its precise no-go

Let pi_ord be the ordered four-owner configuration morphism over the marked
base, with the six-root cleanliness divisor removed. Let L_x,L_y be the
quadratic Kummer classes of the two nonzero evaluations. In the integral
Grothendieck group of constructible Weil complexes define the signed class

\[
 T_{\sigma,\tau}
 =R\pi_{\mathrm{ord},!}\big((1+\tau L_x)\otimes(1+\sigma L_y)\big).
\]

Its extension-field trace is16K_(sigma,tau): the class-indicator expansion
contributes4 and the ordered owner cover contributes4. The signs are virtual
subtraction when sigma or tau is negative; no nonexistent positive rank-one
class indicator is asserted. An integral class clearing the rational source
weight in the principal literal Wick observable is consequently

\[
 \mathcal J_{\mathrm{int}}=\sum_{\sigma,\tau}
       \big(81T_{\sigma,\tau}\otimes T_{\sigma,\tau}
             -36T_{\sigma,\tau}\big),             \tag{9}
\]

whose trace is16 times (4). The source observable is the rationally weighted
class (1/16)mathcal J_int; equivalently its integral parent (9) carries the
native prefactor from Section2 divided by16. The tensor square occurs after the
complete pushforward in each class; the diagonal is the native literal one.
Tensor with the retained invariant deck line if that factor is displayed.
The counting weight1/4 is not a deck-invariant projector: a permutation trace
would include twisted fixed points. Already over F_5 there are10 unordered
pairs of distinct rational roots but20 monic squarefree quadratics, the extra10
being irreducible. This distinction is required over every extension field.

The additive-family analogue inserts the actual Artin--Schreier class
of kx-hy before R pi_ord,!. For a conjugate additive member the phase is negated;
one must not substitute a Verdier dual without checking its normalization.
The principal class (9) needs no additive character or such identification.

A total-Weil-compatible left partial-Frobenius isomorphism of (9) on the common
domain where both parameter tuples are clean, or of a
source object preserving this principal observable, would force equal traces
at the two extension-field points. Equation (8) rules out that isomorphism on
this declared clean family. No generic-support-faithfulness assumption is
needed: the complete pushforward trace itself differs. No theorem about all
possible correspondence categories or about an unknown full-source object is
claimed.

### Exactly what datum survives the owner sum

When the fixed marks lie in F_5, their one-coordinate character rows are
unchanged by lambda->lambda^5. For the class-count quotient (3) and its
principal Wick observable, these rows together with the single coupled bit
chi(rho-lambda) determine (5). The example proves that this bit cannot be
forgotten while preserving that observable. Retaining it is a sufficient
repair for this class-count calculation, not a construction of independent
marked Frobenii. It is not sufficient data for the full additive residue
histogram (1) or the complete native carrier geometry.

## 7. Analytic and global-source boundaries

The integer defect in (8) is asymptotic to -324q^5. Restoring the exact
source-dual principal prefactor c_q^2/(225^2q^12) makes the weighted defect
of order q^-7 (times the common observation mass). This is a nonzero
geometric descent obstruction, not a growing analytic bad moment or an RH
counterexample.

The coefficient projection sums all owners in its prescribed degree block,
all its Boolean histories, and all quadratic classes in the correct order.
It retains its fixed common core and omitted marked root. Additional core
degrees, sums forgetting g, carrier transport, or other signed source regions
could cancel or identify its image. Their complete pushforward is not supplied
by this theorem. In particular, failure of descent here does not disprove a
different full-source architecture that retains the coupled correspondence or
uses complementary cancellations.
