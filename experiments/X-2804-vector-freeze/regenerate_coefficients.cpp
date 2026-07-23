#include <quadmath.h>
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Kahan {
    long double sum = 0;
    long double correction = 0;
    void add(long double value) {
        const long double y = value - correction;
        const long double next = sum + y;
        correction = (next - sum) - y;
        sum = next;
    }
};

static std::vector<uint32_t> simple_primes(uint64_t limit) {
    std::vector<uint8_t> mark(limit + 1, 1);
    mark[0] = 0;
    if (limit >= 1) mark[1] = 0;
    for (uint64_t prime = 2; prime * prime <= limit; ++prime) {
        if (mark[prime]) {
            for (uint64_t multiple = prime * prime; multiple <= limit; multiple += prime) {
                mark[multiple] = 0;
            }
        }
    }
    std::vector<uint32_t> primes;
    for (uint64_t value = 2; value <= limit; ++value) {
        if (mark[value]) primes.push_back(static_cast<uint32_t>(value));
    }
    return primes;
}

static uint64_t integer_sqrt(uint64_t value) {
    uint64_t root = static_cast<uint64_t>(std::sqrt(static_cast<long double>(value)));
    while ((root + 1) * (root + 1) <= value) ++root;
    while (root * root > value) --root;
    return root;
}

int main(int argc, char **argv) {
    if (argc < 8) {
        std::cerr
            << "usage: cutoff cells carrier segment_size start_segment "
            << "end_segment output [higher]\n";
        return 2;
    }
    const uint64_t cutoff = std::strtoull(argv[1], nullptr, 10);
    const int cells = std::atoi(argv[2]);
    const std::string carrier_text = argv[3];
    const uint64_t segment_size = std::strtoull(argv[4], nullptr, 10);
    const uint64_t start_segment = std::strtoull(argv[5], nullptr, 10);
    const uint64_t end_segment = std::strtoull(argv[6], nullptr, 10);
    const std::string output_path = argv[7];
    const bool include_higher = argc > 8 && std::string(argv[8]) == "higher";
    const uint64_t total_segments = (cutoff - 2) / segment_size + 1;
    if (!(cutoff >= 2 && cells >= 1 && segment_size >= 1
          && start_segment < end_segment && end_segment <= total_segments)) {
        return 3;
    }

    const auto base_primes = simple_primes(integer_sqrt(cutoff) + 1);
    std::vector<Kahan> real(cells), imag(cells);
    const __float128 pi = acosq(-1);
    const __float128 log_cutoff = logq(static_cast<__float128>(cutoff));
    const __float128 carrier = strtoflt128(carrier_text.c_str(), nullptr);
    const __float128 two_pi = 2 * pi;
    uint64_t prime_count = 0;
    uint64_t higher_count = 0;

    auto accumulate = [&](uint64_t q, uint64_t p, unsigned exponent) {
        const __float128 log_p = logq(static_cast<__float128>(p));
        const __float128 log_q = static_cast<__float128>(exponent) * log_p;
        const __float128 scaled = static_cast<__float128>(cells) * log_q / log_cutoff;
        const uint64_t lag = static_cast<uint64_t>(floorq(scaled));
        const __float128 fraction = scaled - lag;
        const __float128 amplitude = log_p / (pi * sqrtq(static_cast<__float128>(q)));
        const __float128 phase = remainderq(carrier * log_q, two_pi);
        const long double term_real = static_cast<long double>(amplitude * cosq(phase));
        const long double term_imag = -static_cast<long double>(amplitude * sinq(phase));
        if (lag < static_cast<uint64_t>(cells)) {
            real[lag].add(static_cast<long double>(1 - fraction) * term_real);
            imag[lag].add(static_cast<long double>(1 - fraction) * term_imag);
        }
        if (lag + 1 < static_cast<uint64_t>(cells)) {
            real[lag + 1].add(static_cast<long double>(fraction) * term_real);
            imag[lag + 1].add(static_cast<long double>(fraction) * term_imag);
        }
    };

    for (uint64_t segment = start_segment; segment < end_segment; ++segment) {
        const uint64_t low = 2 + segment * segment_size;
        const uint64_t high = std::min<uint64_t>(cutoff + 1, low + segment_size);
        std::vector<uint8_t> mark(high - low, 1);
        const uint64_t root = integer_sqrt(high - 1);
        for (uint32_t prime : base_primes) {
            if (prime > root) break;
            const uint64_t first = std::max<uint64_t>(
                static_cast<uint64_t>(prime) * prime,
                ((low + prime - 1) / prime) * prime
            );
            for (uint64_t multiple = first; multiple < high; multiple += prime) {
                mark[multiple - low] = 0;
            }
        }
        for (uint64_t offset = 0; offset < high - low; ++offset) {
            if (mark[offset]) {
                const uint64_t prime = low + offset;
                accumulate(prime, prime, 1);
                ++prime_count;
            }
        }
    }

    if (include_higher) {
        for (uint32_t prime : base_primes) {
            uint64_t q = static_cast<uint64_t>(prime) * prime;
            unsigned exponent = 2;
            while (q <= cutoff) {
                accumulate(q, prime, exponent);
                ++higher_count;
                if (q > cutoff / prime) break;
                q *= prime;
                ++exponent;
            }
        }
    }

    std::ofstream output(output_path);
    output << std::setprecision(21);
    output
        << "{\n"
        << "  \"schema\": \"riemann.carrier-piecewise-regenerated-shard.v1\",\n"
        << "  \"cutoff\": " << cutoff << ", \"K\": " << cells
        << ", \"T\": \"" << carrier_text << "\",\n"
        << "  \"segment_size\": " << segment_size
        << ", \"segment_start\": " << start_segment
        << ", \"segment_end\": " << end_segment << ",\n"
        << "  \"include_higher_powers\": "
        << (include_higher ? "true" : "false") << ",\n"
        << "  \"prime_count\": " << prime_count
        << ", \"higher_prime_power_count\": " << higher_count << ",\n"
        << "  \"phase_backend\": "
        << "\"GNU binary128 log/product/remainder/sin/cos; long-double Kahan accumulation\",\n"
        << "  \"real\": [";
    for (int index = 0; index < cells; ++index) {
        if (index) output << ',';
        output << static_cast<double>(real[index].sum);
    }
    output << "],\n  \"imag\": [";
    for (int index = 0; index < cells; ++index) {
        if (index) output << ',';
        output << static_cast<double>(imag[index].sum);
    }
    output << "]\n}\n";
}
