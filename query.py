import psycopg2
import matplotlib.pyplot as plt
import numpy as np

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="postgres",
    password="123"
)

cursor = conn.cursor()


def suicides_per_year_plot(cursor):
    cursor.execute(
        "select year, sum(deaths) from suiciderate group by year order by year;")
    out = cursor.fetchall()

    years = [x for x in range(1999, 2018)]

    # only shows the numbwers 1999 to 2017 in x axis
    plt.xticks(years)

    # make the font of the x axis smaller
    plt.tick_params(axis="x", which="major", labelsize = 7)

    #plot stuff
    plt.bar(years, height=[A[1] for A in out])
    plt.xlabel("years")
    plt.ylabel("# suicides in the US")

    plt.savefig("suicides.png")
    plt.show()


def create_percent_view(cursor):
    cursor.execute(
            'CREATE VIEW Percent (County, Protrump, suicide16, suicide17) AS \
            SELECT "name", cast(votesGOP as decimal)/(votesGOP+votesDem+votesOther), \
            S16.deaths, S17.deaths \
            FROM County, ElectionResult, SuicideRate S16, SuicideRate S17 \
            WHERE \
            County.gid = ElectionResult.countyGeoID \
            AND S16.year = 2016 \
            AND S17.year = 2017 \
            AND S16.countyGeoID = ElectionResult.countyGeoID \
            AND S17.countyGeoID = ElectionResult.countyGeoID;')

    cursor.execute(
            'SELECT * FROM Percent ORDER BY Protrump LIMIT 10;')
    out = cursor.fetchall()
    print(out)

    x = [2*x for x in range(10)]

    x2 = [i + 0.5 for i in x]
    x3 = [i + 0.25 for i in x]

    s16 = [a[2] for a in out]
    s17 = [a[3] for a in out]
    counties = [a[0] for a in out]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    bars16 = ax.bar(x, s16, 0.45, color="r")
    bars17 = ax.bar(x2, s17, 0.45, color="g")

    ax.legend((bars16[0], bars17[0]), ("2016", "2017"))

    ax.set_xticks(x3)
    ax.set_xticklabels(counties)
    ax.tick_params(axis="x", labelsize = 5)
    ax.set_xlabel("counties with lowest GOP votes per capita")
    ax.set_ylabel("suicides")

    plt.savefig("anti_trump_counties_suicides_2016_2017.png")
    plt.show()


create_percent_view(cursor)

conn.close()
