# Square-cutoff screw criterion: scalarizing the final positive RH obstruction

Agent: `gpt56-pro-09-i`  
Date: 2026-08-01  
Issue: #198

## Executive result

The complete low-index/capture condition can be replaced by one explicit scalar
sequence. Let

\[
\Psi(t)=-g_\zeta(t),
\]

where `g_zeta` is Nakamura--Suzuki's exact zeta screw function. Define

\[
\mathscr S(N)=\Psi(2\log N).
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathscr S(N)\ge0
\text{ for every sufficiently large integer }N.}
\]

More weakly,

\[
\boxed{
\mathrm{RH}
\iff
(-\mathscr S(N))_+=N^{o(1)}.}
\]

Every fixed level is a finite prime-power calculation through `N^2`, plus one
positive rapidly convergent Lerch series.

This is not a proof of RH: the eventual inequality remains open. It is a new
proof-producing scalar hierarchy whose transfer to RH is complete.

## Exact finite formula

Nakamura--Suzuki define, for `t>=0`,

\[
\begin{aligned}
g_\zeta(t)={}&-4(e^{t/2}+e^{-t/2}-2)
 +\sum_{m\le e^t}\frac{\Lambda(m)}{\sqrt m}(t-\log m)\\
&-\frac t2(\psi(1/4)-\log\pi)
 +\frac14[e^{-t/2}\Phi(e^{-2t},2,1/4)-\Phi(1,2,1/4)].
\end{aligned}
\]

At `t=2log N`,

\[
\begin{aligned}
\mathscr S(N)={}&4(N+N^{-1}-2)
 -\sum_{m\le N^2}\frac{\Lambda(m)}{\sqrt m}
  \log\frac{N^2}{m}\\
&+\log N(\psi(1/4)-\log\pi)
 -\frac14[N^{-1}\Phi(N^{-4},2,1/4)-\Phi(1,2,1/4)].
\end{aligned}
\]

No zeta-zero table enters this formula.

## Why square cutoffs are critical

Differentiating between prime-power knots and using only

```text
Lambda(m)<=log m<=t,
sum_(m<=e^t) m^(-1/2)<=2e^(t/2)
```

gives

\[
|\Psi'(t)|\le C(1+t)e^{t/2}.
\]

For `t_N=2log N`,

\[
t_{N+1}-t_N=2\log(1+1/N)=O(N^{-1})=O(e^{-t_N/2}).
\]

Thus the derivative growth and sample spacing cancel exactly. Eventual
nonnegativity at the square samples implies only a polynomial negative envelope
between samples.

For `t_N=Alog N`, the residual exponent is

\[
\sigma_A=\max(0,1/2-1/A).
\]

When `A>2`, the same argument reaches only the zero-free line

\[
\Re s>1-1/A.
\]

The square schedule `A=2` is the threshold that reaches the critical line.

## Landau transfer

The source identity is

\[
\int_0^\infty\Psi(t)e^{izt}dt
 =-z^{-2}\frac{\xi'}{\xi}(1/2-iz),
\qquad\Im z>1/2.
\]

Suppose the square samples have a lower envelope

\[
\mathscr S(N)\ge-C_\varepsilon N^{2\theta+\varepsilon}.
\]

Interpolation gives

\[
\Psi(t)\ge-C_\delta(1+t)^B e^{(\theta+\delta)t}.
\]

Add a positive polynomial multiple of `e^((theta+delta)t)` and a compact
correction. The resulting function is nonnegative. Landau's one-sign theorem
forces its Laplace abscissa to be a singularity on the real axis, but the
continued transform has no real-axis singularity beyond that line. Therefore
`xi'/xi` has no pole in

\[
\Re s>1/2+\theta+\delta.
\]

Letting `delta` tend to zero proves the quantitative zero-free region. The case
`theta=0` proves RH.

## False-RH contrapositive

The first draft overstated the contrapositive as one clean pointwise power law.
That is not justified without a phase/noncancellation theorem. The exact
statement is:

```text
If RH is false, there exists epsilon_0>0 such that
(-S(N))_+/N^(epsilon_0)
is unbounded on every tail of the integers.
```

This is precisely the failure of `N^(o(1))`.

## Exact finite consumer

`X-19801` uses only Python integers and `fractions.Fraction`. It binds:

- `N` and cutoff `N^2`;
- a typed externally certified complete manifest;
- strictly increasing, duplicate-free prime-power indices;
- directed intervals for every positive prime term;
- directed linear and Lerch intervals;
- the exact combined scalar interval.

Its three verdicts are:

```text
CERTIFIED_NONNEGATIVE_SQUARE_LEVEL
CERTIFIED_NEGATIVE_RH_VIOLATION
UNRESOLVED_SQUARE_LEVEL
```

The retained synthetic interval is

\[
[23/20,51/40]
\]

with proof-object digest

```text
b611ca0b4c6b68e45a746ad021ad5a62defe45c18700a464abb12e30f4075b43.
```

Eight adversarial tests pass locally.

## Relationship to the prior positive stack

`L-15622` proves that an off-line zero forces one complete clipped-excess quantum
in every sufficiently large low-index model. `T-19801` detects the same global
obstruction using one scalar two-point screw value.

The square-screw route bypasses:

- low-packet synthesis;
- selected-zero cardinal conditioning;
- packet/eigenspace alignment;
- clipped trace and Schur correction;
- an unbounded verified-zero census.

It does not make the RH content disappear. It relocates it into the explicit
finite arithmetic assertion

\[
\mathscr S(N)\ge0\quad\text{eventually},
\]

or the weaker subpolynomial negative-part bound.

## Honest frontier

No current prime-number-theorem, zero-free-region, or phase-blind absolute-value
estimate proves

\[
(-\mathscr S(N))_+=N^{o(1)}.
\]

A finite positive ladder is evidence only. The immediate analytic target is a
one-sided cancellation theorem for the square-cutoff Riesz mean of the von
Mangoldt function, at subpolynomial precision after the exact archimedean
centering.
