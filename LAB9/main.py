import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Percyy46..",
    database="sys"
)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS mcu_movies
             (ID INT PRIMARY KEY NOT NULL,
             MOVIE TEXT NOT NULL,
             DATE TEXT NOT NULL,
             MCU_PHASE TEXT NOT NULL)''')

data = '''1 IronMan May2,2008 Phase1
2 TheIncredibleHulk June13,2008 Phase1
3 IronMan2 May7,2010 Phase1
4 Thor May6,2011 Phase1
5 CaptainAmerica:TheFirstAvenger July22,2011 Phase1
6 Marvel'sTheAvengers May4,2012 Phase1
7 IronMan3 May3,2013 Phase2
8 Thor:TheDarkWorld November8,2013 Phase2
9 CaptainAmerica:TheWinterSoldier April4,2014 Phase2
10 GuardiansoftheGalaxy August1,2014 Phase2
11 Avengers:AgeofUltron May1,2015 Phase2
12 Ant-Man July17,2015 Phase2
13 CaptainAmerica:CivilWar May6,2016 Phase3
14 DoctorStrange November4,2016 Phase3
15 GuardiansoftheGalaxyVol.2 May5,2017 Phase3
16 Spider-Man:Homecoming July7,2017 Phase3
17 Thor:Ragnarok November3,2019 Phase3
18 BlackPanther February16,2018 Phase3
19 Avengers:Infinity War April27,2018 Phase3
20 Ant-ManandtheWasp July6,2018 Phase3
21 CaptainMarvel March8,2019 Phase3
22 Avengers:Endgame April26,2019 Phase3'''

for line in data.split('\n'):
    id_, movie, date_, phase = line.split(maxsplit=3)
    c.execute("INSERT INTO mcu_movies VALUES (%s, %s, %s, %s)", (id_, movie, date_, phase))

conn.commit()
conn.close()
