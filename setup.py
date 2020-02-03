import setuptools


setuptools.setup(
    name='traffic_light',
    version='0.1.dev01',
    packages=setuptools.find_packages(),
    scripts=['bin/traffic_light.py'],
    author='Jason Goodell',
    author_email='jasongoodell@icloud.com',
    incluce_package_data=True,
    description='A traffic light simulator',
    test_suite='tests'
)
