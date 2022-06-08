=====================
 Combinatorics Pages
=====================
 .. toctree::
       :maxdepth: 2

       Type2.rst

=====================
Combinatorics
=====================


Type 1 - Arrangement with Repetition
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In this section, we present some tasks involving arrangement with repetition
problems. In our 2x2 grid, this is the cell in which unrestricted repetition
is allowed, and we are counting ordered outcomes (or arrangements). In problems
like these, we can employ multi-stage processes, where we have the same number
of options at each stage because repetition is allowed.

For instance, consider the following problem: ::

  1. "How many length 5 binary strings are there?"

Here, we have five positions, and we can employ a five-stage process where we
consider the number of options at each position. Since there are 2 options
(0 or 1) at each position no matter the choice of any previous position, we
use the multiplication principle to get 2 * 2 * 2 * 2 * 2 = 2^5 = 32 total
outcomes.

Below is some code that generates all of the outcomes. Notice the nature of the
outcomes themselves - repetition is allowed (something like 0 0 0 0 0 is a valid
outcome), and we are counting ordered outcomes (1 0 0 0 0 and 0 0 0 0 1 are
listed as distinct outcomes).

Active Code 1
-------------

.. activecode:: CodeSample1
   :coach:
   :caption: Code that generates length 5 binary strings

   Digits = [0,1]
   counter = 0
   for i in Digits:
       for j in Digits:
           for k in Digits:
               for l in Digits:
                   for m in Digits:
                       print(i,j,k,l,m)
                       counter += 1
   print(counter)

Now, answer the following questions about these outcomes.

Quick Check 1.1
----------------

.. mchoice:: QC1_1
   :correct: c
   :answer_a: 16 outcomes start with 01
   :answer_b: 4 outcomes start with 01
   :answer_c: 8 outcomes start with 01
   :feedback_a: Incorrect.
   :feedback_b: Incorrect.
   :feedback_c: Correct. 8 outcomes start with 01, as there are 8 possible outcomes for the remaining three positions once 0 and 1 are in the first positions.

   How many outcomes start with 01?

Quick Check 1.2
----------------

.. mchoice:: QC1_2
   :correct: b
   :answer_a: 10101
   :answer_b: 10110
   :answer_c: 11111
   :answer_d: 10111
   :feedback_a: Incorrect. 10101 is the 22nd outcome in the list.
   :feedback_b: Correct. 10110 is the 23rd outcome in the list.
   :feedback_c: Incorrect. 11111 is the 32nd outcome in the list.
   :feedback_d: Incorrect. 10111 is the 24th outcome in the list.

   Following the process that the code represents, what is the 23rd outcome
   in the list?


Let's look at a couple more examples. ::

  2. There are 12 people competing for three different prizes. The same person
  can win multiple prizes, but there are no ties. How many possible outcomes are
  there for how the prizes can be distributed to the people?

Note we can think of a three-stage process, where we give out a first,
second, and third prize. For each stage, any of the 12 people can win, no
matter who was picked previously. Thus, there are 12 choices for each of the
three prizes, so our answer is 12 * 12 * 12 = 12^3 = 1728.

The program below will list all of the outcomes. Run the program below, and
again observe the outcomes.

Active Code 2
--------------

.. activecode:: Codesample1
   :coach:
   :caption: Code that generates arrangements of people

   People = ['A','B','C','D','E','F','G','H','I','J','K','L']
   counter = 0

   for i in People:
       for j in People:
           for k in People:
               print(i,j,k)
               counter += 1
   print(counter)

Now answer the following questions about this code.

Quick Check 2.1
----------------

.. mchoice:: QC1_3
   :correct: b
   :answer_a: Person A and Person G do not receive prizes
   :answer_b: Person A receives the first prize and the third prize, and Person G receives the second prize
   :answer_c: Person A receives the first prize, and Person G receives the second and third prizes
   :feedback_a: Incorrect.
   :feedback_b: Correct. The each term in the output shows who received each respective prize. Because people can receive multiple prizes, here A won two prizes (first and third) and G won the second prize.
   :feedback_c: Incorrect.

   What does the outcome AGA represent in the context of the problem?

Now, let's consider the following problem: ::

  3. I am going to roll a 6-sided dice four consecutive times. How many
  possible outcomes are there for that sequence of four rolls?

Quick Check 3.1
----------------

