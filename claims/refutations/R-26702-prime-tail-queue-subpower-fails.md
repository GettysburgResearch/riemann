# R-26702 — Prime-only queue transport cannot have subpower boundary charge

Claim ID: `R-26702`  
Title: The first prime-density correction forces a positive `sqrt(X)/log^2(X)` exterior queue  
Status: **PROPOSED REFUTATION IMPORT / PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Primary source: PR #274 `R-27302` at `c2e1a978a0156944c26132943fa41bcf7c838fec`  
Scope: refutes only the subpower rate for transports whose endpoints are ordinary primes

## 1. Frozen target

For the parabolic ordinary-prime residual

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p),
\]

the terminal queue of `L-26704` is

\[
\mathcal Q_X
=
\max_{P\le X}
\left(\sum_{P\le p\le X}r_X(p)\right)_+.
\]

The former `PTQ` proposal asserted `mathcal Q_X=X^{o(1)}`.

## 2. Continuum defect and its logarithmic moment

Let

\[
E(\theta)
=
\sum_{k\le1/\theta}g(k\theta)
-
\theta^{-1/2}\log(1/\theta)
\]

be the continuum parabolic residual. Its Mellin transform is

\[
\mathcal M_E(s)
=
\frac4{(2s-1)^2}
\left[\frac{(s-1)\zeta(s)}s-1\right].
\]

Expanding at `s=1` gives

\[
\int_0^1E(\theta)d\theta=0,
\qquad
\int_0^1E(\theta)\log\theta\,d\theta=4(\gamma-1).
\]

Thus

\[
-\int_0^1E(\theta)\log\theta\,d\theta=4(1-\gamma)>0.
\]

## 3. Prime sampling

The uniform finite-difference comparison proposed in `R-27302` is

\[
r_X(p)
=
X^{-1/2}E(p/X)
+O\!\left(\frac{1+\log(X/p)}{p^{3/2}}\right),
\]

with total error `O(log X)` after summing over primes.

Prime-number-theorem partial summation, with a moving low cutoff and the integrability of `E(\theta)(\log\theta)^2`, yields

\[
\sum_{p\le X}E(p/X)
=
\left(4(1-\gamma)+o(1)\right)
\frac{X}{\log^2X}.
\]

Consequently

\[
\boxed{
\sum_{p\le X}r_X(p)
=
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}>0.
}
\]

## 4. Queue lower bound

The full suffix is admissible in the queue maximum, so

\[
\boxed{
\mathcal Q_X
\ge
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
}
\]

Hence the prime-only subpower queue theorem is false if the two analytic passages above withstand review.

## 5. Hypothesis match

The refutation applies to:

```text
nonnegative interval transports
whose source and sink endpoints are ordinary primes
and whose unmatched mass is exported through one exterior prime.
```

It does not apply to:

```text
squarefree composite collectors;
proper-power-neutral incidence compression;
dyadic opposite-parity source recombination;
physical parity/factor-five transition certificates;
signed generation-netted Möbius packets.
```

Prime-to-prime blocks conserve total ordinary-prime incidence. Composite squarefree sources can reduce it because one endpoint can contain several distinct prime factors.

## 6. Reviewer checklist

1. Verify the finite-difference error uniformly down to the moving prime cutoff.
2. Verify the Mellin transform and Laurent expansion at `s=1`.
3. Verify the PNT partial-summation error is `o(X/log^2X)`.
4. Verify the omitted low-ratio range has the same smaller order.
5. Keep the exact finite queue/min-cut theorem separate from the false subpower rate.

## 7. Verdict

```text
finite prime queue algebra       retained
subpower PTQ                     proposed refuted
full RH conclusion from PTQ      unavailable
RH                               unproved
```
