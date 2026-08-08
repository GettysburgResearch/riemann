# T-26802 — Critical annular source-change Selberg descent proposal for RH

Claim ID: `T-26802`  
Title: The RH-sensitive physical source has an exact annular carry image, and its difference from the reserved generalized-prime profile is a complete half-scale divisor family  
Status: **FULL CONDITIONAL RH PROPOSAL — STRICT ANNULAR CHARGE/RESERVE INEQUALITY OPEN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Scope: global full-problem attack; RH is not claimed proved

## 1. Corrections absorbed

The first annular draft used the coefficient sequence
\(a_\omega(m)\log m\) in both physical and carry roles. `R-26802` proves that
its physical primitive cancels every reciprocal-zeta pole. That specialization
is not an RH detector.

The exact annular geometry survives. The RH-sensitive physical coefficients are

\[
 \boxed{x_m=\Lambda_\omega(m),}
\]

whose carry image has coefficient sequence

\[
 \boxed{W=\omega_2*\Lambda_\omega.}
\]

`L-26805` then gives the exact source change

\[
 \boxed{a_\omega*W=\Lambda_\omega,}
\]

with identity coefficient one at the current scale and every remaining term at
scale at most one half.

Thus the source mismatch becomes a strict divisor descent rather than an
uncontrolled same-scale inversion.

## 2. Exact arithmetic source

Retain

\[
 \Omega_2(s)
 =\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
 \tag{T-26802.1}
\]

with coefficient sequence \(\omega_2\), positive inverse \(a_\omega\), and
nonnegative generalized-prime sequence \(\Lambda_\omega\).

The parity frame and finite Bézout synthesis of PR #263 reconstruct the
reciprocal-zeta source without deleting any hypothetical off-line pole. PR #241
supplies the independent-frequency reflected physical block.

Use the compact window

\[
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right],
 \tag{T-26802.2}
\]

and the critical polynomial

\[
 p_{\rm crit}(z)
 =(1-z)(1-2z)(1-\sqrt2z)^2.
\]

The parity-paired safe windows are

\[
 H_\pm=p_{\rm crit}(\pm\tau_{\log2})h_\omega.
 \tag{T-26802.3}
\]

They cancel the \(s=1\) mode and the double \(s=1/2\) mode. PR #263 supplies
the two-channel frame and finite Bézout reconstruction.

## 3. Exact RH-sensitive annular source map

For a dyadic annulus

\[
 \mathcal A_M=[M,2M)\cap\mathbb N,
\]

put

\[
 x_m=\Lambda_\omega(m)\mathbf1_{\mathcal A_M}(m).
 \tag{T-26802.4}
\]

The corresponding physical transform contains

\[
 -\frac{A_\omega'}{A_\omega}(s)
 =-\frac{\zeta'}{\zeta}(s)+\frac{E'}E(s),
\]

so every hypothetical off-line zeta zero remains a pole.

`L-26802` gives the unfiltered exact weighted split. `L-26804` gives, for each
critical parity window, potentials \(F_{\pm,M}\) satisfying

\[
 \boxed{
 \left\|
 H_\pm*
 \sum_m\frac{x_m}{\sqrt m}\delta_{\log m}
 \right\|_2^2
 =
 \sum_{j=1}^{128M-1}
 \frac{|(\mathcal S_{256M-1}F_{\pm,M})(j)|^2}{j(j+1)}.
 }
 \tag{T-26802.5}
\]

The split vectors are finite dyadic combinations of

\[
 \boxed{
 \mathcal W_N(j)
 =\sum_{q\le N}W(q)\chi_{N,q}(j),
 \qquad
 W=\omega_2*\Lambda_\omega.
 }
 \tag{T-26802.6}
\]

This is an exact critically normalized physical-to-carry congruence for the
RH-sensitive source.

## 4. Exact source-change descent to the reserved carry profile

PR #269 proves a strict transition reserve for

\[
 \mathcal P_N(j)
 =\sum_{q\le N}\Lambda_\omega(q)\chi_{N,q}(j).
 \tag{T-26802.7}
\]

`L-26805` proves coefficientwise

\[
 \boxed{
 \Lambda_\omega(n)
 =W(n)+
 \sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)W(n/d).
 }
 \tag{T-26802.8}
\]

Every destination \(n/d\) is at most \(n/2\). In carry coordinates,

\[
 \boxed{
 \mathcal P_N
 =\mathcal W_N+
 \sum_{d=2}^{N}a_\omega(d)
 \sum_{m\le N/d}W(m)\chi_{N,dm}.
 }
 \tag{T-26802.9}
\]

Thus the established reserved profile equals the current RH-sensitive profile
plus a complete family of strict half-scale source rows. The current coefficient
is exactly one; there is no same-scale condition number.

A production proof must complete the \(\mathcal P_N\) square before estimating
the lower-scale family.

## 5. Exact transition localization

PR #269 proves for every source wavelet:

\[
 (\mathcal K(n,m))_-\ne0
 \quad\Longrightarrow\quad
 2m\le n<5m.
 \tag{T-26802.10}
\]

The inner band and the complete quotient tail have the correct sign. The
transition profile \(\mathcal P_N\) has an absolute source-specific Schur
reserve. After (T-26802.9), every adverse current-scale row is therefore
confined to the quotient cells

\[
 \boxed{2,3,4.}
 \tag{T-26802.11}
\]

All other source-change terms are declared lower-scale rows.

## 6. Exact generalized Selberg lower-scale ledger

Put

