# A native off-atomic conductor family needs large additive--Kummer cancellation

Status: **exact canonical coefficient/Boolean-history restriction of the
native family; no complete retained-gamma counterexample**. RH remains
unproved. The construction below has only one arithmetic pair per fibre,
but four literal positive histories. After the prescribed literal Wick
subtraction, its additive and nonprincipal Kummer traces grow like
\(Y^{1/2}/(\log Y)^3\), while their principal difference tends to zero.

This goes beyond the atomic normalization warning R-106131: the growing
terms here survive removal of the literal atomic diagonal, on an explicit
nonzero balanced source. It does not prove that the complete source has
the same growth. Other source coordinates may contribute signed terms,
and the inherited carrier/renewal measure has not been replaced by one.
The statement concerns the coefficient projection specified below, with
all four Boolean histories retained exactly as in T-106140.

The predecessor
[signed history recombination theorem](../l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md)
already proves the exact three-channel correction and pays its principal
part, while warning that its additive and Kummer parts need not be paid
separately. The new result is the cofinal, actual-source power-growth
realization of those dangerous corrections, not a new recombination
identity or a new proof of the inherited principal transfer.

## 1. A fixed-owner, varying-conductor source restriction

Let \(U\) tend through dyadic integers and put \(Y=U^6\). Fix

\[
 P=17\cdot19=323,\qquad Q=11\cdot13=143.
\]

Choose primes in the three independent proportional intervals

\[
 U<g<\frac{101}{100}U,\qquad
 \frac7{125}U^2<\ell<\frac{57}{1000}U^2,\qquad
 \frac{21}{250}U^2<\rho<\frac{17}{200}U^2.
\tag{1}
\]

For all sufficiently large \(U\), these seven physical prime labels are
distinct and avoid 67. Put

\[
 a=g\ell,\quad b=g\rho,\qquad
 N=Pa^2,\quad M=Qb^2.
\tag{2}
\]

The exact rational endpoint inequalities give

\[
 1<323(7/125)^2<N/Y
 <323(101/100)^2(57/1000)^2<11/10,
\]
\[
 1<143(21/250)^2<M/Y
 <143(101/100)^2(17/200)^2<11/10.
\tag{3}
\]

Thus both coordinates lie in the same narrow physical window. The full
core owner inequalities are \(P\le a\), \(Q\le b\); the cross bounds
of L-102958 also hold. They are bounds involving the **full** cores
\(a=gc,b=gd\), not an imposed replacement by reduced \(c,d\).
The reduced cores are the primes \(c=\ell,d=\rho\), so they are coprime,
\(\ell<\rho\), and their canonical least-discrepancy labels are unique.
The common prime satisfies \(g<U^2/4\); the large-common-core excision
does not delete this restriction. All owner/core coprimality conditions
hold. No owner is being identified with a phase prime.

Use the principal coefficient coordinate of L-106026/L-106080, with the
canonical equal-pair gauge. Keep these fixed owners and all triples (1),
and retain the literal balanced Boolean histories. This is the same
source-first coefficient order as the
[Boolean principal adapter](SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md).
Carrier, endpoint-colour, marked-prime and renewal coordinates are not
summed and declared equal to this coefficient projection.

For a prime \(r>U\), the source convention
\(a_U=\epsilon-\mu_U*1\) gives \(a_U(r)=-1\), while
\(a_U(1)=0\). Both primes in each core exceed \(U\). In a factorization
\(a=a_1a_2a_3\), the first two factors must therefore be the two distinct
core primes to give a nonzero balanced term. Precisely

\[
 (g,\ell,1),(\ell,g,1)\quad\hbox{and}\quad
 (g,\rho,1),(\rho,g,1)
\tag{4}
\]

survive, each with coefficient \(+1\). Composite factors, the factor one,
and allocations to the third factor give zero. This is the complete
three-factor Boolean sum, not two histories selected from a larger row.
Hence \(b_U(a)=b_U(b)=2\).

Each full occurrence has four prime labels. The selected unordered owner
pair has share \(1/\binom42=1/6\). One literal one-sided history therefore
has amplitude \(1/(6\sqrt N)\) or \(1/(6\sqrt M)\); the four bilateral
literal histories have the same amplitude

\[
 z_h(t)=\frac{\zeta}{36\sqrt{NM}}e^{it\log(N/M)},\qquad h=1,2,3,4,
 \qquad |\zeta|=1.
\tag{5}
\]

The common phase \(\zeta\) may contain the retained primitive coefficient
phase and the fixed quadratic-class sign. It cancels in all expressions
below. The actual quadratic classes \(\sigma,\tau\) vary with the triple;
they are assigned to their native fibre, not forced to be \(+1\).

There is exactly one arithmetic pair in each retained fibre
\((g,\ell,\rho,\sigma,\tau)\). Different triples give different fibres
and different physical-output pairs. In particular **there are no
distinct-physical-output terms within this restriction**. Its off-atomic
terms are exactly the twelve ordered pairs of distinct histories at the
same physical output.

## 2. The three exact Wick-centered channels

Write \(c_q=(q+1)/(q-1)\) and let \(\Gamma(0)=\|\kappa\|_2^2>0\)
for the actual native kernel and Fourier convention. By (5),

\[
 D(t)=\frac4{36^2NM}=\frac1{324NM},\qquad
 |\sum_hz_h(t)|^2-D(t)=\frac{12}{36^2NM}=\frac1{108NM}.
\tag{6}
\]

All histories have identical physical additive phases. Summing the
\((\ell-1)(\rho-1)\) nonzero additive phase pairs and subtracting their
literal diagonal therefore gives, for one triple,

