from spack import *

# On conatiner we will need: gfal2-util gfal2-all and voms-clients-java

class RucioClients(PythonPackage):
    """Rucio is a software framework that provides functionality to
    organize, manage, and access large volumes of scientific data using
    customisable metadata tags.
    """

    homepage = "https://rucio.cern.ch/"
    url      = "https://pypi.org/packages/source/r/rucio-clients/rucio-clients-32.0.0.tar.gz"

    version('32.8.0', sha256='bb8244a4832e9dc4119b33cd2459b39c47005ed351b4fc2211f00bd374a5ae84')
    depends_on('python@3.9:', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('gfal2-python', type=('build', 'run'))
    depends_on('py-requests@2.25.1:2.31.0', type=('build', 'run'))
    depends_on('py-urllib3@1.26.18', type=('build', 'run'))
    depends_on('py-dogpile.cache@1.2.2', type=('build', 'run'))
    depends_on('py-tabulate@0.9.0', type=('build', 'run'))
    depends_on('py-jsonschema@4.18.0', type=('build', 'run'))

    def install_args(self, spec, prefix):
        # Set the installation prefix
        return ['--prefix={0}'.format(prefix)]
 
    def install(self, spec, prefix):
        # Install using pip
        python('setup.py', 'install', '--prefix={0}'.format(prefix))

