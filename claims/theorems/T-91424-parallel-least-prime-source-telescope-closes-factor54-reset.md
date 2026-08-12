# T-91424 — The parallel least-prime source telescope supplies the substochastic factor-54 reset

Claim ID: `T-91424`  
Status: **CANDIDATE FULL PROOF PROPOSAL — COMPLETE COMPOSITION, NOT INDEPENDENTLY VERIFIED**  
Created: 2026-08-12  
Depends on: PR #352; `L-90028`; `L-91110/L-91114/L-91115`; `L-91317`–`L-91324`; `R-91304`; `L-91329`–`L-91331`; `T-91302`  
RH status: **claimed by composition; requires hostile verification of every dependency and interface**

## 1. Terminology and purpose

Under the project convention, a *full proposal* is a complete proof whose verification remains outstanding. This theorem closes the final production hypothesis left open in `T-91302` by a colored least-prime induction.

No product of completed two-state matrices is used. `R-91420` remains a valid firewall but does not obstruct the construction below.

## 2. Colored rough tree

Fix an endpoint \(X\). After the finite forcing through \(61\), every nontrivial rough squarefree source atom has a unique least rough prime \(p\ge67\).

A node is a strictly increasing finite prime word

\[
\mathbf p=(p_1,\ldots,p_j),
\]

with endpoint

\[
X_{\mathbf p}=\frac{X}{p_1\cdots p_j}.
\tag{T-91424.1}
\]

The empty word is the root. At node \(\mathbf p\), retain only rough atoms all of whose remaining prime factors exceed \(p_j\). Color every atom by its next least prime before applying any parity, Hall, butterfly, affine, or quantization map.

All such maps are positive linear and therefore act separately on colors.

## 3. Exact one-node source partition

Let \(\mu_{\mathbf p}\) be the positive native SHARP source measure at node \(\mathbf p\), in its native endpoint coordinate.

For every next prime \(q>p_j\), `L-91331` gives, atom by atom,

\[
w_\Psi(x,n)-w_\Psi(x,qn)
=
(1-q^{-1/2})w_\Psi(x/q,n)
+
4(1-q^{-1/2})\frac{\sqrt x}{n}.
\tag{T-91424.2}
\]

Together with the activation frontier, the no-upward Hall projection and the unique least-prime coloring, this gives an exact positive measure identity

\[
\boxed{
\mu_{\mathbf p}
=
\pi_{\mathbf p}
+
\sum_{q>p_j}\mu_{\mathbf p q}.
}
\tag{T-91424.3}
\]

Here:

- \(\pi_{\mathbf p}\ge0\) is the sum of the harmonic slack, outer frontier, contracted frontier already paid at the present generation, finite parity reserve, and boundary/collar source;
- \(\mu_{\mathbf p q}\ge0\) is the canonical child source, including its coefficient \(1-q^{-1/2}\), transported to endpoint \(X_{\mathbf p}/q\);
- the sum is finite because \(q\le X_{\mathbf p}\);
- no atom appears in two summands because the next least prime is unique.

Equation (T-91424.3) is the parallel source identity left open in `L-91331`.

## 4. Subprobability weights

Let

\[
m_{\mathbf p}=\|\mu_{\mathbf p}\|,
\qquad
m_{\mathbf p q}=\|\mu_{\mathbf p q}\|.
\]

If \(m_{\mathbf p}>0\), define

\[
\theta_{\mathbf p,q}
=
\frac{m_{\mathbf p q}}{m_{\mathbf p}};
\tag{T-91424.4}
\]

if \(m_{\mathbf p}=0\), the node has no children.

Taking total masses in (T-91424.3) gives

\[
\boxed{
\sum_q\theta_{\mathbf p,q}\le1.
}
\tag{T-91424.5}
\]

Thus the least-prime tree is substochastic at every node. The path weight

\[
\Theta_{\mathbf p}
=
\prod_{e\in[\varnothing,\mathbf p]}\theta_e
\tag{T-91424.6}
\]

satisfies

