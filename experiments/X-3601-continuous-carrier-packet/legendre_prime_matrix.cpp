#include <quadmath.h>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

// EMPIRICAL discovery producer. Prime-power enumeration is exact integer work;
// logarithms, phases, overlap recurrence, accumulation, and output are ordinary
// finite-precision arithmetic and are not a sign certificate.

static std::vector<uint32_t> primes_up_to(uint64_t n) {
    std::vector<uint8_t> mark(n + 1, 1);
    mark[0] = 0;
    if (n >= 1) mark[1] = 0;
    for (uint64_t p = 2; p * p <= n; ++p)
        if (mark[p])
            for (uint64_t k = p * p; k <= n; k += p) mark[k] = 0;
    std::vector<uint32_t> primes;
    for (uint64_t p = 2; p <= n; ++p)
        if (mark[p]) primes.push_back(static_cast<uint32_t>(p));
    return primes;
}

// O(N^2) recurrence for the normalized shifted-Legendre overlap matrix.
static void overlap(int N, long double s, std::vector<long double> &K) {
    const long double a = 2 * s - 1;
    std::vector<long double> P(2 * N + 2);
    P[0] = 1;
    if (P.size() > 1) P[1] = a;
    for (int n = 1; n < static_cast<int>(P.size()) - 1; ++n)
        P[n + 1] = ((2 * n + 1) * a * P[n] - n * P[n - 1]) / (n + 1);

    std::vector<std::vector<long double>> rows(N + 1);
    rows[0].resize(2 * N + 1);
    rows[0][0] = 1 - a;
    for (int n = 1; n <= 2 * N; ++n)
        rows[0][n] = (P[n - 1] - P[n + 1]) / (2 * n + 1);

    for (int m = 0; m < N; ++m) {
        const int max_n = 2 * N - m - 1;
        rows[m + 1].resize(max_n + 1);
        for (int n = 0; n <= max_n; ++n) {
            const long double xp =
                ((n + 1) * rows[m][n + 1] + (n ? n * rows[m][n - 1] : 0)) /
                (2 * n + 1);
            const long double shifted = xp - 2 * s * rows[m][n];
            rows[m + 1][n] =
                ((2 * m + 1) * shifted - (m ? m * rows[m - 1][n] : 0)) /
                (m + 1);
        }
    }

    K.assign((N + 1) * (N + 1), 0);
    for (int m = 0; m <= N; ++m)
        for (int n = 0; n <= N; ++n) {
            const long double scale =
                sqrtl((2 * m + 1.0L) * (2 * n + 1.0L)) / 2;
            const long double direct = scale * rows[m][n];
            const long double transpose = scale * rows[n][m];
            const long double expected = ((m + n) & 1) ? -transpose : transpose;
            K[m * (N + 1) + n] = (direct + expected) / 2;
        }
}

int main(int argc, char **argv) {
    if (argc < 5) {
        std::cerr << "usage: cutoff carrier max_degree output\n";
        return 2;
    }
    const uint64_t cutoff = std::strtoull(argv[1], nullptr, 10);
    const std::string carrier_text = argv[2];
    const int N = std::atoi(argv[3]);
    const std::string output_path = argv[4];
    if (cutoff < 2 || N < 0) return 2;

    const auto primes = primes_up_to(cutoff);
    const int dimension = N + 1;
    std::vector<long double> S(dimension * dimension, 0);
    std::vector<long double> compensation(dimension * dimension, 0);
    std::vector<long double> K;

    const __float128 Tq = strtoflt128(carrier_text.c_str(), nullptr);
    const __float128 piq = acosq(-1);
    const __float128 two_piq = 2 * piq;
    const __float128 Lq = logq(static_cast<__float128>(cutoff));
    const long double pi = acosl(-1.0L);
    uint64_t term_count = 0;

    for (uint32_t p : primes) {
        uint64_t q = p;
        unsigned exponent = 1;
        const __float128 log_p = logq(static_cast<__float128>(p));
        while (q <= cutoff) {
            ++term_count;
            const __float128 log_q = exponent * log_p;
            const long double s = static_cast<long double>(log_q / Lq);
            overlap(N, s, K);
            const __float128 reduced = remainderq(Tq * log_q, two_piq);
            const long double phase = static_cast<long double>(reduced);
            const long double cosine = cosl(phase);
            const long double sine = sinl(phase);
            const long double amplitude =
                static_cast<long double>(log_p / (piq * sqrtq(static_cast<__float128>(q))));

            for (int m = 0; m < dimension; ++m)
                for (int n = m; n < dimension; ++n) {
                    const int difference = n - m;
                    long double phase_factor;
                    if (((m + n) & 1) == 0) {
                        phase_factor = ((difference / 2) & 1) ? -cosine : cosine;
                    } else {
                        phase_factor = (((difference - 1) / 2) & 1) ? -sine : sine;
                    }
                    const long double value =
                        amplitude * K[m * dimension + n] * phase_factor;
                    const int index = m * dimension + n;
                    const long double y = value - compensation[index];
                    const long double next = S[index] + y;
                    compensation[index] = (next - S[index]) - y;
                    S[index] = next;
                    if (n != m) {
                        S[n * dimension + m] = S[index];
                        compensation[n * dimension + m] = compensation[index];
                    }
                }
            if (q > cutoff / p) break;
            q *= p;
            ++exponent;
        }
    }

    const long double T = strtold(carrier_text.c_str(), nullptr);
    const long double alpha = logl(T / (2 * pi)) / (2 * pi);
    std::ofstream out(output_path);
    out << std::setprecision(18);
    out << "{\n\"schema\":\"riemann.legendre-carrier-leading-matrix.v1\",\n"
        << "\"status\":\"EMPIRICAL_NOT_CERTIFIED\",\n"
        << "\"cutoff\":" << cutoff << ",\"T\":\"" << carrier_text
        << "\",\"order\":" << N << ",\"dimension\":" << dimension
        << ",\"prime_power_terms\":" << term_count
        << ",\"alpha\":" << static_cast<double>(alpha) << ",\n"
        << "\"phase_backend\":\"GNU binary128 log/product/remainder; long-double sin/cos and compensated accumulation\",\n"
        << "\"matrix\":[\n";
    for (int m = 0; m < dimension; ++m) {
        out << "[";
        for (int n = 0; n < dimension; ++n) {
            if (n) out << ',';
            out << static_cast<double>(alpha * (m == n) - S[m * dimension + n]);
        }
        out << "]" << (m + 1 < dimension ? "," : "") << "\n";
    }
    out << "],\n\"warning\":\"Leading high-carrier matrix only; no directed rounding or exact archimedean/pole enclosure.\"\n}\n";
}
