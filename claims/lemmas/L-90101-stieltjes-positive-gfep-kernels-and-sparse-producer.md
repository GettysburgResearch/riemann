# L-90101 — Every GFEP coefficient is a positive Stieltjes packet, and the sparse producer inherits the same positive kernel

Claim ID: `L-90101` (provisional branch range)  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: PR #292 `L-28001`; PR #328 `L-32301`; PR #351 `T-90006`, `T-90007`, and `L-90004`  
Scope: exact finite algebra and a positive-measure representation; no Möbius-sum sign and no RH conclusion

## 1. Setup

Fix a real endpoint `X >= 1`, an integer threshold `n >= 2`, and an exit

\[
 p\in W=[n,2n)\cap\mathbb Z,
 \qquad p\le X.
\]

Retain the frozen size-biased binary–ternary chain of `L-28001`.  Write

\[
 E_n(m,p)=\mathbb P_m(Z_{\tau_n}=p),
 \qquad
 G_p(m)=mE_n(m,p),
\tag{L-90101.1}
\]

and set `G_p(m)=0` for `m<n`.  Thus `G_p(m)>=0` and, by `L-90004`,

\[
 G_p(m)=p\sum_{\pi:m\leadsto p}2^{-|\pi|},
\tag{L-90101.2}
\]

where the sum runs over first-entrance paths in the deterministic four-edge child graph, with multiplicity.

Let

\[
 w_X(q)=q^{-1/2}\log\frac Xq\,\mathbf 1_{q\le X}.
\tag{L-90101.3}
\]

The coefficient isolated in `T-90007 §2` is

\[
 c^{X,n}_p(k)
 =\sum_{m=n}^{\lfloor X/k\rfloor}
   \bigl(G_p(m)-G_p(m-1)\bigr)w_X(mk).
\tag{L-90101.4}
\]

`T-90007` established

\[
 \Sigma_{X,n}(p)=\sum_{k\ge1}\mu(k)c^{X,n}_p(k)
\tag{L-90101.5}
\]

and reported `c_p(k)>=0` as a conjecture supported by 9,825 tested pairs.  The conjecture is an immediate finite Abel identity.

## 2. Theorem A — positive Abel normal form

Put `M=floor(X/k)`.  Then

\[
\boxed{
 c^{X,n}_p(k)
 =\sum_{m=n}^{M}G_p(m)
   \bigl[w_X(mk)-w_X((m+1)k)\bigr].
}
\tag{L-90101.6}
\]

Here `w_X((M+1)k)=0`, because `(M+1)k>X`.

Since

\[
 -\frac d{dq}w_X(q)
 =q^{-3/2}\left(1+\frac12\log\frac Xq\right)>0
 \qquad(0<q<X),
\tag{L-90101.7}
\]

the critical weight is decreasing on its support.  Every summand on the right of (L-90101.6) is therefore nonnegative, and hence

\[
\boxed{c^{X,n}_p(k)\ge0.}
\tag{L-90101.8}
\]

### Proof

Apply finite summation by parts to (L-90101.4), with `G_p(n-1)=0`:

\[
\begin{aligned}
\sum_{m=n}^{M}(G_p(m)-G_p(m-1))w_X(mk)
={}&G_p(M)w_X(Mk)\\
&+\sum_{m=n}^{M-1}G_p(m)
  [w_X(mk)-w_X((m+1)k)].
\end{aligned}
\]

Adding the zero terminal value `w_X((M+1)k)=0` gives (L-90101.6).  Equation (L-90101.8) follows from `G_p>=0` and (L-90101.7). ∎

This proof is endpoint-uniform, uses no property of `mu`, and removes the numerical/conjectural status of the positive-kernel statement in `T-90007 §2`.

## 3. Theorem B — positive Stieltjes/path measure

The Abel packet has the exact integral form

\[
\boxed{
 c^{X,n}_p(k)
 =\int_{kn}^{X}
 G_p\!\left(\left\lfloor\frac uk\right\rfloor\right)
 u^{-3/2}\left(1+\frac12\log\frac Xu\right)du.
}
\tag{L-90101.9}
\]

Equivalently, using (L-90101.2), it is the total positive weight of triples

```text
(starting node m, first-entrance path m -> p, continuous point u in [mk,(m+1)k])
```

with density

\[
 p\,2^{-|\pi|}
 u^{-3/2}\left(1+\frac12\log\frac Xu\right)du.
\tag{L-90101.10}
\]

### Proof

For each `m`, integrate (L-90101.7) over `[mk,(m+1)k]`, truncate the final interval at `X`, and sum (L-90101.6).  The intervals partition `[kn,X]` up to endpoints of measure zero. ∎

Thus the GFEP scalar is not merely a formal signed coefficient sum.  It is exactly an inclusion–exclusion sum over explicitly positive transport packets:

\[
 \Sigma_{X,n}(p)
 =\sum_{k\ge1}\mu(k)
   \int_{kn}^{X}G_p(\lfloor u/k\rfloor)
   u^{-3/2}\left(1+\frac12\log\frac Xu\right)du.
\tag{L-90101.11}
\]