\[
 \mathcal F
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
\]

`L-26803` proves

\[
 \boxed{
 a_\omega(n)\log^2n
 =\mathcal F(n)+
 \sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)\mathcal F(n/d).
 }
 \tag{T-26802.12}
\]

The proper-divisor defect is coefficientwise nonnegative and every destination
is at most half scale.

The source-change family (T-26802.8) and the Selberg-defect family
(T-26802.12) use the same positive inverse coefficients. They must be assembled
in one reflected lower-block ledger, not charged separately by total variation.

The digital boundary

\[
 \varepsilon-\frac52\delta_2+\delta_4
 \tag{T-26802.13}
\]

and every finite collar row remain explicit.

## 7. Eight-color orthogonality

The critical filtered output of \(\mathcal A_M\) lies in \([M,128M)\).
Annuli whose base scales differ by \(256\) have disjoint physical support.

Split dyadic annuli into eight colors

\[
 M=2^{8r+c},
 \qquad c=0,1,\ldots,7.
 \tag{T-26802.14}
\]

Within one color, both parity-filtered physical signals are orthogonal across
annuli. The complete source is therefore a fixed eight-channel system.

## 8. Sole open theorem — Corrected Annular Split-Selberg Descent (`ASSD`)

For each sufficiently large annulus and color, assemble:

1. the complete parity-paired RH-sensitive source manifest;
2. PR #241's independent-frequency reflected block;
3. the exact critical annular split congruence (T-26802.5);
4. the source-change square (T-26802.9);
5. transition cells \(2,3,4\) and the PR #269 reserve;
6. the proper-divisor Selberg ledger (T-26802.12);
7. the digital boundary and every finite endpoint/collar row.

The required production inequality is

\[
 \boxed{
 \kappa_0 E_{r,c}+Q_{r,c}
 \le C(1+r)^A+
 \sum_{\ell\ge1}\sum_{d=0}^{7}
 \theta_{\ell,c,d}E_{r-\ell,d},
 }
 \tag{T-26802.15}
\]

with

\[
 Q_{r,c}\ge0,
 \qquad
 \kappa_0>0,
 \qquad
 \theta_{\ell,c,d}\ge0,
\]

and

\[
 \boxed{
 \sup_c\sum_{\ell,d}\theta_{\ell,c,d}<\kappa_0.
 }
 \tag{T-26802.16}
\]

Here \(E_{r,c}\) is the declared parity-paired block energy of the RH-sensitive
reciprocal-zeta source. Every lower-block coefficient must be derived from the
source-change, Selberg-defect, or digital ledger; no undeclared norm estimate is
permitted.

This strict charge/reserve inequality is the corrected `ASSD` theorem.

## 9. Why this is a full-problem attack

The remaining theorem no longer asks for:

- a physical-to-carry operator;
- a safe compact window;
- a parity reconstruction;
- a generic carry frame;
- control of quotient rows beyond factor five;
- an unidentified Selberg remainder;
- an inversion from \(P\) to \(W\);
- Bottom-Charge Positivity as an independent miracle;
- full Carry Saturation, Green Energy, BTP, or Brownian SAT.

All source changes and remainders are exact strict-scale identities. The only
open issue is whether their total reflected lower-block charge is strictly below
the current annular reserve.

## 10. ASSD implies RH

Let

\[
 F_r=\max_cE_{r,c}.
\]

Dropping \(Q_{r,c}\) and using (T-26802.16) gives

\[
 F_r\le C_1(1+r)^A+\vartheta\max_{\ell\ge1}F_{r-\ell},
 \qquad \vartheta<1.
\]

Induction yields

\[
 F_r=O((1+r)^A)=e^{o(r)}.
 \tag{T-26802.17}
\]

The finite parity synthesis transfers the same exponent to the dyadic
fixed-ratio Mertens shell. PR #263 `L-26209` gives the Riesz and bottom-charge
estimates. Their Mellin transform has an uncancelled reciprocal-zeta pole at
every hypothetical zero with real part greater than \(1/2\). Functional-
equation symmetry then gives

\[
 \boxed{\mathrm{ASSD}\Longrightarrow\mathrm{RH}.}
 \tag{T-26802.18}
\]

## 11. Automatic rejection

Reject a claimed proof if it:

1. uses \(a_\omega\log\) as the RH-sensitive physical coefficient;
2. silently replaces \(\mathcal W\) by \(\mathcal P\);
3. drops a source-change proper divisor;
4. takes absolute values before completing the \(\mathcal P\) square;
5. treats \(a_\omega\) as a summable contraction kernel;
6. replaces the two-frequency block by a diagonal integral;
7. omits a parity channel, dyadic delay, or reflected cross term;
8. leaves a negative current row outside cells \(2,3,4\);
9. drops the generalized Selberg defect;
10. has total lower-block charge at least the reserve;
11. promotes a finite matrix ladder to the uniform theorem.

## 12. Exact status

```text
opposite-parity source and parity frame          proposed exact
critical compact physical windows                proposed exact
RH-sensitive annular physical/carry map          proposed exact + replay
source-change current + half-scale identity      proposed exact + replay
factor-five localization for reserved profile    proposed complete
reserved generalized-prime carry Schur moat      proposed complete
positive Selberg proper-divisor half-scale defect proposed exact + replay
ASSD strict reflected charge/reserve inequality  OPEN / RH-BEARING
ASSD -> shell energy -> RH                        complete conditional chain
Riemann Hypothesis                                UNPROVED
```
