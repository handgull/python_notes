import re
string = 'this search inside of this text!'
print('search' in string)  # True
match = re.search('this', string)
print(match)  # ho un match object
# (17, 21) tupla che indica dove è stata trovata la corrispondenza
print(match.span())
print(match.start())  # 17
print(match.end())  # 21
print(match.group())  # this, il match
pattern = re.compile('this')
all_matches = pattern.findall(string)
print(all_matches)  # ['this']
# verifica se la stringa matcha completamente con il patterna dato
full_match = pattern.fullmatch(string)
print(full_match)  # None
match = pattern.match(string)
print(match)  # ho un match object
s = pattern.search(string)
print(s.group(0))
# advanced patterns
# r dice che la stringa seguente è raw va vista in modo particolare soprattutto gli / non si comportanmo normalmente
pattern = re.compile(r"\bS\w+")
