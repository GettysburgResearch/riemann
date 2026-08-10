# L-90209 — The ordered quarter-balanced Pascal policy has an exact sliding-band Green recurrence and a nonlattice continuum spectral gap

Claim ID: `L-90209`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA + COMPLETE CONTINUUM SPECTRAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Markov occupation equivalence `L-33107`; elementary finite sums and Mellin/Fourier analysis  
Scope: one explicit broad balanced policy and its continuum transfer; no proof of the critical Möbius occupation sign and no RH conclusion

## 1. Ordered-uniform quarter-balanced split policy

For every parent `m>=2`, put

\[
 b_m=\left\lceil\frac m4\right\rceil,
 \qquad
 I_m=\{b_m,b_m+1,\ldots,m-b_m\},
 \qquad
 N_m=|I_m|=m-2b_m+1.
\tag{L-90209.1}
\]

All children in `I_m` lie in `[m/4,3m/4]` up to the unavoidable integer
rounding.

On unordered splits `j+(m-j)=m`, `b_m<=j<=floor(m/2)`, define

\[
 \boxed{
 \pi_m(j)=
 \begin{cases}
 2/N_m,&j<m/2,\\
 1/N_m,&m\text{ even and }j=m/2.
 \end{cases}}
\tag{L-90209.2}
\]

This is a probability law: every noncentral split accounts for two ordered
child positions in `I_m`, while the central split accounts for one.

Equivalently, choose an ordered child position uniformly from `I_m`, forget
which side of the split it came from, and then apply the size-biased selected
child rule of `L-33107`.

## 2. Exact selected-child kernel

For every `k<m`, the size-biased child law is

\[
 \boxed{
 P_m(k)
 =\frac{2k}{mN_m}\mathbf1_{b_m\le k\le m-b_m}.
 }
\tag{L-90209.3}
\]

### Proof

For a noncentral split `j`, the lower child receives probability

\[
 \frac{2}{N_m}\frac jm,
\]

and the reflected upper child receives

\[
 \frac{2}{N_m}\frac{m-j}{m}.
\]

At a central split the single child receives the whole split mass
`1/N_m`, which equals `2(m/2)/(mN_m)`.  Hence all child positions in `I_m`
have the common formula (L-90209.3).  Summation gives

\[
 \sum_{k=b_m}^{m-b_m}\frac{2k}{mN_m}=1
\]

because the symmetric interval has mean `m/2`. ∎

This is exactly the full internal Pascal selected-child law

\[
 \frac{2k}{m(m-1)},\qquad1\le k<m,
\]

conditioned on the balanced event `k in I_m`.

## 3. Exact sliding-band occupation recurrence

Let `r_1,...,r_X` be an arbitrary node divergence and put

\[
 s_n=nr_n.
\]

Let `M` solve the Markov occupation equation

\[
 M-MP=s
\]

for the policy (L-90209.3).  A fixed child `n` belongs to `I_m` exactly when

\[
 \left\lceil\frac{4n}{3}\right\rceil\le m\le4n.
\tag{L-90209.4}
\]

Indeed `b_m<=n` is equivalent to `m<=4n`, while
`n<=m-b_m=floor(3m/4)` is equivalent to `m>=ceil(4n/3)`.

Therefore

\[
 \boxed{
 M_n
 =nr_n+
 \sum_{m=\lceil4n/3\rceil}^{\min(4n,X)}
 \frac{2n}{mN_m}M_m.
 }
\tag{L-90209.5}
\]

All parents in the sum are strictly larger than `n`, so this is a triangular
descending recurrence.

Writing `D_n=M_n/n`, the corresponding split flow is

\[
 d_{n,j}=D_n\pi_n(j).
\tag{L-90209.6}
\]

By `L-33107`,

\[
 \boxed{
 M_n\ge0\ \forall n
 \quad\Longleftrightarrow\quad
 d\text{ is a nonnegative exact quarter-balanced fragmentation of }r.
 }
\tag{L-90209.7}
\]

## 4. Linear-time range-update implementation

Equation (L-90209.3) makes the whole Green solve linear after the source has
been formed.  A parent `m` contributes

\[
 \frac{2M_m}{mN_m}\,k
\]

to every future child `k in I_m`.  Thus one keeps a descending range-add scalar
`C`, queries `kC` at the current node, and adds the parent coefficient on the
single interval `[b_m,m-b_m]`.

No quadratic split matrix or LP is needed.  The retained verifier compares this
range implementation with direct `O(X^2)` propagation on small instances.

