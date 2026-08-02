# Integrated packet: proof-boundary corrections

**Packet status:** integrated, reviewed in the exact scopes below  
**Global status:** RH remains unsolved  
**Primary source:** PR [#140](https://github.com/gfreund123/riemann/pull/140) at `5f4df90f890615bde7762278951a8adab7f0083d`  
**Duplicate review unit:** PR [#141](https://github.com/gfreund123/riemann/pull/141) at `e15c50341187b7c0e672594654ad9416b55c9ce7`  
**Review evidence:** `reports/gpt56-pro-09-m/2026-08-01-pre-public-pr-review-132-159.md` at review-source commit `d29dd935958d88560d73b1865185972ec06f1011`  
**Review verdict:** #140 `VERIFIED`; #141 `VERIFIED` but redundant as a merge unit  
**Integration note:** this packet extracts reviewed corrections from #140. It does not retroactively change the status of the claims they correct.

## Why this packet belongs near the front door

Several attractive RH arguments failed because they crossed one of four boundaries:

1. lower zero counts were confused with complete multiplicity counts;
2. a local zero census was used to retire a global functional;
3. a Hermite-matrix inertia formula was misstated;
4. a complex analytic Taylor coefficient was replaced by its real part without a theorem;
5. a claimed complete finite scan omitted one terminal cell.

These are not editorial details. They are reusable proof rules for every program in the repository.

---

## 1. Saturated Hardy-\(Z\) sign chains

### Precise statement

Let \(a<b\). Assume an unconditional, multiplicity-aware count proves that the open slab

\[
a<\Im\rho<b
\]

contains exactly \(m\) nontrivial zero multiplicities. Let

\[
a<t_0<t_1<\cdots<t_m<b
\]

be exact sample points with directed Hardy-\(Z\) intervals that exclude zero and alternate sign at every adjacent pair. Assume the slab endpoints are certified zero-free, or that the count primitive has proved open-endpoint semantics at \(a,b\).

Then:

- every \((t_j,t_{j+1})\) contains a critical-line zero of odd multiplicity;
- the \(m\) disjoint intervals account for at least \(m\) multiplicities;
- equality with the independent total multiplicity forces exactly one multiplicity in each interval;
- every such zero is simple;
- no other on- or off-line zero lies in the slab.

Thus \(N_0(a,b)=N(a,b)=m\).

### Proof extract

Hardy’s \(Z(t)\) is continuous and real. Opposite certified endpoint signs force at least one zero in each open interval. A sign change means the sum of multiplicities in that interval is odd, hence at least one. The intervals are disjoint, so the sign chain supplies at least \(m\) critical-line multiplicities. The independent total count includes every zero in the slab, on or off the line, with multiplicity, and equals \(m\). Every lower bound is therefore sharp: each interval contains one multiplicity and no multiplicity remains elsewhere. Multiplicity one gives simplicity.

The endpoint gate is essential. Without it, a zero at a slab endpoint or sample point may be omitted or counted under a different convention.

### Scope

This is a **local finite zero-location theorem**. It does not evaluate a Pick, Weil, screw, carrier, or direct-\(\xi\) functional.

### Source

- `claims/lemmas/L-13801-saturated-sign-chain-with-endpoint-gates.md`
- source blob `a3cf43412a32a79b8e1ab9d057f85dc0f502436f`

---

## 2. Local zero information does not decide a global functional

### Refuted inference

The following implication is invalid without an additional theorem:

```text
all zeros in a finite ordinate slab lie on the critical line
+ a global functional is sampled near that slab
-----------------------------------------------------------
the global functional candidate is refuted
```

A finite census controls zeros inside the slab. The active Pick, Weil, carrier, screw, and direct-\(\xi\) quantities generally include every zero or every prime contribution.

For example,

\[
\frac{\xi'(s)}{\xi(s)}
=\operatorname*{sym}\sum_\rho\frac1{s-\rho}
\]

contains all zeros. A compactly supported Weil test has a finite prime side but an entire zero transform. A direct-\(\xi\) product contains all zero factors unless an exact deflation or localization theorem removes them.

### Locality gate

A local census can retire a candidate only after proving

\[
\text{candidate predicate fails}
\quad\Longrightarrow\quad
\text{an off-line zero lies in the declared slab}.
\]

Valid mechanisms include:

- the candidate is itself a local count discrepancy;
- a complete slab-complement theorem proves every outside contribution nonnegative;
- a rigorous tail/localization bound is smaller than the candidate moat;
- the complete global sum is partitioned and every complementary block is enclosed.

Centering a test at \(T\), rapid empirical decay, or a nearby zero list is not a locality theorem.

### Consequence for repository work

The default status for a globally supported Pick, Weil, screw, carrier, or direct-\(\xi\) candidate after a local census is:

```text
GLOBAL_FUNCTIONAL_NOT_RETIRED
```

unless a route-specific locality or complement theorem is attached.

### Source

- `claims/refutations/R-13801-local-zero-census-does-not-refute-global-functional.md`
- source blob `492c8b7bc10dd19d0f538ae661f1681732966fec`

---

## 3. Correct Hermite power-sum inertia

### Precise statement

Let a real polynomial \(P\) have:

- \(r\) distinct real roots;
- \(c\) distinct nonreal conjugate pairs;

with arbitrary positive multiplicities. Form the degree-sized Hermite power-sum matrix

\[
H=(q_{i+j}),\qquad
q_k=\sum_{\rho\text{ with multiplicity}}\rho^k.
\]

Then

\[
n_+(H)=r+c,\qquad
n_-(H)=c,\qquad
n_0(H)=\deg P-(r+2c).
\]

Therefore

\[
\operatorname{rank}H=r+2c,
\qquad
\operatorname{signature}H=r.
\]

In particular:

\[
H\succeq0
\quad\Longleftrightarrow\quad
\text{all roots of }P\text{ are real},
\]

and \(H\) is positive definite exactly when every root is real and simple.

### Proof extract

A distinct real root \(x\) of multiplicity \(m\) contributes

\[
m\,v(x)v(x)^{\mathsf T},
\qquad
v(x)=(1,x,\ldots),
\]

which gives one positive direction.

A nonreal pair \(z=x+iy,\bar z\), each of multiplicity \(m\), contributes

\[
m\bigl(v(z)v(z)^{\mathsf T}
+v(\bar z)v(\bar z)^{\mathsf T}\bigr)
=
2m\bigl(\Re v\,\Re v^{\mathsf T}
-\Im v\,\Im v^{\mathsf T}\bigr).
\]

On the real span of \(\Re v,\Im v\), this has one positive and one negative square after an invertible real change of basis. Distinct-root Vandermonde independence separates the root spans up to congruence. Repeated multiplicity changes weights, not rank.

### Corrected error

The earlier formula

\[
\operatorname{signature}H
=(\#\text{ distinct real roots})
-(\#\text{ nonreal conjugate pairs})
\]

is false. For \(P(X)=X^2+1\),

\[
H=\operatorname{diag}(2,-2)
\]

has signature \(0\), not \(-1\).

The central real-rootedness criterion survives; the numerical signature formula did not.

### Certificate boundary

- a negative principal minor is sufficient but not necessary for non-PSD;
- complete finite testing uses exact inertia or LDL data;
- positive semidefiniteness permits repeated real roots;
- the contour or power-sum producer must certify multiplicity and boundary nonvanishing.

### Source

- `claims/lemmas/L-13803-correct-hermite-hankel-inertia.md`
- source blob `fb2c51896fed740cb81ee13ebd750b03b1d839bc`

---

## 4. Complex-center targeted Li coefficients

### Refuted statement

Suppose a complex center \(\alpha=\tfrac12+u+iv\), \(u>0\), is used in

\[
\log\xi(s(z))
=
\log\xi(\alpha)
+\sum_{n\ge1}\frac{\lambda_n^{(\alpha)}}n z^n,
\]

with

\[
s(z)=\frac12+\frac{a+\bar a z}{1-z},
\qquad a=\alpha-\frac12.
\]

Differentiating at \(z=0\) gives

\[
\lambda_1^{(\alpha)}
=
s'(0)\frac{\xi'(\alpha)}{\xi(\alpha)}
=
2u\,\frac{\xi'(\alpha)}{\xi(\alpha)}.
\]

For \(v\ne0\), this is generally complex.

The corrected target claim had instead asserted

\[
\lambda_1^{(\alpha)}
=
2u\,\Re\frac{\xi'(\alpha)}{\xi(\alpha)}.
\]

That is the real part of the analytic coefficient, not the coefficient defined by the generating function. Positivity of the complex coefficient is not an ordered statement.

### What survives

- the half-plane automorphism is algebraically correct;
- model geometry may amplify a hypothetical off-line zero;
- the separate one-point positive-real criterion for \(\Re(\xi'/\xi)\) is a legitimate route under its own reviewed theorem;
- a new generalized Li family would need an explicitly real symmetrized generating function, convergence convention, zero-orbit pairing, and a proof of both criterion directions.

### Secondary correction

For a classical left zero \(\rho=\tfrac12-\delta+i\gamma\),

\[
\left|1-\frac1\rho\right|^2
=
1+\frac{2\delta}{|\rho|^2},
\]

and hence

\[
\left|1-\frac1\rho\right|
=
1+\frac{\delta}{|\rho|^2}
+O\!\left(\frac{\delta^2}{|\rho|^4}\right).
\]

A prior factor \(2\) in the first-order modulus expansion was wrong, although the scale \(\gamma^2/\delta\) remains.

### Source

- `claims/refutations/R-13803-targeted-li-family-is-not-proved-as-stated.md`
- source blob `823796478cc327af11b3add8ba2c9441e6818348`

---

## 5. Complete finite coverage includes the terminal cell

### Defect

A version-1 screw scanner bounded each interval only when it encountered the next prime-power knot. It then stopped after the last knot and omitted

\[
[\log(\text{last prime power}),\log(\text{cutoff})]
\]

unless the cutoff itself was a prime power.

At cutoff \(10^7\), there were \(665{,}134\) prime powers but \(665{,}135\) cells including the terminal interval. The original complete-range proof object was invalid.

### Repair and retained finite result

The repaired scanner:

- explicitly evaluates the terminal interval;
- requires complete cell coverage;
- stores exact binary endpoints;
- fails closed on any gap;
- replayed four disjoint chunks.

The retained same-backend directed replay reported:

```text
prime powers                         665,134
cells including terminal             665,135
all cells strictly positive          true
global lower bound
[0.023227951374527490554974016282146664631 +/- 2.98e-40]
```

### Exact scope

This restores positivity only for the declared scalar screw predicate on

\[
\frac12\le t\le\log(10^7)
\]

under the declared normalization. It does not cover:

- larger \(t\);
- non-arithmetic screw matrices;
- Gaussian or metric witnesses;
- the imported equivalence itself;
- an independent special-function backend.

The integration pass did not rerun this computation.

### Source

- `claims/refutations/R-13804-x5606-terminal-cell-coverage-gap.md`
- source blob `15b8a0e275776fe37d60a3b99528ba357066672a`

---

## Dependencies and source qualifications

- Hardy-\(Z\) claims require an exact real normalization, directed nonzero signs, and a multiplicity-aware total zero count.
- Hermite claims require exact real power sums and zero-free contour boundaries.
- \(\xi'/\xi\) claims require the exact completed-\(\xi\) normalization and zero-free evaluation points.
- Screw-range claims retain the source normalization and same-backend implementation risk stated in the source.

## Common misreadings

- `D(a,b)=0` is not a global RH certificate.
- “All zeros found are simple” is not enough unless total multiplicity is independently saturated.
- A corrected theorem does not verify the original false formula.
- A repaired computation does not make the original incomplete proof object valid.
- A useful model geometry is not an RH criterion until the complete theorem is proved.

## Next missing step

Apply these correction rules to every future integrated packet. In particular, Round 2 should challenge whether the Weil/screw and operator source packets have explicit endpoint, locality, coverage, and source-domain gates rather than prose assurances.
