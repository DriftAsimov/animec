from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  "Topic :: Education :: Testing",
  "Topic :: Software Development :: Libraries"
]
 
setup(
  name='animec',
  version='0.0.6',
  description='An unofficial API to get data about anime characters, anime news and more.',
  long_description=open('README.md', encoding='utf-8').read(),
  long_description_content_type = 'text/markdown',
  url='https://github.com/DriftAsimov/animec',  
  author='DriftAsimov',
  author_email='driftasimov@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['animecharacter anime api character myanimelist news animenews'], 
  packages=find_packages(),
  install_requires=['google-search==1.0.2','bs4==0.0.1','urllib3==1.25.9','google==3.0.0'] 
)
