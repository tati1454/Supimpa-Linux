import os

from utils import create_folder, download_file
import buildgnu
import buildnongnu

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
    create_folder("rootfs/run")

    os.chdir("./rootfs")
    if not os.path.exists("./sbin"):
        os.symlink("./usr/sbin", "./sbin")

    if not os.path.exists("./bin"):
        os.symlink("./usr/bin", "./bin")

    if not os.path.exists("./lib"):
        os.symlink("./usr/lib", "./lib")

    if not os.path.exists("./lib64"):
        os.symlink("./usr/lib64", "./lib64")

    with open("./etc/fstab", "w") as f:
        f.writelines(["none\t/proc\tproc\tdefault",])
    
    os.chdir("..")

if __name__ == "__main__":
    create_folder("tarballs")
    create_folder("buildtrees")
    create_rootfs()
    
    LATEST_GLIBC_VERSION = "2.35"
    buildgnu.build_gnu_package("glibc", LATEST_GLIBC_VERSION)

    LATEST_COREUTILS_VERSION = "9.0"
    buildgnu.build_gnu_package("coreutils", LATEST_COREUTILS_VERSION, "--without-selinux")

    LATEST_BASH_VERSION = "5.1.16"
    buildgnu.build_gnu_package("bash", LATEST_BASH_VERSION)
    os.chdir("./rootfs/bin")
    if not os.path.exists("./sh"):
        os.symlink("./bash", "./sh", target_is_directory=False)
    os.chdir("../../../")

    LATEST_NCURSES_VERSION = "6.3"
    buildgnu.build_gnu_package("ncurses", LATEST_NCURSES_VERSION, "--with-shared --with-termlib --with-versioned-syms")

    LATEST_GREP_VERSION = "3.7"
    buildgnu.build_gnu_package("grep", LATEST_GREP_VERSION)

    LATEST_FINDUTILS_VERSION = "4.9.0"
    buildgnu.build_gnu_package("findutils", LATEST_FINDUTILS_VERSION)

    LATEST_GZIP_VERSION = "1.10"
    buildgnu.build_gnu_package("gzip", LATEST_GZIP_VERSION)

    buildnongnu.build_pcre2()
    buildnongnu.build_openrc("0.44.10")
    buildnongnu.build_util_linux()
    buildnongnu.build_procps()
    buildnongnu.build_kbd()
