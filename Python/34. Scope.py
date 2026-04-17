# Variable scope = where a variable is visible and accessible
# Scope Resolution order = (LEGB) Local -> Enclosed -> Global -> Built in


def func1():
    a = 1  # a is local to func1
    print(a)


def func2():
    a = 2  # a is local to func2
    print(a)


def func1():
    a = 1  # a is local to func1

    def func2():
        print(a)

    func2()


func1()
# --------------------------------------------------------------------

# Global Scope
x = 10


def func1():
    print(x)


def func2():
    print(x)


func1()
func2()

# --------------------------------------------------------------------

