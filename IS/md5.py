def left_rotate(x, n):
  """Performs a left rotation on a 32-bit integer."""
  return ((x << n) | (x >> (32 - n))) & 0xffffffff  # Ensure 32-bit result

def md5_like(message):
  """
  Simplified MD5-like function (not cryptographically secure).
  Processes a message string and returns a pseudo-digest in hexadecimal.
  """

  # Constants (adjust for a more complete implementation)
  K = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

  # Preprocessing (assuming ASCII message)
  message_bytes = bytearray(message, 'ascii')
  message_len = len(message_bytes) * 8  # Length in bits
  message_bytes.append(0x80)  # Padding bit
  while len(message_bytes) % 64 != 56:
    message_bytes.append(0)
  message_bytes += message_len.to_bytes(8, 'big')  # Append message length

  # Divide message into 512-bit (16-word) chunks
  words = [message_bytes[i:i+4] for i in range(0, len(message_bytes), 4)]
  words = [int.from_bytes(w, 'big') for w in words]

  # Function F (simplified)
  def F(x, y, z):
    return (x & y) | (~x & z)

  # Main loop (highly simplified, not a secure implementation)
  a, b, c, d = K
  for i in range(len(words)):
    f = F(b, c, d)
    g = (i >> 2 & 0x03)  # Simplified function selection
    a = left_rotate((a + f + words[i] + g) & 0xffffffff, 7)
    d = b
    b = c
    c = a

  # Combine final state (not a secure digest)
  digest = (a & 0xffffffff).to_bytes(4, 'big')
  digest += (b & 0xffffffff).to_bytes(4, 'big')
  digest += (c & 0xffffffff).to_bytes(4, 'big')
  digest += (d & 0xffffffff).to_bytes(4, 'big')

  # Return pseudo-digest in hexadecimal
  return digest.hex()

# Example usage
message = "Hello, world!"
pseudo_digest = md5_like(message)
print("Pseudo-MD5 Digest:", pseudo_digest)