This is the natural continuous refinement of the `R`-form object algebra in `L-90004`.  It removes packet-cardinality as a fundamental obstruction, because packets may be split measurably.  It does **not** itself supply a sign-preserving coupling between the `mu=+1` and `mu=-1` packet measures.

## 4. Theorem C — every nonnegative exit trace has a positive kernel

Let `a(p)>=0` on `W`, and define

\[
 G_a(m)=\sum_{p\in W}a(p)G_p(m),
 \qquad
 c^{X,n}_a(k)=\sum_{p\in W}a(p)c^{X,n}_p(k).
\tag{L-90101.12}
\]

Then `G_a>=0`, and the same formulas give

\[
\boxed{
 c^{X,n}_a(k)
 =\sum_{m=n}^{\lfloor X/k\rfloor}G_a(m)
 [w_X(mk)-w_X((m+1)k)]\ge0,
}
\tag{L-90101.13}
\]

and

\[
 \sum_{p\in W}a(p)\Sigma_{X,n}(p)
 =\sum_{k\ge1}\mu(k)c^{X,n}_a(k).
\tag{L-90101.14}
\]

In particular, take the true producer trace

\[
 a(p)=h_n(p)=\mathbb P_p(\exists t:Z_t=n).
\tag{L-90101.15}
\]

By the strong Markov identity,

\[
 G_a(m)=m h_n(m).
\tag{L-90101.16}
\]

By `L-32301`, `a` is supported on `p=n`, the one or two ternary contact sites satisfying `floor(2p/3)=n`, and `p=2n-1`.  Therefore

\[
\boxed{
 nA_X(n)
 =\sum_{p\in W}h_n(p)\Sigma_{X,n}(p)
 =\sum_{k\ge1}\mu(k)c^{X,n}_{\mathrm{prod}}(k),
 \qquad c^{X,n}_{\mathrm{prod}}(k)\ge0.
}
\tag{L-90101.17}
\]

This is the exact positive-kernel form for the **actual sparse consumer**, not the stronger coordinatewise GFEP target.

## 5. Theorem D — scale dictionary and the built-in skeptic

The critical weight scales exactly:

\[
 w_X(mk)=k^{-1/2}w_{X/k}(m).
\tag{L-90101.18}
\]

Since `G_p` is endpoint-independent, (L-90101.4) gives

\[
\boxed{
 c^{X,n}_p(k)=k^{-1/2}c^{X/k,n}_p(1).
}
\tag{L-90101.19}
\]

More importantly, for `X/k>=p`, the complete multiples Möbius transform is

\[
\boxed{
 \sum_{j\le X/(kn)}\mu(j)c^{X,n}_p(kj)
 =k^{-1/2}\Sigma_{X/k,n}(p).
}
\tag{L-90101.20}
\]

The same identity holds for every nonnegative trace `a`, including the sparse producer trace.

### Proof

Equation (L-90101.19) is (L-90101.18) substituted into (L-90101.4).  Then

\[
\begin{aligned}
\sum_j\mu(j)c^{X,n}_p(kj)
&=\sum_j\mu(j)(kj)^{-1/2}c^{X/(kj),n}_p(1)\\
&=k^{-1/2}\sum_j\mu(j)c^{X/k,n}_p(j)\\
&=k^{-1/2}\Sigma_{X/k,n}(p),
\end{aligned}
\]

where the middle equality is the same scaling formula read in reverse. ∎

Equation (L-90101.20) is the required adversarial check on a tempting combinatorial proof.  Numerically, the sequence `k -> c_p(k)` exhibits extensive squarefree finite-difference positivity.  But its **full** divisor-lattice primitive at scale `k` is exactly GFEP at the smaller endpoint `X/k`.  Consequently:

```text
“c_p is the divisibility tail of a positive primitive measure”
```

is not a free consequence of (L-90101.8); at full depth it is precisely the statement being sought, recursively rescaled.  A valid primitive-object construction must therefore produce the primitive measure directly, not define it by Möbius inversion of `c_p`.

This also explains why a strong-induction attack is natural but incomplete: all primitive coordinates with `k>=2` are smaller-endpoint GFEP values, while the unsolved `k=1` primitive is the current endpoint itself.

## 6. What is and is not closed

Proved exactly here:

1. every coefficient `c_p(k)` conjectured positive in `T-90007` is nonnegative;
2. each coefficient is a positive Stieltjes/path packet;
3. every nonnegative exit trace, including the three-site producer consumer, inherits the positive kernel;
4. the exact scale/multiples-Möbius dictionary (L-90101.19)--(L-90101.20).

Not proved here:

1. nonnegativity of `sum_k mu(k)c_p(k)`;
2. nonnegativity of the sparse producer sum;
3. a structural coupling of positive and negative squarefree packet layers;
4. GFEP or RH.

The new proof removes one conjectural line from the Fable packet and identifies the precise remaining combinatorial task: construct a positive **primitive packet measure** compatible with the frozen chain, without obtaining it by the circular transform (L-90101.20).
