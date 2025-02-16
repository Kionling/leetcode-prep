
def word_count(words):
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1 
        else:
            count_dict[word] = 1
    return count_dict

print(word_count(["apple", "banana", "apple", "orange", "banana", "banana"]))
# Expected output: {'apple': 2, 'banana': 3, 'orange': 1}

