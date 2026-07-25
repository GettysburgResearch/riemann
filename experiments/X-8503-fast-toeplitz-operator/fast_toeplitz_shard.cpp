#define MPFR_WANT_FLOAT128 1

#include <mpfr.h>
#include <gmp.h>
#include <quadmath.h>

#include <algorithm>
#include <cfenv>
#include <cfloat>
#include <cmath>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#pragma STDC FENV_ACCESS ON

namespace {

constexpr const char *SCHEMA =
    "riemann.piecewise-carrier-fast-toeplitz-midpoint-shard.v1";
constexpr const char *ARITHMETIC_CONTRACT =
    "x86 binary80 nearest basic arithmetic; binary128 segment-relative phase; "
    "MPFR setup; M=32768 R=3; two-hat coefficient deposits; balanced pairwise "
    "summation; zero guarded support-boundary events";

struct MpfrNumber {
    mpfr_t value;
    explicit MpfrNumber(mpfr_prec_t precision) { mpfr_init2(value, precision); }
    ~MpfrNumber() { mpfr_clear(value); }
    MpfrNumber(const MpfrNumber &) = delete;
    MpfrNumber &operator=(const MpfrNumber &) = delete;
};

struct Manifest {
    int cells = 0;
    int vector_bits = 0;
    int autocorrelation_bits = 0;
    int cutoff_power10 = 0;
    std::uint64_t cutoff = 0;
    std::uint64_t segment_size = 0;
    std::uint64_t total_segments = 0;
    std::string vector_sha256;
    std::string normalization_sha256;
    std::string parameter_sha256;
    std::string carrier_numerator;
    std::string carrier_denominator;
};

Manifest read_manifest(const std::string &path) {
    std::ifstream input(path);
    if (!input) {
        throw std::runtime_error("cannot open manifest: " + path);
    }
    std::string magic;
    input >> magic;
    if (magic != "RIEMANN_D0801_AUTOCORRELATION_V1") {
        throw std::runtime_error("bad manifest magic");
    }

    Manifest manifest;
    std::string key;
    int declared_autocorrelations = -1;
    int seen_autocorrelations = 0;
    while (input >> key) {
        if (key == "cells") {
            input >> manifest.cells;
        } else if (key == "vector_scale_bits") {
            input >> manifest.vector_bits;
        } else if (key == "autocorr_scale_bits") {
            input >> manifest.autocorrelation_bits;
        } else if (key == "vector_sha256") {
            input >> manifest.vector_sha256;
        } else if (key == "normalization_sha256") {
            input >> manifest.normalization_sha256;
        } else if (key == "parameter_sha256") {
            input >> manifest.parameter_sha256;
        } else if (key == "cutoff_power10") {
            input >> manifest.cutoff_power10;
        } else if (key == "cutoff") {
            input >> manifest.cutoff;
        } else if (key == "carrier_num") {
            input >> manifest.carrier_numerator;
        } else if (key == "carrier_den") {
            input >> manifest.carrier_denominator;
        } else if (key == "segment_size") {
            input >> manifest.segment_size;
        } else if (key == "total_segments") {
            input >> manifest.total_segments;
        } else if (key == "a_count") {
            input >> declared_autocorrelations;
        } else if (key == "a") {
            int index = -1;
            std::string real_part;
            std::string imaginary_part;
            input >> index >> real_part >> imaginary_part;
            if (index != seen_autocorrelations) {
                throw std::runtime_error("autocorrelation manifest is not ordered");
            }
            ++seen_autocorrelations;
        } else {
            throw std::runtime_error("unknown manifest key: " + key);
        }
    }

    if (manifest.cells < 1 || manifest.cutoff < 2 ||
        manifest.segment_size < 1 || manifest.carrier_denominator == "0") {
        throw std::runtime_error("incomplete manifest");
    }
    if (declared_autocorrelations != manifest.cells + 1 ||
        seen_autocorrelations != declared_autocorrelations) {
        throw std::runtime_error("autocorrelation manifest length mismatch");
    }

    std::uint64_t power10 = 1;
    for (int i = 0; i < manifest.cutoff_power10; ++i) {
        if (power10 > std::numeric_limits<std::uint64_t>::max() / 10) {
            throw std::runtime_error("cutoff power overflow");
        }
        power10 *= 10;
    }
    if (power10 != manifest.cutoff) {
        throw std::runtime_error("cutoff and cutoff_power10 mismatch");
    }
    const std::uint64_t expected_segments =
        (manifest.cutoff - 2) / manifest.segment_size + 1;
    if (expected_segments != manifest.total_segments) {
        throw std::runtime_error("segment count mismatch");
    }
    return manifest;
}

std::vector<std::uint32_t> simple_primes(std::uint64_t limit) {
    std::vector<std::uint8_t> sieve(limit + 1, 1);
    if (!sieve.empty()) {
        sieve[0] = 0;
    }
    if (limit >= 1) {
        sieve[1] = 0;
    }
    for (std::uint64_t p = 2; p * p <= limit; ++p) {
        if (sieve[p]) {
            for (std::uint64_t multiple = p * p; multiple <= limit;
                 multiple += p) {
                sieve[multiple] = 0;
            }
        }
    }
    std::vector<std::uint32_t> primes;
    for (std::uint64_t value = 2; value <= limit; ++value) {
        if (sieve[value]) {
            primes.push_back(static_cast<std::uint32_t>(value));
        }
    }
    return primes;
}

std::vector<std::uint64_t> segment_primes(
    std::uint64_t low,
    std::uint64_t high,
    const std::vector<std::uint32_t> &base_primes) {
    if (!(2 <= low && low < high)) {
        throw std::runtime_error("invalid prime segment");
    }
    std::vector<std::uint8_t> sieve(high - low, 1);
    std::uint64_t root = static_cast<std::uint64_t>(
        std::sqrt(static_cast<long double>(high - 1)));
    while ((root + 1) * (root + 1) <= high - 1) {
        ++root;
    }
    while (root * root > high - 1) {
        --root;
    }
    for (std::uint32_t p32 : base_primes) {
        const std::uint64_t p = p32;
        if (p > root) {
            break;
        }
        const std::uint64_t first_multiple = ((low + p - 1) / p) * p;
        std::uint64_t start = std::max<std::uint64_t>(p * p, first_multiple);
        for (std::uint64_t value = start; value < high; value += p) {
            sieve[value - low] = 0;
        }
    }
    std::vector<std::uint64_t> primes;
    for (std::uint64_t offset = 0; offset < high - low; ++offset) {
        if (sieve[offset] && low + offset >= 2) {
            primes.push_back(low + offset);
        }
    }
    return primes;
}

struct PairwiseAccumulator {
    long double values[64]{};
    bool occupied[64]{};
    std::uint64_t count = 0;

