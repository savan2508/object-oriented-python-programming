from temperature import Temperature


class Calories:
    """
    This class calculate the amount of the calories needed for the day based on the
    temperature.
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature_f = Temperature(country="usa", city="tampa").get()
    temperature_c = (temperature_f - 32) / (9 / 5)
    calorie = Calories(weight=85, height=180, age=27, temperature=temperature_c)
    print(calorie.calculate())


