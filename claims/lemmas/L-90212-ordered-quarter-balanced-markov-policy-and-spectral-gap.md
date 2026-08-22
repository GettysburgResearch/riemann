# L-90212 — The ordered quarter-balanced Pascal policy has an exact sliding-band Green recurrence and a nonlattice continuum spectral gap

Claim ID: `L-90212`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA + COMPLETE CONTINUUM SPECTRAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Markov occupation equivalence `L-33107`; elementary finite sums and Mellin/Fourier analysis  
Scope: one explicit broad balanced policy and its continuum transfer; no proof of the critical Möbius occupation sign and no RH conclusion

## 1. Ordered-uniform quarter-balanced policy

For every parent `m>=2`, put

\[
 b_m=\left\lceil\frac m4\right\rceil,
 \qquad I_m=\{b_m,b_m+1,\ldots,m-b_m\},
 \qquad N_m=m-2b_m+1.
\tag{L-90212.1}
\]

On unordered splits `j+(m-j)=m`, `b_m<=j<=floor(m/2)`, use

\[
 \boxed{
 \pi_m(j)=
 \begin{cases}
 2/N_m,&j<m/2,\\
 1/N_m,&m\text{ even and }j=m/2.
 \end{cases}}
\tag{L-90212.2}
\]

This is a probability law: each noncentral unordered split corresponds to two
ordered child positions in `I_m`, while the central split corresponds to one.
All retained children lie in the fixed quarter-balanced window.

## 2. Exact selected-child kernel

Applying the size-biased selected-child construction of `L-33107` gives

\[
 \boxed{
 P_m(k)=\frac{2k}{mN_m}
 \mathbf1_{b_m\le k\le m-b_m}.
 }
\tag{L-90212.3}
\]

Indeed a noncentral split contributes `(2/N_m)(k/m)` to the child `k`, and at
the central split `1/N_m=2(m/2)/(mN_m)`. Symmetry of `I_m` gives
`sum_k 2k/(mN_m)=1`.

Thus this is the full internal-Pascal child law conditioned to the balanced
interval.

## 3. Exact sliding-band occupation recurrence

Let `r` be any finite node divergence and put `s_n=nr_n`.  Let `M` solve

\[
 M-MP=s.
\]

A fixed child `n` occurs in `I_m` exactly when

\[
 \left\lceil\frac{4n}{3}\right\rceil\le m\le4n.
\tag{L-90212.4}
\]

Hence

\[
 \boxed{
 M_n=nr_n+
 \sum_{m=\lceil4n/3\rceil}^{\min(4n,X)}
 \frac{2n}{mN_m}M_m.
 }
\tag{L-90212.5}
\]

Every parent is strictly larger than `n`, so the solve is triangular.  With
`D_n=M_n/n` and `d_{n,j}=D_n\pi_n(j)`, `L-33107` gives

\[
 \boxed{
 M\ge0
 \iff d\text{ is a nonnegative exact quarter-balanced fragmentation of }r.
 }
\tag{L-90212.6}
\]

Equation (L-90212.3) also yields an `O(X)` range-update implementation after the
source is formed: parent `m` adds the common coefficient `2M_m/(mN_m)` to the
single child interval `I_m`, and the child contribution is its index times the
active range sum.

## 4. Continuum law and characteristic

As `m->infinity`, `k/m->v`, the selected-child law converges to

\[
 \boxed{
 p(v)=4v\mathbf1_{1/4\le v\le3/4}.
 }
\tag{L-90212.7}
\]

Its Mellin moment is

\[
 \phi(z)=\mathbb E[V^z]
 =\frac4{z+2}
 \left[\left(\frac34\right)^{z+2}
       -\left(\frac14\right)^{z+2}\right].
\tag{L-90212.8}
\]

For transpose occupation modes the characteristic is

\[
 \boxed{
 \Delta_{\rm bal}(s)
 =1-\phi(s-1)
 =1-\frac4{s+1}
 \left[\left(\frac34\right)^{s+1}
       -\left(\frac14\right)^{s+1}\right].
 }
\tag{L-90212.9}
\]

Conservation gives `Delta_bal(1)=0`.

## 5. Genuine deterministic spectral gap

For `sigma=Re s>1`,

\[
 |\phi(s-1)|\le\mathbb E[V^{\sigma-1}]<1,
\]

so there is no zero to the right of the conservation line. On `s=1+it`,

\[
 \phi(it)=\mathbb E[e^{it\log V}].
\]

Because `log V` has a nondegenerate absolutely continuous distribution,
strict triangle inequality gives `|phi(it)|<1` for `t!=0`. Therefore

\[
 \boxed{
 \Delta_{\rm bal}(s)=0,\ \Re s\ge1
 \iff s=1.
 }
\tag{L-90212.10}
\]

Furthermore

\[
 \Delta_{\rm bal}'(1)=-\mathbb E\log V>0,
\]

so the conservation root is simple.

There is in fact a strict strip: some fixed `delta>0` satisfies

\[
 \boxed{
 \Delta_{\rm bal}(s)\ne0
 \qquad(\Re s\ge1-\delta,\ s\ne1).
 }
\tag{L-90212.11}
\]

If not, take zeros with real parts tending to one.  A bounded-imaginary
subsequence would converge to the unique boundary zero and violate isolation
of the simple root.  An unbounded-imaginary subsequence is impossible because
the explicit compact-density transform satisfies, uniformly for `sigma` near
one,

\[
 |\phi(\sigma-1+it)|\ll(1+|t|)^{-1}\to0.
\]

Thus the broad continuum policy has a genuine source-independent deterministic
spectral gap.

## 6. Policy dichotomy

This sharply contrasts with `L-90206/L-90208`:

```text
finite fixed-ratio policies:      almost-periodic characteristic, no gap;
frozen binary/ternary policy:     surviving near-critical resonance, refuted;
ordered broad balanced policy:    nonlattice continuum law, strict gap.
```

The theorem does not remove the reciprocal-zeta/Möbius arithmetic obstruction.
It only proves that the deterministic resonance mechanism which killed the
frozen producer does not pre-refute this broad policy.

## 7. Proof boundary

Proved exactly:

- the finite quarter-balanced split law;
- its selected-child kernel;
- the exact sliding-band occupation recurrence;
- linear-time range propagation;
- the continuum child density and characteristic;
- uniqueness and simplicity of the conservation root on `Re s>=1`;
- existence of a strict deterministic spectral gap for the continuum policy.

Still open:

- nonnegativity or subpower negative occupation for the critical Möbius source;
- a finite-to-continuum stability theorem strong enough for arithmetic control;
- the square-root hinge theorem of `T-90205`;
- RH.
