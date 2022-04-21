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
  getValues() {
    return axios.get("/plots/getValues");
  }
  getClassificationResult(_params) {
    return axios.get("/classification/getClassificationResult", {
      params: {
        isCrossValidation: _params.isCrossValidation,
        testDataPercentage: _params.testDataPercentage,
        treesCount: _params.treesCount,
        foldsCount: _params.foldCount,
        neighboursCount: _params.neighboursCount,
      },
    });
  }
}

export default new ApiService();
