# A power-sized live source algebra at the fixed conductors 5 and 7

Status: **exact quantitative continuation of FCM-1; source-support and
faithful-carrier complexity only, not a trace estimate or integration verdict**.

Scope: the same frozen canonical equal-pair source and atom conventions as
[the fixed-conductor multiplicity theorem](LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md).
The only external analytic import remains the unconditional prime number
theorem at the fixed moduli 1, 5 and 7. No prime-distribution hypothesis, new
coefficient family, or growing modulus is introduced. RH and GRH remain open.

The result is stronger than unbounded multiplicity: even after the paid
Boolean histories have been combined, one live residue cell requires a
power-sized faithful source-algebra carrier. This does not force a
power-sized scalar trace, an error term, or the cohomology of an arbitrary
derived realization.

## 1. Quantitative live rectangles

Write \(\log\) for the natural logarithm. Retain \(U=2^k\), \(Y=U^6\),
\(\ell=5\), \(\rho=7\), and the three-prime common core \(g=abh\) of
FCM-1, where

\[
 \sqrt U<a,b<\frac{21}{20}\sqrt U,
 \qquad \frac U4<h<\frac{3U}{10}.
\tag{1.1}
\]

In particular \(U^2/4<g<U^2/3\). For all sufficiently large \(U\), such
primes exist. The Boolean core calculation is unchanged: the full core
\(gq\), for \(q=5,7\), has exactly the two ordered histories
\((ab,hq,1)\) and its swap, each with coefficient 1.

**FCM-3 (quantitative lower bound).** For every sufficiently large dyadic
\(U\) and every choice of core (1.1), the same fibre
\(\iota=(g,5,7,+1,+1)\) contains a fully owner-disjoint \(m\)-by-\(n\)
rectangle satisfying every support condition of FCM-1 and

\[
 m,n\ge\frac{U}{10000\log U}.
\tag{1.2}
\]

Thus its one raw cell \((1,4)\) contains at least

\[
 mn\ge\frac{U^2}{10^8(\log U)^2}
 =\frac{36}{10^8}\frac{Y^{1/3}}{(\log Y)^2}
\tag{1.3}
\]

distinct history-aggregated arithmetic pairs, and four times as many
literal ordered-history atoms. The complete fibre may contain more.

### Proof

The change from FCM-1 is to let the first owner labels grow in a prescribed
interval. Take the set of primes

\[
 \mathcal S_U=\{s\text{ prime}:U/2000<s<U/1000\},
 \qquad K_U=|\mathcal S_U|.
\tag{1.4}
\]

The ordinary prime number theorem gives

\[
 K_U\sim\frac{U}{2000\log U}.
\tag{1.5}
\]

For sufficiently large \(U\), these labels exceed \(a,b\), are smaller
than \(h\), and avoid 5, 7 and 67. This replaces the convenience in FCM-1
that the finitely many first owner labels lay below \(a,b\); no native
condition requires that convenience. All first owner labels still lie below
\(U\) and are distinct from the common core.

Split \(\mathcal S_U\) into two parts of sizes
\(m=\lfloor K_U/2\rfloor\), \(n=K_U-m\). Let \(J_q\) be the
dyadic-interior owner-product intervals constructed in FCM-1. Their
locations and lengths satisfy

\[
 J_q\subset(L_q,11L_q/10),\qquad
 |J_q|\ge L_q/40,\qquad L_q=\frac{U^6}{q^2g^2}.
\tag{1.6}
\]

For every \(s\in\mathcal S_U\), the prospective partner interval
\(J_q/s\) satisfies the **uniform, fixed-constant bounds**

\[
 J_q/s\subset(180U,1500U),
 \qquad |J_q/s|\ge\frac{225}{49}U>\frac92U.
\tag{1.7}
\]

Indeed \(g<U^2/3\) gives \(L_q>9U^2/q^2\), so the smallest possible
left endpoint is greater than \(9000U/49>180U\), and the smallest
length is at least \(9000U/(40\cdot49)=225U/49\). Conversely
\(g>U^2/4\) gives \(L_q<16U^2/q^2\), so the largest possible right
endpoint is less than
\((11/10)(16/25)(2000)U=1408U<1500U\).

Apply the endpoint-uniform fixed-modulus PNT corollary of FCM-1 with
\(T=U\). A more explicit lower constant is useful here: uniformly over
the intervals in (1.7), and over every reduced class modulo 5 or 7, the
number of primes is at least

\[
 \frac{U}{10\log U}
\tag{1.8}
\]

for sufficiently large \(U\). To justify this from the asymptotic rather
than from infinitude alone, write the endpoints as \(A_U,B_U\). On
\([180U,1500U]\), the PNT errors are uniformly \(o(U/\log U)\), and
the main-term difference is

\[
 \frac{B_U-A_U}{\varphi(r)\log U}
 +O\!\left(\frac{U}{(\log U)^2}\right),
 \qquad r\in\{5,7\}.
\tag{1.9}
\]

