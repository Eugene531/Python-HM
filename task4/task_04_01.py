def fabric(lambda_func):
    """
    Фабрика декоратор.

    Эта фабрика создает декоратор, который в свою очередь принимает функцию
    (lambda_func) и возвращает декоратор, способный обернуть другой декоратор.

    :param lambda_func: Функция (lambda).
    :type lambda_func: function.

    :return: Внешний декоратор.
    :rtype: function.
    """
    def repeat_decor(func1):
        """
        Внешний декоратор.

        Этот декоратор принимает другой декоратор (func1) и возвращает декоратор,
        который добавляет логику повторения вызова декорируемой функции.

        :param func1: Декоратор, который будет применен к функции.
        :type func1: function.

        :return: Декоратор с логикой повторения вызова.
        :rtype: function.
        """
        def repeat_args(*args1):
            """
            Декоратор с логикой повторения вызова.

            Этот декоратор принимает аргументы (args1) и возвращает декоратор, который
            добавляет логику к вызову декорируемой функции.

            :param args1: Аргументы, которые будут переданы декорируемой функции.
            :type args1: tuple.

            :return: Декоратор с логикой вызова функции.
            :rtype: function.
            """
            def foo_decor(func2):
                """
                Внутренний декоратор.

                Этот декоратор принимает другую функцию (func2) и возвращает декоратор, который
                добавляет логику повторения к вызову декорируемой функции.

                :param func2: Декорируемая функция.
                :type func2: function.

                :return: Декоратор с логикой вызова функции.
                :rtype: function.
                """
                def foo_args(*args2):
                    if fabric.is_on:
                        return lambda_func(func1(args1[0])(func2)(args2))
                    return lambda_func((func2)(args2))
                return foo_args
            return foo_decor
        return repeat_args
    return repeat_decor


# Добавляем атрибуты к фабрике
fabric.is_on = True
fabric.off = lambda: fabric.__setattr__('is_on', False)
fabric.on = lambda: fabric.__setattr__('is_on', True)


@fabric(lambda x: x ** 2)
def repeat(times):
    """
    Повторить вызов times раз, и вернуть среднее значение.

    Декорируемая функция, которая будет вызывать функцию fun указанное количество
    раз и возвращать среднее значение результатов.

    :param times: Количество раз, которое нужно вызвать функцию fun.
    :type times: int.

    :return: Декорируемая функция.
    :rtype: function.
    """
    def decoreted_fun(fun):
        def decoreted_fun_args(*args):
            avg = sum(fun() for i in range(times)) // times
            return avg
        return decoreted_fun_args
    return decoreted_fun


@repeat(3)
def foo(*args, **kwargs):
    """Функция которая работает... и все (может принимать на вход любые параметры)"""
    print("Foo called!")
    return 4 # К этому значению далее применяется lambda функция (аргумент для fabric)


print(foo(1, 3, 5))
fabric.off()
print(foo(1, 3, 5))
fabric.on()
print(foo(1, 3, 5))
fabric.off()
print(foo(1, 3, 5))
fabric.on()
print(foo(1, 3, 5))
