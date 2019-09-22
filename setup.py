import setuptools

print(setuptools.find_packages())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='nhpgd',
     version='0.203',
     license='MIT',
     author="Andres Vazquez",
     author_email="andres@data99.com.ar",
     description="Lista de Códigos CIE10 en español. Librería Python simple + versión Django",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/cluster311/nhpgd",
     install_requires=[
        
     ],
     include_package_data=True,  # for ZIP file
     packages=['nhpgd', 'nhpgd_django'], 
     
     classifiers=[
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.6',
         'License :: OSI Approved :: MIT License',
         'Framework :: Django',
         'Framework :: Django :: 2.2',
         'Operating System :: OS Independent',
         'Intended Audience :: Developers', 
     ],
     python_requires='>=3.6',
 )