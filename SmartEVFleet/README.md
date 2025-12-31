Smart EV Fleet Manager

This project demonstrates advanced Object-Oriented Programming (OOP) concepts in Python, specifically focusing on data encapsulation, inheritance, and automated object creation.

Core Features

Implementation of the @property decorator and setters to protect sensitive data like battery levels, automatically preventing overcharging and negative values.

A specialized Tesla class that inherits from the base ElectricVehicle class, overriding methods to account for specific energy consumption patterns.

A range calculation system that factors in active features, such as autonomous driving modes, which reduce estimated range by 20%.

A static method for estimating charging time based on charger performance.

A class method factory pattern that parses configuration strings and automatically instantiates the correct subclass based on the provided parameters.

Ability to export object states directly into JSON format for monitoring and logging purposes.

Technical Implementation

The project utilizes decorators including @property, @setter, @staticmethod, and @classmethod.

Implementation of parent-child class relationships with super() calls.

Advanced string parsing, conditional logic, and JSON library integration for data serialization.
