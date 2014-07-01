from distutils.core import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()

setup(name='cisco123',
      version=version,
      author='Cisco Systems, Inc',
      author_email='support@cisco.com',
      # The project's main homepage
      url='www.cisco.com',
      packages=['cisco123'],
      data_files=[('.',['VERSION'])]
      )