    void add(long double value) {
        ++count;
        for (int level = 0; level < 64; ++level) {
            if (!occupied[level]) {
                values[level] = value;
                occupied[level] = true;
                return;
            }
            value += values[level];
            occupied[level] = false;
        }
        throw std::runtime_error("pairwise accumulator overflow");
    }

    long double finish() const {
        long double result = 0;
        for (int level = 0; level < 64; ++level) {
            if (occupied[level]) {
                result += values[level];
            }
        }
        return result;
    }
};

std::string mpz_string(const mpz_t value) {
    char *raw = mpz_get_str(nullptr, 10, value);
    if (!raw) {
        throw std::runtime_error("mpz_get_str failed");
    }
    std::string result(raw);
    void (*free_function)(void *, std::size_t) = nullptr;
    mp_get_memory_functions(nullptr, nullptr, &free_function);
    free_function(raw, result.size() + 1);
    return result;
}

std::pair<std::string, std::string> exact_long_double(long double value) {
    mpfr_t temporary;
    mpfr_init2(temporary, LDBL_MANT_DIG);
    mpfr_set_ld(temporary, value, MPFR_RNDN);
    mpz_t numerator;
    mpz_t denominator;
    mpz_init(numerator);
    mpz_init_set_ui(denominator, 1);
    const mpfr_exp_t exponent = mpfr_get_z_2exp(numerator, temporary);
    if (exponent >= 0) {
        mpz_mul_2exp(numerator, numerator, exponent);
    } else {
        mpz_mul_2exp(denominator, denominator, -exponent);
    }
    const auto result =
        std::make_pair(mpz_string(numerator), mpz_string(denominator));
    mpz_clear(numerator);
    mpz_clear(denominator);
    mpfr_clear(temporary);
    return result;
}

struct SegmentSetup {
    std::uint64_t midpoint = 0;
    long double log_midpoint = 0;
    long double inverse_sqrt_midpoint = 0;
    long long phase_grid_index = 0;
    __float128 phase_residual = 0;
};

struct Deposit {
    long index = -1;
    long double fraction = 0;
    long double amplitude = 0;
    long double phase_real = 0;
    long double phase_imaginary = 0;
};

class FastToeplitzEvaluator {
  public:
    FastToeplitzEvaluator(
        const Manifest &manifest,
        mpfr_prec_t setup_precision,
        int phase_grid)
        : manifest_(manifest),
          precision_(setup_precision),
          cells_(manifest.cells),
          phase_grid_(phase_grid),
          root_real_(phase_grid),
          root_imaginary_(phase_grid) {
        if (FLT_RADIX != 2 || LDBL_MANT_DIG != 64 ||
            sizeof(long double) != 16) {
            throw std::runtime_error(
                "requires x86 binary80 long double ABI");
        }
        if (fegetround() != FE_TONEAREST) {
            throw std::runtime_error("requires FE_TONEAREST");
        }
        if (phase_grid_ < 2 || phase_grid_ % 2 != 0) {
            throw std::runtime_error("phase grid must be positive and even");
        }

        MpfrNumber x(precision_);
        MpfrNumber y(precision_);
        MpfrNumber z(precision_);

        mpfr_const_pi(x.value, MPFR_RNDN);
        pi_long_double_ = mpfr_get_ld(x.value, MPFR_RNDN);
        pi_float128_ = mpfr_get_float128(x.value, MPFR_RNDN);

        mpfr_set_ui(x.value, manifest_.cutoff, MPFR_RNDN);
        mpfr_log(x.value, x.value, MPFR_RNDN);
        log_cutoff_ = mpfr_get_ld(x.value, MPFR_RNDN);

        mpz_t numerator;
        mpz_t denominator;
        mpz_init(numerator);
        mpz_init(denominator);
        if (mpz_set_str(
                numerator,
                manifest_.carrier_numerator.c_str(),
                10) != 0 ||
            mpz_set_str(
                denominator,
                manifest_.carrier_denominator.c_str(),
                10) != 0) {
            mpz_clear(numerator);
            mpz_clear(denominator);
            throw std::runtime_error("invalid carrier rational");
        }
        mpfr_set_z(x.value, numerator, MPFR_RNDN);
        mpfr_set_z(y.value, denominator, MPFR_RNDN);
        mpfr_div(x.value, x.value, y.value, MPFR_RNDN);
        carrier_float128_ = mpfr_get_float128(x.value, MPFR_RNDN);
        mpz_clear(numerator);
        mpz_clear(denominator);

        for (int index = 0; index < phase_grid_; ++index) {
            mpfr_const_pi(x.value, MPFR_RNDN);
            mpfr_mul_ui(
                x.value,
                x.value,
                2UL * static_cast<unsigned long>(index),
                MPFR_RNDN);
            mpfr_div_ui(
                x.value,
                x.value,
                static_cast<unsigned long>(phase_grid_),
                MPFR_RNDN);
            mpfr_sin_cos(y.value, z.value, x.value, MPFR_RNDN);
            root_real_[index] = mpfr_get_ld(z.value, MPFR_RNDN);
            root_imaginary_[index] = -mpfr_get_ld(y.value, MPFR_RNDN);
        }

        base_primes_ = simple_primes(
            static_cast<std::uint64_t>(
                std::sqrt(static_cast<long double>(manifest_.cutoff))) +
            1);
    }

