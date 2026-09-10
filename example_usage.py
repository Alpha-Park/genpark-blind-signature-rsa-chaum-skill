from client import BlindRSASignature

def main():
    print("=== Testing Chaum Blind RSA Signature ===")
    rsa = BlindRSASignature()
    
    m = 256
    r = 7
    print(f"Original Secret Message: {m}")
    
    # 1. Client blinds message
    m_blind = rsa.blind(m, r)
    print(f"Blinded Message: {m_blind}")
    
    # 2. Signer signs blinded message
    s_blind = rsa.sign_blinded(m_blind)
    print(f"Signer Blind Signature: {s_blind}")
    
    # 3. Client unblinds signature
    s = rsa.unblind(s_blind, r)
    print(f"Unblinded Signature: {s}")
    
    # 4. Public verification
    valid = rsa.verify(m, s)
    print(f"Signature Verification: {valid}")
    assert valid
    
    invalid = rsa.verify(m + 1, s)
    print(f"Tampered Verification (should be False): {invalid}")
    assert not invalid
    print("=== Blind RSA Verification Complete ===")

if __name__ == "__main__":
    main()
