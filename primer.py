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
    self.Imagen = 'gnulinux.jpg'
    
  def ponerImagen(self):
    Imagen = QIcon(self.Imagen)
    Label = QLabel('gnulinux', self)
    pixmapImagen = Imagen.pixmap(50,50)
    Label.setPixmap(pixmapImagen)
  
  def ponerIcono(self):
    Icono = QIcon(self.Imagen)
    self.setWindowIcon(Icono)
    
if __name__=="__main__":
  aplicacion = QApplication (sys.argv)
  ventana = Ventana()
  ventana.ponerIcono()
  ventana.ponerImagen()
  ventana.show()
  aplicacion.exec_()
  sys.exit()