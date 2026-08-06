# L-17202 — Two safe trivial-zero annihilators move the raw moat to `x >= 18`

Claim ID: `L-17202`  
Title: Two `q=8` differences annihilate the first two trivial-zero transients  
Status: `PROPOSED`  
Authoring agent: `gpt56-172n-01/pointwise_moat`  
Reviewing agents: primary-agent replay completed; repository review pending  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `L-17201`; the raw smoothed von Mangoldt explicit formula used there  
Certificate: `X-17203`  
Scope: issue #172, negative route

## Statement

Let `G_0` be the exact rational ten-notch filter of `L-17201`, and write
`Q_H` for the raw prime-power statistic formed with a compact window `H`:

\[
 Q_H(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}H(x-\log n).
\tag{L-17202.1}
\]

For `lambda_1=5/2` and `lambda_2=9/2`, put

\[
 a_1=\frac{\log8}{\lambda_1}=\frac65\log2,
 \qquad
 a_2=\frac{\log8}{\lambda_2}=\frac23\log2,
\tag{L-17202.2}
\]

and define the directed auxiliary filter

\[
 G_8=(I-\tfrac18\tau_{a_1})(I-\tfrac18\tau_{a_2})G_0,
 \qquad (\tau_aH)(u)=H(u-a).
\tag{L-17202.3}
\]

Conditional on RH and on the explicit-formula and zero-census dependencies
of `L-17201`,

\[
\boxed{|Q_{G_8}(x)|<6\,10^{-18}\qquad(x\ge18).}
\tag{L-17202.4}
\]

This is a tail-domain raw-prime bound.  It does not replace `L-17201`'s
separate all-real startup constant.

## Transform and strip safety

For positive `lambda`, define

\[
 A_\lambda(z)=1-\frac18
 \exp\!\left(-\frac{\log8}{\lambda}z\right).
\tag{L-17202.5}
\]

Then

\[
 \widehat G_8(z)=\widehat G_0(z)A_{5/2}(z)A_{9/2}(z).
\tag{L-17202.6}
\]

The zeros of `A_lambda` are

\[
 z=-\lambda-\frac{2\pi i k\lambda}{\log8},
 \qquad k\in\mathbb Z.
\tag{L-17202.7}
\]

They lie on `Re z=-5/2` or `Re z=-9/2`, strictly to the left of the entire
shifted nontrivial-zero strip `-1/2<Re z<1/2`.  Thus the new factors cannot
cancel a shifted nontrivial zeta zero.  They preserve the exact pole zero of
`G_0` at `z=1/2`, and

\[
 A_{5/2}(-5/2)=A_{9/2}(-9/2)=0.
\tag{L-17202.8}
\]

Consequently the first two shifted trivial-zero residues vanish exactly.
For real `t`, the triangle inequality gives

\[
 |A_\lambda(it)|\le1+\frac18=\frac98,
\qquad
 |A_{5/2}(it)A_{9/2}(it)|\le\frac{81}{64}.
\tag{L-17202.9}
\]

The inherited `L-17201` critical-line bound therefore becomes

\[
 \sum_\rho|\widehat G_8(i\gamma)|
 <\frac{81}{64}\,4\,10^{-18}
 =5.0625\,10^{-18}.
\tag{L-17202.10}
\]

Zeros are counted with multiplicity.  Equation (L-17202.10) does not claim a
new zero computation: it inherits exactly the Arb/FLINT census and Hadamard
tail certificate of `L-17201` and `X-17202`.

## Exact support ledger

Let `R=sum_(j=1)^10 r_j`, with the exact rational widths of `L-17201`.
That lemma proves `R<17/8` and

\[
 \sup\operatorname{supp}G_0
 =\frac{31}{8}+2R+2\log2.
\tag{L-17202.11}
\]

The two directed shifts add

\[
 a_1+a_2=\frac{28}{15}\log2.
\tag{L-17202.12}
\]

Moreover

\[
 e^{7/10}>
 1+\frac7{10}+\frac1{2!}\left(\frac7{10}\right)^2
 +\frac1{3!}\left(\frac7{10}\right)^3
 =\frac{12013}{6000}>2,
\]

so `log 2<7/10`.  Hence the new terminal support endpoint `b_8` satisfies

\[
\begin{aligned}
 b_8
 &=\frac{31}{8}+2R+\frac{58}{15}\log2\\
 &<\frac{65}{8}+\frac{203}{75}
 =\boxed{\frac{6499}{600}}.
\end{aligned}
\tag{L-17202.13}
\]

Also, signed translation by each factor in (L-17202.3) multiplies the
available total-variation bound by at most `9/8`.  Since `L-17201` proves
`||G_0||_1<=3`,

\[
 \|G_8\|_1\le3\left(\frac98\right)^2=\frac{243}{64}.
\tag{L-17202.14}
\]

## Surviving trivial-zero tail

For `x>=18`, equations (L-17202.13) and (L-17202.14) give

\[
 d:=x-b_8>18-\frac{6499}{600}=\frac{4301}{600}.
\tag{L-17202.15}
\]

The shifted trivial zeros are `-lambda_m`, where
`lambda_m=2m+1/2`, `m>=1`.  The cases `m=1,2` vanish by
(L-17202.8); the first survivor is `lambda_3=13/2`, and the spacing is two.
Using the support and `L^1` bounds,

\[
\begin{aligned}
 B_{\rm triv,8}(x)
 &:=\sum_{m\ge3}e^{-\lambda_mx}
       |\widehat G_8(-\lambda_m)|\\
 &\le\frac{243}{64}
       \frac{e^{-(13/2)d}}{1-e^{-2d}}.
\end{aligned}
\tag{L-17202.16}
\]

The elementary series for `e` gives
`e>1+1+1/2+1/6+1/24=65/24>27/10`.  Since

\[
 \frac{13}{2}\frac{4301}{600}>46,
 \qquad
 2\frac{4301}{600}>14,
\]

equation (L-17202.16) has the exact rational majorant

\[
 B_{\rm triv,8}(x)
 <\frac{243}{64}
   \frac{(10/27)^{46}}{1-(10/27)^{14}}
 <5.46\,10^{-20}.
\tag{L-17202.17}
\]

For `x>=18>b_8`, the compact endpoint distribution is absent.  The pole
residue remains canceled, so the raw explicit formula contains only the
nontrivial-zero sum and the surviving trivial-zero sum.  Combining
(L-17202.10) and (L-17202.17) gives

\[
 |Q_{G_8}(x)|
 <5.0625\,10^{-18}+0.0546\,10^{-18}
 <6\,10^{-18},
\]

which proves (L-17202.4).

## Certification boundary

- `X-17203` replays all new inequalities with exact rational arithmetic and
  first invokes the rational verifier of `X-17202`.
- The first-ten zero census, `N(52.9)=10`, the `xi` reciprocal-zero enclosure,
  and the explicit-formula normalization are inherited dependencies.  No
  independent zero backend is claimed here.
- The added factors are finite signed translations.  No FFT fit, floating
  notch location, or truncated infinite convolution enters the definition.
- A violation of (L-17202.4) on a rigorously evaluated support contained in
  `[18,infinity)` would contradict RH, subject to the stated analytic and
  single-backend review dependencies.
