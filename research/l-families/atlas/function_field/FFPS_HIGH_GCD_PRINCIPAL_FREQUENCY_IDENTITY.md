# The high-gcd far sector has a nonvanishing principal additive frequency

Status: **exact nonzero boundary-kernel mean, exact additive-autocorrelation
and coprimality-inversion identities, and exact identification of the assembled
principal additive frequency with `COREAGG`; no estimate for that frequency,
`HIGHFARGCDWAVE`, RH, or GRH**.

Architecture: **Architecture A only**.

Bounded exact replay:
[`ffps_high_gcd_principal_frequency_identity.py`](ffps_high_gcd_principal_frequency_identity.py).
Canonical fixture:
[`ffps_high_gcd_principal_frequency_identity.json`](ffps_high_gcd_principal_frequency_identity.json).

Frozen source: PR #760 head
`5122e939df2fa322b5a3185cf1d78d4b402f3d5f`, specifically the boundary-field,
shifted-zeta, and high/far localization packets pinned by the replay.

## 0. Outcome

The high/far predecessor removes every prescribed subpower reduced ray and
every prescribed subpower additive-gap window. A tempting next hope is that
the compact boundary primitive might have zero mean, forcing its
autocorrelation to vanish at additive frequency zero. That hope is false.

The extra-notched multiplier is

