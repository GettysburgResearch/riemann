# L-96601 — Initial-prime sieving has an exact source-correct prefix recurrence

Claim ID: `L-96601`  
Status: **PROVED EXACT FINITE RECURRENCE**  
Created: 2026-08-17  
RH status: **not assumed**

Let `P` be a finite squarefree prime product and let

\[
a_{P,*}=q_* * \prod_{p\mid P}(\delta_1-\delta_p)
\]

be the actual finite prime-sieved scalar dictionary. Put

\[
M_P(N)=\sum_{n\le N}{a_{P,*}(n)\over\sqrt n}.
\]

If `p` is a prime not dividing `P`, coefficient comparison gives

\[
\boxed{
a_{Pp,*}(n)=a_{P,*}(n)-\mathbf1_{p\mid n}a_{P,*}(n/p),
}
\tag{L-96601.1}
\]

and hence

\[
\boxed{
M_{Pp}(N)=M_P(N)-p^{-1/2}M_P(\lfloor N/p\rfloor).
}
\tag{L-96601.2}
\]

This is the exact all-scale induction interface. It uses only source actually present in the finite dictionary; no all-integer block is substituted for a `P`-rough store.

When `2\mid P`, write `P=2P_o`. The complete coefficient ledger is

\[
\boxed{
\begin{aligned}
a_{P,*}(n)={}&6\mathbf1_{(n,P)=1}\\
&+\sum_{e\mid P_o}\mu(e)
\bigl[-6\mathbf1_{n=e}+15\mathbf1_{n=2e}
-12\mathbf1_{n=4e}+3\mathbf1_{n=8e}\bigr].
\end{aligned}}
\tag{L-96601.3}
\]

Thus every positive bulk occurrence and every signed correction atom has an explicit owner. The induction step is positive precisely when

\[
\boxed{
M_P(N)\ge p^{-1/2}M_P(\lfloor N/p\rfloor).
}
\tag{L-96601.4}
\]

Equation (L-96601.4), called the **Source-Correct Prefix Shadow inequality**, is not proved here. It is the smallest exact prime-by-prime producer interface left by the scalar route.
