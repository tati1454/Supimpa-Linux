import os
from pathlib import Path
import tarfile

import requests

def create_folder(name):
    if os.path.exists(name):
        return
    os.mkdir(name)

def download_file(url, output):
    if os.path.exists(output):
        print(f"File {output} already exists")
        return

    with requests.get(url, stream=True) as r:
        total_size = 0
        if "Content-Length" in r.headers:
            total_size = int(r.headers["Content-Length"])

        with open(output, "wb") as f:
            progress = 0
            for c in r.iter_content(chunk_size=8192):
                progress += 8192
                f.write(c)
                if total_size != 0:
                    print(f"\rDownloading: {url} to {output} [{(progress / total_size) * 100:.2f}/100]", end="")
                else:
                    print(f"\rDownloading: {url} to {output}", end="")

            print("")

def extract_tarball(tarball, output_directory):
    tarballfolder = Path(tarball).with_suffix('').stem
    if os.path.exists(f"{output_directory}/{tarballfolder}"):
        print(f"File already extracted {output_directory}/{tarballfolder}")
        return
    with tarfile.open(tarball) as tar:
        tar.extractall(output_directory)

def extract_debfile(debfile, output_directory):
    os.system(f"ar vx {debfile} --output {output_directory}")
    extract_tarball(f"{output_directory}/data.tar.xz", output_directory)
    
