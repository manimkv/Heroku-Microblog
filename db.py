#import psycopg2



import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)

#con = psycopg2.connect(database='manimkv') 
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS blogspot")
cur.execute("CREATE TABLE blogspot(id serial,author text,post text,day text,time text,comment text)")
conn.commit()
conn.close()
