from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dblp-python',
      version='0.1',
      description='A simple wrapper around the DBLP API.',
      long_description=readme(),
      classifiers=[
                  'Development Status :: 3 - Alpha',
                  'License :: OSI Approved :: MIT License',
                  ],
      url='https://github.com/scholrly/dblp-python',
      author='Matt Luongo',
      author_email='mhluongo@gmail.com',
      license='MIT',
      packages=['dblp'],
      install_requires=[
                      'requests>=1.0.4',
                  ]
     )
