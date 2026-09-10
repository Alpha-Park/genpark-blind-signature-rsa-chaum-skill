from client import BlindRSASignature
import json

def handle_request(req):
    rsa = BlindRSASignature()
    action = req.get("action")
    if action == "blind":
        m = req.get("m", 0)
        r = req.get("r", 7)
        return {"status": "ok", "blinded": rsa.blind(m, r)}
    elif action == "sign":
        mb = req.get("blinded", 0)
        return {"status": "ok", "blind_sig": rsa.sign_blinded(mb)}
    elif action == "verify":
        m = req.get("m", 0)
        s = req.get("s", 0)
        return {"status": "ok", "valid": rsa.verify(m, s)}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "blind", "m": 123})))
