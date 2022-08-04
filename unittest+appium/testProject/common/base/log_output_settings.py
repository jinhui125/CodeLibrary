# -*- coding: UTF-8 -*-

import functools


class LogOutputSettings:

    @staticmethod
    def log(func):

        @functools.wraps(func)
        def wrapper(*args, **kw):
            if func.__name__ == "locator":
                print("locator(by={0}, element={1})".format(args[1], args[2]))
                print('   定位元素: func: {0}'.format(func.__name__))
                print('     - 定位元素方式：%s' % args[1])
                print('     - 元素值：%s' % args[2])
                print('\n')

            elif func.__name__ == "wait_element":
                print("wait_element(by={0}, element={1}, time={2})".format(args[1], args[2], kw['time']))
                print('   等待元素: func: {0}'.format(func.__name__))
                print('     - 等待元素时间：%s' % kw['time'])
                print('     - 元素值：%s' % args[2])
                print('\n')

            elif func.__name__ == "click":
                print("click(by={0}, element={1})".format(args[1], args[2]))
                print('   点击元素: func: {0}'.format(func.__name__))
                print('     - 元素值：%s' % args[2])
                print('\n')

            elif func.__name__ == "click_enter":
                print("click_enter(by={0}, element={1}, string={2})".format(args[1], args[2], kw["string"]))
                print('   点击并输入字符: func: {0}'.format(func.__name__))
                print('     - 元素值：%s' % args[2])
                print('     - 输入的内容：%s' % kw["string"])
                print('\n')

            elif func.__name__ == "input":
                print("input(by={0}, element={1}, string={2})".format(args[2], args[3], args[1]))
                print('   输入字符: func: {0}'.format(func.__name__))
                print('     - 元素值：%s' % args[2])
                print('     - 输入的内容：%s' % args[1])
                print('\n')

            elif func.__name__ == "checkWidget_exist":
                print("=" * 100)
                print('检查元素是否存在: func: {0}'.format(func.__name__))
                print("=" * 100)
                print('\n')

            elif func.__name__ == "checkWidget_property":
                print("=" * 100)
                print('检查元素属性值: func: {0}'.format(func.__name__))
                print("=" * 100)
                print('\n')

            elif func.__name__ == "checkWidget_toast":
                print("=" * 100)
                print('检查元素是否存在: func: {0}'.format(func.__name__))
                print("=" * 100)
                print('\n')

            # print('call %s' % func.__name__)

            return func(*args, **kw)

        return wrapper

    # @staticmethod
    # def logStep(func):
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel('DEBUG')
    #     formatter = logging.Formatter(
    #         "%(asctime)s - %(message)s"
    #     )
    #     ch = logging.StreamHandler()
    #     ch.setFormatter(formatter)
    #     logger.addHandler(ch)
    #
    #     @functools.wraps(func)
    #     def wrapper(*args, **kw):
    #         print(func.__name__)
    #         print(func.__doc__)
    #         logger.debug(f"func: {func.__name__} {args}")
    #         return func(*args, **kw)
    #
    #     return wrapper
