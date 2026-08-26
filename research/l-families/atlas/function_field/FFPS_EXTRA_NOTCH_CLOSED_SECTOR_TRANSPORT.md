# Mollification transports the extra notch through the parent closure classes

Status: **generic fixed-mollifier transport theorem and summary-level
parent-taxonomy candidate; exact source recombination and a finite
claim-by-claim provenance audit remain required before `EXTSRC106150`**

Bounded exponent replay:
[`ffps_extra_notch_closed_sector_transport.py`](ffps_extra_notch_closed_sector_transport.py).

Frozen parent: PR #719 at exact scientific head
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, specifically the zero-moment
`L-102880`, `L-102953`, `T-102970`, and `T-102990`.  The extra-notched
definition is frozen separately at
`98af0db6ec7f77d6333a77a3dac53c4698852f43`, specifically `L-102701`,
`L-106134`, and `T-106150`.  The replay authenticates exact blobs, avoiding
the duplicate `L-102880` claim number at the first commit.

## 0. Outcome

The extra-notched current is a finite signed logarithmic measure, while the
parent Boolean programme is written for a compact function kernel.  One fixed
positive log-box smoothing puts the new current into the two generic kernel
classes named by the summary descriptions in `T-102990`:

1. compact bounded-variation kernels of zero logarithmic mass, for Type I;
2. fixed compact `L1` kernels, for absolute source closures.

Let `K_ext` be the extra-notched measure.  With

\[
q(s)=1-\sqrt2\,2^{-s},\qquad r(s)=1-2^{-s},
\]

its frozen multiplier is

\[
\widehat K_{\rm ext}(s)
={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)}.
\tag{0.1}
\]

Fix `epsilon>0` independently of the horizon `Y`, and let

\[
\eta_\varepsilon(t)
={1\over\varepsilon}1_{[0,\varepsilon]}(t),
\qquad
k_\varepsilon=\eta_\varepsilon*K_{\rm ext}.
\tag{0.2}
\]

Then `k_epsilon` is compact and of bounded variation,

\[
\int_{\mathbb R}k_\varepsilon(t)dt=0,
\tag{0.3}
\]

and, distributionally,

\[
\partial_t k_\varepsilon
={K_{\rm ext}-\tau_\varepsilon K_{\rm ext}\over\varepsilon},
\qquad
\operatorname{Var}(k_\varepsilon)
\le {2\|K_{\rm ext}\|_{\rm TV}\over\varepsilon},
\qquad
\|k_\varepsilon\|_1\le\|K_{\rm ext}\|_{\rm TV}.
\tag{0.4}
\]

Here `tau_epsilon` is translation by `epsilon`.  The log-box multiplier is

\[
\widehat\eta_\varepsilon(s)
={1-e^{-\varepsilon s}\over\varepsilon s}.
\tag{0.5}
\]

Positive convolution also contracts Jordan negative variation.  Therefore a
raw `WKSFSC` Jordan negative-variation premise controls the mollified live
current.  All constants here may depend on the fixed `epsilon`; this packet
makes no uniform claim as `epsilon` tends to zero.

This nominates a finite route to `EXTSRC106150`; it does not close the adapter.
One must verify that each inherited proof named “absolute”, “summable”,
“polylogarithmic”, or “Type-I lattice” really uses only the corresponding
kernel-class norm at its exact source scope.  The audit must also bind the
seven closed rows and the live row into the exact complete-source
recombination, with the same horizon convention.  The summary theorem
`T-102990` states the taxonomy but cannot replace those checks.

## 1. Generic zero-mass lattice theorem

Let `k` be any fixed compact `BV` logarithmic kernel with

\[
\int k(t)dt=0.
\]

Define

\[
\mathscr L_k(Z)
=\sum_{m\ge1}{1\over m}
k(\log(Z/m^2)).
\tag{1.1}
\]

For

\[
g_Z(x)=x^{-1}k(\log(Z/x^2)),
\]

the substitution `t=log(Z/x^2)` gives

\[
\int_0^\infty g_Z(x)dx
={1\over2}\int_{\mathbb R}k(t)dt=0.
\tag{1.2}
\]

Put `x=sqrt(Z)u` and
`h(u)=u^(-1)k(-2log u)`.  Compactness and bounded variation of `k` give
compact `BV` for `h`, while
`g_Z(x)=Z^(-1/2)h(x/sqrt(Z))`.  Hence

\[
\operatorname{Var}(g_Z)
=Z^{-1/2}\operatorname{Var}(h)
\ll_k Z^{-1/2}.
\tag{1.3}
\]

The one-dimensional Euler summation inequality yields

\[
\boxed{\mathscr L_k(Z)=O_k(Z^{-1/2}).}
\tag{1.4}
\]

With `U=Y^(1/6)`, the unrestricted Type-I row is therefore

\[
O_k(U^2Y^{-1/2})=O_k(Y^{-1/6}).
\tag{1.5}
\]

The frozen `L-102953` also uses an owner-excluded lattice.  Inclusion--exclusion
supplies the missing generic step.  For a squarefree exclusion modulus `R`,

\[
\mathscr L_k^{(R)}(W)
=\sum_{d\mid\operatorname{rad}R}{\mu(d)\over d}
 \mathscr L_k(W/d^2).
\tag{1.6}
\]

Equation (1.4) therefore gives

\[
\mathscr L_k^{(R)}(W)
\ll_k 2^{\omega(R)}W^{-1/2}.
\tag{1.7}
\]

