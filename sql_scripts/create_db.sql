CREATE SCHEMA suicide_schema;
SET SEARCH_PATH TO suicide_schema;

CREATE EXTENSION postgis;

CREATE TABLE "Action" (
    id BIGSERIAL PRIMARY KEY,
    eventCode VARCHAR(255) NOT NULL,
    eventRootCode VARCHAR(255) NOT NULL,
    eventBaseCode VARCHAR(255) NOT NULL,
    isRootEvent BOOLEAN NULL, -- NN
    quadClass INTEGER NULL, -- NN
    goldsteinScale REAL NULL -- NN
);

CREATE UNIQUE INDEX idx_action_event_code ON "Action" (eventRootCode, eventBaseCode, eventCode);

CREATE TABLE Geo (
    id BIGSERIAL PRIMARY KEY,
    "type" INTEGER NULL, -- NN
    fullName VARCHAR(255) NULL,
    countryCode VARCHAR(255) NULL, -- should be 2
    adm1Code VARCHAR(255) NULL, -- should be 4
    adm2Code VARCHAR(255) NULL, -- should be 5
    coordinates GEOGRAPHY(POINT) NULL,
    featureID VARCHAR(255) NOT NULL
);

CREATE UNIQUE INDEX idx_geo_feature_id ON Geo (featureID);
CREATE INDEX idx_geo_coordinates ON Geo USING GIST (coordinates);

CREATE TABLE Actor (
    id BIGSERIAL PRIMARY KEY,
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
    globalEventID BIGINT PRIMARY KEY,
    dateOccurred DATE NULL, -- NN
    actionID BIGINT NOT NULL,
    actor1ID BIGINT NULL,
    actor2ID BIGINT NULL,
    actor1GeoID BIGINT NULL,
    actor2GeoID BIGINT NULL,
    geoID BIGINT NULL,
    avgTone INTEGER NULL, -- NN
    numMentions INTEGER NULL, -- NN
    numSources INTEGER NULL, -- NN
    numArticles INTEGER NULL, -- NN

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

--CREATE TABLE County (
--    geoID INTEGER PRIMARY KEY,
--    stateGeoID INTEGER,
--
--    FOREIGN KEY (geoID) REFERENCES Geo (id),
--    FOREIGN KEY (stateGeoID) REFERENCES "State" (geoID)
--);

CREATE TABLE County (
    gid SERIAL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL,
    fips VARCHAR(5) NOT NULL,
    stateGeoID INTEGER NULL,
    
    FOREIGN KEY (stateGeoID) REFERENCES "State" (geoID)
);

SELECT AddGeometryColumn('', 'County', 'geom', '0', 'MULTIPOLYGON', 2);

CREATE TABLE City (
    geoID INTEGER PRIMARY KEY,
   	countyGID INTEGER,

    FOREIGN KEY (geoID) REFERENCES Geo (id),
    FOREIGN KEY (countyGID) REFERENCES County (GID)
);

CREATE TABLE SuicideRate (
    id BIGSERIAL PRIMARY KEY,
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
    id BIGSERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    votesDem INTEGER NOT NULL,
    votesGOP INTEGER NOT NULL,
    votesOther INTEGER NOT NULL,
    countyGeoID INTEGER NOT NULL,

    FOREIGN KEY (countyGeoID) REFERENCES County (geoID) 
);

CREATE UNIQUE INDEX election_result_county_year ON ElectionResult (year, countyGeoID);