    SegmentSetup setup_segment(std::uint64_t low, std::uint64_t high) const {
        SegmentSetup setup;
        setup.midpoint = low + (high - low) / 2;

        MpfrNumber midpoint(precision_);
        MpfrNumber logarithm(precision_);
        MpfrNumber square_root(precision_);
        MpfrNumber carrier(precision_);
        MpfrNumber pi(precision_);
        MpfrNumber scaled(precision_);

        mpfr_set_ui(midpoint.value, setup.midpoint, MPFR_RNDN);
        mpfr_log(logarithm.value, midpoint.value, MPFR_RNDN);
        setup.log_midpoint = mpfr_get_ld(logarithm.value, MPFR_RNDN);

        mpfr_sqrt(square_root.value, midpoint.value, MPFR_RNDN);
        mpfr_ui_div(square_root.value, 1, square_root.value, MPFR_RNDN);
        setup.inverse_sqrt_midpoint =
            mpfr_get_ld(square_root.value, MPFR_RNDN);

        mpfr_set_float128(carrier.value, carrier_float128_, MPFR_RNDN);
        mpfr_mul(logarithm.value, carrier.value, logarithm.value, MPFR_RNDN);
        mpfr_const_pi(pi.value, MPFR_RNDN);
        mpfr_mul_ui(
            scaled.value,
            logarithm.value,
            static_cast<unsigned long>(phase_grid_),
            MPFR_RNDN);
        mpfr_mul_ui(pi.value, pi.value, 2, MPFR_RNDN);
        mpfr_div(scaled.value, scaled.value, pi.value, MPFR_RNDN);
        setup.phase_grid_index = mpfr_get_si(scaled.value, MPFR_RNDN);

        mpfr_const_pi(pi.value, MPFR_RNDN);
        mpfr_mul_si(
            pi.value,
            pi.value,
            2 * setup.phase_grid_index,
            MPFR_RNDN);
        mpfr_div_ui(
            pi.value,
            pi.value,
            static_cast<unsigned long>(phase_grid_),
            MPFR_RNDN);
        mpfr_sub(logarithm.value, logarithm.value, pi.value, MPFR_RNDN);
        setup.phase_residual =
            mpfr_get_float128(logarithm.value, MPFR_RNDN);
        return setup;
    }

