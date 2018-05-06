from setuptools import setup

setup( name='tayhello',
       version='0.1',
       description='This module makes datetime module more simple. ',
       url='https://github.com/chickachickaaa/tayhello.git',  # usually a github URL after commit
       author='Taylor Higgins',
       author_email='thiggins4890@gmail.com',
       license='MIT',
       packages=['tayhello'],
       install_requires=[ ],
       test_suite='pytest'
       setup_requires=['pytest-runner']
       tests_require=['pytest']
       zip_safe=False )
