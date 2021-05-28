#!/usr/bin/python3

import subprocess

def main():
    subprocess.run(["envsubst", "< /tegola_config/configTemplate.toml >",  "/tegola_config/config.toml"])
    subprocess.run(["/opt/tegola", "--config", "tegola_config/config.toml serve"])

if __name__ == "__main__":
    main()