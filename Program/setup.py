import sys
from cx_Freeze import setup, Executable

# python setup.py build
# python setup.py bdist_msi

base = None

if sys.platform == 'win64': base = 'Win64GUI'

opts = {'include_files': ['mem.gif'], 'includes': ['re']}
setup(name = 'Lotto', version = '1.0', description='Lottery number picker', author='Dany', options= {'build_exe': opts}, executables=[Executable('lotto.py', base=base)])