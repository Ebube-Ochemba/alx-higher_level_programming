def magic_string():
   magic_string.count += 1
   return ', '.join(['BestSchool'] * magic_string.count)
magic_string.count = 0
