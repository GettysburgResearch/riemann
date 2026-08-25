# T-106590 — Macroscopic height collapses to microscopic companion correlation

Claim ID: `T-106590`  
Status: **UNCONDITIONAL ZERO-DENSITY AND FINITE OPERATOR THEOREMS; ENDLOC106590 AND SHALLOWCORR106590 OPEN**  
Created: 2026-08-25  
Depends on: Selberg's zero-density theorem; `L-106500--L-106514`; finite differentiator compression and model-space factorization; pinned `R_5/N>997/1000-o(1)` input  
RH status: **unproved**

This packet is deliberately numbered outside the concurrently occupied
`T-106550` spectral-pressure namespace.

## 1. Unconditional horizontal first moment

For zeta zeros `rho=beta+i gamma`, counted with multiplicity, define

\[
\mathfrak h_\zeta(T)
 =\sum_{T<\gamma\le2T}
  \left|\beta-\frac12\right|.
\tag{T-106590.1}
\]

Functional-equation symmetry gives the exact layer cake

\[
\boxed{
\mathfrak h_\zeta(T)
 =2\int_{1/2}^{1}N(\sigma;T,2T)\,d\sigma.
}
\tag{T-106590.2}
\]

Selberg's uniform zero-density estimate

\[
N(\sigma,X)
 \ll X^{1-\frac14(\sigma-1/2)}\log X
\]

therefore yields

