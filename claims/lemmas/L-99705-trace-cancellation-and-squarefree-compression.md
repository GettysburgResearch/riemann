# L-99705 — The box-flow problem compresses exactly to the decorated squarefree signed source

Claim ID: `L-99705`  
Status: **PROVED EXACT SOURCE-COMPRESSION THEOREM**  
Created: 2026-08-20  
Depends on: `L-99703`, `L-99704`  
RH status: **not assumed**

At a vertex `n`, the two box-source masses are

\[
m_X^\pm(n)=\pi(n)\Phi_X^{\Box}(n)\frac{1\pm f(n)}2.
\]

The common amount

\[
\min(m_X^+(n),m_X^-(n))
=\pi(n)\Phi_X^{\Box}(n)\frac{1-|f(n)|}{2}
\]

may be matched at the same vertex. This is an identity flow: it changes no source label, endpoint, row, or capacity coordinate.

After this cancellation, the residual mass at `n` is

\[
\boxed{
\pi(n)\Phi_X^{\Box}(n)|f(n)|
=\frac{|\beta(n)|}{n}\Phi_X^{\Box}(n),
}
\tag{L-99705.1}
\]

and its channel sign is `sgn beta(n)`. Hence all vertices with `beta(n)=0` disappear from the orientation problem.

The support is explicit. Write `n=67^e m` with `67` not dividing `m`. Then `beta(n)` is nonzero exactly when `m` is squarefree and `e in {0,1,2}`, and

\[
\boxed{
\beta(m)=\mu(m),
\qquad
\beta(67m)=-2\mu(m),
\qquad
\beta(67^2m)=\mu(m).
}
\tag{L-99705.2}
\]

Thus the live cross-source problem is not hidden in the large positive trace `g`. It is the finite three-fibre decoration of the ordinary squarefree parity source, with exact normalized masses

\[
\frac{\Phi_X^{\Box}(m)}m,
\qquad
\frac{2\Phi_X^{\Box}(67m)}{67m},
\qquad
\frac{\Phi_X^{\Box}(67^2m)}{67^2m}.
\tag{L-99705.3}
\]

Because `Phi_X^Box` is decreasing as a function of the source integer, adjoining a prime power `q` obeys the exact capacity comparison

\[
\boxed{
\frac{\Phi_X^{\Box}(nq)}{nq}
\le\frac1q\frac{\Phi_X^{\Box}(n)}n.
}
\tag{L-99705.4}
\]

Equation (L-99705.4) is the scalar same-index child nonexpansivity in its sharpest box form. It is valid for every physical source integer and every prime power, with no continuum approximation.

The theorem separates two issues cleanly:

```text
positive completion trace and repeated-prime uncertainty  cancelled exactly;
decorated squarefree parity transport                     conclusion-producing.
```

Any proposed proof may therefore work directly on the three decorated squarefree fibres. Conversely, a proof which spends the neutral trace as if it supplied oriented capacity is invalid.