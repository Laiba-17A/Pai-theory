class Image:
    def __init__(self, px):
        self.pixelData = px

    def applyTrans(self, tfn):
        self.pixelData = tfn(self.pixelData)

    def getCopy(self):
        newPx = []
        for row in self.pixelData:
            newPx.append(row[:])
        return Image(newPx)


def flipH(px):
    newPx = []
    for row in px:
        newPx.append(row[::-1])
    return newPx


def bright(px, val):
    newPx = []
    for row in px:
        newRow = []
        for v in row:
            newRow.append(v + val)
        newPx.append(newRow)
    return newPx


def rot90(px):
    rows = len(px)
    cols = len(px[0])
    newPx = []
    for c in range(cols):
        newRow = []
        for r in range(rows - 1, -1, -1):
            newRow.append(px[r][c])
        newPx.append(newRow)
    return newPx


class AugmentationPipeline:
    def __init__(self):
        self.trans = []

    def addTrans(self, tfn):
        self.trans.append(tfn)

    def run(self, img):
        results = []
        for tfn in self.trans:
            cp = img.getCopy()
            cp.applyTrans(tfn)
            results.append(cp)
        return results


originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]

img = Image(originalPixels)
pipe = AugmentationPipeline()

pipe.addTrans(flipH)
pipe.addTrans(lambda px: bright(px, 20))
pipe.addTrans(rot90)

results = pipe.run(img)

for i, r in enumerate(results, 1):
    print(f"Augmented Image {i}: {r.pixelData}")
