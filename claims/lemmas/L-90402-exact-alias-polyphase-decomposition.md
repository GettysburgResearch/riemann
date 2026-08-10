# L-90402 — Exact alias/polyphase decomposition of an undersampled Gabor compression

Claim ID: `L-90402`  
Status: **PROPOSED COMPLETE EXACT HARMONIC-ANALYSIS LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Poisson summation; `L-90401`  
Scope: exact completed-frame algebra and resonance localization; it does not estimate the resulting prime-side cross terms and does not prove RH

## 1. Setup

Let `phi in C_c^2(R)` be supported in `[-L/2,L/2]`. Fix a frequency lattice

\[
a+kh,\qquad k\in\mathbb Z,
\]

and put

\[
P=\frac{2\pi}{h}.
\]

No relation between `P` and `L` is assumed. Define

\[
K_{a,h}(\tau,\tau')
 :=\sum_{k\in\mathbb Z}
 \widehat\phi(\tau-a-kh)
 \overline{\widehat\phi(\tau'-a-kh)}.
\tag{L-90402.1}
\]

For `r in Z`, define the overlap/polyphase profile

\[
 c_r(u):=\phi(u)\overline{\phi(u-rP)}.
\tag{L-90402.2}
\]

Only finitely many `c_r` are nonzero, because two support intervals overlap only when `|r|P<L` (up to measure-zero endpoints).

## 2. Exact alias formula

### Theorem

For all real `tau,tau'`,

\[
\boxed{
K_{a,h}(\tau,\tau')
 =P\sum_{r\in\mathbb Z}
 e^{i(\tau'-a)rP}
 \widehat c_r(\tau-\tau').
}
\tag{L-90402.3}
\]

### Proof

Expand the transforms as in `L-90401`. Poisson summation gives

\[
\sum_{k\in\mathbb Z}e^{-ikh(u-w)}
 =P\sum_{r\in\mathbb Z}\delta(u-w-rP).
\]

On the `r`-th term, `w=u-rP`; hence

\[
\begin{aligned}
&Pe^{-iarP}
 \int \phi(u)\overline{\phi(u-rP)}
 e^{i\tau u-i\tau'(u-rP)}du\\
&\qquad=P e^{i(\tau'-a)rP}
 \widehat c_r(\tau-\tau').
\end{aligned}
\]

and summing the finitely many overlap shifts proves (L-90402.3).

When `P>=L`, every `c_r` with `r!=0` vanishes and (L-90402.3) reduces to the scalar no-alias identity of `L-90401`.

## 3. Period averages and the nonnegative alias tax

For a fixed difference `x`, set `tau=t+x`, `tau'=t`. The right side of (L-90402.3) is a finite Fourier series in `t` with period `h`:

\[
K_{a,h}(t+x,t)
 =P\sum_r e^{i(t-a)rP}\widehat c_r(x).
\tag{L-90402.4}
\]

Orthogonality over one period gives the exact identities

\[
\boxed{
\frac1h\int_a^{a+h}K_{a,h}(t,t)dt
 =P\int|\phi(u)|^2du,
}
\tag{L-90402.5}
\]

and

\[
\boxed{
\frac1h\int_a^{a+h}|K_{a,h}(t+x,t)|^2dt
 =P^2\sum_{r\in\mathbb Z}|\widehat c_r(x)|^2.
}
\tag{L-90402.6}
\]

Therefore

\[
\boxed{
\frac1h\int_a^{a+h}|K_{a,h}(t+x,t)|^2dt
 \ge P^2|\widehat{|\phi|^2}(x)|^2.
}
\tag{L-90402.7}
\]

The extra nonzero terms

\[
P^2\sum_{r\ne0}|\widehat c_r(x)|^2
\]

are the **alias tax** in the translation-averaged smooth/Frobenius contribution. Aliasing does not increase the mean diagonal trace, while it adds nonnegative mean-square mass before the oscillatory prime density is used.

This is not yet a no-go theorem for the zeta application: deliberately phase-locking the alias modes to the prime frequencies can create signed cross terms against the prime part of the explicit formula. The exact location of that possible escape is the next section.

## 4. Exact phase-locking window

Let `I=[T,T+H]`. Each alias factor `e^{irP tau}` meets one prime-power frequency through

\[
\int_I e^{irP\tau}\cos(\tau\log n)d\tau.
\]

Writing the cosine as two exponentials yields

\[
\boxed{
\left|\int_I e^{irP\tau}\cos(\tau\log n)d\tau\right|
 \le
 \min\!\left(H,\frac{2}{|rP-\log n|}\right)
 +\min\!\left(H,\frac{2}{|rP+\log n|}\right).
}
\tag{L-90402.8}
\]

Thus a leading-height interaction is possible only in the narrow resonance cells

\[
|rP-\log n|\lesssim H^{-1}.
\tag{L-90402.9}
\]

In particular, choosing

\[
P=\log p
\]

for a prime `p` gives exact phase locking

\[
rP=\log(p^r)
\tag{L-90402.10}
\]

with every prime power in that Euler tower.

This is the first genuinely arithmetic multirate degree of freedom absent from the scalar Montgomery–Taylor problem.

## 5. Polyphase completion returns to the no-alias class

Take `q` equally spaced offsets

\[
a_m=a_0+\frac{mh}{q},\qquad 0\le m<q.
\]

Summing (L-90402.3) over `m` inserts

\[
\sum_{m=0}^{q-1}e^{-2\pi i mr/q}
 =q\,\mathbf1_{q\mid r}.
\]

Equivalently, the union of the `q` cosets is the finer lattice of spacing `h/q`, whose dual period is `qP`. If

\[
qP\ge L,
\]

all surviving nonzero overlaps disappear and the union collapses again to one scalar profile by `L-90401`.

Hence an offset-rich construction helps only by retaining selected alias phases; averaging or completing all phases removes precisely the new information.

## 6. Several lattices

For a finite family `(phi_j,a_j,h_j)`, sum (L-90402.3) over `j`. The completed kernel is a finite matrix-valued trigonometric polynomial in the height variable whose coefficients are the overlap transforms

\[
P_j\widehat{\phi_j(\cdot)\overline{\phi_j(\cdot-rP_j)}}.
\]

The zero-side signature blocks are unchanged: each zero still contributes one evaluation vector across the complete atom family. What changes is solely the prime-side kernel, through the alias frequencies `rP_j`.

## 7. Proof boundary

Closed exactly here:

1. the full alias/polyphase expansion (L-90402.3);
2. exact period-averaged trace and Frobenius identities;
3. the nonnegative smooth alias tax;
4. exact resonance localization and prime-power phase locking;
5. polyphase completion back to the scalar no-alias class.

Still open:

1. a prime-side asymptotic for a useful growing resonant alias bank;
2. whether signed prime interactions can more than pay the alias tax;
3. a zero-proportion improvement;
4. RH.
