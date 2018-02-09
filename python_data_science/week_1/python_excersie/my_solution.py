import re
import collections
tale_of_two_cities_file = open('98-0.txt')
REMOVE_PUNCTUATION_REGEX = re.compile(r"[\.,\/“\(\)\*]") #[,\.“'‘\(\-\*\)\[\]]]")

stopwords_set = set(stopword.strip() for stopword in open('stopwords').readlines())

word_count = {}
for word in tale_of_two_cities_file.read().lower().split():
    clean_word = REMOVE_PUNCTUATION_REGEX.sub("", word.lower())

    if clean_word not in stopwords_set:
        word_count.setdefault(clean_word, 0)
        word_count[clean_word] += 1

word_counter = collections.Counter(word_count)

for (word, count) in word_counter.most_common(10):
    print(word,count)
