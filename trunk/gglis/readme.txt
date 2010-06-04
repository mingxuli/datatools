for building the project, you need install py2exe module and copy the code listed blew to setup.py. Then run "python setup.py py2exe"
#============setup.py============
from distutils.core import setup
import py2exe
setup(
	windows=[{"script":"gglis.py"}],
	data_files = [('plugins',['C:\\Program Files\\Quantum GIS Enceladus\\plugins\\spatialiteprovider.dll']),('data',['D:\\ICIMOD\\GUI\\GGLIS\\src\\data\\nepal.sqlite'])],
	options={"py2exe":{"includes":["sip","PyQt4.QtXml"]}}
	)
#=============================