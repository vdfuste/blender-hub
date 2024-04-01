import PyQt5.QtWidgets as qtw
#import PyQt5.QtGui as qtg

# Cosas que tiene que hacer:
# - Proyectos:
#	- Guardar una lista de proyectos creados.
#	- Añadir y borrar elementos de la lista.
#	- Poder elegir con que versión abrir cada proyecto.
#	- Opción para abrir el modo "Consola".
#
# - Instalaciones:
#	- Descargar diferentes versiones.
#	- Actualizar en vez de descargar (Minor Versions).
#
# - Import Config:
#	- Copiar la configuración entre versiones.

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Blender Hub v0.1.0")
		self.resize(640, 480)
		self.setLayout(qtw.QHBoxLayout())

		todolistLabel = qtw.QLabel("To-Do List")
		self.layout().addWidget(todolistLabel)
		
		self.show()

app = qtw.QApplication([])
mainWindow = MainWindow()

app.exec_()