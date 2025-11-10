
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 2 =========================")
print(" ")

postsList = [
    {'id': 1, 'text': "I LOVE the new #GulPhone! Battery life is amazing."},
    {'id': 2, 'text': "My #GulPhone is a total disaster. The screen is already broken!"},
    {'id': 3, 'text': "Worst customer service ever from @GulPhoneSupport. Avoid!"},
    {'id': 4, 'text': "The @GulPhoneSupport team was helpful and resolved my issue. Great service!"}
]

PUNCTUATION_CHARS = ['.', ',', '!', '?', ':', ';', "'", '"']
STOPWORDS_SET = {'i', 'me', 'my', 'an', 'the', 'is', 'am', 'was', 'to', 'of', 'by', 'for', 'and', 'with', 'this', 'that'}
POSITIVE_WORDS = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS = {'disaster', 'broken', 'bad', 'worst', 'avoid'}


def preprocessText(text, punctuationList, stopwordsSet):
    text = text.lower()
    for p in punctuationList:
        text = text.replace(p, '')
    words = text.split()
    return [w for w in words if w not in stopwordsSet]


def analyzePosts(postsList, punctuation, stopwords, positive, negative):
    def evaluate(post):
        processed = preprocessText(post['text'], punctuation, stopwords)
        score = 0
        for word in processed:
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1
        return {'id': post['id'], 'text': post['text'], 'processedText': processed, 'score': score}
    return list(map(lambda p: evaluate(p), postsList))


def getFlaggedPosts(scoredPosts, sentimentThreshold=-1):
    return [p for p in scoredPosts if p['score'] <= sentimentThreshold]


def findNegativeTopics(flaggedPosts):
    topics = {}
    for post in flaggedPosts:
        for word in post['processedText']:
            if word.startswith('#') or word.startswith('@'):
                topics[word] = topics.get(word, 0) + 1
    return topics


scoredPosts = analyzePosts(postsList, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS, NEGATIVE_WORDS)
flaggedPosts = getFlaggedPosts(scoredPosts, sentimentThreshold=-1)
negativeTopics = findNegativeTopics(flaggedPosts)

print("Analyzed Posts:\n", scoredPosts)
print("\nFlagged Negative Posts:\n", flaggedPosts)
print("\nTrending Negative Topics:\n", negativeTopics)
