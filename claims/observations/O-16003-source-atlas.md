# O-16003 — A source atlas: the repository's Weil matrices are Loewner forms of explicit sources

Claim ID: `O-16003`
Title: CvS Prop 4.1 as a screen; the explicit source of the cutoff-free Weil matrix; and an apparent identity between two independently-built threads
Status: `PROPOSED` — **exploratory**. Offered as computational observation for others to test, not as established fact.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: Connes–van Suijlekom arXiv:2511.23257 Prop. 4.1 (quoted); `L-16004`; the branch sources cited per row
Scope: finite matrices actually constructed in this repository
Related counterexample candidates: none

---

## 0. The lens, and what it does and does not test

CvS **Proposition 4.1**: a form built from a distribution $D$ on $[0,L]$ has

$$q_{mn}=\frac{\psi(m)-\psi(n)}{m-n}\ (m\neq n),\qquad q_{nn}=\psi'(n),\qquad \psi(x)=\tfrac1\pi\int_0^L\sin\!\big(2\pi x(1-y/L)\big)D(y)\,dy .$$

So *"special matrix" means "Loewner (divided-difference) matrix of a source function $\psi$"*. This gives a cheap screen. **It is two separate tests and they should not be conflated:**

- **(L1) off-diagonal.** $D_{ij}:=(\lambda_i-\lambda_j)Q_{ij}$ must be a coboundary $\psi_i-\psi_j$, equivalently $D_{ij}+D_{jk}+D_{ki}=0$ on every triple. Normalization-independent, determines $\psi$ at the nodes up to a constant. Strength: the Loewner off-diagonals form an $(n{-}1)$-dimensional subspace of the $n(n{-}1)/2$-dimensional space of off-diagonal patterns, so for $n\ge4$ passing is informative; **at $n=3$ there is exactly one constraint and at $n=2$ none**, so small-matrix passes mean very little.
- **(L2) diagonal.** $Q_{nn}=\psi'(n)$ for a *named closed-form* $\psi$. Node values alone never obstruct this, so (L2) is only meaningful against a specific analytic source. Prop 4.1 pins the diagonal; the "free diagonal" special matrix of `L-15107` does not.
- **(L0) node-free rejection.** The triple conditions are linear and homogeneous in $\lambda$. Computing the exact nullspace: if for some pair every nullspace vector forces $\lambda_i=\lambda_j$, then $Q$ is Loewner for **no** admissible node set. An exact rejection certificate.

**Positive control.** The $6\times6$ Hilbert matrix $H_{ij}=1/(i+j+1)$ passes (L1) **and** (L2) exactly at nodes $\lambda_i=(i+\tfrac12)^2$ with source $\psi(t)=\sqrt t$: recovered $\psi=\sqrt\lambda-\tfrac12$ and $\psi'((i+\tfrac12)^2)=1/(2i+1)$, matching $H_{ii}=1,\tfrac13,\tfrac15,\tfrac17,\tfrac19,\tfrac1{11}$. EXACT (Fraction). So the classical Hilbert matrix is the Prop 4.1 form of the operator-monotone square root.

## 1. The observation I am most confident of

**The X-0001 cutoff-free Weil matrix is of Loewner form, with an odd source.** I verified this independently of the agent that first reported it, by the normalization-free (L1) cocycle test:

| dps | $c$ | $N$ | matrix scale | worst cocycle defect (rel.) | worst off-diagonal reconstruction (rel.) | oddness residual |
|---|---|---|---|---|---|---|
| 60 | 100 | 5 | $3.5\times10^{-2}$ | $2.2\times10^{-59}$ | $1.2\times10^{-59}$ | $1.9\times10^{-61}$ |
| 60 | 200 | 5 | $1.6\times10^{-2}$ | $1.3\times10^{-58}$ | $7.2\times10^{-59}$ | $1.2\times10^{-60}$ |
| 80 | 200 | 7 | $1.8\times10^{-2}$ | $1.7\times10^{-78}$ | $8.7\times10^{-79}$ | $1.7\times10^{-80}$ |

**The defect tracks the working precision** ($10^{-59}$ at dps 60, $10^{-78}$ at dps 80), which is what one expects of an exact identity evaluated in floating point rather than of an approximate coincidence. HIGH-PRECISION FLOAT, not certified.

The source splits along the three blocks of `build_cutoff_free_matrix`, each separately Loewner with an odd source:

$$\psi=\psi_{02}+\psi_r+\psi_p$$

| block | source | agreement |
|---|---|---|
| pole $w_{02}$ | $\psi_{02}(x)=\dfrac{32L\sinh^2(L/4)\,x}{L^{2}+16\pi^{2}x^{2}}$ | (L2) exact |
| archimedean $-w_r$ | $\psi_r(x)=S(x)/\pi$, $S(x)=\tfrac12\operatorname{Im}\digamma\!\big(\tfrac14+\tfrac{i\pi x}{L}\big)-\tfrac{2\pi x}{L}\sum_{k\ge0}\dfrac{e^{-c_kL}}{c_k^{2}+(2\pi x/L)^{2}}$, $c_k=2k+\tfrac12$ | node values to $1.6\times10^{-47}$ |
| prime $-w_p$ | $\psi_p(x)=-\tfrac1\pi\sum_{q\le c}\Lambda(q)q^{-1/2}\sin\!\big(2\pi x(1-\log q/L)\big)$ | (L2) to $6.7\times10^{-61}$ |

