from setuptools import setup,find_packages

setup(
    name='ANIKET-STT',version='1.0.0',
    author='Aniket Rana',
    author_email="aniketrana5892@gmail.com",
    description='A simple Speech to Text converter using Selenium and Webdriver',
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager'
]
