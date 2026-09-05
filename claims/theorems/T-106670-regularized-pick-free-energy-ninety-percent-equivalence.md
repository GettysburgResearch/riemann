# T-106670 — The mesoscopic 90% frontier is one regularized source-Pick determinant

Claim ID: `T-106670`  
Status: **UNCONDITIONAL EXACT EQUIVALENCE + ONE XI DETERMINANT ESTIMATE OPEN**  
Created: 2026-08-26  
Depends on: `T-106500`, `T-106590`, `T-106620`, `T-106630`, `T-106650`, current `T-106660`, `L-106670--L-106673`, `R-106670`; pinned `R_5/N>997/1000-o(1)` input  
RH status: **unproved**

Retain the regular mesoscopic windows and reduced inner factors of
`T-106620`.  Write

\[
\mathcal C_{\rm full}(T)
=\sum_j\operatorname{tr}_{K_{B_{-,j}}}
\left(I-P_{K_{B_{+,j}}}\right)
\tag{T-106670.1}
\]

for the exact full adverse endpoint charge.  The trace means the compression
to the displayed denominator model space.

## 1. Cutoff family and one global scalar partition function

For `0<eta<infinity`, factor the denominator by pole height and put

\[
M_{j,\eta}=K_{B_{-,j}^{\le\eta}},
\qquad
\mathcal C_{\le\eta}(T)
=\sum_j\operatorname{tr}_{M_{j,\eta}}
\left(I-P_{K_{B_{+,j}}}\right).
\tag{T-106670.2}
\]

At `eta=infinity`, interpret these as the full denominator factor and the full
charge.  Let `G_(j,eta)` be the corresponding denominator kernel Gram and let

\[
V_{j,\eta}=\operatorname{diag}
\bigl(B_{+,j}(b_{j,1}),\ldots,B_{+,j}(b_{j,m_{j,\eta}})\bigr)
\]

in the simple-zero case, with the confluent multiplication jet otherwise.
Choose any deterministic regularization

\[
0<\tau_T<1,
\qquad
\tau_T\longrightarrow0,
\]

for example `tau_T=1/log T`, and define

\[
\boxed{
\mathscr Z_{T,\eta}
=
\prod_j
{\det\!\left(
G_{j,\eta}-\tau_TV_{j,\eta}^*G_{j,\eta}V_{j,\eta}
\right)
\over\det G_{j,\eta}},
}
\tag{T-106670.3}
\]

\[
\boxed{
\mathscr F_{T,\eta}
=-{1\over\tau_T}\log\mathscr Z_{T,\eta}.
}
\tag{T-106670.4}
\]

Every factor lies in `(0,1]`.  By `L-106671`, its node values are the actual
outer-normalized fifth-endpoint source samples

\[
\boxed{
B_{+,j}(b)
=
{2i\lambda_j(hDH_5-(Dh)H_5)(b)\over O_j(b)}.
}
\tag{T-106670.5}
\]

Thus the determinant contains no free transport matrix, inverse Gram, frame
constant, numerator-zero bank, or separately estimated nonnormality term.

## 2. Asymptotically exact equivalence at every cutoff

Applying `L-106670` window by window gives

\[
\boxed{
\mathcal C_{\le\eta}(T)
\le
\mathscr F_{T,\eta}
\le
c(\tau_T)\mathcal C_{\le\eta}(T),
\qquad
c(\tau_T)={-\log(1-\tau_T)\over\tau_T}=1+o(1).
}
\tag{T-106670.6}
\]

Let `E_reg(T)>=0` be the common-zero, confluent, boundary, partition, and
cofinal-exhaustion ledger retained by `T-106620/T-106630`.  For every fixed
cutoff and every strict constant threshold, replacing the exact cutoff charge
by `F_(T,eta)` is therefore an equivalence.

For the full factor, define `MESOFREE106670` by

\[
\boxed{
\limsup_{T\to\infty}
{\mathscr F_{T,\infty}+E_{\rm reg}(T)\over N(T,2T)}
<{97\over1000}.
}
\tag{T-106670.7}
\]

By (T-106670.6), this is equivalent to the exact full endpoint-charge gate of
`T-106500`.

## 3. Height-paid cutoff gates

Let

\[
\mathfrak H_-(T)
=\sum_j\sum_{B_{-,j}(x+iy)=0}y.
\]

`T-106590/T-106620` prove

\[
\mathfrak H_-(T)
\le\left({3\over4000}+o(1)\right)N(T,2T),
\tag{T-106670.8}
\]

and the exact model-space split gives

\[
\mathcal C_{\rm full}(T)
\le
\mathcal C_{\le\eta}(T)+{\mathfrak H_-(T)\over\eta}.
\tag{T-106670.9}
\]

Consequently the source-Pick condition

\[
\boxed{
\limsup_{T\to\infty}
{\mathscr F_{T,\eta}+E_{\rm reg}(T)\over N(T,2T)}
<
{97\over1000}-{3\over4000\eta}
}
\tag{T-106670.10}
\]

implies more than 90% for every fixed `eta>3/388`.  Important exact
specializations are

\[
\begin{array}{c|c}
\eta & \text{cutoff free-energy allowance}\\ \hline
1/100 & 11/500,\\
1/10  & 179/2000,\\
1     & 77/800,\\
\infty& 97/1000.
\end{array}
\tag{T-106670.11}
\]

Thus `11/500` is not intrinsic.  It is the conservative price of paying every
pole above height `0.01` by the first moment.  The full determinant has the
entire `97/1000` allowance.

## 4. Ninety-percent implication and determinant lower bounds

The pinned fifth-derivative theorem gives

\[
{R_5(T,2T)\over N(T,2T)}>{997\over1000}-o(1).
\]

Combining it with either (T-106670.7) or (T-106670.10) yields

\[
\boxed{
\mathrm{MESOFREE}_{106670}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106670.12}
\]

Equivalently, the full gate is the scalar lower bound

\[
\boxed{
\log\mathscr Z_{T,\infty}
\ge
-\tau_T\left[
\left({97\over1000}-\epsilon\right)N(T,2T)
-E_{\rm reg}(T)
\right]
}
\tag{T-106670.13}
\]

for some fixed `epsilon>0` eventually on the predeclared cofinal regular
sequence.  At a finite cutoff, replace `97/1000` by
`97/1000-3/(4000 eta)`.

By `L-106672`, the same target is a sum of bounded conditional costs

\[
\sum_{j,k}-{1\over\tau_T}\log q_{j,k}(\tau_T)+E_{\rm reg}(T),
\tag{T-106670.14}
\]

where every pivot lies in `[1-tau_T,1]` and is computed from the literal source
values in (T-106670.5).

## 5. Exact remaining target

`R-106670` shows that height and signed-index marginals cannot establish the
partition-function lower bound.  The required new input is Xi-specific control
of the degree-zero outer-normalized endpoint phase, now represented by one
positive source-Pick determinant rather than an unspecified matrix transport.

```text
T-106660 phase/resolvent checkpoint               VERIFIED REMOTE
regularized free-energy sandwich                   PROVED EXACT
source-evaluation Pick determinant                 PROVED EXACT
conditional-pivot/global-product factorization     PROVED EXACT
full 97/1000 and cutoff-family equivalences         PROVED EXACT
Xi determinant lower bound                         OPEN / 90%-BEARING
more than 90%                                      UNPROVED
density one / RH                                   UNPROVEN
```
