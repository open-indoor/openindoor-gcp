#!/usr/bin/python3

import subprocess
import os

db_user = os.environ["DB_USER"]
db_port = os.environ["DB_PORT"]
db_pass = os.environ["DB_PASS"]
db_name = os.environ["DB_NAME"]
db_host = os.environ["DB_HOST"]


# Little trick for replace environment variables. As they don't exist during during the build time, we can't use envsubst.
# Moreover, envsubst failed while using it with subprocess.
def main():
    time.sleep(300)
    formerStrings = ["$DB_HOST","$DB_NAME","$DB_PORT","$DB_USER", "$DB_PASS"]
    newerStrings = [db_host,db_name, db_port,db_user,db_pass]
    with open("/tegola_config/configTemplate.toml", "r") as inputFile:
        contents = inputFile.readlines()
    with open("/tegola_config/config.toml", "w+") as outputFile:
        for line in contents:
            for formerString, newerString in zip(formerStrings, newerStrings):
                line = line.replace(formerString, newerString)
            outputFile.write(line)
    subprocess.run(["/opt/tegola", "--config", "tegola_config/config.toml", "serve"])
if __name__ == "__main__":
    main()