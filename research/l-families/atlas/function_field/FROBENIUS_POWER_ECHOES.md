# Frobenius-power echoes of the balanced genus-two control

**Status:** exact pointwise identities, exact compact-group constant terms, and
an exact transform of the frozen member-weight histograms at `q=3,5,7`.

**Scope:** powers `r=1,...,8`; no finite field is enumerated here.  The only
arithmetic input is the source-locked joint `(a_D,b_D)` histogram in
`balanced_control_family_scan.json`.

**What was actually run:** exact Newton recurrences on every histogram atom,
an independent sparse `C_2` Weyl constant-term calculation, and deterministic
normal and optimized-mode tests.  There is no floating point, root finding, or
random sampling.

**Smallest remaining gap:** determine which family corrections in the powered
means and additive-frequency mixed moments persist for general odd `q`, and
separately determine which exact periodic echo signatures correspond to
supersingular or extra-endomorphism strata.

## 1. Definition

Let

\[
 P_D(T)=T^4+a_DT^3+b_DT^2+qa_DT+q^2=\prod_{i=1}^4(T-\alpha_i).
\]

For `r>=1`, define `a_(D,r),b_(D,r)` by

\[
 \prod_i(T-\alpha_i^r)=T^4+a_{D,r}T^3+b_{D,r}T^2
       +q^ra_{D,r}T+q^{2r},
\]

and put

\[
 B_{D,r}=\frac{2a_{D,r}^2}{q^r}-\frac{b_{D,r}^2}{q^{2r}}.
\]

The producer derives the power sums through `2r` by Newton identities. In
particular,

\[
 a_{D,2}=2b_D-a_D^2,
 \qquad b_{D,2}=b_D^2-2qa_D^2+2q^2,
\]

which is also used as an independent regression check.

## 2. Exact echo-collapse theorem

Write a normalized `USp(4)` conjugacy class as

\[
 \{x,x^{-1},y,y^{-1}\},\qquad
 u=x^2+x^{-2},\quad v=y^2+y^{-2}.
\]

If `C_0(z)=2`, `C_1(z)=z`, and
`C_r(z)=z C_(r-1)(z)-C_(r-2)(z)`, then direct expansion gives

\[
 B_r=-C_r(u)C_r(v).
\]

Consequently the *entire infinite power sequence* is determined by only
`B_1` and `B_2`.  More explicitly, set

\[
 p=-B_1=uv,
 \qquad h=\frac{B_1^2+B_2}{2}=u^2+v^2-2.
\]

Then `B_0=-4`,

\[
 B_3=B_1^3-3hB_1+3B_1,
\]

and, for every `r>=4`,

\[
 B_r=pB_{r-1}-hB_{r-2}+pB_{r-3}-B_{r-4}.             \tag{1}
\]

Proof: `-B_r` is the power-sum sequence of

\[
 xy,\;x/y,\;y/x,\;(xy)^{-1}
\]

after replacing `x,y` by `x^2,y^2`.  Their reciprocal quartic has elementary
coefficients `1,p,h,p,1`, so Newton/Cayley--Hamilton gives (1).

This is a useful negative structural result: powers `r>=3` can amplify or
reveal resonances, but they are not independent detector coordinates.  The
echo sequence sees only `(uv,(u+v)^2)` and is blind to the simultaneous sign
change `(u,v)->(-u,-v)`.  In coefficient language,
`u+v=(a_D^2-2b_D)/q` up to the displayed power-polynomial sign convention.

## 3. Exact Haar baseline

The torus restriction collapses to four monomials:

\[
 B(U^r)=-(x^{2r}+x^{-2r})(y^{2r}+y^{-2r}).             \tag{2}
\]

The producer independently integrates (2) with

\[
 \frac1{8}\operatorname{CT}\!\left[
 f\prod_{\alpha\in\{(2,0),(0,2),(1,1),(1,-1)\}}
 (2-X^\alpha-X^{-\alpha})\right].
\]

It recovers

| power | first four Haar moments |
|---:|:---|
| `r=1` | `0, 2, 0, 12` |
| every `2<=r<=8` | `0, 4, 0, 36` |

The same support calculation proves the all-power statement

\[
 \langle B(U^r)B(U^s)\rangle_{USp(4)}=0\quad(r\ne s),
\]

with squared norms `2` at `r=1` and `4` thereafter.  Thus the power echoes are
pairwise orthogonal under Haar even though equation (1) makes them strongly
dependent.

That dependence first becomes visible in distinct mixed third moments. For
every `1<=r<s<t`, an exact Fourier-support argument gives

\[
 \langle B_rB_sB_t\rangle=
 \begin{cases}
 -2,&r+s=t\text{ and }r=1,\\
 -4,&r+s=t\text{ and }r\ge2,\\
 0,&r+s\ne t.
 \end{cases}                                             \tag{3}
\]