\[
 A_{g,\ell,\rho}
 =\frac{\Gamma(0)g^2\ell\rho(\ell-1)(\rho-1)}{108NM}
 =\frac{\Gamma(0)}{108PQg^2}
       (1-1/\ell)(1-1/\rho).
\tag{7}
\]

The source-dual centered-incidence coordinate of L-106191 gives the same
formula: the twelve off-atomic pairs have coincident residues, and the
two centered factors are \((1-1/\ell)(1-1/\rho)\).

The principal and complete nonprincipal Wick-centered terms are

\[
 P_{g,\ell,\rho}
 =\frac{\Gamma(0)g^2\ell\rho c_\ell c_\rho}{108NM}
 =\frac{\Gamma(0)c_\ell c_\rho}{108PQg^2\ell\rho},
\tag{8}
\]
\[
 K_{g,\ell,\rho}=A_{g,\ell,\rho}-P_{g,\ell,\rho}>0.
\tag{9}
\]

Equation (9) retains both mixed and double nonprincipal channels. The
weighted even-character sum is \((\ell-1)(\rho-1)\), of which
\(c_\ell c_\rho\) is principal; it is exactly the frozen T-106140
four-channel identity, with the literal diagonal removed in each channel.
No centered background has been discarded.

All Mellin frequency differences within one fibre are zero, so the
integration is exactly \(\Gamma(0)\). No pointwise use of
\(\widehat\kappa(0)\), numerical quadrature or positivity on a varying
frequency interval is needed here.

## 3. A power-sized off-atomic family and its small principal difference

Let \(A_U,P_U,K_U\) sum (7)--(9) over all triples (1), each in its actual
quadratic-class fibre. The ordinary prime number theorem in fixed
proportional intervals gives

\[
 \#\{(g,\ell,\rho)\}
 \sim\frac1{400000000}\frac{U^5}{(\log U)^3}.
\tag{10}
\]

Indeed the three interval lengths are \(U/100,U^2/1000,U^2/1000\);
the two latter logarithms are asymptotic to \(2\log U\).
This uses no growing-modulus or shrinking-relative-window theorem.
The frozen FCM PNT input already includes this fixed-modulus-one case.

Uniformly on (1),

\[
 A_{g,\ell,\rho}=\Theta(U^{-2}),\qquad
 P_{g,\ell,\rho}=\Theta(U^{-6}),\qquad
 P_{g,\ell,\rho}/A_{g,\ell,\rho}=\Theta(U^{-4}).
\]

Consequently the exact restricted traces satisfy

\[
 \boxed{
 A_U=\Theta\!\left(\frac{Y^{1/2}}{(\log Y)^3}\right),\qquad
 K_U=A_U-P_U=\Theta\!\left(\frac{Y^{1/2}}{(\log Y)^3}\right),\qquad
 P_U=\Theta\!\left(\frac{Y^{-1/6}}{(\log Y)^3}\right).
 }
\tag{11}
\]

All constants include the fixed positive native kernel mass. The exact
difference loses a relative factor of order \(Y^{-2/3}\). The restricted
principal atomic diagonal and full principal moment are respectively
\(P_U/3\) and \(4P_U/3\), so both also tend to zero.

The restriction is entirely in the equal-physical-output diagnostic of
L-106191. Therefore a subpower bound on the absolute equal-output additive
trace cannot hold uniformly over these canonical coefficient/history
restrictions. The same applies to the complete nonprincipal trace of the
restriction. This does **not** refute the actual global gates WCEQ,
WCADD or WCKUM: their unmasked full-source signed sums are different
objects, and may cancel this contribution against omitted source terms.

## 4. The atomization and source boundaries are essential

If the four histories are first merged into a newly declared single atom,
its new diagonal is \(|4z|^2=16|z|^2\), rather than the inherited
\(4|z|^2\). Its newly centered one-atom form is zero. This does not remove
the term (6) for free: it changes the subtracted diagonal by
\(12|z|^2\), exactly the displayed off-atomic contribution in each
channel. Thus merging histories before redefining Wick order is a
different normalization, not a proof of the literal target.

The source-first quotient/completion map preserves the nonzero coefficients
in (4)--(5). The raw mixed-monomial cancellations in EA/PLC concern a
different source projection and cannot cancel them. Conversely this packet
does not construct the complete retained-gamma measure, prove a coefficient
restriction commutes with every physical carrier, or lower-bound the
complete source after all gamma and complementary outputs are restored.

The substantive conclusion is a direct constraint on a proposed native
architecture: neither deleting the literal atomic diagonal nor demanding a
separate absolute bound on every source restriction removes conductor
growth. On this actual source restriction, the principal result is small
because the additive and nonprincipal channels cancel with the exact
T-106140 normalization. A full-source proof must retain the relevant
recombination or supply cancellation from the omitted source.

## 5. Bounded replay and provenance

The replay authenticates the frozen Boolean primitive, source-first adapter,
kernel and native family identities by exact Git blobs. It checks one
predeclared tiny physical record, \(U=256,g=257,\ell=3691,\rho=5521\),
by bounded trial division, verifies the exact windows, complete nine
Boolean allocations per core, canonical share and all three channels.
It independently derives the nonprincipal weight from the even-character
cardinality, and checks the twelve ordered off-history pairs against the
source-dual centered-incidence expression. There is no prime search.

The proportional-window prime count and all-horizon growth in (11) are
proof statements, not extrapolations from that record. The producer binds
this note, itself and the tests by SHA-256 and uses strict typed canonical
JSON comparison. Root validation and the independent exact-SHA review are
recorded separately; no full-gamma or RH conclusion is generated.
