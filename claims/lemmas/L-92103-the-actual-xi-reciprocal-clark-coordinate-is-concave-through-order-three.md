# L-92103 — The actual-Xi reciprocal Clark coordinate is concave through order three

Claim ID: `L-92103`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91905`; `L-92100`--`L-92102`; centered Xi Hadamard grouping  
RH status: **unproved**

## 1. The grouped Xi logarithmic derivative

Put

\[
 \Xi(z)=\xi\left(\frac12+z\right),
 \qquad
 F(x)=\frac{\Xi'(x)}{\Xi(x)},
 \qquad
 p(t)=\frac{F(\sqrt t)}{\sqrt t}.
 \tag{L-92103.1}

The centered even Hadamard product, grouped by the symmetries

\[
 \lambda\mapsto-\lambda,
 \qquad
 \lambda\mapsto\overline\lambda,
\]

gives the locally `C^2`-convergent decomposition on `t>1/4`

\[
\boxed{
 p(t)
 =\sum_{\gamma\in\mathcal Z_0}
   \frac{2m_\gamma}{t+\gamma^2}
 +\sum_{\alpha\in\mathcal Z_{\rm off}}
   \frac{4m_\alpha(t+c_\alpha)}
        {(t+c_\alpha)^2+B_\alpha^2},
}
\tag{L-92103.2}

where

\[
 c_\alpha=b_\alpha^2-a_\alpha^2,
 \qquad
 B_\alpha=2a_\alpha b_\alpha.
\]

The first sum runs over critical-line orbits; the second over one representative
of every off-line quadruple.

## 2. Reserve decomposition

Choose the verified critical orbit `R_0` and fractions from `L-92102`:

\[
 R_0(t)=\frac2{t+r_0},
 \qquad
 R_0=\epsilon_0R_0+\sum_\alpha\epsilon_\alpha R_0,
 \qquad
 \epsilon_0>0.
 \tag{L-92103.3}

For each off-line orbit define

\[
 f_\alpha(t)
 =\frac{4m_\alpha(t+c_\alpha)}
        {(t+c_\alpha)^2+B_\alpha^2}
  +\epsilon_\alpha R_0(t).
 \tag{L-92103.4}

`L-92101` gives

\[
 \boxed{
 \mathcal E[f_\alpha]\ge0,
 \qquad
 \mathcal E[f]=ff''-2(f')^2.
 }
 \tag{L-92103.5}

The leftover reserve block satisfies

\[
 \mathcal E[\epsilon_0R_0]=0.
 \tag{L-92103.6}

Every other critical-line orbit

\[
 g_\gamma(t)=\frac{2m_\gamma}{t+\gamma^2}
\]

also satisfies

\[
 \mathcal E[g_\gamma]=0.
 \tag{L-92103.7}

## 3. Finite partial sums

Regroup (L-92103.2) as

\[
\boxed{
 p
 =\epsilon_0R_0
 +\sum_{\gamma\ne\gamma_0}g_\gamma
 +\sum_\alpha f_\alpha.
}
\tag{L-92103.8}

Every term is positive and has concave reciprocal.  By the parallel-sum
closure theorem `L-92100`, every finite partial sum `p_N` satisfies

\[
 \mathcal E[p_N]\ge0.
 \tag{L-92103.9}

## 4. Passage to the full zero set

The grouped zero count gives, uniformly on compact subsets of `t>1/4`,

```text
critical orbit:
    g=O(m/gamma^2),
    g'=O(m/gamma^4),
    g''=O(m/gamma^6);

off-line orbit:
    q=O(m/b^2),
    q'=O(m/b^4),
    q''=O(m/b^6);

allocated reserve share:
    epsilon_alpha R_0^(k)=O(m_alpha/b_alpha^2)
    for k=0,1,2.
```

The Riemann--von Mangoldt count makes all three derivative series locally
uniformly convergent.  Hence

\[
 p_N\longrightarrow p
 \quad\text{in }C^2_{\rm loc}(1/4,\infty).
\]

Passing to the limit in (L-92103.9) gives

\[
 \boxed{
 p(t)p''(t)-2p'(t)^2\ge0
 \qquad(t>1/4).
 }
 \tag{L-92103.10}

Equivalently,

\[
 \boxed{
 \left(\frac1{p(t)}\right)''\le0
 \qquad(t>1/4).
 }
 \tag{L-92103.11}

Thus the actual-Xi reciprocal Clark coordinate is concave on the complete safe
axis, without assuming RH.

## 5. Original-variable form

By `L-92002`, (L-92103.10) is exactly

\[
\boxed{
 x^2F(x)F''(x)
 -2x^2F'(x)^2
 +xF(x)F'(x)
 +F(x)^2
 \ge0
 \qquad(x>1/2).
}
\tag{L-92103.12}

This closes the compact sign left open on PR #445, subject to review of the
reserve allocation and the centered Hadamard passage.

## 6. What made the proof possible

A single hypothetical off-line orbit has the wrong reciprocal curvature.
The key new input is that rigorous verification supplies a real critical-line
reserve below every possible off-line ordinate.  The defect of an orbit at
height `b` costs only `O(m/b^2)` of that reserve, while

\[
 \sum_{\gamma>H_*}\frac{m_\rho}{\gamma^2}
\]

is tiny.  One low critical orbit therefore absorbs the complete hypothetical
off-line curvature budget with coefficient one.

No cancellation between unverified floating-point approximations is used.
The argument is structural after importing the rigorous verified-height
statement.

## 7. Review joints

1. the exact cross-curvature formula of `L-92101`;
2. the uniform `9m/b^2` allocation bound;
3. the reciprocal-square zero-tail estimate;
4. selection of one reserve orbit below `H_*/2`;
5. the centered Hadamard grouping and locally `C^2` passage;
6. multiplicity bookkeeping for each symmetry orbit.

## 8. Exact boundary

```text
parallel-sum closure                          EXACT
one-orbit reserve absorption                  EXACT
complete reserve budget <1                    PROPOSED COMPLETE
actual-Xi reciprocal concavity                PROPOSED COMPLETE
all actual-Xi three-node matrices             T-92100
higher interpolation orders                   OPEN
Riemann Hypothesis                            UNPROVED
```
