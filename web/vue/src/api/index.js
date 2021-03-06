import axios from "../axios";

class ApiService {
  getData() {
    return axios.get("/data/getPreparedData");
  }
  getStatistics() {
    return axios.get("/stats/getDescriptionStats");
  }
  getPearsonCorr() {
    return axios.get("/plots/getPearsonCorr");
  }
  getValues(attribute) {
    return axios.get("/plots/getValues", {
      params: {
        attribute,
      },
    });
  }
  getClassificationResult(_params) {
    return axios.get("/classification/getClassificationResult", {
      params: {
        isCrossValidation: _params.isCrossValidation,
        testDataPercentage: _params.testDataPercentage,
        treesCount: _params.treesCount,
        foldsCount: _params.foldsCount,
        neighboursCount: _params.neighboursCount,
        knnDistanceAlgorithm: _params.knnDistanceAlgorithm,
        svcKernel: _params.svcKernel,
      },
    });
  }
  getSimpleLinearRegression(attr1, attr2) {
    return axios.get("/plots/getSimpleLinearRegression", {
      params: {
        firstAttribute: attr1,
        secondAttribute: attr2,
      },
    });
  }
  getClassInfo() {
    return axios.get("/data/getClassInfo");
  }
  getOutliers() {
    return axios.get("/data/getOutliers");
  }
  classifyData(_method) {
    return axios.get("/classification/classifyCandidates", {
      params: {
        method: _method,
      },
    });
  }
  getEmptyCells() {
    return axios.get("/data/getEmptyCells");
  }
}

export default new ApiService();