    Deposit evaluate(std::uint64_t q, const SegmentSetup &setup) {
        Deposit deposit;

        const long double z =
            static_cast<long double>(
                static_cast<std::int64_t>(q) -
                static_cast<std::int64_t>(setup.midpoint)) /
            static_cast<long double>(q + setup.midpoint);
        const long double z_squared = z * z;
        long double power = z;
        long double log_increment = 0;
        for (int order = 0; order < 4; ++order) {
            log_increment += 2 * power / (2 * order + 1);
            power *= z_squared;
        }
        const long double log_q = setup.log_midpoint + log_increment;

        const long double y =
            static_cast<long double>(
                static_cast<std::int64_t>(q) -
                static_cast<std::int64_t>(setup.midpoint)) /
            static_cast<long double>(setup.midpoint);
        const long double coefficients[5] = {
            -0.5L,
            3.0L / 8,
            -5.0L / 16,
            35.0L / 128,
            -63.0L / 256,
        };
        long double y_power = 1;
        long double inverse_sqrt_polynomial = 1;
        for (long double coefficient : coefficients) {
            y_power *= y;
            inverse_sqrt_polynomial += coefficient * y_power;
        }
        const long double inverse_sqrt_q =
            setup.inverse_sqrt_midpoint * inverse_sqrt_polynomial;
        deposit.amplitude =
            log_q * inverse_sqrt_q / pi_long_double_;

        const long double support =
            static_cast<long double>(cells_) * log_q / log_cutoff_;
        deposit.index = static_cast<long>(std::floor(support));
        deposit.fraction = support - deposit.index;
        if (deposit.index < 0 || deposit.index >= cells_) {
            return deposit;
        }

        const long double support_boundary = std::min(
            std::fabs(deposit.fraction),
            std::fabs(1 - deposit.fraction));
        minimum_support_boundary_ =
            std::min(minimum_support_boundary_, support_boundary);
        if (support_boundary < std::ldexp(1.0L, -35)) {
            ++guarded_support_boundaries_;
        }

        const __float128 z128 =
            static_cast<__float128>(
                static_cast<std::int64_t>(q) -
                static_cast<std::int64_t>(setup.midpoint)) /
            static_cast<__float128>(q + setup.midpoint);
        const __float128 z128_squared = z128 * z128;
        __float128 power128 = z128;
        __float128 log_increment128 = 0;
        for (int order = 0; order < 4; ++order) {
            log_increment128 +=
                2 * power128 / static_cast<__float128>(2 * order + 1);
            power128 *= z128_squared;
        }
        const __float128 total_residual =
            setup.phase_residual + carrier_float128_ * log_increment128;
        const __float128 scaled_residual =
            static_cast<__float128>(phase_grid_) * total_residual /
            (2 * pi_float128_);
        const long long relative_index = llroundq(scaled_residual);
        const __float128 delta128 =
            total_residual -
            2 * pi_float128_ * static_cast<__float128>(relative_index) /
                static_cast<__float128>(phase_grid_);

        const long double phase_boundary = static_cast<long double>(
            pi_float128_ / static_cast<__float128>(phase_grid_) -
            fabsq(delta128));
        minimum_phase_boundary_ =
            std::min(minimum_phase_boundary_, phase_boundary);
        if (phase_boundary < std::ldexp(1.0L, -55)) {
            ++near_phase_boundaries_;
        }

        const long double delta = static_cast<long double>(delta128);
        const long double delta_squared = delta * delta;
        const long double taylor_real = 1 - delta_squared / 2;
        const long double taylor_imaginary =
            -delta + delta_squared * delta / 6;

        int root_index = static_cast<int>(
            (setup.phase_grid_index + relative_index) % phase_grid_);
        if (root_index < 0) {
            root_index += phase_grid_;
        }
        deposit.phase_real =
            root_real_[root_index] * taylor_real -
            root_imaginary_[root_index] * taylor_imaginary;
        deposit.phase_imaginary =
            root_real_[root_index] * taylor_imaginary +
            root_imaginary_[root_index] * taylor_real;
        return deposit;
    }

