import os
os.environ['CLASSPATH'] = os.path.join(
  os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
  'tika-app-1.4.jar',
)
from jnius import autoclass


FileInputStream = autoclass('java.io.FileInputStream')
Tika = autoclass('org.apache.tika.Tika')
Metadata = autoclass('org.apache.tika.metadata.Metadata')
tika = Tika()
