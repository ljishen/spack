# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Externalmodule(Package):
    homepage = "http://somewhere.com"
    url      = "http://somewhere.com/module-1.0.tar.gz"

    version('1.0', '1234567890abcdef1234567890abcdef')

    depends_on('externalprereq')
