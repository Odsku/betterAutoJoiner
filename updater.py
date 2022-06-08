import sys, os, requests, hashlib

repository = "Odsku/betterAutoJoiner"

def get_files():
    response = requests.get(f"https://api.github.com/repos/{repository}/contents/")

    return response.json()

def download_file(file_name):
    response = requests.get(f"https://raw.githubusercontent.com/{repository}/main/{file_name}")

    return response.text

def get_current():
    version_file = open("VERSION")
    version = version_file.readline()
    version_file.close()

    return float(version)

def is_updated():
    return get_current() >= get_latest()

def get_latest():
    return float(download_file("VERSION"))

def is_same(data1, data2):
    hash1 = hashlib.sha1(data1.encode()).hexdigest()
    hash2 = hashlib.sha1(data2.encode()).hexdigest()

    return hash1 == hash2

def write_file(path, data):
    file = open(path, "w")
    file.write(data)
    file.close()

def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()

    return data

def update():
    files = get_files()
    for file in files:
        if file["name"] != "config.json":
            local_file = read_file(file["name"])
            remote_file = download_file(file["name"]).replace("\r\n", "\n")

            if not is_same(local_file, remote_file):
                write_file(file["name"], remote_file)

def check_update():
    if not is_updated():
        update()
        os.execv(sys.executable, ['python'] + sys.argv)