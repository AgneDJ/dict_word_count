"""Count words in file."""


# put your code here.
def count(filename):

    word_counting_dictionary = {}
    open_file = open(filename)
    # for file in open_file:
    for line in open_file:
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            word_counting_dictionary[word] = word_counting_dictionary.get(
                word, 0) + 1
        # print(word_counting_dictionary[word])
            # if word in word_counting_dictionary:
            #     word_counting_dictionary[word] += 1
            # else:
            #     word_counting_dictionary[word] = 1
    return word_counting_dictionary


file = "test.txt"
print(count(file))
