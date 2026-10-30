# Independent review of the heat-trace lane and prior-art correction

Reviewer: positivity lane, 2026-10-30. Reviewed file: `swarm/heat_trace/report.md`. SHA-256:

`5d37be05f210cad78c1d03d7aafff2eb33e9b0cfbec11b7e79bfd59d03dd27a5`.

## Verdict

The argument in the reviewed version is mathematically sound under its three stated source inputs. I found no blocking error in its normalization, its uniform small-time estimate, its large-time estimate, or its coverage of all claimed derivative orders and times.

**Its numerical conclusion is already exceeded by directly overlapping prior art.** The pinned Polson–Sokolov author manuscript proves the same sign inequalities, with exactly the same heat trace and all-time quantifier, up to more than \(1.52\times10^{25}\), whereas the reviewed result gives \(1.125\times10^{18}\) at the same verified height. The reviewed theorem should be retained, if useful, as an independently derived weaker argument based directly on the counting law and phase cancellation. It must not be described as a new derivative-order frontier or a worldwide record. Its source-qualified proof may have expository or methodological value; this audit does not establish global novelty of that proof.

## 1. Object and normalization

Sra v2 §2.1 uses the heat trace with exponents
\[
\lambda_\rho=-(\rho-\tfrac12)^2=(\gamma_\rho-i\delta_\rho)^2
\]
and one representative of each functional-equation pair, equivalently every upper-half-plane zero with multiplicity. This is exactly the object in the reviewed report.

The Polson–Sokolov source uses \(a_j=-(\rho_j-\tfrac12)^2\), \(W(t)=\sum_j e^{-a_jt}\), and \(c_k(t)=(-1)^kW^{(k)}(t)=\sum_j a_j^ke^{-a_jt}\), with the same convention. Thus \(W=H\) and \(c_k=H_k\) here: no rescaling of time or derivative order is needed. The \(\sqrt{2\theta}\) convention in some earlier Polson abstracts concerns a separately normalized Laplace variable and is not the convention in this book chapter.

Neither this heat trace nor the reciprocal Gaussian-mixture density is the original Riemann theta Fourier kernel. The distinction is respected in the reviewed proof.

## 2. Checks of the analytic proof

### Low derivative orders, every time

For an unverified summand, \(b=2\gamma\delta\) and \(\phi=2\arctan(\delta/\gamma)\) have the same sign. With \(n\le2U/5\), \(n|\phi|\le2/5\); a negative real part therefore requires \(t>\pi/(2\gamma)\). The comparison against the retained verified zero \(\eta\in(U/4,U/3]\) is valid:
\[
a-\eta^2\ge\tfrac78\gamma^2,\qquad
r/\eta^2\le16(\gamma^2+1/4)/U^2.
\]
The derivative of the envelope used in partial summation is negative for \(\gamma\ge U\ge1000\), and the coarse bound \(U^2e^{-9U/80}<1\) suffices. This covers all \(n<400\) under the final hypothesis \(U\ge10^6\).

### Small time, all high derivative orders

The proof controls all integers \(n\ge400\) simultaneously for \(0<t\le10^{-6}\), rather than first fixing \(n\) and then shrinking \(t\).

The key cancellation in the phase
\[
2yu-2n\arctan(u/y),\qquad y=\gamma\sqrt t,\quad u=\delta\sqrt t,
\]
is genuine. Near the saddle \(y=\sqrt n\), the linear phase in \(u\) is proportional to \(y-n/y\), which is small uniformly in \(n\) on a fixed-width saddle interval. The bound \(|\psi|<1/2\) on \(|y-\sqrt n|\le10\) follows from \(n\ge400\), \(|u|\le1/2000\), and the stated arctangent remainder.

The central interval \(|y-\sqrt n|\le1/2\) has at least \(L\log X/20\) zeros, where \(L=t^{-1/2}\ge1000\) and \(X=\sqrt{n/t}\); the error term in the counting law is small against its length times the main-term density. Each central contribution has real part at least \(t^{-n}P_n/8\), \(P_n=n^ne^{-n}\).

The shell envelope \(2P_ne^{-(k-1)^2}\), the shell-count bound \(2L(k+1)\log X\), and the geometric bound on \(\sum_{k\ge10}(k+1)e^{-(k-1)^2}\) give a negative tail far smaller than the central positive mass. The final lower bound with denominator 320 is conservative and valid.

This small-time proof uses only the strip and counting law, with no assumption that high zeros are on the line.

### Large time, the growing finite range

For \(t\ge t_0=10^{-6}\) and \(n\le t_0U^2/8\), the power factor can be absorbed into the Gaussian decay using \(\log(17x)\le3x\), \(x=\gamma^2/U^2\ge1\). The relative tail is bounded by \(e^{-t_0\gamma^2/2}\). The stated reciprocal-square tail estimate then gives \(U^2e^{-t_0U^2/2}<1\), easily satisfied at \(U\ge10^6\).

### Quantifiers

The union of these cases is correct:

- \(n<400\): the low-order argument gives every \(t>0\).
- \(n\ge400\), \(t\le10^{-6}\): the uniform saddle argument applies without an upper bound on \(n\).
- \(t\ge10^{-6}\), \(n\le U^2/(8\cdot10^6)\): the retained-zero argument applies.

There is no exchange of “every fixed \(n\)” with “uniformly all \(n\)” in this proof.

