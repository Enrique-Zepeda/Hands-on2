class Data:
    def __init__(self):
        # Datos fijos para las variables independientes (x) y dependientes (y)
        self.input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.output_data = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    def get_input_data(self):
        return self.input_data
    
    def get_output_data(self):
        return self.output_data
    
    def get_data_points(self):
        return len(self.input_data)


class Calculator:
    def __init__(self, data):
        self.data = data
    
    def sum_product_x_y(self):
        return sum(i * o for i, o in zip(self.data.get_input_data(), self.data.get_output_data()))
    
    def sum_x(self):
        return sum(self.data.get_input_data())
    
    def sum_y(self):
        return sum(self.data.get_output_data())
    
    def sum_x2(self):
        return sum(i ** 2 for i in self.data.get_input_data())


class Model:
    def __init__(self, calculator):
        self.calculator = calculator
        self.data_points = calculator.data.get_data_points()
    
    def pendiente(self):
        numerator = (self.data_points * self.calculator.sum_product_x_y()) - (self.calculator.sum_x() * self.calculator.sum_y())
        denominator = (self.data_points * self.calculator.sum_x2()) - (self.calculator.sum_x() ** 2)
        return numerator / denominator
    
    def intercepto(self, pendiente):
        return (self.calculator.sum_y() - (pendiente * self.calculator.sum_x())) / self.data_points
    
    def train(self):
        pendiente = self.pendiente()
        intercept = self.intercepto(pendiente)
        return intercept, pendiente


class Prediction:
    def __init__(self, model):
        self.model = model
        self.intercept, self.pendiente = self.model.train()
    
    def make_prediction(self, input_value):
        return self.intercept + self.pendiente * input_value


# Código principal: solo se ejecuta si el archivo se ejecuta directamente
if __name__ == "__main__":
    data = Data()
    calculator = Calculator(data)
    model = Model(calculator)
    predictor = Prediction(model)
    
    # Imprime la ecuación de la recta de regresión
    print(f"Ecuación de la línea: y = {predictor.intercept:.2f} + {predictor.pendiente:.2f}x")
    
    # Solicita un valor al usuario para hacer una predicción de y
    try:
        input_value = float(input("Introduce un valor para hacer una predicción: "))
        prediction = predictor.make_prediction(input_value)
        print(f"Predicción para publicidad(x) = {input_value}: ventas(y) = {prediction:.2f}")
    except ValueError:
        print("Por favor, introduce un número válido.")
