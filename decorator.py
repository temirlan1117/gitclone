def tema_decorator(func):
    def wrapper(*args, **kwargs):
        print("функция началась")
        result = func(*args, **kwargs)  # Выполнение декорируемой функции
        print("функция закончилась")
        return result  # Возвращение результата выполнения функции
    return wrapper

@tema_decorator
def test_function():
    print("функция продолжается ")
test_function()