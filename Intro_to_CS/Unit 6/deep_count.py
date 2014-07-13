#Deep Count

def is_list(p):
    return isinstance(p, list)

def deep_count(p):
  sum1 = 0
  for e in p:
      sum1 = sum1 + 1
      if is_list(e):
          sum1 = sum1 + deep_count(e)
  return sum1
  
