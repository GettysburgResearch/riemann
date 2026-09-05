# Pass 4: completion attempt, uniform prime-tail law, and the failure of naive truncation

**RH IS NOT PROVED.** This pass does not claim completion of the user's RH target.
Status: proposed complete proofs of the component statements below, with exact finite controls and a bounded actual-source interval certificate. Independent mathematical review is required.
Parent: PR #793 at bfb66e07f7e38306dbcb916911332a591efce917.
Scope: all three routes remain active; no predecessor file or canonical claim is changed.

The attack was to construct the final positive object directly from the convergent arithmetic source. It encountered a real obstruction, not simply an uncomputed larger matrix: finite arithmetic truncation changes the relevant sign structure. This packet proves that obstruction, repairs the artificial pole, and quantifies the omitted tail uniformly in degree. It does NOT prove positivity after the repair.

## Strongest new estimate: every degree, one PNT error

At the s=2 invariant center let m_n be the full xi log moments, and m_n(X) the same gamma-plus-prime expression with all prime powers through X retained. There is an explicit compound-Poisson cumulative distribution C_n(y) such that

    |2^(n+1)(m_n(X)-m_n)-C_n(log X)| <=5 eps_X,
    eps_X=sup_(v>=X)|psi_C(v)-v|/v,

for EVERY n>=0. This is an unconditional all-degree estimate. Classical PNT makes eps_X tend to zero. The distribution is an exact representation of a continuous comparison kernel, not a random-primes assumption.

Its mean is 2y+2 and variance 10y+22. Hence

    2^(n+1)m_n(X) -> Phi(z),
    n=floor(2log X+z sqrt(10log X)).

The complete proof is in PRIME_TAIL_TRANSITION.md. This is the transition of the artificial pole left by finite truncation, not a zero-density theorem.

## Route 1: a forced negative square and an exact repair

Every finite prime cutoff has a sparse negative square B_n(t)=1-(2t)^n at some n=O(log X). An explicit conservative bound is supplied. For this family the asymptotic crossover occurs at n=2log X, with the Gaussian window above. By contrast, these same squares are positive for the ACTUAL full xi source at every n>=1; the proof uses a source-defined small disk plus two certified signs. No arbitrary-polynomial positivity is inferred.

The repair subtracts the exact continuum tail X^(1-s)/[(s-1)(2s-1)]. It cancels the artificial pole at u=-2 and preserves the uniform all-degree error. Its infinite Hankel matrix converges to the full one with trace-norm error at most 10eps_X. These are not necessarily positive approximants: the corrected X=2 trace is negative. The all-order sign is still open.

## Route 3: every finite prime-cutoff operator has infinite negative index

For the literal arithmetic Hardy kernel from #792/HL-1, keeping the full gamma series but finitely many primes, the operator has infinitely many negative eigenvalues. The proof is exact: remove a rank-two cosh term, and the remaining translation kernel has negative value at zero and decays at infinity. Widely separated bumps produce arbitrarily large negative subspaces.

This does NOT apply to exact finite-dimensional compressions of the FULL operator. Those and finite-prime truncations are different objects. The omitted actual prime tail cancels the deterministic exp(x/2)/2 mode by PNT, but that cancellation does not exclude smaller hypothetical exceptional modes. Read OPERATOR_CUTOFF_INDEX.md.

## Route 2: finite arithmetic cutoffs can falsely pass the endpoint

For any coefficients bounded by one, any finite Laguerre source cutoff obeys E_N^(X)<=4X(N+1). Every subexponential cutoff schedule consequently passes the subexponential upper-growth test, even for the known positive squarefree countercontrol whose INFINITE coefficients grow like 2delta_67(-3)^n. Its omitted tail contains asymptotically the entire bad signal. Read MOBIUS_FALSE_CONVERGENCE.md.

Thus truncation creates false negativity in the moment/operator construction and false apparent success in the reciprocal-energy construction. The general RH criteria remain intact; the invalid operations are the unproved exchanges of arithmetic cutoff and unbounded test order.

## What was run

331 distinct exact rational/interval controls, including eight actual-source interval signs, pass in normal and optimized Python. Eight unit/rejection tests pass in each mode. Four additional corrupted saved-result files are rejected in each mode. RESULTS.json is reconstructed, not trusted by its status flag. Two parent source implementations are authenticated by literal SHA-256 before execution. The broader predecessor suites were not rerun.

No zero census, broad prime scan, floating-point acceptance, Lean build, independent referee acceptance, or RH proof is claimed. The PNT, Gaussian-limit and infinite-index arguments are mathematical proofs to review, not machine proofs supplied by the finite checker.

Replay from this directory, with the unchanged pass2 and pass3 siblings present:

    python verify.py --check RESULTS.json --manifest
    python -O verify.py --check RESULTS.json --manifest
    python verify.py --self-test
    python -O verify.py --self-test

## Exact unfinished step

The full-source Hankel PSD, full signed Mobius-energy bound, and full Hardy arithmetic positivity remain unproved. The continuum correction and convergence estimates do not supply those signs. This pass is a completed analysis of a failed closure mechanism plus a new uniform tail theorem, not an end-to-end RH completion.
