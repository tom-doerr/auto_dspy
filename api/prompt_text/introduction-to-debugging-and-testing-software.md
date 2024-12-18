# Debugging and Testing: An Introductory overview
In this introductory tutorial, I am going to explore and discuss the topics of debugging and testing software. The goal is to provide an introductory basis on how to approach testing and debugging for any code written in any language. Therefore, this material is not focused on any single language and provides a general principles that are applicable in debugging and testing any software, functions, and code.

## Learning Objectives
By the end of this tutorial, the reader should be able to:
1. Explain the meaning of debugging and describe atleast two approaches to debug their code.
2. Define and classify different testing techniques used in Software development.
3. Appraise why one testing technique is suitable for specific scenario than another.
4. Design and develop tests for evaluating software.

Imagine you are in the kitchen preparing your favorite meal or soup. Ideally, you would expect to start and finish without any problems. But in most cases, you encounter challenges. Let's take a simple case where insects like flies, spiders, and roaches keep falling in your meal. This means that before you serve your meal, you have to make sure it has no insects, that is, `debug it`.

## Debugging
Debugging is the process of eliminating bugs. In programming, you will debug a lot. During the software development, you must constantly check whether the code you have written is working the way you expect it to work, before you deploy it to the real world.

>The term "bug" is used to a limited extent to designate any fault or trouble in the
connections or working of electric apparatus.
*Hawkin's New Catechism of Electricity, 1896*

Let's finish our cooking analogy. What can you do to make sure there are no bugs in your soup/meal?
1. keep the lid closed to make sure bugs don't get in. In programming this is `defensive programming`. You try your best to write clean code.
2. Check for bugs in the soup. This is `testing` where you actively stir your soup hoping to catch any bug inside.
3. Eliminate the source of bugs by cleaning the kitchen.
4. Ignore the bugs and claim you have a new recipe for cooking soup with the bugs as a feature: *I discovered high-protein soup*. The buggy program becomes a product, with the bug shipped as a feature. There is no name for this coding style, but we can call it `dangerous programming` *(not recommended)*.

### Tips for debugging
- **Defensive programming attitude** - Defensive programming is a way of writing code. As a programmer, you write code that anticipates and handles potential errors and unexpected cases in your program. For every part of code you write, you are constantly asking yourself `what could go wrong?` and writing a piece of code that will run if `it actually goes wrong`.
- **Write specifications for all your functions**. Function specifications clearly define the expected behavior of the function, input requirements (parameters), output expectations (return values/types), and any constrains or assumptions. For example, let us consider a function that calculates the square root of a number. In the specification of this function, we can indicate that the input values or parameters must be non-negative integers, the precision of the output values such as 2 decimal places, handling of specific cases such as zero and negative values.
- **Modularization** - Break the code down into small units. Functions are great examples. Code blocks or modules help catch bugs quickly. _If it can be a function, make it a function._
- **Assertions** - This involves checking the condition of the input or output. _An assertion is a statement inside the code that verifies an assumption or a condition that should be true at a specific point during the execution of the program._ For example, assume you have a function that calculates the factorial of a positive integer. You can write an assertion that confirms that indeed the input is a positive number. If the input is not a positive number, the assertion will fail and raise an exception providing instant feedback that something is wrong.

## Testing
After writing a piece of code that does a specific task, you should test it to make sure it works or actually__*does it*__. Consider a car-maker. Before selling any car to actual customers in the market, the government requires the car maker and other third parties to test the car to ensure it is safe to drive. Similarly, you should test your code to make sure it works as expected.

Testing is a form of validation. Validation helps discover problems in a program. If no problems are found, it means your program's correctness is high. Other forms of validation other than _testing_ include _code reviews_ and _verification_.

---
> Even with the best validation, it’s very hard to achieve perfect quality in software. Here are some typical residual defect rates (bugs left over after the software has shipped) per kloc (one thousand lines of source code):
>- 1 - 10 defects/kloc: Typical industry software.
>- 0.1 - 1 defects/kloc: High-quality validation. The Java libraries might achieve his level of correctness.
>- 0.01 - 0.1 defects/kloc: The very best, safety-critical validation. NASA and companies like Praxis can achieve this level.
>
>This can be discouraging for large systems. For example, if you have shipped a million lines of typical industry source code (1 defect/kloc), it means you missed 1000 bugs!

