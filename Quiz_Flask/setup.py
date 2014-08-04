from setuptools import setup

setup(name='QuizWithFlask', version='1.0',
      description='Code example demonstrating using Flask in python',
      author='Hckmar', author_email='hckmar@openmailbox.org',
      url='http://www.hckmar.esy.es',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask',
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )