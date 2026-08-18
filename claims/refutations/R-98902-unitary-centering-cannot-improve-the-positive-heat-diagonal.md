# R-98902 — Unitary centering cannot improve the positive heat diagonal

Claim ID: `R-98902`  
Status: **PROVED OPERATOR NO-GO FOR THE PR #613 SCHUR PAYMENT**  
Created: 2026-08-18  
Depends on: `R-98900`, `R-98901`  
RH status: **not assumed**

At a finite generalized-prime cutoff let `varepsilon(f)` be the unnormalised
exponential vector with

\[
f_q=\sqrt{\theta\lambda_\diamond(q)}q^{-1/4},
\]

let `A=dGamma(log q)`, and put

\[
H_T=e^{-A^2/(4T)}\succeq0.
\]

The signed heat packet is a parity matrix coefficient of `H_T`.  Every Schur
or Cauchy--Schwarz payment by the associated positive Gram uses the diagonal
quantity

\[
\mathfrak D_{R,\theta}(T)
=\langle\varepsilon(f),H_T\varepsilon(f)\rangle.
\]

For any unitary `U`, exact conjugation gives

\[
\boxed{
\langle U^*\varepsilon(f),U^*H_TU\,U^*\varepsilon(f)\rangle
=\mathfrak D_{R,\theta}(T).
}
\tag{R-98902.1}
\]

Thus a Weyl change of coordinates cannot reduce the positive diagonal if the
heat operator is conjugated correctly.  If the heat is not conjugated, one is
estimating a different matrix coefficient, as `R-98901` shows.

Moreover the one-particle odd-prime sector already gives, after the cutoff is
sent past `exp(T+1)`,

\[
\mathfrak D_{\theta}(T)
\ge
\theta\sum_{e^T<p\le e^{T+1}}
 p^{-1/2}e^{-(\log p)^2/(4T)}.
\tag{R-98902.2}
\]

The prime number theorem implies

\[
\boxed{
\mathfrak D_{\theta}(T)
\ge \exp((1/4-o(1))T)
}
\tag{R-98902.3}
\]

for every fixed `theta>0`; polynomial factors and the factor `theta` are
absorbed in `o(T)`.  Indeed on the displayed prime interval there are
`exp(T+o(T))` primes, while each summand is
`exp(-(3/4+o(1))T)`.

Consequently a positivity-only Schur payment by this diagonal cannot produce a
uniform exponential rate `exp(96 theta T+o(T))` for all small `theta`: for
`theta<1/384`, `96 theta<1/4`.

This does not refute the abstract scalar inequality `L-98703.1`; it proves that
the specific positive-diagonal/Weyl-centering argument in PR #613 cannot yield
that inequality.  Any valid proof would need an additional signed cancellation
theorem beyond the positive Tao/Fock Gram.
