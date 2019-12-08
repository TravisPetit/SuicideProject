import psycopg2
import csv
import datetime
#from constants import COUNTY_TO_STATE, ABBR_TO_STATE, STATE_TO_ABBR

conn = psycopg2.connect(
	host="localhost",
	user="postgres",
        database="postgres",
	password="123"
        )

cursor = conn.cursor()
cursor.execute("SET search_path TO suicide_schema")

#DATA FORMATING:
#The csv files contain:
#0  A.  GlobalEventID (int)
#1  B.  Day (int)
#2  C.  MonthYear (int)
#3  D.  Year (int)
#4  E.  FractionDate (float)
#5  F.  Actor1Code (string)
#6  G.  Actor1Name (string)
#7  H.  Actor1CountryCode (string)
#8  I.  Actor1KnownGroupCode (string)
#9  J.  Actor1EthnicCode (string)
#10 K.  Actor1Religion1Code (string)
#11 L.  Actor1Religion2Code (string)
#12 M.  Actor1Type1Code (string)
#13 N.  Actor1Type2Code (string)
#14 O.  Actor1Type3Code (string)
#15 P.  Actor2Code (string)
#16 Q.  Actor2Name (string)
#17 R.  Actor2CountryCode (string)
#18 S.  Actor2KnownGroupCode (string)
#19 T.  Actor2EthnicCode (string)
#20 U.  Actor2Religion1Code (string)
#21 V.  Actor2Religion2Code (string)
#22 W.  Actor2Type1Code (string)
#23 X.  Actor2Type2Code (string)
#24 Y.  Actor2Type3Code (string)
#25 Z.  IsRootEvent (int) 1 true, 0 false
#26 AA. EventCode (string)
#27 AB. EventBaseCode (string)
#28 AC. EventRootCode (string)
#29 AD. QuadClass (int)
#30 AE. GoldsteinScale (float)
#31 AF. NumMentions (int)
#32 AG. NumSources (int)
#33 AH. NumArticles (int)
#34 AI. AvgTone (float)
#35 AJ. Actor1Geo_Type (int)
#36 AK. Actor1Geo_FullName (string)
#37 AL. Actor1Geo_CountryCode (string)
#38 AM. Actor1Geo_ADM1Code (string)
#39 AN. Actor1Geo_ADM2Code (string)
#40 AO. Actor1Geo_Lat (float)
#41 AP. Actor1Geo_Long (float)
#42 AQ. Actor1Geo_FeatureID (string)
#43 AR. Actor2Geo_Type (int)
#44 AS. Actor2Geo_FullName (string)
#45 AT. Actor2Geo_CountryCode (string)
#46 AU. Actor2Geo_ADM1Code (string)
#47 AV. Actor2Geo_ADM2Code (string)
#48 AW. Actor2Geo_Lat (float)
#49 AX. Actor2Geo_Long (float)
#50 AY. Actor2Geo_FeatureID (string)
#51 AZ. ActionGeo_Type (int)
#52 BA. ActionGeo_FullName (string)
#53 BB. ActionGeo_CountryCode (string)
#54 BC. ActionGeo_ADM1Code (string)
#55 BD. ActionGeo_ADM2Code (string)
#56 BE. ActionGeo_Lat (float)
#57 BF. ActionGeo_Long (float)
#58 BG. ActionGeo_FeatureID (string)
#59 BH. DateAdded (int)
#60 BI. SourceURL (string)
#61 BJ. Gibberish
#62 BK. Gibberish
#63 BL. Gibberish
#64 BM. Giggerish
#65 BN. Gibberigh
#66 BO. Gibberish
#61 BJ. Gibberish
#62 BK. Gibberish
#63 BL. Gibberish
#64 BM. Giggerish
#65 BN. Gibberigh
#66 BO. Gibberish

def db_int(value):
    if value == '':
        return None
    else:
        try:
            return int(value)
        except ValueError:
            return None

def db_float(value):
    if value == '':
        return None
    else:
        try:
            return float(value)
        except ValueError:
            print('badly formatted float:', value)
            exit()
            return None

def db_str(value):
    if value == '':
        return None
    else:
        return value

def db_bool(value):
    if value == '1':
        return True
    elif value == '0':
        return False
    else:
        return None

def db_datetime(value):
    if value == '':
        return None
    else:
        try:
            return datetime.datetime.strptime(value, '%Y%m%d')
        except ValueError:
            return None

