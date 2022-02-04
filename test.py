import json

with open("sample.json", "r", encoding="utf-8") as sf:
    data = json.load(sf)

daily_pcr_testing_data = data["data"]["daily_pcr_testing_data"]
daily_antigen_testing_data = data["data"]["daily_antigen_testing_data"]

new_dict = {}
# for pcr in daily_pcr_testing_data:
#     for anti in daily_antigen_testing_data:
#         new_dict[pcr["date"]] = {"pcr": pcr["pcr_count"],
#                                  "antigen": anti["antigen_count"]}


def mergeDictionary(dict_1, dict_2):
    dict_3 = {**dict_1, **dict_2}
    for key, value in dict_3.items():
        if key in dict_1 and key in dict_2:
            dict_3[key] = [value, dict_1[key]]
    return dict_3


for i, j in (daily_pcr_testing_data, daily_antigen_testing_data):
    dict_3 = mergeDictionary(i, j)

for k, v in dict_3.items():
    print(k, v)

# print(daily_antigen_testing_data)
