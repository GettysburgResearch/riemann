# Boolean depth recombination and core-shell Carleson envelopes

Status: **exact depth-recombined Boolean coefficient, fixed-ratio core-shell
L1 and source-diagonal L2 majorant theorems, and common-core transfer; no
Hilbert-observation or signed FFPS complementary-current estimate, RH, or
GRH**

Bounded replay:
[`ffps_boolean_depth_recombination_carleson.py`](ffps_boolean_depth_recombination_carleson.py).

This packet sharpens the transfer firewall in
`FFPS_WEIGHTED_RICH_CORE_TRANSFER_FIREWALL.md`.  That packet used the direct
bound `|b_U|<=5^omega`.  Exact depth recombination improves five boxes to
three and proves the strongest shell-uniform coefficient theorem presently
available.

## 0. Outcome

In the squarefree Boolean algebra, write

\[
 \mu_{>U}=\mu_{\rm sf}\mathbf1_{n>U}.
\]

The frozen Vaughan defect and balanced coefficient satisfy

\[
 a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf},
 \qquad
 b_U=a_U\star a_U\star\mu_{\rm sf}.
\]

Using `mu_sf star 1_sf=epsilon`, one gets the exact depth-recombined identity

\[
 \boxed{
 a_U=\mu_{>U}\star\mathbf1_{\rm sf},
 \qquad
 b_U=\mu_{>U}\star\mu_{>U}\star\mathbf1_{\rm sf}.}
\tag{0.1}
\]

Consequently

\[
 \boxed{
 b_U(n)=
 \sum_{\substack{RST=n\\(R,S)=(R,T)=(S,T)=1\\R>U,\ S>U}}
 \mu(R)\mu(S).}
\tag{0.2}
\]

There are only three labelled boxes `R,S,T`, so uniformly in the moving
cutoff

\[
 \boxed{|b_U(n)|\le3^{\omega(n)}.}
\tag{0.3}
\]

This yields genuine fixed-ratio shell estimates.  Put

\[
 r=\lfloor\alpha\log\log x\rfloor,
 \qquad0<\alpha<1/2,
\]

and let `A>1` be fixed.  Uniformly in `U`,

\[
 \boxed{
 \sum_{\substack{x/A<n\le x\\\omega_1(n)<r}}
 {\mu^2(n)|b_U(n)|\over n}
 \ll_{A,\alpha}
 (\log x)^{e_1(\alpha)+o(1)},}
\tag{0.4}
\]

where

\[
 e_1(\alpha)
 ={1\over2}+\alpha-\alpha\log(2\alpha/3).
\tag{0.5}
\]

The full `3^omega` shell has exponent two, so the exact relative majorant
saving is

\[
 \boxed{
 c_1(\alpha)
 ={3\over2}-\alpha+\alpha\log(2\alpha/3)>0.}
\tag{0.6}
\]

The same argument applied to `|b_U|^2<=9^omega` gives a much stronger
source-diagonal L2 envelope.  Both estimates survive the sharp ratio-eight
shell as indicator deletions and survive common-core extraction with an
absolutely summable `g` factor.

This is a real partial `FFPS-RICH-CARLESON` theorem at the Boolean core
coefficient level.  It still does not control the observed FFPS current:
the Hilbert-valued `gamma_omega(t)`, owner sums and signed conductor
recombination are not bounded by the artificial `3^omega` reference norm.

## 1. Exact depth recombination

The Boolean inverse identity gives

\[
 \mu_{\rm sf}\star\mathbf1_{\rm sf}=\varepsilon.
\]

Since `mu_sf=mu_U+mu_>U`,

\[
\begin{aligned}
 a_U
 &=\varepsilon-\mu_U\star\mathbf1_{\rm sf}\\
 &=(\mu_{\rm sf}-\mu_U)\star\mathbf1_{\rm sf}\\
 &=\mu_{>U}\star\mathbf1_{\rm sf}.
\end{aligned}
\]

Therefore

