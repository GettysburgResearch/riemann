# L-90308 — Exact Q4 source/state dictionary for the compact Jordan path

Claim ID: `L-90308`  
Title: The compact main-pole Jordan path is exactly the output of the Q4 Euler–Blaschke colligation; its input, reservoir state and zero-bare relative source are fixed parameter-independent filters of one path, so no derivative gauge is omitted from the all-pass curvature telescope  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/STATE-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: PR #325 `L-32406/L-32415`; PR #339 `L-33804`; `L-90304`, `L-90306`, `L-90307`  
Scope: exact source typing for the principal Q4 all-pass stage; the low-pass/root companion and finite physical collars remain separate

## 1. Four fixed source filters

Put

\[
x=4^{-s},
\qquad
B_0(s)=\frac1{\zeta(s)},
\]

and define

\[
\boxed{
 h=(1-x)g,
 \qquad
 c=(1-4x)g,
 \qquad
 d=(1-x)c=(1-x)(1-4x)g.
}
\tag{L-90308.1}

For the zeroth path value `g_0=B_0`, these are respectively

```text
h_0=(1-4^-s)/zeta(s)                 root source;
c_0=(1-4^(1-s))/zeta(s)=B_sharp(s)  compact main-pole source;
d_0=(1-4^-s)(1-4^(1-s))/zeta(s)     zero-bare source.
```

The last source is exactly `b_diamond` of `L-90304`.

No differentiation has yet been taken; all four relations are finite multiplier identities.

## 2. Exact centered Q4 colligation

Let

\[
z=s-\frac12,
\qquad L=\log4.
\]

Then

\[
e^{-Lz}=2x.
\]

For the Q4 Euler–Blaschke colligation of PR #339,

\[
\phi(z)
=\frac{\frac12-e^{-Lz}}
       {1-\frac12e^{-Lz}},
\qquad
R(z)=\frac{\sqrt3/2}
          {1-\frac12e^{-Lz}},
\tag{L-90308.2}
\]

one has exactly

\[
\boxed{
2\phi(z)=\frac{1-4x}{1-x}=E_4(s),
\qquad
R(z)=\frac{\sqrt3/2}{1-x}.
}
\tag{L-90308.3}

Consequently, for **every** analytic multiplier path `tau -> g_tau`, define `h_tau,c_tau,d_tau` by the fixed filters (L-90308.1).  Then

\[
\boxed{
 c_\tau=2\phi\,h_\tau,
 \qquad
 R h_\tau=\frac{\sqrt3}{2}g_\tau,
 \qquad
 d_\tau=(1-x)c_\tau.
}
\tag{L-90308.4}

Every operator in (L-90308.4) is independent of `tau`.  Therefore all first and second Jordan jets pass through the same state-space identity with no differentiated-filter remainder.

This is the exact source dictionary required by `L-90306/L-90307`.

## 3. Instantiate with the actual compact Jordan path

Let

\[
 c_\tau=K_{\sharp,\tau}
 =b_\sharp*J_{\sharp,\tau}
\tag{L-90308.5}
\]

be the compact-source Jordan path of PR #345 and `L-90304`.  Define

\[
\boxed{
 g_\tau=\frac{c_\tau}{1-4x},
 \qquad
 h_\tau=\frac{1-x}{1-4x}c_\tau,
 \qquad
 d_\tau=(1-x)c_\tau.
}
\tag{L-90308.6}

These are well-defined as formal/analytic Dirichlet multipliers in the declared half-plane and satisfy (L-90308.4) identically.

At `tau=0`,

\[
 c_0=b_\sharp=(1-4x)\mu,
\qquad
 g_0=\mu,
\qquad
 h_0=(1-x)\mu,
\qquad
 d_0=b_\diamond.
\tag{L-90308.7}

Moreover, because the filters are fixed,

\[
\boxed{
 \dot c_0=q_\sharp,
 \quad
 \dot d_0=(1-x)q_\sharp,
 \quad
 \ddot d_0=(1-x)t_\sharp.
}
\tag{L-90308.8}

Thus the first zero-bare source jet is exactly the hard compact aligned innovation used in `L-90304`, and its second jet is exactly the filtered second current whose summatory function is `O(X)` there.

No own-current versus externally filtered-current ambiguity remains in this dictionary.

## 4. Exact matrix curvature conservation

Let `V_tau` be any finite vector of paths to which the same four fixed filters are applied componentwise.  `L-90307.6` and (L-90308.4) give

\[
K_I(\phi h)+K_I(Rh)
=K_I(h)+K_{I-L}(Rh).
\]

Multiply by the exact gains in (L-90308.4):

\[
\boxed{
 K_I(c)+3K_I(g)
 =4K_I(h)+3K_{I-L}(g).
}
\tag{L-90308.9]

(The closing bracket in the tag is typographical only.)

This is an identity of complete Hermitian channel-curvature matrices.  It retains every independent-frequency cross term.  Taking traces recovers the scalar Q4 reservoir identity quoted on the corrected Q2/Q4 branches.

Equation (L-90308.9) is the principal coefficient-one source/state conservation law:

```text
current compact output + current reservoir
 = root input + predecessor reservoir.
```

## 5. The zero-bare output is a stable causal difference of the compact output

On the critical line,

\[
|x|=\frac12.
\]

Therefore

\[
\boxed{
 |1-x|\ge\frac12,
 \qquad
 \left\|(1-x)^{-1}\right\|_{L^2\to L^2}\le2.
}
\tag{L-90308.10}

The inverse has the causal expansion

\[
\boxed{
 c_\tau=(1-x)^{-1}d_\tau
 =\sum_{r\ge0}x^r d_\tau.
}
\tag{L-90308.11}

In critical physical coordinates, `x^r` is a delay by `r log4` with amplitude `2^-r`.  Hence the zero-bare path is not merely algebraically related to the compact output: it is its stable innovation coordinate, and reconstructing the compact path introduces only a positive geometric predecessor state.

For any all-line channel curvature matrix, contraction monotonicity of positive and negative spectral masses gives

\[
\boxed{
 p(K(c))\le4p(K(d)),
 \qquad
 \delta(K(c))\le4\delta(K(d)).
}
\tag{L-90308.12}

On local blocks the same reconstruction is represented by the one-pole causal state (L-90308.11); its tail is geometric and belongs to the declared predecessor-state ledger rather than to a same-scale error.

## 6. What this closes in QIDR

The principal Q4 all-pass stage no longer has an unspecified source map.  For the actual compact Jordan path:

```text
input path       h=(1-x)c/(1-4x);
compact output   c=K_sharp;
reservoir state  (sqrt3/2)g=(sqrt3/2)c/(1-4x);
zero-bare path   d=(1-x)c;
```

and the exact block law is (L-90308.9).

`L-90304/L-90305` supply the lower-order inertia defect for the zero-bare source, while (L-90308.11) supplies its causal reconstruction of the compact output.  The remaining source work is now the root/low-pass side of the finite Q2/Q4 cascade and the explicit insertion of the already-classified finite collars and derivative gauges.

## 7. Proof boundary

Closed exactly here:

1. the principal root/compact/reservoir/zero-bare source dictionary;
2. parameter-independent placement of the complete compact Jordan path;
3. exact typing of its first and second zero-bare jets;
4. the complete matrix-curvature conservation identity;
5. stable causal reconstruction from zero-bare to compact path;
6. all-line positive/negative spectral-mass transfer.

Still open:

1. substitution of the root/low-pass Q2 companion state in the same metric;
2. finite local-block realization of every geometric predecessor state and collar;
3. closure of the global QIDR recurrence;
4. RH.
