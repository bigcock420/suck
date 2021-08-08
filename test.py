(lambda length: __import__('clipboard').copy(''.join([__import__('random').choice(__import__('string').ascii_letters + __import__('string').digits + __import__('string').punctuation) for i in range(length)])))(10)
  
