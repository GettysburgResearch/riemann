# PAPER-0139 — Zur Theorie der abstrakten elliptischen Funktionenkörper. III: Die Struktur des Meromorphismenringes. Die Riemannsche Vermutung

| Field | Value |
|---|---|
| Authors | Hasse, Helmut |
| Year / stratum | 1936 / S2 |
| Venue | J. Reine Angew. Math. 175, 193-208 (1936). |
| Identifiers | zbMATH [0014.24902](https://zbmath.org/?q=an:0014.24902) · DOI [10.1515/crll.1936.175.193](https://doi.org/10.1515/crll.1936.175.193) |
| MSC | 11R58, 14H05 |
| Families | E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/id/PPN243919689_0175 |
| Selection | score 2.8714, in-pool citations 6, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Show the Riemann hypothesis for algebraic function fields of genus 1 over a finite field k_0=\mathbb{F}_q, i.e. that the L-polynomial P(z)=z^2-(q+1-N_1)z+q has roots of absolute value \sqrt q (equivalently (q+1-N_1)^2\le4q), via the structure of the ring of meromorphisms (endomorphisms) of K over the algebraic closure k.

**Historical motivation.** Answer to Artin's conjecture (RH for congruence zeta functions) in genus 1, announced 1933-35; this is the published 'part III' of the Crelle series (dated Gottingen, 22 Nov 1935).

### Main results

- **THM-PAPER-0139-1** (Normenadditionsformel (1), SS1, theorem, scope: global; pp. 193-194). For arbitrary (normalized) meromorphisms \mu,\nu of K: N(\mu+\nu)+N(\mu-\nu)=2N(\mu)+2N(\nu), where N(\mu)=[K:K\mu] is the degree of the extension. Proved via divisor equivalences (2),(2') and the divisor equalities (3),(3'), the latter in full only under a restriction on the inseparability exponents J(\mu),J(\nu),J(\mu\pm\nu), which suffices for (1); the case p=2 treated separately.
- **THM-PAPER-0139-2** (SS2 conclusion, theorem, scope: global; p. 203). N is a positive semidefinite quadratic form on the ring M of meromorphisms: N(\mu\bar\mu - m)=0 for m=N(\mu), and the quadratic polynomial Q(z)=z^2-lz+m (l=\mu+\bar\mu) has discriminant l^2-4m\le0. The quotient ring \Sigma of M is Q, an imaginary quadratic field P(\delta), or an imaginary quadratic division algebra over Q; M is an order in \Sigma.
- **THM-PAPER-0139-3** (SS3, structure of M (k=\bar{\mathbb{F}}_p), theorem, scope: global; pp. 203-205). If k is absolutely algebraic (algebraic closure of \mathbb{F}_p) and \bar\pi\ne\pi (\pi the Frobenius meromorphism (x\pi,y\pi)=(x^q,y^q)), then M is an order in an imaginary quadratic number field in which p splits into two (distinct or equal) prime ideals. The automorphism group is generally cyclic of order 2, order 4 or 6 only for the maximal orders of discriminant -4 or -3. Frobenius satisfies Q(\pi)=\pi^2-l\pi+q=0 with l^2\le4q, N(\pi)=q, J(\pi)=q. Limit cases: (a) \bar\pi=\pi, l=\pm2\sqrt q, \pi^2=q; (b) \bar\pi=-\pi, l=0, \pi^2=-q; they occur iff A=0 (supersingular case); for A\ne0, 0<l^2<4q.
- **THM-PAPER-0139-4** (SS4, Riemann hypothesis for L(s), theorem, scope: global; pp. 205-207). With K_0=k_0(x,y) of genus 1, L(s)=1-(q+1-N_1)q^{-s}+q^{1-2s}, P(z)=q^{2s}L(s)=z^2-(q+1-N_1)z+q (z=q^s), h=P(1)=N_1 the class number. RH, i.e. (q+1-N_1)^2\le4q, follows from the identity P=Q, which reduces to the single equality N(\pi-1)=h=N_1, proved by counting solutions of (\pi-1)\mathfrak p=\mathfrak o in the divisor class group D_0 of degree-0 classes.
- **THM-PAPER-0139-5** (SS4.4 operator form, theorem, scope: global; pp. 207-208). Replacing z=q^s in P(z) by the Frobenius operator \pi gives a null operator on D_0: P(\pi)\mathfrak p=\pi^2\mathfrak p-(q+1-N_1)\pi\mathfrak p+q\mathfrak p=\mathfrak o. The zeros of L(s) lie on \mathrm{Re}\,s=1/2 in the strip 0\le\mathrm{Im}\,s<2\pi/\log q.

### Key definitions

- Meromorphism of K: a field isomorphism of K into itself over k (endomorphism of the associated elliptic curve), forming a ring M
- N(\mu)=[K:K\mu], degree of the meromorphism
- J(\mu): inseparability exponent; c_\mu the factor with (du)\mu=c_\mu du
- \bar\mu: conjugate meromorphism defined by \mu+\bar\mu=l, \mu\bar\mu=m
- Frobenius \pi: (x\pi,y\pi)=(x^q,y^q) with q=|k_0|

### Principal lemmas

- **THM-PAPER-0139-L1** (Inseparability exponent J(\mu), SS1.2; p. 194). J(\mu)=1 iff c_\mu\ne0 (where (du)\mu=c_\mu du); J(n)=1 iff n\not\equiv0 mod p; J(\mu+\nu)\ge\min(J(\mu),J(\nu)); J(\mu\nu)=J(\mu)J(\nu), giving a non-archimedean valuation on M. — *Role:* Controls the degree formulas N=N_0 J needed in (1) and in the final identification N(\pi-1)=N_0(\pi-1).
- **THM-PAPER-0139-L2** (Order of automorphism group (SS3.3); pp. 204-205). \pi^2=q\zeta with \zeta a normalized automorphism, necessarily a 2nd, 4th or 6th root of unity in P(\pi); if \zeta\ne\pm1 then \pi would have degree >2 over P, contradiction; hence \pi^2=\pm q. — *Role:* Shows limit cases a),b) occur iff A=0.
- **THM-PAPER-0139-L3** (Identification N(\pi-1)=h (SS4.3); pp. 206-207). Since c_{\pi-1}=c_\pi-1=-1\ne0, J(\pi-1)=1 and N(\pi-1)=N_0(\pi-1)= number of \mathfrak p in D_0 with (\pi-1)\mathfrak p=\mathfrak o; by Riemann-Roch each degree-0 class is represented uniquely by \mathfrak p/\mathfrak o with \mathfrak p of degree 1, so h=N_1 equals the same count (fixed points of Frobenius). — *Role:* Key step: relates the degree of Frobenius-minus-one to the point count, giving P(1)=Q(1).

