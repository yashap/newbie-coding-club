score_dict = {'assfucking': (-4, 50), 'hi': (1, 1)}

# tweet_body == "Hi Obama is assfucking"
def learn(tweet_body):
    words = tweet_body.split()
    if not words:
        return 0
    total = 0
    weight_total = 0
    for word in words:
        if word in score_dict:
            (score, weight) = score_dict[word]
            total += score * weight
            weight_total += weight
    print(total)

    # update dictionary
    unknown_word_score = total / float(len(words))
    for word in words:
        if word in score_dict:
            score_dict[word] = (score_dict[word] + unknown_word_score) / 2.0
        else:
            score_dict[word] = unknown_word_score
    return total

import pprint
pp = pprint.PrettyPrinter(indent=2)
print(learn("Hi Obama is  assfucking"))
pp.pprint(score_dict)
print(learn("Obama was amazing"))
pp.pprint(score_dict)
