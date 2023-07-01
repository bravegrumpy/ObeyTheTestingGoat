# Python Test Driven Development

This repo follows [Obey the Testing Goat](https://www.obeythetestinggoat.com/pages/book.html#toc) as a guide to python test driven web development.

I am using it specifically to enhance my Django Web Dev skills.

## Hosting

This project is hosted at:

Prod Server: <www.lists.ottg.bravegrumpy.com>
Staging Server: <staging.lists.ottg.bravegrumpy.com>
Testing Server: <test.lists.ottg.bravegrumpy.com>
Dev Server: <dev.lists.ottg.bravegrumpy.com>

## Beyond the Book

Once I've completed this book to the degree that I want to, I hope to:

- [ ] figure out how to containerize this application.
- [ ] found out if there is a free open source version of heroku/cf to push to.
- [ ] write a similar code, but with file i/o.

## Useful TDD Concepts

### Regression

When new code breaks some aspect of th eapplication that used to work.

### Unexpected Failure

When a test fails in a way we weren't expecting.  This either means htat we've made a mistake in our tests or that the tests have helped us find a regression, and we need to fix something in our code.

### Red/Green/Refactor

Another wya of describing the TDD process.  Writhe a test and see it fail(Red), write some code to get it to pass (Green), then refactor to improve the implementation.

### Triangulation

Adding a test case with a new specific example for some existing code, to justify generilizing the implementation. (which might be a "cheat" until that point.)

### Three strikes and refactor

A rule of thumb for when to remove duplication from code.  When two pieces of code look very similar, it oftey pays to wait until you see a third use case, so that you're more sure about what part of the code really is the common, re-usable part to refactor out.

### The scratchpad tod-do list

 A place to write things down that occur to us as we're coding, so that we can finish up what we're doing and come back to them later.

- I have implemented this using the Todo Tree extension, and Github's issue integration feature, so that each time I encounter something like this, I can use the issue workflow.
- In this project, I'm often manually closing issues as they are completed, but this creates infastructure for me to use the main/dev/issue branch strucutre in real projects.

### Ensure that tests don't affect each other

Use Django's test runner in order to create a test database for each run.

### Use a helper wait function

Instead of adding in sleeps where stuff should load, create a function that waits for exactly the right amount of time.

### Go from Working state to Working state with smallest amount of code possible

Do NOT try to fix everything at once. We do not like the refactoring cat.
The refactoring cat seems to be somthing I'm running into at work a little bit.

## Completed Chapters

- [x] [Chapter 7 -- Working Incrementally][Chapter 7]
- [x] [Chapter 6 -- Explicit Waits 1][Chatper 6]
- [x] [Chapter 5 -- Post and Database][Chapter 5]
- [x] [Chapter 4 -- Philosophy and Refactoring][Chapter 4]
- [x] [Chapter 3 -- Unit Test First View][Chapter 3]
- [x] [Chapter 2 -- unittest Module][Chapter 2]
- [x] [Chapter 1 -- Getting Django Set Up Using a Functional Test][Chapter 1]
- [x] [Prerequisites and Installations][Chapter 0]

## Changelog

2023-06-22 -- Setting up environment and stuff

[Chapter 0]: https://www.obeythetestinggoat.com/book/pre-requisite-installations.html
[Chapter 1]: https://www.obeythetestinggoat.com/book/chapter_01.html
[Chapter 2]: https://www.obeythetestinggoat.com/book/chapter_02_unittest.html
[Chapter 3]: https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html
[Chapter 4]: https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html
[Chapter 5]: https://www.obeythetestinggoat.com/book/chapter_post_and_database.html
[Chatper 6]: https://www.obeythetestinggoat.com/book/chapter_explicit_waits_1.html
[Chapter 7]: https://www.obeythetestinggoat.com/book/chapter_working_incrementally.html
