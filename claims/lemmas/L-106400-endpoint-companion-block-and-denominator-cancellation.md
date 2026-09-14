# L-106400 — Endpoint-companion block and exact denominator cancellation

Claim ID: `L-106400`  
Status: **PROVED EXACT AT FINITE REGULAR RATIONAL-ALL-PASS SCOPE**  
Created: 2026-08-24  
Depends on: `L-105280`, `L-105290`  
RH status: **not assumed**

Let \(p\in\mathbb R[x]\) be regular: the real zeros of \(p,p',p'',p'''\)
that occur below are simple and no denominator event lies on the real axis.
Fix \(\lambda>0\) and put

\[
E_{0,\pm}=p\pm i\lambda p',\qquad
E_{2,\pm}=p''\pm i\lambda p'''.
\]

Define the endpoint all-pass quotient

\[
\boxed{
U(x)=\frac{E_{0,-}(x)E_{2,+}(x)}
           {E_{0,+}(x)E_{2,-}(x)}.
}
\tag{L-106400.1}
\]

For real \(x\), the numerator is the conjugate of the denominator, so
\(|U(x)|=1\).

## 1. The intermediate companion cancels

Let \(R_j\) be the number of real zeros of \(p^{(j)}\), and let \(E_1,E_2\)
be the two wrong-extremum counts in the descents

\[
p''\longrightarrow p'\longrightarrow p.
\]

The exact Rolle identities are

\[
R_0-R_1=1-2E_1,\qquad R_1-R_2=1-2E_2.
\]

By `L-105280`, the winding of the endpoint companion ratio is therefore

\[
\boxed{
\operatorname{wind}U=R_0-R_2=2-2(E_1+E_2).
}
\tag{L-106400.2}
\]

No \(p'\)-companion remains in (L-106400.1).  The complete two-rung loss is
one scalar all-pass index.

By the negative-half Fourier/Hankel inequality of `L-105290`,

\[
-\operatorname{wind}U\le \|H_U\|_{\mathcal S_2}^2.
\]

Combining this with (L-106400.2) gives the exact block descent estimate

\[
\boxed{
R_0\ge R_2-\|H_U\|_{\mathcal S_2}^2.
}
\tag{L-106400.3}
\]

The two deterministic Rolle units cancel automatically; no auxiliary
all-pass carrier is required.

## 2. Exact cancellation of the denominator

Write

\[
N=E_{0,-}E_{2,+},\qquad D=E_{0,+}E_{2,-},\qquad U=N/D.
\]

Direct multiplication gives

\[
\boxed{
N-D=2i\lambda\bigl(pp'''-p'p''\bigr).
}
\tag{L-106400.4}
\]

Both potentially dangerous terms cancel:

```text
identity/degree-zero term:   p p'';
quadratic companion term:    lambda^2 p' p'''.
```

Let \(\mathcal I_U=(\ker H_U)^\perp\), the finite-dimensional initial space of
the rational Hankel operator.  Let \(\mathcal G=\operatorname{span}\{g_1,\ldots,g_d\}\)
be a finite analytic source space such that

\[
\mathcal S=D\mathcal G\subseteq\mathcal I_U,
\]

and let

\[
c=\dim\mathcal I_U-\dim\mathcal S.
\]

Define the two Gram matrices

\[
G_{ij}=\langle Dg_i,Dg_j\rangle_{H^2},
\]

\[
Q_{ij}=\left\langle
 P_-\bigl((pp'''-p'p'')g_i\bigr),
 P_-\bigl((pp'''-p'p'')g_j\bigr)
\right\rangle.
\]

Assume \(G\) is positive definite.  Since \(Dg\) is analytic,

\[
H_U(Dg)=P_-(Ng)=P_-((N-D)g)
       =2i\lambda P_-((pp'''-p'p'')g).
\]

Hence the restricted Hilbert--Schmidt norm is exactly

\[
\boxed{
\|H_UP_{\mathcal S}\|_{\mathcal S_2}^2
=4\lambda^2\operatorname{tr}(G^{-1}Q).
}
\tag{L-106400.5}
\]

Because \(|U|=1\), one has \(H_U^*H_U\le I\).  The complement of
\(\mathcal S\) inside \(\mathcal I_U\) therefore costs at most its dimension:

\[
\|H_U\|_{\mathcal S_2}^2
\le c+4\lambda^2\operatorname{tr}(G^{-1}Q).
\]

Substitution in (L-106400.3) yields

\[
\boxed{
R_0\ge R_2-c-4\lambda^2\operatorname{tr}(G^{-1}Q).
}
\tag{L-106400.6}
\]

This is basis independent.  It is the exact finite-dimensional interface
between the topological reverse--Rolle loss and one endpoint Turán packet.

## 3. Entire-window scope

For a real entire function, apply the theorem to a canonical-product
truncation on one regular window and retain the endpoint, multiplicity and
confluent charges explicitly.  The algebra (L-106400.1)--(L-106400.6) is
unchanged.  Passage to Xi requires a cofinal source frame and quantitative
control of \(c\), \(G\), and \(Q\); no such estimate is asserted here.
