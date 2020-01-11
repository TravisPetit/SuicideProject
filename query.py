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
            SELECT \
            "name", \
            cast(votesGOP as decimal)/(votesGOP + votesDem + votesOther), \
            S16.deaths, S17.deaths \
            FROM \
            County, ElectionResult, SuicideRate S16, SuicideRate S17 \
            WHERE \
            County.gid = ElectionResult.countyGeoID \
            AND ElectionResult.year = 2016 \
            AND S16.year = 2016 \
            AND S17.year = 2017 \
            AND S16.countyGeoID = ElectionResult.countyGeoID \
            AND S17.countyGeoID = ElectionResult.countyGeoID ;')


def plot_county_suicides_2016_2017(cursor,N, proTrump):
    """
    N = number of counties
    set proTrump to True to plot the suicide rates of conties with high
    GOP votes per capita and to false otherwise
    """

    if proTrump:
        cursor.execute(
            'SELECT * FROM Percent ORDER BY -Protrump LIMIT {};'.format(N))
    else:
        cursor.execute(
            'SELECT * FROM Percent ORDER BY Protrump LIMIT {};'.format(N))

    out = cursor.fetchall()

    x = [2*x for x in range(N)]

    x2 = [i + 0.5 for i in x]
    x3 = [i + 0.25 for i in x]

    s16 = [a[2] for a in out]
    s17 = [a[3] for a in out]

    counties = [a[0] for a in out]
    counties[0] = counties[0].replace("District of Columbia", "DOC")

    fig = plt.figure()
    ax = fig.add_subplot(111)

    bars16 = ax.bar(x, s16, 0.45, color="r")
    bars17 = ax.bar(x2, s17, 0.45, color="g")

    ax.legend((bars16[0], bars17[0]), ("2016", "2017"))

    ax.set_xticks(x3)
    ax.set_xticklabels(counties)
    ax.set_ylabel("# of suicides")

    if proTrump:
        ax.tick_params(axis="x", labelsize = 7)
        ax.set_xlabel("counties with highest GOP votes per capita")
        plt.savefig("pro_trump_counties_suicides_2016_2017.png")
    else:
        ax.tick_params(axis="x", labelsize = 5)
        ax.set_xlabel("counties with lowest GOP votes per capita")
        plt.savefig("anti_trump_counties_suicides_2016_2017.png")

    plt.show()


def plot_pie(cursor, N):
    """
    out of the top N counties that voted the least for trmp, make a
    pie diagram that shows how the suicides of 2016 and 2017 were 
    distributed
    """

    cursor.execute(
    "SELECT AVG(suicide16), AVG(suicide17) FROM \
            (SELECT suicide16, suicide17 FROM Percent ORDER BY \
            Protrump LIMIT {}) AS temp;".format(N))
    out = cursor.fetchall()

    a,b = out[0][0], out[0][1]

    plt.pie(out[0], explode = (0,0.01),
            labels = ("suicides 2016", "suicides 2017"), shadow = False,
            autopct="%2.1f%%", startangle = 34)

    plt.suptitle(
            "Suicide distribution over the avg no. of suicides\n per year of the top {} counties that have had the lowest GOP votes per capita in 2016".format(N), fontsize = 7.5)

    plt.savefig("pie.png")
    plt.show()




N = 10
create_percent_view(cursor)
plot_county_suicides_2016_2017(cursor,N, False)
plot_county_suicides_2016_2017(cursor,N, True)
plot_pie(cursor, 100)
suicides_per_year_plot(cursor)

conn.close()
