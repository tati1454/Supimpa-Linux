import os

from utils import create_folder, download_file
import buildgnu

def create_rootfs():
    create_folder("rootfs")
    create_folder("rootfs/usr")
    create_folder("rootfs/usr/sbin")
    create_folder("rootfs/usr/bin")
    create_folder("rootfs/usr/lib")
    create_folder("rootfs/usr/lib64")

    create_folder("rootfs/etc")
    create_folder("rootfs/proc")
    create_folder("rootfs/dev")
    create_folder("rootfs/sys")
    create_folder("rootfs/boot")
    create_folder("rootfs/home")
    create_folder("rootfs/root")
    create_folder("rootfs/tmp")

    os.chdir("./rootfs")
    if not os.path.exists("./sbin"):
        os.symlink("./usr/sbin", "./sbin")

    if not os.path.exists("./bin"):
        os.symlink("./usr/bin", "./bin")

    if not os.path.exists("./lib"):
        os.symlink("./usr/lib", "./lib")

    if not os.path.exists("./lib64"):
        os.symlink("./usr/lib64", "./lib64")

    os.chdir("..")

if __name__ == "__main__":
    create_folder("tarballs")
    create_folder("buildtrees")
    create_rootfs()
    
    LATEST_GLIBC_VERSION = "2.35"
    buildgnu.build_gnu_package("glibc", LATEST_GLIBC_VERSION)

    LATEST_COREUTILS_VERSION = "9.0"
    buildgnu.build_gnu_package("coreutils", LATEST_COREUTILS_VERSION, "--disable-selinux")

    LATEST_BASH_VERSION = "5.1.16"
    buildgnu.build_gnu_package("bash", LATEST_BASH_VERSION)

    LATEST_NCURSES_VERSION = "6.3"
    buildgnu.build_gnu_package("ncurses", LATEST_NCURSES_VERSION, "--with-shared --with-termlib")
