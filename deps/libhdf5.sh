#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/libhdf5"

HDF5_VERSION=1.12.0
dir_hdf5=./hdf5

#
# download hdf5 source
#

rm -rf $dir_hdf5
if [[ ! -f hdf5-${HDF5_VERSION}.tar.gz ]]; then
	curl -L https://github.com/HDFGroup/hdf5/archive/refs/tags/hdf5-`echo ${HDF5_VERSION} | tr "." "_"`.tar.gz -o hdf5-${HDF5_VERSION}.tar.gz
fi
tar -xzf hdf5-${HDF5_VERSION}.tar.gz
mv hdf5-hdf5-`echo ${HDF5_VERSION} | tr "." "_"` $dir_hdf5
cp H5pubconf.h $dir_hdf5/src/H5pubconf.h
[ -d ${dir_hdf5} ] && rm -rf ${dir_hdf5}/{tools,test,testpar}
