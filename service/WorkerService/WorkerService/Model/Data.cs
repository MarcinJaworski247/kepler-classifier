using System.Text.Json.Serialization;

namespace WorkerService.Model
{
    public class Data
    {
        [JsonPropertyName("kepid")]
        public long? kepid { get; set; }
        [JsonPropertyName("kepoi_name")]
        public string? kepoi_name { get; set; }
        [JsonPropertyName("kepler_name")]
        public string? kepler_name { get; set; }
        [JsonPropertyName("koi_disposition")]
        public string? koi_disposition { get; set; }
        [JsonPropertyName("koi_pdisposition")]
        public string? koi_pdisposition { get; set; }
        [JsonPropertyName("koi_score")]
        public double? koi_score { get; set; }
        [JsonPropertyName("koi_fpflag_nt")]
        public int? koi_fpflag_nt { get; set; }
        [JsonPropertyName("koi_fpflag_ss")]
        public int? koi_fpflag_ss { get; set; }
        [JsonPropertyName("koi_fpflag_co")]
        public int? koi_fpflag_co { get; set; }
        [JsonPropertyName("koi_fpflag_ec")]
        public int? koi_fpflag_ec { get; set; }
        [JsonPropertyName("koi_period")]
        public double? koi_period { get; set; }
        [JsonPropertyName("koi_period_err1")]
        public double? koi_period_err1 { get; set; }
        [JsonPropertyName("koi_period_err2")]
        public double? koi_period_err2 { get; set; }
        [JsonPropertyName("koi_time0bk")]
        public double? koi_time0bk { get; set; }
        [JsonPropertyName("koi_time0bk_err1")]
        public double? koi_time0bk_err1 { get; set; }
        [JsonPropertyName("koi_time0bk_err2")]
        public double? koi_time0bk_err2 { get; set; }
        [JsonPropertyName("koi_impact")]
        public double? koi_impact { get; set; }
        [JsonPropertyName("koi_impact_err1")]
        public double? koi_impact_err1 { get; set; }
        [JsonPropertyName("koi_impact_err2")]
        public double? koi_impact_err2 { get; set; }
        [JsonPropertyName("koi_duration")]
        public double? koi_duration { get; set; }
        [JsonPropertyName("koi_duration_err1")]
        public double? koi_duration_err1 { get; set; }
        [JsonPropertyName("koi_duration_err2")]
        public double? koi_duration_err2 { get; set; }
        [JsonPropertyName("koi_depth")]
        public double? koi_depth { get; set; }
        [JsonPropertyName("koi_depth_err1")]
        public double? koi_depth_err1 { get; set; }
        [JsonPropertyName("koi_depth_err2")]
        public double? koi_depth_err2 { get; set; }
        [JsonPropertyName("koi_prad")]
        public double? koi_prad { get; set; }
        [JsonPropertyName("koi_prad_err1")]
        public double? koi_prad_err1 { get; set; }
        [JsonPropertyName("koi_prad_err2")]
        public double? koi_prad_err2 { get; set; }
        [JsonPropertyName("koi_teq")]
        public double? koi_teq { get; set; }
        [JsonPropertyName("koi_teq_err1")]
        public double? koi_teq_err1 { get; set; }
        [JsonPropertyName("koi_teq_err2")]
        public double? koi_teq_err2 { get; set; }
        [JsonPropertyName("koi_insol")]
        public double? koi_insol { get; set; }
        [JsonPropertyName("koi_insol_err1")]
        public double? koi_insol_err1 { get; set; }
        [JsonPropertyName("koi_insol_err2")]
        public double? koi_insol_err2 { get; set; }
        [JsonPropertyName("koi_model_snr")]
        public double? koi_model_snr { get; set; }
        [JsonPropertyName("koi_tce_plnt_num")]
        public int? koi_tce_plnt_num { get; set; }
        [JsonPropertyName("koi_tce_delivname")]
        public string? koi_tce_delivname { get; set; }
        [JsonPropertyName("koi_steff")]
        public double? koi_steff { get; set; }
        [JsonPropertyName("koi_steff_err1")]
        public double? koi_steff_err1 { get; set; }
        [JsonPropertyName("koi_steff_err2")]
        public double? koi_steff_err2 { get; set; }
        [JsonPropertyName("koi_slogg")]
        public double? koi_slogg { get; set; }
        [JsonPropertyName("koi_slogg_err1")]
        public double? koi_slogg_err1 { get; set; }
        [JsonPropertyName("koi_slogg_err2")]
        public double? koi_slogg_err2 { get; set; }
        [JsonPropertyName("koi_srad")]
        public double? koi_srad { get; set; }
        [JsonPropertyName("koi_srad_err1")]
        public double? koi_srad_err1 { get; set; }
        [JsonPropertyName("koi_srad_err2")]
        public double? koi_srad_err2 { get; set; }
        [JsonPropertyName("ra_str")]
        public string? ra_str { get; set; }
        [JsonPropertyName("dec_str")]
        public string? dec_str { get; set; }
        [JsonPropertyName("koi_kepmag")]
        public double? koi_kepmag { get; set; }
        [JsonPropertyName("koi_kepmag_err")]
        public double? koi_kepmag_err { get; set; }
    }
}
