# L-90310 — The Q4 two-stage Q2 cascade cancels every internal curvature exactly

Claim ID: `L-90310`  
Title: Composing the minus and plus Q2 all-pass stages and eliminating their shared root state before taking spectral parts reproduces the direct Q4 block identity exactly; no standalone negative-mass theorem is needed for the internal Q2 outputs  
Status: **PROPOSED COMPLETE EXACT MATRIX/STATE-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `L-90309`; `L-90308`; PR #350 `L-34414`  
Scope: exact Q2-to-Q4 cascade cancellation; finite arithmetic collars and source-specific defect estimates remain separate

## 1. The two complementary Q2 stages

Put

\[
z=2^{-s},\qquad \ell=\log2,
\]

and let `tau -> g_tau` be an arbitrary finite-channel analytic multiplier path. Define

\[
\boxed{
 p=(1+z)g,\qquad
 q=(1-2z)g,
}
\tag{L-90310.1}
\]

and the shared internal root

\[
\boxed{
 a=(1-z)p=(1+z)q=(1-z^2)g.
}
\tag{L-90310.2}
\]

The first, minus-Q2 stage has

```text
base     p=(1+z)g;
root     a=(1-z)p;
output   b=(1-2z)p.
```

The second, plus-Q2 stage is the root-of-unity conjugate and has

```text
base     q=(1-2z)g;
root     b=(1+z)q;
output   c=(1+2z)q=(1-4z^2)g.
```

The identity

\[
(1-2z)(1+z)=(1+z)(1-2z)
\]

shows that the output of the first stage and the root of the second are literally the same path `b`; no interpolation or asymptotic identification is involved.

The final output and direct Q4 input are

\[
\boxed{
 c=(1-4z^2)g,
 \qquad
 a=(1-z^2)g.
}
\tag{L-90310.3}
\]

## 2. The two exact stage identities

Let `K_I(v)` denote the complete Hermitian channel-curvature matrix of the path `v` on the physical block `I`, as in `L-90307`.

Apply the Q2 all-pass identity `L-90309.5` to the first stage:

\[
\boxed{
 K_I(b)+K_I(p)
 =2K_I(a)+K_{I-\ell}(p).
}
\tag{L-90310.4}
\]

Apply its root-of-unity conjugate to the second stage:

\[
\boxed{
 K_I(c)+K_I(q)
 =2K_I(b)+K_{I-\ell}(q).
}
\tag{L-90310.5}
\]

Both are identities of full channel matrices in the independent-frequency block orientation.

## 3. Eliminate the internal root before taking positive or negative parts

Twice (L-90310.4) gives

\[
2K_I(b)=4K_I(a)+2K_{I-\ell}(p)-2K_I(p).
\tag{L-90310.6}
\]

Substitute this into (L-90310.5):

\[
K_I(c)+2K_I(p)+K_I(q)
=4K_I(a)+2K_{I-\ell}(p)+K_{I-\ell}(q).
\tag{L-90310.7}
\]

Now use the tight Q2 output-frame identity `L-90309.8`, first on `I`,

\[
2K_I(p)+K_I(q)
=3K_I(g)+3K_{I-\ell}(g),
\tag{L-90310.8}
\]

and then on `I-ell`,

\[
2K_{I-\ell}(p)+K_{I-\ell}(q)
=3K_{I-\ell}(g)+3K_{I-2\ell}(g).
\tag{L-90310.9}
\]

Substitution into (L-90310.7) cancels the current predecessor reservoir exactly and gives

\[
\boxed{
K_I(c)+3K_I(g)
=4K_I(a)+3K_{I-2\ell}(g).
}
\tag{L-90310.10}
\]

Since `2ell=log4`, this is precisely the direct Q4 source/state identity of `L-90308.9`.

## 4. Why the cancellation order is load bearing

The matrices

\[
K_I(p),\quad K_I(q),\quad K_I(b)
\]

need not be positive semidefinite. Estimating their positive and negative parts stage by stage would introduce artificial losses.

Equation (L-90310.10) proves the correct order:

```text
compose both stages;
retain all cross terms;
cancel the shared root and predecessor reservoir matrices exactly;
only then take positive/negative spectral parts.
```

Consequently, the open item stated in `L-90309`—a separate source-specific negative-mass bound for every intermediate Q2 output—is unnecessary for the two-stage Q4 cascade.

The only spectral defects that can survive in a Q4 recurrence are those of the final declared Q4 input/output/reservoir source matrices, together with finite physical collars and differentiated finite gauges.

## 5. Positive spectral storage after exact cancellation

Apply the positive-mass functional

\[
p(H)=\operatorname{tr}H_+
\]

only to (L-90310.10). Subadditivity and `p(-H)=delta(H)` give

\[
\boxed{
 p(K_I(c))
 \le
 4p(K_I(a))
 +3p(K_{I-2\ell}(g))
 +3\delta(K_I(g)).
}
\tag{L-90310.11}

After the critical Q4 normalization by the gain four,

\[
\boxed{
 \frac14p(K_I(c))
 \le
 p(K_I(a))
 +\frac34p(K_{I-\log4}(g))
 +\frac34\delta(K_I(g)).
}
\tag{L-90310.12}

A storage version retaining the current reservoir on the left follows directly from `L-90307.10`; it has coefficient one and pays only the negative masses of the final declared states, not of the cancelled Q2 internals.

## 6. Interaction with the zero-bare compact source

For the actual compact Jordan path, `L-90308` identifies

\[
a=(1-z^2)g,
\qquad
c=(1-4z^2)g,
\qquad
d=(1-z^2)c.
\]

The zero-bare path `d` carries the hard compact innovation and has normalized negative mass `O(1/log n)` by `L-90304/L-90305`. Its stable causal inverse reconstructs `c` with geometric predecessor states.

Equation (L-90310.10) shows that the Q2 cascade introduces no additional same-scale dynamic source beyond this direct Q4 dictionary.

## 7. Proof boundary

Closed exactly here:

1. the two complementary Q2 source stages;
2. identification of the shared internal root;
3. both independent-frequency matrix stage identities;
4. exact elimination of every internal Q2 curvature;
5. recovery of the direct Q4 matrix state law;
6. removal of the need for intermediate-output defect estimates;
7. the final-state positive spectral-mass inequality.

Still open:

1. source-specific treatment of the final root/base reservoir negative mass, or cancellation of it against the corrected zero-bare state;
2. exact insertion of finite collars and strictly delayed differentiated gauges;
3. the globally iterated QIDR recurrence;
4. RH.
