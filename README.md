# LearnPython
Learn Python

# Learning Path
## Python Fundamentals
- Basics
- Data Types and Variables
  - integer, float, boolean, string
- Operators
  - arithmetic (PEMDAS: ()  **  %  *  /  //  +  - )
  - comparison (>  <  >=  <=  ==  !=  is  is not)
  - assignment ( =  **=  %=  *=  /=  //=  +=  -=  |=  &=  ^=  >>=  <<= )
  - logical (or and not)
  - bitwise ( |  &  ^  ~  <<  >> )
  - string
- Conditional statements
  - if-else, if-elsif-else
- Loops
  - for iter in range
  - while condition
  - break, continue, pass
  - nested if and while loops
  - iterating through range vs list
  - while versus for (see Fibonacci example)
- Functions
  - Mutable parameters: lists
  - Immutable parameters: scalars
  - Built-in functions
  - Cast functions (type conversions)
  - Lambda functions (used when function needed as arguments to other functions)
  - Recursive functions
- Recursion vs Iteration
  - Recursion when we want to chunk data
  - Iteration when we want to traverse data, and retain program scope

## Object Oriented Programming in Python
- Procedural vs OO
  - Procedures/methods driven vs object driven (classes and objects).
  - OOP represents real world closely - an application is designed as a collection of objects that interact with each other to accomplish the goals.
- Classes and Objects
  - *Objects*: collection of *data* and *behaviors*
  - *Class*: a *blueprint* for creating objects
  - State of the object modeled using *variables/attributes/properties/members*, and behavior is modeled using *methods/member functions*.  Primitive data types model state of the object, *user defined data types* model state and behavior.
  - Adding property outside of a class (only in a specific object)
- Class and Instance variables
  - Class variables - shared by all object instances of the class.  A change in class variable will impact all objects of the class.  Do not define class variables outside the __initializer__, unless they are constant for all object instances.
  - Instance variables - specific and unique to an object instance.
  - Use __init__ to initialize all properties/variables.  Not doing so can result in "AttributeError: 'Class' object has no attribute 'attribute'", and also it is bad practice to not initialize
- Methods: Instance, Class, and Static methods
  - Instance method: most common - works on instance variables/parameters. Instance methods can also access the class through self.__class__ attribute, and hence modify class state.
  - Class method: works on class variables, with *@classmethod* decorator and *cls* parameter.  They cannot modify object instance state.
  - Static method: independent of class variables - cannot access or modify class variables, and know nothing about class state. Utility methods that can take any set of parameters and work on them.  They are a way to implicitly [namespace](https://realpython.com/python-namespaces-scope/) methods during development as class-affecting and non-class-affecting - as in for testing scenarios. Reference: [Notes on methods](https://realpython.com/instance-class-and-static-methods-demystified/)
  - Parameters - first parameter in a method definition (not invocation) MUST ALWAYS be *self*
  - *self* argument
  - return statement
  - method overloading is *implicit*, not explicit - by adding optional arguments and assigning default values to the arguments. Done so to save cost, memory efficiency, tighter and brief code, polymorphism. 
- Attributes
  - Public - attributes that can be accessed inside and outside a class.  In Python, all attributes are public unless explicitly defined otherwise.
  - Private - specified using leading double underscore nomenclature.
- Information Hiding - hide the class implementation, allow other classes to interact with this class via public interfaces
  - Two key concepts and enablers of information hiding: *Encapsulation* and *Abstraction*
  - Encapsulation - bind data and methods to manipulate the data together in a single unit (class). Hide the state and representation of the object from outside. Main advantages: easy maintenance, properties can be specified easily, you can control which external classes can access class properties.
  - Declare variables to be *private*; implement public getter and setter methods to access them.
- Abstraction
  - Skipped - will return to this
- Inheritance
  - *class* is a sub-class of Python *object class*
  - Parent class (super class/base class) - allows reuse of its public properties in another class.
  - Child class (sub class/derived class) - has all public attributes of the base class, inherits from and/or extends the base class.
  - Inheritance via BaseClass.__init__(), *super()* for child class to refer to base class properties; it can be specified in any order in the constructor, allowing child class to manipulate base class properties at creation.
- Types of Inheritance: (a) Single (b) Multi-level (c) Hierarchical (d) Multiple (e) Hybrid
  - Single: super --> subclass
  - Multilevel: subclass <-- subclass <-- super
  - Hierarchical: subclass1 <-- super --> subclass2
  - Multiple: super1 --> subclass <-- super2
- Benefits of inheritance:
  - Code reuse - common properties and methods go into super class, to be inherited and used by subclases
  - Scoped maintenance - lesser number of places to change the logic or algorithm.
  - Extensibility - base class can be extended in the derived class as per application requirements.
  - Information hiding - encapsulation of private data and exposure of only the necessary public data and methods.
- Polymorphism: ability of an object to take on different shapes and exhibit different behaviors
  - Polymorphism with methods - same method in base class with different implementations in subclasses
  - Polymorphism with inheritance - subclasses inherit properties and methods from base class and extend them.
  - Method overloading - redefining a base class method in the subclass.
  - Overloading built-in operators: \_ \_add\_ \_(self, other), \_ \_ sub\_ \_(self, other), \_ \_mul\_ \_(self, other), \_ \_truediv\_ \_(self, other), \__lt__(self, other), \_ \_gt\_ \_(self, other), \_ \_eq\_ \_(self, other)
  - Duck Typing - polymorphism without inheritance: type(x) statement. Have a set of classes with same method name.  If the objects passed into the invoking class have the method defined, then you can exercise different behaviors from the invoking class.
- Abstract Base Class - when duck typing won't work - when we cannot implement functions without worrying about strict data typing.
  - Abstract class with abstractmethod - *from abc import ABC, abstractmethod*
- Object Relationships:
  - Association: *part-of*, *has-a* . Two types: aggregation, composition
  - Aggregation follows has-a model.  The lifetime of the owned object is not dependent on the lifetime of the owner object.  The parent contains only a reference to the child, which can be delinked.
  - Composition is the practice of accessing other class objects in your class. In such a scenario, the class which creates the object of the other class is known as the *owner* and is responsible for the lifetime of that object.  Composition involves *Part-of* relationships where the part must constitute a segment of the whole object. We can achieve composition by adding smaller parts of other classes to make a complex unit.
  - Inheritance: *is-a*, 

## Data Structures and Algorithms in Python
## Advanced Concepts

# References
1. Educative IO [Python Fundamentals](https://www.educative.io/module/python-fundamentals-for-programmers)
1. Python Crash Course 2nd Ed [Basics](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/part01.xhtml#part01)
1. Python [Built-in functions](https://docs.python.org/3/library/functions.html)