    const std::vector<std::uint32_t> &base_primes() const {
        return base_primes_;
    }

    std::uint64_t guarded_support_boundaries() const {
        return guarded_support_boundaries_;
    }

    std::uint64_t near_phase_boundaries() const {
        return near_phase_boundaries_;
    }

    long double minimum_support_boundary() const {
        return minimum_support_boundary_;
    }

    long double minimum_phase_boundary() const {
        return minimum_phase_boundary_;
    }

  private:
    const Manifest &manifest_;
    mpfr_prec_t precision_;
    int cells_;
    int phase_grid_;
    long double pi_long_double_ = 0;
    long double log_cutoff_ = 0;
    __float128 pi_float128_ = 0;
    __float128 carrier_float128_ = 0;
    std::vector<long double> root_real_;
    std::vector<long double> root_imaginary_;
    std::vector<std::uint32_t> base_primes_;
    std::uint64_t guarded_support_boundaries_ = 0;
    std::uint64_t near_phase_boundaries_ = 0;
    long double minimum_support_boundary_ = 1;
    long double minimum_phase_boundary_ = 1;
};

std::map<std::string, std::string> parse_options(int argc, char **argv) {
    std::map<std::string, std::string> options;
    for (int index = 1; index < argc; ++index) {
        const std::string argument = argv[index];
        if (argument.rfind("--", 0) != 0 || index + 1 >= argc) {
            throw std::runtime_error("bad argument: " + argument);
        }
        options[argument] = argv[++index];
    }
    return options;
}

std::string require_option(
    const std::map<std::string, std::string> &options,
    const std::string &name) {
    const auto found = options.find(name);
    if (found == options.end()) {
        throw std::runtime_error("missing option " + name);
    }
    return found->second;
}

}  // namespace

