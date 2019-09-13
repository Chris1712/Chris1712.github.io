---
layout: post
title:  ""
author: Chris
tags: testing engineering
---
Pattern for builders in java / js


Today I'm going to write about a design pattern I've been using heavily in unit testing, both in java and javascript: a test builder class.

This pattern helps make your test classes much more tidy and readable by centralising the setup logic for mocking, while keeping it flexible enough that it can be used consistently for all your tests.

A very simple example in Java:

// some code todo

Here our class under test is Foo, which relies on the BarService - which is provided by dependency injection. Since many of our tests will require 


Valuable because of flexibility in return, and extensibility - if there's a new method, or new service, it's straightforward to add it to the builder and fix every test.


It's also very valuable for making tests easy to maintain as you refactor your classes, by abstracting the dependency structure of your class away from individual tests. (give example)
