# L-99023 — One square-root thinning closes every physical column without a quantization collar

Claim ID: `L-99023`  
Status: **PROPOSED COMPLETE ALL-COLUMN THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

Let `E_X^I` be the cumulative finite/continuum discrepancy formed from the
actual retained whole integer cells. Its adjacent differences satisfy

\[
|E_X^I(n)-E_X^I(n+1)|<\frac{19}{2}n^{-3/2}.
\tag{L-99023.1}

For every physical column `q>=2`, the exact adjacent-carry formula gives

\[
v_q(E_X^I)=\sum_{jq\in I_X}[E_X^I(jq)-E_X^I(jq+1)].
\]

With `K=floor(X/67)+1`,

\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K}
\]

and

\[
\boxed{
|\mathcal D_4v_q(E_X^I)|
<\frac{171}{4q\sqrt K}.
}
\tag{L-99023.2}

Unlike the former B-spline construction, `L-99022` has no quantization collar.
For `2<=q<=X/4`,

\[
\Omega_X(q)=\frac{\log4}{\sqrt q}>\frac4{3\sqrt q}.
\]

Therefore, using `q>=2`,

\[
\frac{|\mathcal D_4v_q(E_X^I)|}{\Omega_X(q)}
<\frac{513}{16\sqrt{qK}}<\frac{23}{\sqrt K}.
\tag{L-99023.3}

Apply once to the complete labelled parent the scalar

\[
\boxed{\tau_K=\frac{\sqrt K}{\sqrt K+24}.}
\tag{L-99023.4}

Then every nonterminal detail column satisfies

\[
\Xi_q(d_X)
<\tau_K\left(1+\frac{23}{\sqrt K}\right)\Omega_X(q)
=
\frac{\sqrt K+23}{\sqrt K+24}\Omega_X(q)
<\Omega_X(q).
\tag{L-99023.5}

This includes the complete formerly dangerous range `2<=q<K`.

For `q>X/4`, the finite mismatch is below `228X^{-3/2}`. The fixed top
omission removes more than `5033X^{-3/2}` from every terminal column that could
overfill. Hence the terminal reserve is greater than

\[
\boxed{4805X^{-3/2}>0.}
\tag{L-99023.6}

At and above the retained support, the response is zero. Thus

\[
\boxed{\Xi(d_X)\le\Omega_X\quad(q\ge2).}
\tag{L-99023.7}

The positive finite radix-four inverse gives ordinary feasibility from the same
row:

\[
w_X(q)-C_{d_X}(q)
=
\sum_{h\ge0}2^h[\Omega_X(4^hq)-\Xi_{d_X}(4^hq)]\ge0.
\tag{L-99023.8}

No auxiliary port is used. Child capacities are reserved once inside the
exact causal row identity and child ports are identically zero.
