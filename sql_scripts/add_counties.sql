set search_path to suicide_schema;

insert into City (geoID, countyGID) select id gid from Geo join County on st_covers("geom"::geography, coordinates) where "type" = '3';
