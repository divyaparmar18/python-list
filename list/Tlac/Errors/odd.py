def odd_values_string(Str):
  result = ""
  for  i in range(len(Str)):
    if i % 2 == 0:
        result = result + Str[i]
  return result

print "'" +  odd_values_string("abcdef") , odd_values_string("python") + "'"

def odd_value_string(values):
  result = ""
  for i in range(len(values)):
    if i % 2 == 0:
      result = result + values[i]
  return result

print "'" +  odd_values_string("abcdef") , odd_values_string("python") + "'"


def odd_value_string(values):
  results = ""
  for i in range(len(values)):
    if i % 2 == 0:
      results = results + values[i]
  return results

print "'" + odd_value_string('abcdef'),  odd_value_string('python') + "'"
