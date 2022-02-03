import os
import sys

import requests
from flask import Flask, render_template


app = Flask(__name__)
API_LINK = r"https://www.hpb.health.gov.lk/api/get-current-statistical"


@app.route("/")
def index():
    rdata = requests.get(API_LINK).json()

    if rdata["success"] != True:
        return "Error in API"

    last_updated_time = rdata["data"]["update_date_time"]

    today_new_cases = rdata["data"]["local_new_cases"]
    today_new_deaths = rdata["data"]["local_new_deaths"]

    total_active_cases = rdata["data"]["local_active_cases"]
    total_cases = rdata["data"]["local_total_cases"]
    total_individuals_in_hospitals = rdata["data"]["local_total_number_of_individuals_in_hospitals"]
    total_deaths = rdata["data"]["local_deaths"]
    total_recovered = rdata["data"]["local_recovered"]
    total_pcr_testing_count = rdata["data"]["total_pcr_testing_count"]

    return render_template("index.html",
                           last_updated_time=last_updated_time,
                           today_new_cases=today_new_cases,
                           today_new_deaths=today_new_deaths,
                           total_active_cases=total_active_cases,
                           total_cases=total_cases,
                           total_individuals_in_hospitals=total_individuals_in_hospitals,
                           total_deaths=total_deaths,
                           total_recovered=total_recovered,
                           total_pcr_testing_count=total_pcr_testing_count
                           )


@app.route("/more")
def more():
    return "This will be updated in the future"


if __name__ == "__main__":
    app.run("0.0.0.0", port=3336, debug=True)
