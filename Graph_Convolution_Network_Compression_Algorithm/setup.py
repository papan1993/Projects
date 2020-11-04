from setuptools import setup
from setuptools import find_packages

setup(name='pygcn_pruning',
      version='0.1',
      description='Graph Convolutional Networks with Pruning in PyTorch',
      author='Soumyadeep Choudhury',
      author_email='sxc180056@utdallas.edu',
      license='UTD',
      install_requires=['numpy',
                        'torch',
                        'scipy'
                        ],
      package_data={'pygcn': ['README.md']},
      packages=find_packages())
