import os
import tarfile

import requests

def create_folder(name):
    if os.path.exists(name):
        return
    os.mkdir(name)

def download_file(url, output):
    with requests.get(url, stream=True) as r:
        total_size = int(r.headers["Content-Length"])
        with open(output, "wb") as f:
            progress = 0
            for c in r.iter_content(chunk_size=8192):
                progress += 8192
                f.write(c)
                print(f"\rDownloading: {url} to {output} [{(progress / total_size) * 100:.2f}/100]", end="")

            print("")

def extract_tarball(tarball, output_directory):
    with tarfile.open(tarball) as tar:
        tar.extractall(output_directory)
