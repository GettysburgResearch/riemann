# L-90412 — All bulk additive modes of the Q4 innovation are unconditionally at PIG scale

Claim ID: `L-90412`  
Title: The exact compact-Q4 prefix is sparse enough that every additive residue outside a square-root major arc contributes only `O(log N)` after PIG normalization  
Status: **PROPOSED COMPLETE UNCONDITIONAL REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90411`; PR #362 compact innovation; elementary Chebyshev bound  
Scope: complete carry-position field at one integer parent; an adapter to any smaller aligned physical bank is by restriction, not an asserted global Q4 recurrence

## 1. Exact prefix coefficient of the compact innovation

Let \(i_\circ\) be the compact innovation source of PR #362 and put

\[
c_\circ=\mathbf1*i_\circ.
\]

Writing \(L=\log4\), direct Dirichlet-series algebra gives

\[
\boxed{
c_\circ(m)
=
\Lambda(m)
-4\mathbf1_{4\mid m}\Lambda(m/4)
+3L\sum_{r\ge1}\mathbf1_{m=4^r}.
}
\tag{L-90412.1}
\]

Indeed its Dirichlet series is

\[
\boxed{
\sum_{m\ge1}\frac{c_\circ(m)}{m^s}
=
(1-4^{1-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
+
3(\log4)\frac{4^{-s}}{1-4^{-s}}.
}
\tag{L-90412.2}
\]

Thus \(c_\circ\) is supported on prime powers, four times prime powers,
and the four-adic tower.

## 2. Elementary coefficient energy

The Chebyshev estimate \(\psi(X)\ll X\) implies

\[
\sum_{m\le X}\Lambda(m)^2
\le
(\log X)\psi(X)
\ll X\log(2X).
\tag{L-90412.3}
\]

Using \(|u+v+w|^2\le3(|u|^2+|v|^2+|w|^2)\) in
(L-90412.1), together with the shifted copy and the logarithmically many
four-adic atoms, yields

\[
\boxed{
\sum_{m\le N}|c_\circ(m)|^2
\ll N\log(2N).
}
\tag{L-90412.4}
\]

No PNT error term, zero-free region, or RH input is used.

## 3. Bulk additive residues

Let \(Q_{\circ,N}\), \(S_a\) be the carry field and sine sums of
`L-90411`, formed from \(c_\circ\). Define

\[
d_N(a)=\min(a,N-a).
\]

For \(1\le d_N(a)\le N/2\),

\[
\sin\frac{\pi a}{N}
\ge \frac{2d_N(a)}{N}.
\tag{L-90412.5}
\]

Also, unnormalized finite Fourier Parseval gives

\[
\sum_{a=0}^{N-1}
\left|
\sum_{m=1}^{N-1}c_\circ(m)e^{2\pi iam/N}
\right|^2
=
N\sum_{m=1}^{N-1}|c_\circ(m)|^2.
\tag{L-90412.6}
\]

Since \(S_a\) is the imaginary part of this transform,

\[
\sum_{a=1}^{N-1}|S_a|^2
\le
N\sum_{m=1}^{N-1}|c_\circ(m)|^2.
\tag{L-90412.7}
\]

For any \(1\le K\le N/2\), the part of (L-90411.8) with
\(d_N(a)\ge K\) therefore satisfies

\[
\boxed{
\frac1{N^2}
\sum_{\substack{1\le a<N\\d_N(a)\ge K}}
\frac{|S_a|^2}{\sin^2(\pi a/N)}
\ll
\frac{N^2\log(2N)}{K^2}.
}
\tag{L-90412.8}
\]

Taking

\[
K=\lceil\sqrt N\rceil
\]

gives

\[
\boxed{
\mathcal E_{\rm bulk}(N)
\ll N\log(2N).
}
\tag{L-90412.9}
\]

After the natural PIG normalization by \(N\),

\[
\boxed{
\frac{\mathcal E_{\rm bulk}(N)}N
\ll\log(2N).
}
\tag{L-90412.10}
\]

## 4. The exact reduced gate

Let \(Q_{\rm major}\) contain the mean and the residue classes

\[
d_N(a)<\sqrt N.
\]

There are at most \(2\sqrt N+O(1)\) nonzero such residue classes. On the
full carry circle, Fourier orthogonality gives

\[
\|Q_{\circ,N}\|_2^2
=
\|Q_{\rm major}\|_2^2
+O(N\log(2N)).
\tag{L-90412.11}
\]

On a restricted balanced bank, the safe sufficient inequality is

\[
\|Q_{\circ,N}\|_{L^2(\mathrm{bal})}^2
\le
2\|Q_{\rm major}\|_{L^2(\mathrm{bal})}^2
+O(N\log(2N)).
\tag{L-90412.12}
\]

Consequently a polynomial bound for the major-residue energy implies PIG;
the entire bulk is already unconditional.

This reduces the positive product Gram from all \(N\) additive coordinates to:

```text
one mean coordinate
+ at most O(sqrt(N)) low additive residue classes.
```

The square-root major arc is not claimed optimal. The point is qualitative:
the unresolved PIG mass is concentrated near the singular Green modes, not
spread through the complete Gram.
