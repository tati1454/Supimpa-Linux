import os

from utils import create_folder, download_file, extract_tarball

GNU_MIRROR = "http://gnu.mirrors.hoobly.com/"
TARBALLS_DOWNLOAD_DIRECTORY = "./tarballs/"
BUILDTREES_DIRECTORY = "./buildtrees/"
ROOTFS_DIRECTORY = "./rootfs/"
DEFAULT_PREFIX = "/usr/"

def get_source(pkgname, version):
    filename = f"{pkgname}-{version}.tar.gz"
    tarballpath = f"{TARBALLS_DOWNLOAD_DIRECTORY}{filename}"
    buildtreepath = f"{BUILDTREES_DIRECTORY}{pkgname}-{version}"

    if not os.path.exists(tarballpath):
        download_file(f"{GNU_MIRROR}{pkgname}/{filename}", tarballpath)

    if not os.path.exists(buildtreepath):
        extract_tarball(tarballpath, BUILDTREES_DIRECTORY)
    
    return buildtreepath

def build_buildtree(buildtree, autoconf_args):
    wd = os.getcwd()
    os.chdir(buildtree)
    create_folder("./build")
    os.chdir("./build")
    os.system(f"(../configure --prefix {DEFAULT_PREFIX} {autoconf_args} && make -j4) > build.log 2>&1")
    os.chdir(wd)

def install(buildtree):
    wd = os.getcwd()
    os.chdir(buildtree)
    os.chdir("./build")
    rootfs_absolute_path = os.path.abspath(f"{wd}/{ROOTFS_DIRECTORY}")
    os.environ["DESTDIR"] = rootfs_absolute_path
    os.system(f"make DESTDIR={rootfs_absolute_path} install > install.log 2>&1")
    os.chdir(wd)


def build_gnu_package(name, version, configure_flags=""):
    print(f"Building and installing {name}-{version}")
    buildtree = get_source(name, version)
    print(f"Compiling {name}")
    build_buildtree(buildtree, configure_flags)
    print(f"Installing {name}")
    install(buildtree)
    print("")
