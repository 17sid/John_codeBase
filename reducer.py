import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word,count = line.split('   ',1)
    try:
        count = int(count)
    except ValueError:
        continue
        if current_word == word:
            current_count += count
        else:
            if current_word:
                w='%s \t  %s' % (current_word, current_count)
                print(w)
            current_count = count
            current_word = word
if current_word == word:
    c='%s \t  %s' % (current_word,current_count)
    print(c)