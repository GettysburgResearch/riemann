# L-99270 — Zero-free positive smoothing and subpower negative mass both replace pointwise SHARP Harnack positivity

Claim ID: `L-99270`  
Status: **PROVED EXACT CONDITIONAL CONSUMER THEOREM**  
Created: 2026-08-20  
Frozen scalar source: PR #647 at `306d1c66fe4e848efda0bd78b5475aeeed3d5563`  
RH status: **not assumed; conclusion under either stated producer**

Put

\[
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1},
\]

\[
\Psi(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}T(x/n),
\]

and

\[
h(x)=\mathfrak H_{67}(x)
=\Psi(x)-67^{-1/2}\Psi(x/67),
\qquad h(x)=0\quad(0<x<1).
\tag{L-99270.1}
\]

For `Re(s)>1/2`, finite/absolute Fubini gives

\[
\boxed{
F(s):=\int_1^\infty h(x)x^{-s-1}\,dx
=\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-99270.2}
\]

The pointwise tail `h(x)>=0` is sufficient but stronger than the analytic
consumer requires.  The following two strictly weaker producers are also
conclusion-complete.

## 1. A zero-free positive logarithmic box

For any fixed real `A>1`, define the positive multiplicative box smoothing

\[
(\mathcal S_Ah)(X)
=\int_1^Ah(X/u)\,\frac{du}{u}
=\int_{X/A}^{X}h(t)\,\frac{dt}{t},
\tag{L-99270.3}
\]

using zero extension below `1`.  Its Mellin multiplier is

\[
K_A(s)=\int_1^A u^{-s}\frac{du}{u}
=\frac{1-A^{-s}}s,
\tag{L-99270.4}
\]

with the removable value `K_A(0)=log A`.  If `Re(s)>0`, then

\[
|A^{-s}|=A^{-\Re s}<1,
\]

so

\[
\boxed{K_A(s)\ne0\qquad(\Re s>0).}
\tag{L-99270.5}
\]

Initially for `Re(s)>1/2`,

\[
\int_1^\infty(\mathcal S_Ah)(X)X^{-s-1}\,dX
=K_A(s)F(s).
\tag{L-99270.6}
\]

Assume merely that

\[
\boxed{(\mathcal S_Ah)(X)\ge0\quad(X\ge X_0)}
\tag{L-99270.7}
\]

for some finite `X_0`.  Removing the compact interval `[1,X_0]` changes the
Mellin transform by an entire function.  The remaining density is
nonnegative.  If it vanishes identically, its transform is zero and the full
smoothed transform is already entire after the compact correction.  Otherwise
the specialized Landau theorem of `L-99272` applies.  In either case,
(L-99270.5) shows that every zero `rho` with `Re(rho)>1/2` would produce a
nonremovable pole at `s=rho-1/2`.  Hence (L-99270.7) implies RH.

The choice `A=67` is source-aligned:

\[
\boxed{
\int_{X/67}^{X}h(t)\frac{dt}{t}\ge0
\text{ eventually}
\quad\Longrightarrow\quad RH.
}
\tag{L-99270.8}
\]

This criterion allows arbitrarily many pointwise negative cells, provided the
one-octave logarithmic balance remains nonnegative.

## 2. Subpower logarithmic negative mass

Write `h=h_+-h_-`, where `h_+,h_- >=0`, and define

\[
M_-(X)=\int_1^X h_-(t)\frac{dt}{t}.
\tag{L-99270.9}
\]

Assume

\[
\boxed{
M_-(X)=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{L-99270.10}
\]

For every compact subset of `Re(s)>0`, choose `0<epsilon<Re(s)` uniformly.
Integration by parts, or a decomposition into multiplicative blocks, gives
absolute and locally uniform convergence of

\[
N(s)=\int_1^\infty h_-(x)x^{-s-1}\,dx
\tag{L-99270.11}
\]

throughout `Re(s)>0`.  Thus `N` is holomorphic there.

For `Re(s)>1/2`,

\[
\int_1^\infty h_+(x)x^{-s-1}\,dx=F(s)+N(s).
\tag{L-99270.12}
\]

The left side is the Mellin transform of a nonzero nonnegative density.  The
right side is analytic on every positive real point and has every off-line
reciprocal-zeta pole of `F`, because addition of the holomorphic function `N`
cannot remove a pole.  `L-99272` therefore gives

\[
\boxed{(L\text{-}99270.10)\Longrightarrow RH.}
\tag{L-99270.13}
\]

An equivalent `67`-adic sufficient condition is: if

\[
N_k=\int_{67^k}^{67^{k+1}}h_-(t)\frac{dt}{t}
\]

satisfies `N_k=O_epsilon(67^(epsilon k))` for every `epsilon>0`, then RH.

## 3. Logical relation of the producers

```text
pointwise h>=0 eventually
        => logarithmic-box positivity for every A>1
        => one zero-free smoothed producer;

pointwise h>=0 eventually
        => M_-(X)=O(1)
        => subpower negative-mass producer.
```

Neither converse is used or asserted.  The two new criteria are genuine
weakenings of the T-99250 pointwise tail and do not import a row, Hall,
Volterra, score, capacity, or prime-square theorem.
