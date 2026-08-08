# T-29001 — Atomized carry-frame and endpoint-tree proposal for RH

Claim ID: `T-29001`  
Title: The complete carry-position frame, exact Selberg–Kummer interior reserve, and balanced-tree endpoint commutator reduce RH to one source-specific endpoint recurrence  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT ENDPOINT-TREE RECURRENCE OPEN**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: `L-29001`--`L-29003`; PR #241 `L-9518`; PR #269 source package; PR #289 prime-annulus commutator  
Scope: complete conditional deduction; RH is not claimed proved

## 1. Why the carry-position variable must be retained

Averaging the carry position before squaring produces one useful scalar kernel,
but it collapses the transverse normal frame.  `L-29001` instead retains

\[
 \theta\in[\eta,1-\eta]
\]

through the complete square.  The resulting vector field is

\[
 \mathfrak P_\theta(t)
 =\sum_q\frac{\Lambda(q)}{\sqrt q}
  z_{\theta,\omega}(t-\log q),
\tag{T-29001.1}
\]

with transform

\[
 -E(s)N_\theta(s)\frac{\zeta'}\zeta(s),
 \qquad s=z+\frac12.
\tag{T-29001.2}
\]

Its balanced residue frame has strictly positive norm at every nontrivial zeta
zero.  Therefore

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathscr E_\eta(J)=e^{o(J)},
}
\tag{T-29001.3}

where

