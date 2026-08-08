# T-26802 — Annular split-Selberg descent proposal for RH

Claim ID: `T-26802`  
Title: Exact annular physical/carry transference plus a positive half-scale Selberg defect reduce RH to one source-bound reserve inequality  
Status: **FULL CONDITIONAL RH PROPOSAL — ANNULAR RESERVE INEQUALITY OPEN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Scope: global full-problem attack; RH is not claimed proved

## 1. Purpose

The previous consolidated proposal `T-26801` left an unspecified
physical-to-carry operator inside `F5PBT`.

`L-26802` removes that ambiguity for the compact opposite-parity window.
`L-26804` proves that the identity survives every finite dyadic translation
filter, in particular the critical Euler filter cancelling the pole and double
half-pole modes. Thus the safe parity-paired physical channels themselves have
explicit weighted carry splits.

`L-26803` separately removes the unspecified Selberg remainder: its complete
proper-divisor defect is nonnegative and lies at strict half scale.

The remaining theorem is therefore a quantitative reflected reserve inequality,
not a source-map existence assertion.

## 2. Frozen exact source

Retain

\[
 \Omega_2(s)
 =\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
 \tag{T-26802.1}
\]

with coefficient sequence \(\omega_2\), positive inverse \(a_\omega\), and
nonnegative generalized-prime sequence \(\Lambda_\omega\).

The parity frame and finite Bézout synthesis of PR #263 reconstruct this source
without deleting any off-line zeta pole. PR #241 supplies the independent-
frequency reflected physical block.

The compact physical window used in the source map is

\[
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right].
 \tag{T-26802.2}
\]

Define the critical polynomial

\[
 p_{\rm crit}(z)
 =(1-z)(1-2z)(1-\sqrt2z)^2
\]

and the parity-paired safe windows

\[
 H_\pm=p_{\rm crit}(\pm\tau_{\log2})h_\omega.
 \tag{T-26802.2a}
\]

Their multipliers cancel the \(s=1\) mode and the double \(s=1/2\) mode.
PR #263 supplies the two-channel frame and finite Bézout reconstruction.

## 3. Exact current-scale source map

For a dyadic annulus

\[
 \mathcal A_M=\{m:M\le m<2M\},
\]

put

\[
 x_m=a_\omega(m)\log m\,\mathbf1_{\mathcal A_M}(m).
\]

For the unfiltered window, `L-26802` gives the exact weighted split on row
\(16M-1\). For the two critical windows, `L-26804` gives potentials
\(F_{\pm,M}\) and the exact identities

\[
 \boxed{
 \left\|
 H_\pm*
 \sum_m\frac{x_m}{\sqrt m}\delta_{\log m}
 \right\|_2^2
 =
 \sum_{j=1}^{128M-1}
 \frac{
 |(\mathcal S_{256M-1}F_{\pm,M})(j)|^2
 }{j(j+1)}.
 }
 \tag{T-26802.3}
\]

The split vectors are finite dyadic combinations of the annular
generalized-prime Kummer features. The critical square-root normalization,
the main-pole cancellation, both parity channels, and every dyadic delay are
included exactly.

No generic operator theorem or unsafe unfiltered physical window is used.

## 4. Exact transition localization

PR #269 proves for every source wavelet:

\[
 (\mathcal K(n,m))_- \ne0
 \quad\Longrightarrow\quad
 2m\le n<5m.
 \tag{T-26802.5}
\]

It also proves a uniform carry-feature Schur reserve and transfers that reserve
to the actual generalized-prime profile.

Consequently, after the annular map (T-26802.3), every potentially adverse
current-scale forcing row lies in the three quotient cells

\[
 2,\quad3,\quad4.
 \tag{T-26802.6}
\]

The inner band and the complete quotient tail have the correct sign.

## 5. Exact lower-scale Selberg ledger

Put

\[
 \mathcal F
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
\]

`L-26803` proves

\[
 a_\omega(n)\log^2n
 =
 \mathcal F(n)
 +
 \sum_{\substack{k\mid n\\k\ge2}}
 a_\omega(k)\mathcal F(n/k).
 \tag{T-26802.7}
\]

Every argument \(n/k\) on the right is at most \(n/2\). Hence the complete
proper-divisor Selberg defect is a nonnegative lower-block ledger delayed by at
least \(\log2\).

The three digital boundary atoms

\[
 \varepsilon-\frac52\delta_2+\delta_4
 \tag{T-26802.8}
\]

are retained separately. No boundary term is absorbed into the proper-divisor
sum.

## 6. Eight-color orthogonality

The critical filtered output of \(\mathcal A_M\) lies in
\([M,128M)\). Annuli with base scales differing by \(256\) have disjoint
physical support.