\[
\begin{aligned}
 b_U
 &=\mu_{>U}\star\mathbf1_{\rm sf}
   \star\mu_{>U}\star\mathbf1_{\rm sf}
   \star\mu_{\rm sf}\\
 &=\mu_{>U}\star\mu_{>U}\star\mathbf1_{\rm sf},
\end{aligned}
\]

proving (0.1)--(0.2).  This recombines all Boolean Vaughan representations
before an absolute value is taken.  It is strictly sharper than separately
bounding the two `a_U` factors.

Every prime label of `n` is assigned to exactly one of `R,S,T`.  Dropping the
two product cutoffs and the Möbius signs proves (0.3).  The exact support
condition also remains visible:

\[
 b_U(n)\ne0
 \Longrightarrow
 n=RST\text{ for two disjoint factors }R,S>U
 \Longrightarrow n>U^2.
\tag{1.1}
\]

## 2. Fixed-ratio L1 shell theorem

For `0<t<1`, define the nonnegative multiplicative function

\[
 f_t(n)=\mu^2(n)3^{\omega(n)}t^{\omega_1(n)}.
\]

Mertens in the two reduced classes modulo four gives

\[
 \sum_{p\le x}{f_t(p)\over p}
 ={3\over2}(1+t)\log\log x+O_t(1).
\tag{2.1}
\]

The standard nonnegative multiplicative mean-value bound therefore yields

\[
 \sum_{n\le x}f_t(n)
 \ll_t
 x(\log x)^{\frac32(1+t)-1}.
\tag{2.2}
\]

This is the elementary Halberstam--Richert/Wirsing upper bound: its right side
is `x/log x` times the exponential of the prime sum (2.1).  No short-interval
theorem is needed.  On `x/A<n<=x`, one has `1/n<=A/x`, so

\[
 \sum_{x/A<n\le x}{f_t(n)\over n}
 \ll_{A,t}(\log x)^{\frac32(1+t)-1}.
\tag{2.3}
\]

If `omega_1(n)<r`, then

\[
 1\le t^{-(r-1)}t^{\omega_1(n)}.
\]

Equations (0.3) and (2.3) give

\[
 \sum_{\substack{x/A<n\le x\\\omega_1(n)<r}}
 {|b_U(n)|\over n}
 \ll
 (\log x)^{\frac32(1+t)-1-\alpha\log t+o(1)}.
\tag{2.4}
\]

The optimizer is `t=2alpha/3`.  This proves (0.4)--(0.6).  For the diagnostic
value

\[
 \alpha=0.274064461784,
\]

the single-shell exponents are

\[
 e_1(\alpha)=1.239934868312,
 \qquad
 c_1(\alpha)=0.760065131688.
\tag{2.5}
\]

The theorem is uniform in `U` because only (0.3) was used.  It is also stable
under any indicator-valued core deletion, including squarefreeness,
owner/core exclusion, one fixed physical shell and renewal masks.

## 3. Pair and common-core transfer

After common-core extraction the two original cores are

\[
 a=gc,
 \qquad b=gd,
 \qquad \mu^2(gcd)=1,
\]

and the literal coefficient denominator is

\[
 {1\over g^2cd}={1\over ab}.
\]

The recombined majorant gives

\[
 |b_U(gc)b_U(gd)|
 \le9^{\omega(g)}3^{\omega(c)+\omega(d)}.
\tag{3.1}
\]

Hence the common part costs the absolute constant

\[
 \boxed{
 \sum_g{\mu^2(g)9^{\omega(g)}\over g^2}<\infty.}
\tag{3.2}
\]

For fixed-ratio shells on `c,d`, the full pair majorant has log exponent four.
If either reduced core is poor, the union bound and (0.4) give exponent

\[
 2+e_1(\alpha)
 ={5\over2}+\alpha-\alpha\log(2\alpha/3),
\tag{3.3}
\]

so the pair retains exactly the saving (0.6).  Coprimality and the sharp
ratio-eight overlap only delete positive-majorant terms.

This is the first coefficient-level result that simultaneously respects:

```text
the exact Boolean depth recombination;
the moving Vaughan cutoff;
fixed multiplicative physical shells;
reduced-core richness after gcd extraction;
the exact g^-2 common-core weight.
```

## 4. Source-diagonal L2 envelope

