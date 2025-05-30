import base64
import hashlib
import hmac
from time import time

from api import steam_guard_code_len, steam_guard_code_translations

class Account:
    def __init__(self, shared_secret):
        self.shared_secret = shared_secret
    
    def generate_guard_code(self):
        temp = base64.b64decode(self.shared_secret)
        current_time = time() // 30
        time_array = int(current_time).to_bytes(8)
        hmac_generator = hmac.new(temp, time_array, hashlib.sha1)
        hashed_data = hmac_generator.digest()
        b = hashed_data[19] & 0xF
        code_point = (hashed_data[b]&0x7F) << 24 | (hashed_data[b+1]&0xFF) << 16 | (hashed_data[b+2]&0xFF) << 8 | (hashed_data[b+3]&0xFF)
        code_array = bytearray(5)
        for i in range(5):
            code_array[i] = steam_guard_code_translations[code_point % steam_guard_code_len]
            code_point //= steam_guard_code_len
        return code_array.decode()