import string, random, clipboard

clipboard.copy(''.join([random.choice([string.ascii_letters + "123456789" + string.punctuation]) for i in range(20)]))