Split all dyadic annuli into the eight colors

\[
 M=2^{8r+c},
 \qquad c=0,1,\ldots,7.
 \tag{T-26802.9}
\]

Within each fixed color, both parity-filtered physical signals are orthogonal
across annuli. The full energy is bounded by a fixed multiple of the sum of the
eight color energies. Thus a recurrence may be proved independently on a
fixed eight-channel system.

## 7. Sole open theorem — Annular Split-Selberg Descent (`ASSD`)

For each sufficiently large annulus and each color, assemble:

1. the complete parity-paired source manifest;
2. PR #241's independent-frequency reflected block;
3. the exact congruence (T-26802.3);
4. all transition cells \(2,3,4\);
5. the generalized-prime carry Schur reserve;
6. every proper-divisor route from (T-26802.7);
7. the three digital boundary atoms;
8. all finite endpoint and collar rows.

The required production inequality is

\[
 \boxed{
 \kappa_0 E_{r,c}+Q_{r,c}
 \le
 C(1+r)^A
 +
 \sum_{\ell\ge1}\sum_{d=0}^{7}
 \theta_{\ell,c,d}E_{r-\ell,d},
 }
 \tag{T-26802.10}
\]

where

\[
 Q_{r,c}\ge0,
 \qquad
 \kappa_0>0,
 \qquad
 \theta_{\ell,c,d}\ge0,
 \tag{T-26802.11}
\]

and the strict reserve condition is

\[
 \boxed{
 \sup_c
 \sum_{\ell,d}\theta_{\ell,c,d}
 <\kappa_0.
 }
 \tag{T-26802.12}
\]

Here \(E_{r,c}\) is the declared block energy of the parity-paired
inverse-zeta source, or an exactly equivalent synthesized \(\omega_2\) energy.
The equivalence map must be included in the proof object.

Equations (T-26802.10)--(T-26802.12) are `ASSD`.

## 8. Why ASSD is narrower than the former hinges

ASSD does not ask for:

- a physical-to-carry operator: `L-26802/L-26804` give the safe parity-channel maps explicitly;
- a generic carry frame: only the actual annular source is used;
- control of quotient rows beyond factor five: their sign is closed;
- an unsigned Selberg remainder: `L-26803` routes it positively to half scale;
- Bottom-Charge Positivity as an independent miracle;
- full Carry Saturation, Greedy Slack, Green Energy, BTP, or Brownian SAT.

The only open issue is whether the total declared lower-block and boundary
charge is strictly smaller than the reflected current-scale reserve.

## 9. ASSD implies RH

Let

\[
 F_r=\max_{c}E_{r,c}.
\]

Dropping \(Q_{r,c}\) and using (T-26802.12) gives

\[
 F_r
 \le
 C_1(1+r)^A+\vartheta\max_{\ell\ge1}F_{r-\ell},
 \qquad
 \vartheta<1.
\]

Induction yields

\[
 F_r=O((1+r)^A)=e^{o(r)}.
 \tag{T-26802.13}
\]

The finite parity synthesis transfers the same exponent to the dyadic fixed-
ratio Mertens shell. PR #263 `L-26209` then gives the Riesz and bottom-charge
estimates, and the uncancelled reciprocal-zeta Mellin pole excludes every zero
with real part greater than \(1/2\). Functional-equation symmetry yields

\[
 \boxed{\mathrm{ASSD}\Longrightarrow\mathrm{RH}.}
 \tag{T-26802.14}
\]

## 10. Automatic rejection

Reject a proposed ASSD proof if it:

1. replaces the compact normalized window by an unnormalized step;
2. uses one Fourier frequency instead of PR #241's two-frequency block;
3. omits a parity channel, dyadic delay, or reflected cross term;
4. partitions an odd-core fiber before exact recombination;
5. identifies the carry and physical Grams without replaying (T-26802.3);
6. drops the proper-divisor defect rather than routing it through
   (T-26802.7);
7. leaves a transition row outside cells \(2,3,4\);
8. charges a same-scale boundary term as lower scale;
9. has total lower-block coefficient at least the current reserve;
10. promotes a finite matrix ladder to the uniform recurrence.

## 11. Exact status

```text
opposite-parity source and parity frame       proposed exact
critical parity-filtered compact windows       proposed exact
critical filtered annular split isometries     proposed exact + replay
factor-five transition localization            proposed complete
actual generalized-prime carry reserve         proposed complete
positive proper-divisor half-scale defect      proposed exact + replay
ASSD strict reflected recurrence               OPEN / RH-BEARING
ASSD -> shell energy -> RH                     complete conditional chain
Riemann Hypothesis                             UNPROVED
```
