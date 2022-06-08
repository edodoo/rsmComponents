=============================
The Multiplication Principle
=============================

The Multiplication Principle (MP) is a foundational counting principle that helps
us determine the number of outcomes of a multi-stage counting process. Generally,
the idea is that a counting process can be broken into multiple stages, and, if
certain conditions are met, then the number of outcomes of the total process is
the product of the number of outcomes at each stage.

We prefer Tucker's (2002) statement of the MP, provided below. In this worksheet,
we will talk through the reasons for components of Tucker's statement and
provide practice with the MP.



Multiplication Principle (MP)
-------------------------------

  Suppose a procedure can be broken into m successive (ordered) stages, with :math:`r_1`
  different outcomes in the first stage, :math:`r_2` different outcomes in the second stage, ..., and
  :math:`r_m` different outcomes in the mth stage. If the number of outcomes at each stage is independent
  of the choices in previous stages and if the composite outcomes are all distinct, then
  the total procedure has :math:`r_1 \times r_2 \times ... \times r_m` different composite outcomes.

This may sound abstract, and our goal is to present and discuss a sequence of problems
that make the Multiplication Principle (MP) more clear. Consider first a problem about
creating outfits from your wardrobe.

Problem 1: Outfits
~~~~~~~~~~~~~~~~~~~~~~
  You have four different tops (a tee, a sweater, a tank, and a blouse) and three different bottoms
  (shorts, capris, and jeans). How many different outfits are you able to make.

To solve this problem, we can think about dressing ourselves in two stages. First, you put
a top, and second you put on bottoms. We can use a similar counting process, where first we specify
a top to wear, and then we specify a bottom to wear.

You'll notice that we aren't restricting which tops and bottoms may go together, so
we say that the choice of bottom is independent of the choice of top. Thus, for any of
the four tops, we have three bottoms we can choose.

Further, anytime we choose a top and a bottom, we will get a unique outfit. While this
may seem obvious now, it's important to make sure when we solve other problems.

The reason for pointing out that our counting process can occur in two stages, that
the number of choices in each stage is independent, and that the resulting (composite)
outcomes are all distinct is so that we know we are in the exact situation that
the MP describes. Now that we have done so, we know that there are :math:`4\times 3 = 12`
outcomes.

To visualize these outcomes, consider the table below where we list every outcome:

+--------------+---------------------+------------------------+---------------------+
|              |        **Shorts**   |        **Capris**      |     **Jeans**       |
+--------------+---------------------+------------------------+---------------------+
| **Tee**      | (Tee, Shorts)       |   (Tee, Capris)        |   (Tee, Jeans)      |
+--------------+---------------------+------------------------+---------------------+
| **Sweater**  | (Sweater, Shorts)   | (Sweater, Capris)      | (Sweater, Jeans)    |
+--------------+---------------------+------------------------+---------------------+
| **Tank**     | (Tank, Shorts)      | (Tank, Capris)         | (Tank, Jeans)       |
+--------------+---------------------+------------------------+---------------------+
| **Blouse**   | (Blouse, Shorts)    |  (Blouse, Capris)      | (Blouse, Jeans)     |
+--------------+---------------------+------------------------+---------------------+


This table neatly organizes the outcomes by using rows to distinguish between the tops,
and columns to distinguish between the bottoms. You may notice that in any row
all the tops are the same, and in any column all the bottoms are the same. We could have
created this table one row at a time, where for every option of top we cycled through
every option of bottom. Let's do this process using computer code.

Examine the code below, and consider how the nested lines that say ``for i in Tops:``
and ``for j in Bottoms:`` may correspond to the process of cycling through every possibility for a bottom
for every possibility of top. After you run it, compare the result to the table above and relate
the result to the mathematical expression :math:`4\times 3` .

Tops and Bottoms
~~~~~~~~~~~~~~~~~

.. activecode:: CodeSampleMult1
   :coach:
   :caption: Code that generates possible outfits

   Tops = ['tee', 'sweater','tank', 'blouse']
   Bottoms = ['shorts', 'capris', 'jeans']
   counter=0

   for i in Tops:
       for j in Bottoms:
           print(i,j)
           counter+=1
   print(counter)





