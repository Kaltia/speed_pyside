# git init
# git add primer.py
# git commit
# git remote add origin repositorio
# git push origin rama{master}

import sys
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel

class Ventana(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setWindowTitle("Ventana")
    self.setGeometry(400, 200, 300, 250)
    
  def ponerImagen(self):
    Imagen = QIcon('gnulinux.jpg')
    Label = QLabel('gnulinux', self)
    pixmapImagen = Imagen.pixmap(50,50)
    Label.setPixmap(pixmapImagen)
    
if __name__=="__main__":
  aplicacion = QApplication (sys.argv)
  ventana = Ventana()
  ventana.ponerImagen()
  ventana.show()
  aplicacion.exec_()
  sys.exit()
