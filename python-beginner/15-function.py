# function python


def greeting():
    return "Hello Yums"


greeting1 = greeting()
print(greeting1)

# argument & parameter
# parameter dan argument itu istilah yang berbeda, tapi penggunaan sama
# parameter -> variabel yang dimasukkan dalam fungsi yang didefinisikan
# argument -> value yang dimasukkan dalam fungsi ketika di panggil


def sayHello(name):  # name -> parameter
    return f"Hello {name}"


greeting2 = sayHello("Asraf")  # Asraf -> argument
print(greeting2)

# *agrs dan **kwargs
# *args -> menerima banyak argument
# **kwargs -> menerima argument key dan value


def count_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


count1 = count_numbers(1, 2, 3, 4, 5)
print(count1)

count2 = count_numbers(6, 7, 8, 9, 10)
print(count2)


def func_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    return kwargs


kwargs1 = func_kwargs(name="asraf", age=20)
print(kwargs1)

# * dan **
# * -> unpacking kumpulan value dalam sebuah tupple
# ** -> unpacking kumpulan key dan value


def count_numbers_other(a, b, c, d):
    return a + b + c + d


tuppleData = (11, 12, 13, 14)
count3 = count_numbers_other(*tuppleData)
print(count3)


def func_kwargs_other(name, fname):
    print(name)
    print(fname)


dict1 = {"name": "Asraf", "fname": "Muhmmad"}
func_kwargs_other(**dict1)


# scope
def myFunc():
    # local scope
    x = 3
    print(x)


# print(x) -> tidak bisa karena scope dari variable x hanya di function myFunction
myFunc()


# global scope
def myFunction():
    global y
    y = 5
    print(y)


myFunction()
print(y)  # bisa diakses diluar karena global variable


# nonlocal scope
def myFunctionn():
    x = "hai"

    def myFunctionnn():
        nonlocal x
        x = "hello"

    myFunctionnn()
    return x


print(
    myFunctionn()
)  # nonlocal digunakan agar variable local bisa diakses diluar, jadi nilai nya bisa dirubah jika memiliki variable yang sama di luar function nya


# decorator
# menerima function lain untuk dijalankan dalam sebuah function
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myInnerFunc():
    return "Yumas"


print(myInnerFunc())


# decorator menerima parameter
def showcase(n):
    def showcase(func):
        def myInner():
            if n == 1:
                a = func().upper()
            else:
                a = func().lower()
            return a

        return myInner

    return showcase


@showcase(1)
def myFunctionOke():
    return "Takayums"


print(myFunctionOke())
