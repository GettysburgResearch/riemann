# A smooth-prime selected-row count via zero density

**Status:** Proposed source-dependent argument, not an improvement of the current detector count or a zero-free region. It uses the proof, not just the printed statement, of Xu–Sang's [Theorem 1.2 and §§6–7](https://arxiv.org/html/2610.17675v2), and the usual explicit formula for a smoothed Hecke prime sum. Independent review is requested, particularly for uniform height, deleted factors, and the exact physical-slot matching. No priority claim is made.

Fix a finite set S of Eisenstein primes containing those above 6 and a finite set Θ of finite-order ray characters supported on S. Let U≥2, `0<η≤A`, and `U^η≤P≤U^A`. For a fixed smooth compactly supported test V on the positive reals, define

    Q_u(P,t,ν)=P^(−1/2) Σ_{p∉S} ν(p) χ_p(u) V(Np/P) (Np/P)^(it),

where ν∈Θ, p ranges over prime ideals, u ranges over good primary sixth-power-free rows of norm at most U, and the sextic symbol carries its coprime zero extension. For every `0<σ<3/4` with `(1+σ)/2>51/100`, every ε>0, and some sufficiently small τ>0 depending on the fixed data and ε, the proposed bound is

    #{u: |Q_u(P,t,ν)|² ≥ P^σ}
       ≪ U^[R((1+σ)/2)+ε]                          (1)

uniformly for `|t|≤U^τ`, ν∈Θ, and P in the specified range, with

    R(a)=(31−32a)/(21−12a).

Finite fixed linear combinations of such sums are allowed, after choosing a smaller τ, provided their coefficient sizes and profiles are uniformly bounded. At `σ=223/500`, this gives `R(723/1000)=0.6381045115…`. The bound is weaker than the approximately 0.6094 existing count at the relevant PR94 corner. It does not apply to arbitrary bounded prime weights or moving arbitrary prime subsets, and therefore does not prove the broad PR93 selected-norm input or the physical-return bridge.

## Input on zeros

Xu–Sang §6.1 forms the family `ν(n)χ_n(u)^±1` for a finite group Θ containing the fixed twists, with primitive conductor `≪_S U` and deleted Euler factors supported on primes whose radical has norm `≪_S U`. Proposition 6.3 bounds the number of rows in each zero-location bin by `U^{R(a)+ε}` with a fixed polynomial height cost. In the proof of Theorem 1.2, §6.3 sets the detector height `H₁=U^τ`; the printed theorem states a polylogarithmic-height zero-density count, but the bin argument already counts *rows* with a zero at `Re ρ≥a` and `|Im ρ|≤U^τ`, for a sufficiently small τ chosen after the allowed loss. The finite family includes the twists and both orientations. Cumulative rows follow by the same dyadic summation and a trivial count at sufficiently small norm, with a smaller τ. This polynomial-height row-count extraction is an explicit source-dependent bridge to be independently checked; it is not attributed to the printed theorem verbatim.

Only finitely many sixth-power-free good rows can produce a principal primitive character after a fixed ν twist: Kummer valuation modulo six forces all good valuations to be bounded by fixed support, and there are finitely many unit and bad-prime classes. Remove these rows.

## Large prime response forces a zero

Write `a=(1+σ)/2`. Choose a fixed small `h>0` such that `a−h>51/100` and `2h<σ`. Suppose a row's primitive L-function for the twist has no zero in `Re s≥a−h` and `|Im s|≤2U^τ`. Its conductor is `≪U`. The smoothed explicit formula, after inserting the harmless `log(Np)` weight and compensating it in the uniformly smooth profile, gives

    Σ_p ν(p)χ_p(u)V(Np/P)(Np/P)^(it)
       ≪ P^(a−h) U^{O(τ)} (log U)^C + P^(1/2)(log U)^C
          + O(P U^(−Mτ)),

for any fixed M, with τ>0 sufficiently small and constants depending on the smooth test and the fixed arithmetic data. The sum over low zeros uses the standard `O((T+1) log(U(T+3)))` individual zero count; the high-zero tail uses rapid decay of the Mellin transform. Prime powers and the finitely many deleted Euler factors give the displayed square-root or logarithmic errors. Pick first h and then τ so small that the `U^{O(τ)}` factor is at most `P^{h/4}`, uniformly since `P≥U^η`; finally choose M large enough that the high-zero term is also `o(P^a)`. Since `a−1/2=σ/2`, the normalized prime response is then strictly smaller than `P^{σ/2}` for sufficiently large U. Consequently every selected row has a zero with `Re ρ≥a−h` and `|Im ρ|≤2U^τ`.

Apply the polynomial-height row-bin input at `a−h` and choose h small after ε. Continuity of R gives (1). A finite sum of fixed-twist profiles is handled by the triangle inequality and an arbitrarily small threshold loss. The proof allows norm twists of height at most U^τ because the Mellin transform is shifted by t; its truncation interval is enlarged by at most that amount. □

A physical application still requires demonstrating that its actual slot coefficients and windows decompose into a fixed number of the above smooth fixed-twist prime sums, with no unsupported arbitrary masks, and that its row decomposition meets the sixth-power-free and good-prime hypotheses. If the frequency allowance is chosen before a slot's positive length lower bound, its required order of choices must also be checked.
