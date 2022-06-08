=====================
Combinatorics
=====================

.. Here is were you specify the content and order of your new book.

.. Each section heading (e.g. "SECTION 1: A Random Section") will be
   a heading in the table of contents. Source files that should be
   generated and included in that section should be placed on individual
   lines, with one line separating the first source filename and the
   :maxdepth: line.

.. Sources can also be included from subfolders of this directory.
   (e.g. "DataStructures/queues.rst").


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

First, make a guess as to what you think the total will be. Write it here.

.. fillintheblank:: fitb-ex1
   :casei:

   I think that there are |blank| rearrangements of the letters in the word ROCKET

   -   :120: Correct.
       :x: Incorrect. The answer is 120.


Here is some code that will solve the problem. Do not run it, but answer questions
about it below.

Active Code
------------

.. activecode:: CodeSample8
   :coach:
   :caption: Create some code

   Rocket = ['R', 'O', 'C', 'K', 'E', 'T']
   counter = 0

   for i in Rocket:
       for j in Rocket:
           if j != i:
               for k in Rocket:
                   if k != j and k != i:
                       for l in Rocket:
                           if l != k and l != j and l != i:
                               for m in Rocket:
                                   if m != l and m != k and m != j and m != i:
                                       for n in Rocket:
                                           if n != m and n != l and n != k and n != j and n != i:
                                               print(i,j,k,l,m,n)
                                               counter += 1
   print(counter)


If you were to run the code above, think about what the output would be.

How many of the outcomes in the output of this code will start with "O" as the
first letter? How many will start with "ET"? Answer this question below.

.. fillintheblank:: fitb-ex2
   :casei:

   |blank| of the outcomes will start with "O", and |blank| of the outcomes will start with "ET".

   -   :60: Correct.
       :x: Incorrect. The answer is 60.
   -   :24: Correct.
       :x: Incorrect. The answer is 24.


General formula for Arrangements without Repetition of all n elements
------------------------------------------------------------------------

In the problems above, we arranged all of the elements in a given set (all of
the numbers, all of the friends, all of the letters). When we are arranging all
n elements in a set, there is a general formula that we can use. In general,
if we have n distinct objects, and we are arranging n of them where repetition
is not allowed, there are n choices for the first position, n-1 for the second,
n-2 for the third, etc. It is useful to think of this as a product of r terms,
n*(n-1)*(n-2)* ... * 3 * 2 * 1$. This expression, the product of the positive
integers from 1 to n is written as n!.

This is called "n factorial," and it both represents the mathematical expression
of the product of positive integers from 1 to $n$, and the number of arrangements
of n distinct objects. For example, then, there are 20! ways to arrange 20
different books in a row on a shelf, there are 150! ways to rank 150 restaurants
in a given city, and there are 26! arrangements of the letters in the alphabet.

While n! give the total number of arrangements of an entire set of n elements,
sometimes we might want to arrange SOME but not ALL of the elements in a set.
Consider the following problem.

::

  4. Nine horses compete in a race, and there will be a first, second, and third
  prize given (assume no ties). How many possibilities are there for how prizes are
  distributed to the horses?

Note in this case, we only want to count arrangements of 3 of the 9 horses.
Here we have a 3-stage process, and our number of options at each stage are
reduced by 1. In particular, we have 10 options for who receives first place, 9
options for second (because whichever horse placed first cannot also place second),
and 8 options for third. Our expression is 9 * 8 * 7 = 504.

Write some code to solve this problem.

.. activecode:: CodeSample9
   :coach:
   :caption: Create some code to answer the Horse Race problem



.. shortanswer:: short-ex1

   In the space below, explain how you know how many nested for loops your code
   should have.

::

  5. There are 8 class projects and four teams of students who will work on those
  projects. In how many ways can the projects be assigned to the students if
  each team works on one project, and no two teams can work on the same project?

We consider a four-stage process of assigning a project to each of four different
teams. There are 8 options for which project the first team gets, then 7 for the
second team since projects cannot be repeated, then 6 for the third and 5 for
the fourth. Thus our expression is 8 * 7 * 6 * 5 = 1680.

Maybe a Parson's problem or some given code here.

