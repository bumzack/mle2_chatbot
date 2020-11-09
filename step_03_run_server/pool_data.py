import csv
import sys
from typing import Optional

from step_03_run_server.const import POOL_NAME, AUSLASTUNG_TODAY, AUSLASTUNG_TOMORROW, ADDRESS, DISTRICT, TOMORROW
from step_03_run_server.zip_mapping import district_zip_mapping, district_name_mapping

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

                print('row ' + str(i) +
                      '     name:  ' + row[POOL_NAME] + ' \n       address: ' + row[ADDRESS] + ',  district:   "' + row[
                          DISTRICT] + '", auslastung_today' +
                      row[AUSLASTUNG_TODAY] + '", auslastung_to,morrow' +
                      row[AUSLASTUNG_TOMORROW])

                pos_comma = row[ADDRESS].find(",")
                add = row[ADDRESS][pos_comma + 1:].strip()
                dist = district_zip_mapping[row[DISTRICT]]
                entry = {
                    'name': row[POOL_NAME],
                    'address': add,
                    'district': str(dist),
                    'auslastung_today': row[AUSLASTUNG_TODAY],
                    'auslastung_tomorrow': row[AUSLASTUNG_TOMORROW]
                }
                print("entry: {}".format(entry))

                self.pool_data.append(entry)

        for p in self.pool_data:
            print('name:  ' + p["name"] + ' \n       address: ' + p["address"] + ',  district:   "' + str(p[
                                                                                                              "district"]) + '", auslastung_today:  ' +
                  p["auslastung_today"] + '", auslastung_tomorrow' + p["auslastung_tomorrow"] + '')

    def findByDistrict(self, district):
        pass

    def get_pools_for_day_and_district(self, day: str, district: str) -> Optional[str]:
        print("get_pools_for_day_and_district()  day: {}, district: ".format(day, district))
        pools = []
        for p in self.pool_data:
            district = district_name_mapping[district]
            if p["district"] == district:
                print("found district   '{}'".format(district))
                entry = {
                    "name": p["name"],
                    "address": p["address"],
                }
                if day == TOMORROW:
                    entry["auslastung"] = p[AUSLASTUNG_TOMORROW]
                else:
                    entry["auslastung"] = p[AUSLASTUNG_TODAY]

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
