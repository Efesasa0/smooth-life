# Smooth Life 🪱

https://github.com/Efesasa0/smooth-life/assets/70029284/7518d4ee-49f4-4618-884a-6c4d8f5eb4dc

Smooth Life is a continous version of Conway's Game of Life where cells live in a floating-point domain. This project visualizes the dynamics inside such game in real-time.

The implementation uses Flask to display the states in a streaming fashion.

## Installation

### Setting Up a Virtual Environment

**With python venv:**

1. Navigate to project directory:

```bash
git clone https://github.com/Efesasa0/smooth-life.git
```

2. Create virtual environment:

```bash
python3 -m venv smooth
```

3. Activate it:

```bash
source smooth/bin/activate

```

**With conda**

1. Create conda environment:

```bash
conda create --name smooth python=3.9
```

2. Activate it:

```bash
conda activate smooth

```

### Installing Dependencies

After activating your virtual environment, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the Application
To run the Smooth Life simulation and start the Flask server, execute:

```bash
flask run
```

Then run the solara based app on seperate terminal.

```bash
solara run --theme-variant dark sol.py
```

A window will pop up displaying the interface.

### Additional Sources

1. [Generalization of Conway’s ”Game of Life” to a continuous domain - SmoothLife](https://arxiv.org/pdf/1111.1567.pdf)
2. [Lenia — Biology of Artificial Life](https://arxiv.org/pdf/1812.05433.pdf)
3. [Conway's Game of Life by NeuralNine](https://www.youtube.com/watch?v=cRWg2SWuXtM&ab_channel=NeuralNine)
4. [Conway's Game of Life by Tech with Tim](https://www.youtube.com/watch?v=YDKuknw9WGs&t=459s&ab_channel=TechWithTim)
5. [Smooth Life by Birdbrain](https://www.youtube.com/watch?v=6kiBYjvyojQ&ab_channel=Birdbrain)
6. [Smooth Life by tsoding](https://github.com/tsoding/SmoothLife)

### Challenges

* Get accurate representation of the SmoothLife paper.
* Implement interface with real-time parameter adjustments.
* Initially the scope was only getting the paper implementation. Expanding it to be interacted via user interface was not planned. Major changes for the backend would be nice.

### Extras

* Add additional kernels into calculation can change outcomes drastically.
* Add user interaction feature for real-time parameter adjustments. ✅
    * Prettify user interface, perhaps reimplement with JS

You can address the flow_demo.ipynb to see the idea of a simpler version
