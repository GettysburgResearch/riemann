// g++ -O3 -std=c++17 newton_prefix_nov18.cpp -lcrypto -o newton_prefix
// Stream an exact Mobius prefix and directed dyadic bounds for its energy.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <openssl/evp.h>

using U64 = std::uint64_t;
using U128 = unsigned __int128;
using I128 = __int128;
constexpr U64 max_endpoint = (U64{1} << 32) - 1;
constexpr U64 segment_size = U64{1} << 18;

static std::string decimal(I128 value) {
    if (value < 0) return "-" + decimal(-value);
    std::string digits;
    do {
        digits.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    } while (value);
    std::reverse(digits.begin(), digits.end());
    return digits;
}

using Digest = std::unique_ptr<EVP_MD_CTX, decltype(&EVP_MD_CTX_free)>;

static std::string current_hash(const Digest& digest) {
    Digest copy(EVP_MD_CTX_new(), EVP_MD_CTX_free);
    unsigned char raw[EVP_MAX_MD_SIZE];
    unsigned int size = 0;
    if (!copy || EVP_MD_CTX_copy_ex(copy.get(), digest.get()) != 1 ||
        EVP_DigestFinal_ex(copy.get(), raw, &size) != 1 || size != 32)
        throw std::runtime_error("SHA-256 finalization failed");
    std::ostringstream hex;
    for (unsigned int i = 0; i < size; ++i)
        hex << std::hex << std::setfill('0') << std::setw(2) << unsigned(raw[i]);
    return hex.str();
}

static std::vector<U64> base_primes(U64 last, bool divide) {
    std::vector<U64> primes;
    if (divide) {
        for (U64 n = 2; n*n <= last; ++n) {
            bool prime = true;
            for (U64 p : primes) {
                if (p*p > n) break;
                if (n % p == 0) { prime = false; break; }
            }
            if (prime) primes.push_back(n);
        }
    } else {
        std::vector<bool> composite(65536);
        for (U64 n = 2; n*n <= last; ++n) {
            if (composite[n]) continue;
            primes.push_back(n);
            for (U64 k = n*n; k < composite.size(); k += n) composite[k] = true;
        }
    }
    return primes;
}

struct Bounds { I128 low = 0, high = 0; };

static Bounds weighted(U128 total, U64 left_denominator, U64 right_denominator) {
    if (total > std::numeric_limits<U64>::max())
        throw std::runtime_error("numerator cannot be shifted exactly");
    const U128 numerator = total << 64;
    const auto low = numerator / right_denominator;
    const auto high = numerator / left_denominator + (numerator % left_denominator != 0);
    if (high >> 126) throw std::runtime_error("accumulator domain exceeded");
    return {static_cast<I128>(low), static_cast<I128>(high)};
}

struct Energy {
    Bounds square, mean;
    void add(U64 first, U64 last, U128 squares, U128 positive, U128 negative) {
        const U64 left = first*(first+1), right = last*(last+1);
        const auto sq = weighted(squares, left, right);
        const auto pos = weighted(positive, left, right);
        const auto neg = weighted(negative, left, right);
        square.low += sq.low;
        square.high += sq.high;
        mean.low += pos.low - neg.high;
        mean.high += pos.high - neg.low;
    }
};

int main(int argc, char** argv) {
    if (argc != 3 || (std::string(argv[2]) != "multiply" &&
                      std::string(argv[2]) != "divide")) {
        std::cerr << "usage: newton_prefix LAST multiply|divide\n";
        return 2;
    }
    const U64 stop = std::stoull(argv[1]);
    if (stop < 1 || stop > max_endpoint) throw std::runtime_error("invalid endpoint");
    const bool divide = std::string(argv[2]) == "divide";
    const auto primes = base_primes(stop, divide);
    Digest digest(EVP_MD_CTX_new(), EVP_MD_CTX_free);
    if (!digest || EVP_DigestInit_ex(digest.get(), EVP_sha256(), nullptr) != 1)
        throw std::runtime_error("SHA-256 initialization failed");

    std::vector<U64> checkpoints;
    for (U64 k : {U64{1}, U64{3}, U64{15}, U64{255}, U64{65535}, max_endpoint})
        if (k < stop) checkpoints.push_back(k);
    checkpoints.push_back(stop);
    const U64 size = divide ? segment_size-129 : segment_size;
    std::vector<std::uint32_t> factor(size);
    std::vector<std::int8_t> signs(size);
    std::vector<unsigned char> bytes(size);
    std::int64_t mertens = 0;
    U64 zeros = 0, largest_abs = 0, index = 0, blocks = 0;
    Energy energy;
    std::cout << "{\"method\":\"" << argv[2] << "\",\"bits\":64,\"rows\":[\n";

    for (U64 first = 1; first <= stop;) {
        const U64 last = std::min({first+size-1, stop, checkpoints.at(index)});
        const U64 count = last-first+1;
        for (U64 i = 0; i < count; ++i) {
            factor[i] = divide ? static_cast<std::uint32_t>(first+i) : 1U;
            signs[i] = 1;
        }
        for (U64 p : primes) {
            if (p*p > last) break;
            const U64 start = ((first+p-1)/p)*p;
            for (U64 n = start; n <= last; n += p) {
                const U64 i = n-first;
                if (divide) {
                    factor[i] /= static_cast<std::uint32_t>(p);
                    if (factor[i] % p == 0) signs[i] = 0;
                } else {
                    factor[i] *= static_cast<std::uint32_t>(p);
                }
                signs[i] = -signs[i];
            }
            if (!divide) {
                const U64 square = p*p;
                for (U64 n = ((first+square-1)/square)*square; n <= last; n += square)
                    signs[n-first] = 0;
            }
        }
        for (U64 left = first; left <= last;) {
            // Different partitions provide separate enclosures in each mode.
            const U64 length = std::max(U64{1}, left/(divide ? 98317 : 65536));
            const U64 right = std::min(last, left+length-1);
            U128 squares = 0, positive = 0, negative = 0;
            for (U64 n = left; n <= right; ++n) {
                const U64 i = n-first;
                const bool leftover = divide ? factor[i] > 1 : factor[i] < n;
                const int mu = leftover ? -signs[i] : signs[i];
                bytes[i] = static_cast<unsigned char>(mu+1);
                zeros += (mu == 0);
                mertens += mu;
                const U64 magnitude = mertens < 0 ? U64(-mertens) : U64(mertens);
                largest_abs = std::max(largest_abs, magnitude);
                squares += U128(magnitude)*magnitude;
                (mertens >= 0 ? positive : negative) += magnitude;
            }
            energy.add(left, right, squares, positive, negative);
            ++blocks;
            left = right+1;
        }
        if (EVP_DigestUpdate(digest.get(), bytes.data(), count) != 1)
            throw std::runtime_error("SHA-256 update failed");
        if (last == checkpoints.at(index)) {
            if (index) std::cout << ",\n";
            std::cout << "{\"N\":" << last << ",\"M\":" << mertens
                      << ",\"max_abs_M\":" << largest_abs << ",\"zeros\":" << zeros
                      << ",\"blocks\":" << blocks << ",\"sha256\":\"" << current_hash(digest)
                      << "\",\"E\":[\"" << decimal(energy.square.low) << "\",\""
                      << decimal(energy.square.high) << "\"],\"u\":[\""
                      << decimal(energy.mean.low) << "\",\"" << decimal(energy.mean.high)
                      << "\"]}" << std::flush;
            ++index;
        }
        first = last+1;
    }
    std::cout << "\n]}\n";
}
