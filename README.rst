==============================================
traits: explicitly typed attributes for Python
==============================================

http://docs.enthought.com/traits

.. image:: https://api.travis-ci.org/enthought/traits.png?branch=master
   :target: https://travis-ci.org/enthought/traits
   :alt: Build status

.. image:: https://coveralls.io/repos/enthought/traits/badge.png
   :target: https://coveralls.io/r/enthought/traits
   :alt: Coverage status
   
This is a fork of the Traits Package that adds support wxPythonPhoenix and Python3   

The Traits project is at the center of all Enthought Tool Suite development
and has changed the mental model used at Enthought for programming in the
already extremely efficient Python programming language. We encourage everyone
to join us in enjoying the productivity gains from using such a powerful
approach.

The Traits project allows Python programmers to use a special kind of type
definition called a *trait*, which gives object attributes some additional
characteristics:

- **Initialization**: A trait has a *default value*, which is
  automatically set as the initial value of an attribute before its
  first use in a program.
- **Validation**: The type of a trait attribute is *explicitly declared*. The
  type is evident in the code, and only values that meet a
  programmer-specified set of criteria (i.e., the trait definition) can
  be assigned to that attribute.
- **Delegation**: The value of a trait attribute can be contained either
  in the defining object or in another object *delegated* to by the
  trait.
- **Notification**: Setting the value of a trait attribute can *notify*
  other parts of the program that the value has changed.
- **Visualization**: User interfaces that allow a user to *interactively
  modify* the value of a trait attribute can be automatically
  constructed using the trait's definition. (This feature requires that
  a supported GUI toolkit be installed. If this feature is not used, the
  Traits project does not otherwise require GUI support.)

A class can freely mix trait-based attributes with normal Python attributes,
or can opt to allow the use of only a fixed or open set of trait attributes
within the class. Trait attributes defined by a class are automatically
inherited by any subclass derived from the class.

Dependencies
------------

Traits runs on both Python 2 and Python 3. It requires Python 2.7
or Python >= 3.4.

Traits has the following optional dependencies:

* `NumPy <http://pypi.python.org/pypi/numpy>`_ to support the trait types
  for arrays.
* `Traitsui <https://pypi.python.org/pypi/traitsui>`_ to support Gui
  Views.

To build the full documentation one needs:

* sphinx > 1.2.3
* mock (optional if traitsui is not available)
