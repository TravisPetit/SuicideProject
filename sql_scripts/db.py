import psycopg2
import csv

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

ACTION_STR = 'INSERT INTO "Action" \
(id, eventCode, eventRootCode, eventBaseCode, isRootEvent, quadClass, goldsteinScale, avgTone)\
VALUES '


LEN = 163536
i=0
while(i < LEN):
    i+=1
    filename = "../gdelt/files/"  + str(i) + ".csv"
    index = 0
    with open(filename, mode="r") as data:
        reader = csv.reader(data, delimiter ="\t")
        for row in reader:
            index+=1
            print(row)
            s_action = "("
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
            # ...
conn.close()
cursor.close()
