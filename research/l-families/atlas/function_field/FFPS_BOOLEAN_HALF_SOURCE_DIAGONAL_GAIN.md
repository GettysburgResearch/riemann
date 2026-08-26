# The exact Boolean half-source diagonal gain

Status: **exact half-source recombination and polynomially saving free
owner--core source diagonal on one physical horizon; no off-diagonal physical
Gram, reflection-signature, signed family estimate, RH, or GRH**

Bounded replay:
[`ffps_boolean_half_source_diagonal_gain.py`](ffps_boolean_half_source_diagonal_gain.py).

Frozen interface: PR #751 `L-106132--L-106133` and `T-106150`.

## 0. Outcome

The three-box identity for the full Boolean coefficient has a sharper
one-half-source precursor.  Let

\[
 h(S)=(-1/2)^{|S|},
 \qquad f_U=a_U\star h.
\]

If

\[
 q(S)=2^{-|S|},
\]

then exact Boolean recombination gives

\[
 \boxed{f_U=\mu_{>U}\star q.}
\tag{0.1}
\]

Consequently

\[
 \boxed{
 f_U(n)=
 \sum_{\substack{RT=n\\(R,T)=1\\R>U}}
 \mu(R)2^{-\omega(T)},
 \qquad
 |f_U(n)|\le(3/2)^{\omega(n)},}
\tag{0.2}
\]

and

