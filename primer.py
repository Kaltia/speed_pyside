# git init
# git add primer.py
# git commit
# git remote add origin repositorio
# git push origin rama{master}

import sys
import os
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel
#Esta clase se Define la Ventana.
class Ventana(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setWindowTitle("Ventana")
    self.setGeometry(400, 200, 300, 250)
    
  def ponerImagen(self, img):
    Imagen = QIcon(img)
    Label = QLabel(os.path.basename(img), self)
    pixmapImagen = Imagen.pixmap(50,50)
    Label.setPixmap(pixmapImagen)
    self.ponerIcono(img)
  
  def ponerIcono(self, img):
    Icono = QIcon(img)
    self.setWindowIcon(Icono)
    
if __name__=="__main__":
  if len(sys.argv) <= 1:
    sys.exit(-1)
    
  if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]):
    sys.exit(-1)
    
  aplicacion = QApplication (sys.argv)
  ventana = Ventana()
  # ventana.ponerIcono()
  ventana.ponerImagen(sys.argv[1])
  ventana.show()
  aplicacion.exec_()
  sys.exit()
