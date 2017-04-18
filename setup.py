from setuptools import setup

url = ""
version = "0.0.2"
readme = open('README.rst').read()

setup(name="awesome",
      packages=["awesome"],
      version=version,
      description="http://tjelvarolsson.com/blog/begginers-guide-creating-clean-python-development-environments/",
      long_description=readme,
      include_package_data=True,
      author="David Antliff",
      author_email="david.antliff@gmail.com",
      url=url,
      install_requires=[],
      download_url="{}/tarball/{}".format(url, version),
      scripts = ['bin/do_awesome.py'],
      entry_points={
          'console_scripts': [
              'do_awesome2 = awesome.__main__:main',
              'do_awesome3 = awesome.do_awesome3:main',
          ],
      },
      license="MIT")
