# Object Oriented Programming in Python

01. [Classes](https://github.com/arvimal/Python-and-OOP#01-classes)
02. [Instances, Instance methods, Instance attributes](https://github.com/arvimal/Python-and-OOP#02-instances-instance-methods-instance-attributes)
03. [Class attributes](https://github.com/arvimal/Python-and-OOP#03-class-attributes)
04. [The __init__ constructor](https://github.com/arvimal/Python-and-OOP#04-the-init-constructor)
05. [Inheritance (Inheriting {attributes,methods,constructors etc..})](https://github.com/arvimal/Python-and-OOP#05-inheritance-inheriting-attributesmethodsconstructors-etc)
06. [Encapsulation](https://github.com/arvimal/Python-and-OOP#06-encapsulation)
07. [Polymorphism](https://github.com/arvimal/Python-and-OOP#07-polymorphism)
08. [Instance methods](https://github.com/arvimal/Python-and-OOP#08-instance-methods)
09. [Multiple Inheritance and method/attribute lookup](https://github.com/arvimal/Python-and-OOP#10-multiple-inheritance-and-how-lookup-works)
10. [Method Resolution Order (MRO)](https://github.com/arvimal/Python-and-OOP#11-method-resolution-order-mro)
11. [Decorators](https://github.com/arvimal/Python-and-OOP#12-decorators)
12. [Static methods](https://github.com/arvimal/Python-and-OOP#13-static-methods)
13. [Class methods](https://github.com/arvimal/Python-and-OOP#14-class-methods)


# NOTES
------------
#### 01. Classes

Classes are the building blocks in Object Oriented Programming. 

Classes can be seen as blueprints from which you create your Instances. 

------------
#### 02. Instances, Instance methods, Instance attributes

------------
#### 03. Class attributes 

Attributes or methods specific to a class are called Class attributes 

Example:

```
class MyClass(object):
    value = 10
    
    def __init__(self):
        pass
```

Here `value` is a class attribute. These are used when certain values need to be set outside a function.

------------
#### 04. The __init__ constructor

The __init__() constructor is a magic method which gets called when a class is instantiated. 

Any attributes set under the __init__() constructor will be instantiated at the time of instance creation.

------------
#### 05. Inheritance (Inheriting {attributes,methods,constructors etc..})

-------------
#### 06. Encapsulation

------------
#### 07. Polymorphism

------------
#### 08. Instance methods

------------
#### 09. Multiple Inheritance and method/attribute lookup 

* Any class can inherit from other classes.
* Any python class can inherit from multiple classes at the same time.
* The class that inherits another class is called the Base/Child class.
* The class being inherited by the Child class is called the Parent class.
* The child class inherits any methods and attributes defined in the parent classes.
* Python uses a depth-first method resolution order (MRO) to fetch methods.
* When two classes inherits from the same class, from Python2.3 onwards, the MRO omits the first occurrence of the class.
* This new MRO lookup method applies from Python2.3, and is for the new-style classes.
	*NOTE:* New style classes inherits from the 'object' parent class.

------------
#### 10. Method Resolution Order (MRO)

* Python has a method lookup order, called `MRO` (Method Resolution Order)
* The MRO path can be printed to stdout using `print <class-name>.mro()`
* Python, by default, uses a depth-first lookup path for MRO.

* ie.. Imagine you have four classes, A, B, C, D.

  1. You instance is created from `D`.
  2. `D` inherits from `B` and `C`
  3. `B` inherits from `A`.
  4. Both `C` and `A` has a method with the same name.
  5. Since python follows a depth-first MRO, the method is called from `A`

REFERENCE: Check the code examples in:
  * 14-multiple-inheritance-1.py
  * 15-multiple-inheritance-2.py

In some cases, the inheritance can get quite cumbersome when multiple classes inherit from the same classes, in multiple levels. 

**NOTE** : From Python2.3, the MRO has changed slightly in order to speed up the method lookups.

The MRO lookup now skips/omits the initial occurrences of classes which occurs multiple time in the lookup path.

* Example:
  1. Four classes, A, B, C, D.
  2. D inherits from both B and C
  3. B inherits from A
  4. C inherits from A
  5. Both C and A contains a similar named method.
  6. Your instance in created from class D.
  7. You try a lookup for the method which is named both in A and C.
  8. The usual lookup should be D -> B -> A -> C -> A
  	a. Hence since the method exists in A and C, it should return from A.
  	b. But since the class A is occurring twice and due to the new MRO method, the lookup will be 
  	D -> B -> C -> A.
  9. The lookup should return the method from class C, rather than A.

REFERENCE: Check the code example in:
  * 16-multiple-inheritance-3.py

--------------
#### 11. Decorators

--------------
#### 12. Static methods

--------------
#### 13. Class methods

--------------

#### 14. Magic methods

Magic methods 



