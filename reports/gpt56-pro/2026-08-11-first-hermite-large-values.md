# First-Hermite large-value continuation — 2026-08-11

## Frozen base

```text
repository: gfreund123/riemann
base PR:    #385
base head:  ea2d7c26c1fd3a58c3e31609cb2411ea0c0fd20a
branch:     research/gpt56-pro/385-first-hermite-large-values
```

## Result

The first-Hermite prime channel is

\[
\mathcal P(q,x)
=
\frac{1}{2\sqrt\pi q^{3/2}}
\Re\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\left(1-\frac{(\log n)^2}{2q}\right)
e^{-(\log n)^2/(4q)}
n^{ix}.
\]

A negative complete scalar at height \(x\asymp X\) forces the unnormalised Dirichlet polynomial to have size \(\gg\log X\).

The coefficient square is only

\[
\sum_n|b_q(n)|^2=q+O(\sqrt q).
\]

Grouping prime powers by prime gives independent bounded blocks in the Bohr lift. Bernstein moments, Gaussian truncation at \(n\le e^{8q}\), and Montgomery–Vaughan applied to the \(k\)-th power yield

\[
\frac{|E_q(X)|}{X}
\le
C\left[
\frac{Ck(q+k)}{(\log X)^2}
\right]^k
\]

whenever \(8kq\le\tfrac12\log X\).

Optimizing \(k\) gives

\[
|E_q(X)|
\le
CX\exp\left[-c\frac{\log X}{q+1}\right].
\]

Consequently, for every fixed \(\varepsilon>0\),

\[
\left|
\left\{
x\in[X,2X]:
\exists\,1\le q\le(\log X)^{1-\varepsilon},
\ q\in\mathbb N,\ 
\mathcal M(q,x)<0
\right\}
\right|
\le
X e^{-c_\varepsilon(\log X)^\varepsilon}.
\]

Thus the unresolved pointwise sign is confined to an exponentially sparse resonance set. This is much larger simultaneous \(q\)-coverage than the pointwise \(4\log\log X\) wedge, but it is an almost-everywhere theorem and does not prove RH.

## New firewall

At moment order \(2k\), the transfer requires \(kq\ll\log X\). A terminal pair at depth \(y<1/2\) contributes at most \(e^{2kqy^2}=o(X)\) at the full budget. Therefore arbitrarily strong average large-value estimates of this support type remain compatible with one isolated off-line pair.

The next target is an inverse theorem for the exceptional set: large value \(\gg\log X\) must force rigid alignment among many prime blocks, and that alignment must then be excluded at a zeta-zero carrier.

## Verification

```text
PASS_FIRST_HERMITE_LARGE_VALUES
```

The replay checks finite identities and scale laws only.
