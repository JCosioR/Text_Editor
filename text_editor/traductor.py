class Traductor:
    def __init__(self):
        self.equivalencias = {
            "int main() {" : "if __name__ == \"__main__\":",
            "printf(" : "print(",
            "return 0;":"",
            ";":"",
            "if (" : "if ",
            "else": "else:",
            "for (": "for ",
            "whille (": "while ",
            "int " : "",
            "float ": "",
            "char ": "",
            "scanf(": "input(",
            "&": "",
        }
    
    def traducir(self, codigo_c):
        lineas = codigo_c.split("\n")
        codigo_python = []

        for linea in lineas:
            for c_key, py_value in self.equivalencias.items():
                if c_key in linea:
                    linea = linea.replace(c_key, py_value)
            codigo_python.append(linea)

        return "\n".join(codigo_python)