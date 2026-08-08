import math

class PasswordSecurityEngine:
    """Calculates password entropy (bits of security) for generated strings."""
    
    @staticmethod
    def calculate_entropy(password: str) -> float:
        if not password:
            return 0.0
        
        pool_size = 0
        if any(c.islower() for c in password):
            pool_size += 26
        if any(c.isupper() for c in password):
            pool_size += 26
        if any(c.isdigit() for c in password):
            pool_size += 10
        if any(not c.isalnum() for c in password):
            pool_size += 32
            
        if pool_size == 0:
            return 0.0
            
        entropy = len(password) * math.log2(pool_size)
        return round(entropy, 2)