### Proof architecture

(1) Prove the parallelogram law N(\mu+\nu)+N(\mu-\nu)=2N(\mu)+2N(\nu) from divisor equivalences; with N\ge0 this makes N a positive semidefinite quadratic form on the meromorphism ring M and gives l^2\le4m for Q(z)=z^2-lz+m (SS1-SS2). (2) Structure of M as an order in an imaginary quadratic field or definite quaternion-type division algebra (SS2.3). (3) For finite base field, Frobenius \pi satisfies Q(\pi)=0 with l^2\le4q (SS3). (4) Identify Q with the L-polynomial P by checking they agree at one point z=1 (both quadratic with the same constant term q after functional equation): P(1)=h, Q(1)=N(\pi-1), and N(\pi-1)=h by fixed-point counting (SS4). Hence the eigenvalues of Frobenius are the zeros of P and satisfy |\pi|=\sqrt q. Imported results: Riemann-Roch, the general theory of congruence zeta functions (Hasse, Sitz. Ber. Berlin 1934), Hasse's own parts I and II (cited as H I, H II) and a Behrbohm/Teichmuller simplification of the quadratic-form argument (footnote p. 203).

Dependency edges: CAND-00130 → CAND-00151 (same programme; see abstract-foundation paper (unverified direction))

**Imported results.** Riemann-Roch theorem; Hasse, Uber die Kongruenzzetafunktionen, Sitzungsber. Preuss. Akad. Wiss. Berlin 1934 (rationality of L(s), functional equation); Wedderburn-type classification of quadratic division algebras over Q (cited as 'bekannter Satz'); H I, H II (Crelle 175, 1936) results

