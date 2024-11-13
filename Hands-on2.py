class LinearRegressionModel:
    def __init__(self):
        # Datos fijos (hardcoded) para las variables independientes (x) y dependientes (y)
        self.input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # Datos de x
        self.output_data = [2, 4, 6, 8, 10, 12, 14, 16, 18]  # Datos de y
        self.data_points = len(self.input_data)  # Número total de puntos de datos
    
    def sum_product_x_y(self):
        # Calcula la suma de la longitud de cada par (x, y)
        return sum(i * o for i, o in zip(self.input_data, self.output_data))
    
    def sum_x(self):
        # Calcula la suma de todos los valores de x
        return sum(self.input_data)
    
    def sum_y(self):
        # Calcula la suma de todos los valores de y
        return sum(self.output_data)
    
    def sum_x2(self):
        # Calcula la suma de los cuadrados de cada valor de x
        return sum(i ** 2 for i in self.input_data)
    
    def pendiente(self):
        # Calcula la pendiente de la línea de regresión
        numerator = (self.data_points * self.sum_product_x_y()) - (self.sum_x() * self.sum_y())
        denominator = (self.data_points * self.sum_x2()) - (self.sum_x() ** 2)
        return numerator / denominator  # Devuelve el valor de la pendiente
    
    def intercepto(self, pendiente):
        # Calcula el intercepto (intercept), que es el valor de y cuando x es 0
        return (self.sum_y() - (pendiente * self.sum_x())) / self.data_points
    
    def train(self):
        # Ajusta el modelo a los datos calculando los valores de pendiente y intercepto
        pendiente = self.pendiente()  # Calcula la pendiente usando calculate_slope
        intercept = self.intercepto(pendiente)  # Calcula el intercepto usando calculate_intercept
        return intercept, pendiente  # Devuelve el intercepto y la pendiente
    
    def make_prediction(self, input_value, intercept, pendiente):
        # Utiliza la ecuación de la recta para predecir y basado en un valor dado de x
        return intercept + pendiente * input_value  # Devuelve el valor predicho de y


# Código principal: solo se ejecuta si el archivo se ejecuta directamente
if __name__ == "__main__":
    # Crea una instancia del modelo de regresión lineal
    model = LinearRegressionModel()
    
    # Entrena el modelo para calcular los parámetros de la recta de regresión
    intercept, pendiente = model.train()

    # Imprime la ecuación de la recta de regresión
    print(f"Ecuación de la línea: y = {intercept:.2f} + {pendiente:.2f}x")

    # Solicita un valor al usuario para hacer una predicción de y
    try:
        # Pide al usuario que introduzca un valor para x
        input_value = float(input("Introduce un valor para hacer una predicción: "))
        
        # Usa el modelo para predecir y basado en el valor de x ingresado
        prediction = model.make_prediction(input_value, intercept, pendiente)
        
        # Imprime el resultado de la predicción
        print(f"Predicción para publicidad(x) = {input_value}: ventas(y) = {prediction:.2f}")
    except ValueError:
        # Maneja el error si el usuario ingresa un valor no numérico
        print("Por favor, introduce un número válido.")
