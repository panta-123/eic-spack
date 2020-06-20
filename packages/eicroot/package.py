# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eicroot(CMakePackage):
    """EicRoot software framework"""

    homepage = "http://github.com/eic/EicRoot"
    url      = "http://github.com/eic/EicRoot"
    git      = "http://github.com/eic/EicRoot.git"

    version('master', branch='master')

    depends_on('root@6.00.00: +vmc')
    depends_on('geant3-vmc')
    depends_on('geant4-vmc')

    def patch(self):
        # Replace __USE_BSD with __USE_MISC in recent gcc
        filter_file(
            '__USE_BSD',
            '__USE_MISC',
            "dbase/dbValidation/ValTimeStamp.cxx")
        # Replace lib64/libgeant321.so with lib/libgeant321.so
        filter_file(
            'lib64/libgeant321.so',
            'lib/libgeant321.so',
            "eic/htc/CMakeLists.txt")

    def cmake_args(self):
        spec = self.spec

        args = []
        # args.append('-DEICSMEAR=') # FIXME 'eic-smear'
        # args.append('-DCBMROOT=') # FIXME ???
        # args.append('-DOPENCASCADE=') # FIXME 'opencascade'
        # args.append('-DJANA=') # FIXME 'jana2'
        args.append('-DG3VMC={0}'.format(spec['geant3-vmc'].prefix))
        args.append('-DG4VMC={0}'.format(spec['geant4-vmc'].prefix))
        args.append('-DCAD2ROOT=no')
        args.append('-DHTC=no')

        return args
