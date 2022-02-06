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
    os.system(f"make DESTDIR={rootfs_absolute_path} install-strip")
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
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
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
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)

def build_selinux():
    wd = os.getcwd()
    download_file("https://github.com/SELinuxProject/selinux/releases/download/3.3/selinux-3.3.tar.gz", "./tarballs/selinux-3.3.tar.gz")
    extract_tarball("./tarballs/selinux-3.3.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/selinux-3.3")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system(f"make CFLAGS=-Wno-unused-variable DESTDIR={rootfs_absolute_path} install -j4")
    os.chdir(wd)

def build_audit_userspace():
    wd = os.getcwd()
    download_file("https://github.com/linux-audit/audit-userspace/archive/refs/tags/v3.0.7.tar.gz", "./tarballs/audit-userspace-3.0.7.tar.gz")
    extract_tarball("./tarballs/audit-userspace-3.0.7.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/audit-userspace-3.0.7")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("./autogen.sh && mkdir -p ./build")
    os.chdir("./build")
    os.system("../configure --prefix=/usr && make -j4")
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)

def build_libcap_ng():
    wd = os.getcwd()
    download_file("https://github.com/stevegrubb/libcap-ng/archive/refs/tags/v0.8.2.tar.gz", "./tarballs/libcap-ng-0.8.2.tar.gz")
    extract_tarball("./tarballs/libcap-ng-0.8.2.tar.gz", "./buildtrees")
    os.chdir("./buildtrees/libcap-ng-0.8.2")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("./autogen.sh && mkdir -p ./build")
    os.chdir("./build")
    os.system("../configure --prefix=/usr && make -j4")
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)

def build_net_tools():
    wd = os.getcwd()
    download_file("https://sourceforge.net/projects/net-tools/files/net-tools-2.10.tar.xz", "./tarballs/net-tools-2.10.tar.xz")
    extract_tarball("./tarballs/net-tools-2.10.tar.xz", "./buildtrees")
    os.chdir("./buildtrees/net-tools-2.10")
    rootfs_absolute_path = os.path.abspath(f"{wd}/rootfs")
    os.system("make config && make -j4")
    os.system(f"make DESTDIR={rootfs_absolute_path} install")
    os.chdir(wd)
