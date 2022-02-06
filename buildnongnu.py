import os

from utils import create_folder, download_file, extract_debfile, extract_tarball

def build_pcre2():
    download_file("http://mirrors.kernel.org/ubuntu/pool/main/p/pcre3/libpcre3_8.39-9_amd64.deb", "./tarballs/libpcre3_8.39-9_amd64.deb")
    create_folder("./buildtrees/libpcre")
    extract_debfile("./tarballs/libpcre3_8.39-9_amd64.deb", "./buildtrees/libpcre/")
    os.system("cp ./buildtrees/libpcre/lib/x86_64-linux-gnu/libpcre.so.3.13.3 ./rootfs/lib/")
    os.chdir("./rootfs/lib")
    if not os.path.exists("./libpcre.so.3"):
        os.symlink("./libpcre.so.3.13.3", "./libpcre.so.3")
    print(os.getcwd())
    os.chdir("../../../")

def build_openrc(version):
    wd = os.getcwd()
    download_file(f"https://github.com/OpenRC/openrc/archive/refs/tags/{version}.tar.gz", f"./tarballs/openrc-{version}.tar.gz")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    extract_tarball(f"./tarballs/openrc-{version}.tar.gz", "./buildtrees")
    os.chdir(f"./buildtrees/openrc-{version}")
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)

def build_util_linux():
    wd = os.getcwd()
    download_file("https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.38/util-linux-2.38-rc1.tar.gz", "./tarballs/util-linux-2.38-rc1.tar.gz")
    extract_tarball("./tarballs/util-linux-2.38-rc1.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/util-linux-2.38-rc1")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("./autogen.sh && mkdir -p ./build")
    os.chdir("./build")
    os.system("../configure --prefix=/usr && make -j4")
    os.system(f"sudo make DESTDIR={rootfs_absolute_path} install-strip")
    os.chdir(wd)

def build_procps():
    wd = os.getcwd()
    download_file("https://gitlab.com/procps-ng/procps/-/archive/v3.3.16/procps-v3.3.16.tar.gz", "./tarballs/procps-v3.3.16.tar.gz")
    extract_tarball("./tarballs/procps-v3.3.16.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/procps-v3.3.16")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("./autogen.sh && mkdir -p ./build")
    os.chdir("./build")
    os.system("../configure --prefix=/usr && make -j4")
    os.system(f"sudo make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)

def build_kbd():
    wd = os.getcwd()
    download_file("https://github.com/legionus/kbd/archive/refs/tags/v2.4.0.tar.gz", "./tarballs/kbd-2.4.0.tar.gz")
    extract_tarball("./tarballs/kbd-2.4.0.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/kbd-2.4.0")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("./autogen.sh && mkdir -p ./build")
    os.chdir("./build")
    os.system("../configure --prefix=/usr && make -j4")
    os.system(f"sudo make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)
