# generator for fibonacci & Yanghui triangles

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done'
  

def triangles():
  n = 0
  yield [1]
  prev = [1, 1]
  yield prev
  while n < 100:
    res = [1] * (n + 3)
    for i in range(len(res)):
      if i == 0 or i == len(res) - 1:
        res[i] = 1
      else:
        res[i] = prev[i-1] + prev[i]
    prev = res
    yield res
    n = n + 1
  return 'done'


def triangles1():
  res = [1]
  while True:
    yield res
    res = [1] + [res[i-1] + res[i] for i in range(1, len(res))] + [1]
    
