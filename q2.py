
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 2 =========================")
print(" ")

postsList = [
    {'id': 1, 'text': "I LOVE the new #GutPhone! Battery life is amazing."},
    {'id': 2, 'text': "My #GutPhone is a total disaster. The screen is already broken!"},
    {'id': 3, 'text': "Worst customer service ever from @GutPhoneSupport. Avoid!"},
    {'id': 4, 'text': "The @GutPhoneSupport team was helpful and resolved my issue. Great service!"}
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
    filtered = []
    for w in words:
        if w not in stopwordsSet:
            filtered.append(w)
    return filtered


def analyzePosts(postsList, punctuation, stopwords, positive, negative):
    analyzed = []
    for post in postsList:
        processed = preprocessText(post['text'], punctuation, stopwords)
        score = 0
        for word in processed:
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1
        analyzed.append({
            'id': post['id'],
            'text': post['text'],
            'processedText': processed,
            'score': score
        })
    return analyzed


def getFlaggedPosts(scoredPosts, sentimentThreshold=-1):
    flagged = []
    for post in scoredPosts:
        if post['score'] <= sentimentThreshold:
            flagged.append(post)
    return flagged


def findNegativeTopics(flaggedPosts):
    topics = {}
    for post in flaggedPosts:
        for word in post['processedText']:
            if word.startswith('#') or word.startswith('@'):
                if word in topics:
                    topics[word] += 1
                else:
                    topics[word] = 1
    return topics


scoredPosts = analyzePosts(postsList, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS, NEGATIVE_WORDS)
flaggedPosts = getFlaggedPosts(scoredPosts, sentimentThreshold=-1)
negativeTopics = findNegativeTopics(flaggedPosts)

print("Analyzed Posts:\n", scoredPosts)
print("\nFlagged Negative Posts:\n", flaggedPosts)
print("\nTrending Negative Topics:\n", negativeTopics)