Since \(B_U-A_U>(9/2)U\) and \(\varphi(r)\le6\), the leading
coefficient is at least \(3/4\). It comfortably implies the smaller
constant \(1/10\) in (1.8). There are only finitely many reduced residue
classes, so their thresholds can be combined. Uniformity in \(s\) and
the chosen core follows from the same compact endpoint bounds; no modulus
varies with \(U\).

On the other hand (1.5) gives \(K_U\le U/(1000\log U)\) eventually.
Choose the partner primes successively. At each step fewer than \(K_U\)
previous partners are forbidden, whereas (1.8) supplies at least one
hundred times that upper bound. The required residue class is
\(s^{-1}\bmod7\) for left owners and \(s^{-1}\bmod5\) for right
owners. Every partner exceeds \(180U\), so none is a first owner or
core prime. All partner primes can therefore be chosen distinct.

The owners, physical products, dyadic blocks, kernel positivity check,
canonical shares and same-cell congruences now satisfy the identical
checks as in FCM-1. Finally (1.5) and the floor operation imply (1.2) for
all sufficiently large \(U\); for example first use
\(K_U\ge U/(2500\log U)\), then absorb the single floor loss. This
proves FCM-3. No explicit common threshold is asserted. \(\square\)

## 2. Matching upper order in the stated disjoint-owner class

For one allowed core \(g\), let \(G_g(U)\) be the largest area \(mn\)
of an owner-disjoint arithmetic rectangle satisfying the same physical
window, congruences and support conditions. This maximum counts arithmetic
pairs after the specified history aggregation. It is not total cell
occupancy, and its definition retains global disjointness of all owner
labels across both sides.

**FCM-4 (sharp order within this class).** Uniformly over the allowed cores,

\[
 G_g(U)=\Theta\!\left(\frac{U^2}{(\log U)^2}\right).
\tag{2.1}
\]

The lower bound is FCM-3. For the upper bound, the physical window and
\(g>U^2/4\) imply for every owner on either side

\[
 P_i,Q_j<\frac{11}{10}\frac{16}{25}U^2
 =\frac{88}{125}U^2<U^2.
\tag{2.2}
\]

A semiprime product below \(U^2\) has at least one prime factor below
\(U\). Choose such a factor from each owner. Global disjointness makes
the chosen factors distinct, whence

\[
 m+n\le\pi(U),\qquad
 mn\le\frac{\pi(U)^2}{4}
 =O\!\left(\frac{U^2}{(\log U)^2}\right).
\tag{2.3}
\]

This upper bound may fail if owner labels are allowed to repeat or if a
larger complete source population is counted. Neither relaxation is made.
\(\square\)

## 3. The resulting complexity obstruction

Let a proposed finite carrier faithfully represent the source algebra of
all retained arithmetic pairs in each live cell. The frozen source-algebra
lemma then gives, for the cells above,

\[
 \operatorname{rank}\ge mn
 \gg\frac{Y^{1/3}}{(\log Y)^2}.
\tag{3.1}
\]

Thus neither a conductor-only rank bound \(r\le f(\ell,\rho)\) nor
a horizon-subpower rank bound \(r(Y)=Y^{o(1)}\) can hold for that faithful
carrier architecture. The contradiction already occurs with
\((\ell,\rho)=(5,7)\), along \(Y=2^{6k}\).

This is a precise restriction on one candidate ontology, not on every
Riemann structure. In particular:

- faithfulness of all arithmetic atom idempotents is a hypothesis;
- a rank-one object on a growing source space is not ruled out;
- cohomology after a signed derived pushforward need not retain those
  idempotents faithfully;
- principal-specific quotients and nonlinear sufficient statistics are not
  subject to this rank proof;
- the literal and history-recentered diagonal conventions remain distinct,
  as recorded in FCM-2 and its paid conversion ledger;
- the source coefficients are not declared independent parameters.

At these fixed conductors the additive/principal and Kummer/principal
history-correction ratios remain 12 and 11. Rank growth alone therefore
does not reopen the paid representation-history correction or yield an
unpaid analytic error. The complete signed cross-group current is still the
load-bearing open problem.

## 4. Provenance and review boundary

This is a mathematical continuation of the exact source-locked FCM-1
packet. It reuses its frozen source manifest, core proof, physical map,
canonical atom resolution and external PNT reference. No new finite-source
search or growing-horizon computation is required for FCM-3 or FCM-4.
The existing small panels authenticate the finite source interface, not
the all-horizon asymptotic.

An independent adversarial reconstruction checked the interval constants,
the fixed-modulus uniformity, the greedy exclusion budget, the replacement
of the earlier small-label ordering convenience, and the scope of the
upper bound. The elementary arguments and prime-distribution input are
classical; no external novelty or priority is claimed. Canonical scientific
integration and the remaining arithmetic estimates are separate tasks.
