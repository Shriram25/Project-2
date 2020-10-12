from flask import Flask
from flask import render_template
from pymongo import  MongoClient
import json
from bson import json_util
##from bson.json import  dumps
import os
import csv
import pandas as pd
#import sys,getopt,pprint

app = Flask(__name__)


# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = MongoClient(conn)

db= client.fortune500db

csvfile = open('data/f500.csv', 'r')
reader = csv.DictReader( csvfile )
print(reader)
#for records in reader:\

 #   print(records)
# db.projects.drop()
#header= [ "_projectid","_teacher_acctid","_schoolid","school_ncesid","school_latitude","school_longitude","school_city","school_state","school_zip","school_metro","school_district","school_county","school_charter","school_magnet","school_year_round","school_nlns","school_kipp","school_charter_ready_promise","teacher_prefix","teacher_teach_for_america","teacher_ny_teaching_fellow","primary_focus_subject","primary_focus_area","secondary_focus_subject","secondary_focus_area","resource_type","poverty_level","grade_level","vendor_shipping_charges","sales_tax","payment_processing_charges","fulfillment_labor_materials","total_price_excluding_optional_support","total_price_including_optional_support","students_reached","total_donations","num_donors","eligible_double_your_impact_match","eligible_almost_home_match","funding_status","date_posted","date_completed","date_thank_you_packet_mailed","date_expiration" ]

db.fortune500.drop()
for row in reader:
    db.fortune500.insert(row)



# END - subprogram insert data to DB

@app.route("/")
def index():
    companies = list(db.fortune500.find())    
    return render_template("index.html",data = companies)

if __name__ == "__main__":
    app.run(debug=True)
