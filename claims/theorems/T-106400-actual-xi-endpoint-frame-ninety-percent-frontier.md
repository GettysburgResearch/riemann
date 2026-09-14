# T-106400 — Actual-Xi endpoint-frame frontier for more than ninety percent

Claim ID: `T-106400`  
Status: **UNCONDITIONAL STRUCTURAL THEOREMS + CONDITIONAL 90.745% CUT; ROBUSTFRAME106400 OPEN**  
Created: 2026-08-24  
Depends on: `L-106400--L-106402`; pinned fixed-order bound `R_2/N>599/625-o(1)`  
RH status: **unproved**

## 1. One endpoint block replaces two separate rungs

For \(F=\Xi\), let

\[
U_T=
\frac{(F-i\lambda_TF')(F''+i\lambda_TF''')}
     {(F+i\lambda_TF')(F''-i\lambda_TF''')}
\]

on a compatible regular window.  The intermediate \(F'\) companion cancels.
If \(E_1,E_2\) are the two wrong-extremum losses, then

\[
\operatorname{wind}U_T=2-2(E_1+E_2).
\]

For any source frame \(\mathcal S_T=D_T\mathcal G_T\) inside the finite initial
space of \(H_{U_T}\), with complement dimension \(c_T\), define

\[
(G_T)_{ij}=\langle D_Tg_i,D_Tg_j\rangle
\]

and

\[
(Q_T)_{ij}=\left\langle
H_{\mathcal T_\Xi}g_i,H_{\mathcal T_\Xi}g_j
\right\rangle,
\qquad
\mathcal T_\Xi=\Xi\Xi'''-\Xi'\Xi''.
\]

Then `L-106400` gives

\[
\boxed{
R_0(T)
\ge
R_2(T)-c_T-4\lambda_T^2\operatorname{tr}(G_T^{-1}Q_T)-o(N(T)).
}
\tag{T-106400.1}

The \(o(N)\) term is only the declared endpoint, multiplicity and cofinal
regularization ledger.

## 2. The actual numerator is already source-positive

`L-106401` proves unconditionally that

\[
\widehat{\Xi'^2-\Xi\Xi''}(\xi)
=\frac12\int(2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du
=\Lambda_\Xi(\xi)\ge0,
\]

and

\[
\widehat{\mathcal T_\Xi}(\xi)=-i\xi\Lambda_\Xi(\xi).
\]

Thus \(Q_T\succeq0\) is the Gram of one explicit actual-Xi Hankel operator with
kernel

\[
(x+s)\Lambda_\Xi(x+s).
\]

No frozen-to-actual numerator transfer remains.  The open analysis concerns
only the endpoint denominator frame and the normalized size of this already
identified positive Gram.

## 3. Robust two-scalar sufficient condition

Let \(G_{0,T}>0\) be a predeclared frozen/source Gram of dimension \(d_T\), and
put

\[
\widetilde G_T
=G_{0,T}^{-1/2}G_TG_{0,T}^{-1/2},
\]

\[
\widetilde Q_T
=4\lambda_T^2G_{0,T}^{-1/2}Q_TG_{0,T}^{-1/2}.
\]

Define `ROBUSTFRAME106400` by the three estimates

\[
\boxed{
d_T\ge\left(\frac{999}{1000}-o(1)\right)N(T),
}
\tag{T-106400.2}

\[
\boxed{
\|\widetilde G_T-I\|_{\mathrm F}^2
\le\left(\frac1{100}+o(1)\right)d_T,
}
\tag{T-106400.3}

\[
\boxed{
\operatorname{tr}\widetilde Q_T
\le\left(\frac1{200}+o(1)\right)d_T.
}
\tag{T-106400.4}

No operator-norm approximation is requested.

By `L-106402`, discard the eigenvalues of \(\widetilde G_T\) below \(1/2\).
Their number is at most \((1/25+o(1))d_T\), while inversion on the retained
frame costs at most two.  The complete normalized defect payment is therefore
at most

\[
\frac{1019}{20000}+o(1)=0.05095+o(1).
\]

Using the pinned unconditional fixed-order input

\[
\frac{R_2(T)}{N(T)}>\frac{599}{625}-o(1),
\]

one obtains

\[
\boxed{
\mathrm{ROBUSTFRAME}_{106400}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
\ge\frac{18149}{20000}
=0.90745.
}
\tag{T-106400.5}

In particular, `ROBUSTFRAME106400` proves more than ninety percent.

## 4. Exact remaining work

The new interface has only two analytic rows beyond frame dimension:

```text
endpoint-denominator frame:
  one-percent Frobenius-square comparison with the frozen positive frame;

actual Xi exterior-square leakage:
  one-half-percent normalized trace bound for the explicit theta-Hankel Gram.
```

The following are no longer open interfaces:

```text
two independent derivative-rung estimates;
intermediate Xi-prime companion transport;
identity-carrier bookkeeping;
quadratic companion term;
frozen-to-actual numerator identification;
ordinary-L2 replacement of winding;
operator-norm closeness of the denominator frame.
```

The frozen Wick and owner-conductor calculations elsewhere on the branch show
that the model lies well inside the numerical targets, but they do not prove
(T-106400.3)--(T-106400.4) for the actual Xi frame.

## 5. Boundary

```text
endpoint all-pass telescope                      PROVED EXACT
intermediate companion cancellation              PROVED EXACT
denominator-cancelled linear Turan packet         PROVED EXACT
actual Xi exterior-square Fourier density         PROVED UNCONDITIONALLY
actual Turan packet = explicit Hankel source       PROVED EXACT
Frobenius quantile absorption                     PROVED EXACT
ROBUSTFRAME106400                                 OPEN / RECORD-BEARING
more than ninety percent                          UNPROVED
almost all / density one                          UNPROVED
Riemann Hypothesis                                UNPROVED
```