General Formula for Arrangements without Repetition
----------------------------------------------------

Notice that there is a commonality among the mathematical expressions that solve
this particular kind of problem. In general, if we have $n$ distinct objects, and
we are arranging r of them where repetition is not allowed, there are n choices
for the first position, n-1 for the second, n-2 for the third, etc. It is
useful to think of this as a product of r terms, n*(n-1)*(n-2)* ... * (n-r+1).
This expression is sometimes denoted as P(n,r) or $_nP_r$, where P stands for
permutation. Note that this product can be rewritten efficiently as a
ratio of two factorials, because as terms cancel we get the desired product:
$$\frac{n!}{(n-r)!}$$

In terms of coding problems like these, notice that we can have $n$ elements in
our initial list, and we have $r$ nested for loops with the restriction that
elements cannot be repeated. These correspond to the $r$ stages in our counting
process, where at each stage we are cycling through all $n$ options in our list,
excluding elements that cannot be repeated as we go.

As is often the case, most problems will not be only a direct application of this
formula, but rather they will involve or incorporate that formula in some way
into a broader problem. Here we offer some examples of how this formula might
arise or be used in problems.

::

  6. How many arrangements of the letters in the word CATTLE have the Ts together
  at the beginning or the end of the word?

Here we have two cases - when the Ts are at the beginning of the word and then
the Ts are at the end of the word. If the Ts are at the beginning, there are 4!
ways to arrange the rest of the letters, and if the Ts are at the end, there are
4! ways to arrange the rest of the letters. We can add these two distinct cases,
so we get a final expression of $4! + 4! = 48$. The program below lists these
outcomes.

Write some code below that would print all outcomes for Problem 6.

.. activecode:: CodeSample10
   :coach:
   :caption: Create some code to answer the CATTLE problem

::

  7. You have 10 different hardcover books and 8 different paperback books.
  How many ways are there to arrange 3 hardback books and 5 paperback books if
  each kind of book has to be in a block together?



.. parsonsprob:: PP_licenseplates
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Hardcover = ['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
   Paperback = ['P1','P2','P3','P4','P5','P6','P7','P8']

   =====
   counter = 0
   =====
   for i in Hardcover:
       for j in Hardcover:
           if j != i:
   =====
               for k in Hardocver:
                   if k!=j and k!= i:
   =====
                       for l in Paperback:
                           for m in Paperback:
                               if m!= l:
   =====
                                   for n in Paperback:
                                       if n != m and n!= l:

   =====
                                           print(i,j,k,l,m,n)
                                           counter +=1
   =====
   for i in Paperback:
       for j in Paperback:
           if j != i:
   =====
               for k in Paperback:
                   if k!=j and k!= i:
   =====
                       for l in Hardcover:
                           for m in Hardcover:
                               if m!= l:
   =====
                                   for n in Hardcover:
                                       if n != m and n!= l:
   =====
                                           print(i,j,k,l,m,n)
                                           counter +=1
   =====
   print(counter)


Here we have two cases - either the hardcover books are first, or the paperback
books are first. In the first case, we have a two-stage counting process of first
arranging the three hardcover books (there are $\frac{10!}{(10-3)!}$ such
arrangements) and then arranging the paperback books (there are $\frac{8!}{(8-5)!}$
such arrangement). Because for each of those stages, the number of choices is
independent, we can use the multiplication principle. Thus, the number of arrangements
with hardcover then paperback books is $P(10,3)\cdot P(8,5)$, or $\frac{10!}{(10-3)!}
\cdot \frac{8!}{(8-5)!}.$

The second case is similar - first we arrange paperback books ($\frac{8!}{(8-5)!}$),
then we arrange hardcover books ($\frac{10!}{(10-3)}!$). Again we use the
multiplication principle, so the number of arrangements with paperback then
hardcover books is $P(8,5) \cdot P(10,3)$, or $\frac{8!}{(8-5)!} \cdot \frac{10!}{(10-3)!}.$

For the total, we add both cases, so our total is $\frac{10!}{(10-3)!} \cdot
\frac{8!}{(8-5)!} + \frac{8!}{(8-5)!} \cdot \frac{10!}{(10-3)!} = 483840$.

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
