# Long-source seed and the half-slope barrier

Status: proposed conditional adapter and counterexample; two independent agents checked the amplifier algebra and rank-one construction against the source interfaces. No formal replay has been performed. No zero-free theorem is claimed.

Source: PR93 of [QuasiRiemannTracker](https://github.com/GTimG/QuasiRiemannTracker/pull/93), head `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`; inspect `SelectedNormIteration.lean`, `UniformSlotAmplification.lean`, `SelectedContraction.lean`, `Contraction.lean` and `SelectedSlotData.lean` under `submissions/2026-10-28-joint-detector-fine-chain/src/Candidate/Local/Qrh/JointDetector`. Imported analytic inputs are not independently verified here.

## A conditional amplifier adapter

Fix `0<sigma<=1` and the squarefree selected family in the source's `SquarefreeLongNormBound`: literal bounded slot descriptors, one early slot mesh, coefficient-mass and total-width conditions, supported squarefree rows with the stated ray condition and norms in `[B,2B]`, and arbitrary ordinary source ideals of norms at most `L`. Assume a direct long-source bound with full source quantifier order

```
N(F,S) <= K Z^epsilon * (L + B^sigma L^(1-sigma))     (B <= L <= Z^P).
```

Here `N` is the squared norm of the selected matrix and the constant may depend on the fixed slot count, coefficient bound and width floor but not on the moving data or `Z`. Then the source's `uniform_slot_crossing` gives the all-source bound

```
N(F,S) << Z^epsilon' * (L + B^(1-sigma) L^sigma)
```

on the source's bounded polynomial ranges, for every prescribed `epsilon'>0` after choosing all auxiliary losses and the early mesh sufficiently small. The source states its existing `squarefree_family_long_to_all` with `sigma>=1/2`, but the algebra below and `uniform_slot_crossing` itself only use `0<sigma<=1`. This is a paper-level extension of the adapter, not a compiled Lean theorem.

For `L>=B`, the assumed bound is at most `2 K Z^epsilon L`. For `L<B`, set the crossing target `t=log(B/L)/log Z`. Since `1<=L<B<=Z^A`, `0<t<=A`. The source's amplifier produces a merged ordinary source set at scale `B<=Y<=B Z^(mesh+loss)` and bounds

```
N(F,S) <= C Z^loss N(F,S_merged)/(Y/L)^sigma.
```

With the long bound at `Y`, `B^sigma Y^(1-sigma)<=Y`, so the right side is at most a fixed constant times

```
Z^(loss+epsilon) * L^sigma Y^(1-sigma)
 <= Z^(loss+epsilon+(mesh+loss)(1-sigma)) B^(1-sigma) L^sigma.
```

Take the fixed polynomial source cap `P>=3A+1` and the fixed losses and early mesh small enough that the merged source scale is admitted; the original `uniform_slot_crossing` chooses its mesh before the later slot dictionary. This proves the conditional squarefree statement without using any contraction iteration. It does not automatically supply the analogous natural-row operator or the actual physical prime-slot estimate; their decomposition, retained masks, histogram and quantifiers must be transported separately.

The difficult region of the seed is `B<=L<=B^2`: the source's elementary initial bound is `O(Z^epsilon(L+B^2))`, so for `L>=B^2` the desired seed follows from its linear term. At `L=B` the desired bound is `O(Z^epsilon B)`. For `sigma=223/500` this is a concrete proposed source estimate that could feed the PR94 bottleneck analysis, but it has not been proved.

## The seed fails at small slopes in the broad source class

For any `0<sigma<=1/6`, the proposed squarefree long seed is false at `L=B`, even with all source quantifiers respected. Choose `B=Z` and a fixed positive slot width `w` below the supplied mesh with `w<1`; choose slot ideals `J^6` with `J` supported away from primes above `2,3` and `N(J)<=Z^(w/6)`. There are `>>Z^(w/6)` such ideals. Give them equal coefficients, normalized to have a sufficiently large fixed squared mass `Cslot`. Then every prime row selected below has squared slot value at least `Z^(w/6)>=Z^(sigma*w)`.

Choose prime ideals of norm in `[B,2B]` outside the fixed bad primes. Their primary generators have only finitely many residue classes modulo `36`, so by the prime ideal theorem and pigeonhole at least `>>B/log B` of them share one residue class. Let `F` be that squarefree prime-row family, so the source's ray hypothesis holds; the chosen class can vary with `Z` because the family is live data under the uniform estimate. Take the dual ordinary source set to be all ideals `K^6` with good `K` and `N(K)<=B^(1/6)`. It contains `>>B^(1/6)` ideals, all of norm at most `L=B`. Slot and dual ideals are supported away from bad primes. Their roots have norm much smaller than every row prime, so both are coprime to all rows. Sextic multiplicativity and the zero mask give

```
chi(pi,J^6) = chi(pi,K^6) = 1.
```

Thus the selected matrix is identically one, and its squared operator norm is `#F * #S >> B^(7/6)/log B`. The proposed long seed at `L=B` is only `O(Z^epsilon B)`, contradicted by any fixed `epsilon<1/6`. The coefficient and width constants stay fixed before `Z` tends to infinity. This refutes the stated broad arbitrary-ideal slot seed at these small slopes, but it does not refute the target `sigma=223/500` or a source theorem restricted to actual prime slots.

For cube rows and square slot/source ideals the analogous rank-one example gives at most `B^(1/3+1/2)=B^(5/6)` in the `L=B` scaling; it does not contradict the proposed `O(B)` seed at `sigma=223/500`. A proof of the latter remains a genuinely open arithmetic input.
