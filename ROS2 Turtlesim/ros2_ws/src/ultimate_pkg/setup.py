from setuptools import setup

import os
from glob import glob 

package_name = 'ultimate_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=['ultimate_pkg/turtle_driver'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='goku',
    maintainer_email='kishanbillava73@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_driver = ultimate_pkg.turtle_driver:main',
        ],
    },
)
