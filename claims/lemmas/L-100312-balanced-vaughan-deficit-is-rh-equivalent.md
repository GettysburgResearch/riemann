# L-100312 — The balanced Vaughan deficit is an exact RH-equivalent terminal gate

Claim ID: `L-100312`  
Status: **PROVED CONDITIONAL CONCLUSION + CONVERSE**  
Created: 2026-08-20  
Depends on: `L-100310`, `L-100311`; PRs #653, #674, #675  
RH status: **not assumed**

Set \(U_X=\lfloor X^{1/3}\rfloor\) and define

\[
\boxed{
\mathrm{BVD}_{100310}:\qquad
\int_2^Y(\mathcal B_{U_X}(X))_-\frac{dX}{X}=Y^{o(1)}.
}
\tag{L-100312.1}
\]

By `L-100311`,

\[
\mathcal W_1=\mathcal T_{U_X}+\mathcal B_{U_X},
\]

and \(\int_2^\infty|\mathcal T_{U_X}(X)|\,dX/X<\infty\). Hence
`BVD100310` gives subpower negative mass for the zero-safe scalar
\(\mathcal W_1\). The Mellin--Landau consumer therefore yields

\[
\boxed{\mathrm{BVD}_{100310}\Longrightarrow RH.}
\tag{L-100312.2}
\]

Conversely, RH gives the Littlewood bound for \(\mu\), and ordinary partial
summation against the compact piecewise-smooth kernel gives

\[
\mathcal W_1(X)=O_\varepsilon(X^\varepsilon).
\]

Together with (L-100311.6),

\[
\mathcal B_{U_X}(X)=O_\varepsilon(X^\varepsilon).
\]

Therefore

\[
\boxed{RH\Longrightarrow\mathrm{BVD}_{100310}.}
\tag{L-100312.3}
\]

So the balanced trilinear estimate is RH-equivalent. The reduction is still
substantive: it proves unconditionally that no linear, diagonal, carrier,
normalization, or Type-I term remains. Any successful proof must now exploit
the signs inside one explicit compact trilinear form.
