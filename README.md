# sistema-aureo 
# 1. Crear estructura de carpetas base
mkdir -p ~/STP-Φ/{Φ_kernel/{axioms,meta_inference,fractal_memory},Φ_tools/{build,langs/{cpp,rust,go,python,java},webstack,symbolicIO,pkgman},Φ_projects/{demo_0Aureo,ascii_engine,agente_álgido,humanoides_Φ},Φ_data/{logs,fractals,raw},Φ_docs}

# 2. Inicializar archivos base
touch ~/STP-Φ/Φ_docs/{manifesto.txt,memoria_tecnica.pdf,README.md}

# 3. Clonar herramientas esenciales
cd ~/STP-Φ/Φ_tools/langs/cpp
git clone https://github.com/ggerganov/llama.cpp

cd ~/STP-Φ/Φ_tools/langs/rust
git clone https://github.com/ekzhang/bore

cd ~/STP-Φ/Φ_tools/webstack
git clone https://github.com/vercel/next.js

cd ~/STP-Φ/Φ_tools/symbolicIO
git clone https://github.com/fxnn/ascii-tables

# 4. Instalar librerías esenciales en Termux (sin root)
pkg update -y && pkg upgrade -y
pkg install -y git clang cmake build-essential rust golang python nodejs openjdk-17 termux-api

# 5. Instalar Python packages
pip install numpy sympy rich asciimatics

# 6. Instalar Node packages
npm install -g typescript esbuild

# 7. Inicializar entorno simbólico
echo "Φ_kernel operativo" > ~/STP-Φ/Φ_kernel/axioms/axiom_0.txt
echo "Ψ: proporción de sentido interno" >> ~/STP-Φ/Φ_kernel/axioms/axiom_0.txt
# 8. Compilar y probar un módulo C++ simbólico
cd ~/STP-Φ/Φ_projects/demo_0Aureo
cat <<EOF > main.cpp
#include <iostream>
const double PHI = 1.6180339887;
int main() {
    std::cout << "Bienvenido al Núcleo Φ\n";
    std::cout << "Φ constante: " << PHI << std::endl;
    return 0;
}
EOF

clang++ main.cpp -o demo_0Aureo && ./demo_0Aureo

# 9. Ejecutar ejemplo Python simbólico
cd ~/STP-Φ/Φ_projects/demo_0Aureo
cat <<EOF > simbolo.py
from sympy import *
init_printing()
phi = (1 + sqrt(5)) / 2
print("Φ simbólico:", phi)
EOF

python simbolo.py

# 10. Ejecutar demo ASCII simbólico
cat <<EOF > ~/STP-Φ/Φ_projects/ascii_engine/ascii_phi.py
from asciimatics.screen import Screen
def demo(screen):
    screen.print_at("Φ", 10, 5, colour=3)
    screen.refresh()
    screen.wait_for_input(10)
Screen.wrapper(demo)
EOF

python ~/STP-Φ/Φ_projects/ascii_engine/ascii_phi.py

# 11. Iniciar servidor local para interfaz
cd ~/STP-Φ/Φ_tools/webstack/next.js/examples/hello-world
npm install && npm run dev

# 12. Probar comunicación de red simbólica
cd ~/STP-Φ/Φ_tools/langs/rust/bore
cargo build --release
./target/release/bore local 8000

# 13. Registrar logs de uso
date > ~/STP-Φ/Φ_data/logs/session_$(date +%s).log
# 14. Crear y versionar tu primer script Φ simbólico
cd ~/STP-Φ/Φ_projects/demo_0Aureo
git init
git add main.cpp simbolo.py
git commit -m "Versión inicial Φ simbólica"

# 15. Visualizar estructura del stack
tree ~/STP-Φ -L 2

# 16. Añadir módulo de visualización científica
pip install matplotlib sympy numpy

cat <<EOF > ~/STP-Φ/Φ_projects/demo_0Aureo/plot_phi.py
import matplotlib.pyplot as plt
import numpy as np
phi = (1 + 5 ** 0.5) / 2
x = np.linspace(0, 4*np.pi, 500)
y = np.sin(x * phi)
plt.plot(x, y)
plt.title("Onda simbólica Φ")
plt.show()
EOF

python ~/STP-Φ/Φ_projects/demo_0Aureo/plot_phi.py

# 17. Añadir módulo de análisis simbólico
cat <<EOF > ~/STP-Φ/Φ_projects/demo_0Aureo/phi_algebra.py
from sympy import *
init_printing()
x = symbols('x')
expr = (1 + sqrt(5))/2 * x**2 + x + 1
print("Expresión con Φ:", expr)
print("Derivada:", diff(expr, x))
EOF

python ~/STP-Φ/Φ_projects/demo_0Aureo/phi_algebra.py

# 18. Guardar y versionar cambios
git add plot_phi.py phi_algebra.py
git commit -m "Añadidos módulos de visualización y álgebra simbólica Φ"

# 19. Crear backup simbólico comprimido
cd ~/STP-Φ
tar -cvf STP-Φ_$(date +%F).tar Φ_projects Φ_data Φ_tools | zstd -19 -T4 -o STP-Φ_backup.zst
# 20. Añadir documentación simbólica Φ
mkdir -p ~/STP-Φ/Φ_docs

cat <<EOF > ~/STP-Φ/Φ_docs/README.md
# STP-Φ (Sistema Transcompilador Poshumano)

## Descripción
Stack simbólico-matemático basado en Φ (número áureo) que integra análisis algebraico, visualización, compresión, lenguajes múltiples y control de versiones.

## Estructura
- Φ_projects/: Scripts, algoritmos y prototipos
- Φ_data/: Datos generados o procesados
- Φ_tools/: Herramientas personalizadas
- Φ_docs/: Documentación técnica

## Dependencias clave
- C++, Python, Rust, Go, Java, Node
- Git, Zstd, Matplotlib, SymPy, CMake
- Todas integradas sin redundancia en un stack mínimo áureo

## Ejecución básica
- `python3 plot_phi.py` para visualizar
- `g++ main.cpp -o main && ./main` para C++
EOF

# 21. Añadir PDF simbólico técnico (Markdown → PDF)
pip install markdown markdown2pdf

markdown2pdf ~/STP-Φ/Φ_docs/README.md -o ~/STP-Φ/Φ_docs/STP-Φ.pdf

# 22. Versionar documentación
cd ~/STP-Φ/Φ_projects/demo_0Aureo
git add ../../Φ_docs
git commit -m "Documentación inicial y PDF generado"

# 23. Añadir módulo de mutación matemática
cat <<EOF > ~/STP-Φ/Φ_projects/demo_0Aureo/mutation_phi.py
from sympy import symbols, simplify, sqrt
x = symbols('x')
phi = (1 + sqrt(5)) / 2
mut = simplify((phi ** 2 - phi - 1).evalf())
print("Mutación verificada:", mut == 0)
EOF

python3 mutation_phi.py

# 24. Plan de expansión
mkdir -p ~/STP-Φ/Φ_projects/genetico
mkdir -p ~/STP-Φ/Φ_projects/visual_engine
mkdir -p ~/STP-Φ/Φ_projects/0Aureo_AI

# 25. Backup final de fase 1
cd ~/STP-Φ
tar -cvf STP-Φ_finalFase1.tar Φ_projects Φ_data Φ_tools Φ_docs | zstd -19 -T4 -o STP-Φ_f1.zstd
