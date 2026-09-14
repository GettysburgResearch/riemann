# L-106451 — The fifth-derivative endpoint has a strict four-channel source contraction

Claim ID: `L-106451`  
Status: **PROVED EXACT FOR THE TRUNCATED POSITIVE/NEGATIVE XI FOURIER SOURCE**  
Created: 2026-08-25  
Depends on: `L-105260`, `L-106413`, `L-106450`  
RH status: **not assumed**

Let `Phi(u)>=0` be the positive even Xi Fourier density and truncate it to
`|u|<=L`.  Fix `lambda>0` and put

\[
c=\lambda L<1.
\]

Use the endpoint companions at derivative orders zero and five.  The harmless
constant phase `i^5` is absorbed into the fifth-derivative channel coordinate.
The positive/negative-frequency expansion has two same-sign Hankel channels
and two reflected Toeplitz channels, exactly as in `L-106413`.

## 1. Same-sign channel

For `u,v in [0,L]`, define the symmetrized positive denominator density

\[
\boxed{
\begin{aligned}
a_5(u,v)={1\over2}\big[&
 (1-\lambda u)(1+\lambda v)v^5\\
&+(1-\lambda v)(1+\lambda u)u^5
\big].
\end{aligned}
}
\tag{L-106451.1}

The absolute denominator-cancelled endpoint density is

\[
\boxed{
r_5(u,v)
 =\lambda |u-v|\,|u^5-v^5|.
}
\tag{L-106451.2}

Since every coefficient product in (L-106451.1) is at least `1-c`,

\[
a_5(u,v)\ge{1-c\over2}(u^5+v^5).
\tag{L-106451.3}

Moreover

\[
|u-v|\le L,
\qquad
|u^5-v^5|\le u^5+v^5,
\]

and therefore

\[
\boxed{
0\le r_5(u,v)
 \le {2c\over1-c}\,a_5(u,v).
}
\tag{L-106451.4

After integration on each sum-frequency fibre, the same inequality holds for
the corresponding positive Fourier densities.  Consequently the same-sign
Hankel energy obeys

\[
\boxed{
\mathcal E_{\rm same}
 \le\left({2c\over1-c}\right)^2
 \mathcal E_{\rm den,same}.
}
\tag{L-106451.5

## 2. Reflected channel

For one reflected orientation the positive denominator density is bounded
below by

\[
{(1-c)^2\over2}(u^5+v^5),
\]

whereas the absolute endpoint density is bounded above by

\[
2\lambda(u+v)(u^5+v^5)
 \le4c(u^5+v^5).
\]

Thus the reflected Toeplitz channel obeys

\[
\boxed{
\mathcal E_{\rm refl}
 \le\left({4c\over(1-c)^2}\right)^2
 \mathcal E_{\rm den,refl}.
}
\tag{L-106451.6

The estimate is orientation-by-orientation; no cancellation between the two
reflected channels is used.

## 3. Explicit four-channel constant

Choose

\[
\boxed{c={1\over200}.}
\]

Then one same-sign orientation costs

\[
\left({2c\over1-c}\right)^2
 =\left({2\over199}\right)^2
 ={4\over39601},
\]

and one reflected orientation costs

\[
\left({4c\over(1-c)^2}\right)^2
 =\left({800\over39601}\right)^2
 ={640000\over1568239201}.
\]

Paying all four channels gives

\[
\boxed{
\begin{aligned}
\mathfrak r_5
&\le2{4\over39601}
 +2{640000\over1568239201}\\
&={1596808\over1568239201}
 <{1\over980}.
\end{aligned}
}
\tag{L-106451.7

The strict final comparison follows from

\[
1596808\cdot980=1564871840<1568239201.
\]

## 4. Meaning and boundary

The all-pass index is independent of the positive shift `lambda`; choosing
`lambda L=1/200` reduces the source energy without changing the endpoint
zero-count index.

This theorem proves the finite four-channel ratio relative to its positive
endpoint denominator bank.  It does not prove the cofinal bank trace equals
the complete Xi zero-count scale, nor control the signed complement after the
bank is embedded in the full companion model space.  Those terms remain
explicit in `T-106450`.