import hashlib
import time
import os

class PropertyTransaction:
    def __init__(self):
        self.keys = {}
    
    def generate_key(self, party):
        key = os.urandom(16).hex()
        self.keys[party] = key
        print(f"✓ Key generated for {party}")
        return key
    
    def encrypt_doc(self, doc, party):
        if party not in self.keys:
            self.generate_key(party)
        
        # Simple XOR encryption for demo
        key = self.keys[party]
        encrypted = ''.join(chr(ord(c) ^ len(key)) for c in doc)
        print(f"✓ Document encrypted for {party}")
        return encrypted
    
    def decrypt_doc(self, encrypted, party):
        key = self.keys[party]
        decrypted = ''.join(chr(ord(c) ^ len(key)) for c in encrypted)
        print(f"✓ Document decrypted for {party}")
        return decrypted
    
    def sign_doc(self, doc):
        signature = hashlib.sha256(doc.encode()).hexdigest()[:16]
        print(f"✓ Document signed: {signature}")
        return signature
    
    def process_contract(self):
        print("=== Property Transaction Demo ===")
        
        contract = "Property Sale: 123 Main St, £250,000"
        
        # Seller signs
        seller_sig = self.sign_doc(contract)
        
        # Encrypt for transmission
        encrypted = self.encrypt_doc(contract, "Buyer")
        
        # Buyer receives and decrypts
        decrypted = self.decrypt_doc(encrypted, "Buyer")
        
        # Buyer signs
        buyer_sig = self.sign_doc(decrypted)
        
        tx_id = f"TX_{int(time.time())}"
        
        print(f"\n📋 Transaction Complete!")
        print(f"   ID: {tx_id}")
        print(f"   Seller: {seller_sig}")
        print(f"   Buyer: {buyer_sig}")
        print(f"   Status: SUCCESS")

# Run the demo
if __name__ == "__main__":
    demo = PropertyTransaction()
    demo.process_contract()