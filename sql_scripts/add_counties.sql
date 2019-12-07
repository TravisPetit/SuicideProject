set search_path to suicide_schema;

DROP TABLE County;
DROP TABLE City;

ALTER TABLE "uscounties"
RENAME TO County;

CREATE TABLE City (
    	geoID INTEGER PRIMARY KEY,
   	countyGID INTEGER,

    	FOREIGN KEY (geoID) REFERENCES Geo (id),
    	FOREIGN KEY (countyGID) REFERENCES County (GID)
);

INSERT INTO City (geoID, countyGID) SELECT id gid FROM Geo join County ON st_covers("geom"::geography, coordinates) WHERE "type" = '3';
