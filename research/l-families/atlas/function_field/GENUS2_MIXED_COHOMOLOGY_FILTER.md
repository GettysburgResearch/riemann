# A mixed-cohomology filter and Frobenius interferometer

Status: **PROVED FROM THE SOURCE-LOCKED MARKED-TRACE TOWER, WITH STANDARD
DELIGNE PURITY USED FOR RECURRENCE MINIMALITY**.  The packet uses exact
lattice algebra and prime-power recurrences; it enumerates no field, curve,
or family.

Let

\[
 P_D(u)^{-1}=\sum_{n\geq0}r_D(n)u^n
\]

for the genus-two quintic family.  The exact marked traces through weight
ten are

\[
\begin{aligned}
T_4&=-3, & T_6&=-4,\\
T_8&=-\Theta_{8,2}-q-6,\qquad &
T_{10}&=(q-1)\Theta_{12}-\Theta_{8,2}-\Theta_{10,2}-q-7.
\end{aligned}                                                   \tag{1}
\]

Here \(\Theta_{12}\) is the level-one \(\Delta\) trace, while
\(\Theta_{8,2}\) and \(\Theta_{10,2}\) are the traces of the unique
level-two newforms in weights eight and ten.

The producer rejects any change to the four prerequisite JSON packets.  It
pins the all-\(q\) \(T_4\), \(T_6\), \(T_8\), and \(T_{10}\) inputs by full
source commit, LF-normalized SHA-256, and canonical payload SHA-256.  In
particular, the \(T_{10}\) theorem is pinned to commit
`42910253be8173c6cd0de19a7a7403d0c31b5c22`; none of the formulas below is
inferred from the three prime controls used by the replay.

## 1. Exact background and channel cancellation

Consider

\[
 F_c=c_4r_4+c_6r_6+c_8r_8+c_{10}r_{10}.                       \tag{2}
\]

Demand that its marked trace cancel the Tate \(q\)- and constant channels
and the weight-eight level-two channel.  The complete integral solution is

\[
\boxed{
(c_4,c_6,c_8,c_{10})
=m(1,-1,-1,1)+k(4,-3,0,0),\qquad m,k\in\mathbf Z.}             \tag{3}
\]

Every such filter has trace

\[
\boxed{
T(F_c)=m\bigl((q-1)\Theta_{12}(q)-\Theta_{10,2}(q)\bigr).}     \tag{4}
\]

Indeed, weight-eight cancellation forces \(c_8=-c_{10}\); this also
cancels the \(q\)-term.  The remaining constant equation is

\[
3c_4+4c_6=-c_{10}.                                             \tag{5}
\]

Solving (5) over \(\mathbf Z\) gives (3).  Including the lower channel
\(r_2\) cannot improve the exact cancellation: its \(q-1\) trace forces its
coefficient to zero.

The only primitive support-at-most-two direction is the already-known null
filter \(4r_4-3r_6\), whose trace is zero.  Up to sign, the two primitive
three-scale mixed filters are

\[
\boxed{
M_4=3r_{10}-3r_8-r_4,\qquad
M_6=4r_{10}-4r_8-r_6.}                                       \tag{6}
\]

Their traces are respectively three and four times (4).  The canonical
integral unit-response filter is

\[
\boxed{H=r_{10}-r_8+r_4-r_6.}                                 \tag{7}
\]

This is an exact cohomological residual filter, not a memberwise sign
detector.

## 2. Haar-optimal filters

Since \(r_{2j}=q^j\chi_{(2j,0)}\) and the four characters are distinct,
\(USp(4)\) orthogonality gives

\[
\operatorname{Var}_{\rm Haar}(F_c)
=c_4^2q^4+c_6^2q^6+c_8^2q^8+c_{10}^2q^{10}.                   \tag{8}
\]

Per unit response, the sparse variances are

\[
V(M_4/3)=q^{10}+q^8+{q^4\over9},
\qquad
V(M_6/4)=q^{10}+q^8+{q^6\over16}.                             \tag{9}
\]

Thus \(M_4\) is strictly better for every odd \(q\geq3\), because

\[
V(M_6/4)-V(M_4/3)
={q^4(9q^2-16)\over144}>0.                                    \tag{10}
\]

For unit integral response, write

\[
(c_4,c_6,c_8,c_{10})=(1+4k,-1-3k,-1,1).
\]

Then

\[
V(k)-V(0)
=q^4k\bigl((8+6q^2)+(16+9q^2)k\bigr),                        \tag{11}
\]

which is positive for every nonzero integer \(k\).  Hence (7) is the
unique integral Haar minimizer.

Over \(\mathbf Q\), put \(\Delta_q=9q^2+16\).  The unique unit-response
minimum is

\[
\boxed{
G_q=r_{10}-r_8-{3q^2\over\Delta_q}r_4
                   -{4\over\Delta_q}r_6,}                    \tag{12}
\]

with

\[
\boxed{V_{\min}=q^{10}+q^8+{q^6\over9q^2+16}.}                \tag{13}
\]

## 3. Same-characteristic Frobenius interferometry

