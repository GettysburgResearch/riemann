# Implication matrix and hybrid closure candidates

Status: research synthesis; RH unproved.

## Goal

The live repository contains several producer, transport, critical-estimate, detector, and no-go theorems that are individually incomplete but may compose across branches. This note treats them as an implication matrix rather than a route list.

## Canonical node classes

- P: source-faithful producer / ownership theorem
- T: transport / compactification / desmoothing theorem
- E: critical signed, negative-mass, variation, or Carleson estimate
- D: Mellin/Mertens/Landau detector
- N: exact no-go / interface firewall

## Matrix highlights

| source node | target node | relation | status |
|---|---|---|---|
| PR #652 sequential first-owner Euler identity | native source preservation | exact | proved |
| PR #653 subpower negative mass | RH | implication | proved |
| PR #663 every SHARP power m>=2 positive | critical m=1 | homogeneity descent | blocked at prime-harmonic wall |
| PR #676 centered Bernstein hierarchy | critical remainder | exact positive descent until final step | proved |
| PR #677 finite Euler squaring | critical owner mass | converts p^-1 to p^-2 below cutoff | proved on finite corridor |
| PR #674 minimal ratio-eight wavelet | compact Mertens frame | exact | proved |
| PR #675 wavelet energy | RH | equivalence | proved |
| PR #688 largest-prime decomposition | rough bilinear source | exact, smooth sector removed | proved |
| PR #671 root-containing Hardy/GCD squares | RH | equivalence | proved; not discarded, but no independent leverage |
| PR #673 positive priority flux | closure | false | refuted |
| PR #686 QPET one-pole route | closure | false | refuted |

## Hybrid A: largest-prime ownership + finite cofactor squaring + compact wavelet

Start from PR #688:

G_mu(X)
 = - sum_{p>Y_X} p^-1/2
      sum_{X/(8p)<=m<=X/p, P+(m)<p}
      mu(m)m^-1/2 K_0(X/(pm))
   + X^-1/6+o(1).

The outer prime p is unique. This matters because finite Euler squaring may be applied only to the cofactor m, leaving p as a literal owner. For a cutoff Z below p, square the small-prime Euler factors of m:

(1-r_q U_q)(1+r_q U_q)=1-r_q^2 U_(q^2).

Thus every squared cofactor prime contributes activity 1/q^2, while p remains the unique unsquared owner. The smooth sector is already negligible and the wavelet support has fixed ratio 8.

The intended composite theorem is HCFB100600:

1. choose Y_X=(log X)^(3/2);
2. choose a cofactor cutoff Z_X growing subpolynomially but below every retained owner p;
3. square q<=Z_X inside m only;
4. prove the resulting cofactor owner mass is <1 uniformly;
5. use adjacent-level pairing in m before summing p;
6. show the remaining unsquared cofactor tail contributes X^o(1) in logarithmic negative mass.

Why the combination is genuinely new: PR #688 alone leaves a signed rough bilinear form; PR #677 alone gives only an initial positivity corridor and cannot be positively inverted. Largest-prime ownership prevents squaring from acting on the terminal p and allows the completion to be interpreted as a source refinement of m rather than an X-dependent modification of the conclusion-facing detector.

Open interface: source-faithful cofactor desquaring/averaging after summing over the unique p. This must be proved without a signed inverse.

## Hybrid B: activation-free quadratic descent + compact wavelet Abel frame

PR #673 gives

dG_{-1}(u)=4e^{-u}L_{-1}(e^u)du
with G_{-1}>=0 and no activation atoms.
PR #689 gives an exact compact Abel-Mertens representation of the ratio-eight wavelet.

The candidate is to express the compact wavelet as a finite signed dilation of L_{-1}, then integrate by parts against dG_{-1}. If the resulting coefficient on downward variation is nonnegative, the RH-equivalent wavelet estimate follows from the positive quadratic envelope plus a subpower boundary term.

This composition is not assumed valid. Its kernel sign is the first hostile check.

## Hybrid C: finite squaring + centered Bernstein final step

PR #676 fails only at sigma=1. PR #677 replaces p^-1 by p^-2 below Z, leaving only sum_(Z<p<=X)1/p. On X<=Z^(10/9), the complete critical owner mass is <3/4, so the final centered remainder is positive after finite completion.

The missing composition theorem is not positivity of an X-dependent completed observable; that route is invalid for Landau. The correct use is local: insert exact same-prime three-state blocks only inside the activation/downward-variation ledger of the fixed original critical observable. Small primes then become strictly subcritical locally, while only a short large-prime collar remains.

## Priority matrix

1. HCFB100600: largest-prime + cofactor squaring + wavelet.
2. LVAR100601: local squaring inside activation-free variation ledger.
3. QWAT100602: quadratic-downward-variation to compact-wavelet Abel transport.

Any one of these, if completed with subpower logarithmic loss, feeds an already-proved detector and yields RH.

## Firewalls retained

- RH-equivalent does not mean useless; it means no gain follows from tautological reformulation alone.
- Positive finite-completion inversion is false.
- X-dependent initial positivity corridors cannot be fed directly to Landau.
- Root-containing positive squares do not become root-free by estimating only excess terms.
- Source-blind Cauchy-Schwarz and generic labelled collapse pay power-sized multiplicity.

RH remains unproved.