# L-15119 — Exact arithmetic source of the truncated Weil special matrix

Claim ID: `L-15119`  
Status: **PROVED FORMULA AUDIT; DIRECTED PRODUCER NOT YET RUN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: Connes--Consani--Moscovici, *Zeta Spectral Triples*, equations (2.9), (3.13)--(3.16), (4.2)--(4.14), and (5.2)  
Scope: the actual arithmetic residue-line / threshold stage  
Related counterexample candidates: none

## 1. Conventions

Let

\[
 L=2\log\lambda,
 \qquad
 U_n(x)=L^{-1/2}e^{2\pi inx/L},
 \qquad |n|\le N,
\]

and let `V_n` be the transported basis on `[lambda^-1,lambda]`.  The truncated
Weil matrix has the special form

\[
 Q_{nn}=a_n,
 \qquad
 Q_{nm}=\frac{\beta_n-\beta_m}{n-m}
 \quad(n\ne m),
 \tag{L-15119.1}
\]

with `beta_-n=-beta_n`.  Addition of one constant to every `beta_n` is
irrelevant.

Write

\[
 \rho(x)=\frac{e^{x/2}}{e^x-e^{-x}}.
\]

## 2. Polar/end-point source

The `W_(0,2)` off-diagonal matrix is

\[
 32L\sinh^2(L/4)
 \frac{L^2-16\pi^2mn}
 {(L^2+16\pi^2m^2)(L^2+16\pi^2n^2)}.
\]

It is the divided-difference matrix of

\[
 \boxed{
 \beta_n^{(0,2)}
 =32L\sinh^2(L/4)
   \frac{n}{L^2+16\pi^2n^2}.}
 \tag{L-15119.2}
\]

Indeed the numerator after subtraction is

\[
 n(L^2+16\pi^2m^2)-m(L^2+16\pi^2n^2)
 =(n-m)(L^2-16\pi^2mn).
\]

## 3. Archimedean source

Define

\[
 \boxed{
 \alpha_L(n)
 =\frac1\pi\int_0^L
   \sin\left(\frac{2\pi nx}{L}\right)\rho(x)\,dx.}
 \tag{L-15119.3}
\]

The off-diagonal archimedean matrix `W_R` is

\[
 (W_R)_{nm}
 =\frac{\alpha_L(m)-\alpha_L(n)}{n-m}.
\]

Thus its special source is `-alpha_L(n)`.  Since the Weil form is

\[
 Q_W=W_{0,2}-W_R-\sum_pW_p,
\]

the archimedean contribution to the source of `Q_W` is

\[
 \boxed{+\alpha_L(n).}
 \tag{L-15119.4}
\]

The paper supplies rapidly convergent hypergeometric/digamma expressions for
(L-15119.3), but the integral itself is the clean proof-facing definition.

## 4. Complete prime-power source

For `q=p^a`, put `Lambda(q)=log p`.  The prime matrix uses

\[
 q(U_n,U_m)(\log q)
 =\frac{
   \sin(2\pi m\log q/L)-
   \sin(2\pi n\log q/L)
 }{\pi(n-m)}.
\]

Therefore `W_p` has source

\[
 -\frac1\pi
 \sum_{1<q\le e^L}
 \frac{\Lambda(q)}{\sqrt q}
 \sin\left(\frac{2\pi n\log q}{L}\right).
\]

After the minus sign in the Weil form, the arithmetic prime-power source is

\[
 \boxed{
 \beta_n^{\rm pp}
 =\frac1\pi
 \sum_{1<q\le e^L}
 \frac{\Lambda(q)}{\sqrt q}
 \sin\left(\frac{2\pi n\log q}{L}\right).}
 \tag{L-15119.5}
\]

This is a finite sum over **all** prime powers, not only ordinary primes.

## 5. Total arithmetic source

Combining the three off-diagonal channels gives the exact source

\[
 \boxed{
 \beta_n^{\rm Weil}(L)
 =32L\sinh^2(L/4)
   \frac{n}{L^2+16\pi^2n^2}
 +\alpha_L(n)
 +\frac1\pi
  \sum_{1<q\le e^L}
  \frac{\Lambda(q)}{\sqrt q}
  \sin\left(\frac{2\pi n\log q}{L}\right).}
 \tag{L-15119.6}
\]

The diagonal entries of the raw Weil matrix contain additional scalar terms.
They are irrelevant to the special source and are replaced uniquely by the
kernel-pinning diagonal when `T_p(c)` is formed.

The arithmetic target-pinned line has source

\[
 \boxed{
 \beta_n^{\rm Weil}(L)-cn,}
 \tag{L-15119.7}
\]

modulo addition of an arbitrary constant.  This is the only non-circular
completion family in the Finsler/Bézoutian program.

## 6. Directed production

A proof object for (L-15119.6) requires:

1. exact `L`, node range, and normalization;
2. a complete prime-power manifest through `e^L`;
3. directed `log q`, square-root, sine, and scalar accumulation;
4. a directed enclosure of the archimedean integral (or of the equivalent
   special-function formula);
5. a directed enclosure of `sinh(L/4)`;
6. the exact odd-parity checks `beta_-n=-beta_n` and `beta_0=0`;
7. an independent reconstruction of every off-diagonal matrix entry from the
   source differences.

Once the actual target coefficients are supplied by `L-15117`, the canonical
source from `L-15118` and the arithmetic source above live in exactly the same
node and phase coordinates.

## 7. New comparison target

Let

\[
 g_n=-\frac{P'(n)}{P(n)}
\]

be the canonical Herglotz source.  The proof problem is not to show merely that
`P` is real-rooted.  It is to find one scale `a>0`, boundary scalar `c`, and
constant `d` for which

\[
 \beta_n^{\rm Weil}(L)
 \approx a g_n+cn+d
\]

strongly enough, relative to the canonical positive moat, to keep the complete
special matrix positive.  `L-15120` gives the scale-invariant exact theorem.

## 8. Gap audit

1. Signs depend on the convention
   `Q_nm=(beta_n-beta_m)/(n-m)`; reversing either denominator reverses the
   displayed source.
2. The finite prime sum includes higher powers exactly once.
3. Ordinary numerical cancellation in (L-15119.5) is not a directed enclosure.
4. The raw diagonal of the Weil matrix is not used as the target-pinning
   diagonal.
5. Formula (L-15119.6) supplies finite arithmetic data; it does not establish
   any cofinal comparison with the canonical source.