# OOP in TypeScript

## 1. What Is OOP?

OOP (Object-Oriented Programming) is a programming style where we structure our code using classes and objects.
1. Encapsulation — protect data and control access.
2. Inheritance — reuse code from parent classes.
3. Polymorphism — use the same method with different implementations.
4. Abstraction — expose essential behavior while hiding implementation details

OOP helps you:
- Organize code.
- Reuse code through inheritance.
- Protect data through encapsulation.
- Model real-world things using objects.

Key concepts:
- class defines a blueprint.
- constructor() initializes an object.
- this refers to the current instance.
- new creates an object.
- void means the method doesn't return a value.

## 2. Class and Object

- Class → A blueprint for creating objects.
- Object → An instance of a class.

```ts
class Person {}

const person1 = new Person();
```

## 3. Attributes and Methods

- Attributes → Variables or properties inside a class.
- Methods → Functions inside a class.

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    greet(): string {
        return `Hello, I'm ${this.name} and I am ${this.age}`;
    }
}

const p1 = new Person("Ebraam", 22);
console.log(p1.greet());
```

Output:

```ts
Hello, I'm Ebraam
```

## 4. The `constructor` Method

In TypeScript, `constructor()` 
It runs automatically when you create an object using `new`.

```ts
class Person {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

const p1 = new Person("Ebraam");
console.log(p1.name);
```

Output:

```ts
Ebraam
```

## 5. The `this` Keyword

In TypeScript, `this` refers to the current object

```ts
class Person {
    constructor(public name: string) {}

    greet(): string {
        return `Hello, ${this.name}`;
    }
}

const p1 = new Person("Ebraam");
console.log(p1.greet());
```

Note: TypeScript supports parameter properties. Writing `public name: string` in the constructor automatically declares and initializes the property, so you don't need to write `this.name = name` separately.

## 6. Encapsulation (Data Protection)

TypeScript provides access modifiers such as `public`, `private`, and `protected`.
Encapsulation controls how data is accessed or modified using access modifiers.

```ts
class Bank {
    private balance: number;

    constructor(balance: number) {
        this.balance = balance;
    }

    getBalance(): number {
        return this.balance;
    }
}

const bank = new Bank(1000);

console.log(bank.getBalance());
// console.log(bank.balance); // Error: private property
```

- `public` → Accessible from anywhere (the default).
- `private` → Accessible only inside the class.
- `protected` → Accessible inside the class and its subclasses.

Note: TypeScript's `private` is primarily enforced by the type checker. JavaScript's `#balance` syntax provides runtime-enforced private fields.

## 7. Inheritance

Inheritance allows one class to reuse properties and methods from another class using `extends`.
Inheritance reuse code from parent classes.

```ts
class Animal {
    speak(): string {
        return "Animal speaks";
    }
}

class Dog extends Animal {
    override speak(): string {
        return "Woof!";
    }
}

const d = new Dog();
console.log(d.speak());
```

Output:

```
Woof!
```

`override` explicitly indicates that a subclass is replacing an inherited method. It is supported in modern TypeScript.

## 8. Multiple Inheritance

TypeScript does not support multiple class inheritance. A class can extend only one class.

However, you can implement multiple interfaces or combine behaviors using other techniques.

```ts
class A {
    methodA(): string {
        return "A";
    }
}

class B {
    methodB(): string {
        return "B";
    }
}

interface HasA {
    methodA(): string;
}

interface HasB {
    methodB(): string;
}

class C implements HasA, HasB {
    methodA(): string {
        return "A";
    }

    methodB(): string {
        return "B";
    }
}

const c = new C();
console.log(c.methodA(), c.methodB());
```

Output:

```
A B
```

Important: `implements` checks that a class satisfies an interface; it does not inherit method implementations from other classes.

## 9. Polymorphism

Polymorphism allows different classes to provide their own implementations of the same method.
Polymorphism use the same method with different implementations.

```ts
class Cat {
    sound(): string {
        return "Meow";
    }
}

class Dog {
    sound(): string {
        return "Woof";
    }
}

const animals = [new Cat(), new Dog()];

for (const animal of animals) {
    console.log(animal.sound());
}
```

Output:

```ts
Meow
Woof
```

TypeScript uses structural typing, so unrelated classes can be used together when they have compatible methods.

## 10. Abstraction

Abstraction hides implementation details and defines what subclasses must provide.

In TypeScript, you can use `abstract` classes and methods.
private side: number declares a private property called side and initializes it with the constructor argument.
- An `abstract` class cannot be instantiated directly.
- An `abstract` method must be implemented by a concrete subclass.
- `super()` calls the parent class constructor.


```ts
abstract class Shape {
    abstract area(): number;
}

class Square extends Shape {
    constructor(private side: number) {
        super();
    }

    override area(): number {
        return this.side * this.side;
    }
}

const square = new Square(5);
console.log(square.area());
```

Output:

```ts
25
```

## Quick revision: Python vs TypeScript OOP

| Concept            | TypeScript                            |
| ------------------ | ------------------------------------- |
| Create a class     | `class Person {}`                     |
| Create an object   | `new Person()`                        |
| Constructor        | `constructor()`                       |
| Current object     | `this`                                |
| Inheritance        | `class Dog extends Animal {}`         |
| Parent constructor | `super()`                             |
| Private property   | `private balance`                     |
| Abstract class     | `abstract class`                      |
| Class-level method | `static` method (not identical)       |
| Static method      | `static` method                       |
| Type annotations   | Built into the language's type system |
