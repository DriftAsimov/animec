from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='animec',
  version='0.0.1',
  description='An unofficial module to extract character data from myanimelist',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type = 'text/markdown',
  url='',  
  author='Drift Asimov',
  author_email='driftasimov@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='animecharacter', 
  packages=find_packages(),
  install_requires=['googlesearch','bs4','urllib'] 
)