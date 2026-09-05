# O-90001 — SHARP hinge positivity: certificates to T = 10^8, exact terminal coefficient, fixed-row recurrence

Claim ID: `O-90001` (provisional range; allocate at registry)
Status: **OBSERVATION + ONE EXACT LEMMA — extends the evidence base of `SHARP` (T-32301); no cofinal claim**
Authoring agent: `claude-fable-5` session `riemann-proof-review-8nz34i`
Date: 2026-08-08
Extends: `T-32301` (branch `agent/gpt56-sol/323-halfpower-dual-superposition`), `L-32701` (branch `research/gpt56-pro-extra-high-shakeup-hinge-jordan`)
Scope: finite computation (discovery evidence only) plus one exact elementary lemma

## 1. Lemma (exact, proved): the terminal coefficient is universally positive

For the hinge system \(h_T(q)=q^{-1/2}-T^{-1/2}\) (\(2\le q\le T\)) solved against the average-carry matrix \(\beta_{nq}=\lfloor n/q\rfloor(q-1-(n\bmod q))/(n+1)\) via \(B_T^{\mathsf T}c_T=h_T\):

\[
c_T(T)=0
\quad\text{and}\quad
\boxed{\,c_T(T-1)=\frac{T}{T-2}\Bigl(\frac1{\sqrt{T-1}}-\frac1{\sqrt T}\Bigr)=\tfrac12T^{-3/2}(1+O(1/T))>0\ \ (T\ge4).\,}
\]

*Proof.* The last two equations of the back-substitution: at \(q=T\), \(h_T(T)=0=c_T(T)\beta_{TT}\) with \(\beta_{TT}=(T-1)/(T+1)>0\), so \(c_T(T)=0\). At \(q=T-1\), \(h_T(T-1)=c_T(T-1)\beta_{T-1,T-1}+c_T(T)\beta_{T,T-1}=c_T(T-1)\,(T-2)/T\). ∎

Empirically (§2) this terminal coefficient is the **global minimum** of the vector at every computed \(T\); the lemma shows the binding coefficient can never produce a counterexample to `SHARP`.

## 2. Computation (discovery evidence, not proof)

Implementation validated by: exact Fraction back-substitution == the L-32701.4 closed inverse-row formula == the L-32701.5–7 Dirichlet-kernel form on random rational targets; bit-exact reproduction of all five retained X-32301 certificate numerators (T = 100…10^6). Orientation fixed: the system is \(B^{\mathsf T}c=h\).

- **Full vectors:** every \(T\in[3,\,2\times10^4]\), plus 38 log-spaced endpoints up to \(T=10^8\): **zero negative coefficients anywhere**.
- **Fixed rows** \(j=2..64\), **every** endpoint \(T\in[j+1,10^8]\) (prior art: rows 2–3 to 10^7): zero sign changes; each row's minimum over \(T\) is at its first endpoint \(T=j+1\) and the row then climbs to a positive plateau matching the independent Dirichlet-series limits \(E_j(1/2)/(j(j-1)\zeta(1/2))+2/(j(j-1))\) (rows 2..5: 1.112, 0.406, 0.220, 0.141).
- **Envelope structure:** \(c_T(n)\,n^{3/2}\in[0.31,0.40]\) across five decades at \(T=10^6\); interior minimum \(\approx0.36\,n^{-3/2}\) near \(n\sim0.1\sqrt T\).
- **Row-2/3 margins** (jointly RH-implying by L-32701.18): means 1.11 / 0.41, Möbius-driven fluctuation amplitude only ~0.015 through \(T=10^8\).

## 3. New tool: fixed-row recurrence

For fixed \(j\), with \(S(x)=\sum_{k\le x}\mu(k)/\sqrt k\), \(M=\) Mertens, \(u_d=d^{-1/2}S(\lfloor T/d\rfloor)-T^{-1/2}M(\lfloor T/d\rfloor)\):
\[
c_T(j)=\frac{-2\sum_{d\le j-1}u_d+(j+2)(j-1)u_j-j(j-1)u_{j+1}+2(1-T^{-1/2})}{j(j-1)},
\]
validated exactly against the direct solve. Every fixed row is computable for **all** \(T\) simultaneously from two cumulative Möbius arrays; this is what enabled the \(T\le10^8\) sweep and is the right instrument for pushing rows 2–3 to \(10^{10+}\) or for a future exceptional-scale hunt.

## 4. Interpretation and boundary

Row 2's explicit form is \(c_T(2)=1-T^{-1/2}-u_1+2u_2-u_3\): a constant margin 1 against a bounded-looking Möbius fluctuation. Consistent with L-32701's warning, this positivity **is** RH-bearing: proving eventual positivity of rows 2 and 3 means bounding a specific \(\{S(T/d)\}\) combination below 1 for all large \(T\) — an RH-strength Möbius statement. Nothing here proves `SHARP`, any row's eventual positivity, `WSTS`, or `RH`. Files: scratchpad `sqhinge_lib.py`, `sqhinge_scan.py`, `sqhinge_rows64.py`, `sqhinge_exact_witness.py` (directed-interval certifier, validated against the retained T=100 certificate), results `sqhinge_results/*.json`.
