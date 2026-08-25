# R-106508 — A radial source filter is not an input model multiplier

Claim ID: `R-106508`  
Status: **PROVED EXACT TYPE FIREWALL; BINDS THE XI SPECIALIZATIONS OF L-106504--L-106506**  
Created: 2026-08-25  
RH status: **unproved**

## 1. The two variables are different

In the positive-frequency realization, a Hankel operator has kernel

\[
(H_k f)(x)=\int_0^\infty k(x+s)f(s)\,ds.
\]

The current ratio of `L-106500/L-106502` is a multiplier in the **symbol
frequency**

\[
q=x+s.
\]

It sends a radial kernel `j(q)` to `r(q)j(q)`.  It is therefore a Hankel Schur
multiplier on the diagonals `x+s=q`.

By contrast, `L-106504--L-106506` use an operator

\[
(M_r f)(s)=r(s)f(s)
\]

in the **input frequency** `s`.  No change of notation identifies these two
operators.

## 2. Exact norm discrepancy

For a radial kernel `k`, weighting the symbol density gives

\[
\boxed{
\|\mathscr R^{1/2}H_k\|_{\mathcal S_2}^2
=\int_0^\infty q\,r(q)|k(q)|^2\,dq.
}
\tag{R-106508.1}

Multiplying the input instead gives

\[
\begin{aligned}
\|H_kM_r^{1/2}\|_{\mathcal S_2}^2
&=\int_0^\infty\int_0^\infty
 |k(x+s)|^2r(s)\,dx\,ds\\
&=\boxed{
\int_0^\infty |k(q)|^2
\left(\int_0^q r(s)\,ds\right)dq.
}
\end{aligned}
\tag{R-106508.2}

The two formulas agree for all kernels only if

\[
q r(q)=\int_0^q r(s)\,ds
\]

for almost every `q`, which forces `r` to be constant.

The saturating Xi profile `r^sharp_(K,h)` is nonconstant.  Consequently its
source contraction cannot be inserted into a model-space trace merely by
writing the same scalar function as an input multiplier.

## 3. Binding consequences

The following remain valid:

```text
L-106500  positive odd-current source hierarchy;
L-106502  high-frequency saturation as a source-frequency statement;
L-106503  companion pole-height majorization;
L-106504  abstract causal reserve lemma for a genuinely declared input weight;
L-106505  abstract positive-contraction principal-angle split;
L-106506  finite canonical-correlation matrix for that declared input weight;
L-106507  topology-safe common-outer cancellation and Dirichlet domination.
```

The following promotion is **not** established:

```text
source Schur filter r^sharp_(K,h)
      => input model multiplier R^sharp_(K,h)
      => small endpoint Hankel charge.
```

Any use of `L-106504.6`, `L-106505.6`, or `L-106506.4` as a consequence of the
diagonal current contraction must include a new radial-to-input transference
theorem.  Without it, those Xi specializations are quarantined.

## 4. Correct surviving route

`L-106507` avoids the type mismatch.  It cancels only the common **outer**
factor and gives the topology-safe bound

\[
\|H_U\|_{\mathcal S_2}^2
\le\left\|{N-D\over O}\right\|_{\mathcal D}^2.
\]

The conclusion-facing task is therefore an outer-normalized analytic
Dirichlet estimate, or an explicit theorem transferring the radial current
filter to that Dirichlet norm.  Neither is proved by scalar source positivity
alone.