.. mchoice:: QC1_4
   :correct: d
   :answer_a: 4
   :answer_b: 24
   :answer_c: 10
   :answer_d: 6
   :feedback_a: Incorrect. We are rolling four times, but there are 6 options for what can occur on each roll.
   :feedback_b: Incorrect.
   :feedback_c: Incorrect.
   :feedback_d: Correct. There are 6 options for what will come up on a given roll, one for each face of the dice.

   If you were to write code to produce outcomes, how many elements would you
   have in your starting list?

Quick Check 3.2
----------------

.. mchoice:: QC1_5
   :correct: b
   :answer_a: 6
   :answer_b: 4
   :answer_c: 10
   :answer_d: 24
   :feedback_a: Incorrect. You have six options per roll, but you are rolling the dice four times.
   :feedback_b: Correct. You are rolling four times, and each roll represents a stage in the counting process.
   :feedback_c: Incorrect.
   :feedback_d: Incorrect.

   If you were to write code to produce outcomes, how many nested for loops
   would you have?

Quick Check 3.3
----------------

.. mchoice:: QC1_6
  :correct: a
  :answer_a: 6 * 6 * 6 * 6
  :answer_b: 4 * 4 * 4 * 4 * 4 * 4
  :answer_c: 6 * 4
  :answer_d: 6 + 6 + 6 + 6
  :feedback_a: Correct. Each time you flip, you have 6 possible outcomes (no matter what was rolled previously); as you are rolling 4 times, using the multiplication principle we yield 6*6*6*6.
  :feedback_b: Incorrect.
  :feedback_c: Incorrect.
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes?

Now, in the space below, write code that generates all possible outcomes for
rolling a 6-sided dice four consecutive times.

Active Code 3
-------------

.. activecode:: CodeSample3
   :coach:
   :caption: Code that counts four consecutive dice rolls



Now, consider a couple of variations on this problem. ::

   4. Suppose now I want to roll a 6-sided dice eight consecutive times. What
   is a mathematical expression for the number of outcomes?

Quick Check 4.1
----------------

.. mchoice:: QC1_7
  :correct: c
  :answer_a: 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6
  :answer_b: 8 * 8 * 8 * 8
  :answer_c: 6 ^ 8
  :answer_d: 8 * 8 * 8 * 8 * 8 * 8
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct. There are eight dice rolls, each of which has 6 options; using the multiplication principle we get 6*6*6*6*6*6*6*6 = 6^8.
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes for this problem?

::

    5. How many outcomes are there for rolling a 4-sided dice six consecutive
    times? What is a mathematical expression for the number of outcomes?

Quick Check 5.1
----------------

.. mchoice:: QC1_8
  :correct: b
  :answer_a: 6 + 6 + 6 + 6
  :answer_b: 4 * 4 * 4 * 4 * 4 * 4
  :answer_c: 6 ^ 4
  :answer_d: 4 + 4 + 4 + 4 + 4 + 4
  :feedback_a: Incorrect.
  :feedback_b: Correct. We roll the dice six times, and there are four options at each stage in the process.
  :feedback_c: Incorrect
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes for this problem?

::

   6. How many outcomes are there for rolling a 20-sided dice three times? Remix
   code from above to write code that would generate all possible outcomes.


Active Code 4
--------------

.. activecode:: Codesample4
  :coach:
  :caption: Code that generates outcomes of rolling a 20-sided dice three times.



General formula for Arrangements with Repetition
-------------------------------------------------

We now discuss a general formula for these kinds of problems.

Notice that there is a commonality among the mathematical expressions that
solve this particular kind of problem. In general, if we have *n* distinct
objects, and we are arranging *r* of them, where repetition is allowed, there
are *n^r* total outcomes.

To see why this works, note that if we are arranging *r* elements, we can
think of *r* stages in our counting process, and at each stage we consider how
many options there are at that stage. Since repetition is allowed, we have *n*
options at each stage. These are independent choices at each stage, and using
the multiplication principle, we multiply *n* together *r* times, giving
us *n^r*.

In terms of coding problems like this, notice that we can have *n* elements in
our initial list, and we have $r$ nested for loops without restriction. These
correspond to the *r* stages in our counting process, where at each stage we
are cycling through all *n* options in our list. ::

  7. How many different license plate are there that consist of three letters,
  followed by three numbers?


.. parsonsprob:: PP_licenseplates
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Numbers = [0,1,2,3,4,5,6,7,8,9]
   Letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
   'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   =====
   counter = 0
   =====
   for i in Letters:
   =====
       for j in Letters:
   =====
           for k in Letters:
   =====
               for l in Numbers:
   =====
                   for m in Numbers:
   =====
                       for n in Numbers:
   =====
                           print(i,j,k,l,m,n)
                           print(counter)
   =====
   print(counter)


