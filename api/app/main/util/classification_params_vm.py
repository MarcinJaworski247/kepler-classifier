class ClassificationParamsVM:
    def __init__(self, isCrossValidation, testDataPercentage, treesCount, neighboursCount, foldsCount):
        self.isCrossValidation = isCrossValidation
        self.testDataPercentage = testDataPercentage
        self.treesCount = treesCount
        self.neighboursCount = neighboursCount
        self.foldsCount = foldsCount