Fix an odd prime \(p\).  Let \(\gamma_p,\delta_p\) be the roots for
\(\Delta\), and let \(\mu_p,\nu_p\) be those for the weight-ten level-two
form:

\[
\begin{aligned}
\gamma_p+\delta_p&=\tau(p),&\gamma_p\delta_p&=p^{11},\\
\mu_p+\nu_p&=g_p,&\mu_p\nu_p&=p^9.
\end{aligned}                                                   \tag{14}
\]

For an arithmetic extension \(q=p^r\) with \(r\geq1\), the unit mixed
response in (4) is

\[
\begin{aligned}
C_r
&=(p^r-1)(\gamma_p^r+\delta_p^r)-(\mu_p^r+\nu_p^r)\\
&=(p\gamma_p)^r+(p\delta_p)^r-\gamma_p^r-\delta_p^r
  -\mu_p^r-\nu_p^r.                                           \tag{15}
\end{aligned}
\]

For recurrence bookkeeping only, extend the right side of (15) formally to
\(r=0\), where \(C_0=-2\).  This initial value is not a family statistic over
the nonexistent field with \(q=1\).

Thus its six spectral roots are

\[
\boxed{
\{p\gamma_p,p\delta_p,\gamma_p,\delta_p,\mu_p,\nu_p\}.}     \tag{16}
\]

If \(E\) denotes the forward shift in \(r\), the exact order-six
annihilator is

\[
\boxed{
\begin{aligned}
A_p(E)={}&(E^2-p\tau(p)E+p^{13})
          (E^2-\tau(p)E+p^{11})\\
 &\times(E^2-g_pE+p^9).
\end{aligned}}                                                  \tag{17}
\]

The root magnitudes are respectively \(p^{13/2}\), \(p^{11/2}\), and
\(p^{9/2}\).  They are therefore pairwise disjoint.  Within each quadratic
the roots are also distinct: equality would force the square of an integer
Hecke coefficient to equal \(4p^e\) with \(e\) odd, impossible because its
\(p\)-adic valuation would be odd.  All six exponential coefficients in
(15) are nonzero.  Consequently (17) is the minimal recurrence, not just
an annihilator.

Write the three quadratic factors of (17) as

\[
\begin{aligned}
P_s(E)&=E^2-p\tau(p)E+p^{13},\\
P_u(E)&=E^2-\tau(p)E+p^{11},\\
P_g(E)&=E^2-g_pE+p^9.
\end{aligned}                                                   \tag{18}
\]

Products of the other two factors give three exact channel isolators:

\[
\boxed{
\begin{array}{c|c|c}
\text{surviving channel}&\text{operator applied to }C_r&
  \text{recurrence afterward}\\ \hline
p^r\Theta_{12}(p^r)&P_u(E)P_g(E)&P_s(E)\\
-\Theta_{12}(p^r)&P_s(E)P_g(E)&P_u(E)\\
-\Theta_{10,2}(p^r)&P_s(E)P_u(E)&P_g(E)
\end{array}}                                                   \tag{19}
\]

The last operator is also the coarse notch that kills both level-one
channels.  Conversely, \(P_g(E)\) kills the level-two weight-ten channel
and leaves the shifted-minus-unshifted \(\Delta\) spectrum.  The producer
checks all three isolators and their surviving quadratic recurrences with
exact integer arithmetic at \(p=3,5,7\); factor annihilation together with
the same standard purity premise proves them for every odd prime.

The phenomenon is a concrete renormalization warning.  Before filtering,
the \(p^{13r/2}\) component dominates the extension tower even though (4)
contains a lower-weight level-two form with coefficient one.  Raw large-
\(r\) moments will not reveal the latter; the exact recurrence notch does.

## 4. Reproducibility contract

Run

```text
python research/l-families/atlas/function_field/genus2_mixed_cohomology_filter.py --check
python -O research/l-families/atlas/function_field/genus2_mixed_cohomology_filter.py --check
python -m pytest -q tests/test_genus2_mixed_cohomology_filter.py
```

The producer fails closed without relying on Python `assert`.  It preflights
caps of four source files and 2,000,000 source bytes before reading them,
then enforces dynamic caps of 50,000 exact operations, 1,000 lattice
regression points, 5,000 recurrence steps, and extension exponent 18.  A
250,000-byte output cap is checked before either writing or reading the
fixture.  The four-second elapsed-time cap is checked after complete
packet-manifest and canonical-payload serialization and hashing.  The
bounded \((m,k)\)-scan is only a regression check: Bézout's
identity proves the complete lattice.  Likewise, the three small-prime
recurrences are falsification controls: factor annihilation and standard
Deligne purity prove the all-prime statement.  The canonical output is
`genus2_mixed_cohomology_filter.json`.

## 5. Scope

This packet concerns exact family means and compact-group variances.  It
does not assert an individual sign, a zero theorem, RH or GRH, an
average-to-principal-member amplifier, a global motive, or a new
Euler-product identity.  The recurrence is a same-prime extension-tower
identity; it must not be confused with a multi-prime compatible-system
claim.  No external novelty claim is made.
