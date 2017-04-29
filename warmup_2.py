
def string_times(string, n):
  return string * n


def front_times(string, n):
  front = string[0:3]
  if len(string) <= 3:
      return string * n
  else:
      return front * n
