# L-106130 — Function-field nonprincipal prime-owner shells have square-root size

Claim ID: `L-106130`  
Programme aliases: `LFAM2.FF_PRIME_OWNER_EXPLICIT_FORMULA`, `LFAM1.NONPRINCIPAL_OWNER_MODEL`, `STRESS.FROBENIUS_PRIME_WICK_GAIN`  
Status: **PROVED UNCONDITIONAL FUNCTION-FIELD THEOREM**  
Created: 2026-08-25  
Depends on: polynomial Dirichlet `L`-function explicit formula and function-field RH  
Programme issues: #737, #736, #743  
Number-field RH status: **not assumed; no transfer claimed**

Let

\[
 A=\mathbf F_q[T]
\]

and let `mathfrak l` be a monic irreducible polynomial of degree `m`.  Let
`chi` be a nonprincipal primitive multiplicative character modulo
`mathfrak l`.  Write

\[
 L(u,\chi)=\prod_{j=1}^{r}(1-\alpha_j u),
 \qquad r\le m-1.
\]

The function-field Riemann hypothesis gives

\[
 |\alpha_j|\le q^{1/2}.
\tag{L-106130.1}
\]

## 1. Exact von Mangoldt explicit formula

The logarithmic derivative gives, for every `n>=1`,

\[
\boxed{
 \sum_{\substack{f\ {m monic}\\\deg f=n}}
 \Lambda(f)\chi(f)
 =-\sum_{j=1}^{r}\alpha_j^n.
}
\tag{L-106130.2}
\]

Consequently

\[
 \left|
 \sum_{\deg f=n}\Lambda(f)\chi(f)
 \right|
 \le (m-1)q^{n/2}.
\tag{L-106130.3}
\]

## 2. Prime shell

Separating prime powers in (L-106130.2) yields

\[
 n\sum_{\substack{P\ {m monic\ irreducible}\\\deg P=n}}
 \chi(P)
 =-\sum_j\alpha_j^n-\mathcal R_n,
\]

where

\[
 |\mathcal R_n|
 \le
 \sum_{\substack{k\mid n\\k\ge2}}
 {n\over k}\,{q^{n/k}\over n/k}
 \ll n q^{n/2}.
\]

Therefore

\[
\boxed{
 \left|
 \sum_{\deg P=n}\chi(P)
 \right|
 \ll {m+n\over n}q^{n/2}.
}
\tag{L-106130.4}
\]

After the critical owner normalization `|P|^{-1/2}=q^{-n/2}`,

\[
\boxed{
 \left|
 \sum_{\deg P=n}{\chi(P)\over|P|^{1/2}}
 \right|
 \ll {m+n\over n}.
}
\tag{L-106130.5}
\]

The bound is polynomial in the conductor and shell degrees.  Excluding the
finitely many prime divisors of a declared squarefree core changes the left
side by at most the number of those divisors.

## 3. Equal-pair owner Wick square

For one complete prime shell put

\[
 \mathcal P_{\chi,n}
 =\sum_{\deg P=n}{\chi(P)\over|P|^{1/2}}.
\]

The equal-pair semiprime owner amplifier is

\[
 \mathcal W_{\chi,n}
 ={1\over2}
 \left[
  \mathcal P_{\chi,n}^2
  -\sum_{\deg P=n}{\chi(P)^2\over|P|}
 \right].
\]

The diagonal term is `O(1/n)`, while (L-106130.5) gives

\[
\boxed{
 |\mathcal W_{\chi,n}|
 \ll \left({m+n\over n}\right)^2+{1\over n}.
}
\tag{L-106130.6}
\]

Thus every complete nonprincipal prime-owner Wick shell has polynomial size,
rather than the exponentially large principal size.

## 4. Principal contrast

For the principal character,

\[
 \sum_{\deg P=n}{1\over|P|^{1/2}}
 \sim {q^{n/2}\over n}.
\tag{L-106130.7}
\]

Hence no memberwise argument can treat the principal and nonprincipal owner
channels identically.  The family supplies a genuine square-root gain only in
the nonprincipal channels; principal individualization remains a separate
problem.

## 5. Meaning for the bilateral tensor

In the function-field mirror of `T-106120`:

```text
nonprincipal--nonprincipal owner Wick factors:
  polynomially bounded shell by shell;

mixed channels:
  one polynomial owner factor and one principal main factor;

principal--principal channel:
  two principal main factors and no Frobenius cancellation.
```

This identifies Frobenius square-root cancellation as the exact mechanism
behind the nonprincipal prime-product collision estimate.  The remaining
geometric work is to transport (L-106130.6) through incomplete Boolean-core
incidence masks and to classify constant constituents of the mixed and double
Kummer sheaves.

## 6. Number-field export target

The number-field analogue needed for `BTNN106122` is not pointwise GRH for
each Dirichlet character.  A sufficient export would be a family-averaged
prime-owner Wick estimate at the same normalized square-root scale, with the
least-core conductors and rough-core masks retained.  Candidate tools are:

```text
hybrid multiplicative large sieve;
Kuznetsov/Petersson after an exact coefficient match;
relative trace formula for the prime-product collision variety;
new exponential-sum estimates suggested by the function-field monodromy.
```

## Scope

This is an unconditional theorem over `F_q[T]`.  It proves no number-field
moment, no instance of `BTPN106122` or `BTNN106122`, and no statement of the
classical Riemann Hypothesis.
