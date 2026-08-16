# L-91880 — The actual arithmetic coupling has an explicit native source and two disjoint physical sectors

Claim ID: `L-91880`  
Status: **PROPOSED COMPLETE LIVE SOURCE-MARGINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Frozen predecessor: PR #509 at `e01daee9cdfea35d2a7d2591f1df6c8080084119`  
Review inputs: PRs #501, #503, #504, #508  
RH status: **unproved**

## 1. Native input datum

Let

\[
c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j)
\]

be the exact native Möbius row. Its ordinary, detail and literal-score
observations are

\[
C_{c_X}=w_X,
\qquad
\Xi_{c_X}=\Omega_X,
\qquad
\mathcal H(c_X)=J_\Lambda(X).
\tag{L-91880.1}
\]

No positivity of `c_X` is assumed.

For integer `X`, put

\[
K=\lfloor X/67\rfloor+1,
\qquad W=10000,
\qquad
\mathcal I_X=\{K+2,\ldots,X-W-3\}.
\]

The exact native source is split into two disjoint sectors.

### Bulk Volterra sector

For a tagged complete cell `(n,u)`, with `n in I_X`, `0<=u<1`, put

\[
s=n+u,
\qquad x=X/s,
\]

and for every squarefree `k<=x` define

\[
\ell_x(k)=k^{-1/2}(2\sqrt{x/k}-1)>0.
\]

The paired bulk occurrence measures are

\[
\boxed{
 d\Sigma_{X,B}^{\pm}(n,u,k)
 =\frac2s\mathbf1_{\mu(k)=\pm1}\ell_x(k)\,du.
}
\tag{L-91880.2}
\]

Every bulk colour multiplies the same nonnegative infinitesimal row `p_s`.
The exact Volterra order swap gives the retained native continuum observation.
Because `x<67`, every active `k` has all prime factors at most `61`; there is no
rough owner in this sector.

### Anchored finite sector

Let `A_X` be the literal finite native source on the complement of the complete
Volterra cells. Apply the exact paired `P_61` stopping-line identity before
signed observation. A source path has the label

\[
\omega=(n,h,i,d,\varepsilon,c),
\tag{L-91880.3}
\]

where:

```text
n           anchored finite endpoint owner;
h           ordered rough-prime history;
i           unique least rough owner, or root owner;
d|P61       complete small-prime part;
epsilon     paired orientation bit;
c           complete causal current/child path.
```

Its coefficient is the literal native source coefficient times the product of
the exact stopping-line and causal coefficients along the path:

\[
\boxed{
a_X(\omega)
=a_X^{\rm native}(n,k)
 \prod_{r\in h}\gamma_r(c),
\qquad \gamma_r(c)\ge0.
}
\tag{L-91880.4}
\]

The finite stopping-line and first-owner identities imply

\[
\sum_{\omega\text{ over one native occurrence}}a_X(\omega)
=a_X^{\rm native}(n,k).
\tag{L-91880.5}
\]

The orientation bit is never erased before physical placement. The finite
forcing alone has the rough-lift observation; the oriented actual rough
children contribute the negative rough reservoir, so the complete anchored
stopping line has the native—not rough-lift—observation.

## 2. Signed comparison is not source

Let `E_X^I` be the exact retained-cell finite/continuum defect. Then

\[
\boxed{
 c_X=c_{X,A}+\overline c_{X,I}+\mathcal R E_X^I.
}
\tag{L-91880.6}
\]

The first two terms are observations of the anchored and bulk source sectors.
The last term is a signed observation correction. It is not a positive source
marginal and receives no Hall edge, first owner or child label.

## 3. Source space

The live positive input incidence space is

\[
\boxed{
\mathscr S_X
=\mathscr S_{X,B}^{+}\dotplus\mathscr S_{X,B}^{-}
 \dotplus\mathscr S_{X,A}^{+}\dotplus\mathscr S_{X,A}^{-}.
}
\tag{L-91880.7}
\]

The rough-lift row is only a normalization audit and is not a component of
`S_X`. The input marginal is exactly the native paired Möbius source underlying
(L-91880.6).

```text
bulk input marginal                  exact native Volterra Mobius source
anchored input marginal              exact native finite paired source
rough lift as parent                 forbidden
orientation bit                      retained
signed comparison                    separate observation ledger
```
