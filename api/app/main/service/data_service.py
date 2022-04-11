import pandas as pd
from random import randrange
import datetime
import json

from app.main.util.vm import DataVM

ORIGINAL_FILE_PATH = 'D:\keppler-classifier\keppler-data.csv'
PREPARED_FILE_PATH = 'D:\keppler-classifier\keppler-data-prepared.csv'


def prepare_data():
    # read data from csv. skip first 31 rows which are just in informative purpose
    df = pd.read_csv(ORIGINAL_FILE_PATH, delimiter=",")
    # drop not nesessary columns
    df = drop_unnecessary_columns(df)
    # convert CONFIRMED and FALSE POSITIVE to 1 and 0
    df.koi_disposition.loc[(df.koi_disposition == "CONFIRMED")] = 1
    df.koi_disposition.loc[(df.koi_disposition == "FALSE POSITIVE")] = 0
    # delete CANDIDATES
    df = delete_candidates(df)
    # change hours to decimal degrees
    df['ra_str'] = df['ra_str'].apply(convert_minutes_to_degrees)
    df['dec_str'] = df['dec_str'].apply(convert_minutes_to_degrees)
    # change column names
    df = df.rename(columns={'ra_str': 'ra'})
    df = df.rename(columns={'dec_str': 'dec'})
    # fill empty cells
    df = fill_empty_cells(df)
    save_prepared_data(df)

def save_prepared_data(df):
    df.to_csv(PREPARED_FILE_PATH, index=False, sep=",")

def drop_unnecessary_columns(df):
    df.drop([
        # "kepoi_name", 
        # "kepler_name", 
        'koi_pdisposition', 
        'koi_score',
        'koi_tce_plnt_num', 
        'koi_tce_delivname',
        'koi_prad_err1',
        'koi_prad_err2',
        'koi_teq_err1',
        'koi_teq_err2',
        'koi_insol_err1',
        'koi_insol_err2',
        'koi_steff_err1',
        'koi_steff_err2',
        'koi_period_err1',
        'koi_period_err2',
        'koi_time0bk_err1',
        'koi_time0bk_err2',
        'koi_impact_err1',
        'koi_impact_err2',
        'koi_duration_err1',
        'koi_duration_err2',
        'koi_depth_err1',
        'koi_depth_err2',
        'koi_slogg_err1',
        'koi_slogg_err2',
        'koi_srad_err1',
        'koi_srad_err2',
        'koi_kepmag_err'
        ], 
        axis=1, inplace=True)
    return df

def get_prepared_data():
    data =  pd.read_csv(PREPARED_FILE_PATH, delimiter=",")
    list_of_objects = [(DataVM(
        row.kepid,
        row.kepoi_name,
        row.kepler_name,
        row.koi_disposition,
        row.koi_fpflag_nt,
        row.koi_fpflag_ss,
        row.koi_fpflag_co,
        row.koi_fpflag_ec,
        row.koi_period,
        row.koi_time0bk,
        row.koi_impact,
        row.koi_duration,
        row.koi_depth,
        row.koi_prad,
        row.koi_teq,
        row.koi_insol,
        row.koi_model_snr,
        row.koi_steff,
        row.koi_slogg,
        row.koi_srad,
        row.ra,
        row.dec,
        row.koi_kepmag,
        )) for index, row in data.iterrows() ]  
    for item in list_of_objects:
        item = item.to_json()
    return list_of_objects

def delete_candidates(df):
    df = df[df.koi_disposition != "CANDIDATE"]
    return df

def convert_minutes_to_degrees(value):
    if value[:1] == '+':
        degrees = value[1:3]
        minutes = value[4:6]
        seconds = value[7:9]
        minutes_total = int(degrees) + int(minutes) + int(seconds) / 60
        decimal_degrees = minutes_total / 60
        return decimal_degrees
    else:
        # change format 20h19m20s to 20:19:20
        value = value.replace('m', ':')
        value = value.replace('h', ':')
        value = value.replace('s', ':')
        # remove decimal part of seconds
        value = value.split('.', 1)[0]
        time = datetime.datetime.strptime(value, '%H:%M:%S')
        minutes_total = time.hour * 60 + time.minute + time.second / 60
        decimal_degrees = minutes_total / 60
        return decimal_degrees

def fill_empty_cells(df):
    df.koi_fpflag_nt.fillna(randrange(1), inplace=True)
    df.koi_fpflag_co.fillna(randrange(1), inplace=True)
    df.koi_fpflag_ec.fillna(randrange(1), inplace=True)
    df.koi_fpflag_nt.fillna(randrange(1), inplace=True)
    df.koi_period.fillna(df.koi_period.mean(), inplace=True)
    df.koi_time0bk.fillna(df.koi_time0bk.mean(), inplace=True)
    df.koi_impact.fillna(df.koi_impact.mean(), inplace=True)
    df.koi_duration.fillna(df.koi_duration.mean(), inplace=True)
    df.koi_depth.fillna(df.koi_depth.mean(), inplace=True)
    df.koi_prad.fillna(df.koi_prad.mean(), inplace=True)
    df.koi_teq.fillna(df.koi_teq.mean(), inplace=True)
    df.koi_insol.fillna(df.koi_insol.mean(), inplace=True)
    df.koi_model_snr.fillna(df.koi_model_snr.mean(), inplace=True)
    df.koi_steff.fillna(df.koi_steff.mean(), inplace=True)
    df.koi_slogg.fillna(df.koi_slogg.mean(), inplace=True)
    df.koi_srad.fillna(df.koi_srad.mean(), inplace=True)
    df.ra.fillna(df.ra.mean(), inplace=True)
    df.dec.fillna(df.dec.mean(), inplace=True)
    df.koi_kepmag.fillna(df.koi_kepmag.mean(), inplace=True)
    return df