from .atomic import (Regex)

letters = Regex("[a-zA-Z]+")
letter = Regex("[a-zA-Z]")
numbers = Regex("[0-9]+")
number = Regex("[0-9]")
optSpace = Regex(" *")
spacep = Regex(" +")