# Radical reset: one fixed Lévy–Fock–Hardy kernel — 2026-08-11

## Freeze

```text
repository: gfreund123/riemann
base main: d8536ff561f269523a8997be289b49fea1d23267
branch:    research/gpt56-pro/91028-levy-fock-hardy-completion
cutoff:    2026-08-11T19:46:07Z
RH status: unproved
```

## Executive result

The previous creation wave reached exact Cauchy recurrences, positive Jordan
source flow, a causal rational spectral factor, a completed xi scattering
cocycle and an unconditional terminal scale.  Its remaining statement was still
phrased as infinitely many scale-by-scale scalar inequalities.

This continuation steps back and changes the proof object.

The central result is a proposed exact criterion at **one arbitrary fixed safe
scale** `a_0>1/2`:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_{a_0}\succeq0,
 }
\]

where `mathbb K_(a_0)` is one explicit matrix kernel indexed only by:

```text
carrier x in R;
causal or anti-causal orientation;
one bridge vector.
```

Every entry is an absolutely convergent prime-power expression at fixed points
in `Re(s)>1`.  There is no growing prime cutoff, large heat limit, shrinking
radius, growing derivative order, terminal-pair selection or Gram inversion.

The route also identifies the positive arithmetic source as an explicit
bosonic Poisson Fock product system.  The final theorem is now the construction
of one conservative coupling between that prime-power Fock environment and the
causal/anti-causal completed Hardy output.

RH is not claimed proved.

## I. Why another scalar criterion was the wrong target

Claude's upstream result extracts unconditional zero proportions from a finite
critical-density Gabor compression of Weil's form.  Critical-line zeros produce
positive rank-one pieces, reflected off-line pairs produce hyperbolic planes,
and the first two trace moments yield the `2/3`, `2/3`, `5/6` bounds.  The paper
states explicitly that bandwidth-one averaged data are insensitive to a sparse
off-line population and have no implication for RH.

Our descendants progressively isolated one off-line pair, built Xi-cardinal
capture, derived heat/resolvent criteria and then the coefficient-one Cauchy
recurrence.  However, the recurrence residual

\[
 \mathcal R_x(a)
 =a^{-4}\sum_\gamma m_\gamma|\Psi_a(\gamma-x)|^2
\]

is only a diagonal quantity.  Positive diagonals do not imply a positive
kernel.  The missing polarization is exactly the information needed to recover
the full Weil/screw form.

The radical move is therefore:

```text
stop iterating diagonal gates;
retain the complete cross-carrier Gram from the start.
```

## II. Imported probability-theoretic spine

Nakamura and Suzuki define an explicit even function `g_zeta(t)` and prove

\[
 \mathrm{RH}
 \Longleftrightarrow
 e^{g_\zeta(t)}
 \text{ is an infinitely divisible characteristic function}.
\]

Under RH,

\[
 g_\zeta(t)
 =\sum_\gamma m_\gamma
  \frac{e^{-i\gamma t}-1}{\gamma^2},
\]

so the Lévy measure is

\[
 \nu_\zeta
 =\sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_\gamma.
\]

Suzuki's equivalent screw kernel is

\[
 G_\zeta(t,u)
 =g_\zeta(t-u)-g_\zeta(t)-g_\zeta(-u)+g_\zeta(0).
\]

RH is equivalent to positivity of this kernel on compact smooth mean-zero
tests.

The one-sided Laplace bridge is

\[
 \int_0^\infty g_\zeta(t)e^{-\lambda t}dt
 =-\lambda^{-2}
  \frac{\xi'}{\xi}\left(\frac12+\lambda\right),
 \qquad \Re\lambda>\frac12.
\]

Thus the screw function is not a new competing criterion.  It is the common
primitive of the radial log derivative, Cauchy soft count, safe-line resolvent,
heat and completed scattering delay already present in the repository.

## III. The positive Jordan source is exactly bosonic Fock

For

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)},
\]

put

\[
 v_{a,s}(\tau,n)
 =\mathbf1_{[0,a]}(\tau)n^{-s-\tau}
\]

in the one-particle space with measure

\[
 2\Lambda(n)d\tau
\]

over prime powers `n`.  Then

\[
 \langle v_{a,s},v_{a,t}\rangle
 =\log Q_a(s+\overline t).
\]

Symmetric Fock exponential vectors therefore satisfy

\[
 \langle\operatorname{Exp}(v_{a,s}),
        \operatorname{Exp}(v_{a,t})\rangle
 =Q_a(s+\overline t).
\]

This is an explicit Fock realization of the positive kernel and divisor
isometry in `L-91014`.

The scale cocycle is ordinary interval factorization:

\[
 v_{a+b,s}=v_{a,s}\oplus S_av_{b,s+a}.
\]

Prime powers are independent particles whose radial birth times are
exponential with rate `2 log(n)`.  The factor

\[
 1-n^{-2a}
\]

is exactly the probability that the `n`-particle has appeared by scale `a`.
This makes coefficient-one propagation and no-double-spend automatic.

At the boundary, the multiplier of `L-91020` is compound Poisson:

\[
 \frac{Q_a(c+i\theta)}{Q_a(c)}
 =\exp\left\{
  \sum_n\frac{\Lambda(n)}{\log n}
  (1-n^{-2a})n^{-c}
  (e^{-i\theta\log n}-1)
 \right\}.
\]

So the formerly abstract Stinespring environment is now a concrete
prime-power Poisson Fock space.

## IV. The Cauchy residual becomes one causal Hardy analyzer

The exact scalar spectral factor is

