import solara

r_a = solara.reactive(21)
factor = solara.reactive(3)
mask_ratio = solara.reactive(0.2)
organism_count = solara.reactive(2)
alpha_n = solara.reactive(0.028)
alpha_m = solara.reactive(0.5)
b1 = solara.reactive(0.05)
b2 = solara.reactive(0.2)
d1 = solara.reactive(0.05)
d2 = solara.reactive(0.05)
dt = solara.reactive(0.05)

@solara.component
def Page():
    with solara.Columns([20, 60, 20]):
        with solara.Column():
            solara.Markdown("""
# About Smooth Life 🪱
Smooth life is a varient of [Conway's Game of Life] that runs on a continous domain. 
                            
Rather then a single pixel/cell having 0 or 1 value, their death/alive status is a floating point between 0 and 1.
                            
Additionaly, the kernels used to calculate the state value via simple convolution are circular, making the results smoother.""")
            solara.Markdown("""
### Parameter Details
* `r_a`: Radius for activity calculation. Affects the local neighborhood size.
* `factor`: Scaling factor for the inner kernel radius, influencing core interaction.
* `mask_ratio`: Determines the density of initial organism distribution.
* `organism_count`: Initial count of organisms.
* `alpha_n`: Controls the transition smoothness for birth conditions.
* `alpha_m`: Adjusts the transition smoothness for survival conditions.
* `b1`, `b2`: Birth thresholds. Values between which a cell starts birth process.
* `d1`, `d2`: Death thresholds. Defines the range for cell death.
* `dt`: Time step for simulation updates, influencing the speed of state changes.""")
        with solara.Column():
            solara.HTML(tag="div", unsafe_innerHTML=f'<iframe src="http://127.0.0.1:5000/?r_a={r_a.value}&factor={factor.value}&mask_ratio={mask_ratio.value}&organism_count={organism_count.value}&alpha_n={alpha_n.value}&alpha_m={alpha_m.value}&b1={b1.value}&b2={b2.value}&d1={d1.value}&d2={d2.value}&dt={dt.value}" width=1000 height=1000></iframe>')
        with solara.Column():
            solara.Markdown("""
# Tune the Parameters.
Note: Each action, will refresh the simulation.""")
            solara.SliderInt("r_a", value=r_a, min=1, max=30, thumb_label="always")
            solara.SliderInt("factor", value=factor, min=1, max=10, thumb_label="always")
            solara.SliderFloat("mask_ratio", value=mask_ratio, min=0, max=1, step=0.1, thumb_label="always")
            solara.SliderInt("organism_count", value=organism_count, min=1, max=10, thumb_label="always")
            solara.SliderFloat("alpha_n", value=alpha_n, min=0, max=2, step= 0.001, thumb_label="always")
            solara.SliderFloat("alpha_m", value=alpha_m, min=0, max=2, step= 0.001, thumb_label="always")
            solara.SliderFloat("b1", value=b1, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("b2", value=b2, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("d1", value=d1, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("d2", value=d2, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("dt", value=dt, min=0, max=2, step= 0.001, thumb_label="always")