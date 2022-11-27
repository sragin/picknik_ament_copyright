from setuptools import find_packages
from setuptools import setup

package_name = 'koceti_ament_copyright'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    package_data={'': [
        'template/*',
    ]},
    zip_safe=False,
    author='Jongpil Kim',
    author_email='jpkim@koceti.re.kr',
    maintainer='Jongpil Kim',
    maintainer_email='jpkim@koceti.re.kr',
    url='https://github.com/PickNikRobotics/picknik_ament_copyright',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Check source files for KOCETI-specific copyright reference.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'ament_copyright.copyright_name': [
            'koceti = koceti_ament_copyright.copyright_names:koceti',
        ],
        'ament_copyright.license': [
            'koceti_proprietary = koceti_ament_copyright.licenses:koceti_proprietary',
        ],
    },
)