Indeed, the zero Fourier coefficient of
`(z^(2r)+z^(-2r))(z^(2s)+z^(-2s))(z^(2t)+z^(-2t))` exists exactly when
`r+s=t` and equals two.  This gives the torus value `-4`.  The `C_2` Weyl
density changes it only when the next frequency is four, exactly when `r=1`,
and its four axis terms add `+2`.  The complete `1<=r<s<t<=8` scan is retained
as a machine regression for (2), not as the proof.

## 4. Frozen finite-family comparison

The committed JSON records, separately for `q=3,5,7` and every `1<=r<=8`:

- exact support and sign counts;
- moments through order four and their exact Haar differences;
- `E(B_1 B_r)`, the centered covariance, and two mixed cubic controls;
- counts satisfying `B_r=B_1` or `B_r=-B_1`;
- the growth of distinct echo prefixes;
- coefficient states that collide under the complete echo detector; and
- exact globally periodic or antiperiodic sequences certified from four
  recurrence initials.

The final item is stronger than observing a repetition in eight terms: once
four consecutive initials agree with a shifted (or negated shifted) sequence,
the common order-four recurrence propagates that equality forever.

The detector-collapse census is already sharp at depth two:

| `q` | states `(a_D^2,b_D)` | distinct `B_1` | distinct complete echoes | collision classes |
|---:|---:|---:|---:|---:|
| 3 | 18 | 14 | 17 | 1 |
| 5 | 45 | 33 | 39 | 5 |
| 7 | 75 | 55 | 67 | 7 |

For all three fields, the number of distinct prefixes stops increasing after
`(B_1,B_2)`, exactly as the theorem predicts.  The collisions are genuine:
even after quotienting the automatic `a_D -> -a_D` twist symmetry, different
coefficient states can have the same *entire* echo sequence.

The recurrence-certified periodic strata are small and unusually rigid:

| `q` | coefficient state | member weight | exact polynomial form | echo period divides |
|---:|:---|---:|:---|---:|
| 3 | `(0,0)` | 12 | `T^4+9` | 2 |
| 3 | `(9,6)` | 6 | `(T^2+3)(T^2+a_DT+3)`, `a_D=+-3` | 3 |
| 5 | `(0,0)` | 50 | `T^4+25` | 2 |
| 5 | `(0,+-10)` | 6 | `(T^2+-5)^2` | 1 |
| 7 | `(0,0)` | 336 | `T^4+49` | 2 |
| 7 | `(0,14)` | 42 | `(T^2+7)^2` | 1 |

After `T=sqrt(q) Z`, these forms have root-of-unity normalized spectra:
`Z^4+1=Phi_8(Z)`, `(Z^2+-1)^2`, or (in the split `q=3` case) an order-four
pair and an order-twelve pair.  This exact cyclotomic factorization is the
reason these are credible endomorphism/supersingularity targets.  The packet
does not import the classification theorem that would turn that spectral
observation into a statement about the Jacobian's endomorphism algebra.

### A deliberately quarantined all-`q` candidate

The three exact second-power means simplify to

\[
 \langle B_2\rangle_{q=3}=-\frac{500}{3^7},\quad
 \langle B_2\rangle_{q=5}=-\frac{12584}{5^7},\quad
 \langle B_2\rangle_{q=7}=-\frac{101100}{7^7}.
\]

All three agree with the sparse expression

\[
 \boxed{\;\langle B_2\rangle
 ?=-\frac{(q-1)(q^5+q^2-q+1)}{q^7}\;} .               \tag{4}
\]

Equation (4) is a **conjectural three-field pattern**, not interpolation
evidence strong enough for a theorem.  Its advantage is that the remaining
proof burden is explicit and low-dimensional: use

\[
 a_{D,2}=2b_D-a_D^2,\qquad
 b_{D,2}=b_D^2-2qa_D^2+2q^2
\]

and evaluate the resulting fourth-degree coefficient moment exactly over the
family.  A single further field could refute (4), but should not be obtained by
heavy enumeration on this machine.

The interpretation remains deliberately cautious.  A global echo period is a
genuine spectral resonance of this four-term trace sequence, but cancellations
can erase parts of the original Frobenius spectrum.  It is therefore a
candidate signature for supersingularity, CM, or extra endomorphisms—not a
proof of any of them.

## 5. Firewalls and replay

Exactly proved here:

1. every displayed Newton transform of a locked histogram atom;
2. the pointwise all-power collapse (1);
3. the displayed `C_2` Haar constant terms;
4. all member-weight statements for the frozen `q=3,5,7` histograms; and
5. global periodicity of the explicitly listed recurrence-certified profiles.

Not proved here:

- an all-`q` formula for any powered family moment;
- a limiting equidistribution rate;
- an endomorphism classification from echo data;
- mutual independence of the Haar power controls; or
- any implication for RH or GRH.

Replay with:

```text
python research/l-families/atlas/function_field/frobenius_power_echoes.py --check
python -m unittest tests.test_frobenius_power_echoes
python -O -m unittest tests.test_frobenius_power_echoes
```

The fixture locks the input JSON and producer, this producer, this note, and
the test by LF-normalized SHA-256.  The resource ledger records fewer than
20,000 Laurent operations and fewer than 20,000 histogram-atom/power steps.
