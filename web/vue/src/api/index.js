import axios from "../axios";

class ApiService {
  getData() {
    return axios.get("/data/getPreparedData");
  }
}

export default new ApiService();
