
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 4 =========================")
print(" ")

class Image:
    def __init__(self, pixelData):
        self.pixelData = pixelData

    def applyTransformation(self, transformationFunc):
        self.pixelData = transformationFunc(self.pixelData)

    def getCopy(self):
        return Image([[value for value in row] for row in self.pixelData])


def flipHorizontal(pixelData):
    return [row[::-1] for row in pixelData]


def adjustBrightness(pixelData, brightnessValue):
    return [[value + brightnessValue for value in row] for row in pixelData]


def rotateNinetyDegrees(pixelData):
    return [list(row) for row in zip(*pixelData[::-1])]


class AugmentationPipeline:
    def __init__(self):
        self.transformations = []

    def addTransformation(self, transformFunc):
        self.transformations.append(transformFunc)

    def processImage(self, originalImage):
        results = []
        for func in self.transformations:
            imgCopy = originalImage.getCopy()
            imgCopy.applyTransformation(func)
            results.append(imgCopy)
        return results


originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]

img = Image(originalPixels)
pipeline = AugmentationPipeline()

pipeline.addTransformation(flipHorizontal)
pipeline.addTransformation(lambda data: adjustBrightness(data, 20))
pipeline.addTransformation(rotateNinetyDegrees)

augmentedImages = pipeline.processImage(img)

for i, newImg in enumerate(augmentedImages, start=1):
    print(f"Augmented Image {i}: {newImg.pixelData}")
