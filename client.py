class BlindRSASignature:
    """
    Chaum Blind RSA Digital Signature Scheme.
    Allows a client to obtain a valid digital signature on a secret message without revealing its contents to the signer.
    """
    def __init__(self, p=61, q=53):
        self.n = p * q
        phi = (p - 1) * (q - 1)
        self.e = 17 # coprime to phi = 3120
        self.d = pow(self.e, -1, phi)

    def blind(self, m, r=7):
        r_e = pow(r, self.e, self.n)
        return (m * r_e) % self.n

    def sign_blinded(self, m_blinded):
        return pow(m_blinded, self.d, self.n)

    def unblind(self, s_blinded, r=7):
        r_inv = pow(r, -1, self.n)
        return (s_blinded * r_inv) % self.n

    def verify(self, m, s):
        return pow(s, self.e, self.n) == (m % self.n)
