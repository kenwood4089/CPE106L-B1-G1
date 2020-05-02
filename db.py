import sqlite3

conn = sqlite3.connect('ADVENTURE_TRIP.db')
c = conn.cursor()
c.execute("""
            CREATE TABLE IF NOT EXISTS ADVENTURE_TRIP(
            TRIP_ID DECIMAL(3,0) PRIMARY KEY,
            TRIP_NAME VARCHAR(100),
            START_LOCATION CHAR(50),
            STATE CHAR(2),
            DISTANCE NUMERIC(4,0),
            MAX_GROUP_SIZE NUMERIC(4,0),
            TYPE CHAR(50),
            SEASON CHAR(50) )""")

c.execute("""INSERT INTO ADVENTURE_TRIP VALUES(
        45,
        'Jay Peak',
        'Jay',
        'Vt',
        8,
        8,
        'Hiking',
        'Summer'
        );
         """)
#c.execute("""DROP TABLE ADvENTURE_TRIP""")
conn.commit()
conn.close
    
