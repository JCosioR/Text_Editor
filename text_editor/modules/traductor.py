class Traductor:
    def __init__(self):
        #letra = {a,b,c,...z,A,B,C,...,Z}
        #digito = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        #simbolos = {#, (, ) [, ], ;, operadores, {, }, }
        #identificadores, palabras reservadas, nombres de funciones, numeros (int, float)
        
        
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
