# L-99702 — A reversible prime-birth/death network gives the exact cross-source Green identity for SHARP

Claim ID: `L-99702`  
Status: **PROVED EXACT FINITE NETWORK THEOREM**  
Created: 2026-08-20  
Depends on: `L-99700`, `L-99701`, `R-99700`  
RH status: **not assumed**

The divisor-owner chain of `L-99701` moves only downward and is degenerate on squarefree source. The minimal repair is to add its detailed-balance reverse edges.

Fix `X>=1`. Let the vertices be the integers `1<=n<=X`. For every prime power `q` and every `nq<=X`, put an edge labelled `(n,q)` with conductance

\[
\boxed{
c_X(n,q)=\frac{\Lambda_g(q)g(n)}{nq}.}
\tag{L-99702.1}
\]

Define the positive vertex measure

\[
\pi(n)=\frac{g(n)}n.
\tag{L-99702.2}
\]

The birth and death rates

\[
b(n,nq)=\frac{\Lambda_g(q)}q,
\qquad
d(nq,n)=\frac{\Lambda_g(q)g(n)}{g(nq)}
\tag{L-99702.3}
\]

satisfy exact detailed balance

\[
\boxed{
\pi(n)b(n,nq)=c_X(n,q)=\pi(nq)d(nq,n).
}
\tag{L-99702.4}
\]

Thus all source integers, including distinct squarefree integers, live in one prescribed reversible network. No post-hoc Gram or unknown sign enters its definition.

For functions `F,G` on the vertices, define

\[
\mathcal E_X(F,G)
=\frac12\sum_{nq\le X}c_X(n,q)
 [F(n)-F(nq)][G(n)-G(nq)],
\tag{L-99702.5}
\]

where distinct prime-power labels are retained as distinct edges. Let `mathcal L_X` be the corresponding positive Laplacian, so

\[
\langle\mathcal L_XF,G\rangle_{\pi}=\mathcal E_X(F,G).
\tag{L-99702.6}
\]

Put `f=beta/g` as in `L-99701`. The downward owner identity gives the exact formula

\[
\boxed{
(\mathcal L_Xf)(n)
=2(\log n)f(n)
+\sum_{q\le X/n}\frac{\Lambda_g(q)}q
 [f(n)-f(nq)].
}
\tag{L-99702.7}
\]

The second term is the genuinely new cross-source prime-birth contribution. It is nonzero on the squarefree sector and is exactly what the divisor-only martingale omitted.

Define the normalized SHARP potential

\[
\Phi_X(n)=\mathbf1_{n\le X}
\frac{\sqrt n}{\sqrt X}T(X/n)
=\mathbf1_{n\le X}\left(4-3\sqrt{n/X}\right).
\tag{L-99702.8}
\]

Then the live scalar is one exact network pairing:

\[
\boxed{
\frac{h(X)}{\sqrt X}
=\sum_{n\le X}\pi(n)f(n)\Phi_X(n)
=\langle f,\Phi_X\rangle_{\pi}.
}
\tag{L-99702.9}
\]

Let

\[
\mathfrak R_X(n)
=(\mathcal L_Xf)(n)-2(\log X)f(n).
\tag{L-99702.10}
\]

Combining (L-99702.6), (L-99702.9), and (L-99702.10) gives the exact ground-state Green identity

\[
\boxed{
2\log X\,\frac{h(X)}{\sqrt X}
=\mathcal E_X(f,\Phi_X)
-\langle\mathfrak R_X,\Phi_X\rangle_{\pi}.
}
\tag{L-99702.11}
\]

This is the first exact identity in the route that sees both:

```text
within-integer logarithmic ownership;
cancellation between distinct squarefree source integers.
```

There is also a useful positivity audit. The local values of `f` are

```text
p != 67:  1, -1, 0, 0, ...

p  = 67:  1, -1, 1/3, 0, 0, ... .
```

Since `Phi_X(n)>=Phi_X(nq)>=0`, a finite local case check gives, edge by edge,

\[
\boxed{
[f(n)-f(nq)]
[f(n)\Phi_X(n)-f(nq)\Phi_X(nq)]\ge0.
}
\tag{L-99702.12}
\]

Hence

\[
\boxed{\mathcal E_X(f,f\Phi_X)\ge0.}
\tag{L-99702.13}
\]

Equation (L-99702.13) is a genuine common Schur/Green positivity statement. It controls the parity trace channel. It does not, by itself, orient the signed pairing (L-99702.9); the remaining orientation is isolated exactly by (L-99702.11).