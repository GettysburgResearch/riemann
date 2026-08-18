#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

using std::int32_t;
using std::int64_t;

static const int PRIMES[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};

static void gen_divs_rec(int idx, int64_t value, int mu, int64_t cap,
                         std::vector<std::pair<int64_t,int>>& out) {
    if (idx == static_cast<int>(sizeof(PRIMES)/sizeof(PRIMES[0]))) {
        out.push_back({value, mu});
        return;
    }
    gen_divs_rec(idx + 1, value, mu, cap, out);
    const int p = PRIMES[idx];
    if (value <= cap / p) {
        gen_divs_rec(idx + 1, value * p, -mu, cap, out);
    }
}

static inline int qstar(int m) {
    if (m < 2) return 0;
    if (m == 2) return 15;
    if (m == 3) return 6;
    if (m == 4) return 3;
    return 6;
}

struct MinResult {
    double value = std::numeric_limits<double>::infinity();
    int x = -1;
};

static MinResult scan_margin(const std::vector<int32_t>& fcoef,
                             const std::vector<int32_t>& mcoef,
                             int af, int am, int start_x) {
    const int N = static_cast<int>(fcoef.size()) - 1;
    std::vector<double> S(N + 1, 0.0), T(N + 1, 0.0);
    for (int n = 1; n <= N; ++n) {
        const double c = static_cast<double>(af) * static_cast<double>(fcoef[n])
                       + static_cast<double>(am) * static_cast<double>(mcoef[n]);
        const double inv = 1.0 / std::sqrt(static_cast<double>(n));
        S[n] = S[n-1] + c * inv;
        T[n] = T[n-1] + c * inv * std::log(static_cast<double>(n));
    }
    const double log4 = std::log(4.0);
    MinResult result;
    for (int x = start_x; x <= N; ++x) {
        const int k = x / 4;
        const double lx = std::log(static_cast<double>(x));
        const double v = log4 * S[k] + lx * (S[x] - S[k]) - (T[x] - T[k]);
        if (v < result.value) {
            result.value = v;
            result.x = x;
        }
    }
    return result;
}

int main(int argc, char** argv) {
    const int N = argc > 1 ? std::atoi(argv[1]) : 5000000;
    if (N < 67) {
        std::cerr << "N must be at least 67\n";
        return 2;
    }

    std::vector<std::pair<int64_t,int>> divs;
    gen_divs_rec(0, 1, 1, N / 2, divs);
    std::sort(divs.begin(), divs.end());

    std::vector<int32_t> fcoef(N + 1, 0), mcoef(N + 1, 0);
    int64_t ops = 0;
    for (const auto& [d, mu] : divs) {
        const int maxm = static_cast<int>(N / d);
        for (int m = 2; m <= maxm; ++m) {
            const int n = static_cast<int>(d * static_cast<int64_t>(m));
            const int q = qstar(m);
            fcoef[n] += mu * q;
            mcoef[n] += q;
            ++ops;
        }
    }

    int32_t max_abs_f = 0, max_m = 0;
    for (int n = 1; n <= N; ++n) {
        max_abs_f = std::max<int32_t>(max_abs_f, std::abs(fcoef[n]));
        max_m = std::max(max_m, mcoef[n]);
    }

    const MinResult lower = scan_margin(fcoef, mcoef, 42, -1, 67); // 42F-M
    const MinResult upper = scan_margin(fcoef, mcoef, -20, 1, 67); // M-20F

    std::cout << std::setprecision(17);
    std::cout << "schema=riemann.p61-bias-diagnostic.v2\n";
    std::cout << "N=" << N << "\n";
    std::cout << "divisors_generated_safely=" << divs.size() << "\n";
    std::cout << "coefficient_updates=" << ops << "\n";
    std::cout << "max_abs_signed_coefficient=" << max_abs_f << "\n";
    std::cout << "max_unsigned_coefficient=" << max_m << "\n";
    std::cout << "minimum_42F_minus_M=" << lower.value << "\n";
    std::cout << "argmin_42F_minus_M=" << lower.x << "\n";
    std::cout << "minimum_M_minus_20F=" << upper.value << "\n";
    std::cout << "argmin_M_minus_20F=" << upper.x << "\n";
    std::cout << "continuum_reduction=diagnostic_integer_knots; margins are affine in log(x) between consecutive integer knots\n";
    std::cout << "classification=diagnostic floating-point scan, not directed proof\n";
    return 0;
}
