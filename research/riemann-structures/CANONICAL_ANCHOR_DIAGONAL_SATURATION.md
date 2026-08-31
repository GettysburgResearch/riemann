# A canonical source realizes the already-known opposite-owner diagonal obstruction

Status: **exact seven-window canonical coefficient restriction and cofinal
principal anchor-diagonal estimate**. R-106095 and R-106110 already retract
L-106094 and identify its unpaid opposite-owner \(Q\) count. That correction
is inherited, not a new error discovered by this packet. The added result is
an actual canonical coefficient family and an exact factorization realizing
power growth in its principal channel.

Only the declared seven-window source restriction is estimated here.
It is not claimed orthogonal in the physical Mellin norm. No lower bound for
the unrestricted canonical tail, complete retained-gamma family, or native
principal moment follows. No RH claim is made.

## 1. Keep the inherited operation and source normalization

Use exactly the seven disjoint prime windows of the frozen dense-owner
packet, with \(U\) dyadic and \(Y=U^6\):
\[
 I_j=((1+j/1000)U,(1+(j+1)/1000)U),\quad j=1,\ldots,7.
\]
Choose \(p,q,r,s,g,\ell,\rho\) successively in those windows. Let
\(\mathcal P_U=\{pq\}\), \(\mathcal Q_U=\{rs\}\), and let
\(\mathcal R_U\) be the primes in \(I_7\).
For every \(g,\ell,P,Q\), sum **all** \(\rho\in\mathcal R_U\) inside
the opposite tail. The left anchor is \(\alpha=(g,\ell,P)\); \(Q\)
is its separate opposite-owner index, exactly as in L-106093.

The frozen source proves all required clean pair incidences, \(\rho>\ell\),
\(g<U^2/4\), the full-core owner inequalities, and
\[
 N=P(g\ell)^2,\quad M_\rho=Q(g\rho)^2,\qquad
 Y<N,M_\rho<11Y/10.                                         \tag{1}
\]
Both cores have two positive Boolean histories and canonical pair share
\(1/6\). Their aggregated one-sided amplitudes are therefore
\[
 A_\alpha(t)=\frac{e^{-it\log N}}{3\sqrt N},\qquad
 B_{g,\ell,Q}(t)
 =\sum_{\rho\in\mathcal R_U}
       \frac{e^{-it\log M_\rho}}{3\sqrt{M_\rho}}.              \tag{2}
\]
The anchor-dependent incidence mask is identically one on this prescribed
rectangle because the seven prime windows are disjoint. This statement is
about this coefficient restriction, not about additional native gamma labels.

For each \(Q,\ell\), retain its unique actual quadratic class
\(\sigma=\chi_\ell(Qg^2)=\chi_\ell(Q)\). Summing those classes does not
duplicate any \(Q\). A different choice of principal square root changes
only the harmless fixed class sign. The principal channel in L-106093.9 has
the exact factor \(c_\ell=(\ell+1)/(\ell-1)\).

Define the same-anchor principal quantity in this restricted model by
\[
 H_U=
 \sum_{g,\ell,P,Q}g^2\ell Q\,c_\ell
 \int_{\mathbb R}|A_\alpha(t)|^2|B_{g,\ell,Q}(t)|^2d\nu(t),
 \qquad d\nu=\frac{|\widehat\kappa(t)|^2}{2\pi}\,dt.             \tag{3}
\]
The left anchor is diagonalized; distinct right-tail primes are not.
This is the principal portion of the old \(Q\)-indexed operation, not the
corrected dual-amplified operation which sums \(Q\) before squaring.

## 2. The opposite-owner count survives exactly

