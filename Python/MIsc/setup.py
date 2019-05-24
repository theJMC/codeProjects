from cx_Freeze import setup, Executable

executables = [Executable("Inventory_System_V2.py", base=None)]

setup(name='Inventory System',
      options= {"build_exe": {"packages":["numpy"]}},
      version='0.1',
      description='My Inventory System Using a CSV File'
      executables = executables
      )