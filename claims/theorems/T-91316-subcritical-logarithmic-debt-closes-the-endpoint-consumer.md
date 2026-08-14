# T-91316 — A strictly subcritical reset with logarithmic local debt closes the endpoint consumer

Claim ID: `T-91316`  
Status: **PROVED CONDITIONAL CONSUMER**  
Created: 2026-08-14  
Depends on: `T-91313`; packet homogeneity and subadditivity  
RH status: **conditional**

Let `Lambda(X)` be the worst positive normalized packet deficit through scale
`X`.  Suppose that for constants

\[
 0<\theta<1,
 \qquad R>1,
 \qquad C,C_0\ge0,
\]

one has, for all sufficiently large `X`,

\[
\boxed{
 \Lambda(X)
 \le C\log(3X)+
 \theta\Lambda(X/R+C_0).
}
\tag{T-91316.1}
\]

Iterating until the endpoint enters a fixed base range gives

\[
 \Lambda(X)
 \le C\log(3X)\sum_{k\ge0}\theta^k
 +O_{\rm base}(1).
\]

Therefore

\[
\boxed{
 \Lambda(X)
 \le\frac{C}{1-\theta}\log(3X)+O_{\rm base}(1)
 =O(\log X)=o(\log^2X).
}
\tag{T-91316.2}
\]

The explicit values `theta<1/8` and `R=67` are more than sufficient.  By the
one-sided endpoint consumer `T-91313`, the corresponding native producer would
imply RH.

The theorem is only a consumer.  It does not prove the exact positive typed
entry, common mass normalization, or one-use boundary ledger required to
obtain (T-91316.1).
