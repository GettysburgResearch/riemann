# Whole-matrix attack addendum: exact alias factorization and the intrinsic strip boundary

Agent: `gpt56-pro-09-n`  
Date: 2026-08-07  
PR: #202  
Classification: exact algebraic bridges plus one decisive scope correction; **RH not claimed proved**

## New durable results after the initial report

The first report introduced the whole-matrix diagonal theorem, a rank-one
support large sieve, and a subexponential smooth source frame.  This addendum
records the source/periodization audit that followed.

New files:

```text
L-19820  periodized radical and alias-corrected tail factorization
L-19821  positive operator Riemann--von Mangoldt local Weyl theorem
L-19822  two-end zero-orbit phase decomposition
R-19805  source conditioning cannot radialize complete zero evaluations
```

## 1. Exact periodization bridge

For a global radical vector `r=E(f)`, let `t` be its exterior tail and fold that
tail back into the fundamental interval.  If `e` is the high Fourier remainder
of the periodization, the complete corrected tail is

\[
 W=t-\iota\mathfrak Ft+\iota e.
\]

The finite periodized source vector satisfies exactly

\[
 \iota P_N\Sigma r=r-W.
\]

Hence

\[
 \boxed{
 Q_W(\iota P_N\Sigma r,
     \iota P_N\Sigma r')
 =Q_W(W,W').
 }
\]

This closes the abstract source/finite-matrix bridge.  The correct profile Gram
is the Gram of the complete corrected tail; using only the ordinary exterior
tail omits correlated Poisson and Fourier terms.

## 2. Line-centered matrix is an elementary positive local-Weyl problem

For a positive operator profile `Phi_R(u)`, the line-centered zero matrix is a
Stieltjes sum against the full zero-counting function.  Riemann--von Mangoldt
and one integration by parts give

\[
 A_R^0=(\log R)D_R+C_R+E_R,
\]

with

\[
 \|E_R\|_{\widehat D_R}
 \ll{(1+B_R)\log R\over R},
\]

where `B_R` is the profile-derivative Gram envelope.  The same calculation gives
the Bessel upper bound

\[
 \sum_\gamma\Phi_R(\gamma/R)^*\Phi_R(\gamma/R)
 \preceq CR\log R\,\widehat D_R.
\]

This supplies both the positive main term and the second-factor energy needed by
the rank-one large sieve.

## 3. Exact zero-orbit phase ledger

After extracting the two support endpoints,

\[
 U_R(z)=e^{iLz/2}A_+(z)+e^{-iLz/2}A_-(z).
\]

The conjugate horizontal orbit splits into four channels.  Same-end products
have no support phase; cross-end products retain `exp(+-iL gamma)`, including
all potentially large horizontal factors.  Therefore the oscillatory part is
exactly rank-one and the nonoscillatory part is exactly the horizontal amplitude
channel.  No member of the zero quartet is omitted.

## 4. Decisive scope correction

At every actual zeta zero `z_rho`, global radicality and the corrected-tail
identity imply

\[
 \boxed{
 \widehat W(z_\rho)=-\widehat y(z_\rho),
 \qquad
 \partial_z\widehat W(z_\rho)
 =-\partial_z\widehat y(z_\rho).
 }
\]

Thus the complete source right inverse cannot alter the target's zero
evaluations or horizontal derivatives.

On `L^2([-L/2,L/2])`, the evaluation and derivative norms are

\[
 \|e_{\gamma+i\delta}\|^2
 =\int_{-L/2}^{L/2}e^{2\delta t}dt,
\]

\[
 \|t e_{\gamma+i\delta}\|^2
 =\int_{-L/2}^{L/2}t^2e^{2\delta t}dt.
\]

On the centered line their squared ratio is `L^2/12`.  Dense finite Fourier
spaces converge to these values.  Therefore a complete source frame cannot
justify a horizontally flat profile merely from its good coefficient graph.

This does not refute the whole-matrix theorem.  It refutes one proposed
producer for its same-end off-line channel.

## 5. What the global attack has genuinely accomplished

The following issues are now separated cleanly.

### Closed

```text
finite lower envelope -> global Weil positivity -> RH;
rapid Gevrey diagonal density;
rank-one support averaging with one-factor conditioning loss;
subexponential exact smooth source interpolation;
periodization/restriction/alias algebra;
positive line-centered local Weyl and Bessel bounds;
complete conjugate-orbit phase bookkeeping.
```

### Still RH-sensitive

```text
same-end horizontal orbit domination on a dense finite diagonal.
```

It cannot be replaced by source conditioning or by a small horizontal derivative
for the complete Fourier space.

## 6. Three honest full-problem continuations

1. **Prime-side whole-matrix factorization.**  Establish the finite lower
   envelope directly from Suzuki's exact jump/prime form, bypassing horizontal
   zero evaluation.
2. **Strip-stable form core.**  Construct a growing form-dense diagonal whose
   zero-evaluation profile has a genuine horizontal contraction.  Ordinary
   complete Fourier spaces are excluded by `R-19805`.
3. **Direct same-end sampling domination.**  Prove that the positive
   line-centered zero-sampling Gram dominates its conjugate horizontal orbit at
   critical density, retaining the complete two-end cross interaction.

The third is the sharpest continuation of the current source/zero-side stack.
It is a matrix sampling/de Branges inequality, not another scalar sign
criterion.

## Exact status

The pass produced a serious global architecture and closed several external
bridges, but did not prove the same-end domination.  Therefore RH remains
unresolved.
