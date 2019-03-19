from setuptools import setup

def readme():
    with open('README.md', encoding='utf8') as f:
        return f.read()

setup(name='banhammer',
      version='0.1.0',
      description='Generates GIFs based on Tom Scott\'s Banhammer',
      long_description=readme(),
      url='https://github.com/DerpyChap/banhammer',
      author='DerpyChap',
      author_email='holla@derpychap.co.uk',
      license='ISC',
      packages=['banhammer'],
      install_requires=['pillow', 'imageio', 'numpy'],
      include_package_data=True,
      zip_safe=False)
