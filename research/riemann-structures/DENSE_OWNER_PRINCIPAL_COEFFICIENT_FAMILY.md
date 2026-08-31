# A complete dense-owner coefficient restriction has a power-sized principal moment

Status: **exact canonical coefficient/Boolean-history restriction, not the
complete retained-gamma family**. RH remains unproved. The source projection
below has a principal moment of order \(Y^{1/2}/(\log Y)^{11}\), despite
its literal principal diagonal tending to zero. It uses the actual balanced
coefficients and canonical owner shares, not arbitrary chosen amplitudes.
The projection is not asserted to be orthogonal for the physical Mellin
norm. Consequently its energy does not lower-bound the complete source:
the omitted gamma phases, coefficients and complementary source can cancel
the selected field.

This is a direct principal-family test of the remaining source/readout
interface. It differs from
[OAC](NATIVE_OFF_ATOMIC_CONDUCTOR_CANCELLATION.md), whose growing additive
and Kummer history corrections have a small principal difference. Here
the coherent **distinct arithmetic owner pairs**, summed before the square,
already give a growing principal moment in the declared coefficient
projection. The result strengthens the absolutely small fixed-conductor
restriction in [PQR](POST_QUOTIENT_PRINCIPAL_READOUT_BARRIER.md).

## 1. Seven prime windows and the actual source

Let \(U\) tend through sufficiently large dyadic integers, and set
\(Y=U^6\). For \(j=1,\ldots,7\), let

\[
 I_j=\left((1+j/1000)U,(1+(j+1)/1000)U\right).
\tag{1}
\]

Choose the seven prime labels in this order:

\[
 p\in I_1,\quad q\in I_2,\quad r\in I_3,\quad s\in I_4,
 \quad g\in I_5,\quad\ell\in I_6,\quad\rho\in I_7.
\tag{2}
\]

Keep **all** choices of the two left owner primes \((p,q)\) and the two
right owner primes \((r,s)\) for each fixed triple \((g,\ell,\rho)\).
Write

\[
 P=pq,\quad Q=rs,\quad a=g\ell,\quad b=g\rho,\qquad
 N=P(g\ell)^2,\quad M=Q(g\rho)^2.
\tag{3}
\]

All seven labels are distinct. Since the owner windows precede the core
windows, \(P<Q<g\ell<g\rho\), proving the full-core owner inequalities
of L-102958. Every owner is coprime to both cores and to every owner on the
opposite side. A prime may occur in several **different** owner products
on the same side; no native per-interaction condition forbids this. No
claim of globally owner-disjoint rectangles is made here.

Every prime exceeds \(U\), and every prime is below \((126/125)U\).
Thus

\[
 Y<N,M<(126/125)^6Y<11Y/10.
\tag{4}
\]

The common prime satisfies \(g<U^2/4\) for large \(U\). The reduced
cores are \(c=\ell,d=\rho\), so the least-prime assignment is unique,
\(\ell<\rho\), and both are in their native long-core range. No large
common-core, owner-overlap or physical-shell excision removes this block.
The fixed prime 67 is avoided for large \(U\).

Use the scalar coefficient-coordinate extraction of the frozen NMO source
projection and the source-first Boolean/completion order. Keep the actual
balanced core and canonical owner weights. Do not replace the complete
gamma function by this extraction. Each two-prime core has exactly the
two histories \((g,\ell,1),(\ell,g,1)\), or the corresponding rho
histories, with coefficient \(+1\). This follows from
\(a_U(1)=0\), \(a_U(t)=-1\) for a prime \(t>U\), and the complete
nine allocations of two labels into three factors. Thus each core has
\(b_U=2\), and each occurrence has four labels and owner share \(1/6\).

The resulting bilateral arithmetic coefficient and its four literal
history amplitudes are

\[
 c_{P,Q}=\frac1{9\sqrt{NM}}>0,\qquad
 z_{P,Q,h}(t)=\frac1{36\sqrt{NM}}e^{it\log(N/M)},\quad h=1,2,3,4.
\tag{5}
\]

Primitive coefficient phases are treated exactly as in the declared NMO
coefficient extraction. Their compatibility with the complete retained
gamma readout is not assumed.

## 2. Keep the complete quadratic-class partition

Let \(m\) be the number of left products \(P\), and \(n\) the number of
right products \(Q\). Distinct choices in the disjoint prime windows give
distinct products, so

\[
 m=\#\mathcal P(I_1)\#\mathcal P(I_2),\qquad
 n=\#\mathcal P(I_3)\#\mathcal P(I_4).
\]

For each fixed \((g,\ell,\rho)\), partition these lists by their actual
native quadratic classes

\[
 \tau=\chi_\rho(P),\qquad \sigma=\chi_\ell(Q).
\]

Write the class sizes \(m_+,m_-\) and \(n_+,n_-\). Both signs are
allowed; empty classes contribute zero. No distribution theorem for primes
modulo the growing conductors is used. The elementary identities give

\[
 \sum_\tau m_\tau^2\ge m^2/2,\qquad
 \sum_\sigma n_\sigma^2\ge n^2/2.
\tag{6}
\]

In L-106120.6, the principal even characters have roots \(\chi=\psi=1\),
so their character multiplier is exactly one. Choosing the other roots
multiplies the whole fixed class by \(\sigma\) or \(\tau\), leaving
its squared modulus unchanged. Therefore the actual principal member in
each retained class is, up to a constant sign,

