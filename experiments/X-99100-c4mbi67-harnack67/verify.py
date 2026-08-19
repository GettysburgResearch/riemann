#!/usr/bin/env python3
"""Independent fast verifier for T-99100."""
from __future__ import annotations
import hashlib, json, math, re
from pathlib import Path
from typing import Dict, List

HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "results" / "harnack67_exact_2e9.json"
RESULT_TEXT = HERE / "results" / "harnack67_exact_2e9.txt"
SEGMENTS = HERE / "results" / "harnack67_segments_2e9.txt"
EXPECTED = {
    "N": 2_000_000_000,
    "prime": 67,
    "scale": 1 << 40,
    "segments": 20,
    "nonzero": 1_520_151_319,
    "minimum_lower_num": 57_262_723_035,
    "minimum_lower_at": 61_848_971,
    "minimum_upper_num": 57_692_032_737,
    "minimum_upper_at": 61_848_971,
    "final_lower_num": 5_575_436_478_759,
    "final_upper_num": 5_589_318_993_237,
    "proof_object_sha256": "e4534298fd460fdaef22065645a6abd25022f58a093580ca00321de29b8e17c4",
}

def mobius_linear(n: int) -> List[int]:
    mu = [0] * (n + 1); lp = [0] * (n + 1); primes: List[int] = []; mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i; primes.append(i); mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n: break
            lp[i*p] = p; mu[i*p] = 0 if p == lp[i] else -mu[i]
    return mu

def a_direct(mu: List[int], n: int) -> int:
    a = (6 if n == 1 else 0) - 6 * mu[n]
    if n % 2 == 0: a += 9 * mu[n//2]
    if n % 4 == 0: a -= 3 * mu[n//4]
    return a

def b_factor(n: int, mu: List[int]) -> int:
    m = n; e2 = 0
    while m % 2 == 0: m //= 2; e2 += 1
    e67 = 0
    while m % 67 == 0: m //= 67; e67 += 1
    c2 = (2, -5, 4, -1); c67 = (1, -2, 1)
    b = (6 if n == 1 else 0) - (6 if n == 67 else 0)
    if e2 < len(c2) and e67 < len(c67): b += -3 * c2[e2] * c67[e67] * mu[m]
    return b

def exact_small_scan(limit: int = 200_000) -> int:
    mu = mobius_linear(limit)
    scale = 1 << 40; scale2 = scale * scale; lo = 0; min_lo = None
    for n in range(1, limit + 1):
        direct = a_direct(mu, n) - (a_direct(mu, n//67) if n % 67 == 0 else 0)
        factored = b_factor(n, mu)
        assert direct == factored, (n, direct, factored)
        if direct:
            q = math.isqrt(scale2 // n)
            assert q*q*n <= scale2 < (q+1)*(q+1)*n
            lo += direct*q if direct > 0 else direct*(q+1)
        if n >= 2 and (min_lo is None or lo < min_lo): min_lo = lo
    assert min_lo is not None and min_lo > 0
    return min_lo

def parse_segment_bundle() -> List[Dict[str, int]]:
    chunks = re.split(r"^===== segment \d+ =====\n", SEGMENTS.read_text(encoding="utf-8"), flags=re.M)[1:]
    assert len(chunks) == 20
    out: List[Dict[str, int]] = []
    integer_keys = {"L","R","scale","nonzero","relative_min_lower_num","relative_min_upper_num","delta_lower_num","delta_upper_num"}
    for chunk in chunks:
        d: Dict[str, int] = {}
        for line in chunk.splitlines():
            p = line.split()
            if not p: continue
            if p[0] in integer_keys: d[p[0]] = int(p[1])
            elif p[0] == "relative_min_lower": d["relative_min_lower_at"] = int(p[-1])
            elif p[0] == "relative_min_upper": d["relative_min_upper_at"] = int(p[-1])
        out.append(d)
    return out

def main() -> None:
    d = json.loads(RESULT_JSON.read_text(encoding="utf-8"))
    for k, v in EXPECTED.items(): assert d[k] == v, (k, d[k], v)
    assert d["verdict"] == "PASS_T99100_HARNACK67_TWO_BILLION_EXACT_SEGMENTED"
    assert d["status"] == {"global_cprefix_sign": False, "global_harnack67": False, "harnack67_through_2e9": True, "rh_established": False}
    saved_hash = d.pop("proof_object_sha256")
    canonical = json.dumps(d, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(canonical).hexdigest() == saved_hash
    d["proof_object_sha256"] = saved_hash
    segs = parse_segment_bundle(); cum_lo = cum_hi = 0; best_lo = best_hi = None
    for k, s in enumerate(segs, 1):
        assert s["L"] == (k-1)*100_000_000 + 1 and s["R"] == k*100_000_000
        cand_lo = cum_lo + s["relative_min_lower_num"]
        cand_hi = cum_hi + s["relative_min_upper_num"]
        if best_lo is None or cand_lo < best_lo[0]: best_lo = (cand_lo, s["relative_min_lower_at"])
        if best_hi is None or cand_hi < best_hi[0]: best_hi = (cand_hi, s["relative_min_upper_at"])
        cum_lo += s["delta_lower_num"]; cum_hi += s["delta_upper_num"]
    assert best_lo == (EXPECTED["minimum_lower_num"], EXPECTED["minimum_lower_at"])
    assert best_hi == (EXPECTED["minimum_upper_num"], EXPECTED["minimum_upper_at"])
    assert cum_lo == EXPECTED["final_lower_num"] and cum_hi == EXPECTED["final_upper_num"]
    assert "PASS YES" in RESULT_TEXT.read_text(encoding="utf-8")
    small_min = exact_small_scan()
    print("PASS_T99100_HARNACK67_FAST_REPLAY")
    print(saved_hash)
    print(f"small_exact_min_lower_num={small_min}")
if __name__ == "__main__": main()
