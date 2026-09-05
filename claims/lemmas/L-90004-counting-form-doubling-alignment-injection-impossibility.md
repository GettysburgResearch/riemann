# L-90004 — Counting form of the GFEP source, the exact doubling alignment, and injection impossibility

Claim ID: `L-90004` (provisional range; allocate at registry)
Status: **IDENTITIES PROVED (exact rational verification); INJECTION IMPOSSIBILITY PROVED (finite witnesses, independently re-verified); within-row convexity PROVED — net verdict WALL_RENAMED; no RH claim**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, final dispatch Prong G2 + adversarial review
Date: 2026-08-09
Companions: `T-90006` (flow/cut duality), `T-90007` (cut classification + constraint-relative refutation)
Scope: exact combinatorial structure of the GFEP functional; two proved impossibility results

## 1. Counting theorem (proved)

\(U_X\) is the unique divisor-lattice primitive of \(w_X\): \(\sum_{k\le X/m}U_X(mk)=w_X(m)\) for every \(m\le X\); equivalently \(U_X(m)=\sum_{m\mid j,\ j/m\ \text{squarefree}}\mu(j/m)\,w_X(j)\) — a \(w\)-weighted Möbius-signed count of squarefree chains \(m\to j\). Moment identities: \(\langle U,\mathbf1\rangle=\log X\); \(\langle U,\log\rangle=\sum_{q\le X}\Lambda(q)w_X(q)\) (the chain map's prime ramp **is** \(U\)'s log-moment — the LP duality pairing in counting coordinates); \(\langle U,\mathrm{Id}\rangle=\sum_q\varphi(q)w_X(q)\). (Verified to 1e-48/1e-50.)

## 2. Path-count normal form (proved)

\(E_n(m,p)=(p/m)\,W_n(m,p)\) with \(W_n(m,p)=\sum_{\text{first-entrance paths }m\to p}(1/2)^{\mathrm{length}}\) over the deterministic 4-edge digraph \(m\to\{\lfloor m/2\rfloor,\lceil m/2\rceil,\lceil m/3\rceil,\lfloor2m/3\rfloor\}\) (with multiplicity); \(G:=pW=mE\) obeys the plain child-average recursion. Hence
\[
\mathrm{GFEP}(p)\iff\sum_{(m,k):\,k\ \text{squarefree},\,mk\le X,\,m\ge n}\mu(k)\,w(mk)\,dW(m)\ \ge\ 0 .
\]
Detached-band decomposition valid for all band \(p\) (fixing the \(p=2n-1\) edge case): \(\Sigma(p)=pR_X(p)+\sum_{m\ge2n}U_X(m)\,dG'(m)\), \(dG'(2n):=G(2n)\). (Exact rational verification, zero violations.)

## 3. The exact doubling alignment (proved — the hunted identity exists)

\[
\boxed{\,W(2m,p)=W(m,p)+\tfrac12\bigl[W(\lceil2m/3\rceil,p)+W(\lfloor4m/3\rfloor,p)\bigr]\quad(m\ge n)\,}
\]
— both binary edges of the even node \(2m\) land on \(m\), so the path family of \(2m\) contains a full copy of that of \(m\) plus a nonnegative ternary excess: **network doubling exactly mirrors arithmetic doubling** \(\mu(2j)=-\mu(j)\). The exact 2-adic fold identity converts the Möbius sign flip into the transport difference \(dW(2m)-dW(m)\) (verified to 1e-50). But the fold kernels are **not sign-definite** (both signs occur in \(dW\) above \(2n\) and in \(dW(2m)-dW(m)\); measured).

## 4. Within-row convexity (proved) — the exact boundary of the injective method

\(D_j(m):=w(mj)-w((m{+}1)j)\) satisfies \(D_j(m)>D_{2j}(m)\) whenever \((2m{+}2)j\le X\) (one-line calculus), so in the within-row 2-adic pairing the dominance direction equals \(\mu(j)\) itself: **the within-row injection proves row-source positivity exactly on the \(C_N>0\) cells (\(m>X/5\), the L-28002 region) — and provably nothing below.** The injective method's reach coincides exactly with the previously-known deterministic frontier.

## 5. Injection impossibility (proved, finite witnesses; weight convention pinned)

**Convention (required):** chains are weighted by the full object weight \(|dW(m)|\,w(mk)\) — *not* by \(w(mk)\) alone (under the bare-\(w\) reading the second mechanism fails; the review first refuted and then confirmed it under this convention).

No weight-dominant injection from negative chains \(B\) to positive chains \(A\) exists in either canonical object algebra (dG-form or R-form), at any structural level (free, node-fiber, row-fiber). Two independent kill mechanisms, each with exact witnesses spanning \(X=100..1000\), \(n/X\) from 0.5 down to 0.013:
1. **Cardinality pigeonhole:** deep in the open sector \(\#B>\#A\) outright — e.g. \((X,n,p)=(1000,23,30)\): 545 vs 522; \((29,40)\): 372 vs 362; \((50,70)\): 175 vs 159; \((100,13,13)\): 30 vs 25. No injection of any kind exists.
2. **Rank-2 pigeonhole:** \(B\)'s two largest chains are the exit-dipole shadows \((p{+}1,k{=}1)\) and \((p,k{=}2)\) with weights \(w(p{+}1)>w(2p)\), while the only \(A\)-chain of weight \(\ge w(2p)\) is \((p,k{=}1)\) (the second-largest, \((p{+}1,k{=}2)=w(2p{+}2)<w(2p)\) exactly): two pigeons, one hole.

The per-chain margins tend to 1 (razor's edge): the obstruction is tight, matching T-90005 §3's magnitude-hardness and T-90007 §3's constraint-relative refutation — a sign-pattern-only injection would contradict the stored finite certificate \(\min_p\Sigma^\varepsilon=-0.4712\).

## 6. Net

The bijective/injective lane — the last unfenced proof-shape — is now closed with exact witnesses precisely at the known deterministic frontier, while the exact identities (§§1–3) give the GFEP functional its final combinatorial coordinates: **a Möbius-signed, transport-weighted chain count whose positivity at every exit is the wall.** Artifacts: `experiments/X-90007-gambit-artifacts/` (G2 exact-rational scripts + the reviewer's `rev_g2.py`, `rev_final.py`); journal `wf_81bc35a7-548`.
