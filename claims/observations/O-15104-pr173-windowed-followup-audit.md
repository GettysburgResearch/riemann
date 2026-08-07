# O-15104 — Audit of PR #173's hard-window follow-up computation

Claim ID: `O-15104`  
Status: **AUDIT; USEFUL EMPIRICAL CORRECTION, COFINAL CLAIM UNPROVED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Scope: the three follow-up commits on PR #173 after the initial audit  
Related counterexample candidates: none

## 1. What the new computation fixes

The initial PR #173 census used the surrogate coefficients

\[
 p_j^{\rm full}=(-1)^j\Xi(2\pi\alpha j)
\]

instead of the windowed coefficients defined in its own analytic claim.

The new scripts

```text
experiments/X-16002-cvs-sampled-target-census/twotargets.py
experiments/X-16002-cvs-sampled-target-census/windowed_small.py
```

now evaluate

\[
 p_j^{\rm win}
 =(-1)^j\,2\int_0^{1/(2\alpha)}
 \Phi(t)\cos(2\pi\alpha jt)\,dt,
 \tag{O-15104.1}
\]

where the displayed `Phi` is the `Xi`-normalized logarithmic radical `4K`.

This is the correct coefficient formula for the **hard-window** target associated with the stated interval and scaling.

The follow-up finds, in particular, opposite verdicts at

\[
 (\alpha,N)=(1,6):
\]

```text
sampled-Xi surrogate: deficit 4
hard-window target:   deficit 0.
```

This is important evidence. It confirms that replacing the windowed coefficient by a full transform sample is not a harmless approximation for the finite gate.

## 2. What the new computation does not prove

The scripts use:

- ordinary `mpmath` quadrature at 60 decimal digits;
- a finite `n<40` kernel sum with a heuristic relative stopping condition;
- decimal rationalization at 45 or 50 digits;
- exact Sturm arithmetic only after those ordinary numerical steps.

No directed quadrature enclosure, analytic kernel-series tail, or coefficient-to-inertia moat is supplied. Hence the exact Sturm counts certify the resulting decimal-rational surrogate, not the exact hard-window coefficients.

The computed range is

\[
 0.5\le\alpha\le1.1,
 \qquad
 N\in\{6,8,10\}.
\]

It shows the empirical table

```text
alpha=1.1,1.0: pass
alpha=0.9,0.8,0.7: deficit 4
alpha=0.6: deficit 8
```

at those levels. It does **not** prove:

1. a sharp hard-window threshold;
2. threshold independence from `N`;
3. persistence along every growing schedule `N(alpha)` as `alpha->0`;
4. incompatibility of the two cofinal hypotheses.

The last inference had previously relied on the false converse to gap parity. The exact counterexample in `R-15103` shows that empty low-frequency node gaps do not force nonreal numerator roots.

## 3. Hard window versus production smooth cutoff

`L-15101` uses a smooth cutoff to remain in the declared form core. The new scripts use the discontinuous indicator of

\[
 |t|\le1/(2\alpha).
\]

The hard-window experiment is a valuable nearby model, but it is not automatically the production repaired target. A proof-level transfer requires either:

- direct evaluation of the actual smooth-cutoff coefficients; or
- a directed coefficient perturbation bound and the kernel-pinned inertia moat of `L-15113`.

## 4. Corrections in the new erratum that should be retained

The updated `R-16001` now correctly acknowledges:

1. the original census used the wrong vector;
2. the numerical constant `alpha_c about 1.0644` belongs only to the sampled surrogate;
3. arbitrary special completion and the fixed arithmetic scalar line are different readings;
4. the fixed arithmetic scalar gate remains open.

These are substantial and welcome corrections.

## 5. Remaining contradiction in the erratum

The erratum says `L-16003(iv)` remains correct and that no roots occur on the outer rays. This is false. The exact target

\[
 \lambda=(-1,0,1),
 \qquad
 p=(-1,3,-1),
 \qquad
 P(s)=s^2-3
\]

has both roots on the outer rays. Gap parity parts (i)--(iii) survive; the claimed exact distribution in part (iv) does not.

The new empirical example with many empty sign-change gaps and all roots real is itself further evidence that the local sign pattern is only a lower-bound mechanism, not a complete root census.

## 6. Correct current status

The follow-up computation upgrades the audit as follows:

```text
sampled-Xi scale obstruction:
    empirical surrogate result, not a production theorem

hard-window small-level failures:
    useful ordinary high-precision evidence

cofinal hard/smooth-window incompatibility:
    open

fixed arithmetic scalar completion:
    open and not decided by either root census
```

No new GitHub Actions or directed result is attached to the PR head at this audit point.

## 7. Next proof step

Use Issue #176:

1. produce directed coefficients of the actual smooth target;
2. transfer canonical inertia using `L-15113`;
3. separately evaluate the arithmetic residue line / `L-15109` thresholds;
4. retain a finite ladder only as evidence until one cofinal theorem is proved.