# R-91880 — The infinitesimal Volterra packet is not a causal-generator type

Claim ID: `R-91880`  
Status: **PROVED EXACT TYPE FIREWALL**  
Created: 2026-08-16  
Review source: PR #503  
RH status: **unproved**

Let

\[
g_s(m)=\left(\sqrt m-\frac m{\sqrt s}\right)\mathbf 1_{m\le s},
\qquad
p_s=\mathcal R g_s.
\]

At

\[
(p,y,s,j)=(67,15,1005,14)
\]

the exact directed certificate of PR #503 gives

\[
\boxed{
-\frac{184291}{10^9}
< p_{1005}(14)-67^{-1/2}p_{15}(14)
< -\frac{184290}{10^9}<0.
}
\tag{R-91880.1}
\]

Therefore the operation

\[
p_s\longmapsto p_s-p^{-1/2}p_{s/p}
\]

is not a positive causal generator on the Volterra infinitesimal family.
Neither endpoint integration nor target-mass normalization can repair a
negative component coordinate which already occurs on one fibre.

The successor uses the following strict type split:

```text
Volterra infinitesimal packet p_s:
    root-current only;
    rank-one small-divisor cancellation;
    direct endpoint placement;
    never a causal parent and never a rough child.

complete finite-Q arithmetic packet:
    may enter the exact P61 stopping line;
    retains the parity/orientation bit;
    uses first rough ownership and complete finite-Q causal paths;
    terminal leaves are compiled by the hardened Target-Lorenz theorem.
```

At the same numerical parameters the complete finite-Q causal coordinate obeys

\[
\boxed{
Q_{1005}(14)-67^{-1/2}Q_{15}(14)>\frac15.
}
\tag{R-91880.2}
\]

The replay proves both (R-91880.1) and (R-91880.2) with rational interval
arithmetic. Thus the new split does not evade the counterexample by changing a
constant: it applies the causal operator only to a packet class on which the
frozen finite-Q theorem is valid.

```text
infinitesimal causal positivity             false / exact witness
bulk use of infinitesimal causal operator   forbidden
finite-Q causal packet at witness           positive with moat >1
anchored finite-Q causal paths               permitted on frozen theorem
Riemann Hypothesis                          unproved
```