Problem 2: Outfits Part 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Suppose now you had 4 different tops, 5 different bottoms, and 3 different pairs of shoes.
  Describe why the number of ways to choose a top, the number of ways to choose
  a bottom, and the number of ways to choose a pair of shoes are independent of
  each other. Describe also why each composite outcome (a full outfit) is unique.
  Then, use the MP to find a mathematical expression for the total number of outcomes.


The code below will list all possible outfits. Before you run it, predict how the printed
outcomes will be organized. Then, jot down your prediction for the first 5 outcomes that
will be printed.

Tops, Bottoms, and Shoes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activeCode:: CodeSampleMult2
   :coach:
   :caption: Outfits including shoes

   Tops = ['tee', 'sweater','tank', 'blouse']
   Bottoms = ['shorts', 'capris', 'jeans']
   Shoes = ['sneakers', 'sandals', 'keds']
   counter=0

   for i in Tops:
       for j in Bottoms:
           for k in Shoes:
               print(i,j)
               counter+=1
   print(counter)


.. shortanswer:: short-mult1

  In the space below, describe if your predicted first 5 outcomes matched the first 5
  outcomes that were printed. If they were the same, tell us about your reasoning.
  If they were different, describe why they were different.

Cartesian Product Problems
---------------------------------

The two problems you have solved (both of the outfit problems) are examples of
Cartesian Product Problems. By starting with two sets, for example a set :math:`T`
which denotes all Tops and a set :math:`B` which denotes all Bottoms, we can create
a new set of all pairs of Tops and Bottoms exactly as we did for the first problem.
We call this new set the Cartesian product of :math:`T` and :math:`B`, and we use the
symbols :math:`T\times B` to denote this set.

More formally, if you start with any two sets, say sets :math:`X` and :math:`Y`,
the Cartesian product of :math:`X` and :math:`Y` is the set of all pairs :math:`(x,y)`
where :math:`x` comes from :math:`X` and :math:`y` comes from :math:`Y`. We use the symbols
:math:`X\times Y` to denote the Cartesian product of sets :math:`X` and :math:`Y`. We can also
take the Cartesian product of more than two sets, and the resulting Cartesian product is
all the ways to take an element from each set and pair them together. We have seen this as well, like
when we found all outfits that consisted of a top, a bottom, and a pair of shoes. If :math:`T` is the
set of tops, :math:`B` is the set of bottoms, and :math:`S` is the set of shoes, then
the set :math:`T\times B\times S` is all the possible combinations of a top, a bottom, and a
pair of shoes.

In the realm of counting problems, we say a problem is a Cartesian Product Problem
if the set of outcomes of that problem can be encoded as a Cartesian product. As we have described,
both of the outfits problems you've solved are Cartesian Product Problems. A nice
similarity among all Cartesian Product Problems is that they can be solved using
the multiplication principle. If you can represent the outcomes of a counting problem
as a Cartesian product of sets, then the total number of outcomes is the product
of the size of each set. For example, when we counted the total number of outfits
we could make from a set of tops (:math:`T` with size :math:`|T|`) a set of bottoms (:math:`B`
with size :math:`|B|`) and a set of shoes (:math:`S` with size :math:`|S|`), we found
that the total number of outfits was :math:`|T|\times |B| \times |S|` (the total
number of tops times the total number of bottoms times the total number of pairs of shoes).

Let's solve another Cartesian Product Problem.

Problem 3: Coin, Dice, Letter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to first flip a fair coin, then roll a 6-sided die, and
  then pick a letter from the alphabet?

.. shortanswer:: shortmult2

  First things first, explain why problem 3 is a Cartesian Product Problem. Then,
  describe how you will find the total number of outcomes.

The code below generates the outcomes of problem 3. We will represent the ways to flip a coin
as 'H' and 'T', the ways to roll a 6-sided dice as the numbers 1 through 6, and the ways
to choose a letter from the alphabet as the numbers 1 through 26. Predict the first
five outcomes of the code before you run it.

.. activecode:: CodeSampleMult3
  :coach:

  Coin = ['H', 'T']
  Dice = range(1,7)
  Letters = range(1,27)
  counter = 0

  for i in Coin:
      for j in Dice:
          for k in Letters:
              print(i,j,k)
              counter+=1
  print(counter)

.. shortanswer:: shortmult3

  As you scroll through the output of the above code, you may notice that the outcomes
  are split into two groups--those that start with "T" and those that start with "H".
  How many outcomes are in each group? Are you able to use the MP to solve this?

