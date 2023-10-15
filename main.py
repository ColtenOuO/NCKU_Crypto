from Crypto.Cipher import AES
import base64
import itertools

# 加密参数
key = "|q▆~k=▆&?I$Fx▆N▆"
mode = AES.MODE_ECB
padding = '\x00'

# 加密后的Base64编码密文
cipher_text = base64.b64decode("FZp57a6p84EUNC7I/ENj4RhPZtryOJr4che9JbA8ng1eI8ZMTlsl8kzicBDqkOqkFj3lwC69KR2MeA8lscVlig==")

# 字符集合，包括可能的字符
charset = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# 所有可能的字符替代组合
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
        # 解密失败，继续下一个字符的尝试
        continue