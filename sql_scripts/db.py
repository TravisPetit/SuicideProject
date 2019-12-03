import psycopg2
import csv
import datetime

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
            return None

def db_str(value):
    if value == '':
        return None
    else:
        value

def db_bool(value):
    if value == 1:
        return True
    elif value == 0:
        return False
    else:
        return None

def db_datetime(value, format):
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
        self.Day = row[1]
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

def add_geo(typ, full_name, country_code, adm1_code, adm2_code,
            lat, long, feature_id, cursor):
    cursor.execute('INSERT INTO Geo '
                  + '("type", fullName, countryCode, adm1Code, adm2Code, '
                     + 'coordinates, featureID) '
                  + 'VALUES (%i, %s, %s, %s, %s, %s, %s) '
                  + 'ON CONFLICT idx_geo_type_fullName DO UPDATE SET typ = EXCLUDED.typ '
                  + 'RETURNING id;'
                  , (typ, full_name, country_code, adm1_code, adm2_code,
                      'POINT(%f %f)' % (long, lat), feature_id))
    return cursor.fetchone()[0]

def add_geos(row, cursor):
    (actor1_geo_id, actor2_geo_id, action_geo_id) = (None, None, None)
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
    return (actor1_geo_id, actor2_geo_id, action_geo_id)

ACTION_STR = 'INSERT INTO "Action" \
(id, eventCode, eventRootCode, eventBaseCode, isRootEvent, quadClass, goldsteinScale, avgTone)\
VALUES '


LEN = 163536
i=0
while(i < LEN):
    i+=1
    filename = "../gdelt/files/"  + str(i) + ".csv"
    with open(filename, mode="r") as data:
        reader = csv.reader(data, delimiter ="\t")
        for row in map(GDELTRow, reader):
            print(row)
            (actor1_geo_id, actor2_geo_id, action_geo_id) = add_geos(row, cursor)
            #(actor1_id, actor2_id) = add_actors(row, cursor)
            #action_id = add_action(row, cursor)
            #add_event(row, 
            #       actor1_geo_id, actor2_geo_id, action_geo_id,
            #       actor1_id, actor2_id, action_id)
            '''s_action = "("
            s_action += str(index)  + ","  #id
            s_action += row[26] + ","  #eventCode
            s_action += row[28] + ","  #eventRootCode
            s_action += row[27] + ","  #eventBaseCode
            s_action += row[25] + ","  #isRootEvent
            s_action += row[29] + ","  #quadClass
            s_action += row[30] + ","  #goldstein
            s_action += row[34]        #avgTone
            s_action += ")"
            cursor.execute( ACTION_STR + s_action )
            # ...'''
conn.close()
cursor.close()