.. mchoice:: MP_1
    :correct: a
    :answer_a: 1840
    :answer_b: 240
    :answer_c: 480
    :feedback_a: Correct
    :feedback_b: Incorrect. This counts the number of types for each style.
    :feedback_c: Incorrect. This does not account for the choices of color.

    A store carries 8 styles of pants. For each style, there are 10 different
    possible waist sizes, 6 pant lengths, and 4 color choices. How many
    types of pants does the store have?

.. mchoice:: MP_2
    :correct: b
    :answer_a: 24
    :answer_b: 23
    :answer_c: 15
    :feedback_a: Incorrect. Does your solution count both no As and no Bs?
    :feedback_b: Correct. Well done!
    :feedback_c: Incorrect. Are you allowing for no As and at least one B?

    How many nonempty collections of letters can be formed from three As and five Bs?
    Hint: this problem is very similar to, but not exactly, a Cartesian Product Problem.

Look at the code below. Then explain why it does or does not print the outcomes of
the previous problem.

.. activecode:: CodeSampleMult4
    :coach:
    :Caption: Does this count all nonempty collections letters formed from 3 As and 5 Bs?

    A = [0,1,2,3]
    B = [0,1,2,3,4,5]
    counter=0

    for i in A:
        for j in B:
            if i!=0 or j!=0:
                print(i,j)
                counter+=1
    print(counter)

Cartesian products with copies of the same set
-------------------------------------------------

So far, we have only looked at Cartesian Product Problems where each set of objects
was distinct (for example, the set of Tops was distinct from the set of Bottoms).
However, there are counting problems that make use of Cartesian products of the
same set multiple times. Consider the following problem.

Problem 4: Coin Flip
~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to flip a coin 4 times in a row?

If we think of the outcomes of flipping a coin once as either `H` or `T`, then
we can think about the outcome of flipping a coin four times as a string of four
letters, where any letter is either an `H` or a `T`. For example, the outcome
`HHTH` can represent flipping a head on the first, second, and fourth toss, and flipping
a tail on the third toss. If we let the set of flipping a coin once be :math:`F=\{H,T\}`,
then the outcomes of flipping a coin four times in a row  can be represented as
:math:`F\times F\times F\times F`. Like before, the total number of outcomes
of these problems is still the product of the size of each set. In the case of flipping
a coin four times, there are :math:`2\times 2\times 2\times 2 = 16` outcomes.

We should talk about the independence of choices at each stage and the uniqueness
of composite outcomes. We'll use coin flips as an example. By saying that the
choices at each stage are independent, we mean that no matter the previous coin flip
the possible ways to flip the next coin are exactly the same. For example, if your
first coin was flipped heads, then the second coin could still be heads or tails. When
we say uniqueness of composite outcomes, we mean that each four letter combination
of Hs and Ts represent a different outcome. For example, compare outcomes HHTH and
HTHH. Even though each of these outcomes had three heads and one tails, the outcomes are unique
because the tails were in different coin flips; in the first outcome, the tail occurred
on the third coin flip whereas in the second outcome the tail occurred on the
second coin flip. Because the orders of the Hs and Ts matter in the outcomes, then
the composite outcomes are unique.

Problem 5: Quiz Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  On a quiz, there are 6 True/False questions. How many ways can a student
  finish the quiz, if they put an answer for every question?

For the problem above, write some code that prints the possible outcomes.

.. activecode:: CodeSampleMult5
  :coach:
  :caption: Ways to finish a 6-question T/F quiz

  Answers = ['T', 'F']
  counter = 0

  %Finish the code here


Problem 6: 3-digit sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many 3-digit sequences can we make using the letters {a, b, c, d, e, f}, if
  we can repeat letters in our sequence?

For the problem above above, write some code that prints the possible outcomes.

.. activecode:: CodeSampleMult6
  :coach:
  :caption: Possible 3-letter sequences

  Letters = ['a','b','c','d','e','f']
  counter = 0

  %Finish the code here



Why Independence Matters
---------------------------

While we have discussed that the number of choices at each stage of the counting
process is independent of each other in problems like the Outfits problem or the Head
Tails problem, we have not given any examples of when the number of choices aren't independent.
We will give a cautionary example of a problem where the number of choices is not independent.
With this in mind, one of the best ways to determine if the number of choices
at each stage is independent is to focus on how you might write down each
outcome, taking note if there are ways to reduce the number of options at later stages
by selecting specific options in earlier stages.