## 3. Sra comparison

The retrieved full text of Sra v2 is `work/sra-v2.txt`, extracted from the PDF blob `f98e0bd0d2d1353245a482581ffa74580c644996` in the author's preprint repository.

Sra Proposition B.1 explicitly gives an asymptotic for **each fixed nonnegative integer** \(j\). That statement alone does not yield the reviewed uniform-in-\(n\) small-time estimate. Sra's representation, zero-count bounds, retained-zero method and finite-verification inputs supply essential context, but the exact uniform theorem in the reviewed file is not directly asserted by that proposition.

This distinction from Sra does not establish novelty relative to other authors, as the following primary source demonstrates.

## 4. Exact overlapping Polson–Sokolov theorem

**Authors:** Nicholas G. Polson and Vadim Sokolov.  
**Title:** *Computing the Riemann Hypothesis: Thorin Measures, Pólya Densities and Hitting Times*.  
**Author repository:** [VadimSokolov/computing_rh](https://github.com/VadimSokolov/computing_rh).  
**Pinned commit:** `f7fdd71f29826a69d84f7d1d416768fdfc02d477` (2026-10-28).  
**README edition/version:** first edition, version 1.4.1.  
**DOI recorded in README:** [10.5281/zenodo.23741450](https://doi.org/10.5281/zenodo.23741450).  
**Exact TeX:** [ch/ch12.tex at the pinned commit](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/ch12.tex), blob `bf3b3bd9e964c4358e48267c3831450c8eaac2f2`.

Theorem 5.1.13, page 112, label `thm:ch12:window`, states the all-time signs through
\[
k\le1.29(H-23)^2>1.16\times10^{25},\qquad H=3\times10^{12}.
\]
It also gives the stronger time-dependent window \(k\le t(H-23)^2\) for \(t\ge1.29\).

Theorem 5.1.16, page 115, label `ps:thm:free`, subsequently improves the result:
\[
(-1)^kW^{(k)}(t)>0
\quad\text{for every }t>0,\quad
0\le k\le1.70(H-23)^2,
\]
and the last quantity exceeds \(1.52\times10^{25}\). It also asserts complete monotonicity on the finite time interval \((0,1.70]\).

The exact theorem number/page is present in the pinned `book.lock.json` entry. The primary TeX was inspected directly at the pinned link/blob above; it is not reproduced in this research packet.

The book's source proof uses Hermite bounds on the explicit formula, prime-power estimates, and a verified-zero window around the saddle. The last theorem reports a ball-arithmetic computation over prime powers up to \(10^9\). This audit verified the exact statement and the overlap, **not** the complete correctness of those numerical certifications. Prior-art qualification does not require treating those computations as independently rerun.

The same chapter includes a Gaussian saddle expansion (label `prop:ch12:ray`) with an explicit cubic error, so even the broad saddle/Gaussian idea should not be advertised as unprecedented.

## 5. Earlier SSRN record and its limits

An indexed primary record was retrieved for Nicholas G. Polson, *Thorin Measures and the Reciprocal Xi Function*, [SSRN 7320139](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7320139), [DOI 10.2139/ssrn.7320139](https://doi.org/10.2139/ssrn.7320139): written 2026-08-20, posted 2026-08-21, 28 pages.

Its indexed abstract states that every derivative condition through order \(8\times10^{10}\) holds without hypothesis. No version identifier was exposed in the retrieved record, and direct SSRN full-text access was blocked. The exact heat-trace/time quantifiers of that older paper were therefore **not** independently checked. In particular the \(\sqrt{2\theta}\) Laplace convention in its abstract should not be silently identified with the book's unscaled \(W\). The full pinned book source supplies the exact matching theorem needed here, and supersedes the weaker abstract-only comparison.

## 6. Implications for the positivity lane

The same book treats the reciprocal density \(f_X\) in [ch/polya3.tex](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/polya3.tex) and [ch/polya6.tex](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/polya6.tex). The normalization matches the positivity report.

Its theorem `pol:thm:pf2` is explicitly titled “PF2, floating point certificate”; it uses Fourier quadrature in the center and a verified low-zero residue expansion in the tail. The preceding section still asks for an exact or interval-arithmetic proof. Sra's separate analytic theorem supplies stronger rigor for this property.

The theorem `pol:thm:approxpf` controls **uniform density and derivative differences**, with \(\varepsilon_0\le1.57\times10^{-10}\), \(\varepsilon_1\le1.3\times10^{-9}\), and \(\varepsilon_2\le1.3\times10^{-8}\). These are not total-variation bounds merely because a summary describes a small distance.

No sequential Laplace-factor removal theorem or tilted-residual log-concavity induction was found in these full sections or targeted repository searches. Our finite-removal corollary is therefore distinct from the exact statements screened here, but is honestly described as a quantified extension of Sra's Appendix C.3 mechanism. This limited screen is not a claim of global priority.

The book's [ch/ch13.tex](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/ch13.tex) already builds off-line-zero perturbations passing large finite heat-trace/Hankel tests. Our countermodel has a different exact target: failure of log-concavity under one Laplace-factor removal, and subsequent failure of positivity, even with arbitrarily small total variation from a PF-infinity density and entire order-one reciprocal. The generic message that finite positivity cannot prove RH is already present in prior literature and is not our novelty claim.

