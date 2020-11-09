import csv
import sys
from typing import Optional

from step_03_run_server.const import POOL_NAME, UTILIZATION_TODAY, UTILIZATION_TOMORROW, ADDRESS, DISTRICT, TOMORROW
from step_03_run_server.district_utils import district_zip_mapping, district_name_mapping, word_sim, THRESHOLD_SIMILARITY

sys.path.append('./')


class PoolData:
    def __init__(self):
        self.pool_data = []

        with open('../input_data/SCHWIMMBADOGD.csv', newline='') as csvfile:
            pool_data_tmp = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in pool_data_tmp:
                if i == 0:
                    i = i + 1
                    continue

                print('row ' + str(i) + "     ")
                for f in row:
                    print("field    {}".format(f))

                # print('row ' + str(i) +
                #       '     name:  ' + row[POOL_NAME] + ' \n       address: ' + row[ADDRESS] + ',  district:   "' + row[
                #           DISTRICT] + '", auslastung_today   "' +
                #       row[AUSLASTUNG_TODAY] + '", auslastung_tomorrow     "' +
                #       row[AUSLASTUNG_TOMORROW] + '"')

                pos_comma = row[ADDRESS].find(",")
                add = row[ADDRESS][pos_comma + 1:].strip()
                dist = district_zip_mapping[row[DISTRICT]]
                entry = {
                    'name': row[POOL_NAME],
                    'address': add,
                    'district': str(dist),
                    'utilization_today': row[UTILIZATION_TODAY],
                    'utilization_tomorrow': row[UTILIZATION_TOMORROW]
                }
                print("entry: {}".format(entry))

                self.pool_data.append(entry)

        # for p in self.pool_data:
        #     print('name:  ' + p["name"] + ' \n       address: ' + p["address"] + ',  district:   "' + str(
        #         p["district"]) + '", "utilization"_today:  "' +
        #           p["utilization_today"] + '", "utilization"_tomorrow:  "' + p["utilization_tomorrow"] + '"')

    def findByDistrict(self, district):
        pass

    def get_pools_for_day_and_district(self, day: str, district: str) -> Optional[str]:
        print("get_pools_for_day_and_district()  day: {}, district: {} ".format(day, district))
        pools = []

        max_sim = 0
        zip_code = ""
        for d, zipcode in district_name_mapping.items():
            sim = word_sim(d.lower(), district.lower())
            if sim > max_sim:
                zip_code = zipcode
                max_sim = sim
        if max_sim < THRESHOLD_SIMILARITY:
            return None

        for p in self.pool_data:
            print("comparing p[district] = {}   with zip_code = {}".format(p["district"], zip_code))
            if str(p["district"]) == str(zip_code):
                print("found district   '{}'".format(district))
                entry = {
                    "name": p["name"],
                    "address": p["address"],
                    "utilization": ""
                }

                if str(day.lower()) == str(TOMORROW):
                    entry["utilization"] = p["utilization_tomorrow"]
                else:
                    entry["utilization"] = p["utilization_today"]

                pools.append(entry)

        resp = ""
        if len(pools) < 1:
            return None
        else:
            for p in pools:
                tmp = ""
                for key, value in p.values():
                    tmp = tmp + " " + key + ": " + value
                resp = resp + tmp + "\n"

        return resp
