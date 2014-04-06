import sys
from PySide.QtGui import QApplication, QWidget

class Ventana(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setWindowTitle("Ventana")
    self.setGeometry(400, 200, 300, 250)
    
if __name__=="__main__":
  ventana = Ventana()
  aplicacion = QApplication (sys.argv)
  ventana.show()
  aplicacion.exec_()
  sys.exit()