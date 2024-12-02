# leosparks

this prototype demonstrates a Face ID-based locking system that integrates facial recognition technology with an electronic door lock for secure access control. It contains  the following components:

Arduino Microcontroller:

Acts as the central controller to process inputs and outputs.
Nano Terminal Adapter:

Simplifies wiring by providing screw terminals for easy and secure connections to external components.
Relay Module:

Serves as an intermediary switch to control the electronic door lock based on the Arduino's signal.
Electronic Door Lock:

A solenoid or latch mechanism that locks/unlocks the door when triggered by the relay.
Functionality
The system uses a facial recognition module or camera (not shown here but assumed to be part of the design) to authenticate users.
Upon successful identification:
The Arduino sends a signal to the relay module.
The relay activates the electronic door lock, unlocking the door.
If authentication fails, the lock remains engaged, ensuring security.
Purpose
This prototype demonstrates a smart access control system for homes, offices, or secure facilities. It showcases how facial recognition can be seamlessly integrated with existing microcontroller-based systems for modern, contactless door locking solutions.
