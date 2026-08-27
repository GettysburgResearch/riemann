# R-105416 — Raw shifted-zero flow omits the source anchor and the even central branch

Claim ID: `R-105416`  
Status: **PROVED EXACT COMPOSITIONAL FIREWALL**  
Created: 2026-08-24  
Depends on: `L-105416`  
RH status: **not assumed**

## 1. Raw critical motion is not boundary capacity

For the inverse-power test `Psi_(q,a)`, the raw oriented motion of the
noncentral zeros is

\[
{1\over2}
\left.\partial_\alpha
\mathfrak Z_\alpha^\sharp(\Psi_{q,a})
\right|_0
=-q^T\mathsf C_k^{(a)}q.
\]

The boundary quantity is instead

\[
q^T\mathsf S_k^{(a)}q
=q^T\mathsf A_k^{(a)}q-q^T\mathsf C_k^{(a)}q.
\]

The missing term is the residue of the meromorphic test at the analytic source
anchor. It is generally order one and cannot be discarded as a contour error.

## 2. Exact odd polynomial separator

Let

\[
F(z)=z^5/5-5z^3/3+4z,
\qquad
F'(z)=(z^2-1)(z^2-4).
\]

The nonzero critical points are `+-1,+-2`. For `q=1,a=0`, exact arithmetic
gives

\[
q^T\mathsf A_1^{(0)}q=1,
\qquad
{1\over2}\mathfrak Z_0'=-{4\over5}.
\]

But an outer polynomial window has boundary remainder `z/5`, so

\[
\boxed{
q^T\mathsf S_1^{(0)}q
=1-{4\over5}={1\over5}>0.
}
\]

The raw zero motion has the wrong value and even the wrong sign.

## 3. Exact even central-branch separator

Let

\[
F(z)=z^6/6-5z^4/4+2z^2+3,
\qquad
F'(z)=z(z^2-1)(z^2-4).
\]

The central residue is

\[
\rho_0={3\over4}.
\]

After its correct removal, the first source coefficient is

\[
a_0={23\over16}.
\]

The noncentral shifted-zero flow is

\[
{1\over2}\mathfrak Z_0'=-{61\over48}.
\]

The full polynomial boundary remainder is `z/6`, and indeed

\[
\boxed{
{23\over16}-{61\over48}={1\over6}.
}
\]

Using the raw ratio `(F'-alpha F)/(F'+alpha F)` without factoring the moving
central zero replaces the regularized tangent by `-2F/F'` and reintroduces the
principal part `-2rho_0/z`. Every inverse-power test is then malformed.

## 4. Finite sampling is not the outer-phase gate

Even after the critical poles are signed, checking

\[
\operatorname{Im}F(z_j)/F'(z_j)\ge0
\]

at finitely many outer-boundary points does not invoke the harmonic minimum
principle. `OPG105417` requires a cofinal uniform lower bound on the complete
outer boundary. A finite packet or bounded confluent order cannot substitute
for that condition.

## 5. Binding conclusions

```text
raw shifted-zero motion                     = negative critical consumption;
anchor-renormalized flow                     = boundary reserve;
even raw ratio                               contains a moving central defect;
finite outer samples                         do not imply the phase gate.
```

Any continuation omitting the anchor residue or the even central branch is
non-normative.