int main(int argc, char **argv) {
    try {
        const auto options = parse_options(argc, argv);
        const Manifest manifest =
            read_manifest(require_option(options, "--manifest"));
        const std::uint64_t start_segment =
            std::stoull(require_option(options, "--start-segment"));
        const std::uint64_t end_segment =
            std::stoull(require_option(options, "--end-segment"));
        const std::string output_path =
            require_option(options, "--output");
        const int phase_grid =
            options.count("--phase-grid")
                ? std::stoi(options.at("--phase-grid"))
                : 32768;
        const mpfr_prec_t setup_precision =
            options.count("--setup-precision")
                ? std::stol(options.at("--setup-precision"))
                : 192;

        if (!(2000 <= start_segment && start_segment < end_segment &&
              end_segment <= manifest.total_segments)) {
            throw std::runtime_error(
                "fast coefficient range must lie in [2000,total_segments)");
        }
        if (phase_grid != 32768) {
            throw std::runtime_error("L-8505 requires phase grid M=32768");
        }
        if (setup_precision < 128) {
            throw std::runtime_error("setup precision must be at least 128 bits");
        }
        if (fesetround(FE_TONEAREST) != 0) {
            throw std::runtime_error("could not set FE_TONEAREST");
        }

        FastToeplitzEvaluator evaluator(
            manifest,
            setup_precision,
            phase_grid);
        std::vector<PairwiseAccumulator> real_accumulators(manifest.cells);
        std::vector<PairwiseAccumulator> imaginary_accumulators(manifest.cells);
        PairwiseAccumulator absolute_amplitude_accumulator;
        std::uint64_t prime_count = 0;

        for (std::uint64_t segment_index = start_segment;
             segment_index < end_segment;
             ++segment_index) {
            const std::uint64_t low =
                2 + segment_index * manifest.segment_size;
            const std::uint64_t high = std::min<std::uint64_t>(
                manifest.cutoff + 1,
                low + manifest.segment_size);
            const SegmentSetup setup = evaluator.setup_segment(low, high);
            const auto primes =
                segment_primes(low, high, evaluator.base_primes());
            for (std::uint64_t q : primes) {
                const Deposit deposit = evaluator.evaluate(q, setup);
                if (deposit.index < 0 || deposit.index >= manifest.cells) {
                    continue;
                }
                const long double coefficient_real =
                    deposit.amplitude * deposit.phase_real;
                const long double coefficient_imaginary =
                    deposit.amplitude * deposit.phase_imaginary;
                const long double left_weight = 1 - deposit.fraction;
                real_accumulators[deposit.index].add(
                    left_weight * coefficient_real);
                imaginary_accumulators[deposit.index].add(
                    left_weight * coefficient_imaginary);
                if (deposit.index + 1 < manifest.cells) {
                    real_accumulators[deposit.index + 1].add(
                        deposit.fraction * coefficient_real);
                    imaginary_accumulators[deposit.index + 1].add(
                        deposit.fraction * coefficient_imaginary);
                }
                absolute_amplitude_accumulator.add(
                    std::fabs(deposit.amplitude));
            }
            prime_count += primes.size();
            std::cerr << "segment=" << segment_index
                      << " primes=" << prime_count << '\n';
        }

        if (evaluator.guarded_support_boundaries() != 0) {
            throw std::runtime_error(
                "guarded support boundary encountered; directed fallback required");
        }

        std::ofstream output(output_path);
        if (!output) {
            throw std::runtime_error("cannot open output path");
        }
        output << "{\n";
        output << "  \"schema\": \"" << SCHEMA << "\",\n";
        output << "  \"segment_start\": " << start_segment << ",\n";
        output << "  \"segment_end\": " << end_segment << ",\n";
        output << "  \"prime_count\": " << prime_count << ",\n";
        output << "  \"higher_prime_power_count\": 0,\n";
        output << "  \"total_terms\": " << prime_count << ",\n";
        output << "  \"include_higher_powers\": false,\n";
        output << "  \"vector_independent\": true,\n";
        output << "  \"source_manifest_vector_sha256\": \""
               << manifest.vector_sha256 << "\",\n";
        output << "  \"parameter_sha256\": \""
               << manifest.parameter_sha256 << "\",\n";
        output << "  \"normalization_sha256\": \""
               << manifest.normalization_sha256 << "\",\n";
        output << "  \"phase_grid_M\": " << phase_grid << ",\n";
        output << "  \"phase_taylor_R\": 3,\n";
        output << "  \"log_series_terms\": 4,\n";
        output << "  \"sqrt_polynomial_degree\": 5,\n";
        output << "  \"setup_precision_bits\": "
               << setup_precision << ",\n";
        output << "  \"mpfr_version\": \""
               << mpfr_get_version() << "\",\n";
        output << "  \"arithmetic_contract\": \""
               << ARITHMETIC_CONTRACT << "\",\n";
        output << "  \"guarded_support_boundary_count\": "
               << evaluator.guarded_support_boundaries() << ",\n";
        output << "  \"near_phase_boundary_count\": "
               << evaluator.near_phase_boundaries() << ",\n";
        output << std::setprecision(21);
        output << "  \"minimum_support_boundary_distance\": \""
               << evaluator.minimum_support_boundary() << "\",\n";
        output << "  \"minimum_phase_boundary_distance\": \""
               << evaluator.minimum_phase_boundary() << "\",\n";

        const auto absolute_amplitude =
            exact_long_double(absolute_amplitude_accumulator.finish());
        output << "  \"absolute_amplitude_midpoint\": {"
               << "\"numerator\": \"" << absolute_amplitude.first
               << "\", \"denominator\": \""
               << absolute_amplitude.second << "\"},\n";
        output << "  \"lags\": [\n";
        for (int lag = 0; lag < manifest.cells; ++lag) {
            const auto real_value =
                exact_long_double(real_accumulators[lag].finish());
            const auto imaginary_value =
                exact_long_double(imaginary_accumulators[lag].finish());
            output << "    {\"lag\": " << lag
                   << ", \"real\": {\"numerator\": \""
                   << real_value.first
                   << "\", \"denominator\": \""
                   << real_value.second
                   << "\"}, \"imag\": {\"numerator\": \""
                   << imaginary_value.first
                   << "\", \"denominator\": \""
                   << imaginary_value.second << "\"}}";
            if (lag + 1 < manifest.cells) {
                output << ',';
            }
            output << '\n';
        }
        output << "  ]\n";
        output << "}\n";
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
