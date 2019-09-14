---
layout: post
title:  "The Test Builder Pattern"
author: Chris
tags: engineering testing
---
Today I'm going to write about a design pattern I've been using heavily in unit testing, both in java and javascript: a test builder class.

This pattern helps make your test classes much more tidy and readable by centralising the logic for mocking and other setup, while keeping it flexible enough that it can be used consistently for all your tests.

A very simple example in Java with junit 5 and Mockito:

```

class FooTest {

    @Test
    @DisplayName("Should format a count of 2 correctly")
    void countOfTwo() {
        // Arrange
        Foo target = new FooTestBuilder().setBarCount(2).build();

        // Act
        String result = target.howMany();

        // Assert
        assertEquals("There are 2.", result);
    }

}

class FooTestBuilder {

    BarService mockBarService = Mockito.mock(BarService.class);

    public FooTestBuilder setBarCount(Integer count) {
        Mockito.when(mockBarService.count()).thenReturn(count);
        return this;
    }

    public Foo build() {
        return new Foo(mockBarService);
    }

}
```
Here our class under test is Foo, which relies on the BarService, provided to the class by dependency injection in the constructor. Since many of our tests will require mocking the dependencies of Foo, we can use the builder to abstract away the details from the individual tests.

Obviously this example is simple and the mocking here can easily be done as part of the test, but in more realistic scenarios where your class under test will have more dependencies, each with more methods, the flexibility of this setup is very valuable.

You can also provide setter methods, in addition, with a simple method like:
```
    public FooTestBuilder setBarService(BarService barService) {
        this.mockBarService = barService;
        return this;
    }
```
In this way you can still have your mock configured by the builder, but you can provide the reference yourself in your test, to enable verification of the called methods. This becomes valuable especially when your dependencies aren't particularly easy to mock, with static methods or objects that aren't injected (in Java I'd use PowerMock methods like mockStatic() and whenNew() to overcome these issues).


Additionally, this pattern (like builders in general) is very extensible - when there's a new dependency for Foo, adding it to the builder once will fix all our tests.

It's also very valuable for making tests easy to maintain as you refactor your classes, by abstracting the dependency structure of your class away from individual tests.

In the last few months I've found myself using this pattern for unit testing of almost all complex classes - and for abstracting away messy setup like [Angular TestBed](https://angular.io/api/core/testing/TestBed) and [Powermock](https://github.com/powermock/powermock), I've found it works extremely well.