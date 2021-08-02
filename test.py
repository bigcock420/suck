import string, random, clipboard

def generate_sample(length: int) -> str:
  return clipboard.copy(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)]))
  
generate_sample(10)
