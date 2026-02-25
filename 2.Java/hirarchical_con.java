// Parent class
class Animal {
    void eat() {
        System.out.println("eating...");
    }
}

// Child class 1
class Dog extends Animal {
    void bark() {
        System.out.println("barking...");
    }
}

// Child class 2
class Cat extends Animal {
    void meow() {
        System.out.println("meowing...");
    }
}

// Main class
public class hirarchical_con {
    public static void main(String[] args) {

        // Creating object of Cat
        Cat c = new Cat();
        c.meow();  // Cat's own method
        c.eat();   // Inherited from Animal

        // Creating object of Dog
        Dog d = new Dog();
        d.bark();  // Dog's own method
        d.eat();   // Inherited from Animal
    }
}
