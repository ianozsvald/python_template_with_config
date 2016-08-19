from setuptools import setup, find_packages

setup(
    name='python_template_with_config',
    version='0.1.0',
    description='Template of a Python module',
    long_description="<add a longer description>",
    author='Written by Ian Ozsvald',
    author_email='ian@ianozsvald.com',
    url='https://github.com/ianozsvald/',
    license='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["numpy>=1.10"],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
