import solara

R_A = solara.reactive(21)
FACTOR = solara.reactive(3)
ORGANISM_COUNT = solara.reactive(2)
ALPHA_N = solara.reactive(0.028)
ALPHA_M = solara.reactive(0.5)
B1 = solara.reactive(0.05)
B2 = solara.reactive(0.2)
D1 = solara.reactive(0.05)
D2 = solara.reactive(0.05)


@solara.component
def Page():
    with solara.Columns([20, 80]):
        with solara.Column():
            solara.Markdown("Parameters")
            solara.SliderInt("R_A", value=R_A, min=1, max=30, thumb_label="always")
            solara.SliderInt("FACTOR", value=FACTOR, min=1, max=10, thumb_label="always")
            solara.SliderInt("ORGANISM_COUNT", value=ORGANISM_COUNT, min=1, max=10, thumb_label="always")
            solara.SliderFloat("ALPHA_N", value=ALPHA_N, min=0, max=2, step= 0.001, thumb_label="always")
            solara.SliderFloat("ALPHA_M", value=ALPHA_M, min=0, max=2, step= 0.001, thumb_label="always")
            solara.SliderFloat("B1", value=B1, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("B2", value=B2, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("D1", value=D1, min=0, max=1, step= 0.001, thumb_label="always")
            solara.SliderFloat("D2", value=D2, min=0, max=1, step= 0.001, thumb_label="always")


        with solara.Column():
            solara.HTML(tag="div", unsafe_innerHTML=f'<iframe src="http://127.0.0.1:5000/?R_A={R_A.value}&FACTOR={FACTOR.value}&ORGANISM_COUNT={ORGANISM_COUNT.value}&ALPHA_N={ALPHA_N.value}&ALPHA_M={ALPHA_M.value}&B1={B1.value}&B2={B2.value}&D1={D1.value}&D2={D2.value}" width=1000 height=1000></iframe>')