\[
 F_{\sigma,\tau}(t)=
 \sum_{P\in\tau,\ Q\in\sigma}c_{P,Q}e^{it\log(N/M)}.
\tag{7}
\]

The owner sums occur before squaring, as the native family requires. A
restriction to arbitrary independent coefficients is not being introduced.

## 3. The native kernel gives a uniform positive Gram estimate

Let \(d\nu(t)=|\widehat\kappa(t)|^2dt/(2\pi)\), and write
\(\Gamma(v)=\int e^{itv}d\nu(t)\). The authenticated PQR kernel argument
proves

\[
 \Gamma(v)>1\quad(|v|<1/5),\qquad
 |\Gamma(v)|\le\Gamma(0)\le384.
\tag{8}
\]

By (4), every Mellin ratio belongs to \((10/11,11/10)\), so any two
frequencies in any retained class differ by less than
\(2\log(11/10)<1/5\). Also

\[
 \frac{10}{99Y}<c_{P,Q}<\frac1{9Y}.
\tag{9}
\]

The actual principal weight is
\(w_{g,\ell,\rho}=g^2\ell\rho c_\ell c_\rho\), where
\(c_t=(t+1)/(t-1)\). It has order \(U^4\), uniformly on (1).
From positivity of the coefficients and (8), the full principal energy at
this fixed triple, summed over its complete class partition, satisfies

\[
 \begin{aligned}
 E_{g,\ell,\rho}
 &=w\sum_{\sigma,\tau}\int|F_{\sigma,\tau}|^2d\nu\\
 &\ge w\left(\frac{10}{99Y}\right)^2
       \left(\sum_\tau m_\tau^2\right)
       \left(\sum_\sigma n_\sigma^2\right)\\
 &\ge\frac w4\left(\frac{10}{99Y}\right)^2m^2n^2.
 \end{aligned}
\tag{10}
\]

The upper Gram bound similarly gives

\[
 E_{g,\ell,\rho}\le
 384w\left(\frac1{9Y}\right)^2m^2n^2.
\tag{11}
\]

Its inherited literal principal diagonal is exactly

\[
 D_{g,\ell,\rho}
 =\frac{w\Gamma(0)}4\sum_{P,Q}c_{P,Q}^2
 =\Theta(wmn/Y^2).
\tag{12}
\]

In particular (10)--(12) yield a source-vector norm amplification of order
\(\sqrt{mn}\), and the explicit bound

\[
 \frac{25}{11616}mn\le\frac{E_{g,\ell,\rho}}{D_{g,\ell,\rho}}\le4mn.
\tag{13}
\]

No inference from a pointwise value at \(t=0\) is involved.

## 4. A complete varying-conductor coefficient-family lower bound

The ordinary PNT in the seven fixed proportional intervals gives

\[
 m,n=\Theta(U^2/(\log U)^2),\qquad
 \#\{(g,\ell,\rho)\}=\Theta(U^3/(\log U)^3).
\tag{14}
\]

Combining (10)--(14), the declared coefficient family has

\[
 \boxed{
 E_U=\Theta\!\left(\frac{U^3}{(\log U)^{11}}\right)
     =\Theta\!\left(\frac{Y^{1/2}}{(\log Y)^{11}}\right),\qquad
 D_U=\Theta\!\left(\frac{U^{-1}}{(\log U)^7}\right)
     =\Theta\!\left(\frac{Y^{-1/6}}{(\log Y)^7}\right).
 }
\tag{15}
\]

Its literal centered principal trace is \(E_U-D_U\), with the same
power-sized leading order as \(E_U\). The four histories at each pair
contribute only \(3D_U\) to the principal equal-pair correction. Thus
the distinct-arithmetic-pair part has the same leading growth even after
those histories are grouped with the exact paid correction. This is not
the history-only phenomenon in OAC or SRECOMB.

The diagonal estimate in the source-first adapter is therefore compatible
with, and insufficient for, a large readout after the owner sums. Any
principal moment theorem covering every such canonical coefficient
restriction is false. The full T-106140 target is not a restriction-stable
theorem of that form. Its actual unmasked gamma source may have essential
phase correlations or complementary cancellation; the projection above
has not been shown to preserve their observed norm.

In particular (15) must not be reported as a disproof of the complete
principal moment, the inherited reduction, or RH. It identifies an exact
source-facing test that a proposed gamma adapter or positive comparison
must pass. Simply forgetting the unresolved gamma readout and retaining
only the arithmetic coefficient majorant loses essential information.

## 5. Bounded replay and the asymptotic proof

The bounded fixture uses a fixed \(U=2^{20}\), two predeclared verified
primes in each of the first four windows, and one in each of the last
three. It contains four left and four right owner products, all sixteen
arithmetic pairs and sixty-four literal histories. The acquisition scout
has a hard cap of 200 odd candidates per window. The producer independently
trial-divides the eleven supplied labels and verifies all windows and
source conditions; no search occurs during replay.

The replay authenticates the Boolean primitive, NMO coefficient projection,
PQR kernel proof, source-first adapter and native family/owner-size
definitions by exact Git blobs. It retains the complete actual Legendre
partition, native irrational coefficient squares and positive branch,
four-history diagonal, and exact rational Gram lower/upper bounds. It does
not approximate the Mellin integral or infer the cofinal count from a tiny
fixture. The proof of (14) is the ordinary PNT argument.

The note, producer, acquisition fixture, scout and tests are bound in the
generated proof object. Root validation and independent exact-SHA review
are recorded separately; the complete-gamma and RH flags remain false.