Coordinating multiple applications of this formula
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As is often the case, most problems will not be only a direct application of
this formula, but rather they will involve or incorporate that formula in some
way into a broader problem. Here we offer some examples of how this formula
might arise or be used in problems. ::

  7. How many different license plates involving three letters and three digits
  are there if the three letters appear together at the beginning of the license
  plate?

Notice here that there are two cases, each of which involves our formula. In
both cases we are considering 26 options for each letter and 10 options for
each digit; the multiplication principle applies in each case.

In one case, the three letters are at the beginning of the license plate. Then
there are 26 * 26 * 26 * 10 * 10 * 10 or 26^3 * 10^3 = 17,576,000 total
license plates.

In the other case, the three letters are at the end of the license plate. Then
there are 10 * 10 * 10 * 26 * 26 * 26 or 10^3 * 26^3 = 17,576,000 total
license plates.

These are distinct cases, so we can add the total together, so our total number
of license plates is 26^3 * 10^3 + 10^3 * 26^3 = 35,152,000.

.. parsonsprob:: PP_licenseplates2
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Numbers = [0,1,2,3,4,5,6,7,8,9]
   Letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
   'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   =====
   counter = 0
   =====
   for i in Letters:
       for j in Letters:
           for k in Letters:
   =====
               for l in Numbers:
                   for m in Numbers:
                       for n in Numbers:
   =====
                           print(i,j,k,l,m,n)
                           counter += 1
   =====
   for a in Numbers:
       for b in Numbers:
           for c in Numbers:
   =====
               for d in Letters:
                   for e in Letters:
                       for f in Letters:
   =====
                           print(a,b,c,d,e,f,g)
                           counter +1 =
   =====
   print(counter)


Now let's try another problem. ::

  8. At my bank, a PIN number consists of 4 digits (from 0 to 9). How many PIN
  numbers are there with no consecutive digits?

Note, here, we can apply our formula. We can think of a 4-stage process, where
in each stage we consider the number of options for each respective digit
(first, second, third, and fourth). In the first stage we can choose any number,
so there are 10 options. In the second stage, we can choose any number except
what was chosen first, so there are 9 options. In the third stage, we can choose
any number except what was chosen directly previously, so again there are 9
options. In the fourth stage, again we have 9 options.

So, our final answer is 10 * 9^3 = 7,290.

To code this, note that for our later stages we include a conditional statement
that doesn't allow for the previous letter to be included. Run the code and
examine the output.

Active Code 5
--------------

.. activecode:: CodeSample5
   :coach:
   :caption: Code that counts PIN numbers with no consecutive digits.

   Digits = [0,1,2,3,4,5,6,7,8,9]
   counter = 0

   for i in Digits:
       for j in Digits:
           if j != i:
               for k in Digits:
                   if k != j:
                       for l in Digits:
                           if l != k:
                               print(i,j,k,l)
                               counter += 1
   print(counter)


Quick Check 8.1
----------------

.. mchoice:: QC1_9
  :correct: b
  :answer_a: It makes sure the second digit is not the same as the first digit.
  :answer_b: It makes sure the third digit is not the same as the first digit.
  :answer_c: It makes sure the third digit is not the same as the second digit.
  :answer_d: It makes sure the third digit is not the same as either of the first two digits.
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct. All we need for this problem to ensure non-consecutivity is to have each digit not be equal to the digit directly preceding it. Thus, "if k != j" ensures the third digit is not the same as the second digit.
  :feedback_d: Incorrect.

  What does the conditional statement "if k != j" accomplish?



NOTE: STOP READING HERE
:::::::::::::::::::::::::::

Type 2 - Arrangement without Repetition - Permutations
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In this section, we present some tasks involving arrangement without repetition
problems. In our 2x2 grid, this is the cell in which repetition is not allowed,
and we are counting ordered outcomes (or arrangements). In problems like these,
we can employ multi-stage processes, where the number of options is reduced at
each stage, because repetition is not allowed.

For instance, consider the following problem: ::

  1. "How many arrangements are there of the numbers 1, 2, 4, and 4?"

Here, we have four positions, and we can employ a 4-stage process we consider
the number of options at each position. Note that once a number is selected
for the first position, that number now cannot be used again, so the number of
options for the second position is reduced by 1. The same is true for the third
and fourth positions. Because there is the same number of options no matter what
particular element was chosen at each stage, the number of options are
independent, and so we can use the multiplication principle. We get
4*3*2*1 = 24  total outcomes.

