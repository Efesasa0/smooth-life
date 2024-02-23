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
    with solara.Columns([20, 80]):
        with solara.Column():
            solara.Markdown("Parameters")
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
            solara.SliderFloat("dt", value=d2, min=0, max=1, step= 0.001, thumb_label="always")


        with solara.Column():
            solara.HTML(tag="div", unsafe_innerHTML=f'<iframe src="http://127.0.0.1:5000/?r_a={r_a.value}&factor={factor.value}&mask_ratio={mask_ratio.value}&organism_count={organism_count.value}&alpha_n={alpha_n.value}&alpha_m={alpha_m.value}&b1={b1.value}&b2={b2.value}&d1={d1.value}&d2={d2.value}&dt={dt.value}" width=1000 height=1000></iframe>')