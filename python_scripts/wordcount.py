def file_to_str(f):
  project_root = "/Users/yasha.podeswa/Documents/everything_else/git_repos/newbie_coding_club/python_scripts"
  with open(project_root + "/" + f, 'rU') as text:
    return text.read()

def word_count(text):
  words = text.split()
  counts = {}
  alpanums = {'0': True, '1': True, '2': True, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True, '9': True, 'a': True, 'b': True, 'c': True, 'd': True, 'e': True, 'f': True, 'g': True, 'h': True, 'i': True, 'j': True, 'k': True, 'l': True, 'm': True, 'n': True, 'o': True, 'p': True, 'q': True, 'r': True, 's': True, 't': True, 'u': True, 'v': True, 'w': True, 'x': True, 'y': True, 'z': True, 'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True, 'H': True, 'I': True, 'J': True, 'K': True, 'L': True, 'M': True, 'N': True, 'O': True, 'P': True, 'Q': True, 'R': True, 'S': True, 'T': True, 'U': True, 'V': True, 'W': True, 'X': True, 'Y': True, 'Z': True}

  for word in words:
    lc_word = word.lower()
    word_list = []
    for char in lc_word:
      if char in alpanums:
        word_list.append(char)
    simple_word = "".join(word_list)

    if simple_word in counts:
      counts[simple_word] += 1
    elif simple_word != "":
      counts[simple_word] = 1

  return counts

def dict_range(d):
  if len(d) == 0 or type(d) is not dict:
    raise Exception("You must pass a non-empty dictionary to the dict_range function")

  lowest, highest = None, None

  for key in d:
    val = d[key]
    if lowest and highest:
      if val < lowest:
        lowest = val
      if val > highest:
        highest = val
    else:
      lowest, highest = val, val

  x = highest
  out_dict = {}
  while x <= highest:
    out_dict[x] = []
    x += 1

  return out_dict, lowest, highest

def main():
  raw = file_to_str("alice_in_wonderland.txt")
  counts = word_count(raw)
  # print counts
  print dict_range(counts)

main()