---

### Importance of Testing
Testing involves using the function's or program's specifications to come up with a set of inputs and outputs and running your code against them. The goal is to find out if the program functions as expected.

While testing, assertions are used to ensure that the expected performance is achieved.

For example, consider a function that should return `True` when provided with a positive integer. To test this function, we can give it a positive integer as input and assert that the output is `True`.

Also, we can assert that the output is `not false`, or provide a non-positive integer, say zero or a negative number and assert that the output is `not true`.

Therefore, the basic idea in testing your code is coming up with a set of inputs and outputs, and asserting that the code performs as expected in the light of those inputs and outputs.

If unexpected behavior is observed during testing, it means the program or code is buggy and should be edited to handle such cases.

### Classes / Types of Tests
#### 1. Unit Testing
Unit testing involves validating a single piece of program such as testing a single function in the program.

A well-tested program will have written tests for each individual module within it. A **Unit Test** is a test that validates an individual module such as a function, or a Class in isolation.

Testing modules in isolation makes debugging an application easy. If a unit test fails, it means that the bug is inside the module, rather than everywhere else in the program. If a module passes the test, it means that the bug is not within the code in that module, thus no need to debug the code inside it. This is the real power of unit tests.

#### 2. Regression Testing
Regression testing involves validating that a piece of code works correctly after new features or functionalities have been included. It involves ensuring that functionalities that had been tested before the new feature, functionality, or edits still work correctly.

The two common aspects of regression testing include adding test for bugs as you find them and catching reintroduced errors that were previously fixed.
- *Adding tests for bugs as you find them*: When a bug is discovered, a regression test is created to reproduce the bug. This test is then added to the test suite to ensure that the bug does not reappear in the future. Regression testing helps to prevent the recurrence of known issues.

- *Catching reintroduced errors*: As the software evolves and new features are added or existing code is modified, there is a risk of inadvertently reintroducing bugs or breaking previously fixed functionality. Regression tests help identify such regressions, allowing developers to rectify them before releasing the software.

#### 3. Integration Testing
This type of testing involves validating that the various components of the program interact and function as expected. It involves testing and asserting the program works correctly as a whole.

While unit tests are focused on individual components of the program, the integration tests focus on ensuring that multiple units work together as a whole.

Verifying if the overall program works: Integration testing evaluates the functioning of different components when combined into a cohesive system. It assesses the communication, data flow, and compatibility between modules, subsystems, or services.

> **Common mistake is Rushing to do this**: Integration testing is often performed towards the later stages of the software development process, closer to the release. Due to time constraints or development delays, there is sometimes a tendency to rush through integration testing, potentially leading to overlooking certain issues. However, it is crucial to allocate sufficient time and resources for comprehensive integration testing to ensure the overall system's reliability and stability.

## Software Testing Techniques
This far, we have looked at the different ways testing is achieved. But how do you decide how you will write the tests to your program? On what basis do you test a function, or a class, or the entire program? Do you test based on the specification, the way code is implemented, or maybe follow your gut? _How does the gut even know what to do?_


> Just a reminder, a **specification** _refers to the description of the function’s behavior, that is, the types of parameters, type of return value, and constraints and relationships between them._


There are two fundamental approaches to testing programs: black box and white box testing. Let's explore both of them.
### A. Black Box Testing
Black box testing refers to creating tests that are derived entirely from the specification of the function or the program. This means that the test cases are developed by looking at the definition of the function through its specification.

The objective of black box testing is to identify defects or inconsistencies between the expected behavior and the actual behavior of the software. It aims to ensure that the software meets the specified requirements, works correctly with various inputs, and produces the desired outputs.

In this test approach, the tests are designed without looking at the code. Testers design test cases based on functional specifications, user stories, or use cases, and execute them to validate the software's behavior.

There are two advantages we can derive from this approach. First, testing can be done by someone other than the implementer to avoid some implementer biases. Also,testing can be reused if implementation changes.

### B. White Box Testing
White box testing involves looking at how the code is implemented to guide the design of test suites. All the possibilities that can occur based on the code implementation are considered during the design of a test suite.

Testers design test cases based on the internal structure of the software, including code branches, loops, and data structures. They may perform techniques like `code coverage analysis`, unit testing, and debugging to validate the software's correctness and efficiency.

