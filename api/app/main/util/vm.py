import json

class DataVM:
    def __init__(
        self, 
        kepid, 
        kepoi_name, 
        kepler_name, 
        koi_disposition, 
        koi_fpflag_nt, 
        koi_fpflag_ss, 
        koi_fpflag_co, 
        koi_fpflag_ec,
        koi_period, 
        koi_time0bk,
        koi_impact, 
        koi_duration, 
        koi_depth,
        koi_prad, 
        koi_teq, 
        koi_insol, 
        koi_model_snr,
        koi_steff, 
        koi_slogg,
        koi_srad,
        ra,
        dec,
        koi_kepmag
        ):
        self.kepid = kepid
        self.kepoi_name = kepoi_name
        self.kepler_name = kepler_name
        self.koi_disposition = koi_disposition
        self.koi_fpflag_nt = koi_fpflag_nt
        self.koi_fpflag_ss = koi_fpflag_ss
        self.koi_fpflag_co = koi_fpflag_co
        self.koi_fpflag_ec = koi_fpflag_ec
        self.koi_period = koi_period
        self.koi_time0bk = koi_time0bk
        self.koi_impact = koi_impact
        self.koi_duration = koi_duration
        self.koi_depth = koi_depth
        self.koi_prad = koi_prad
        self.koi_teq = koi_teq
        self.koi_insol = koi_insol
        self.koi_model_snr = koi_model_snr
        self.koi_steff = koi_steff
        self.koi_slogg = koi_slogg
        self.koi_srad = koi_srad
        self.ra = ra
        self.dec = dec
        self.koi_kepmag = koi_kepmag

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)