For the source diagonal, use

\[
 |b_U(n)|^2\le9^{\omega(n)}.
\]

On a fixed-ratio shell,

\[
 \sum_{x/A<n\le x}{\mu^2(n)9^{\omega(n)}\over n^2}
 \ll_A{x^{-1}}(\log x)^8.
\tag{4.1}
\]

Adding the poor-core marker and optimizing at `t=2alpha/9` gives

\[
 \boxed{
 \sum_{\substack{x/A<n\le x\\\omega_1(n)<r}}
 {|b_U(n)|^2\over n^2}
 \ll
 x^{-1}(\log x)^{e_2(\alpha)+o(1)},}
\tag{4.2}
\]

where

\[
 e_2(\alpha)
 ={7\over2}+\alpha-\alpha\log(2\alpha/9),
\]

and the relative `9^omega` shell saving is

\[
 \boxed{
 c_2(\alpha)
 ={9\over2}-\alpha+\alpha\log(2\alpha/9)>0.}
\tag{4.3}
\]

For a pair after common-core extraction, the `g` factor is

\[
 \boxed{
 \sum_g{\mu^2(g)81^{\omega(g)}\over g^4}<\infty.}
\tag{4.4}

Thus the principal atomic/source-diagonal topology has an especially strong
coefficient envelope.  This does not control off-diagonal near collisions;
PR #751 already warns that a source-diagonal estimate cannot replace the
coherent observed current.

## 5. What remains open

The exact identity (0.1) identifies the smallest source-faithful object that
an observation theorem must see:

\[
 \sum_{\substack{R,S>U\\(R,S)=1}}
 {\mu(R)\mu(S)\over RS}
 \sum_{\substack{T\\(T,RS)=1}}{1\over T}
 \mathcal O_{P,RST},
\tag{5.1}
\]

with the physical shell, carrier and owner labels still inside
`mathcal O`.  Separating the three sums or taking a modulus before their
recombination loses the Boolean cancellation.

The coefficient theorems above do not prove a fully observed
`FFPS-RICH-CARLESON(alpha)` estimate for three reasons:

1. `gamma_omega(t)=Y^{o(1)}` is not a fixed logarithmic weight and is not
   controlled by `3^omega` in the frozen claims;
2. the ratio-eight kernel is signed and Hilbert-valued, so an L1 coefficient
   majorant is not the conclusion norm;
3. conductor fibres must be recombined before an absolute value, as required
   by `R-106123` and `T-106140`.

The next exact gate is therefore:

```text
FFPS-RICH-OBS(alpha):
  apply the actual carrier/owner observation to the recombined three-box
  field (5.1), sum the inherited depth and conductor coordinates, and prove
  that its poor-reduced-core restriction loses a fixed power of log Y in the
  source-dual Hilbert norm (or directly in the signed complementary current).
```

Any proof may use (0.4) and (4.2) as endpoint coefficient bounds.  It still
needs a source-to-observation operator theorem; ambient factor density alone
cannot supply one.

## 6. Proof ledger

Proved exactly or from the stated standard multiplicative mean-value bound:

- the depth-recombined identity (0.1)--(0.2);
- the three-box uniform envelope (0.3);
- the fixed-ratio L1 poor-core shell theorem (0.4)--(0.6);
- pair/common-core transfer with the exact `g^-2` weight;
- the source-diagonal L2 shell theorem (4.1)--(4.4).

Not proved:

- comparison with the actual fully observed FFPS norm;
- `FFPS-RICH-OBS(alpha)`;
- a bound for the signed complementary current;
- principal individualization, RH, or GRH.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_boolean_depth_recombination_carleson.py --check
python -B -O research/l-families/atlas/function_field/ffps_boolean_depth_recombination_carleson.py --check
python -B -m unittest tests.test_ffps_boolean_depth_recombination_carleson
python -B -O -m unittest tests.test_ffps_boolean_depth_recombination_carleson
```

The replay compares the original and recombined Boolean formulas on every
cutoff cell through support size six and evaluates two scalar exponent
panels.  It enumerates no FFPS source family, conductor family, curve or
point.
