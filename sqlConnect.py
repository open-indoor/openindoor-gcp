import psycopg2

connection = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='34.78.47.231', port='5432', sslmode='require', sslrootcert="server-ca.pem",sslcert="client-cert.pem", sslkey="client-key.pem")
cursor = connection.cursor()
# cursor.execute('CREATE EXTENSION postgis;')
# connection.commit()
# cursor.execute('CREATE EXTENSION dblink;')
cursor.execute('CREATE EXTENSION postgis_topology; SELECT * FROM pg_extension; ')
for query in cursor:
    print (str(query))

cursor.close()
connection.close()