Set
\[
 S_U=
 \int_{\mathbb R}
 \left|\sum_{\rho\in\mathcal R_U}
       \frac{e^{-2it\log\rho}}{\rho}\right|^2d\nu(t).
\]
The common \(Q g^2\) phase has modulus one, so
\[
 \int|B_{g,\ell,Q}|^2d\nu=\frac{S_U}{9g^2Q}.
\]
Also \(|A_\alpha|^2=1/(9Pg^2\ell^2)\). Therefore every \(Q\) gives
the same principal contribution at fixed \(g,\ell,P\):
\[
 g^2\ell Qc_\ell\int|A_\alpha|^2|B_{g,\ell,Q}|^2d\nu
 =\frac{c_\ell S_U}{81g^2\ell P}.
\]
Consequently the exact factorization is
\[
 \boxed{
 H_U=\frac{\#\mathcal Q_U}{81}
      \left(\sum_g\frac1{g^2}\right)
      \left(\sum_\ell\frac{c_\ell}{\ell}\right)
      \left(\sum_{P\in\mathcal P_U}\frac1P\right)S_U.
 }                                                          \tag{4}
\]
No estimate or deletion has produced the factor \(\#\mathcal Q_U\).
It is the literal sum remaining after the proposed external weight cancels
the reciprocal \(Q\).

Write \(\Gamma(v)=\int e^{itv}d\nu(t)\). All \(\rho\)'s are in one
fixed narrow interval; hence
\(|2\log(\rho/\rho')|<1/5\).
The frozen native kernel bound is \(\Gamma(v)>1\) on that interval
and \(|\Gamma(v)|\le\Gamma(0)\le384\). It gives
\[
 \left(\sum_\rho\frac1\rho\right)^2
 < S_U
 \le384\left(\sum_\rho\frac1\rho\right)^2.                      \tag{5}
\]
This is an observed norm estimate, not a point evaluation at \(t=0\).

The ordinary PNT in the seven fixed proportional windows yields
\[
 \begin{gathered}
 \#\mathcal Q_U=\Theta(U^2/\log^2U),\qquad
 \sum_g g^{-2}=\Theta(1/(U\log U)),\\
 \sum_\ell c_\ell/\ell=\Theta(1/\log U),\qquad
 \sum_P P^{-1}=\Theta(1/\log^2U),\qquad
 S_U=\Theta(1/\log^2U).
 \end{gathered}
\]
Combining these estimates in (4),
\[
 \boxed{
 H_U=\Theta\!\left(\frac{U}{(\log U)^8}\right)
     =\Theta\!\left(\frac{Y^{1/6}}{(\log Y)^8}\right).
 }                                                          \tag{6}
\]
The physical horizon can be \(X=16Y\), as every index in (1) fits.
The conclusion does not hide an independently enlarged \(X\).
No growing-modulus prime theorem is used.

## 3. Do not confuse anchor diagonal with atomic diagonal

If the right-tail prime is also diagonalized, replace \(S_U\) by
\[
 S_U^{\rm atom}=\Gamma(0)\sum_{\rho\in\mathcal R_U}\rho^{-2}
                =\Theta(1/(U\log U)).
\]
Denote the result of that replacement in (4) by \(H_U^{\rm atom}\).
Then
\[
 \boxed{H_U^{\rm atom}=\Theta((\log U)^{-7}).}                  \tag{7}
\]
Thus (6) does not arise merely from charging the principal atomic diagonal.
The coherent right-tail pairs are essential.

The two literal left Boolean histories each have amplitude \(A_\alpha/2\).
Keeping them as distinct diagonal anchor coordinates, while summing both
right histories inside the tail, changes (3) to \(H_U/2\).
If both sides are kept as literal atoms and the right-tail prime is also
diagonalized, the four literal combinations change (7) to
\(H_U^{\rm atom}/4\). These are exact resolution factors in this model.
No regrouped diagonal is silently substituted for the inherited one.

## 4. Prior correction and exact scope

R-106095 already explains that the \(Q\)-weighted fixed-fibre estimate leaves
a count of \(Q\)-fibres. R-106110 already withdraws the complete same-anchor
diagonal claim and requires \(Q\) to be summed inside the family amplitude.
The still-positive historical header in L-106094 must be read with those
binding retractions.

The present packet supplies the cofinal, observed, canonical coefficient
realization (4)--(7) of that known obstruction. It does not reopen the old
claim, and does not contradict the valid fixed-\(Q\) estimate L-106092.
Nor does it estimate the corrected dual-amplified moment, where cross-\(Q\)
terms are retained inside one member.

Omitted coefficients can cancel a restricted tail after physical readout.
For that reason (6) is not promoted to an unrestricted-tail or full-native
lower bound. The unresolved gamma decoder remains the one stated in the
[observation-gap audit](NATIVE_DECODER_OBSERVATION_GAP.md).

## 5. Bounded replay

The producer authenticates the exact frozen dense artifact and checks all
sixteen \(P,Q\) pairs and their canonical coefficient squares. In that
fixture the rho window has one certified prime. It computes \(H/\Gamma(0)\)
both as the direct sixteen-term physical sum and from (4), verifies that
summing the four \(Q\)'s multiplies the fixed-\(Q\) value by exactly four,
and checks the two literal-history resolution factors.

Simple rational reciprocal-tail controls check the bounds used in (5); they
are explicitly not new prime-source fixtures. The finite single-rho fixture
does not pretend to witness the asymptotic coherent rho count. That count
and the powers in (6)--(7) are proved analytically above from the already
frozen windows and kernel bound.

No new prime search, large phase sum, Fourier integral approximation or
imported executable is used. The publishing agent ran Ruff, producer
write/check and optimized check, and all ten tests in each mode. The ordinary
and optimized tests passed in 1.122 and 1.183 seconds respectively. A final
binding replay follows this validation paragraph; its result and exact
scientific commit are recorded in the handoff and independent review.
The producer binds this note, its code and its tests to its artifact.

| Source | Frozen commit | Git blob |
|---|---|---|
| L-106092, fixed-Q local bound | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | 8dd3a5e54fefe04cc48f1b90e54b5a8266e57476 |
| L-106093, original indexed moment | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df |
| L-106094, historical withdrawn claim | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | 9fea4d5f23feae12d2ac00bbc84b56d6065806fc |
| R-106095, prior Q correction | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | 8d01e79483827f867c91bdafb56569baae5c99c2 |
| R-106110, prior withdrawal and repair | 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b | 019d7e501be0ce6ec8914e5ca505fd61c3923e1f |
| Dense-owner proof | 1fea3c9ce079325d19f5b43c6daa59c76afff921 | c1eeffbc6aa814f860875d58205e97a4d945dc2c |
| Dense-owner artifact | 1fea3c9ce079325d19f5b43c6daa59c76afff921 | 1c289fb3c7d8e959b010267751834ebad6914ec5 |

The complete paths are fixed in the producer. No inherited scientific source
is edited by this sequel.