class GDELTRow:
    def __init__(self, row):
        self.GlobalEventID = db_int(row[0])
        self.Day = db_datetime(row[1])
        self.Actor1Code = db_str(row[5])
        self.Actor1Name = db_str(row[6])
        self.Actor1CountryCode = db_str(row[7])
        self.Actor1KnownGroupCode = db_str(row[8])
        self.Actor1EthnicCode = db_str(row[9])
        self.Actor1Religion1Code = db_str(row[10])
        self.Actor1Religion2Code = db_str(row[11])
        self.Actor1Type1Code = db_str(row[12])
        self.Actor1Type2Code = db_str(row[13])
        self.Actor1Type3Code = db_str(row[14])
        self.Actor2Code = db_str(row[15])
        self.Actor2Name = db_str(row[16])
        self.Actor2CountryCode = db_str(row[17])
        self.Actor2KnownGroupCode = db_str(row[18])
        self.Actor2EthnicCode = db_str(row[19])
        self.Actor2Religion1Code = db_str(row[20])
        self.Actor2Religion2Code = db_str(row[21])
        self.Actor2Type1Code = db_str(row[22])
        self.Actor2Type2Code = db_str(row[23])
        self.Actor2Type3Code = db_str(row[24])
        self.IsRootEvent = db_bool(row[25])
        self.EventCode = db_str(row[26])
        self.EventBaseCode = db_str(row[27])
        self.EventRootCode = db_str(row[28])
        self.QuadClass = db_int(row[29])
        self.GoldsteinScale = db_float(row[30])
        self.NumMentions = db_int(row[31])
        self.NumSources = db_int(row[32])
        self.NumArticles = db_int(row[33])
        self.AvgTone = db_float(row[34])
        self.Actor1Geo_Type = db_int(row[35])
        self.Actor1Geo_FullName = db_str(row[36])
        self.Actor1Geo_CountryCode = db_str(row[37])
        self.Actor1Geo_ADM1Code = db_str(row[38])
        self.Actor1Geo_ADM2Code = db_str(row[39])
        self.Actor1Geo_Lat = db_float(row[40])
        self.Actor1Geo_Long = db_float(row[41])
        self.Actor1Geo_FeatureID = db_str(row[42])
        self.Actor2Geo_Type = db_int(row[43])
        self.Actor2Geo_FullName = db_str(row[44])
        self.Actor2Geo_CountryCode = db_str(row[45])
        self.Actor2Geo_ADM1Code = db_str(row[46])
        self.Actor2Geo_ADM2Code = db_str(row[47])
        self.Actor2Geo_Lat = db_float(row[48])
        self.Actor2Geo_Long = db_float(row[49])
        self.Actor2Geo_FeatureID = db_str(row[50])
        self.ActionGeo_Type = db_int(row[51])
        self.ActionGeo_FullName = db_str(row[52])
        self.ActionGeo_CountryCode = db_str(row[53])
        self.ActionGeo_ADM1Code = db_str(row[54])
        self.ActionGeo_ADM2Code = db_str(row[55])
        self.ActionGeo_Lat = db_float(row[56])
        self.ActionGeo_Long = db_float(row[57])
        self.ActionGeo_FeatureID = db_str(row[58])

# The county_votes.csv file contains:
# 0  A index (int)
# 1  B combined_fips (int)
# 2  C votes_dem_2016 (int)
# 3  D votes_gop_2016 (int)
# 4  E toatl_votes_2016 (int)
# 5  F per_dem_2016 (float)
# 6  G per_gop (float)
# 7  H diff_2016 (int)
# 8  I per_point_diff_2016 (float)
# 9  J state_abbr (string)
# 10 K county_name (string)
# 11 L FIPS (int)
# 12 M total_votes_2012 (int)
# 13 N votes_dem_2012 (int)
# 14 O votes_gop_2012 (int)
# 15 P county_fips (int)
# 16 Q state_fips (int)
# 17 R per_dem_2012 (float)
# 18 S per_gop_2012 (float)
# 19 T diff_2012 (int)
# 20 U per_point_diff_2012 (float)

class CountyVotesRow:
    def __init__(self, row):
        self.fips = db_str(row[11])

        self.votes_dem_2016 = db_int(row[2])
        self.votes_gop_2016 = db_int(row[3])
        self.votes_other_2016 = db_int(row[4] - row[3] - row[2])

        self.votes_dem_2012 = db_int(row[13])
        self.votes_gop_2012 = db_int(row[14])
        self.votes_other_2016 = db_int(row[12] - row[13] - row[14])

        self.county = db_str(row[10].lower())
        #self.state = db_str(COUNTY_TO_STATE[row[10].lower()])

def county_to_geo_id(county_str, cursor):
    cursor.execute('SELECT id FROM Geo JOIN County ON st_covers("geom"::geography, coordinates) WHERE "name"= %s LIMIT 1', (county_str))
    return cursor.fetchone()[0]


