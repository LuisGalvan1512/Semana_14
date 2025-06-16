# 🌳 Estructura de Datos y Algoritmos – Semana 14

> 📚 **Tema:** Heap Sort  
> 📅 **Fecha:** 16/06/2025  
> 🏫 **Institución:** Tecsup  
> 👨‍🏫 **Profesor:** Garamendi Sarmiento, Elliot Leo

---

## 🎬 ¿Qué aprendimos esta semana?

![GIF explicativo](https://drive.google.com/uc?export=view&id=16WX8Xv2bcK--RYDUccNSjVGkKX4e7-2F)


Esta semana profundizamos en la estructura de datos **heap**, esencial para implementar colas de prioridad y algoritmos de ordenamiento eficiente. Entre los puntos clave:

- 🗂️ Representación de un heap en un **arreglo** y fórmula de parent/child (índices).  
- 🆕 Construcción básica de **MinHeap**: inicialización, métodos `is_empty()`, `size()` y `peek()`.  
- 🧭 Navegación interna: cálculo de índices de padre (`(i-1)//2`), hijo izquierdo (`2i+1`) y derecho (`2i+2`), con validaciones.  
- ⬆️ **Inserción** en MinHeap con “percolate up”: añadir al final y burbujeo ascendente en O(log n).  
- ⬇️ **Eliminación** del mínimo con “percolate down”: reemplazar raíz, hundir elemento y restaurar la propiedad en O(log n).  
- 🔄 **MaxHeap** y método `build_heap`: construcción bottom-up en O(n) para soportar heap sort y extracción del máximo.  

---

## 👥 Integrantes del equipo

- Luis Enrique Galván Morales  
- Juan Alexis Aguirre Saavedra  
- Samir Haziel Alfonso Solórzano  
- Aldo Sebastián Alva Capcha

---

## ⚙️ Herramientas utilizadas

- 🐍 Python  
- 💻 Visual Studio Code / PyCharm  
- 🌐 GitHub para control de versiones

---

## 📂 Archivos del laboratorio

| Archivo             | Descripción                                                      |
|---------------------|------------------------------------------------------------------|
| `challenge_1.py`    | MinHeap básico: init, `is_empty()`, `size()`, `peek()`           |
| `challenge_2.py`    | Navegación de heap: cálculos de padre e hijos y validaciones    |
| `challenge_3.py`    | Inserción en MinHeap con heapify_up (burbujeo ascendente)       |
| `challenge_4.py`    | Eliminación en MinHeap con heapify_down (burbujeo descendente)  |
| `challenge_5.py`    | MaxHeap y `build_heap`: heapify bottom-up y operaciones completas|

---

## ✅ Conclusiones

- 🌳 **Estructura en arreglo:** Comprender la representación de un heap como arreglo facilita indexar padres e hijos sin punteros.  
- 🔄 **Operaciones en O(log n):** Inserción y eliminación con heapify up/down garantizan eficiencia para colas de prioridad y ordenamientos.  
- ⚙️ **Construcción en O(n) y flexibilidad:** `build_heap` permite transformar un arreglo arbitrario en un heap en tiempo lineal, adaptable a MinHeap o MaxHeap según el caso.

---

## 🚀 Bonus

> Con la base de MinHeap y MaxHeap, podemos implementar **heap sort** para ordenar en O(n log n) y optimizar algoritmos de planificación de tareas, gestión de eventos y búsqueda de caminos más cortos en grafos.  