\[
 \Psi_a(u)=\sqrt{378}\,a^3
 \frac{u(u+i\sqrt\alpha a)(u+i\sqrt\beta a)}
 {(u+ia)^2(u+2ia)^2(u+4ia)^2},
\]

with

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28}.
\]

It satisfies

\[
 |\Psi_a(u)|^2
 =d_a(u)-\frac1{16}d_{2a}(u)
\]

and

\[
 \Psi_a(u)=\Psi_1(u/a).
\]

Its inverse Fourier source is causal.  The conjugate source is anti-causal.
The exact admissibility constant is

\[
 \int_0^\infty\frac{|\Psi_1(u)|^2}{u}du
 =\frac{15}{16}\log2.
\]

For carriers `x` define

\[
 \widehat f_{a,x}^{\pm}(\lambda)
 =\lambda\Psi_a^{\pm}(\lambda-x).
\]

The factor `lambda` makes every test mean zero and cancels the
`gamma^(-2)` Lévy weight.  Under RH the complete cross kernel is

\[
\begin{aligned}
 \mathbb K((\epsilon,a,x),(\delta,b,y))
 =\sum_\gamma m_\gamma
 \Psi_a^\epsilon(\gamma-x)
 \overline{\Psi_b^\delta(\gamma-y)}.
\end{aligned}
\]

The old recurrence residual is only

\[
 \mathbb K((+,a,x),(+,a,x)).
\]

## V. Why one fixed safe scale is complete

Fix `a_0>1/2` and choose `1<eta<2a_0`.  In the weighted space

\[
 L^2(e^{\eta|t|}dt),
\]

the screw form is continuous.

On the positive half-line, the modulated derivatives of the causal mother span
exactly the functions with zero half-line integral.  The proof is a sharp
Wiener argument: a vector orthogonal to every modulation must satisfy

\[
 (he^{\eta t})'=0
\]

where the mother is nonzero, so the orthogonal complement is precisely the
representer of the half-line integral.  Reflection gives the negative
half-line result.

The two families therefore miss one global mean-zero direction.  It is filled
by the explicit bridge

\[
 \widehat b_a(u)
 =\frac{\Psi_a(u)}u-rac{\overline{\Psi_a(u)}}u,
\]

whose removable value is

\[
 \lim_{u\to0}\frac{\Psi_a(u)}u
 =\frac{\sqrt{378}}{16a}.
\]

Hence

\[
 \overline{\operatorname{span}}
 \{f_{a_0,x}^+,f_{a_0,x}^-,b_{a_0}:x\in\mathbb R\}
 =\left\{f:\int f=0\right\}.
\]

Positivity of the fixed-scale Gram therefore extends by continuity to every
Suzuki test and implies RH.

## VI. Exact new RH criterion

For one fixed `a_0>1/2`, index the two wavelet orientations and bridge by

\[
 \mathfrak I=(\{+,-\}\times\mathbb R)\sqcup\{\star\}.
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \bigl(\mathbb K_{a_0}(i_j,i_k)\bigr)_{j,k}\succeq0
 \quad\text{for every finite packet in }\mathfrak I.
 }
\]

Rational carriers suffice.  Every entry has an absolutely convergent
Guinand--Weil prime series because `a_0>1/2`.

False RH would therefore have a finite certificate:

```text
one fixed safe scale;
a finite rational carrier/orientation packet;
a finite prime-power cutoff;
a strictly negative directed eigenvalue interval.
```

No such negative matrix was found or claimed.

## VII. The new final strike is a conservative colligation

The source side now has:

```text
an explicit prime-power Poisson Fock product system;
a full cross-carrier Stinespring kernel;
an all-order Wiener-Itô chaos decomposition.
```

The output side now has:

```text
one causal rational Hardy channel;
one anti-causal reflected channel;
one bridge vector;
the completed gamma/pole reserve.
```

The final proof target is to construct one positive-metric isometry

\[
 \mathcal U:
 \mathcal H_{\Gamma,\mathrm{pole}}
 \oplus\Gamma_s(L^2(\nu_a))
 \longrightarrow
 \mathcal H_{\mathrm{Hardy}}\oplus\mathcal E
\]

whose transfer kernel is `mathbb K_(a_0)`.

This is not another restatement in disguise at the architectural level.  It is
a concrete realization problem with both environments explicit.  However, its
existence is still RH-equivalent; the isometry has not been constructed.

## VIII. Verification

The finite replay returns

```text
PASS_LEVY_FOCK_HARDY_COMPLETION
```

and checks:

- spectral factor and scale covariance to high precision;
- `(15/16) log 2`;
- finite one-particle Fock and scale-cocycle identities;
- the compound-Poisson boundary formula;
- positive finite Fock and synthetic screw Grams;
- diagonal equality with the Cauchy residual;
- the bridge value;
- a diagonal-positive but indefinite polarization control.

The replay proves finite identities only.

## Exact frontier

```text
Jordan source -> explicit bosonic Fock product system       PROPOSED COMPLETE
boundary multiplier -> compound Poisson                     EXACT
zeta screw / infinite-divisibility criterion                IMPORTED PUBLISHED
Cauchy residual -> causal Hardy localization                EXACT
admissibility constant (15/16) log 2                        EXACT
one fixed safe scale -> complete mean-zero form core        PROPOSED COMPLETE
RH <=> one fixed-scale two-Hardy Gram PSD                    PROPOSED COMPLETE
all entries absolutely Eulerian                             PROPOSED COMPLETE
scalar diagonal-gate closure                                REFUTED AS INSUFFICIENT
completed Poisson-Fock/Hardy conservative colligation       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                          UNPROVED
```