\[
\boxed{
\mathfrak h_\zeta(T)=O(T)
 =o(N(T,2T)).
}
\tag{T-106590.3}

In the centered Xi variable this is exactly the total vertical-height mass of
the Xi zero divisor in the dyadic real window.

It also gives, for fixed `A>0`,

\[
N\!\left(\frac12+{A\over\log T};T,2T\right)
 \ll e^{-A/4}N(T,2T),
\tag{T-106590.4}
\]

and all but `o(N)` zeros lie in every strip

\[
\left|\beta-\frac12\right|
 <{A(T)\over\log T}
\qquad(A(T)\to\infty).
\tag{T-106590.5}

## 2. Exact finite derivative and companion height theorem

For a polynomial `p` put

\[
\mathfrak h_+(p)
 =\sum_{p(z)=0}(\Im z)_+.
\]

If `A=diag(z_1,...,z_n)` and
`e=n^(-1/2)(1,...,1)^T`, the zeros of `p'/n` are the eigenvalues of the
compression of `A` to `e^perp`. Schur triangularization and Ky Fan's
variational principle give

\[
\boxed{
\mathfrak h_+(p^{(k)})\le\mathfrak h_+(p)
\qquad(0\le k<n).
}
\tag{T-106590.6}

The matrix determinant lemma gives

\[
\begin{aligned}
p+i\lambda p'
 &=\det(zI-A+i\lambda n ee^*),\\
p-i\lambda p'
 &=\det(zI-A-i\lambda n ee^*).
\end{aligned}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathfrak h_+(p+i\lambda p')
 &\le\mathfrak h_+(p),\\
\mathfrak h_+(p-i\lambda p')
 &\le\mathfrak h_+(p)+\lambda n.
\end{aligned}
}
\tag{T-106590.7}

For odd fixed `K`, `q=p^(K)`, and

\[
D_{K,\lambda}=(p+i\lambda p')(q-i\lambda q'),
\]

one obtains

\[
\boxed{
\mathfrak h_+(D_{K,\lambda}^{\rm red})
 \le2\mathfrak h_+(p)+\lambda(n-K).
}
\tag{T-106590.8}

Common-factor reduction can only decrease the left side.

## 3. Every deep model-space direction is paid by height

Let a reduced finite endpoint symbol be

\[
U=\omega B_+\overline{B_-},
\]

with denominator zeros `b_j=a_j+i y_j`.  For `eta>0`, factor

\[
B_-=B_{\le\eta}B_{>\eta}.
\]

The model space decomposes orthogonally:

\[
K_{B_-}
 =K_{B_{\le\eta}}
  \oplus B_{\le\eta}K_{B_{>\eta}}.
\]

Using the exact charge identity

\[
\|H_U\|_{S_2}^2
 =\operatorname{tr}
  (T_{B_+}^*P_{K_{B_-}}T_{B_+}),
\]

one gets

\[
\boxed{
\|H_U\|_{S_2}^2
 =\mathcal C_{\le\eta}(U)
  +\mathcal C_{>\eta}(U),
}
\tag{T-106590.9}
\]

with no cross term.  Since each deep direction costs at most one,

\[
\boxed{
\mathcal C_{>\eta}(U)
 \le\deg B_{>\eta}
 \le {\sum_jy_j\over\eta}.
}
\tag{T-106590.10}

Thus, whenever the endpoint denominator has total height `o(N)`, one may
choose `eta_T->0` with

\[
{\sum_jy_j\over\eta_T}=o(N)
\]

and obtain

\[
\boxed{
\|H_{U_T}\|_{S_2}^2
 \le\mathcal C_{\le\eta_T}(U_T)+o(N).
}
\tag{T-106590.11}

The only possible power-sized adverse charge is supported on a
vanishing-height companion model space.

## 4. The two literal remaining statements

Define `ENDLOC106590`:

```text
The regular finite canonical-product exhaustion consumed by the fifth-endpoint
index has the same reduced companion divisor as the actual Xi endpoint, up to
an o(N) endpoint/confluent ledger, and its denominator upper-height sum is
o(N).
```

Equations (T-106590.2)--(T-106590.8) prove all finite and zero-density inputs;
`ENDLOC106590` is only the cofinal window/product-tail identification.

Assuming it, choose `eta_T` as above and define

\[
\mathfrak C_{\rm sh}(T)
 =\|P_{K_{B_{-,T}^{\le\eta_T}}}T_{B_{+,T}}\|_{S_2}^2.
\tag{T-106590.12}
\]

Define `SHALLOWCORR106590`:

```text
limsup C_sh(T)/N(T,2T) < 97/1000.
```

Then the fifth-endpoint index and
`R_5/N>997/1000-o(1)` give

\[
\boxed{
\mathrm{ENDLOC}_{106590}
\wedge
\mathrm{SHALLOWCORR}_{106590}
\Longrightarrow
\liminf_{T\to\infty}
 {N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106590.13}

The corresponding threshold for `95%` is `47/1000`.

The shallow term is the literal confluent Cauchy canonical-correlation defect
of the denominator and numerator inner factors. It is the microscopic core of
`RESGRAM106450`, `HBSIG/HBRT106451`, `CANONCORR106530`, and
`ORIENTEDANGLE106540`.

## 5. Binding microscopic firewall

For `c>1`, the functions

\[
F_n(z)=c+\cos(nz)
\]

have a positive even Fourier source, no real zeros, and a completely
real-rooted fifth derivative. Their zeros are

\[
{(2k+1)\pi\over n}
 \pm i{\operatorname{arcosh}c\over n}.
\]

On every fixed real interval, zero count is `Theta(n)` while total vertical
height is `O(1)`. Therefore vanishing height mass, positivity of the Fourier
source, and real-rootedness of the fifth derivative do not control the
microscopic topological units.

A proof of `SHALLOWCORR106590` must use genuinely Xi-specific microscopic
information: endpoint-companion correlation, near-line repulsion, the literal
arithmetic source, or an equivalent phase-angle theorem.

```text
Selberg horizontal first moment O(T)             PROVED UNCONDITIONALLY
finite derivative/companion height majorization  PROVED EXACT
deep model-space charge paid by height            PROVED EXACT
ENDLOC106590 cofinal endpoint localization        OPEN / ANALYTIC
SHALLOWCORR106590 microscopic correlation         OPEN / RECORD-BEARING
ninety percent / density one / RH                 UNPROVED
```