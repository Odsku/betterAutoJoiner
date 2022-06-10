import sys, os, requests, hashlib

repository = "Odsku/betterAutoJoiner"

def create_file(path, data):
    try:
        file = open(path, "x")
        file.write(data)
        file.close()
    except Exception as e:
        print(e)
        return

def write_file(path, data):
    try:
        file = open(path, "w")
        file.write(data)
        file.close()
    except Exception as e:
        print(e)
        return

def read_file(path):
    try:
        file = open(path, "r")
        data = file.read()
        file.close()
    except Exception as e:
        print(e)
        return False
    else:
        return data

def get_files():
    try:
        response = requests.get(f"https://api.github.com/repos/{repository}/contents")
    except Exception as e:
        print(e)
        return False
    else:
        if "message" in response.json():
            print("API rate limit.")
            return False

        return response.json()

def download_file(file_name):
    try:
        response = requests.get(f"https://raw.githubusercontent.com/{repository}/main/{file_name}")
    except Exception as e:
        print(e)
        return False
    else:
        return response.text

def get_current():
    version = read_file("VERSION")

    if version:
        return float(version)
    else:
        return 0.0

def is_updated():
    return get_current() >= get_latest()

def get_latest():
    version = download_file("VERSION")

    if version:
        return float(version)
    else:
        return 0.0

def is_same(data1, data2):
    hash1 = hashlib.sha1(data1.encode()).hexdigest()
    hash2 = hashlib.sha1(data2.encode()).hexdigest()

    return hash1 == hash2

def update():
    files = get_files()
    if files:
        for file in files:
            local_file = read_file(file["name"])
            remote_file = download_file(file["name"])

            if remote_file and local_file:
                remote_data = remote_file.replace("\r\n", "\n")
                local_data = local_file.replace("\r\n", "\n")

                if not is_same(local_data, remote_data):
                    write_file(file["name"], remote_data)

            elif remote_file:
                remote_data = remote_file.replace("\r\n", "\n")
                create_file(file["name"], remote_data)

def check_update():
    if not is_updated():
        update()
        os.system(f"{sys.executable} {' '.join(sys.argv)}")

# Copyright © 2022 Odsku. All rights reserved.