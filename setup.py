from setuptools import setup, find_packages

setup(
    name = 'holaMundoK',
    packages = ['holaMundoK'],   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '0.0.1',
    description = 'Paquete de prueba para generar libreria',
    author='Camilo Castellanos',
    url="https://github.com/CamiloCastellanos/PrimeraLibreriaPY",
    classifiers = ["Prueba Konrad"],
    )