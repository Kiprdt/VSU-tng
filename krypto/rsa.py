import math
import random


class RSA:

    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e

    # these methods are useless
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def generate_prime():
        while True:
            p = random.randint(2**2, 2**5)
            q = random.randint(2**2, 2**5)
            phi = (p - 1) * (q - 1)
            e = random.randint(3, phi)
            if q < p < 2 * q and RSA.is_prime(p) and RSA.is_prime(q) and math.gcd(e, (p - 1) * (q-1)) == 1:
                break
        return q, p, e
    # end of useless

    def key_generate(self):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        d = pow(self.e, -1, phi)
        return (self.e, n), (d, n)

    def encrypt(self, message):
        n = self.p * self.q
        key = self.e
        return pow(message, key, n)

    def decrypt(self, cipher):
        n = self.p * self.q
        key = RSA.key_generate(self)[1][0]
        return pow(cipher, key, n)

    @staticmethod
    def fractions(n, e):
        sequence = []
        q = n // e
        r = n % e
        sequence.append(q)
        while r != 0:
            n, e = e, r
            q = n // e
            r = n % e
            sequence.append(q)
        return sequence

    @staticmethod
    def convergents(sequence):
        numerator = [sequence[0], sequence[0] * sequence[1] + 1]
        denominator = [1, sequence[1]]
        for i in range(2, len(sequence)):
            numerator.append(sequence[i] * numerator[i - 1] + numerator[i - 2])
            denominator.append(sequence[i] * denominator[i - 1] + denominator[i - 2])
        return numerator, denominator

    def wiener_attack(self):
        sequence = RSA.fractions(self.p * self.q, self.e)
        numerators, denominators = RSA.convergents(sequence)
        n = self.p * self.q
        for i in range(len(numerators)):
            d_n = numerators[i]
            k_n = denominators[i]
            ph = (self.e * d_n - 1) // k_n
            a = 1
            b = -n + ph - 1
            c = n
            discriminant = b**2 - 4 * a * c
            if discriminant > 0:
                pn = (n - ph + 1 + gmpy2.isqrt(discriminant)) // 2
                qn = (n - ph + 1 - gmpy2.isqrt(discriminant)) // 2
                if pn * qn == n:
                    phi = (pn - 1) * (qn - 1)
                    return pow(self.e, -1, phi)


rsa1 = RSA(239, 379, 17993)
print(rsa1.encrypt(45))
print(rsa1.decrypt(rsa1.encrypt(45)))
print(rsa1.wiener_attack())

# p = 239, q = 379, e = 17993
# p = 30763, q = 39667, e = 1073780833
# p = 47129, q = 59333, e = 1779399043
# p = 778579, q = 389297, e = 2421079
# p = 107, q = 131, e = 9187
