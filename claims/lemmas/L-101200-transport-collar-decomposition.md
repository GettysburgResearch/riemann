# L-101200 — Exact transport–collar decomposition of a signed physical observation

Claim ID: `L-101200`  
Status: **PROVED EXACT MEASURE IDENTITY**  
Created: 2026-08-21  
RH status: **not assumed**

Let \(\mu^-\) and \(\mu^+\) be finite positive measures, let \(K\ge0\) be a measurable observable, and let \(\pi\) be a positive subcoupling whose first and second marginals are dominated by \(\mu^-\) and \(\mu^+\). Put

\[
\rho^- = \mu^--(\operatorname{pr}_1)_*\pi,
\qquad
\rho^+ = \mu^+-(\operatorname{pr}_2)_*\pi.
\]

For

\[
S_K=\int K\,d\mu^+-\int K\,d\mu^-
\]

one has exactly

\[
\boxed{
S_K=\int[K(y)-K(x)]\,d\pi(x,y)
 +\int K\,d\rho^+-\int K\,d\rho^- .
}
\tag{L-101200.1}
\]

Consequently

\[
\boxed{
(S_K)_-
\le
\int[K(x)-K(y)]_+\,d\pi(x,y)
+\int K\,d\rho^- .
}
\tag{L-101200.2}
\]

The proof is substitution of the two marginal decompositions. If \(K=\int\mathbf 1_{A_t}\,d\nu(t)\), \(d\nu\ge0\), then Tonelli also gives

\[
\int[K(x)-K(y)]_+\,d\pi
\le \int \pi(A_t\times A_t^c)\,d\nu(t).
\tag{L-101200.3}
\]

Thus a capacity estimate and a collar-crossing estimate close only when they refer to the **same coupling, normalization, and physical observable**.
