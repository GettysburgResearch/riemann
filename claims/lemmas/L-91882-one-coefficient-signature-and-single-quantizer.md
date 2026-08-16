# L-91882 — One block quantizer preserves a single coefficient signature in all native coordinates

Claim ID: `L-91882`  
Status: **PROVED FORMAL COMPILER; LIVE INSTANTIATION IS `L-91881`**  
Created: 2026-08-16  
Depends on: `L-91881`, positive martingale quantization, same-index placement  
RH status: **unproved**

## 1. Disjoint common target

Define

\[
\mathcal T_X
=\mathcal T_X^{\rm anc}\dotplus\mathcal T_X^{\rm bulk},
\]

where the bulk target is

\[
\mathcal T_X^{\rm bulk}
=\coprod_{n=K+2}^{X-W-3}\{n\}\times[0,1).
\]

The anchored target contains already finite placed rows. The tags prevent two
adjacent cells or an anchored point and a bulk point from being identified.

## 2. Single label-blind quantizer

The sole quantizer is

\[
\boxed{
Q_X^{\rm live}=I_{\rm anc}\oplus Q_{\rm bulk}.
}
\tag{L-91882.1}

It is one Markov operator on the disjoint target. It depends only on the
physical target point, never on source sign, Hall edge, Lorenz leaf, first
owner, orientation bit, causal path or child label.

Apply the common thinning

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

once to `Gamma_X^0`. The retained coupling is

\[
\boxed{
\Gamma_X
=\tau_K(\operatorname{id}\times Q_X^{\rm live})_\#\Gamma_X^0.
}
\tag{L-91882.2}

The positive and negative source-incidence discard marginals are explicitly
`(1-tau_K)` times the original anchored and bulk marginals.

## 3. One coefficient signature

For a physical output atom `z`, let `kappa_X(z)` be the product of:

```text
native source coefficient;
stopping-line/casual path coefficient, when anchored;
Hall or Lorenz incidence/residual coefficient;
physical placement coefficient;
one quantizer weight;
common thinning tau_K.
```

Each factor occurs once. For every declared linear observation `L`,

\[
\boxed{
L(d_X)=\sum_z\kappa_X(z)L(z).
}
\tag{L-91882.3}

The same `kappa_X(z)` occurs in target, declared score, literal score, every
component row, ordinary `q`, ordinary `4q`, and every additive boundary
coordinate. Score superordination enters only through the explicit nonnegative
leaf surplus `sigma_omega`.

## 4. Common-row detail

Let `d_X` be the output row marginal of `Gamma_X`. Compute

\[
C_q(d_X)=\sum_z\kappa_X(z)C_q(z),
\qquad
C_{4q}(d_X)=\sum_z\kappa_X(z)C_{4q}(z).
\]

Only after both complete sums define

\[
\boxed{
\Xi_q(d_X)=C_q(d_X)-2C_{4q}(d_X).
}
\tag{L-91882.4}

No branchwise detail inequality is subtracted from another branchwise
inequality. Thus the ordinary and detail ledgers refer to the same finite row
identifier.

## 5. Observation correction

The retained-cell quadrature defect, intrinsic collar and terminal comparison
form one signed vector `e_X` after positive realization. Literal omissions and
the thinning discard give positive unused capacity `u_X`. They are not
additional source stages. If the frozen all-column bounds prove `e_X<=u_X`,
then

\[
r_X=u_X-e_X\ge0
\]

is the actual native response complement.

```text
one target                                anchored plus tagged bulk
one quantizer                             block Markov operator
label dependence                          forbidden
one coefficient signature                 all linear observations
q and 4q                                  complete sums first
detail                                    common-row subtraction
signed comparison                         second ledger
```
