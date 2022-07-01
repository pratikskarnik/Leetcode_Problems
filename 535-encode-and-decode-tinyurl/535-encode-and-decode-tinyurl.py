import base64
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded_chars = []
        key="password"
        for i in range(len(longUrl)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(longUrl[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return encoded_string

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        encoded_chars = []
        key="password"
        for i in range(len(shortUrl)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(shortUrl[i]) - ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return encoded_string


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))