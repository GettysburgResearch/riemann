"""Bounded, pure numerical providers. All analytic values are scouts, not certificates."""
from __future__ import annotations
import hashlib
import json
import math
from decimal import Decimal, localcontext
from functools import lru_cache
from pathlib import Path
from typing import Literal
import mpmath
from pydantic import BaseModel, ConfigDict, Field, model_validator

VERSION = "0.1.0"

class Spec(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    module: Literal["geometry", "primes", "euler", "mobius", "zeros", "height"] = "geometry"
    function: Literal["zeta", "eta", "xi", "beta", "chi3"] = "zeta"
    dps: int = Field(30, ge=20, le=70)
    re_min: float = Field(-1, ge=-4, le=4)
    re_max: float = Field(2, ge=-4, le=4)
    t_min: float = Field(10, ge=-1000, le=1000)
    t_max: float = Field(35, ge=-1000, le=1000)
    sigma: float = Field(0.5, ge=-4, le=4)
    t: float = Field(14.134725, ge=-1000, le=1000)
    grid: int = Field(40, ge=16, le=80)
    samples: int = Field(384, ge=32, le=2048)
    limit: int = Field(2000, ge=10, le=200000)
    buckets: int = Field(360, ge=16, le=1024)
    kernel_n: int = Field(48, ge=8, le=96)
    width: float = Field(0.5, ge=0.03, le=4)
    zero_count: int = Field(24, ge=2, le=64)
    omit_prime: Literal[0, 2, 3, 5, 7] = 0
    height_record: Literal[1, 2] = 1

    @model_validator(mode="after")
    def limits(self):
        if self.re_max - self.re_min < 1e-6 or self.t_max - self.t_min < 1e-6:
            raise ValueError("Bounds must increase by at least 1e-6; use the exact-height desk for huge coordinates.")
        if self.module == "euler" and self.limit > 10000:
            raise ValueError("The live Euler provider supports a prime cutoff at most 10000.")
        return self

class Coordinate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    anchor: str = Field(pattern=r"^-?\d{1,100}$", max_length=101)
    offset: str = Field(pattern=r"^-?\d{1,20}(\.\d{1,60})?$", max_length=82)

    def exact(self):
        with localcontext() as ctx:
            ctx.prec = 200
            return format(Decimal(self.anchor) + Decimal(self.offset), "f")

def finite(x):
    try:
        value = float(x)
        return value if math.isfinite(value) and not (value == 0 and x != 0) else None
    except (ValueError, OverflowError, TypeError):
        return None

def reduce_series(xs, ys, budget=360):
    """First/min/max/last per contiguous finite bucket; retain every missing-data break.

    Extrema and sums concern the *sampled* input, not the continuous function.
    No cancellation or event inference is made from the display vertices.
    """
    if len(xs) != len(ys) or budget < 1:
        raise ValueError("Mismatched arrays or invalid budget")
    n = len(xs)
    if not n:
        return {"points": [], "envelopes": [], "input_count": 0, "missing_count": 0}
    step = max(1, math.ceil(n / budget))
    selected, envelopes = set(), []
    missing = 0
    start = 0
    while start < n:
        if ys[start] is None or not math.isfinite(float(ys[start])):
            selected.add(start)
            missing += 1
            start += 1
            continue
        end = start + 1
        while end < min(n, start + step) and ys[end] is not None and math.isfinite(float(ys[end])):
            end += 1
        indices = range(start, end)
        lo, hi = min(indices, key=lambda k: ys[k]), max(indices, key=lambda k: ys[k])
        selected.update((start, end - 1, lo, hi))
        if step > 1:
            values = [ys[k] for k in indices]
            envelopes.append({"x0": xs[start], "x1": xs[end-1], "min": ys[lo], "max": ys[hi],
                              "min_x": xs[lo], "max_x": xs[hi], "count": end-start,
                              "sum": math.fsum(values), "absolute_sum": math.fsum(abs(v) for v in values)})
        start = end
    return {"points": [[xs[k], finite(ys[k])] for k in sorted(selected)], "envelopes": envelopes,
            "input_count": n, "missing_count": missing,
            "contract": "Sampled first/min/max/last, extrema locations, signed and absolute bucket sums; gaps retained. Not a continuous bound."}

def series(label, xs, ys, budget, unit=""):
    return {"label": label, "unit": unit, **reduce_series(xs, ys, budget)}

@lru_cache(maxsize=4)
def sieve(n):
    """Linear sieve: exact primes and Möbius values for every integer 1..n."""
    lp, mu, primes = [0]*(n+1), [0]*(n+1), []
    mu[1] = 1
    for i in range(2, n+1):
        if not lp[i]:
            lp[i], mu[i] = i, -1
            primes.append(i)
        for p in primes:
            if i*p > n:
                break
            lp[i*p] = p
            if i % p == 0:
                mu[i*p] = 0
                break
            mu[i*p] = -mu[i]
    return primes, mu

def evaluator(ctx, name, s):
    if name == "eta":
        return ctx.altzeta(s)
    if name == "beta":
        return ctx.dirichlet(s, [0, 1, 0, -1])
    if name == "chi3":
        return ctx.dirichlet(s, [0, 1, -1])
    if name == "xi":
        if s == 0 or s == 1:
            return ctx.mpf("0.5")
        # This identity removes the s=0 and negative-even gamma poles.
        if s.real < ctx.mpf("0.5"):
            s = 1-s
        return (s-1)*ctx.power(ctx.pi, -s/2)*ctx.gamma(1+s/2)*ctx.zeta(s)
    return ctx.zeta(s)

def safe_eval(ctx, name, s):
    try:
        z = evaluator(ctx, name, s)
        if not ctx.isfinite(z):
            return None
        return z
    except (ValueError, ZeroDivisionError, OverflowError):
        return None

def geometry(q, ctx):
    n = q.grid
    # Include endpoints; pixels represent samples, not certified whole cells.
    sigmas = [q.re_min+(q.re_max-q.re_min)*j/(n-1) for j in range(n)]
    ts = [q.t_min+(q.t_max-q.t_min)*j/(n-1) for j in range(n)]
    phase, magnitude, real, imag = [], [], [], []
    for t in ts:
        for sigma in sigmas:
            z = safe_eval(ctx, q.function, ctx.mpc(str(sigma), str(t)))
            phase.append(finite(ctx.arg(z)) if z is not None else None)
            magnitude.append(finite(ctx.log1p(abs(z))) if z is not None else None)
            real.append(finite(z.real) if z is not None else None)
            imag.append(finite(z.imag) if z is not None else None)
    xs = [q.t_min+(q.t_max-q.t_min)*j/(q.samples-1) for j in range(q.samples)]
    values = [safe_eval(ctx, q.function, ctx.mpc(str(q.sigma), str(t))) for t in xs]
    curves = [series(label, xs, [finite(f(z)) if z is not None else None for z in values], q.buckets)
              for label, f in [("Re f", lambda z:z.real), ("Im f", lambda z:z.imag), ("|f|", abs)]]
    events = []
    if q.function == "zeta":
        zs = [finite(ctx.siegelz(ctx.mpf(str(t)))) for t in xs]
        curves.append(series("Hardy Z(t), on σ = 1/2", xs, zs, q.buckets))
        for i in range(1, len(xs)):
            if zs[i] is not None and zs[i-1] is not None and zs[i]*zs[i-1] < 0:
                events.append({"x0": xs[i-1], "x1": xs[i], "kind": "sampled sign change", "status": "uncertified"})
    return {"series": curves, "grid": {"kind":"complex", "n":n, "x":sigmas, "y":ts,
            "phase":phase, "magnitude":magnitude, "real":real, "imag":imag}, "events": events,
            "metrics": {"grid_samples": n*n, "slice_samples":q.samples, "candidate_brackets":len(events)},
            "formula": "Vertical slice f(σ+it); Hardy Z(t)=exp(iθ(t)) ζ(1/2+it) is always on the critical line.",
            "warnings": ["Domain colors and sign-change candidates are not zero certificates or a complete census.",
                         "Hue = phase; brightness = log(1+|f|). Missing/nonfinite samples are masked."]}

@lru_cache(maxsize=1)
def gram_constants():
    ctx = mpmath.mp.clone()
    ctx.dps = 35
    return [0.0] + [float(ctx.zeta(k+1)) for k in range(1, 81)]

def li_r(x):
    """Floating Gram/Ei series, x>=2 in our bounded arithmetic desk; not enclosures."""
    u, term = math.log(x), 1.0
    li_terms, r_terms = [], []
    zetas = gram_constants()
    for k in range(1, 81):
        term *= u/k
        a = term/k
        li_terms.append(a)
        r_terms.append(a/zetas[k])
    return 0.5772156649015329 + math.log(u)+math.fsum(li_terms), 1+math.fsum(r_terms)

def primes_desk(q, ctx):
    primes, _ = sieve(q.limit)
    prime_set = set(primes)
    theta = psi = 0.0
    count = 0
    lambdas = {}
    for p in primes:
        k = p
        while k <= q.limit:
            lambdas[k] = math.log(p)
            k *= p
    xs = list(range(2, q.limit+1))
    values = [[] for _ in range(7)]
    for x in xs:
        if x in prime_set:
            count += 1
            theta += math.log(x)
        psi += lambdas.get(x, 0)
        li, r = li_r(x)
        for a, v in zip(values, [count, li, r, count-li, count-r, (psi-x)/math.sqrt(x), (theta-x)/math.sqrt(x)]):
            a.append(v)
    labels = ["π(x)", "Li(x), principal value", "R(x), Gram series", "π(x) − Li(x)", "π(x) − R(x)", "(ψ(x) − x)/√x", "(θ(x) − x)/√x"]
    return {"series": [series(a,xs,b,q.buckets) for a,b in zip(labels,values)], "events":[],
            "metrics":{"π(limit)":count, "last_prime":primes[-1], "integer_samples":len(xs)},
            "formula":"π(x)=#{p≤x}; ψ(x)=Σ[p^k≤x] log p. Li(x)=Ei(log x); R(x)=1+Σ[k≥1](log x)^k/(k·k!·ζ(k+1)).",
            "warnings":["π and the prime sieve are exact at sampled integers. Logs, Li, R and residuals are floating scouts.",
                        "Li/R use 80-term series in the bounded domain 2≤x≤200000; no interval error bound is asserted.",
                        "Every integer is computed before reduction. Bucket extrema do not assert between-integer extrema."]}

def euler(q, ctx):
    primes, _ = sieve(q.limit)
    s = ctx.mpc(str(q.sigma), str(q.t))
    target = safe_eval(ctx, "zeta", s)
    product = ctx.mpc(1)
    xs, re, im, error, mod = [],[],[],[],[]
    for p in primes:
        if p == q.omit_prime:
            continue
        factor = 1-ctx.power(p, -s)
        if factor == 0:
            raise ValueError("This finite Euler product has a pole at a selected local factor.")
        product /= factor
        xs.append(p)
        re.append(finite(product.real)); im.append(finite(product.imag))
        mod.append(finite(abs(product)))
        error.append(finite(abs(product-target)) if target is not None else None)
    warnings = ["The curve is a finite product. The standard infinite Euler product converges absolutely only for Re(s)>1."]
    if q.sigma <= 1:
        warnings.append("OUTSIDE ABSOLUTE CONVERGENCE: this is NOT analytic continuation of the Euler product.")
    if q.omit_prime:
        warnings.append("A local factor is omitted. The comparison target remains the original ζ(s), not the altered product's infinite limit.")
    return {"series":[series(a,xs,b,q.buckets) for a,b in [("Re E_P",re),("Im E_P",im),("|E_P|",mod),("|E_P − ζ(s)|",error)]],
            "argand":{"real":re,"imag":im,"cutoffs":xs},"events":[],
            "metrics":{"factors":len(xs), "ζ(s)":ctx.nstr(target, q.dps) if target is not None else "pole / unavailable", "E_P(s)":ctx.nstr(product,q.dps)},
            "formula":"E_P(s)=∏[p≤P, p not omitted] (1−p^(−s))^(−1). Inspect cutoff sensitivity; no product-tail bound is supplied.", "warnings":warnings}

def mobius(q, ctx):
    _, mu = sieve(max(q.limit, q.kernel_n))
    xs = list(range(1, q.limit+1))
    total, harmonic, variation = 0, 0.0, 0.0
    m, normalized, h, v = [],[],[],[]
    for x in xs:
        total += mu[x]; harmonic += mu[x]/x; variation += abs(mu[x])/x
        m.append(total); normalized.append(total/math.sqrt(x)); h.append(harmonic); v.append(variation)
    n, split = q.kernel_n, q.kernel_n//2
    weights = [mu[i]/math.sqrt(i) for i in range(1,n+1)]
    logs = [math.log(i) for i in range(1,n+1)]
    matrix = [weights[i]*weights[j]*math.exp(-((logs[i]-logs[j])/q.width)**2/2) for i in range(n) for j in range(n)]
    aa=math.fsum(matrix[i*n+j] for i in range(split) for j in range(split))
    bb=math.fsum(matrix[i*n+j] for i in range(split,n) for j in range(split,n))
    cross=2*math.fsum(matrix[i*n+j] for i in range(split) for j in range(split,n))
    energy=math.fsum(matrix)
    return {"series":[series(a,xs,b,q.buckets) for a,b in [("M(x)",m),("M(x)/√x",normalized),("Σ μ(n)/n",h),("Σ |μ(n)|/n",v)]],
            "grid":{"kind":"interaction","n":n,"values":matrix,"x":list(range(1,n+1)),"y":list(range(1,n+1))}, "events":[],
            "metrics":{"M(limit)":total,"kernel_prefix":n,"split_at":split,"energy_A":aa,"energy_B":bb,"cross_term":cross,"full_energy":energy,"identity_residual":energy-(aa+bb+cross)},
            "formula":"aₙ=μ(n)/√n; Kₘₙ=exp(−(log m−log n)²/(2h²)); Q=Σₘₙ aₘKₘₙaₙ=Q_A+Q_B+2C_AB; A=first half of the finite prefix, B=its complement.",
            "warnings":[f"The interaction panel uses the COMPLETE finite prefix 1..{n}, not the larger Mertens-curve prefix 1..{q.limit}.","All cross terms are retained. The floating kernel energy is not a theorem about an infinite operator or RH."]}

def zeros(q, ctx):
    ts = [ctx.im(ctx.zetazero(k)) for k in range(1,q.zero_count+1)]
    xs = list(range(1,len(ts)))
    gaps=[float(ts[i+1]-ts[i]) for i in range(len(xs))]
    normalized=[float((ts[i+1]-ts[i])*ctx.log((ts[i+1]+ts[i])/(4*ctx.pi))/(2*ctx.pi)) for i in range(len(xs))]
    return {"series":[series("Raw consecutive gap",xs,gaps,q.buckets),series("Locally normalized gap",xs,normalized,q.buckets)],
            "events":[{"index":i+1,"x0":float(t),"x1":float(t),"decimal":ctx.nstr(t,q.dps),"kind":"mpmath zetazero","status":"approximate"} for i,t in enumerate(ts)],
            "metrics":{"zeros_requested":len(ts),"smallest_gap":min(gaps),"largest_gap":max(gaps)},
            "formula":"Normalized gap = (γₙ₊₁−γₙ) log(((γₙ+γₙ₊₁)/2)/(2π))/(2π). No finite-sample ensemble claim.",
            "warnings":["mpmath's indexed critical-line zeros are ordinary high-precision numerical data, not a certificate produced by this application.","These few low zeros do not represent asymptotic statistics. Raw data, not display decimation, determine gaps."]}

RECORDS = {
    1: {"anchor":"763173730199776587433631628770", "lo":"-0.068203", "hi":"-0.068103", "S":"4.184313 < S(γ₁+0) < 4.185380 (imported claim)"},
    2: {"anchor":"201016554543249943627430143193", "lo":"0.078398", "hi":"0.078428", "S":"−4.33869 < S(γ₂−0) < −4.33837 (imported claim)"},
}

def height(q, ctx):
    r=RECORDS[q.height_record]
    lo, hi = Coordinate(anchor=r["anchor"],offset=r["lo"]), Coordinate(anchor=r["anchor"],offset=r["hi"])
    with localcontext() as dc:
        dc.prec=200
        width=format(Decimal(r["hi"])-Decimal(r["lo"]),"f")
    return {"series":[],"events":[{"x0":float(r["lo"]),"x1":float(r["hi"]),"kind":"imported fine bracket","status":"primitive replay pending"}],
            "record":r,"metrics":{"anchor":r["anchor"],"left_exact":lo.exact(),"right_exact":hi.exact(),"width_exact":width,"primitive_Z_replayed":False},
            "formula":"t=T+δ. Add exact decimal strings before any conversion; only local offsets reach the canvas.",
            "sources":["https://github.com/GettysburgResearch/riemann/blob/d5d55b7950a4cc8a850e99c82b8f40e1699c7a3e/standalone/2026-09-15-s-argument-records/news.txt"],
            "warnings":["Two fine brackets only, transcribed from the source-pinned, user-supplied announcement in #891; original announcement credited there to Avraham Eisenberg.","No coarse-bracket import, Hardy-Z evaluation, certificate replay or independent record verification is performed here.","The plot is an interval on the offset axis, NOT a synthetic Z curve. Empty space is not evidence of no zeros."]}

PROVIDERS={"geometry":geometry,"primes":primes_desk,"euler":euler,"mobius":mobius,"zeros":zeros,"height":height}

def compute(payload):
    q=Spec.model_validate(payload)
    ctx=mpmath.mp.clone(); ctx.dps=q.dps
    ctx._fp=mpmath.fp  # mpmath 1.3 zetazero requires its read-only fast context.
    data=PROVIDERS[q.module](q,ctx)
    data.update(schema_version=1,engine_version=VERSION,engine_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),request=q.model_dump(),
                evidence="imported claim; primitive replay pending" if q.module=="height" else "numerical scout; not certified",
                provider=f"mpmath {mpmath.__version__}; Python integer sieve; float display",
                precision={"requested_dps":q.dps,"working_note":"dps applies to mpmath evaluations. Coordinates/grids and displayed curves are binary64; prime main terms and kernels use binary64."})
    encoded=json.dumps(data,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    data["result_id"]=hashlib.sha256(encoded).hexdigest()
    return data
