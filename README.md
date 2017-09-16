# Airplane Seating Sim

## Description
This was a project done for the class Mathematical Modeling. This simulator was made to help compare airplane boarding
methods. [Problem Statement](http://www.comap.com/undergraduate/contests/mcm/contests/2007/problems/)

After some research, we focused on the ZigZag model. The ZigZag model was developed by combining some key ideas found
in back-to-front and outside-in boarding to make efficient use of the aisle. This simulator uses the [Zellegraphics](http://mcsp.wartburg.edu/zelle/python/graphics.py)
library for visualization. You can read more about the development of the model [here](selective-boarding-minimize.pdf)

## Assumptions
There are several key assumptions made while developing this model and applied by the simulator:
- All Passengers move at the same rate. The simulator has support for aisle rate variations.
It can have values (0.2, 0.4, ..., 2.0).

- Carry-On Luggage stowing rate is constant. The simulator does not have support to vary this due to time constraints.

- Adjacent passengers boarding opposite rows on opposite sides will not interfere with each other.

- All passengers arrive on time.

## Using Simulator
Clone the repo:
```
    git clone https://github.com/lamdaV/AirplaneSeatingSim.git
```

Run the script:
```
    python src/main.py
```

Parameters:
- `-m`, `--model` followed either `zone` or `zig` with default `zone`
- `-r`, `--rows` followed by some integer with default `3`
- `-v`, `--visualize` this is a flag to toggle visualizer with default to `False`
- `-c`, `--constant` this is a flag to toggle constant aisle movement rate to `1` with default `False`
