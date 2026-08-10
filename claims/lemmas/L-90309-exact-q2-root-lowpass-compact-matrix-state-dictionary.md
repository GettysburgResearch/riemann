# L-90309 — Exact Q2 root/low-pass/compact matrix state dictionary

Claim ID: `L-90309`  
Title: The scale-two root, low-pass and compact outputs form one exact critical-Haar/all-pass matrix colligation; all independent-frequency cross terms are retained and the compact/low-pass pair is a tight coefficient-one frame of the base source and its predecessor  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/HILBERT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; `L-90307`; elementary two-tap filter algebra  
Scope: exact Q2 companion state required by QIDR; no arithmetic negative-mass estimate or RH conclusion

## 1. Four scale-two paths

Put

\[
z=2^{-s},
\qquad \ell=\log2,
\]

and let `tau -> g_tau` be any finite-channel analytic multiplier path.  Define by fixed parameter-independent filters

\[
\boxed{
 p_\tau=(1+z)g_\tau,
 \qquad
 r_\tau=(1-z)g_\tau,
 \qquad
 c_{2,\tau}=(1-2z)g_\tau.
}
\tag{L-90309.1}

The names are:

```text
p    low-pass / plus-Haar output;
r    root / minus-Haar output;
c2   scale-two compact output;
g    reservoir/base path.
```

At `g_0=1/zeta`, all three finite factors have their zeros on the boundary lines, so each output retains every nontrivial zeta-zero pole.

## 2. Q2 all-pass colligation

In the centered variable

\[
w=s-\frac12
\]

one has

\[
e^{-\ell w}=\sqrt2\,z.
\]

Take the all-pass/state pair

\[
\phi_2(w)
=\frac{2^{-1/2}-e^{-\ell w}}
       {1-2^{-1/2}e^{-\ell w}},
\qquad
R_2(w)
=\frac{2^{-1/2}}
       {1-2^{-1/2}e^{-\ell w}}.
\tag{L-90309.2}

Then exactly

\[
\boxed{
\sqrt2\,\phi_2(w)=\frac{1-2z}{1-z},
\qquad
R_2(w)=\frac{1}{\sqrt2(1-z)}.
}
\tag{L-90309.3}

Consequently

\[
\boxed{
 c_{2,\tau}=\sqrt2\,\phi_2 r_\tau,
 \qquad
 R_2 r_\tau=\frac1{\sqrt2}g_\tau.
}
\tag{L-90309.4}

Every filter is independent of `tau`; all source/current/second-current jets therefore obey the same colligation.

## 3. Exact Q2 curvature matrix identity

Apply `L-90307.6` with delay `ell` to the channel path `r_tau` and multiply by the gains in (L-90309.4).  One obtains the exact independent-frequency matrix identity

\[
\boxed{
K_I(c_2)+K_I(g)
=2K_I(r)+K_{I-\ell}(g).
}
\tag{L-90309.5}

This is an identity of complete Hermitian channel curvatures, not only of scalar traces.

It has the state interpretation

```text
compact output + current reservoir
 = twice the root input + predecessor reservoir.
```

## 4. Exact critical-Haar identity

The low-pass and root multipliers satisfy, for independent critical-line frequencies `t,u`,

\[
\begin{aligned}
&(1+z_t)(1+z_{-u})+(1-z_t)(1-z_{-u})\\
&\qquad=2+2z_tz_{-u}
=2+e^{-i\ell(t-u)},
\end{aligned}
\tag{L-90309.6}

because `z_t z_-u=2^-1 e^-i ell(t-u)`.

Multiplication by the physical block kernel converts the second term into the predecessor block.  Polarizing channel by channel gives

\[
\boxed{
K_I(p)+K_I(r)
=2K_I(g)+K_{I-\ell}(g).
}
\tag{L-90309.7]

(The closing bracket in the tag is typographical only.)

Thus the critical-Haar split is already a lossless block state law; no diagonal-frequency approximation is involved.

## 5. Tight compact/low-pass output frame

Eliminate `K_I(r)` between (L-90309.5) and (L-90309.7).  From (L-90309.7),

\[
K_I(r)=2K_I(g)+K_{I-\ell}(g)-K_I(p).
\]

Substitution in (L-90309.5) yields

\[
\boxed{
2K_I(p)+K_I(c_2)
=3K_I(g)+3K_{I-\ell}(g).
}
\tag{L-90309.8}

This is the exact matrix version of the Q2 tight output frame.  In normalized direct-sum language,

\[
\left(\sqrt{\frac23}p,\frac1{\sqrt3}c_2\right)
\]

has the same complete channel-curvature matrix as

\[
(g,g_{\rm predecessor}).
\]

The identity remains true after positive carry-position integration, independent-frequency physical localization, and finite Toeplitz compression because it is already a polarized multiplier identity.

## 6. Positive spectral storage consequence

Apply `p(H)=tr(H_+)` and `delta(H)=tr(H_-)` only after the exact internal state `r` has been eliminated.

From (L-90309.8), subadditivity gives

\[
\boxed{
 p(2K_I(p)+K_I(c_2))
 \le 3p(K_I(g))+3p(K_{I-\ell}(g)).
}
\tag{L-90309.9}

For the individual output masses, (L-90307.9) gives

\[
\boxed{
\begin{aligned}
2p(K_I(p))+p(K_I(c_2))
&\le3p(K_I(g))+3p(K_{I-\ell}(g))\\
&\quad+2\delta(K_I(p))+\delta(K_I(c_2)).
\end{aligned}}
\tag{L-90309.10}

Hence the only obstruction to a coefficient-one positive-storage recursion through the Q2 split is the negative spectral mass of its two actual outputs.  No root-state or filter cross-term remains.

## 7. Relation to Q4 and the zero-bare source

Since

\[
1-4z^2=(1-2z)(1+2z),
\]

the Q4 compact factor is a two-stage scale-two cascade, the second stage being the same construction after the root-of-unity substitution `z -> -z`.  Applying (L-90309.5)--(L-90309.8) twice and cancelling the internal root states reproduces the Q4 source/state identity of `L-90308`.

The zero-bare compact difference used in `L-90304` is a fixed difference of the Q4 compact output, so `L-90305/L-90307` transport its `O(1/log n)` normalized negative mass through every finite Q2/Q4 synthesis once the output source is matched.

## 8. Proof boundary

Closed exactly here:

1. the Q2 root/low-pass/compact source dictionary;
2. the Q2 all-pass matrix curvature identity;
3. the critical-Haar matrix identity;
4. elimination of the internal root state;
5. the tight compact/low-pass output frame;
6. the positive-spectral-storage inequality after exact cancellation;
7. the two-stage Q4 cascade interpretation.

Still open:

1. a source-specific lower-order negative-mass theorem for every Q2 output actually retained in the final cascade, or an exact cancellation reducing them all to the zero-bare Q4 defect;
2. finite collars and differentiated source gauges;
3. the globally closed QIDR recurrence;
4. RH.
