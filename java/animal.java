package com.hello.demo;
import java.io.IOException;

/**
 * Created by liusj on 17/6/11.
 */

public class Animal {
    public static void testClassMethod() {
        System.out.println("The static method in Animal");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Animal");
    }
public static class Cat extends Animal {
    public static void testClassMethod() {
        System.out.println("The static method in Cat");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Cat");
    }
}

public static void main(String[] args) throws IOException{
        Cat myCat = new Cat();
        Animal myAnimal = myCat;
        myAnimal.testClassMethod();
        myCat.testClassMethod();
        myAnimal.testInstanceMethod();
        myCat.testInstanceMethod();
}
}