Consider the following problem:

Problem 7: Face Card, Heart Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to make a two-card hand, where the first card is a face
  card and the second card is a heart? You may assume that the order of the cards
  matters, but you must have two distinct cards (e.g. you cannot have two Jacks of Hearts).

On the face of it (pun intentional), this problem seems like a Cartesian Product Problem.
After all, there are are 12 face cards (3 per suit) and 13 hearts, so why isn't the
answer :math:`12\times 13`? The problem is that the number of ways to pick a heart is
not independent of the number of ways to pick a face card. For example, if we picked the
king of spades as our face card, then there are 13 possible ways to pick a heart
card; however, if we picked the king of **hearts** as our face card, then there
are only 12 ways to pick a different heart card. Hence, this problem is not a Cartesian
Product Problem.

That is not to say that we cannot use the MP in our solution of the problem, only that
the solution is not :math:`12\times 13`. For this problem, we can break our solutions into
two cases: in the first case, our face card is not a heart card, and in the second case our
face card is a heart card. In the first case, the number of choices at each stage is independent,
because choosing a non-heart face card does not limit the number of heart cards to draw. Hence, there
are 9 non-heart face cards, and for each of these there are 13 possible heart cards to draw. So, there are
:math:`9\times 13 = 117` ways to fulfill our first case. In the second case, although each
choice of a heart face-card limits the options for the second card (e.g. if our face card is
the king of hearts, then the remaining cards to draw are the ace through queen of hearts), the
**number of options** for drawing the second card remains the same. For any choice of
heart face-card, there are 12 options for the second card. Hence, we can apply the MP
to find that there are :math:`3\times 12 = 36` ways to fulfill our second case. Because the
two cases are distinct and the two cases demonstrate all ways to select a face card and
a heart, then there are :math:`9\times 13 + 3\times 12 = 153` ways to select a face
card and a heart card.



Applying the MP to other types of problems
--------------------------------------------

While Cartesian Product Problems are excellent examples of problems that can
be solved using the MP, there are other types of problems that can be solved using
the MP. This really comes down to a key distinction in how the MP is worded. Specifically,
we can apply the MP when the **number of choices at each stage** is independent. This is not
exactly the same as saying the **choices at each stage** is independent. The exact choices at
each stage are allowed to change, as long as the number of choices does not. We will
work through a few problems where the exact choices change at each stage, although
the number of choices remains the same.

Consider the following problem:

Problem 8: Small lottery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You have placed slips of paper with the numbers 1 through 10 in a baseball cap,
  with one sheet of paper per number. How many ways are there to draw three slips of paper
  from the hat, one at a time, in order to create a sequence of three numbers?

We can think about a counting process for this problem as occurring in three three stages:
choosing the first slip, choosing the second slip, and choosing the third slip. Let's discuss
each stage. For the first stage, there are 10 ways of choosing a slip because there are
10 slips of paper in the hat. However, the options for the second stage depend on what you
drew in the first stage. For example, if you chose number 1 in the first stage, then
the options for the second stage are the numbers 2 through 10. However, no matter the
choice in the first stage, you have only removed one of the slips of paper so there
must be nine choice in the second stage. We can therefore apply the MP because the number
of choices at the second stage is always nine, even if the exact choices may be different. Similarly,
for any choice in the first and second stage, you have only removed two of the slips, so there
are eight choices for the third stage. Therefore, there are :math:`10\times 9\times 8` ways
to draw the slips of paper from the hat.   

Problem 9: How to ostracize your friends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Suppose that you are good friends with Ralph, Jack, Simon, and Piggy. Unfortunately,
  the magical conch is telling you that you must select a best friend (who you will share
  your boar dinner with) and a least best friend (who you will ostracize from your group). How many
  ways are there to do this?

Let's consider the case where you choose Ralph as your best friend. In this case, the people
you can choose to ostracize are Jack, Simon, and Piggy. However, if you choose Jack
as your best friend, then the people you can choose to ostracize are Ralph, Simon, and Piggy.
Clearly, the people you can ostracize depends on who you choose to be your best friend.
However, the number of people you can ostracize is independent of who you choose to be
your best friend: for every possible best friend, there are three possible people you can
ostracize. Thus, we can still apply the MP to solve this problem, finding that there are
:math:`4\times 3 = 12` ways to choose a best friend and a person to ostracize.
