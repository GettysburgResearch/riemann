# L-24514 — Continuum dilation duality and Möbius uniqueness

Claim ID: `L-24514`  
Status: `PROPOSED — complete elementary continuum theorem`  
Scope: universal carry-seed obstruction  
Issue: #245

Let `B:[0,1]->R` be absolutely continuous, with

\[
B(0)=B(1)=0,
\qquad
\int_0^1\frac{|B(t)|}{t}\,dt<\infty.
\]

Put

\[
g(t)=-B'(t)
\]

and define the finite dilation sum

\[
\boxed{
(\mathcal Tg)(\theta)
=\sum_{1\le k\le1/\theta}g(k\theta)
\qquad(0<\theta\le1).
}
\tag{L-24514.1}
\]

The continuum prime-ramp envelope is

\[
h(\theta)=\theta^{-1/2}\log(1/\theta).
\tag{L-24514.2}
\]

## 1. Harmonic regularization identity

For `epsilon>0` and `N=floor(1/epsilon)`, direct substitution gives

\[
\int_\epsilon^1(\mathcal Tg)(\theta)d\theta
=\sum_{k\le N}\frac1k\int_{k\epsilon}^1g(u)du.
\tag{L-24514.3}
\]

Since `int_0^1 g=0`, this is

\[
-\int_0^1g(u)
\left[
H_N-H_{\lceil u/\epsilon\rceil-1}
\right]du,
\tag{L-24514.4}
\]

with the empty harmonic sum interpreted as zero. The elementary harmonic
asymptotic

\[
H_N-H_{\lceil u/\epsilon\rceil-1}\longrightarrow\log(1/u)
\]

and dominated truncation on `[delta,1]`, followed by `delta downarrow0`, give

\[
\boxed{
\lim_{\epsilon\downarrow0}
\int_\epsilon^1(\mathcal Tg)(\theta)d\theta
=-\int_0^1g(u)\log(1/u)du
=\int_0^1\frac{B(u)}u du.
}
\tag{L-24514.5}
\]

The last equality is ordinary integration by parts. This is the continuum
version of the exact von Mangoldt duality in `L-24501`; the harmonic numbers are
the finite cutoff regularizer.

Moreover,

\[
\boxed{
\int_0^1h(\theta)d\theta=4.
}
\tag{L-24514.6}
\]

Therefore

\[
\boxed{
\lim_{\epsilon\downarrow0}
\int_\epsilon^1
\left[h(\theta)-(\mathcal Tg)(\theta)\right]d\theta
=4-\int_0^1\frac{B(u)}u du.
}
\tag{L-24514.7}
\]

## 2. Saturation at the critical objective

Assume

\[
(\mathcal Tg)(\theta)\le h(\theta)
\quad\text{for almost every }\theta\in(0,1)
\tag{L-24514.8}
\]

and

\[
\int_0^1\frac{B(u)}u du=4.
\tag{L-24514.9}
\]

The integrand in (L-24514.7) is nonnegative and has integral zero. Hence

\[
\boxed{
(\mathcal Tg)(\theta)=h(\theta)
\quad\text{for almost every }\theta\in(0,1).
}
\tag{L-24514.10}
\]

Thus a universal continuum seed cannot retain the full critical objective while
leaving strict slack on a set of positive measure. Every positive excess must be
balanced by negative slack elsewhere.

## 3. Möbius uniqueness of the saturated profile

For finite dilation sums, ordinary Möbius inversion gives the unique formal
solution of (L-24514.10):

\[
\boxed{
g_*(t)
=\sum_{1\le k\le1/t}\mu(k)h(kt)
=t^{-1/2}
\sum_{k\le1/t}\frac{\mu(k)}{\sqrt k}
\log\frac1{kt}.
}
\tag{L-24514.11}
\]

Indeed,

\[
\sum_{m\le1/t}g_*(mt)
=\sum_{r\le1/t}h(rt)\sum_{k\mid r}\mu(k)
=h(t).
\tag{L-24514.12}
\]

Consequently every saturated continuum seed has the same derivative almost
everywhere, namely the smoothed Möbius profile (L-24514.11).

## 4. Consequence for parabolic reshaping

Finite-dimensional perturbations of the parabolic seed can move excess between
reciprocal cells, but cannot produce a non-arithmetic pointwise minorant with
objective `4`. If a perturbation makes the small-ratio excess strictly negative,
(L-24514.7) forces positive excess elsewhere unless it reconstructs the Möbius
profile.

This explains both the positive fixed-ratio band certified in `X-24502` and the
failure of smooth continuum LP reshaping as a complete closure. The remaining
theorem must transport signed excess or prove positivity of the exact
Möbius-saturated inverse.

## Relation to Lagarias

The finite harmonic difference in (L-24514.4) is the same elementary cutoff
mechanism emphasized by Lagarias's harmonic-number formulation of RH. Here it
regularizes the dilation dual; in `T-24502/L-24506` it regularizes Robin's
maximal-order divisor criterion. The two routes share a harmonic wrapper but
retain different arithmetic cores.

## Status boundary

This lemma is an exact obstruction and uniqueness theorem. It does not establish
positivity of the Möbius profile and does not prove RH.
