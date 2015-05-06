from setuptools import setup
from setuptools import find_packages

install_requires = [
    'letsencrypt',
    'zope.interface',
]

setup(
    name='letsencrypt-iis',
    version='0',
    author='Felix Rieseberg',
    install_requires=install_requires,
    packages=find_packages(),
    entry_points={
        # TODO: entry point group 'letsencrypt.authenticators' should
        # be removed once lets-encrypt-preview#376 is pulled in;
        # 'letsencrypt.plugins' is already included for future
        # compatibility with #376
        'letsencrypt.authenticators': [
            'iis=letsencrypt_iis.configurator:IISConfigurator',
        ],
        'letsencrypt.plugins': [
            'iis=letsencrypt_iis.configurator:IISConfigurator',
        ],

    }
)
