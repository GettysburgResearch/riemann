# L-94120 — Contractive paired source trees admit an exact projective leafwise realization

Claim ID: `L-94120`  
Status: **PROVED ABSTRACT POSITIVE-GLUING THEOREM**  
Created: 2026-08-16  
Primary inputs: stopped-hazard budget `L-91355/L-91402/L-91403/L-91650`  
RH status: **unproved**

## 1. Typed source category

Let `Src` be the cone of finite positive measures on labels

\[
(\text{endpoint cell},\text{parity},\text{rough history},
 \text{first owner},\text{causal path},\text{physical placement}).
\]

Parity is part of the source label.  Signed observation is the linear map

\[
\mathcal O(\Sigma)=\Sigma_{\rm even}-\Sigma_{\rm odd}.
\]

A paired causal object consists of a parent incidence and its oriented child
incidence before `O` is applied.  It is not required to be a positive physical
row.  A terminal realization is a positive map from such a paired object to a
complete typed packet containing target, declared score, every component row,
ordinary `q`, ordinary `4q`, and boundary coordinates.

## 2. One nonduplicating causal budget

At a source node `v`, let `p_1<...<p_k` be its ordered admissible rough primes,
put

\[
r_i=p_i^{-1/2},\qquad
s_0=1,\qquad s_i=\prod_{h\le i}(1-r_h),
\]

\[
\lambda_i=r_i s_{i-1},\qquad
\alpha_i=r_i\lambda_i.
\]

The exact source identity is

\[
P_v=s_kP_v+\sum_i\lambda_iD_{v,i}
       +\sum_i\alpha_i A_{p_i}P_{vi},
\tag{L-94120.1}
\]

where `D_(v,i)` retains both parent and oriented-child incidences.  The parent
marginal is spent once because

\[
s_k+\sum_i\lambda_i=1.
\tag{L-94120.2}
\]

The genuinely recursive child mass obeys

\[
\sum_i\alpha_i<67^{-1/2}<\frac18.
\tag{L-94120.3}
\]

No physical observation has yet occurred.

## 3. Exact stopped-hazard output contract

The source node is first passed through the exact least-prime stopping/hazard
compiler of `L-91355`, `L-91402`, `L-91403` and `L-91650`.  Its output is not an
arbitrary one-prime difference.  It has the typed form

\[
P_v=G_v^{\rm leaf}+F_v,
\tag{L-94120.4}
\]

where:

* `G_v^leaf` is a finite positive combination of **terminal** `P_61` causal
  leaves `(p,y)` with `p>=67` and `1<=y<67`;
* `F_v` is a positive paired source frontier consisting of the actual oriented
  native children, with all parity, first-owner and same-index labels retained;
* every parent source incidence is used exactly once in either a leaf coupling
  or the frontier;
* every frontier child has scale at most `scale(v)/67`; and
* its total target mass is less than one eighth of the incoming target mass.

The source coefficient of a terminal path is the product of the exact hazard
coefficients and the original stopping-line coefficient.  No coefficient is
introduced by physical observation.  `L-94121` reconstructs this output
contract atom by atom for the live native fibre; it is not assumed merely from
the abstract theorem.

## 4. Projective realization

Let `F_n` be the unresolved paired source frontier after `n` recursive levels
and let `G_n` be the sum of all terminal leaf realizations already produced.
Substituting (L-94120.4) only inside `F_n` gives the exact source-marginal
identity

\[
P_X=G_n+F_n.
\tag{L-94120.5}
\]

No member of `F_n` has been physically observed.  If `M_X` is the root target
mass, the stopped-hazard contract gives

\[
M(F_n)\le 8^{-n}M_X,
\qquad
\operatorname{scale}(F_n)\le X/67^n.
\tag{L-94120.6}
\]

For fixed `X`, after more than `log X/log 67` levels every frontier packet lies
in the directed outer terminal class.  Thus there is no infinite unresolved
residue.  Replace that final frontier by its positive outer realization and sum
all terminal maps.  The result is one positive complete packet `G_X` whose
source marginal is exactly `P_X`.

Because every terminal map uses one common coefficient vector in all
coordinates, the projective sum does too.  Tonelli applies to the finite
positive source sum.  Ordinary `q` and ordinary `4q` are evaluated on `G_X`
before detail is formed.

## 5. What the theorem does not do

The theorem never claims that an intermediate oriented child is a positive row.
It never promotes an actual child to full endpoint capacity.  It never scales a
signed comparison error by source mass.  It only glues source incidences and
terminal positive realizations.

```text
parent source ownership                 exact / one-use
intermediate oriented child             source-only / unobserved
terminal leaf realization               positive
frontier target mass                    <8^(-n) M_X
frontier termination                    finite for fixed X
coordinate coefficient system           common
branchwise q/4q subtraction              forbidden
```