\[
 \widehat K_{\rm ext}(s)
 ={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
 \qquad
 q(s)=1-\sqrt2\,2^{-s},\quad r(s)=1-2^{-s},
\tag{0.1}
\]

and the boundary primitive satisfies

\[
 \widehat K_{\rm bd}(s)={\widehat K_{\rm ext}(s)\over s}.
\tag{0.2}
\]

Since

\[
 {r(s)\over s}\longrightarrow\log2,\qquad
 q(0)=1-\sqrt2,\qquad
 {(s-1)(5s+3/2)\over s-1/2}\longrightarrow3,
\]

one obtains the exact nonzero boundary mean

\[
\boxed{
 \widehat K_{\rm bd}(0)
 =3(1-\sqrt2)^2(\log2)^2
 =(9-6\sqrt2)(\log2)^2>0.
}
\tag{0.3}
\]

For the imported autocorrelation

\[
 \mathcal R(u)=\int_{\mathbb R}K_{\rm bd}(v)K_{\rm bd}(v+u)\,dv,
\]

Fubini gives

\[
\boxed{
 \int_{\mathbb R}\mathcal R(u)\,du
 =\left(\int_{\mathbb R}K_{\rm bd}(v)\,dv\right)^2
 =(153-108\sqrt2)(\log2)^4>0.
}
\tag{0.4}
\]

Thus there is no hidden vanishing moment at the principal additive frequency.

More strongly, the entire principal additive-frequency ledger is exactly the
positive RH-equivalent core energy already named `COREAGG`. For a fixed
squarefree common shell \(g\) and height block \(I\), put

\[
 f_{g,I}^{\alpha}(a)
 =\mathbf1_{\substack{a\ {\rm squarefree}\\(a,67g)=1}}
 {\mu(a)\over\sqrt a}\mathcal W_I^\alpha(ga),
\tag{0.5}
\]

with finite support supplied by the physical height restriction. Define the
unrestricted additive autocorrelation

\[
 C_{g,I}^{\rm all}(h)
 =\sum_a f_{g,I}^{\alpha}(a)
       \overline{f_{g,I}^{\alpha}(a+h)}.
\tag{0.6}
\]

Then

\[
\boxed{
 \sum_h C_{g,I}^{\rm all}(h)
 =\left|\sum_a f_{g,I}^{\alpha}(a)\right|^2
 =|\mathcal Z_{I,g}^{\alpha}|^2.
}
\tag{0.7}
\]

After the exact reduced-coprimality projector, let

\[
 C_{g,I}^{\rm cop}
 =\sum_{\substack{a,b\ {\rm squarefree}\\
                  (a,b)=1,\ (ab,67g)=1}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal W_I^\alpha(ga)
 \overline{\mathcal W_I^\alpha(gb)}.
\tag{0.8}
\]

Möbius inversion of \((a,b)=1\) gives

\[
\boxed{
 C_{g,I}^{\rm cop}
 =\sum_{\substack{d\ {\rm squarefree}\\(d,67g)=1}}
 {\mu(d)\over d}
 |\mathcal Z_{I,gd}^{\alpha}|^2.
}
\tag{0.9}
\]

Finally, the positive common-shell assembly satisfies

\[
\boxed{
 \sum_g{\kappa_2(g)\over g}C_{g,I}^{\rm cop}
 =
 \sum_r{\tau(r)\over r^2}
 |\mathcal Z_{I,r}^{\alpha}|^2.
}
\tag{0.10}
\]

The right side is exactly the one-block `COREAGG` energy. Therefore the
principal additive frequency is not a removable nuisance: after the exact
coprimality and common-shell transforms, it is the RH-equivalent positive
quantity itself.

Consequently a proof of Architecture A cannot consist only of:

- annihilating the zero additive frequency by a kernel moment;
- bounding fixed or subpower shifts;
- proving a minor-arc-only estimate;
- or proving cancellation only after deleting the principal additive mode.

It must control the assembled principal frequency, or produce a signed
identity which transports that frequency into another tractable coordinate.

## 1. Exact boundary mean

Equation (0.3) follows directly from (0.1)--(0.2). Its positivity is exact:

\[
 9^2-2\cdot6^2=9>0.
\tag{1.1}
\]

Squaring gives

\[
 (9-6\sqrt2)^2=153-108\sqrt2,
\]

and

\[
 153^2-2\cdot108^2=81>0.
\tag{1.2}
\]

No numerical approximation to \(\sqrt2\) or \(\log2\) is used.

The zero logarithmic mass of \(K_{\rm ext}\) is compatible with (0.3):
\(K_{\rm ext}=DK_{\rm bd}\), so differentiating the nonzero-mean compact
primitive produces a zero-mass signed measure.

## 2. Additive Fourier identity

Because the support of \(f_{g,I}^\alpha\) is finite,

\[
\begin{aligned}
 \sum_h C_{g,I}^{\rm all}(h)
 &=\sum_h\sum_a
 f_{g,I}^\alpha(a)
 \overline{f_{g,I}^\alpha(a+h)}\\
 &=\sum_{a,b}
 f_{g,I}^\alpha(a)\overline{f_{g,I}^\alpha(b)}
 =\left|\sum_a f_{g,I}^\alpha(a)\right|^2.
\end{aligned}
\tag{2.1}
\]

The last sum is precisely the previously defined core coordinate

\[
 \mathcal Z_{I,g}^{\alpha}
 =\sum_{\substack{a\ {\rm squarefree}\\(a,67g)=1}}
 {\mu(a)\over\sqrt a}\mathcal W_I^\alpha(ga).
\tag{2.2}
\]

Equivalently, for

\[
 F_{g,I}^\alpha(\vartheta)
 =\sum_a f_{g,I}^\alpha(a)e(a\vartheta),
\]

finite Fourier expansion gives

\[
 \sum_h C_{g,I}^{\rm all}(h)e(h\vartheta)
 =|F_{g,I}^\alpha(\vartheta)|^2.
\tag{2.3}
\]

Equation (0.7) is the value at \(\vartheta=0\).

The high/far packet pays every \(|h|\le G(H)\) for prescribed
\(G(H)=H^{o(1)}\). Hence the far-shift sum is the principal frequency
\(|\mathcal Z_{I,g}^{\alpha}|^2\) minus an already paid near-lag polynomial.
It is not a purely minor-arc remainder.

## 3. Coprimality inversion

Insert

\[
 \mathbf1_{(a,b)=1}=\sum_{d\mid(a,b)}\mu(d)
\tag{3.1}
\]

into (0.8). On squarefree support write \(a=dm\), \(b=dn\). Then
\((d,mn)=1\), and

\[
 {\mu(a)\mu(b)\over\sqrt{ab}}
 ={\mu(m)\mu(n)\over d\sqrt{mn}}.
\tag{3.2}
\]

For each fixed \(d\), the \(m,n\) sums factor, proving (0.9). This is an
identity in the real multiquadratic field generated by the finitely many
square roots in the block.

## 4. Reassembly as COREAGG

Put \(r=gd\). Because \(g,d\) are squarefree and coprime, the coefficient of
\(|\mathcal Z_{I,r}^{\alpha}|^2\) in the left side of (0.10) is

\[
 {1\over r}\sum_{g\mid r}\kappa_2(g)\mu(r/g).
\tag{4.1}
\]

At one prime,

\[
 \kappa_2(p)-1=\left(1+{2\over p}\right)-1={2\over p}.
\tag{4.2}
\]

Multiplicativity therefore gives

\[
 \sum_{g\mid r}\kappa_2(g)\mu(r/g)
 =\prod_{p\mid r}{2\over p}
 ={\tau(r)\over r},
\tag{4.3}
\]

which proves (0.10).

After summing over \(I\), the right side is exactly

\[
 \mathfrak C_\alpha(H)
 =\sum_r{\tau(r)\over r^2}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^{\alpha}|^2.
\tag{4.4}
\]

The earlier packets prove

\[
 \mathrm{COREAGG}
 \Longleftrightarrow\mathrm{PRIMCAR}
 \Longrightarrow\mathrm{RH}.
\tag{4.5}
\]

Equation (0.10) does not estimate this energy; it identifies its additive
principal-frequency meaning.

## 5. Consequences for the next analytic attack

The exact remaining Architecture A target now has three simultaneous
features:

```text
long additive shifts beyond every prescribed subpower window;
a multiplicatively balanced high reduced pair;
a nonvanishing principal additive frequency whose assembled value is COREAGG.
```

A viable dispersion or circle-method proof must therefore include a
principal-frequency theorem of RH strength. Standard fixed-shift estimates,
qualitative density-saving averages, or minor-arc cancellation alone do not
match the target normalization.

The shifted-zeta packet gives the complementary multiplicative statement:
one isolated untruncated Mellin frequency retains the two reciprocal zeta
factors

\[
 {1\over
 \zeta^{(67)}(s-i\xi)\zeta^{(67)}(s+i\xi)}.
\tag{5.1}
\]

The additive principal mode and the multiplicative reciprocal-zeta poles are
two exact coordinates of the same obstruction. A full proof must control one
without assuming the desired zero-free half-plane.

## 6. Scope firewall

- The nonzero boundary mean does not by itself imply failure of RH.
- The principal-frequency identities are finite exact algebra, not estimates.
- The coprime frequency can be signed for fixed \(g\); positivity appears
  after the exact common-shell assembly (0.10).
- The paid near-shift result does not bound the far-shift principal frequency.
- Architecture B is not used.
- No novelty or priority claim is made for finite autocorrelation or Möbius
  inversion separately.

**No HIGHFARGCDWAVE, COREAGG, PRIMCAR, RH, or GRH estimate is proved.**

## 7. Proof ledger

| statement | grade |
|---|---|
| nonzero boundary mean (0.3) | **PROVED EXACT** |
| positive autocorrelation zero frequency (0.4) | **PROVED EXACT** |
| additive principal-frequency identity (0.7) | **PROVED EXACT** |
| coprimality inversion (0.9) | **PROVED EXACT** |
| assembled frequency equals COREAGG (0.10) | **PROVED EXACT** |
| near shifts are subpower | **IMPORTED FROM FROZEN SOURCE** |
| COREAGG to RH chain | **IMPORTED FROM FROZEN SOURCE** |
| HIGHFARGCDWAVE / COREAGG / RH / GRH | **NOT PROVED** |

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_high_gcd_principal_frequency_identity.py --check
python -B -O research/l-families/atlas/function_field/ffps_high_gcd_principal_frequency_identity.py --check
python -B -m unittest tests.test_ffps_high_gcd_principal_frequency_identity
python -B -O -m unittest tests.test_ffps_high_gcd_principal_frequency_identity
```

The replay uses exact rational multiquadratic arithmetic to verify the finite
autocorrelation, coprimality-inversion, and global core-reassembly identities.
It evaluates no zeta zero, finite field, curve, conductor family, or
\(L\)-function.
