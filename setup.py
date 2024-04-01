from setuptools import setup, find_packages

setup(
    name='redocmx',
    version='0.0.2',
    author='redoc.mx',
    author_email='soporte@redoc.mx',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    description='Conversión CFDI a PDF',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['cfdi a pdf', 'cfdi', 'cfdi to pdf', 'conversión cfdi a pdf', 'sat mexico', 'mexico'],
    url='https://github.com/redocmx/client-python',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
