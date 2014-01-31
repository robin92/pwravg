pwravg
================
Another semester has just passed? Tired of counting collected *ECTS* points and couting your average grade? Well, you may want to relax - here comes **pwravg**!

This application counts your average and more, based on a source code of **EdukacjaCL**'s webpage. Additionally, **pwravg** can serve as a library for processing raw HTML data into friendlier notation and be a bedrock of a new application.

### Running
In order to work, **pwravg** doesn't need installing! Just download the latest version from [GitHub](https://github.com/robin92/pwravg/) to your computer, extract it and type ``python -m pwravg``.

When started application will wait for data input. Data can also be read from text file with ``-f /path/to/file`` argument. When data has been successfully parsed you will be presented your average in a nice way. You can limit results to specific semesters with ``-s semesters-numbers`` switch. 

### Installation
For those of you who just can't stand not having it installed. Just download the latest version and run a bundled ``setup.py`` script which will install **pwravg** into your system.

Please note that installation process is performed by ``setuptools`` package, so install that first.

### Final notes
This application has been written for **Python >= 3** and almost for sure won't work with any lower version.
