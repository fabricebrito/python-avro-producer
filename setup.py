from setuptools import setup, find_packages
from io import open

print(find_packages('src'))

console_scripts = []

console_scripts.append('produce={0}.producer.app:main'.format(find_packages('src')[0]))

console_scripts.append('consume={0}.consumer.app:main'.format(find_packages('src')[0]))

setup(entry_points={'console_scripts': console_scripts},
      packages=find_packages(where='src'),
      package_dir={'': 'src'}) 