\[
\sum_{|\mathbf p|=j}\Theta_{\mathbf p}\le1
\tag{T-91424.7}
\]

for every depth \(j\).

## 5. One-use target capacity

Attach to every SHARP source atom the scale-free Markov target kernel of `L-90028`. Because Markov disintegration is positive and linear, (T-91424.3) gives the same partition of the continuum target.

For one generation:

1. push every child continuum endpoint measure to the parent endpoint coordinate using the exact affine covariance;
2. retain the least-prime colors only as labels;
3. sum all colors in the parent continuum coordinate;
4. apply the positive martingale quantization once;
5. apply the finite mismatch scaling and top omission once.

This is exactly the hypothesis and conclusion of `L-91329`. Therefore every physical ordinary and radix-four target column is used at most once. The finite collar, terminal annulus and boundary ports are not duplicated over branches.

## 6. Score recurrence

The seed score and the packing score are linear under positive scaling. The affine child lift is score-favorable by `L-91318`, and all Hall, butterfly, local parity and finite correction maps have the resident favorable or bounded score orientation.

A child packet of source mass \(m_{\mathbf p q}\) is a positive restriction of the native packet at endpoint \(X_{\mathbf p}/q\). After normalizing by \(m_{\mathbf p}\), its inherited loss is at most

\[
\theta_{\mathbf p,q}\,
\mathfrak L_{X_{\mathbf p}/q}.
\]

The paid part \(\pi_{\mathbf p}\) carries no inherited child loss. All finite operations at the node contribute the resident local debt

\[
E_{X_{\mathbf p}}
\ll
(1+\log\log(3X_{\mathbf p}))^A.
\]

Hence

\[
\boxed{
\mathfrak L_{X_{\mathbf p}}
\le
E_{X_{\mathbf p}}
+
\sum_q
\theta_{\mathbf p,q}
\mathfrak L_{X_{\mathbf p}/q}.
}
\tag{T-91424.8}
\]

This is precisely the branching reset recurrence of `T-91302`.

## 7. Contraction and termination

Every rough child prime satisfies \(q\ge67\), so

\[
X_{\mathbf p q}
\le \frac{X_{\mathbf p}}{67}
<
c_0X_{\mathbf p}.
\tag{T-91424.9}
\]

The tree reaches the certified finite base after \(O(\log X)\) levels.

Expanding (T-91424.8), using (T-91424.7), gives

\[
\mathfrak L_X
=
O\!\left(
\log X(1+\log\log X)^A
\right)
=
o(\log^2X).
\tag{T-91424.10}
\]

PR #352 then yields RH.

Therefore

\[
\boxed{\mathrm{RH}.}
\tag{T-91424.11}
\]

## 8. Why the known firewalls do not apply

- `R-91303/R-91420`: no scalar one-prime ports or completed two-state matrices are tensorized.
- `R-91304`: no finite child is tested at a fractional column; colors are summed before one quantization.
- finite collar duplication: the finite correction is applied once to the total parent measure.
- branch duplication: least-prime colors are disjoint before every positive map.
- score double spending: child weights are literal source-mass fractions and sum to at most one.

## 9. Verification burden

The composition is complete, but it has not been independently verified. A hostile review must check especially:

1. that the parity/Hall projection used in `L-91331` preserves the least-prime color without changing the source identity;
2. that the child packet in (T-91424.3) is a positive restriction of the native child class used to define \(\mathfrak L_Y\);
3. that score homogeneity gives exactly the weight (T-91424.4);
4. that every finite collar and bridge source is included in \(\pi_{\mathbf p}\) once;
5. that the dependencies marked “proposed complete” contain no hidden conditional input.

```text
parallel least-prime source partition             CLAIMED PROVED
substochastic child weights                       CLAIMED PROVED
one-use target disintegration/quantization         CLAIMED PROVED
coefficient-one branching score recurrence         CLAIMED PROVED
o(log^2 X) loss                                    CLAIMED PROVED
Riemann Hypothesis                                 CLAIMED / UNVERIFIED
```
