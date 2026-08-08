# L-26205 — Parity-paired Euler-fiber frame and positive summed forcing

Claim ID: `L-26205`  
Status: `PROPOSED COMPLETE — exact two-channel source algebra and strip reserve pending independent review`  
Scope: a fixed two-channel strengthening of the Euler-fiber source; no RH input  
Date: 2026-08-08  
Depends on: `L-26202`, `L-26204`; PR #241 `L-9518`

Let

\[
\chi_2(n)=(-1)^{v_2(n)}.
\tag{L-26205.1}
\]

This is a completely multiplicative real character. Put

\[
b_+(n)=b_{\mathcal E}(n),
\qquad
b_-(n)=\chi_2(n)b_{\mathcal E}(n),
\tag{L-26205.2}
\]

and define `a_+-`, `Lambda_+-`, and `C_+-` by the same twist:

\[
a_-=\chi_2a_+,
\qquad
\Lambda_-=\chi_2\Lambda_+,
\qquad
C_-=\chi_2C_+.
\tag{L-26205.3}
\]

Here

\[
C_\pm=b_\pm*(a_\pm\log^2)
=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\tag{L-26205.4}
\]

All identities follow because a completely multiplicative twist commutes with Dirichlet convolution and with multiplication by `log n`.

## 1. Two local Euler phases

Let

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2.
\tag{L-26205.5}
\]

Writing

\[
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\]

one has

\[
\boxed{
B_+(s)=p(2^{-s})\mathcal O(s),
\qquad
B_-(s)=p(-2^{-s})\mathcal O(s).
}
\tag{L-26205.6}
\]

Both channels retain every zero of `zeta(s)` in the open critical strip. The extra local factors have zeros only on boundary lines.

## 2. Exact closed-strip frame reserve

Let `z` be complex with

\[
\frac12\le |z|\le\frac1{\sqrt2}.
\tag{L-26205.7}
\]

Then

\[
\boxed{
|p(z)|^2+|p(-z)|^2\ge\frac{45}{4}.
}
\tag{L-26205.8}
\]

### Proof

Put

\[
x=|z|^2\in[1/4,1/2],
\qquad
u=\cos(2\arg z)\in[-1,1].
\]

Direct expansion gives

\[
\begin{aligned}
\frac12\bigl(|p(z)|^2+|p(-z)|^2\bigr)
={}&16\nu^2x^2\\
&+\nu\Bigl[(32+48\sqrt2)x^3
 +(68+48\sqrt2)x^2
 +(8+12\sqrt2)x\Bigr]\\
&+16x^4+(68+48\sqrt2)x^3\\
&+(80+48\sqrt2)x^2+(17+12\sqrt2)x+1.
\end{aligned}
\tag{L-26205.9}
\]

The derivative with respect to `nu` is positive throughout `[-1,1]`, because its value at `nu=-1` is

\[
2\Bigl[(32+48\sqrt2)x^3
 +(36+48\sqrt2)x^2
 +(8+12\sqrt2)x\Bigr]>0.
\]

Hence the minimum occurs at `nu=-1`. There

\[
|p(z)|^2+|p(-z)|^2
=2(x+1)(2x+1)^2(4x+1).
\tag{L-26205.10}
\]

This is increasing for `x>0`; at `x=1/4` it equals `45/4`.

The minimum is attained at `z=+- i/2`.

## 3. Comparison with the unfiltered inverse-zeta source

For `1/2<=Re s<=1`, put `z=2^{-s}`. Since

\[
\frac1{\zeta(s)}=(1-z)\mathcal O(s),
\]

(L-26205.8) gives

\[
\boxed{
|B_+(s)|^2+|B_-(s)|^2
\ge
\frac{45}{4(1+1/\sqrt2)^2}
\left|\frac1{\zeta(s)}\right|^2.
}
\tag{L-26205.11}
\]

The reverse comparison also holds with one absolute constant, because the local factors are bounded on the closed annulus and

\[
|1-z|\ge1-1/\sqrt2.
\]

Thus the paired source is uniformly equivalent to the original inverse-zeta source on the entire closed critical strip, not merely on a compact substrip.

## 4. Positive summed Selberg forcing

By `L-26202`,

\[
C_+(n)\ge0
\qquad(n\ge1).
\]

Equation (L-26205.3) therefore gives

\[
\boxed{
C_+(n)+C_-(n)
=\bigl(1+\chi_2(n)\bigr)C_+(n)
\ge0.
}
\tag{L-26205.12}
\]

The sum vanishes when `v_2(n)` is odd and equals `2C_+(n)` when `v_2(n)` is even.

Applying the independent-frequency reflected identity of PR #241 separately to the two channels and adding gives the exact paired Hermitian energy. Equation (L-26205.12) is a genuine coefficientwise positivity gain. It is not, by itself, an upper bound for a physical block; the inverse pairs and every cross term must remain in the production ledger.

## 5. Parity orthogonalization of the five-tap fiber

Let `Z_+` and `Z_-` be the compact signals formed with the same real window and the two sources. Put

\[
Z_{\rm ev}=\frac{Z_++Z_-}{2},
\qquad
Z_{\rm odd}=\frac{Z_+-Z_-}{2}.
\tag{L-26205.13}
\]

Then `Z_ev` contains exactly the coefficients with even `v_2`, while `Z_odd` contains exactly those with odd `v_2`, and

\[
\boxed{
\|Z_+\|_2^2+\|Z_-\|_2^2
=2\|Z_{\rm ev}\|_2^2+2\|Z_{\rm odd}\|_2^2.
}
\tag{L-26205.14}
\]

For one odd squarefree core, the normalized local taps from `L-26204` split as

\[
\boxed{
\begin{array}{c|ccc}
\text{even }v_2&1&2+3\sqrt2&1\\
\text{positions}&0&2&4
\end{array}}
\tag{L-26205.15}
\]

and

\[
\boxed{
\begin{array}{c|cc}
\text{odd }v_2&-\left(2+\frac{3\sqrt2}{2}\right)&-\left(2+\frac{3\sqrt2}{2}\right)\\
\text{positions}&1&3.
\end{array}}
\tag{L-26205.16}
\]

Each parity subfiber is sign-complete. The paired energy removes every even/odd two-adic cross term while retaining all odd-prime Möbius signs and all same-sign odd Möbius cubes.

## 6. Paired fixed-source RH criterion

For any fixed compact real window whose transform has no zeros in the open centered strip, the sum of the two fixed block energies is subexponential if and only if RH. This follows from (L-26205.11), the reverse local comparison, and the same block-Laplace theorem used for the fixed-ratio shell.

The paired source therefore supplies a stronger proof-facing target than one scalar Euler fiber:

```text
closed-strip multiplier reserve
+ coefficientwise positive summed forcing
+ exact parity-channel orthogonalization.
```

It still requires a source-specific physical-block upper estimate.

## 7. Proof boundary

Closed exactly:

- the twisted inverse/source algebra;
- the sharp `45/4` local frame reserve;
- closed-strip equivalence with `1/zeta`;
- coefficientwise positivity of the summed Selberg forcing;
- parity orthogonalization and sign-complete subfibers.

Not closed:

- a paired two-frequency block contraction;
- a strict lower-scale recurrence;
- RH.
