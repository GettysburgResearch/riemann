# R-100721 — The unrestricted left Taylor certificate is power-sized

Claim ID: `R-100721`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-21  
Depends on: `L-100720--L-100723`  
RH status: **not assumed**

The first draft of the cubic collar gate defined

\[
\mathcal L(t)
={1\over2}\int_0^t(t-u)^2|\widetilde H'''(u)|du
\]

and proposed integrating `mathcal L` over every later physical scale. That
statement is false for every nonzero centered collar.

Let

\[
T_*=\sup\operatorname{supp}\widetilde H'''<\infty
\]

and put

\[
m_j=\int_0^{T_*}u^j|\widetilde H'''(u)|du
\qquad(j=0,1,2).
\]

If the collar is nonzero, then `m_0>0`. For every `t>=T_*`,

\[
\boxed{
\mathcal L(t)
={m_0\over2}t^2-m_1t+{m_2\over2}.
}
\tag{R-100721.1}

Thus

\[
\mathcal L(t)\sim{m_0\over2}t^2.
\]

In the physical variable `X=t^2`,

\[
\int^{Y}\mathcal L(\sqrt X){dX\over X}
\asymp Y.
\tag{R-100721.2}

The actual centered collar, and hence its negative part, is already zero on
this deep range. The power loss is entirely an artefact of spending the left
Taylor remainder after the right boundary has become exact.

Consequently the former statement `LPCC100723`, which integrated the raw left
certificate without an adaptive cutoff, is false and is removed from the
conclusion graph.

`L-100723` repairs the gate by spending

```text
left certificate only where L<=R;
right certificate only where R<L.
```

The deterministic partition is made from the two source-owned certificates,
not from the sign of the physical scalar.
