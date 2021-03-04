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
  version='0.0.2',
  description='An unofficial module to extract character data from myanimelist',
  long_description=open('README.md').read(),
  long_description_content_type = 'text/markdown',
  url='https://github.com/DriftAsimov/animec',  
  author='DriftAsimov',
  author_email='driftasimov@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='animecharacter', 
  packages=find_packages(),
  install_requires=['google-search==1.0.2','bs4==0.0.1','urllib3==1.25.9'] 
)