**Techniques.** positive-definite norm form on endomorphism ring; Riemann-Roch; degree of Frobenius-minus-1 equals number of fixed points; inseparability exponent valuation; reduction of quadratic L-polynomial identity to one value

## Context and interpretation

**Importance and obstacle overcome.** First complete proof of the RH for a family of curves over finite fields (genus 1, Hasse's theorem |q+1-N_1|\le2\sqrt q); overcame the lack of a positivity statement by finding the positive semidefinite form N on meromorphisms with the parallelogram law, avoiding Ostrowski-type archimedean valuation arguments (original approach replaced via Behrbohm, footnote 5).

**Relation to prior work.** Parts I and II (H I, H II) of the same series in Crelle 175; Hasse, 'Uber die Kongruenzzetafunktionen' (Sitz.-Ber. Berlin 1934); Behrbohm (note appended to Hasse's Gottingen Nachrichten 1935 announcement), Teichmuller (simplified argument); Witt reviews in Zbl. 13 (1936) 197-198; later Deuring and Weil.

**Limitations and open questions.** Genus 1 only; Hasse notes the (3) divisor equalities are proved under a restriction on inseparability exponents (enough for (1)), and that the general case 'should not be hard'. Structure of M in the case \bar\pi=\pi remains open (p. 205): which of the types I, II, III occurs; type III occurs e.g. for p=3, q=3^2, y^2=x^3-2x-1.

**Ideas in remarks/appendices/abandoned paths.** p. 208: RH reformulated as 'P(\pi) is the zero operator on D_0', replacing z=q^s by Frobenius; figure on p. 207 depicts double zeros and generic position of conjugate zeros in the strip 0\le\mathrm{Im}\,s<2\pi/\log q (limit cases a),b) correspond to supersingular, \pi^2=\pm q); p. 205 observation that case \bar\pi=\pi leaves open which of the three types I, II, III of M occurs.

## Research potential

- **Hypotheses that might be weakened.** The restriction on inseparability exponents J in the proof of (3) is flagged by Hasse as removable; p=2 special handling could be audited separately. Genus-1 assumption is the principal one.
- **Generalizations.** Weil's 1940-48 extension to arbitrary genus replaces N by the Rosati-type positive involution on divisor correspondences (Castelnuovo-Severi inequality); Hasse's N(\pi-1)=h step is the genus-1 case of the Lefschetz fixed-point formula.
- **Candidate connections.** Template for 'positivity of a quadratic form on an endomorphism ring implies zeros on a critical line', an analogy for Weil-positivity / Li-Keiper-type criteria in the number-field case; the operator form P(\pi)=0 on D_0 is the Frobenius-eigenvalue picture behind Hilbert-Polya heuristics.
- **Reusable lemmas.** Parallelogram law (1) and l^2\le4q from positivity of N; the single-point identification trick P(1)=Q(1).
- **Possible experiments.** Verify numerically over \mathbb{F}_q (small q) for random elliptic curves that N(\pi-1)=#E(\mathbb{F}_q), l=q+1-N_1 and that the zero strip positions match the pictures (p. 207); also compute M for supersingular curves with \bar\pi=\pi.
- **Risks / barriers.** No known analogue of an endomorphism ring with positive form for \zeta(s) over \mathbb{Q}; the transfer to number fields requires an arithmetic-geometry object (Deninger's cohomological programme, F_1-geometry) that is not available.

## Audit notes (Level 1 reader)

Pages 195-202 (proof of (1), details of positivity and N\ge0) were not read; assessment of those steps is unverified. In pp. 203-208 no gap noticed; the claim at p. 203 that 'N(\mu)\ge0 is adjoined' as a hypothesis is justified by definition of N as a degree (non-negative).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00130`; harvest queries: kw_RH_any.
- Triage decision: include — Hasse's elliptic function field series containing the proof of RH for elliptic curves.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
