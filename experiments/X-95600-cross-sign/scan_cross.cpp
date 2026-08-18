#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

namespace {
constexpr int BANDS = 10;
constexpr int KMAX = 3;
constexpr int SMIN = 2;
constexpr int SMAX = 6;
constexpr long double LOG2L = 0.693147180559945309417232121458176568L;

struct BandState {
    long double mu_pow[4]{};      // k=1..3: sum mu*n^(k-1/2)
    long double mu_log_pow[4]{};  // k=1..3: sum mu*log(n)*n^(k-1/2)
    long double raw[6][3]{};      // p=1..5, q=0..2: sum n^p log(n)^q
};

struct Coeffs {
    long double a[BANDS][4]{};
    long double b[BANDS][4]{};
    long double d[BANDS][7][3]{}; // s=2..6, q=0..2
};

std::vector<int8_t> mobius_sieve(int n) {
    std::vector<int8_t> mu(n + 1, 0);
    std::vector<int> primes;
    std::vector<uint8_t> composite(n + 1, 0);
    mu[1] = 1;
    primes.reserve(n / 10);
    for (int i = 2; i <= n; ++i) {
        if (!composite[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            long long v = 1LL * i * p;
            if (v > n) break;
            composite[(int)v] = 1;
            if (i % p == 0) {
                mu[(int)v] = 0;
                break;
            }
            mu[(int)v] = -mu[i];
        }
    }
    return mu;
}

Coeffs make_coeffs() {
    const long double A[6] = {1, 1, -8, -8, 16, 16};
    const long double B[6] = {0, -1, -8, 0, 32, 16};
    const long double Q[4] = {1, -7.0L/8.0L, 7.0L/32.0L, -1.0L/64.0L};
    const long double low[4] = {0, 5, -63, 170};
    const long double high[4] = {0, -1.0L/3.0L, 1, -2.0L/3.0L};
    Coeffs out;
    auto build = [&](const long double src[6], long double dest[BANDS][4]) {
        for (int j = 0; j < BANDS; ++j) {
            for (int h = 0; h < 4; ++h) {
                for (int r = 0; r < 6; ++r) {
                    if (src[r] == 0) continue;
                    int t = r + h;
                    const long double* branch = nullptr;
                    if (t <= j - 2) branch = low;
                    else if (t == j - 1 || t == j) branch = high;
                    else continue;
                    long double pref = Q[h] * src[r] * std::pow(2.0L, -0.5L * r);
                    for (int k = 1; k <= 3; ++k) {
                        dest[j][k] += pref * branch[k] * std::pow(2.0L, (long double)t * k);
                    }
                }
            }
        }
    };
    build(A, out.a);
    build(B, out.b);
    for (int j = 0; j < BANDS; ++j) {
        for (int k = 1; k <= 3; ++k) {
            for (int l = 1; l <= 3; ++l) {
                int s = k + l;
                out.d[j][s][2] += out.a[j][k] * out.a[j][l];
                out.d[j][s][1] += LOG2L * (out.a[j][k] * out.b[j][l] + out.b[j][k] * out.a[j][l]);
                out.d[j][s][0] += LOG2L * LOG2L * out.b[j][k] * out.b[j][l];
            }
        }
    }
    return out;
}

void update(BandState& st, int n, int sign, const std::vector<int8_t>& mu,
            const std::vector<double>& logs, const std::vector<double>& sqrts) {
    if (n <= 0 || (n & 1) == 0 || mu[n] == 0) return;
    const long double sgn = (long double)sign;
    const long double muv = (long double)mu[n];
    const long double x = (long double)n;
    const long double logx = (long double)logs[n];
    const long double sqrtx = (long double)sqrts[n];
    long double nkmh = sqrtx; // n^(1-1/2)
    for (int k = 1; k <= 3; ++k) {
        st.mu_pow[k] += sgn * muv * nkmh;
        st.mu_log_pow[k] += sgn * muv * logx * nkmh;
        nkmh *= x;
    }
    long double np = x;
    const long double log2x = logx * logx;
    for (int p = 1; p <= 5; ++p) {
        st.raw[p][0] += sgn * np;
        st.raw[p][1] += sgn * np * logx;
        st.raw[p][2] += sgn * np * log2x;
        np *= x;
    }
}

struct Point { int X{}; long double A{}; long double D{}; long double cross{}; };

std::string ld_json(long double x) {
    if (!std::isfinite((double)x)) return "null";
    std::ostringstream oss;
    oss << std::setprecision(18) << (double)x;
    return oss.str();
}

} // namespace

int main(int argc, char** argv) {
    int N = 5000000;
    std::string output;
    if (argc >= 2) N = std::atoi(argv[1]);
    if (argc >= 3) output = argv[2];
    if (N < 2) return 2;

    auto mu = mobius_sieve(N);
    std::vector<double> logs(N + 1, 0.0), sqrts(N + 1, 0.0);
    for (int n = 1; n <= N; ++n) {
        logs[n] = std::log((double)n);
        sqrts[n] = std::sqrt((double)n);
    }
    Coeffs coeff = make_coeffs();
    std::array<BandState, BANDS> bands{};

    long long positive_count = 0;
    int last_positive = 0;
    int first_all_negative_candidate = 1;
    long double max_positive = -std::numeric_limits<long double>::infinity();
    int max_positive_X = 0;
    long double max_abs_A = -1;
    int max_abs_A_X = 0;
    Point max_positive_point{}, max_abs_point{};
    std::vector<int> requested = {92, 105, 106, 256, 368, 1000, 10000, 100000, 1000000, N};
    std::sort(requested.begin(), requested.end());
    requested.erase(std::unique(requested.begin(), requested.end()), requested.end());
    std::vector<Point> samples;

    for (int X = 1; X <= N; ++X) {
        int prev = X - 1;
        for (int j = 0; j < BANDS; ++j) {
            int hi_new = X >> j;
            int hi_old = prev >> j;
            if (hi_new > hi_old) update(bands[j], hi_new, +1, mu, logs, sqrts);
            int lo_new = X >> (j + 1);
            int lo_old = prev >> (j + 1);
            if (lo_new > lo_old) update(bands[j], lo_new, -1, mu, logs, sqrts);
        }
        if (X < 2) continue;
        long double invpow[7]{};
        invpow[0] = 1;
        long double invX = 1.0L / (long double)X;
        for (int k = 1; k <= 6; ++k) invpow[k] = invpow[k-1] * invX;
        long double Aval = 0, Dval = 0;
        for (int j = 0; j < BANDS; ++j) {
            for (int k = 1; k <= 3; ++k) {
                Aval += invpow[k] * (coeff.a[j][k] * bands[j].mu_log_pow[k]
                                     + LOG2L * coeff.b[j][k] * bands[j].mu_pow[k]);
            }
            for (int s = SMIN; s <= SMAX; ++s) {
                int p = s - 1;
                Dval += invpow[s] * (coeff.d[j][s][2] * bands[j].raw[p][2]
                                      + coeff.d[j][s][1] * bands[j].raw[p][1]
                                      + coeff.d[j][s][0] * bands[j].raw[p][0]);
            }
        }
        long double cross = Aval * Aval - Dval;
        Point pt{X, Aval, Dval, cross};
        if (X >= 16 && cross > 0) {
            ++positive_count;
            last_positive = X;
            if (cross > max_positive) {
                max_positive = cross;
                max_positive_X = X;
                max_positive_point = pt;
            }
        }
        if (fabsl(Aval) > max_abs_A) {
            max_abs_A = fabsl(Aval);
            max_abs_A_X = X;
            max_abs_point = pt;
        }
        if (std::binary_search(requested.begin(), requested.end(), X)) samples.push_back(pt);
    }

    int negative_from = last_positive + 1;
    std::ostream* osp = &std::cout;
    std::ofstream ofs;
    if (!output.empty()) { ofs.open(output); osp = &ofs; }
    std::ostream& os = *osp;
    os << "{\n";
    os << "  \"schema\": \"riemann.q4.95600.cross-sign-scan.v1\",\n";
    os << "  \"arithmetic_class\": \"FLOATING_DISCOVERY_ONLY\",\n";
    os << "  \"scan_limit\": " << N << ",\n";
    os << "  \"positive_off_diagonal_endpoints\": " << positive_count << ",\n";
    os << "  \"last_positive_endpoint\": " << last_positive << ",\n";
    os << "  \"negative_for_every_scanned_endpoint_from\": " << negative_from << ",\n";
    os << "  \"largest_positive_cross\": {\"X\": " << max_positive_X
       << ", \"annular_sum\": " << ld_json(max_positive_point.A)
       << ", \"diagonal\": " << ld_json(max_positive_point.D)
       << ", \"cross\": " << ld_json(max_positive_point.cross) << "},\n";
    os << "  \"largest_absolute_annular_sum\": {\"X\": " << max_abs_A_X
       << ", \"annular_sum\": " << ld_json(max_abs_point.A)
       << ", \"diagonal\": " << ld_json(max_abs_point.D)
       << ", \"cross\": " << ld_json(max_abs_point.cross) << "},\n";
    os << "  \"samples\": [\n";
    for (size_t i = 0; i < samples.size(); ++i) {
        const auto& p = samples[i];
        os << "    {\"X\": " << p.X << ", \"annular_sum\": " << ld_json(p.A)
           << ", \"diagonal\": " << ld_json(p.D) << ", \"cross\": " << ld_json(p.cross) << "}";
        os << (i + 1 == samples.size() ? "\n" : ",\n");
    }
    os << "  ],\n";
    os << "  \"does_not_prove\": [\"eventual cross sign\", \"UOSACF\", \"Riemann Hypothesis\"]\n";
    os << "}\n";
    return 0;
}
