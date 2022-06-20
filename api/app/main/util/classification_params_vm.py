class ClassificationParamsVM:
    def __init__(self, isCrossValidation, testDataPercentage, treesCount, neighboursCount, foldsCount, svcKernel, knnDistanceAlgorithm):
        self.isCrossValidation = isCrossValidation
        self.testDataPercentage = testDataPercentage
        self.treesCount = treesCount
        self.neighboursCount = neighboursCount
        self.foldsCount = foldsCount
        self.svcKernel = svcKernel
        self.knnDistanceAlgorithm = knnDistanceAlgorithm
