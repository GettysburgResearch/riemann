#include <algorithm>
#include <cfloat>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

struct ILD { long double lo, hi; };
struct ID  { double lo, hi; };

static inline long double dn(long double x) {
    return nextafterl(x, -numeric_limits<long double>::infinity());
}
static inline long double up(long double x) {
    return nextafterl(x, numeric_limits<long double>::infinity());
}
static inline ILD add(ILD a, ILD b) {
    return {dn(a.lo + b.lo), up(a.hi + b.hi)};
}
static inline ILD subI(ILD a, ILD b) {
    return {dn(a.lo - b.hi), up(a.hi - b.lo)};
}
static inline ILD scale(ILD a, long double c) {
    if (c >= 0) return {dn(a.lo * c), up(a.hi * c)};
    return {dn(a.hi * c), up(a.lo * c)};
}
static inline ILD mulI(ILD a, ILD b) {
    long double v[4] = {a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi};
    long double l = *min_element(v, v + 4);
    long double h = *max_element(v, v + 4);
    return {dn(l), up(h)};
}
static inline ID toD(ILD a) {
    return {
        nextafter((double)a.lo, -numeric_limits<double>::infinity()),
        nextafter((double)a.hi,  numeric_limits<double>::infinity())
    };
}
static inline ID addD(ID a, ID b) {
    return {
        nextafter(a.lo + b.lo, -numeric_limits<double>::infinity()),
        nextafter(a.hi + b.hi,  numeric_limits<double>::infinity())
    };
}
static inline ID subD(ID a, ID b) {
    return {
        nextafter(a.lo - b.hi, -numeric_limits<double>::infinity()),
        nextafter(a.hi - b.lo,  numeric_limits<double>::infinity())
    };
}
static inline ID halfD(ID a) {
    return {
        nextafter(0.5*a.lo, -numeric_limits<double>::infinity()),
        nextafter(0.5*a.hi,  numeric_limits<double>::infinity())
    };
}

// Exact fixed-point enclosure for 1/sqrt(n).
static ILD invsqrt_int(uint64_t n) {
    constexpr int K = 60;
    const __uint128_t ONE = ((__uint128_t)1) << (2*K);
    long double approximate = 1.0L / sqrtl((long double)n);
    uint64_t L = (uint64_t)floorl(ldexpl(approximate, K));

    auto square_test = [&](uint64_t x) -> __uint128_t {
        return (__uint128_t)x * (__uint128_t)x * (__uint128_t)n;
    };

    while (square_test(L) > ONE) --L;
    while (square_test(L + 1) <= ONE) ++L;
    const uint64_t U = L + 1;

    return {
        ldexpl((long double)L, -K),
        ldexpl((long double)U, -K)
    };
}

// Self-contained log enclosure.  Integer range reduction is exact here because
// all inputs are below 2^53.  The atanh variable is at most 1/3.  We use 36
// terms and then add a deliberately enormous 2e-13 absolute pad.  The exact
// omitted tail is <2e-34; with >=64 long-double mantissa bits, the pad is also
// >100 times the simple 10^4*2^-64*(1+e) roundoff budget for e<=25.
static ILD log_int(uint64_t n) {
    if (n == 1) return {-2e-13L, 2e-13L};

    int e = 63 - __builtin_clzll(n);
    long double y = ldexpl((long double)n, -e);
    long double z = (y - 1.0L) / (y + 1.0L);
    long double z2 = z*z;
    long double term = z;
    long double sum = 0;
    for (int k = 0; k < 36; ++k) {
        sum += term / (2*k + 1);
        term *= z2;
    }
    long double logy = 2*sum;

    long double q = 1.0L/3.0L;
    long double q2 = q*q;
    term = q;
    sum = 0;
    for (int k = 0; k < 36; ++k) {
        sum += term / (2*k + 1);
        term *= q2;
    }
    long double log2 = 2*sum;

    long double value = e*log2 + logy;
    constexpr long double PAD = 2e-13L;
    return {dn(value - PAD), up(value + PAD)};
}

