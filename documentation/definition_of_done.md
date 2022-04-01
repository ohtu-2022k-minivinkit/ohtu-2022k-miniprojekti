# Definition of done

By done we mean in general that a requirement has been analyzed, designed, programmed, tested, tests have been automated, code has been documented, integrated and taken to production. More specifically this means that:
- User story has to have acceptance criteria that is documented by writing it in Robot Framework syntax. This documentation can be found through a link in README.md.
- Code has been written in maintainable manner:
    - Architecture is clear and sensible.
    - Code follows style guidelines laid out in PEP 8 (https://peps.python.org/pep-0008/).
    - Pylint gives at least a score of 7 (IS THIS ENOUGH?).
- Branch coverage of the tests has to be at least 70% (IS THIS ENOUGH?) for everything else except trivial code (e.g. getters and setters).
- Client is able to see the status of the code and tests ... HOW?
