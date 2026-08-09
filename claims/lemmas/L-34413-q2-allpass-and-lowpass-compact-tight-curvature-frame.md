# L-34413 — Q2 all-pass and the low-pass/compact tight curvature frame

Claim ID: `L-34413`  
Title: Over the Möbius odd-Jordan path, the radix-two Euler–Blaschke factor gives an exact coefficient-one block telescope; eliminating its root state produces a tight frame between the corrected low-pass source and the Q2 compact source  
Status: **PROPOSED COMPLETE EXACT INDEPENDENT-FREQUENCY/CURVATURE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; `L-34409`; odd-prime Jordan deformation  
Scope: aligned logarithmic blocks and aligned integer rows; no dissipative estimate for either output and no RH conclusion

## 1. Three radix-two filters

Put

\[
z=2^{-s},\qquad \ell=\log2,
\]

and retain

\[
 g_\tau(s)=\frac1{\zeta(s)}J_{{\rm odd},\tau}(s).
\]

Define

\[
\boxed{
p_\tau=(1+z)g_\tau,
\qquad
r_\tau=(1-z)g_\tau,
\qquad
c_\tau=(1-2z)g_\tau.
}
\tag{L-34413.1}

The sources at `tau=0` are respectively

\[
(\varepsilon+\delta_2)\mu,
\qquad
(\varepsilon-\delta_2)\mu,
\qquad
(\varepsilon-2\delta_2)\mu.
\]

Thus `p` is the corrected odd-relative low-pass source of `L-34409`, `r` is the zero-bare-charge root source, and `c` is the denominator-free Q2 main-pole source.

All three filters are independent of the Jordan parameter.

## 2. Exact Q2 all-pass factor

On the critical line put

\[
w=\sqrt2\,z,
\qquad |w|=1,
\qquad a=2^{-1/2}.
\]

Then

\[
\frac{1-2z}{1-z}
=\sqrt2\frac{a-w}{1-aw}.
\tag{L-34413.2}
\]

The scalar factor

\[
\phi_2(w)=\frac{a-w}{1-aw}
\]

is all-pass, and its reservoir is

\[
R_2(s)=\frac{\sqrt{1-a^2}}{1-aw}
=\frac{1/\sqrt2}{1-z}.
\tag{L-34413.3}

Therefore

\[
\boxed{c_\tau=\sqrt2\,\phi_2 r_\tau,}
\tag{L-34413.4}
\]

and the reservoir denominator cancels exactly:

\[
\boxed{R_2r_\tau=\frac1{\sqrt2}g_\tau.}
\tag{L-34413.5}

## 3. Independent-frequency block telescope

Let `B_I` denote the exact two-frequency physical block Gram of PR #241.  The all-pass identity of PR #339 gives

\[
B_I(f)-B_I(\phi_2f)
=B_I(R_2f)-B_{I-\ell}(R_2f).
\]

Apply this with `f=r_tau`, multiply by two, and use (L-34413.4)--(L-34413.5):

\[
\boxed{
2B_I(r_\tau)-B_I(c_\tau)
=B_I(g_\tau)-B_{I-\ell}(g_\tau).
}
\tag{L-34413.6}

Every term uses the same independent-frequency kernel.  There is no one-frequency localization or unidentified transference.

Differentiating in the imaginary odd-Jordan direction yields

\[
\boxed{
\mathfrak C_I(c)+\mathfrak C_I(g)
=2\mathfrak C_I(r)+\mathfrak C_{I-\ell}(g).
}
\tag{L-34413.7}

Since the root source has bare charge zero, its source curvature is a pure current square.

## 4. Exact low-pass/root Haar identity

The filters `1+z` and `1-z` have cancelling cross terms.  Since multiplication by `z=2^{-s}` is a delay by `ell` with squared critical amplitude `1/2`, the complete block identity is

\[
\boxed{
B_I(p_\tau)+B_I(r_\tau)
=2B_I(g_\tau)+B_{I-\ell}(g_\tau).
}
\tag{L-34413.8}

Again differentiation commutes with every filter, giving

\[
\boxed{
\mathfrak C_I(p)+\mathfrak C_I(r)
=2\mathfrak C_I(g)+\mathfrak C_{I-\ell}(g).
}
\tag{L-34413.9}

This is the critically weighted form of the Möbius Haar identity in `L-34409`.

## 5. Eliminate the root state

Multiply (L-34413.9) by two and substitute (L-34413.7).  The root curvature cancels exactly:

\[
\boxed{
2\mathfrak C_I(p)+\mathfrak C_I(c)
=3\mathfrak C_I(g)
 +3\mathfrak C_{I-\ell}(g).
}
\tag{L-34413.10}

The same equality holds for the complete two-frequency block Grams before differentiation:

\[
\boxed{
2B_I(p_\tau)+B_I(c_\tau)
=3B_I(g_\tau)+3B_{I-\ell}(g_\tau).
}
\tag{L-34413.11}

Thus the pair

```text
corrected low-pass source  p=(1+2^-s)g,
Q2 compact source          c=(1-2^(1-s))g
```

is an exact tight output frame for the current base state and its immediate predecessor.  The root source is its internal all-pass state, not an additional unresolved species.

## 6. Aligned row form

Let

\[
Q_0(e)=\mathcal L_e(\mu*\Lambda_{\rm odd}).
\]

At the row `2e`, aligned scaling gives

\[
\boxed{
Q_p(2e)=Q_0(2e)+Q_0(e),
}
\tag{L-34413.12}

\[
\boxed{
Q_r(2e)=Q_0(2e)-Q_0(e),
}
\tag{L-34413.13}

and

\[
\boxed{
Q_c(2e)=Q_0(2e)-2Q_0(e).
}
\tag{L-34413.14}

At the level of first-current squares, (L-34413.10) contains the elementary orthogonality

\[
\boxed{
2|Q_0(2e)+Q_0(e)|^2
+|Q_0(2e)-2Q_0(e)|^2
=3|Q_0(2e)|^2+6|Q_0(e)|^2.
}
\tag{L-34413.15}

The second-current/bare-source terms obey the same weighted identity because it was derived from the complete Jordan paths, not added after the current calculation.

## 7. What this changes

The scale-two root detail can now be eliminated exactly between two source-complete identities.  The final recurrence may be sought in either equivalent coordinate:

```text
base + predecessor states;

or

2 x corrected low-pass output
+ 1 x Q2 compact output.
```

The output frame is finite and parameter independent.  It does not by itself upper-bound either output curvature.  In particular, positivity of their scalar reserves is not enough; `L-34412` still requires the complete polarized output jet matrix or an equivalent reflected dissipative orientation.

## 8. Proof boundary

Closed exactly:

1. Q2 Euler–Blaschke factorization;
2. reservoir cancellation;
3. independent-frequency block telescope;
4. low-pass/root Haar block identity;
5. exact elimination of the root state;
6. tight low-pass/Q2 compact curvature frame;
7. aligned row current formulas.

Open:

1. dissipative control of the two tight-frame output curvatures;
2. a coefficient-one global recurrence;
3. RH.
