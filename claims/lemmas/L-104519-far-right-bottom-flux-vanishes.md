# L-104519 — Far-right Stirling exhaustion removes the lower horizontal flux

Claim ID: `L-104519`  
Status: **PROVED ANALYTICALLY ON A TWO-LIMIT EXHAUSTION**  
Created: 2026-08-22  
Depends on: `L-104518`; Stirling's formula in the zero-free half-plane  
RH status: **not assumed**

Let

\[
F_k(z)=\Xi^{(k)}(z),
\qquad
E_k(z)=F_k(z)-i\lambda F_{k+1}(z),
\qquad
\lambda>0.
\]

On the lower horizontal line

\[
z=x-iH,
\qquad |x|\le T,
\]

put

\[
s=\frac12+iz=\frac12+H+ix.
\]

Thus `H->infinity` in the `z`-plane is the classical far-right zero-free
half-plane for `xi(s)`.

## 1. Uniform derivative-ratio asymptotics

Write

\[
a(s)=\frac{d}{ds}\log\xi(s).
\]

Stirling's formula and the absolutely convergent Euler product give, uniformly
for `|Im s|<=T`,

\[
a(s)
=
\frac12\log\frac{s}{2\pi}
+
O_T\!\left(\frac1{|s|}\right),
\tag{L-104519.1}
\]

and

\[
a^{(j)}(s)=O_{j,T}(|s|^{-j})
\qquad(j\ge1).
\tag{L-104519.2}
\]

The complete Bell-polynomial formula for derivatives of `exp(log xi)` yields,
for every fixed `K` and uniformly for `0<=k<=K`,

\[
\frac{\xi^{(k)}(s)}{\xi(s)}
=
a(s)^k
\left[
1+
O_{K,T}\!\left(
\frac1{H\log^2H}
\right)
\right].
\tag{L-104519.3}
\]

More generally the estimate remains uniform for a moving `K=K(H)` whenever

\[
\frac{K(H)^2}{H\log^2H}\longrightarrow0.
\tag{L-104519.4}
\]

Consequently

\[
\frac{\xi^{(k+1)}(s)}{\xi^{(k)}(s)}
=
a(s)
+
O_{K,T}\!\left(\frac1{H\log H}\right).
\tag{L-104519.5}
\]

Since `d/dz=i d/ds`,

\[
\frac{F_{k+1}(z)}{F_k(z)}
=
ia(s)
+
O_{K,T}\!\left(\frac1{H\log H}\right).
\tag{L-104519.6}
\]

## 2. Companion nonvanishing and ratio cancellation

Equation (L-104519.6) gives

\[
E_k(z)
=
F_k(z)
\left[
1+\lambda a(s)
+
O_{K,T}\!\left(\frac1{H\log H}\right)
\right].
\tag{L-104519.7}
\]

The bracket is nonzero for all sufficiently large `H`, uniformly for
`|x|<=T` and `k<=K`.

Furthermore,

\[
\boxed{
\frac{E_k'(z)}{E_k(z)}
-
\frac{E_{k+1}'(z)}{E_{k+1}(z)}
=
O_{K,\lambda,T}\!\left(\frac1{H\log H}\right).
}
\tag{L-104519.8}
\]

The common gamma carrier `ia(s)` cancels before the estimate is taken.

## 3. Lower horizontal charge tends to zero

Let the lower side be oriented from `T-iH` to `-T-iH`.  Its charge satisfies

\[
\boxed{
\left|
{1\over2\pi i}
\int_{T-iH}^{-T-iH}
\left(
\frac{E_k'}{E_k}
-
\frac{E_{k+1}'}{E_{k+1}}
\right)dz
\right|
\ll_{K,\lambda,T}
\frac{T}{H\log H}.
}
\tag{L-104519.9}
\]

Hence it tends to zero as `H->infinity`.

For a finite derivative ladder `0<=k<=r(T)`, choose `H=H(T)` after the
derivative order so that

\[
\frac{r(T)^2T}{H(T)\log H(T)}\longrightarrow0.
\tag{L-104519.10}
\]

Then the lower-side charge vanishes **simultaneously at every level of that
finite ladder**.

## 4. Consequence for the corrected last-defect theorem

At finite `H`, `L-104518` remains the exact statement and the complete exterior
boundary must be retained.

Under the ordered exhaustion

```text
first choose the finite derivative ladder and the real height T;
then send H to infinity subject to (L-104519.10),
```

the lower horizontal term vanishes.  The corrected exterior gate becomes a
genuine two-vertical-side limit:

\[
\boxed{
\mathrm{EFLUX104518}
\quad\rightsquigarrow\quad
\mathrm{VFLUX}_{\infty,104519}.
}
\]

This does not prove that the limiting vertical flux is zero.  It proves that
there is no third bottom-boundary obstruction and repairs the earlier
vertical-only formulation with an explicit limiting protocol.
