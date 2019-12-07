COUNTY_TO_STATE = {}
with open("../../counties/UScounties.csv", mode="r") as data:
    reader = csv.reader(data, delimiter ="\t")
    skip1 = True
    for row in reader:
        if skip1:
            skip1 = False
            continue
        COUNTY_TO_STATE[row[0].lower()] = row[1].lower()

ABBR_TO_STATE = {
    "AL" : "alabama",
    "AK" : "alaska",
    "AZ" : "arizona",
    "AR" : "arkansas",
    "CA" : "california",
    "CO" : "colorado",
    "CT" : "connecticut",
    "DE" : "delaware",
    "FL" : "florida",
    "GA" : "georgia",
    "HI" : "hawaii",
    "ID" : "idaho",
    "IL" : "illinois",
    "IN" : "indiana",
    "IA" : "iowa",
    "KS" : "kansas",
    "KY" : "kentucky",
    "LA" : "louisiana",
    "ME" : "maine",
    "MD" : "maryland",
    "MA" : "masachusetts",
    "MI" : "michigan",
    "MN" : "minnesota",
    "MS" : "mississippi",
    "MO" : "missouri",
    "MT" : "montana",
    "NE" : "nebraska",
    "NV" : "nevada",
    "NH" : "new hampshire",
    "NJ" : "new jersey",
    "NM" : "new mexico",
    "NY" : "new york",
    "NC" : "north carolina",
    "ND" : "north dakota",
    "OH" : "ohio",
    "OK" : "oklahoma",
    "OR" : "oregon",
    "PA" : "pennsylvania",
    "RI" : "rhode island",
    "SC" : "south carolina",
    "SD" : "south dakota",
    "TN" : "tennessee",
    "TX" : "texas",
    "UT" : "utah",
    "VT" : "vermont",
    "VA" : "virgina",
    "WA" : "washington",
    "WV" : "west virgina",
    "WI" : "wisconsin",
    "WY" : "wyoming",
    "DC" : "district of columbia",
    "MH" : "marshall islands"
    }

STATE_TO_ABBR = {v: k for k, v in ABBR_TO_STATE.iteritems()}

#COUNTY_TO_ADM1 = ???
