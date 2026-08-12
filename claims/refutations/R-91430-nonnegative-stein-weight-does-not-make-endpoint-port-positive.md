# R-91430 — A nonnegative Stein weight does not make the Brownian endpoint port positive

Claim ID: `R-91430`  
Status: **EXACT SIGNATURE FIREWALL / CORRECTED BROWNIAN CLOSING TARGET**  
Created: 2026-08-12  
Depends on: `L-91422`  
Corrects: any reading of `L-91422.9--11` in which the weighted endpoint term is itself positive  
RH status: **unproved**

## 1. The endpoint term isolated in `L-91422`

For independent completed Brownian coordinates `Z_1,Z_2`, put

\[
 c_{\tau,u}
 =(1+\tanh\Delta)\tau_u(Z_1)
 +(1-\tanh\Delta)\tau_u(Z_2)\ge0,
 \qquad \Delta=Z_1-Z_2.
\]

The endpoint derivative in `L-91422.6` is

\[
 D_+\mathcal A_F
 =\overline{F(Z_1)}F(Z_2)
  +\overline{F(-Z_2)}F(-Z_1).
\tag{R-91430.1}
\]

The coefficient is nonnegative. The form (R-91430.1) is not.

## 2. Exchange symmetrization

The joint law of `(Z_1,Z_2)` is invariant under exchange. The coefficient
`c_(tau,u)` is also invariant under exchange, while

\[
 D_+\mathcal A_F(Z_2,Z_1)
 =\overline{D_+\mathcal A_F(Z_1,Z_2)}.
\]

Consequently

\[
 \mathbb E[c_{\tau,u}D_+\mathcal A_F]
 =\mathbb E[c_{\tau,u}\mathcal H_F],
\tag{R-91430.2}
\]

where the real endpoint form is

\[
 \boxed{
 \mathcal H_F(z_1,z_2)
 =\Re\!\left(\overline{F(z_1)}F(z_2)\right)
  +\Re\!\left(\overline{F(-z_2)}F(-z_1)\right).
 }
\tag{R-91430.3}
\]

## 3. Exact signature

Treat the four evaluations

\[
 a=F(z_1),\quad b=F(z_2),\quad
 c=F(-z_2),\quad d=F(-z_1)
\]

as independent complex coordinates. Then

\[
 \mathcal H_F=\Re(\bar a b)+\Re(\bar c d).
\]

Each two-coordinate block has Hermitian matrix

\[
 \begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}
\]

and eigenvalues `+1/2,-1/2`. Hence the full generic endpoint form has

\[
 \boxed{\operatorname{sig}(\mathcal H_F)=(2,2).}
\tag{R-91430.4}
\]

A nonnegative scalar multiplier cannot change this signature.

## 4. Explicit exponential witness

Let `z_1\ne z_2` be real and choose the one-frequency exponential polynomial

\[
 F(x)=e^{i\xi x},
 \qquad
 \xi=\frac{\pi}{z_2-z_1}.
\]

Then

\[
 \mathcal H_F(z_1,z_2)
 =2\cos(\xi(z_2-z_1))=-2.
\tag{R-91430.5}
\]

Thus the endpoint contribution in `L-91422.9` may be strictly negative even
where `c_(tau,u)>0`.

## 5. Consequence

The phrase

```text
nonnegative-weight boundary port
```

is correct only as a statement about its scalar coefficient. It must not be
promoted to

```text
positive boundary form.
```

The Brownian route therefore requires an explicit diagonal/theta reserve for
the two negative endpoint squares. `L-91431` gives the sharp completion and
turns this firewall into a quantified closing target.

```text
Stein coefficient c_tau                         NONNEGATIVE EXACT
endpoint Hermitian form                         SIGNATURE (2,2)
nonnegative coefficient -> positive endpoint    FALSE
single-exponential negative witness              EXACT
sharp diagonal completion                       L-91431
Brownian reflection positivity                  OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```
