from MainPackage import main_script as main
#from MainPackage.SubPackage import subscript
#from MainPackage.SubPackage.subscript import hello_subscript заимпортит метод
from MainPackage.SubPackage.subscript import * # заимпортит все


main.hello_main()
hello_subscript()