\[
 \mathscr E_\eta(J)
 =\int_J^{J+1}\int_\eta^{1-\eta}
   |\mathfrak P_\theta(t)|^2d\theta dt.
\tag{T-29001.4}

Unlike the former transference schemas, this energy is already the exact finite
carry Gram

\[
 \frac1X\int_\eta^{1-\eta}
 \left|\sum_{m\le X}\Lambda(m)Z_{X,m}(\theta)\right|^2d\theta
\tag{T-29001.5}

at `X=e^t`.  No unknown physical-to-carry map remains.

## 2. The exact interior/boundary split

For one binomial row define

\[
 F_n(j)=\log\binom nj
\]

and the complete Selberg forcing row

\[
 S_n(j)
 =\sum_d[\Lambda(d)\log d+(\Lambda*\Lambda)(d)]
       \chi_{n,d}(j).
\]

`L-29002` proves pointwise

\[
\boxed{
 Q_n(j):=F_n(j)^2-S_n(j)\ge0.
}
\tag{T-29001.6}

Moreover,

\[
\boxed{
 Q_n(j)=0
 \iff j\in\{0,1,n-1,n\}.
}
\tag{T-29001.7}

On every fixed balanced cone,

\[
 S_n(j)
 \le O_\eta\left(\frac{\log^2n}{n}\right)F_n(j)^2.
\tag{T-29001.8}

Thus the complete reflected Selberg forcing leaves an asymptotically full
positive reserve on every interior carry row.  The only nontrivial zero-reserve
channel is the endpoint-neighbor pair selected by the dyadic source.

## 3. Exact endpoint routing

Let `T_n` be the canonical balanced fragmentation tree of `L-29003`.  Then

\[
 [n,1]\equiv T_n-T_{n-1}\pmod{\ker\partial},
\tag{T-29001.9}

with equality of every carry column and of the entropy objective.  For a complete
endpoint coefficient family `c_n`,

\[
\boxed{
 \sum_{n=2}^{N}c_n[n,1]
 \equiv
 c_NT_N+\sum_{n=2}^{N-1}(c_n-c_{n+1})T_n.
}
\tag{T-29001.10
}

Every proper tree descendant lies at most at half the parent scale.  The endpoint
obstruction has therefore become one outer boundary and one first-difference
coefficient ledger.

## 4. Sole closing theorem — `ETSR`

The **Endpoint-Tree Selberg Recurrence** is the following source-specific
statement.

> For one fixed `eta in (0,1/2)` there are absolute constants `A,C`, a fixed
> logarithmic reserve `delta>0`, and a complete source-bound decomposition of
> every atomized reflected block such that
> \[
> \boxed{
> \mathscr E_\eta(J)+\mathscr Q_\eta(J)
> \le
> C(1+J)^A
> +\sum_{\nu}\theta_\nu
>   \mathscr E_\eta(J_\nu),
> }
> \tag{ETSR}
> \]
> where
> \[
> \mathscr Q_\eta(J)\ge0,
> \qquad
> J_\nu\le J-\delta,
> \qquad
> \sum_\nu\theta_\nu\le1.
> \]
> The term `mathscr Q_eta` is the complete sum of the pointwise reserves
> `Q_n(j)` from `L-29002`.  Every zero-reserve endpoint row must be transformed
> by (T-29001.10) before a norm is taken.  The outer tree, all coefficient
> differences, all Pascal cycles, all dyadic siblings, and every finite cutoff
> must be retained.

A strict sum below one is welcome but is not required.  A fixed lower-scale
shift with total coefficient one and a polynomial inhomogeneous term already
implies a polynomial bound by iteration.

## 5. Conditional completion

Assume `ETSR`.  Dropping the nonnegative reserve gives

\[
 \mathscr E_\eta(J)
 \le C(1+J)^A
  +\max_{u\le J-\delta}\mathscr E_\eta(u)
\tag{T-29001.11}

in the conservative coefficient-one case.  Iteration through
`O(J/delta)` scales gives

\[
\boxed{
 \mathscr E_\eta(J)\ll(1+J)^{A+1}.
}
\tag{T-29001.12}

Hence `mathscr E_eta(J)=e^{o(J)}`.  The vector-valued pole criterion
`L-29001.26` excludes every zeta zero with real part greater than one half.
Functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-29001.13}

The averaged coordinate of the atomized bank is the top-quarter prime-annulus
statistic on PR #289, so the same recurrence also proves `PAE`.  The stable
fixed-ratio filters then export the exact `2/3` first-cell Mertens mutation.

## 6. Why this is not another ambient positivity conjecture

The proposal does not ask for:

- positivity of a carry inverse;
- a generic operator norm;
- bounded packet rank;
- a fixed-order Abel kernel;
- a one-frequency analytic square;
- a physical-to-carry transference theorem;
- full Carry Saturation;
- WSTS as a black box.

The positive part is explicit and already proved row by row in `L-29002`.  The
only open statement is the signed, source-complete endpoint Abel ledger after
the exact balanced-tree replacement.

## 7. Production requirements

A valid `ETSR` object must emit:

1. the complete balanced carry-position partition;
2. the independent-frequency physical normal matrix;
3. the exact equality with the carry Gram of `L-29001`;
4. every ordinary Selberg linear and convolution coefficient;
5. the pointwise reserve `Q_n(j)` with no omitted endpoint;
6. the complete endpoint coefficient sequence before differencing;
7. the exact tree and Pascal-cycle expansion from `L-29003`;
8. every outer-tree and cutoff term;
9. a proof that all declared children lie at `J-delta` or lower;
10. the prime-annulus and `2/3` Mertens mutations.

Automatic rejection applies if the certificate averages `theta` before
squaring, drops a translate cross term, spends the reserve twice, estimates an
endpoint before tree recombination, or places target energy inside the
polynomial channel.

## 8. Exact status

```text
atomized Nyman/carry frame                   PROPOSED COMPLETE
vector-valued pole criterion                 PROPOSED COMPLETE
physical normal energy = carry Gram          PROPOSED COMPLETE
Selberg-Kummer interior reserve              PROPOSED COMPLETE
endpoint = balanced-tree commutator          PROPOSED COMPLETE
fixed-order Abel ambient shortcuts           REFUTED
ETSR endpoint-tree recurrence                OPEN / RH-BEARING
ETSR -> atomized energy -> RH                 COMPLETE CONDITIONAL
Riemann Hypothesis                           UNPROVED
```

This is a full-problem proposal with one explicit arithmetic recurrence.  It is
not represented as a completed proof until `ETSR` is constructed.