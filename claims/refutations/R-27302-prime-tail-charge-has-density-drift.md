# R-27302 — The prime-only tail charge has a positive `sqrt(X)/log^2(X)` drift

Claim ID: `R-27302`  
Title: The full ordinary-prime residual suffix is asymptotically positive, so prime-to-prime blocks alone cannot have subpower exterior charge  
Status: **PROPOSED COMPLETE ASYMPTOTIC REFUTATION OF `PTC` — PENDING REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: PR #248 parabolic profile; PR #265 `L-26202`; the prime number theorem  
Scope: refutes `T-27302/PTC` if the uniform finite-difference and prime-sampling steps pass review; does not refute composite-endpoint PNL

## 1. Ordinary-prime residual

For a prime \(p\le X\), put

\[
r_X(p)
=
v_p(b_X^{(0)})
-
\frac1{\sqrt p}\log\frac Xp.
\tag{R-27302.1}
\]

The proposed Prime Tail Charge satisfies

\[
C_X^{\uparrow}
\ge
\left(\sum_{p\le X}r_X(p)\right)_+,
\tag{R-27302.2}
\]

because the suffix beginning at the first prime is one of the suffixes in its
definition.

## 2. Uniform finite-difference approximation

Write

\[
b_X^{(0)}(m)=\sqrt X\,B(m/X),
\]

where

\[
B(t)=2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right],
\qquad 0<t\le1.
\]

Let

\[
g(t)=-B'(t),
\qquad
E(\theta)=
\sum_{1\le k\le1/\theta}g(k\theta)
-
\theta^{-1/2}\log(1/\theta).
\tag{R-27302.3}
\]

A one-step Taylor expansion with the explicit bound

\[
|B''(t)|
\ll
\frac{1+\log(1/t)}{t^{3/2}}
\]

and the convergent sum \(\sum k^{-3/2}\) gives, uniformly for primes
\(p\le X\),

\[
\boxed{
r_X(p)
=
\frac1{\sqrt X}E(p/X)
+
O\left(
 \frac{1+\log(X/p)}{p^{3/2}}
\right).
}
\tag{R-27302.4}
\]

The total error is

\[
\sum_{p\le X}
O\left(
 \frac{1+\log(X/p)}{p^{3/2}}
\right)
=O(\log X).
\tag{R-27302.5}
\]

## 3. Exact Mellin transform of the continuum defect

For \(\Re s>1\), finite dilation and the substitution \(u=k\theta\) give

\[
\int_0^1
\left(\sum_{k\le1/\theta}g(k\theta)\right)
\theta^{s-1}\,d\theta
=
\zeta(s)\int_0^1g(u)u^{s-1}\,du.
\tag{R-27302.6}
\]

Since \(g=-B'\) and the endpoint terms vanish,

\[
\begin{aligned}
\int_0^1g(u)u^{s-1}\,du
&=(s-1)\int_0^1B(u)u^{s-2}\,du\\
&=(s-1)\left[
 \frac{2}{(s-\frac12)^2}
 -\frac4{s-\frac12}
 +\frac4s
\right]\\
&=\frac{4(s-1)}{s(2s-1)^2}.
\end{aligned}
\tag{R-27302.7}
\]

Also

\[
\int_0^1
\theta^{s-3/2}\log(1/\theta)\,d\theta
=
\frac4{(2s-1)^2}.
\tag{R-27302.8}
\]

Therefore the Mellin transform of \(E\) is

\[
\boxed{
\mathcal M_E(s)
=
\frac4{(2s-1)^2}
\left[
 \frac{(s-1)\zeta(s)}s-1
\right].
}
\tag{R-27302.9}
\]

Using

\[
(s-1)\zeta(s)=1+\gamma(s-1)+O((s-1)^2),
\]

one obtains

\[
\boxed{
\int_0^1E(\theta)\,d\theta=0,
\qquad
\int_0^1E(\theta)\log\theta\,d\theta
=4(\gamma-1).
}
\tag{R-27302.10}
\]

In particular,

\[
-\int_0^1E(\theta)\log\theta\,d\theta
=4(1-\gamma)>0.
\tag{R-27302.11}
\]

The positivity uses only the elementary bound \(\gamma<1\).

## 4. Prime sampling asymptotic

The profile satisfies

\[
E(\theta)
\ll
\theta^{-1/2}(1+\log(1/\theta)),
\tag{R-27302.12}
\]

so \(E\), \(E\log\theta\), and \(E(\log\theta)^2\) are integrable at zero.

Apply the prime number theorem after truncating at

\[
\theta\ge(\log X)^{-8}.
\]

On the truncated interval, partial summation gives

\[
\sum_p E(p/X)
=
X\int_0^1
\frac{E(\theta)}{\log(X\theta)}\,d\theta
+o\left(\frac X{\log^2X}\right).
\tag{R-27302.13}
\]

The omitted low range is \(o(X/\log^2X)\) by (R-27302.12). Expanding

\[
\frac1{\log(X\theta)}
=
\frac1{\log X}
-
\frac{\log\theta}{\log^2X}
+
O\left(
 \frac{(\log\theta)^2}{\log^3X}
\right)
\]

and using (R-27302.10) gives

\[
\boxed{
\sum_{p\le X}E(p/X)
=
\left(4(1-\gamma)+o(1)\right)
\frac X{\log^2X}.
}
\tag{R-27302.14}
\]

Combining (R-27302.4), (R-27302.5), and (R-27302.14),

\[
\boxed{
\sum_{p\le X}r_X(p)
=
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
}
\tag{R-27302.15}
\]

## 5. Refutation of PTC

Equation (R-27302.2) now gives

\[
\boxed{
C_X^{\uparrow}
\ge
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
}
\tag{R-27302.16}
\]

Therefore

\[
C_X^{\uparrow}\ne X^{o(1)}.
\]

Subject to review of Sections 2 and 4, the `PTC` hinge of `T-27302` is false.

## 6. What survives

The exact greedy formula and proper-power neutrality of prime-endpoint blocks in
`L-27303` remain valid. What fails is the claim that prime endpoints alone can
absorb the residual with subpower exterior charge.

The positive drift has a clear origin: the continuum defect has total mass
zero, but ordinary primes sample it with density

\[
\frac1{\log(X\theta)}.
\]

The first density correction is the nonzero logarithmic moment
\(4(1-\gamma)\).

A viable neutral repair must therefore use squarefree **composite** collector
endpoints. Such a block can repair several ordinary-prime rows at once while
remaining exactly invisible to every proper prime power. This is the corrected
frontier.

## 7. Review targets

1. Check the endpoint convention in the uniform finite-difference expansion.
2. Check the Mellin integration by parts and the Laurent derivative at `s=1`.
3. Make the PNT partial-summation error uniform after the moving low cutoff.
4. Verify that the low-ratio truncation is `o(X/log^2 X)`.
5. Keep the exact block algebra of `L-27303` separate from the rejected PTC rate.

## 8. Status

```text
prime-incidence greedy algebra        RETAINED
prime-only subpower tail charge PTC   PROPOSED REFUTED
positive density drift constant       4(1-gamma)
proper-power-neutral composite lift   OPEN
Riemann Hypothesis                    UNPROVED
```
