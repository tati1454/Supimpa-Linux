import os

from utils import create_folder, download_file, extract_debfile, extract_tarball

def build_pcre2():
    download_file("http://mirrors.kernel.org/ubuntu/pool/main/p/pcre3/libpcre3_8.39-9_amd64.deb", "./tarballs/libpcre3_8.39-9_amd64.deb")
    create_folder("./buildtrees/libpcre")
    extract_debfile("./tarballs/libpcre3_8.39-9_amd64.deb", "./buildtrees/libpcre/")
    os.system("cp ./buildtrees/libpcre/lib/x86_64-linux-gnu/* ./rootfs/lib/")

def build_openrc(version):
    wd = os.getcwd()
    download_file(f"https://github.com/OpenRC/openrc/archive/refs/tags/{version}.tar.gz", f"./tarballs/openrc-{version}.tar.gz")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    extract_tarball(f"./tarballs/openrc-{version}.tar.gz", "./buildtrees")
    os.chdir(f"./buildtrees/openrc-{version}")
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)
