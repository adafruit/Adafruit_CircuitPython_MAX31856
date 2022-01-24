Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-max31856/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/max31856/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_MAX31856/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_MAX31856/actions/
    :alt: Build Status

A CircuitPython driver for the MAX31856 Universal Thermocouple Amplifier

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-max31856/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-max31856

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-max31856

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-max31856

Usage Example
=============

.. code:: python3

      import board
      import digitalio
      import adafruit_max31856

      # Create sensor object, communicating over the board's default SPI bus
      spi = board.SPI()

      # allocate a CS pin and set the direction
      cs = digitalio.DigitalInOut(board.D5)
      cs.direction = digitalio.Direction.OUTPUT

      # create a thermocouple object with the above
      thermocouple = adafruit_max31856.MAX31856(spi, cs)

      # print the temperature!
      print(thermocouple.temperature)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/max31856/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/siddacious/Adafruit_CircuitPython_MAX31856/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
