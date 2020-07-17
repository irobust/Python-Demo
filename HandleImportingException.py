try:
    import termios
    import tty
    import sys
    import numpy

    def getkey():
        pass

except ModuleNotFoundError:
    print("Module not found")
    ValueError("Invalid module name")


except ImportError:
    import msvcrt

    def getkey():
        return msvcrt.getch()

finally:
    getkey()

