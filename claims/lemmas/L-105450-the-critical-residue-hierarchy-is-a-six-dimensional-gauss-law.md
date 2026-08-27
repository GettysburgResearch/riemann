# L-105450 — The critical-residue hierarchy is a six-dimensional Gauss law

Claim ID: `L-105450`  
Status: **PROVED EXACT DISTRIBUTIONAL REFORMULATION ON THE SIMPLE STRATUM**  
Created: 2026-08-24  
Depends on: `L-105328`, `L-105446`, `T-105330`  
RH status: **not assumed**

## 1. Lifted differential potential

Let `F` be real entire of definite parity and put

\[
m={F\over F'}.
\]

On the base-zero upper half-plane define

\[
\mathcal C(a,h)
={1\over2}\left[h\Re m'(a+ih)-\Im m(a+ih)\right]
\]

and

\[
\mathcal W(a,h)={\mathcal C(a,h)\over h^3}.
\]

For `y in R^5`, set

\[
\widetilde{\mathcal W}(a,y)
=\mathcal W(a,|y|).
\]

By `L-105446`, this is harmonic away from the lifted critical-pole set.

## 2. One real critical residue is one Newton charge

At a simple real noncommon critical point `c`,

\[
m(z)={\rho_c\over z-c}+O(1),
\qquad
\rho_c={F(c)\over F''(c)}.
\]

Its lifted contribution is

\[
\widetilde{\mathcal W}_c(a,y)
={\rho_c\over[(a-c)^2+|y|^2]^2}.
\tag{L-105450.1}

The area of the unit five-sphere is

\[
|S^5|=\pi^3.
\]

Since, distributionally in `R^6`,

\[
\Delta |X|^{-4}=-4\pi^3\delta_0,
\]

one has

\[
\boxed{
\Delta_{\mathbb R^6}
\widetilde{\mathcal W}_c
=-4\pi^3\rho_c\,\delta_{(c,0)}.
}
\tag{L-105450.2}

Equivalently, for every sufficiently small sphere around the lifted critical
point,

\[
\boxed{
\rho_c
=-{1\over4\pi^3}
\int_{\partial B_\varepsilon(c,0)}
\partial_n\widetilde{\mathcal W}\,dS.
}
\tag{L-105450.3}

Thus the derivative-ratio residue is a literal Gauss flux.

## 3. Finite-window charge ledger

Let `I` be a compact real interval containing only simple noncommon critical
points and choose a six-dimensional domain `D` whose axis intersection is
`I`, with boundary avoiding every lifted pole. Summing (L-105450.2) and using
the divergence theorem gives

\[
\boxed{
\sum_{c\in I}\rho_c
=-{1\over4\pi^3}
\int_{\partial D}
\partial_n\widetilde{\mathcal W}\,dS.
}
\tag{L-105450.4}

Weighted and multipole versions follow by testing the distributional equation
against harmonic polynomials. The familiar first-residue and moment ledgers
are therefore ordinary multipole moments of one Newton source.

## 4. Exact sign interpretation

Equation (L-105450.2) gives

\[
\boxed{
\rho_c\le0
\quad\Longleftrightarrow\quad
\Delta\widetilde{\mathcal W}_c
\text{ is a nonnegative point measure}.
}
\tag{L-105450.5}

Hence, on the complete simple real-critical stratum,

\[
\boxed{
\text{all critical residues are nonpositive}
\quad\Longleftrightarrow\quad
\Delta\widetilde{\mathcal W}
\text{ is a nonnegative measure supported on the axis}.
}
\tag{L-105450.6}

Through `L-105328` and `T-105330`, this is exactly the critical
Vandermonde/Hankel hierarchy `CRVH105330`.

The determinant hierarchy, pointwise residue orientation and distributional
subharmonicity of the six-dimensional microscope are three coordinates of one
sharp defect.

## 5. Nonreal critical points become shell singularities

Let

\[
c=\alpha+i\eta,
\qquad \eta>0,
\]

be a nonreal critical pole of `m`. The axisymmetric lift samples
`m(a+i|y|)`. Therefore the singular locus is

\[
\boxed{
\{(a,y)\in\mathbb R\times\mathbb R^5:
 a=\alpha,\ |y|=\eta\}.
}
\tag{L-105450.7}

It is an off-axis four-sphere rather than an axis point.

Its real lifted distribution is not a nonnegative point measure on the axis;
it is precisely the geometric form of the nonreal conjugate correction in the
Bezoutian and moment ledgers. Thus

```text
real critical point      -> axial Newton point source;
nonreal critical point   -> off-axis spherical shell singularity;
positive real residue    -> negative distributional source;
nonpositive real residue -> nonnegative distributional source.
```

## 6. Sharp critical gate in local PDE form

On the simple noncommon stratum,

\[
\boxed{
\mathrm{CRVH105330}
\Longleftrightarrow
\begin{cases}
\text{the lifted singular support is contained in the axis},\\
\Delta\widetilde{\mathcal W}\ge0
\text{ as a Radon measure}.
\end{cases}
}
\tag{L-105450.8}

This is local: every wrong residue or nonreal critical point is detected in an
arbitrarily small six-dimensional neighbourhood of its lifted source. No
large packet determinant is required once the potential is available.

## 7. Scope

Multiple critical points produce confluent higher-order source distributions
and remain in the existing multiplicity ledger. The Gauss-law reformulation
does not prove that the source is positive or axis-supported for Xi. It gives a
local PDE target exactly equivalent to the sharp critical hierarchy.