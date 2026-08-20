# L-99580 — IHR67 is an exact relative-persistence stop-loss transform

Claim ID: `L-99580`  
Status: **PROVED EXACT FINITE-AT-EACH-SCALE THEOREM**  
Created: 2026-08-20  
Frozen parent: PR #649 at `433fd3662f7b2e4ba384ce64f196380e88624090`  
RH status: **not assumed**

## 1. Labelled threshold source

Let `V` contain:

- two labels of cost `2` and activity `2^(-1/2)`;
- one label of cost `2` and activity `2^(-3/2)`;
- one label of cost `p` and activity `p^(-1/2)` for every odd prime `p`.

Let `v_*` be one additional distinguished label of cost `67` and activity
`r=67^(-1/2)`, and put `V^+=V union {v_*}`.

For a finite subset `S` put

\[
a(S)=\sum_{v\in S}\log c(v),
\qquad
r(S)=\prod_{v\in S}r(v).
\]

At every fixed logarithmic scale `L`, only labels and subsets with `a(S)<=L`
contribute, so every expression below is finite.

Define

\[
\mathcal E_L(V^+)
=\sum_{\varnothing\ne S\subset V^+}
 (-1)^{|S|+1}r(S)(L-a(S))_+.
\tag{L-99580.1}
\]

## 2. Exact identity

Let `C_*(x)` and `W_X` be the primitive and integrated `5:3` scalar from
`L-99261/L-99262`, and put

\[
\mathfrak H_{67}(X)=W_X-rW_{X/67}.
\]

The labelled-subset Euler product is

\[
E(z)=
(1-2^{-z})^2(1-2^{-z-1})
\prod_{p\ \mathrm{odd}}(1-p^{-z}).
\]

The primitive scalar has symbol `6(1-E(z))`. Adding the distinguished label
multiplies `E(z)` by `(1-67^{-z})`. Therefore

\[
\boxed{
\frac{\mathfrak H_{67}(e^L)}6
=\mathcal E_L(V^+)-r(L-\log67)_+.
}
\tag{L-99580.2}
\]

Equivalently, define

\[
d\nu(u)=
\sum_{\varnothing\ne S\subset V^+}
 (-1)^{|S|+1}r(S)\,\delta_{a(S)}(du)
-r\,\delta_{\log67}(du).
\tag{L-99580.3}
\]

Then

\[
\boxed{
\frac{\mathfrak H_{67}(e^L)}6
=\int_{[0,L]}(L-u)\,d\nu(u).
}
\tag{L-99580.4}
\]

Thus IHR67 is exactly a stop-loss inequality for one source-specific signed
subset-product measure.

## 3. Relative quota-complex interpretation

Select every label of `V^+` independently with its stated activity. For a
selected finite label set `R`, let `K_L[R]` be the multiplicative quota complex
of subsets with log-cost at most `L`, and define its Euler persistence by

\[
\operatorname{PE}_L(K[R])
=\sum_{\varnothing\ne S\subset R}
 (-1)^{|S|+1}(L-a(S))_+.
\]

Coefficientwise expansion gives

\[
\boxed{
\frac{\mathfrak H_{67}(e^L)}6
=\mathbb E\left[
 \operatorname{PE}_L(K_L[R])
 -\mathbf1_{v_*\in R}(L-\log67)_+
\right].
}
\tag{L-99580.5}
\]

The subtraction removes only the distinguished singleton. Every mixed face
containing `v_*` remains.

## 4. Critical finite-difference identity

Put

\[
\Phi(L)=L_+e^{L/2},
\qquad
(\tau_af)(L)=f(L-a).
\]

Let

\[
\mathscr D_0=
(I-\tau_{\log2})^2
\left(I-\frac12\tau_{\log2}\right)
(I-\tau_{\log67})
\prod_{\substack{p\ \mathrm{odd}\\p\ne67}}
(I-\tau_{\log p}),
\tag{L-99580.6}
\]

where factors with shift larger than `L` act as the identity. The factor at
`67` inside `mathscr D_0` is the original prime label; the outside factor below
is the distinguished duplicate. Critical conjugation gives

\[
\boxed{
e^{L/2}\frac{\mathfrak H_{67}(e^L)}6
=(I-\tau_{\log67})(I-\mathscr D_0)\Phi(L).
}
\tag{L-99580.7}
\]

Hence IHR67 is the source-specific one-step monotonicity

\[
(I-\mathscr D_0)\Phi(L)
\ge (I-\mathscr D_0)\Phi(L-\log67).
\tag{L-99580.8}
\]

## 5. A source-specific transport certificate

Split the finite restriction of `nu` into positive and negative parts. A
sufficient certificate for (L-99580.4) is a nonnegative transport from every
negative atom at log-cost `v` into positive mass at log-costs `u<=v`, with
unused positive mass allowed. Indeed,

\[
(L-u)_+\ge(L-v)_+\qquad(u\le v).
\]

The transport must use the actual prime-log subset products and activities.
`R-99580` proves that a source-blind duplicate-label version is false.


# L-99581 — Every off-line zero forces two-sided IHR67 oscillation

Claim ID: `L-99581`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: `L-99261/L-99262` for the exact scalar transform  
RH status: **not assumed**

Put `z=s+1/2`. The exact Mellin transform is

\[
\boxed{
\int_1^\infty \mathfrak H_{67}(X)X^{-s-1}\,dX
=
\frac{1-67^{-z}}{s^2}
\left[
 6-\frac{3(2^{-z}-1)(2^{-z}-2)}{\zeta(z)}
\right].
}
\tag{L-99581.1}
\]

This holds initially for `Re(s)>1/2` and continues meromorphically to
`Re(s)>0`. The continued expression is analytic at every positive real `s`:

- at `z=1`, the reciprocal-zeta term vanishes;
- on `(1,infinity)`, the Euler product has no zero;
- on `(1/2,1)`, the alternating eta representation shows that zeta is real and
  nonzero.

Let `rho` be a nontrivial zero with `Re(rho)>1/2`. None of the explicit
multipliers vanishes there:

\[
|67^{-\rho}|<1,
\]

\[
2^{-\rho}=1\Longrightarrow\Re\rho=0,
\qquad
2^{-\rho}=2\Longrightarrow\Re\rho=-1.
\]

Thus (L-99581.1) has a genuine pole at

\[
s_0=\rho-\frac12,
\qquad \Re s_0>0,
\]

with the same multiplicity as the zeta zero.

The arithmetic definition gives
`mathfrak H_67(X)=O(sqrt(X)log(2X))`, so its Mellin integral has finite
abscissa of convergence. If `mathfrak H_67` were eventually nonnegative,
Landau's one-sign theorem would force a singularity at a positive real
abscissa. The continued expression has no such singularity. Applying the same
argument to `-mathfrak H_67` excludes eventual nonpositivity.

Therefore

\[
\boxed{
\zeta(\rho)=0,\ \Re\rho>\tfrac12
\Longrightarrow
\mathfrak H_{67}(X)>0\text{ and }\mathfrak H_{67}(X)<0
\text{ for arbitrarily large }X.
}
\tag{L-99581.2}
\]

Finite verification, however large, cannot replace the global source-specific
transport or cancellation theorem.