\[
 \boxed{f_U(n)\ne0\Longrightarrow n>U.}
\tag{0.3}

This identifies the constant left unspecified in `L-106133.13`: one can take
`C=3/2`, uniformly in the moving cutoff.

More importantly, (0.2)--(0.3) make the **actual free owner--core source
diagonal polynomially small**.  The half-field atoms have the injective
physical form

\[
 n=pa^2,
 \qquad(p,a)=1,
\]

with coefficient `f_U(a)/(sqrt(p)a)`.  On a horizon `pa^2<=C_0Y` and with
`U=floor(Y^(1/6))`,

\[
 \boxed{
 \sum_{\substack{p,a\\pa^2\le C_0Y\\(p,a)=1}}
 {|f_U(a)|^2\over pa^2}
 \ll_{C_0}
 Y^{-1/6}(\log Y)^{5/4}\log\log(3Y).}
\tag{0.4}

The earlier source ledger recorded only `Y^o(1)`.  Equation (0.4) is a
power-saving strengthening, obtained without enumerating a source atom and
without a character or sheaf estimate.

This pays every literal atomic/free-diagonal contribution of the half-source
with ample margin.  It does not pay correlations between distinct physical
products in the ratio-eight window.  Those correlations are exactly the
reflection/near-collision obstruction retained by `T-106150`.

## 1. Exact half-source recombination

The preceding depth packet proves

\[
 a_U=\mu_{>U}\star\mathbf1_{\rm sf}.
\]

Hence

\[
 f_U
 =\mu_{>U}\star(\mathbf1_{\rm sf}\star h).
\]

At every labelled prime, the two local weights in
`1_sf star h` are `1` and `-1/2`; their sum is `1/2`.  Therefore

\[
 (\mathbf1_{\rm sf}\star h)(S)=2^{-|S|}=q(S),
\]

which proves (0.1)--(0.2).  Dropping the cutoff and signs gives the local
absolute assignment weight

\[
 1+{1\over2}={3\over2},
\]

proving the uniform majorant.  Every surviving term contains `R>U`, proving
(0.3).

As a check, if every prime of a nonempty support `S` exceeds `U`, then

\[
 f_U(S)
 =\sum_{\varnothing\ne R\subseteq S}
 (-1)^{|R|}2^{-|S\setminus R|}
 ={(-1)^{|S|}-1\over2^{|S|}}.
\tag{1.1}

Thus the rough half-source vanishes at even depth and equals
`-2^(1-|S|)` at odd depth.  Convolving two copies recovers the rough even
depth coefficient in the full `b_U` source.

The depth dilation `T_theta` of `L-106133` multiplies a size-`k` coefficient
by `theta^k`, with `0<=theta<=1`; all estimates here are therefore uniform in
the Beta parameter.

## 2. Tail estimate for the half-core

Square (0.2):

\[
 |f_U(a)|^2\le(9/4)^{\omega(a)}.
\tag{2.1}

For the nonnegative multiplicative function

\[
 F(a)=\mu^2(a)(9/4)^{\omega(a)},
\]

the standard mean-value bound gives

\[
 \sum_{a\le x}F(a)
 \ll x(\log x)^{5/4}.
\tag{2.2}

Partial summation, or a dyadic decomposition, now yields

\[
 \boxed{
 \sum_{a>U}{\mu^2(a)(9/4)^{\omega(a)}\over a^2}
 \ll U^{-1}(\log(2U))^{5/4}.}
\tag{2.3}

This bound is uniform in the upper physical horizon; extending the sum to
infinity only increases its positive majorant.

## 3. The owner sum is paid

If `f_U(a)` is nonzero, (0.3) gives `a>U`.  On

\[
 pa^2\le C_0Y
\]

one therefore has

\[
 p\le {C_0Y\over U^2}.
\tag{3.1}

Drop `(p,a)=1` and all owner exclusions.  Equations (2.3) and the elementary
prime harmonic bound give

\[
\begin{aligned}
 \sum_{pa^2\le C_0Y}{|f_U(a)|^2\over pa^2}
 &\le
 \left(\sum_{p\le C_0Y/U^2}{1\over p}\right)
 \left(\sum_{a>U}{(9/4)^{\omega(a)}\mu^2(a)\over a^2}\right)\\
 &\ll
 \log\log(3Y)\,U^{-1}(\log(2U))^{5/4}.
\end{aligned}
\tag{3.2}

Substituting `U=floor(Y^(1/6))` proves (0.4).  The two labelled copies of
`67` and any finite endpoint-colour multiplicity change only the implied
constant.  Owner, marked-prime and renewal deletions commute with the
half-source by `L-106133` and can only lower this positive diagonal bound.

This is the literal source-space diagonal before physical near-collision
observation.  The injectivity of `(p,a)->pa^2` ensures there is no hidden
equal-product multiplicity.

## 4. Poor-half-core refinement

Although (0.4) already has a power saving without a richness restriction, the
poor half-core has an additional log saving.  Let

\[
 r=\lfloor\alpha\log\log Y\rfloor,
 \qquad0<\alpha<1/2.
\]

Insert `t^omega_1(a)` in (2.1), use the same nonnegative multiplicative
mean-value bound, and optimize at

\[
 t={2\alpha\over9/4}={8\alpha\over9}.
\]

Then

\[
 \sum_{\substack{a>U\\\omega_1(a)<r}}
 {|f_U(a)|^2\over a^2}
 \ll
 U^{-1}(\log Y)^{e_{1/2}(\alpha)+o(1)},
\tag{4.1}

where

\[
 e_{1/2}(\alpha)
 ={1\over8}+\alpha-\alpha\log(8\alpha/9).
\tag{4.2}

The full `(9/4)^omega` tail exponent is `5/4`, so the relative envelope
saving is

\[
 \boxed{
 c_{1/2}(\alpha)
 ={9\over8}-\alpha+\alpha\log(8\alpha/9)>0.}
\tag{4.3}

At `alpha=0.274064461784`,

\[
 e_{1/2}=0.786091435960,
 \qquad
 c_{1/2}=0.463908564040.
\]

Multiplication by the owner harmonic factor in (3.2) preserves that log
saving.

This refinement concerns richness of the half-core `a`.  The block amplifier
selects eligible primes in the **full convolution output** core.  A projection
on poor full cores does not factor into independent projections on the two
half-sources.  Therefore (4.1) is an endpoint estimate for a future bilinear
argument, not a proof of `FFPS-RICH-OBS(alpha)`.

## 5. Exact remaining obstruction

`L-106133` and `T-106150` write the balanced current as a Beta average of a
Wick/Boolean convolution square of the one-owner half-field.  Equation (0.4)
shows that its literal diagonal is not the obstruction.

What remains is the off-diagonal form

\[
 \sum_{pa^2\ne qb^2}
 {f_U(a)\over\sqrt p\,a}
 {f_U(b)\over\sqrt q\,b}
 K\!\left({pa^2\over qb^2}\right),
\tag{5.1}

where `K` is the signed carrier-recombined ratio-eight kernel and all Boolean
disjointness contractions remain typed.  A free-diagonal estimate does not
bound (5.1): many distinct injective products can still lie in one compact
multiplicative window.

The next useful theorem must therefore exploit at least one of:

- reflection cancellation in `T-106150`;
- the two-large-Moebius representation of the full output coefficient;
- a genuine operator/Carleson bound for the ratio-eight observation;
- or the connected additive/Kummer recombination of `T-106140`.

No additional atomic or owner-dimension estimate is needed at this stage.

## 6. Proof ledger

Proved exactly or by the stated standard multiplicative mean-value bound:

- the exact half-source identity (0.1)--(0.2);
- the uniform `(3/2)^omega` coefficient bound and support cutoff;
- the half-core square tail (2.3);
- the actual owner--core source-diagonal power saving (0.4);
- the poor-half-core log refinement (4.1)--(4.3).

Not proved:

- the off-diagonal ratio-eight form (5.1);
- a poor **full-output** core projection theorem after convolution;
- `FFPS-RICH-OBS(alpha)`, `REFSIG106150`, or the signed family gates;
- principal individualization, RH, or GRH.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_boolean_half_source_diagonal_gain.py --check
python -B -O research/l-families/atlas/function_field/ffps_boolean_half_source_diagonal_gain.py --check
python -B -m unittest tests.test_ffps_boolean_half_source_diagonal_gain
python -B -O -m unittest tests.test_ffps_boolean_half_source_diagonal_gain
```

The replay checks the original and recombined half-source on every cutoff cell
through support size six and evaluates one scalar exponent panel.  It
enumerates no FFPS family, conductor family, curve, or point.