def state_to_geo_id(state_str, cursor):
    cursor.execute('SELECT id FROM Geo JOIN County ON st_covers("geom"::geography, coordinates) WHERE "state_name"= %s LIMIT 1', (state_str))
    return cursor.fetchone()[0]


def add_election_result(year, votes_dem, votes_gop, votes_other, county_geo_id, cursor):
    cursor.execute('INSERT INTO ElectionResult '
                   + '(year, votesDem, votesGOP, votesOther, countyGeoID) '
                   + 'VALUES (%s, %s, %s, %s, %s)'
                   , (year, votes_dem, votes_gop, votes_other, county_geo_id))


def add_election_results(row, cursor):
    add_election_result(2016, row.votes_dem_2016, row.votes_gop_2016, row.votes_other_2016, county_to_geo_id(row.county))
    add_election_result(2012, row.votes_dem_2012, row.votes_gop_2012, row.votes_other_2012, county_to_geo_id(row.county))


# the underlying cause of death file contains
# 0. Notes (string)
# 1. County, State abbr (string)
# 2. County Code (string)
# 3. year (int)
# 4. YearCode (int)
# 5. deaths (int)
# 6. population (int)
# 7. Crude rate (float)
# 8. Age adjusted rate (float)

class UnderlyingCauseOfDeathRow:
    def __init__(self, row):
        self.county = db_str(row[1].split(",")[0].splice())
        self.year = db_int(row[3])
        self.deaths = db_int(row[5])
        self.population = db_int(row[6])
        self.crude_rate = db_str(row[7])
        self.age_adjusted_rate = db_str(row[8])


def add_suicide_rate(year, population, deaths, crude_rate, age_adjusted_rate, county_geo_id, cursor):
    cursor.execute('INSERT INTO SuicideRate '
                   + '(year, "population", deaths, crudeRate, ageAdjustedRate, countyGeoID) '
                   + 'VALUES '
                   + '(%s, %s, %s, %s, %s, %s)', (year, population, deaths, crude_rate, age_adjusted_rate, county_geo_id))


def add_suicide_rates(row, cursor):
    geoID = county_to_geo_id(row.county)
    add_suicide_rate(row.year, row.population, row.deaths, row.crude_rate, row.age_adjusted_rate, geoID, cursor)


#def add_state(state_str, cursor):
#    cursor.execute('INSERT INTO "STATE" VALUES (geoID) (SELECT id FROM Geo WHERE adm1Code = %s LIMIT 1)', (STATE_TO_ABBR[state_str]))


#def add_county(fips, county_str, cursor):
#    cursor.execute('INSERT INTO County VALUES (fips, geoID, stateGeoID) '
#                   + '(%s, SELECT id FROM Geo WHERE adm2Code = %s LIMIT 1, SELECT id from Geo WHERE adm1Code = %s LIMIT 1)',
#                   (fips, COUNTY_TO_ADM1[county_str], STATE_TO_ABBR[COUNTY_TO_STATE[county_str]]))


def add_geo(typ, full_name, country_code, adm1_code, adm2_code,
            lat, lon, feature_id, cursor):
    cursor.execute('INSERT INTO Geo '
                  + '("type", fullName, countryCode, adm1Code, adm2Code, '
                     + 'coordinates, featureID) '
                  + 'VALUES (%s, %s, %s, %s, %s, %s, %s) '
                  + 'ON CONFLICT (featureID) DO UPDATE SET "type" = EXCLUDED."type" '
                  + 'RETURNING id;'
                  , (typ, full_name, country_code, adm1_code, adm2_code,
                      None if lon is None else 'POINT({} {})'.format(lon, lat), feature_id))
    return cursor.fetchone()[0]

def add_geos(row, cursor):
    actor1_geo_id, actor2_geo_id, action_geo_id = None, None, None
    if row.Actor1Geo_Type is not None and row.Actor1Geo_Type != 0:
        actor1_geo_id = add_geo(row.Actor1Geo_Type, row.Actor1Geo_FullName,
                row.Actor1Geo_CountryCode, row.Actor1Geo_ADM1Code,
                row.Actor1Geo_ADM2Code, row.Actor1Geo_Lat,
                row.Actor1Geo_Long, row.Actor1Geo_FeatureID,
                cursor)
    if row.Actor2Geo_Type is not None and row.Actor2Geo_Type != 0:
        actor2_geo_id = add_geo(row.Actor2Geo_Type, row.Actor2Geo_FullName,
                row.Actor2Geo_CountryCode, row.Actor2Geo_ADM1Code,
                row.Actor2Geo_ADM2Code, row.Actor2Geo_Lat,
                row.Actor2Geo_Long, row.Actor2Geo_FeatureID,
                cursor)
    if row.ActionGeo_Type is not None and row.ActionGeo_Type != 0:
        action_geo_id = add_geo(row.ActionGeo_Type, row.ActionGeo_FullName,
                row.ActionGeo_CountryCode, row.ActionGeo_ADM1Code,
                row.ActionGeo_ADM2Code, row.ActionGeo_Lat,
                row.ActionGeo_Long, row.ActionGeo_FeatureID,
                cursor)
    return actor1_geo_id, actor2_geo_id, action_geo_id

