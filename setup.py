from distutils.core import setup

setup(name='MyPackageBNP',
      version='1.0',
      description='Package that says hello in several languages',
      author='Mickael BOLNET',
      author_email='mickael.bolnet@web-n-data.com',
      packages=['MyPackage'],
      requires=['numpy'],
      package_dir={'MyPackage': 'MyPackage'},
      )
