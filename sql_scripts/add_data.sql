set search_path to suicide_schema;

COPY "Event"(
	GlobalEventID,
       	Day,
       	NumSources,
       	NumMentions,
       	NumArticles,
	SourceURL)
FROM
'/home/travis/SuicideProject/gdelt/test.csv' WITH (FORMAT CSV);