Below is some code that generates all of the outcomes. The j != i is means j is
not equal to i. This ensures that the choice for the second position will not
be equal to the choice for the first position. Thus, these conditional statements
ensure that an element cannot be repeated.

Notice the outcomes themselves - repetition is not allowed (we do not get
something like 1 1 1 1 or 2 4 1 4), and we are counting ordered outcomes
(1 2 3 4 and 2 1 4 3 are listed as distinct outcomes).

Active Code
------------

.. activecode:: CodeSample6
   :coach:
   :caption: Create some code

   Numbers = [1, 2, 3, 4]
   counter = 0

   for i in Numbers:
     for j in Numbers:
       if j != i:
         for k in Numbers:
           if k != j and k != i:
             for l in Numbers:
               if l != k and l != j and l != i:
                 print(i,j,k,l)
                 counter += 1
   print(counter)

As another example, consider the following problem. ::

  2. How many ways are there to arrange three friends, John, Angel, and
  Dan in a row?

This is an arrangement without repetition problem because we are counting
ordered arrangements (John, Dan, Angel is a distinct arrangement than Angel,
Dan, John). And, once a friend is placed in a position, they cannot sit in
another position, and so repetition is not allowed. (That is, we will never
have an outcome like John, John, John, as that does not make sense in the
context of the problem.) How many arrangements are there of three friends?
What is a mathematical expression for this?

Below, write a program that will list all outcomes of arranging these three
friends. Check to see if you get what you expect, and look at the outcomes
to see if they make sense.

Active Code
------------

.. activecode:: CodeSample7
   :coach:
   :caption: Create some code

   Friends = ['Angel', 'Dan', 'John']
   counter = 0

   for i in Friends:
       for j in Friends:
           if j != i:
               for k in Friends:
                   if k != j and k != i:
                       print(i,j,k)
                       counter += 1
   print(counter)


::

  3. How many ways are there to arrange the letters in the word ROCKET?

What is a mathematical expression for this, and how many arrangements are
there? Why is this problem an arrangement without repetition problem?

Section 3: Links
::::::::::::::::

Runestone uses the ``restructuredText`` (rst) markup language.  We chose this over markdown largely because rst is extensible.  Nearly all of the basic markup tasks are already handled by restructuredText.  You should check out the docs for the basics of restructuredText (link below). Our extensions are all for the interactive elements.  One key hint about restructuredText:  Its like **Python** -- *indentation matters!*

* `restructuredText Docs <http://docutils.sourceforge.net/rst.html>`_
* `Runestone Docs <https://runestone.academy/runestone/static/authorguide/index.html>`_
* Join the discussion on our `Google Group <https://groups.google.com/forum/#!forum/runestone_instructors>`_
* Tell us about problems on `Github <https://github.com/RunestoneInteractive/RunestoneComponents>`_


SECTION 4: Sample Directives
::::::::::::::::::::::::::::

ActiveCode
----------

.. activecode:: codeexample2
   :coach:
   :caption: This is a caption

   print("My first program adds a list of numbers")
   myList = [1, 2, 3, 4, 5]
   total = 0
   for num in myList:
       for num2 in myList:
            print(num,num2)
            total = total + 1
   print(total)

Multiple Choice
---------------

.. mchoice:: question1_2
    :multiple_answers:
    :correct: a,b,d
    :answer_a: red
    :answer_b: yellow
    :answer_c: black
    :answer_d: green
    :feedback_a: Red is a definitely on of the colors.
    :feedback_b: Yes, yellow is correct.
    :feedback_c: Remember the acronym...ROY G BIV.  B stands for blue.
    :feedback_d: Yes, green is one of the colors.

    Which colors might be found in a rainbow? (choose all that are correct)

These are just two of the many interactive components for writing online course materials.  You can see examples of all of them `On our Example Page <http://interactivepython.org/runestone/static/overview/overview.html>`_

Now feel free to modify this file to start creating your own interactive page.


Section 5: Theme 2
:::::::::::::::::::

You can override the style rules in the default theme by adding css rules to a file named **theme-overrides.css** (the filename is important - this will replace an existing file). Make sure the file's directory is part of the ``html_static_path``. You can do so by placing it in a folder **_static**, then modifying ``html_static_path`` in conf.py to include that folder:



If you want to do more significant changes to the theme, you should copy the files in the runestone/common/project/template/sphinx_bootstrap to a directory like ``_templates/my_theme``. Then make sure these values are set in conf.py:

.. code::

    html_theme_path = ["_templates"]
    html_theme = 'my_theme'