This methodology has some significant drawbacks. First, it is easy to miss some paths or possibilities because some functions can have numerous pathways. Consider loops, how many paths do you need to consider and how many are you likely to miss?

Another drawback is that some loops can require tests going through them arbitrary amount of times.

Some tricks in dealing with white box testing is to ensure that tests cover all possible branches of the loop conditional. While dealing with for loops, ensure that you test when the loop is not entered, when the loop is only executed once, and when the body of the loop executes more than once. Similar case applies while working with while loops by including all cases that include the loop exit in your test suite.

### Let us now briefly discuss other useful testing techniques that you will come across.
1. **Equivalence Partitioning Testing** - This approach is used in black box testing in which, a range of values, inputs, or outputs are divided into two partitions: valid and invalid partitions. The valid partition consists of values or inputs that are accepted by the test object as valid from the specifications. The invalid partition consists of a set of test values or inputs that are invalid and should produce unintended outcomes or errors.
2. **Boundary Value Analysis** - This is a black box technique that extends equivalence partitioning. The tester focuses on the values at the boundary of valid and invalid partitions. Boundary value analysis can take two forms, two-value and three-value analysis. In two-value analysis, the test examines the minimum and maximum values of the boundary, while in three-value analysis the test focuses on the value before the boundary, at the boundary, and just after the boundary. In most cases, boundary value analysis and equivalence partitioning are used together to increase test coverage.
   1. **Decision Table testing** - The decision table testing involves testing the behavior of the code, system, or text object in presence of different combinations of inputs. In this approach to testing, there are predefined rules, cases, or conditions that are required for the test object. For example, a login functionality that accepts a valid password and a valid username has two predefined possible outcomes, the home screen after successful login, and the error screen if details are wrong. A decision table can be used to design tests using different combinations of password and username through cause-effect table as follows.

| Condition   | test-1 | test-2 | test-3 | test-4 | 
|-------------|--------|--------|--------|--------|
| username    | True   | False  | False  | True   |
| Password    | False  | False  | True   | True   |
| Home screen | False  | False  | False  | True   |

      The decision table testing is very effective for evaluation of code that integrates business logic.
3. **State transition testing** - It is a software testing technique that focuses on testing the behavior of a system or software application as it transitions between different states. It is particularly useful for systems that have distinct states and where the behavior depends on the current state and the transitions between states.
    <details>
    <summary>To understand better, let us use an illustrative analogy of the ATM.</summary>
    Initially, the ATM is in the `state` of idleness that is just displaying a default screen. This state changes when an ATM card is entered. Entering the ATM card triggers an `event` that changes the initial state. Each user action, triggers an event, that triggers a system event. For example, when the user enters their PIN, the ATM initiates a system event that verifies the PIN is correct. Therefore, the _state transition testing_ involves testing the system while in different states.</details>

These are just some approaches you can use in testing your code. Others you should definitely check out include
+ Use case-based testing.
+ Gray box testing - which basically combines black box and white box techniques.
+ Automation Testing.
+ Smoke Testing.
+ Security Testing.
+ User Acceptance Testing

Generally, this introduction material has covered debugging, and testing. With these concepts, you should have a significant understanding of software debugging and testing. The next recommended steps is to familiarize yourself with language-specific testing environments and the best practices in testing.
> If you are using PHP, you should check out [PHPUNIT](https://phpunit.de/) or [Pest](https://pestphp.com/) which are testing tools to help you create and run tests on your code and applications. For python check out [Pytest](https://pytest.org/) or unittest. For Ruby, check out RSpec and Cucumber.

# References
* [Lecture 7:Testing, Debugging, Exceptions, and Assertions (MIT OCW)](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-7-testing-debugging-exceptions-and-assertions/)
* [Reading 3: Testing (MIT OCW)](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/03-testing/)
* [Reading 11: Debugging (MIT OCW)](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/11-debugging/)
* [Software Testing Techniques - geeksforgeeks.com](https://www.geeksforgeeks.org/software-testing-techniques/)

I hope you had fun reading about debugging and software testing. I am [Francis Njuguna](https://github.com/mwanginjuguna/) and my goal is to share information about programming and software engineering as I learn and practice. Feel free to leave feedback or add a contribution to [GitHub repo](https://github.com/mwanginjuguna/software-testing/).

Bye for now, Cheers.