## 5. Continuum selected-child law

As `m->infinity`, with `k/m->v`, the conditional child law converges to

\[
 \boxed{
 p(v)=4v\,\mathbf1_{1/4\le v\le3/4}.
 }
\tag{L-90209.8}
\]

This is precisely the quarter-balanced continuum law already identified in
`L-33107`, now attached to the concrete finite policy (L-90209.2).

Its Mellin moment is

\[
 \boxed{
 \phi(z)=\mathbb E[V^z]
 =\frac4{z+2}
 \left[\left(\frac34\right)^{z+2}
       -\left(\frac14\right)^{z+2}\right].
 }
\tag{L-90209.9}
\]

For transpose occupation modes the natural characteristic is

\[
 \boxed{
 \Delta_{\rm bal}(s)
 =1-\phi(s-1)
 =1-\frac4{s+1}
 \left[\left(\frac34\right)^{s+1}
       -\left(\frac14\right)^{s+1}\right].
 }
\tag{L-90209.10}
\]

The conservation root is

\[
 \Delta_{\rm bal}(1)=0.
\tag{L-90209.11}
\]

## 6. The broad continuum policy has a genuine spectral gap

Unlike the two-ratio characteristic of `L-90206`, the law (L-90209.8) is
absolutely continuous and nonlattice.

### No zeros on or to the right of the conservation line

For `sigma=Re s>1`,

\[
 |\phi(s-1)|
 \le\mathbb E[V^{\sigma-1}]<1,
\]

so `Delta_bal(s)!=0`.

On `s=1+it`,

\[
 \phi(it)=\mathbb E[e^{it\log V}].
\]

If `t!=0`, strict triangle inequality gives

\[
 |\phi(it)|<1
\]

because `log V` has a nondegenerate continuous distribution on an interval.
Thus

\[
 \boxed{
 \Delta_{\rm bal}(s)=0,\ \Re s\ge1
 \quad\Longleftrightarrow\quad s=1.
 }
\tag{L-90209.12}
\]

Moreover

\[
 \Delta_{\rm bal}'(1)=-\phi'(0)=-\mathbb E\log V>0,
\tag{L-90209.13}
\]

so the conservation root is simple.

### Strict strip separation

There exists a fixed `delta>0` such that

\[
 \boxed{
 \Delta_{\rm bal}(s)\ne0
 \qquad
 (\Re s\ge1-\delta,\ s\ne1).
 }
\tag{L-90209.14}
\]

Proof by contradiction.  If zeros `s_j` had `Re s_j->1`, then:

- if `Im s_j` is bounded, a subsequence converges to a zero on `Re s=1`; by
  (L-90209.12) it converges to `1`, contradicting isolation of the simple root;
- if `|Im s_j|->infinity`, the explicit formula gives uniformly for
  `sigma` in a fixed compact interval around one
  \[
  |\phi(\sigma-1+it)|
  \le\frac{C}{1+|t|}\to0,
  \]
  contradicting `phi(s_j-1)=1`.

Thus the broad continuum policy has a genuine deterministic spectral gap.

This is the exact opposite of `L-90206`, where finitely many logarithmic step
sizes created almost-periodic characteristic zeros with real part tending to
one.

## 7. Why this matters after the frozen-producer refutation

`T-90204` proves that the half-binary/half-ternary producer fails because its
finite-ratio characteristic excites near-critical deterministic resonances.
The ordered policy (L-90209.2) removes precisely that geometric disease:

```text
frozen two-ratio policy:       almost-periodic / no spectral gap / refuted;
ordered broad balanced policy: nonlattice continuum / strict spectral gap.
```

This does **not** prove positivity of the critical arithmetic occupation.  The
reciprocal-zeta/Möbius source remains.  It does show that the new policy is not
pre-refuted by the deterministic mechanism which killed GFEP/BTF.

## 8. Proof boundary

Proved exactly:

1. a concrete quarter-balanced split probability at every finite parent;
2. the selected-child kernel;
3. the exact sliding parent interval and occupation recurrence;
4. the linear-time range-update realization;
5. the continuum child density and Mellin characteristic;
6. uniqueness of the conservation root on `Re s>=1`;
7. existence of a strict deterministic spectral gap for the continuum broad policy.

Still open:

- nonnegativity/subpower negative part of the Möbius occupation for this policy;
- a finite-to-continuum spectral stability theorem strong enough to control the arithmetic source;
- the square-root hinge theorem isolated in `T-90205`;
- RH.