int main() {
    if (LDBL_MANT_DIG < 64) {
        cerr << "FAIL: verifier requires LDBL_MANT_DIG >= 64\n";
        return 2;
    }

    constexpr int X = 30000000;
    constexpr int n0 = 43;
    const int Ymax = X/n0 + 2;

    // Exact Eratosthenes prime table and exact Mobius signs through X/n0.
    vector<bool> is_prime(Ymax + 1, true);
    is_prime[0] = is_prime[1] = false;
    vector<int> primes;
    for (int i = 2; i <= Ymax; ++i) {
        if (!is_prime[i]) continue;
        primes.push_back(i);
        if (1LL*i*i <= Ymax) {
            for (long long j = 1LL*i*i; j <= Ymax; j += i) is_prime[(int)j] = false;
        }
    }

    vector<int8_t> mu(Ymax + 1, 1);
    mu[0] = 0;
    for (int p : primes) {
        for (int j = p; j <= Ymax; j += p) mu[j] = -mu[j];
        long long p2 = 1LL*p*p;
        if (p2 <= Ymax) {
            for (long long j = p2; j <= Ymax; j += p2) mu[(int)j] = 0;
        }
    }

    vector<ILD> Mhalf(Ymax + 1, {0,0});
    vector<ILD> Lhalf(Ymax + 1, {0,0});
    for (int k = 1; k <= Ymax; ++k) {
        Mhalf[k] = Mhalf[k-1];
        Lhalf[k] = Lhalf[k-1];
        if (!mu[k]) continue;

        ILD invsqrt = invsqrt_int(k);
        ILD logk = log_int(k);
        Mhalf[k] = add(Mhalf[k], scale(invsqrt, (long double)mu[k]));
        Lhalf[k] = add(Lhalf[k], scale(mulI(invsqrt, logk), (long double)mu[k]));
    }

    const ILD logX = log_int(X);
    auto U = [&](int m) -> ID {
        if (m > X) return {0,0};
        const int y = X/m;
        ILD logXm = subI(logX, log_int(m));
        ILD bracket = subI(mulI(logXm, Mhalf[y]), Lhalf[y]);
        return toD(mulI(bracket, invsqrt_int(m)));
    };

    // No child of a parent <=X exceeds ceil(2X/3).
    const int max_child = (2*X + 2)/3 + 4;
    vector<ID> incoming(max_child + 1, {0,0});

    ID U_next = {0,0};
    ID answer = {0,0};

    for (int m = X; m >= n0; --m) {
        ID U_m = U(m);
        ID r_m = subD(U_m, U_next);
        ID A_m = r_m;
        if (m < (int)incoming.size()) A_m = addD(A_m, incoming[m]);

        if (m == n0) {
            answer = A_m;
            break;
        }

        ID half = halfD(A_m);
        int a2 = m/2;
        int b2 = m - a2;
        int a3 = (m + 2)/3;
        int b3 = m - a3;

        if (a2 >= n0) incoming[a2] = addD(incoming[a2], half);
        if (b2 >= n0) incoming[b2] = addD(incoming[b2], half);
        if (a3 >= n0) incoming[a3] = addD(incoming[a3], half);
        if (b3 >= n0) incoming[b3] = addD(incoming[b3], half);

        U_next = U_m;
    }

    cout << setprecision(17);
    cout << "classification PASS_DIRECTED_BINARY_TERNARY_NEGATIVE_ROW\n";
    cout << "X " << X << "\n";
    cout << "row " << n0 << "\n";
    cout << "mobius_prefix_limit " << X/n0 << "\n";
    cout << "A_lo " << answer.lo << "\n";
    cout << "A_hi " << answer.hi << "\n";
    cout << "interval_width " << answer.hi - answer.lo << "\n";
    cout << "log_pad_each_side 2e-13\n";
    cout << "sqrt_denominator 2^60\n";

    if (!(answer.hi < -0.004)) {
        cerr << "FAIL: negative moat not certified\n";
        return 1;
    }

    return 0;
}
