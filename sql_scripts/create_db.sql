CREATE SCHEMA suicide_schema;
SET SEARCH_PATH TO suicide_schema;

CREATE EXTENSION postgis;

CREATE TABLE "Action" (
    id SERIAL PRIMARY KEY,
    eventCode VARCHAR(255) NOT NULL,
    eventRootCode VARCHAR(255) NOT NULL,
    eventBaseCode VARCHAR(255) NOT NULL,
    isRootEvent BOOLEAN NOT NULL,
    quadClass INTEGER NOT NULL,
    goldsteinScale REAL NOT NULL
);

CREATE UNIQUE INDEX idx_action_event_code ON "Action" (eventRootCode, eventBaseCode, eventCode);

CREATE TABLE Geo (
    id SERIAL PRIMARY KEY,
    "type" INTEGER NOT NULL,
    fullName VARCHAR(255) NOT NULL,
    countryCode VARCHAR(255) NULL, -- should be 2
    adm1Code VARCHAR(255) NULL, -- should be 4
    adm2Code VARCHAR(255) NULL, -- should be 5
    coordinates GEOGRAPHY(POINT) NULL,
    featureID VARCHAR(255) NOT NULL
);

CREATE UNIQUE INDEX idx_geo_feature_id ON Geo (featureID);
CREATE INDEX idx_geo_coordinates ON Geo USING GIST (coordinates);

CREATE TABLE Actor (
    id SERIAL PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    countryCode VARCHAR(255) NULL, -- should be 3
    knownGroupCode VARCHAR(255) NULL,
    ethnicCode VARCHAR(255) NULL,
    religion1Code VARCHAR(255) NULL,
    religion2Code VARCHAR(255) NULL,
    type1Code VARCHAR(255) NULL,
    type2Code VARCHAR(255) NULL,
    type3Code VARCHAR(255) NULL
);

CREATE UNIQUE INDEX idx_actor_code ON Actor (code, "name");

CREATE TABLE "Event" (
    globalEventID INTEGER PRIMARY KEY,
    dateOccurred DATE NOT NULL,
    actionID INTEGER NOT NULL,
    actor1ID INTEGER NULL,
    actor2ID INTEGER NULL,
    actor1GeoID INTEGER NULL,
    actor2GeoID INTEGER NULL,
    geoID INTEGER NULL,
    avgTone INTEGER NOT NULL,
    numMentions INTEGER NOT NULL,
    numSources INTEGER NOT NULL,
    numArticles INTEGER NOT NULL,

    FOREIGN KEY (actionID) REFERENCES "Action" (id),
    FOREIGN KEY (actor1ID) REFERENCES Actor (id),
    FOREIGN KEY (actor2ID) REFERENCES Actor (id),
    FOREIGN KEY (actor1GeoID) REFERENCES Geo (id),
    FOREIGN KEY (actor2GeoID) REFERENCES Geo (id),
    FOREIGN KEY (geoID) REFERENCES Geo (id)
);

CREATE TABLE "State" (
    geoID INTEGER PRIMARY KEY,

    FOREIGN KEY (geoID) REFERENCES Geo (id)
);

CREATE TABLE County (
    geoID INTEGER PRIMARY KEY,
    stateGeoID INTEGER,

    FOREIGN KEY (geoID) REFERENCES Geo (id),
    FOREIGN KEY (stateGeoID) REFERENCES "State" (geoID)
);

CREATE TABLE City (
    geoID INTEGER PRIMARY KEY,
    countyGeoID INTEGER,

    FOREIGN KEY (geoID) REFERENCES Geo (id),
    FOREIGN KEY (countyGeoID) REFERENCES County (geoID)
);

CREATE TABLE SuicideRate (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    "population" INTEGER NOT NULL,
    deaths INTEGER NOT NULL,
    crudeRate REAL NULL,
    ageAdjustedRate REAL NULL,
    countyGeoID INTEGER NOT NULL,

    FOREIGN KEY (countyGeoID) REFERENCES County (geoID) 
);

CREATE UNIQUE INDEX suicide_rate_county_year ON SuicideRate (year, countyGeoID);

CREATE TABLE ElectionResult (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    votesDem INTEGER NOT NULL,
    votesGOP INTEGER NOT NULL,
    votesOther INTEGER NOT NULL,
    countyGeoID INTEGER NOT NULL,

    FOREIGN KEY (countyGeoID) REFERENCES County (geoID) 
);

CREATE UNIQUE INDEX election_result_county_year ON ElectionResult (year, countyGeoID);