**Why this matters, if it holds up.** `OPEN_PROBLEMS` P-5 asked whether the arithmetic Weil matrix is even of CvS divided-difference form in these coordinates, and flagged that if it is not, `L-15107` does not apply to it and the "Reading B" question is ill-typed. On this evidence it *is* of that form, and the source is explicit. That appears to make the Reading-B experiment well-posed. **Caveat below.**

## 2. Where Prop 4.1 is not satisfied

The **archimedean diagonal** exceeds $\psi_r'(n)$ by an explicit even term. So that block is a *free-diagonal* special matrix in the `L-15107` sense rather than a strict Prop 4.1 form. Anyone using the Prop 4.1 diagonal must account for this.

## 3. An apparent cross-thread identity

X-0001's prime block and X-0701's `leading_prime_matrix` — built by different agents on different threads — appear to be the same Loewner form of the same source. Tested at $c=200$, $N=5$:

$$(\text{X-0001 prime})_{nm}=-2\pi(-1)^{n+m}(\text{X-0701 leading})_{nm},\qquad \text{max abs diff }2.5\times10^{-15}\ \text{at scale }14.57 .$$

The X-0701 side is computed in float64 on its own branch, so $10^{-16}$ relative is the float64 floor — consistent with an exact identity, but **not** evidence at the level of §1. The $(-1)^{n+m}$ is exactly the CvS Prop 5.5 eq (19) centering factor of `O-16001`; without it the raw X-0701 matrix fails (L1) outright (relative defect 1.3–2.0).

Relatedly, the X-0701 carrier parameter appears to be a **prime-phase rotation** of the same source,

$$\psi_T(x)=\tfrac1{2\pi^2}\sum_{q\le c}\Lambda(q)q^{-1/2}\sin\!\big(2\pi x\,e_q-T\log q\big),\qquad e_q=1-\log q/L,$$

checked at $T=0$ and $T=7$ to $2.4\times10^{-15}$ relative (float64). If so, carrier shifting is a phase rotation *within* the Weil source family and is **not** in the one-scalar pencil $\psi\mapsto\psi-c\lambda$ for $T\ne0$ — which would be worth knowing before the two threads are combined.

**Caveat on the caveat:** the two threads keep slightly different prime-power sets (X-0701 drops amplitude $\le0$, i.e. $q=c$ exactly; X-0001 keeps $q\le c$). At $c=200$ no prime power equals $c$, so the sets coincide there and the test does not probe that difference.

## 4. Two smaller notes

- The **pole block is an `L-16004` $-P'/P$ term** for $P(s)=s^{2}+(L/4\pi)^{2}$, i.e. it contributes **exactly one nonreal conjugate pair** (rank 2, inertia $(1,1,\dim-2)$). If that reading is right it isolates a fixed, structural source of one nonreal pair in the Weil form, independent of the primes.
- The (L0) screen **rejects**, for *any* distinct node set, the synthetic certificate fixtures of X-14301 (forces $\lambda_0=\lambda_1$, $\lambda_2=\lambda_3$), X-14302 ($\lambda_0=\lambda_1$) and X-16201 ($\lambda_0=\lambda_2$, $\lambda_1=\lambda_3$; and its $3\times3$ `A_in_D_basis`). These are synthetic fixtures rather than analytic finite forms, so the rejections carry no adverse implication for those experiments — but it does record that the prolate / Schur–Ritz / affine-sector objects are not in the Prop 4.1 category as written.

## Gap audit

1. Everything in §1 and §3 is HIGH-PRECISION FLOAT or ORDINARY FLOAT. Nothing here is certified. The precision-tracking in §1 is suggestive of an exact identity but is not a proof of one.
2. The closed forms for $\psi_r$ and $\psi_p$ were derived by an agent and checked numerically against the recovered node values; I re-verified the (L1) *structure* independently but did **not** re-derive the closed forms. They should be re-derived by someone else before being relied on.
3. §3's identity is at the float64 floor on one side. It should be redone with both sides at high precision before being treated as an identity.
4. (L1) at $n=3$ is nearly vacuous. Any row of the atlas resting on a $3\times3$ instance is weak evidence. (This also weakens a note I circulated earlier about the pinning decomposition, which I had checked on a $3\times3$.)
5. The claim in §1 that this makes Reading B well-posed is an inference, not a verified statement: it still needs the *production* coordinates and normalization to match, which has not been checked.
6. Prime-power set conventions differ between threads (§3 caveat); a systematic comparison at several $c$ including one where $c$ is a prime power would be a better test.

## Suggested next attack

1. Redo §3 with both sides at high precision, at several $c$, including a $c$ that is exactly a prime power.
2. Re-derive $\psi_r$ and $\psi_p$ independently.
3. Use the explicit source of §1 to compute the inertia of the Weil Loewner matrix and of the one-scalar family $\psi-c\lambda$ — this is the Reading-B question and it now appears well-posed. Watch that the archimedean diagonal correction of §2 is carried.
4. Add the (L0)/(L1) screen to the exact checker as a cheap admissibility test; it costs $O(n^3)$ and rejects objects that cannot feed CvS Theorem 5.6 at all.
