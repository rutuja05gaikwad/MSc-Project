from setuptools import setup, find_packages # type: ignore

setup(
    name='malware_scan_setup',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3'
    ],
    entry_points={
        'console_scripts': [
            'setup_malware_scan=malware_scan_setup.deploy:main'
        ]
    },
    include_package_data=True,
    description='Setup AWS infrastructure for malware scanning with ClamAV',
)