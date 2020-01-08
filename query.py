import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="postgres",
    password="123"
)

cursor = conn.cursor()

cursor.execute(
        "select year, sum(deaths) from suiciderate group by year order by year;")
out = cursor.fetchall()

conn.close()

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
