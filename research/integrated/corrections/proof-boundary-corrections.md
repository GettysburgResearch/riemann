# Integrated packet: proof-boundary corrections

**Packet status:** integrated reviewed corrections, refutations, and one repaired finite computation  
**Scope:** local finite zero logic, finite algebraic correction, refuted conditional claims, and one finite repaired range; no global RH conclusion  
**Global status:** RH remains unsolved  
**Primary source:** PR [#140](https://github.com/gfreund123/riemann/pull/140) at `5f4df90f890615bde7762278951a8adab7f0083d`  
**Duplicate review unit:** PR [#141](https://github.com/gfreund123/riemann/pull/141) at `e15c50341187b7c0e672594654ad9416b55c9ce7`  
**Review evidence:** `reports/gpt56-pro-09-m/2026-08-01-pre-public-pr-review-132-159.md` at `d29dd935958d88560d73b1865185972ec06f1011`  
**Review verdict:** #140 `VERIFIED`; #141 `VERIFIED` but redundant as a separate merge unit  
**Integration boundary:** every correction below is a distinct reviewed object. No correction retroactively verifies the object it corrects.

## Contents and claim status

| Object | Reviewed status | Exact scope | Original-versus-repair boundary |
|---|---|---|---|
| Saturated Hardy-\(Z\) sign chain | `VERIFIED` | One finite ordinate slab with exact endpoint and total-multiplicity gates | Native local theorem; no global-functional conclusion |
| Local census versus global functional | `REFUTED AS A GENERAL INFERENCE` | Methodological boundary | The invalid inference remains invalid unless a locality/complement theorem is added |
| Hermite power-sum inertia | `VERIFIED CORRECTION` | One finite real polynomial/Hermite matrix | Corrects a false signature formula; the real-rootedness criterion survives |
| Complex-center targeted Li family | `REFUTED AS WRITTEN` | Conditional analytic criterion | No replacement generalized Li theorem is integrated |
| Terminal screw cell coverage | Original proof object `REFUTED`; repaired range `VERIFIED` | One declared finite scalar range | The repaired replay is a new object and does not validate version 1 |

These five objects are grouped because each identifies a reusable proof boundary.

---

## 1. Saturated Hardy-\(Z\) sign chains

### Statement

Let \(a<b\). Assume an unconditional, multiplicity-aware count proves that the open slab

\[
a<\Im\rho<b
\]

contains exactly \(m\) nontrivial zero multiplicities. Let

\[
a<t_0<t_1<\cdots<t_m<b
\]

be exact sample points with directed Hardy-\(Z\) intervals that exclude zero and alternate sign at every adjacent pair. Assume either:

- the slab endpoints are certified zero-free; or
- the count primitive has proved open-endpoint semantics at \(a,b\).

Then:

1. each \((t_j,t_{j+1})\) contains a critical-line zero of odd multiplicity;
2. the \(m\) disjoint intervals account for at least \(m\) multiplicities;
3. equality with the independent total multiplicity forces exactly one multiplicity in each interval;
4. every such zero is simple;
5. no other on- or off-line zero lies in the slab.

Thus

\[
N_0(a,b)=N(a,b)=m.
\]

### Proof extract

Hardy’s \(Z(t)\) is continuous and real. Opposite certified signs force at least one zero in every open interval. A sign change gives odd total multiplicity in that interval, hence at least one. The intervals are disjoint, so they account for at least \(m\) critical-line multiplicities. The independent total count includes all slab zeros, on or off the line, with multiplicity, and equals \(m\). Every lower bound is therefore sharp: one multiplicity lies in every interval and none remains elsewhere. Multiplicity one gives simplicity.

The endpoint gate is load-bearing. Without it, a zero at an endpoint or sample point may be silently omitted or counted under another convention.

### Boundary

This is a **local finite zero-location theorem**. It does not evaluate any Pick, Weil, screw, carrier, or direct-\(\xi\) functional.

### Exact source

- `claims/lemmas/L-13801-saturated-sign-chain-with-endpoint-gates.md`
- source blob `a3cf43412a32a79b8e1ab9d057f85dc0f502436f`

---

## 2. A local zero census does not decide a global functional

### Refuted inference

Without another theorem, the following implication is invalid:

```text
all zeros in one finite ordinate slab lie on the critical line
+ a global functional is sampled near that slab
-----------------------------------------------------------
the global functional candidate is refuted
```

A finite census controls zeros inside the slab. The active Pick, Weil, carrier, screw, and direct-\(\xi\) quantities generally include all zeros or all required prime contributions.

For example, in the centered symmetric normalization,

\[
\frac{\xi'(s)}{\xi(s)}
=
\operatorname*{sym}\sum_\rho\frac1{s-\rho}
\]

contains every zero. A compactly supported Weil test has a finite prime side but an entire zero transform. A direct-\(\xi\) product retains all zero factors unless a proved deflation or localization theorem removes them.

### Locality gate

A local census can retire a candidate only after proving

\[
\text{candidate predicate fails}
\Longrightarrow
\text{an off-line zero lies in the declared slab}.
\]

Valid mechanisms include:

- the candidate itself is a local count discrepancy;
- a complete complement theorem proves all outside contributions nonnegative;
- a rigorous tail bound is smaller than the candidate moat;
- the complete global sum is partitioned and every complementary block is enclosed.

Centering at \(T\), rapid empirical decay, or a nearby zero list is not a locality theorem.

### Exact source

- `claims/refutations/R-13801-local-zero-census-does-not-refute-global-functional.md`
- source blob `492c8b7bc10dd19d0f538ae661f1681732966fec`

---

## 3. Correct Hermite power-sum inertia

### Statement

Let a real polynomial \(P\) have:

- \(r\) distinct real roots;
- \(c\) distinct nonreal conjugate pairs;

with arbitrary positive multiplicities. Form the degree-sized Hermite power-sum matrix

\[
H=(q_{i+j}),
\qquad
q_k=\sum_{\rho\text{ with multiplicity}}\rho^k.
\]

Then

\[
n_+(H)=r+c,\qquad
n_-(H)=c,\qquad
n_0(H)=\deg P-(r+2c).
\]

Consequently,

\[
\operatorname{rank}H=r+2c,
\qquad
\operatorname{signature}H=r.
\]

Therefore \(H\succeq0\) exactly when every root is real, and \(H\succ0\) exactly when every root is real and simple.

### Proof extract

A distinct real root \(x\) of multiplicity \(m\) contributes

\[
m\,v(x)v(x)^{\mathsf T},
\]

which gives one positive direction. A nonreal pair \(z,\bar z\) contributes

\[
2m\bigl(\Re v\,\Re v^{\mathsf T}
-\Im v\,\Im v^{\mathsf T}\bigr),
\]

which has one positive and one negative square on its real two-dimensional span. Distinct-root Vandermonde independence separates the root spans up to congruence. Multiplicity changes weights, not rank.

### Original error

The earlier formula

\[
\operatorname{signature}H
=
(\#\text{ distinct real roots})
-
(\#\text{ nonreal conjugate pairs})
\]

is false. For \(P(X)=X^2+1\), \(H=\operatorname{diag}(2,-2)\) has signature \(0\), not \(-1\).

The PSD real-rootedness criterion survives; the numerical signature formula does not.

### Certificate boundary

A negative principal minor is sufficient but not necessary for non-PSD. A complete finite test uses exact inertia or \(LDL^{\mathsf T}\). Positive semidefiniteness permits repeated real roots. The power-sum producer must certify multiplicity and boundary nonvanishing.

### Exact source

- `claims/lemmas/L-13803-correct-hermite-hankel-inertia.md`
- source blob `fb2c51896fed740cb81ee13ebd750b03b1d839bc`

---

## 4. Complex-center targeted Li coefficients

### Original claim: refuted as written

Let \(\alpha=\tfrac12+u+iv\), \(u>0\), and define

\[
\log\xi(s(z))
=
\log\xi(\alpha)
+
\sum_{n\ge1}\frac{\lambda_n^{(\alpha)}}n z^n,
\]

where

\[
s(z)
=
\frac12+\frac{a+\bar a z}{1-z},
\qquad
a=\alpha-\frac12.
\]

Differentiation at \(z=0\) gives

\[
\lambda_1^{(\alpha)}
=
s'(0)\frac{\xi'(\alpha)}{\xi(\alpha)}
=
2u\,\frac{\xi'(\alpha)}{\xi(\alpha)}.
\]

For \(v\ne0\), this is generally complex. Replacing it by

\[
2u\,\Re\frac{\xi'(\alpha)}{\xi(\alpha)}
\]

changes the analytic coefficient defined by the generating function. Positivity of the original complex coefficient is not an ordered statement.

### What survives

- the half-plane automorphism is algebraically correct;
- model geometry may amplify a hypothetical off-line zero;
- the separate one-point positive-real criterion for \(\Re(\xi'/\xi)\) remains a valid source-qualified route;
- a replacement generalized Li theorem would require an explicitly real symmetrized generating function, a zero-orbit pairing, a convergence convention, and proofs of the required criterion directions.

No such replacement theorem is integrated here.

### Secondary correction

For a classical left zero \(\rho=\tfrac12-\delta+i\gamma\),

\[
\left|1-\frac1\rho\right|^2
=
1+\frac{2\delta}{|\rho|^2},
\]

so

\[
\left|1-\frac1\rho\right|
=
1+\frac{\delta}{|\rho|^2}
+
O\!\left(\frac{\delta^2}{|\rho|^4}\right).
\]

A prior factor \(2\) in the first-order modulus expansion was wrong.

### Exact source

- `claims/refutations/R-13803-targeted-li-family-is-not-proved-as-stated.md`
- source blob `823796478cc327af11b3add8ba2c9441e6818348`

---

## 5. Complete finite coverage includes the terminal cell

### Original proof object: refuted

The version-1 screw scanner bounded a cell only when it encountered the next prime-power knot, then stopped after the last knot. Unless the cutoff itself was a prime power, it omitted

\[
[\log(\text{last prime power}),\log(\text{cutoff})].
\]

At cutoff \(10^7\), there were \(665{,}134\) prime powers but \(665{,}135\) cells including the terminal interval. The original complete-range proof object was invalid.

### Repaired object: separate finite result

The repaired scanner:

- evaluates the terminal interval explicitly;
- requires complete cell coverage;
- stores exact binary endpoints;
- fails closed on any gap;
- replays four disjoint chunks.

The retained same-backend directed replay reported:

```text
prime powers                         665,134
cells including terminal             665,135
all cells strictly positive          true
global lower bound
[0.023227951374527490554974016282146664631 +/- 2.98e-40]
```

This is a **new repaired finite object**. It does not make version 1 valid.

### Exact scope

The repair establishes positivity only for the declared scalar screw predicate on

\[
\frac12\le t\le\log(10^7)
\]

under the declared source normalization. It does not cover larger \(t\), non-arithmetic screw matrices, Gaussian or metric witnesses, the imported equivalence itself, or an independent special-function backend.

This integration did not rerun the computation.

### Exact source

- `claims/refutations/R-13804-x5606-terminal-cell-coverage-gap.md`
- source blob `15b8a0e275776fe37d60a3b99528ba357066672a`

---

## Shared source qualifications

- Hardy-\(Z\) claims require exact real normalization, directed nonzero signs, endpoint semantics, and a multiplicity-aware total zero count.
- Hermite claims require exact real power sums and zero-free contour boundaries.
- \(\xi'/\xi\) claims require the exact completed-\(\xi\) normalization and zero-free evaluation points.
- Screw-range claims retain the source normalization and same-backend implementation risk stated in the source.

## Common misreadings

- \(D(a,b)=0\) is not a global RH certificate.
- “All zeros found are simple” is insufficient unless total multiplicity is saturated.
- A corrected theorem does not verify the original false formula.
- A repaired computation does not validate the incomplete original proof object.
- Useful model geometry is not an RH criterion until the complete theorem is proved.

## Next integration frontier

Apply these rules to the next explicit-formula and operator imports: every extracted object must state endpoint semantics, locality, coverage, source normalization, form domain, and whether it is the original object or a separately reviewed repair.
