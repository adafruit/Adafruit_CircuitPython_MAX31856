Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-max31856/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/max31856/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_MAX31856.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_MAX31856
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

Usage Example
=============
::

  import board
  import busio
  import digitalio
  import adafruit_max31856

  # create a spi object
  spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

  # allocate a CS pin and set the direction
  cs = digitalio.DigitalInOut(board.D5)
  cs.direction = digitalio.Direction.OUTPUT

  # create a thermocouple object with the above
  thermocouple = adafruit_max31856.MAX31856(spi, cs)

  # print the temperature!
  print(thermocouple.temperature)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/siddacious/Adafruit_CircuitPython_MAX31856/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-max31856 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
