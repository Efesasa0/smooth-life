# Smooth Life 🪱

Smooth Life is a continous version of Conway's Game of Life where cells live in a floating-point domain. This project visualizes the dynamics inside such game in real-time.

The implementation uses Flask to display the states in a streaming fashion.

## Installation

### Setting Up a Virtual Environment

**With python venv:**

1. Navigate to project directory:

```console
git clone https://github.com/Efesasa0/smooth-life.git
```

2. Create virtual environment:

```console
python3 -m venv smooth
```

3. Activate it:

```console
source smooth/bin/activate

```

**With conda**

1. Create conda environment:

```console
conda create --name smooth python=3.9
```

2. Activate it:

```console
conda activate smooth

```

### Installing Dependencies

After activating your virtual environment, install the required dependencies by running:

```console
pip install -r requirements.txt
```

### Running the Application
To run the Smooth Life simulation and start the Flask server, execute:

```console
python flask_demo.py
```

Navigate to http://localhost:82 in your web browser to view the simulation.

### Sources

1.
2.
3.
4.

### Challenges

*
*
*

### Extras

* Add additional kernels into calculation can change outcomes drastically.
* Add user interaction feature for real-time parameter adjustments.
