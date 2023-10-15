from Crypto.Cipher import AES
import base64
import itertools

key = "|qL~k=S&?I$Fx+N("
mode = AES.MODE_ECB
padding = '\x00'

cipher_text = base64.b64decode("FZp57a6p84EUNC7I/ENj4RhPZtryOJr4che9JbA8ng1eI8ZMTlsl8kzicBDqkOqkFj3lwC69KR2MeA8lscVlig==")

charset = 'LS!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
#|qL~k=S&?I$Fx+N(
combinations = itertools.product(charset, repeat=key.count('▆'))

for replacement_chars in combinations:
    modified_key = key
    for char in replacement_chars:
        modified_key = modified_key.replace('▆', char, 1)
    print(modified_key)
    try:
        decryptor = AES.new(modified_key.encode('utf-8'), mode)
        plaintext = decryptor.decrypt(cipher_text).rstrip(padding.encode('utf-8'))
        print(f"GET：{plaintext.decode('utf-8')}")
    except:
        continue