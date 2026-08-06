# Integration handoff — `r`-adic Haar continuation

Branch: `agent/gpt56-pro-09-n/202-haar-renormalization`  
Parent PR: #218  
Status: all new claims `PROPOSED`; RH not claimed

## New files

1. `T-20203` — every fixed integer dilation and every positive finite mixture
   has an RH-equivalent critical-mesh sign/subpower criterion.
2. `L-20202` — exact square-cutoff prime formula; negative prime support below
   `n^(2/(r+1))`; positive Lerch factorization.
3. `L-20203` — exact Chebyshev–Riesz identity; negative kernel support below
   `e^2 n^(2/(r+1))`.
4. `L-20204` — explicit Fejér–Gram portfolio of four-tap FIR vectors.
5. `R-20201` — off-center GGC positivity does not automatically continue to the
   central RH-equivalent measure.
6. `M-20202` — cofinal polygon/Selberg/Stieltjes attack.
7. `X-20202` — exact synthetic checker and eight tests.

## Review order

1. `claims/theorems/T-20203-critical-mesh-r-adic-screw-criterion.md`
2. `claims/lemmas/L-20202-exact-r-adic-square-cutoff-formula.md`
3. `claims/lemmas/L-20204-r-adic-fejer-gram-factorization.md`
4. `claims/lemmas/L-20203-r-adic-chebyshev-riesz-identity.md`
5. `claims/refutations/R-20201-offcenter-ggc-does-not-supply-central-haar-measure.md`
6. `experiments/X-20202-r-adic-screw/`
7. methodology and report

## Load-bearing audit targets

- factor `r/z^2` in the Laplace transform;
- multiplicity in the `r`-adic and positive-mixture residue balances;
- Landau continuation with the critical mesh `2 log(n)/r`;
- prime sign threshold `n^(2/(r+1))`;
- gamma and Lerch signs;
- factor `1/2` in the screw/Gram convention;
- Stieltjes integration-by-parts boundary at `x=1` and continuity at
  `x=n^(2/r)`.

## Merge relationship

This is a direct continuation of PR #218 and should remain stacked on the
square-screw normalization of PR #202 until both imported interfaces are
reviewed. It also has a nondependent conceptual connection to PR #219's
prime-polygon transport; a detailed comment was posted there.

## Exact remaining theorem

Prove for one fixed `r` or one fixed positive mixture

```text
(-H(n))_+ = n^o(1).
```

The new stack makes the adverse prime/Riesz support arbitrarily thin but does
not yet control the long positive-kernel block against the sign-changing
Chebyshev error.
