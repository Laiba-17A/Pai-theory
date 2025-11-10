
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 2 =========================")
print(" ")

postslist = [
    {'id': 1, 'text': "I LOVE the new #GutPhone! Battery life is amazing."},
    {'id': 2, 'text': "My #GutPhone is a total disaster. The screen is already broken!"},
    {'id': 3, 'text': "Worst customer service ever from @GutPhoneSupport. Avoid!"},
    {'id': 4, 'text': "The @GutPhoneSupport team was helpful and resolved my issue. Great service!"}
]

PUNCTUATION_CHARS = ['.', ',', '!', '?', ':', ';', "'", '"']
STOPWORDS_SET = {'i', 'me', 'my', 'an', 'the', 'is', 'am', 'was', 'to', 'of', 'by', 'for', 'and', 'with', 'this', 'that'}
POSITIVE_WORDS = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS = {'disaster', 'broken', 'bad', 'worst', 'avoid'}


def preprocessText(text, punclist, sw):
    text = text.lower()
    for p in punclist:
        text = text.replace(p, '')
    words = text.split()
    filtered = []
    for w in words:
        if w not in sw:
            filtered.append(w)
    return filtered


def analyzePosts(postsList, punc, stop, pos, negt):
    analyzed = []
    for post in postsList:
        processed = preprocessText(post['text'], punc, stop)
        score = 0
        for word in processed:
            if word in pos:
                score += 1
            elif word in negt:
                score -= 1
        analyzed.append({
            'id': post['id'],
            'text': post['text'],
            'processedtext': processed,
            'score': score
        })
    return analyzed


def getFlaggedPosts(sposts, st=-1):
    flagged = []
    for post in sposts:
        if post['score'] <= st:
            flagged.append(post)
    return flagged


def findNegativeTopics(fposts):
    topics = {}
    for post in fposts:
        for word in post['processedtext']:
            if word.startswith('#') or word.startswith('@'):
                if word in topics:
                    topics[word] += 1
                else:
                    topics[word] = 1
    return topics


s = analyzePosts(postslist, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS, NEGATIVE_WORDS)
f = getFlaggedPosts(s,-1)
n = findNegativeTopics(f)

print("Analyzed Posts:\n", s)
print("\nFlagged Negative Posts:\n", f)
print("\nTrending Negative Topics:\n", n)