def add_actor(code, name, country_code, known_group_code,
        ethnic_code, religion1_code, religion2_code,
        type1_code, type2_code, type3_code, cursor):
    cursor.execute('INSERT INTO Actor '
                  + '(code, "name", countryCode, knownGroupCode, ethnicCode, '
                     + 'religion1Code, religion2Code, type1Code, type2Code, type3Code) '
                  + 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '
                  + 'ON CONFLICT (code, "name") DO UPDATE SET code = EXCLUDED.code '
                  + 'RETURNING id;'
                  , (code, name, country_code, known_group_code,
                        ethnic_code, religion1_code, religion2_code,
                        type1_code, type2_code, type3_code))
    return cursor.fetchone()[0]

def add_actors(row, cursor):
    actor1_id, actor2_id = None, None
    if row.Actor1Code is not None:
        actor1_id = add_actor(row.Actor1Code, row.Actor1Name,
                row.Actor1CountryCode, row.Actor1KnownGroupCode,
                row.Actor1EthnicCode, row.Actor1Religion1Code,
                row.Actor1Religion2Code, row.Actor1Type1Code,
                row.Actor1Type2Code, row.Actor1Type3Code,
                cursor)

    if row.Actor2Code is not None:
        actor2_id = add_actor(row.Actor2Code, row.Actor2Name,
                row.Actor2CountryCode, row.Actor2KnownGroupCode,
                row.Actor2EthnicCode, row.Actor2Religion1Code,
                row.Actor2Religion2Code, row.Actor2Type1Code,
                row.Actor2Type2Code, row.Actor2Type3Code,
                cursor)
    return actor1_id, actor2_id

def add_action(row, cursor):
    cursor.execute('INSERT INTO "Action" '
                  + '(eventCode, eventRootCode, eventBaseCode, isRootEvent, quadClass, goldsteinScale) '
                  + 'VALUES (%s, %s, %s, %s, %s, %s) '
                  + 'ON CONFLICT (eventRootCode, eventBaseCode, eventCode) DO UPDATE SET goldsteinScale = EXCLUDED.goldsteinScale '
                  + 'RETURNING id;'
                  , (row.EventCode, row.EventRootCode, row.EventBaseCode, row.IsRootEvent, row.QuadClass, row.GoldsteinScale))
    return cursor.fetchone()[0]

def add_event(row, cursor,
        actor1_geo_id, actor2_geo_id, action_geo_id,
        actor1_id, actor2_id, action_id):
    cursor.execute('INSERT INTO "Event" '
                  + '(globalEventID, dateOccurred, actionID, actor1ID, actor2ID, actor1GeoID, actor2GeoID, '
                      + 'geoID, avgTone, numMentions, numSources, numArticles)'
                  + 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
                  , (row.GlobalEventID, row.Day, action_id, actor1_id, actor2_id, action_geo_id, actor1_geo_id, actor2_geo_id,
                        row.AvgTone, row.NumMentions, row.NumSources, row.NumArticles))

with open("./underlying_cause_of_death.txt") as data:
    reader = csv.reader(data, delimiter = "\t")
    limit = 1
    for row in reader:
        limit +=1
        print(row)
        if limit == 10:
            break

with open("../../counties/county_votes.csv") as data:
    reader = csv.reader(delimiter = ",")
    for row in map(CountyVotesRow, reader):
        add_election_results(row, cursor)

LEN = 163536
for i in range(LEN):

    filename = "../../gdelt/files/"  + str(i) + ".csv"

    try:
        with open(filename, mode="r") as data:
            reader = csv.reader(data, delimiter ="\t")
            for row in map(GDELTRow, reader):
                actor1_geo_id, actor2_geo_id, action_geo_id = add_geos(row, cursor)
                actor1_id, actor2_id = add_actors(row, cursor)
                action_id = add_action(row, cursor)
                add_event(row, cursor,
                       actor1_geo_id, actor2_geo_id, action_geo_id,
                       actor1_id, actor2_id, action_id)
        if i%500 == 0:
            time = str(datetime.datetime.now().time().replace(microsecond=0))
            print(time + "   " + str(i) + " / " + str(LEN))

    except IOError as e:
        print("Skipping file " + str(i) + ".csv")
        continue

    conn.commit()

cursor.close()
conn.close()