At the exact parent scope, the finite owner, marked-prime, and Boolean
multiplicity ledger supplies `2^omega(R)=Y^(o(1))`; this hypothesis is not a
consequence of the kernel lemma.  The kernel-independent squarefree identity is

\[
\mathscr L_{k,{\rm sf}}^{(R)}(Z)
=\sum_{\substack{\ell\ge1\\(\ell,R)=1}}
 {\mu(\ell)\over\ell^2}
 \mathscr L_k^{(R)}(Z/\ell^4).
\tag{1.8}
\]

Compact support restricts `ell` to `O_k(Z^(1/4))`.  Applying (1.7) termwise
cancels the factor `ell^2` and yields

\[
\mathscr L_{k,{\rm sf}}^{(R)}(Z)
\ll_k Y^{o(1)}Z^{-1/4}.
\tag{1.9}
\]

Finally, the exact Type-I weights in `L-102953` give

\[
Y^{-1/4+o(1)}
\left(\sum_{d\le U}d^{-1/2}\right)^2
\ll Y^{-1/12+o(1)}.
\tag{1.10}
\]

Thus the Type-I mechanism transports to every fixed mollified extra-notched
kernel, conditional only on the exact parent exclusion-multiplicity ledger
just stated.

## 2. Generic absolute-sector theorem

Suppose a source sector has atoms `(c_alpha,n_alpha)` satisfying, on the
active horizon,

\[
\sum_\alpha|c_\alpha|=Y^{o(1)}.
\tag{2.1}
\]

For any fixed compact `L1` log kernel `k`, Tonelli gives

\[
\begin{aligned}
\int\left|
\sum_\alpha c_\alpha
k(\log X-\log n_\alpha)
\right|{dX\over X}
&\le
\|k\|_1\sum_\alpha|c_\alpha|\\
&=Y^{o(1)}.
\end{aligned}
\tag{2.2}
\]

This is insensitive to the precise dyadic notch, sign pattern, or compact
support endpoints.

## 3. Summary taxonomy and provenance boundary

The frozen theorem lists seven closed classes:

| parent sector | transport mechanism |
|---|---|
| Boolean Type-I row | (1.6)--(1.10), using the parent multiplicity ledger |
| finite and terminal rows | fixed finite kernel norm |
| equal reduced core | absolute source bound |
| one-sided reduced core | absolute source bound |
| very-large common square core | absolute summability |
| squared/higher-prime-power colour | polylogarithmic absolute ledger |
| equal-pair owner multiplicity | polylogarithmic absolute ledger |

At the theorem-summary level, the table supplies a candidate transport for
every named closed sector.  It does not yet prove that the only live row after
the new observation is the coprime two-sided Boolean core.

The load-bearing caveat is provenance.  Some older claims use special
pointwise facts about the explicit `K_L`; a summary word such as “closed” does
not prove that no such fact entered a downstream estimate.  Each of the seven
rows must be traced to its exact last proof before `EXTSRC106150` is promoted
from nominated to proved.

## 4. One-sided compatibility

Positive smoothing satisfies

\[
\boxed{
\|(\eta_\varepsilon*H)_-\|_{L^1}
\le\|H_-\|_{\rm TV}.}
\tag{4.1}
\]

More locally, for every log interval `I`, positivity and Fubini give

\[
\int_I(\eta_\varepsilon*H)_-(t)dt
\le H_-(I-[0,\varepsilon]).
\tag{4.2}
\]

Thus a dyadic-horizon estimate needs only `O_epsilon(1)` neighbouring dyadic
blocks.  This is harmless only because `epsilon` is fixed.

It commutes with source shifts, Boolean projections, and fixed dyadic
operators.  Hence

```text
raw Jordan WKSFSC
  -> mollified live negative-mass bound;

proved EXTSRC106150, including the seven-row provenance and source binding
  -> mollified closed field has absolute subpower mass;

both together
  -> mollified complete extra-notched beta current has subpower negative mass.
```

The separate analytic consumer is recorded in
`FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md`; this packet neither re-audits
that consumer nor supplies its still-open `EXTSRC106150` premise.

## 5. Boundary and next exact task

Proved here:

- compact `BV`, zero-mass, and one-sided properties of the smoothed kernel;
- the unrestricted and owner-excluded generic zero-mass lattice estimates;
- the squarefree-transfer and Type-I exponents under the parent
  `Y^(o(1))` exclusion-multiplicity hypothesis;
- the generic absolute-source transfer;
- the transcription of the seven summary closure labels in `T-102990` and a
  candidate generic transport mechanism for each.

Still required:

- a claim-by-claim audit of the seven frozen parent closures at
  `ec6635b4...`;
- a corrected source-lock replacing the false common-mother/native-kernel
  identification;
- exact complete-source recombination and horizon compatibility after
  mollification;
- the full-source statement `EXTSRC106150`;
- raw Jordan `WKSFSC106150`.

The audit should start with `L-102953` and `T-102970`, then walk backward only
where those files cite an inherited absolute ledger.  It need not recompute a
single conductor or source family.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_extra_notch_closed_sector_transport.py --check
python -B -O research/l-families/atlas/function_field/ffps_extra_notch_closed_sector_transport.py --check
python -B -m unittest tests.test_ffps_extra_notch_closed_sector_transport
python -B -O -m unittest tests.test_ffps_extra_notch_closed_sector_transport
```

The replay authenticates seven frozen source blobs and checks only rational
exponents and four scalar contraction panels.  It enumerates no source atom,
conductor, curve, or point.
