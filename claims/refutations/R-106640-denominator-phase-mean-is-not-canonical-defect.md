# R-106640 — The denominator phase mean is not the canonical-correlation defect

Claim ID: `R-106640`  
Status: **PROVED EXACT ONE-POLE FIREWALL**  
Created: 2026-08-26  
Depends on: corrected `L-106514`  
RH status: **not assumed**

The equality asserted by the former versions of `L-106514`, `T-106540`, and
`L-106601` fails for the smallest nontrivial finite-inner example.

Let

\[
B_-(z)=\frac{z-i}{z+i},
\qquad
B_+(z)=\frac{z-1-i}{z-1+i},
\qquad
U=\frac{B_+}{B_-}.
\]

Both inner functions are canonically normalized at infinity.

## 1. Exact canonical charge

The normalized upper-half-plane kernel overlap at \(b=i\) and \(c=1+i\) is

\[
\left|\langle e_b,e_c\rangle\right|^2
=
\frac{4\operatorname{Im}b\,\operatorname{Im}c}
{(\operatorname{Im}b+\operatorname{Im}c)^2
 +(\operatorname{Re}b-\operatorname{Re}c)^2}
=
\frac45.
\]

Therefore

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=
1-\frac45
=
\frac15.
}
\tag{R-106640.1}
\]

Equivalently,

\[
|B_+(i)|^2=\frac15.
\]

## 2. Exact denominator phase statistic

The complex cross-Dirichlet residue is

\[
\Delta
=
\frac{B_+'(i)}{B_-'(i)}
=
\frac{12}{25}-\frac{16}{25}i.
\tag{R-106640.2}
\]

Since the denominator degree is one,

\[
\frac1{2\pi}\int_{\mathbb R}
\beta_-'(t)\operatorname{Re}U(t)\,dt
=
\operatorname{Re}\Delta
=
\frac{12}{25}.
\]

Hence

\[
\boxed{
\frac1{2\pi}\int_{\mathbb R}
\beta_-'(t)\bigl(1-\operatorname{Re}U(t)\bigr)\,dt
=
\frac{13}{25}.
}
\tag{R-106640.3}
\]

Thus

\[
\boxed{
\frac15\ne\frac{13}{25}.
}
\tag{R-106640.4}
\]

The phase mean overpays the canonical charge by

\[
\frac{13}{25}-\frac15=\frac8{25}.
\]

## 3. General one-pole formula

For

\[
b=a+iy,\qquad c=d+iv,\qquad y,v>0,
\]

put

\[
D=(a-d)^2+(y+v)^2.
\]

The canonical overlap and the real cross-Dirichlet scalar are

\[
\mathcal O=\frac{4yv}{D},
\]

\[
\operatorname{Re}\Delta
=
\frac{4yv\bigl((y+v)^2-(a-d)^2\bigr)}{D^2}.
\]

Their difference is

\[
\boxed{
\mathcal O-\operatorname{Re}\Delta
=
\frac{8yv(a-d)^2}{D^2}
\ge0.
}
\tag{R-106640.5}
\]

Equality holds only for vertical alignment \(a=d\).  Therefore canonical
normalization at infinity does not repair the old identity.

## 4. Consequence

```text
phase statistic = exact all-pass charge            FALSE
phase statistic >= exact all-pass charge            TRUE by L-106514
small phase statistic -> small canonical charge     VALID SUFFICIENT ROUTE
small canonical charge -> equally small phase mean  NOT VALID
```

The current `MESOTRANS106630` gate is formulated directly in the exact
canonical charge and is not refuted by this example.
