import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QListWidgetItem,QListWidget
from PyQt5 import uic
import clips

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Estructura_Mejorada.ui', self)

        # Inicializa la interfaz
        self.init()

    def init(self):
        self.btCargar.clicked.connect(self.ui_cargar_clp)
        self.bt_Prueba.clicked.connect(self.ui_prueba_clp)
        self.listPlantillas = self.findChild(QListWidget, 'listPlantillas')
        self.listRules = self.findChild(QListWidget, 'listRules')
        self.listFacts = self.findChild(QListWidget, 'listFacts')
    
    def ui_cargar_clp(self):
        try:
            with open("Animales.clp", "r") as file:
                clp_code = file.read()

                # Dividir el código en líneas y eliminar líneas vacías y comentarios
                lines = [line.strip() for line in clp_code.split('\n') if line.strip() and not line.strip().startswith(';;')]

                facts, rules, templates = [], [], []
                current_list = None

                for line in lines:
                    if line.startswith('(deffacts'):
                        current_list = facts
                    elif line.startswith('(defrule'):
                        current_list = rules
                    elif line.startswith('(deftemplate'):
                        current_list = templates

                    if current_list is not None:
                        current_list.append(line)

                for fact in facts:
                    self.add_facts(self.listFacts, fact)

                for rule in rules:
                    self.add_rules(self.listRules, rule)
                
                for template in templates:
                    self.add_template(self.listPlantillas, template)

                self.txt_basura.setText('Archivo CLP cargado correctamente.')
        except clips.ClipsError as e:
                self.txt_basura.setText(f'Error al cargar el archivo CLP: {str(e)}')


    def ui_prueba_clp(self):
        # Aquí ejecutas el programa CLIPS
        try:
            clips.reset()
            clips.run()
            self.txt_prueba.setText('Programa CLIPS ejecutado correctamente.')
        except clips.ClipsError as e:
            self.txt_prueba.setText(f'Error al ejecutar el programa CLIPS: {str(e)}')

    def add_facts(self, list_widget, item):
       if list_widget is not None:
        start_index = item.find('(')
        end_index = item.rfind(')')

        if start_index != -1 and end_index != -1:
            content = item[start_index + 1:end_index]
            # Divide el contenido en líneas y agrega cada línea por separado
            lines = [line.strip() for line in content.split('\n') if line.strip()]

            # Elimina el paréntesis de cierre en el último elemento si existe
            if lines and lines[-1].endswith(')'):
                lines[-1] = lines[-1][:-1].strip()

            for line in lines:
                list_widget.addItem(QListWidgetItem(line))
    
    def add_rules(self, list_widget, item):
        if list_widget is not None:
            # Encuentra el índice de "deffacts" o "defrule"
            start_index_rule = item.find('defrule')
            if start_index_rule != -1:
                # Toma la porción de la cadena después de "defrule"
                content = item[start_index_rule + len('defrule'):]
                # Obtén la primera palabra después de "defrule"
                next_word = content.split()[0]
                list_widget.addItem(QListWidgetItem(next_word.strip()))



    def add_template(self, list_widget, item):
        if list_widget is not None:
            start_index_template = item.find('deftemplate')
            if start_index_template != -1:
                # Toma la porción de la cadena después de "deftemplate"
                content = item[start_index_template + len('deftemplate'):]
                # Obtiene la primera palabra después de "deftemplate"
                template_name = content.split()[0]
                list_widget.addItem(QListWidgetItem(template_name.strip()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = UI()
    ventana.show()
    sys.exit(app.exec_())
