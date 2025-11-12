from manim import *
# Code2Video dash_length patch
from manim import Line as _CODE2VIDEO_ORIGINAL_LINE, DashedLine as _CODE2VIDEO_DASHED_LINE

def Line(*args, dash_length=None, **kwargs):
    if dash_length is not None:
        return _CODE2VIDEO_DASHED_LINE(*args, dash_length=dash_length, **kwargs)
    return _CODE2VIDEO_ORIGINAL_LINE(*args, **kwargs)

class GeneratedScene(Scene):
    def construct(self):
        # Configure the camera for 1920x1080 resolution and white background
        self.camera.background_color = WHITE
        self.camera.frame_width = 16  # Corresponds to 1920 pixels width
        self.camera.frame_height = 9   # Corresponds to 1080 pixels height
        self.renderer.frame_rate = 30

        # 1. Create Axes for Price and Quantity
        # Define the range for the axes
        x_range = [0, 10, 1] # Quantity
        y_range = [0, 10, 1] # Price
        
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=7,
            y_length=7,
            axis_config={"color": BLACK, "include_numbers": False},
            tips=False # No arrows at the end of axes
        ).to_edge(DOWN + LEFT)

        # Labels for axes
        x_label = Text("Quantity (Q)", font_size=28, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Price (P)", font_size=28, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.2)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # 2. Define and Draw Supply and Demand Curves
        # Demand function: P = -Q + 8 (downward sloping)
        def demand_func(x):
            return -x + 8

        # Supply function: P = Q + 2 (upward sloping)
        def supply_func(x):
            return x + 2

        demand_curve = axes.get_graph(demand_func, x_range=[0, 8], color=BLUE)
        supply_curve = axes.get_graph(supply_func, x_range=[0, 8], color=RED)

        demand_label = Text("Demand (D)", font_size=24, color=BLUE).next_to(demand_curve, UP + RIGHT, buff=0.1)
        supply_label = Text("Supply (S)", font_size=24, color=RED).next_to(supply_curve, UP + LEFT, buff=0.1)

        self.play(Create(demand_curve), Write(demand_label))
        self.play(Create(supply_curve), Write(supply_label))
        self.wait(1)

        # 3. Identify and Mark Equilibrium
        # Equilibrium: -Q + 8 = Q + 2  =>  2Q = 6  =>  Qe = 3
        # Pe = 3 + 2 = 5
        eq_q = 3
        eq_p = 5
        equilibrium_point = axes.coords_to_point(eq_q, eq_p)

        eq_dot = Dot(equilibrium_point, color=BLACK, radius=0.08)
        
        eq_q_line = axes.get_vertical_line(equilibrium_point, color=GRAY, line_arg={"stroke_width": 2, "dash_length": 0.1})
        eq_p_line = axes.get_horizontal_line(equilibrium_point, color=GRAY, line_arg={"stroke_width": 2, "dash_length": 0.1})

        eq_q_label = Text("Qe", font_size=24, color=BLACK).next_to(eq_q_line, DOWN, buff=0.1)
        eq_p_label = Text("Pe", font_size=24, color=BLACK).next_to(eq_p_line, LEFT, buff=0.1)

        self.play(
            FadeIn(eq_dot, scale=0.5),
            Create(eq_q_line),
            Create(eq_p_line),
            Write(eq_q_label),
            Write(eq_p_label)
        )
        self.wait(1.5)

        # 4. Disequilibrium: Surplus (Price above equilibrium)
        diseq_p_surplus = 7 # P₁
        diseq_p_surplus_point = axes.coords_to_point(0, diseq_p_surplus)

        diseq_p_surplus_line_h = axes.get_horizontal_line(diseq_p_surplus_point, color=PURPLE, line_arg={"stroke_width": 2})
        diseq_p_surplus_label = Text("P₁", font_size=24, color=PURPLE).next_to(diseq_p_surplus_line_h, LEFT, buff=0.1)

        self.play(Create(diseq_p_surplus_line_h), Write(diseq_p_surplus_label))
        self.wait(0.5)

        # Quantities at P₁: Qd₁ = 1, Qs₁ = 5
        qd1 = 1
        qs1 = 5

        qd1_point = axes.coords_to_point(qd1, diseq_p_surplus)
        qs1_point = axes.coords_to_point(qs1, diseq_p_surplus)

        qd1_dot = Dot(qd1_point, color=BLUE, radius=0.06)
        qs1_dot = Dot(qs1_point, color=RED, radius=0.06)

        qd1_line = axes.get_vertical_line(qd1_point, color=BLUE, line_arg={"stroke_width": 2, "dash_length": 0.1})
        qs1_line = axes.get_vertical_line(qs1_point, color=RED, line_arg={"stroke_width": 2, "dash_length": 0.1})

        qd1_label = Text("Qd₁", font_size=24, color=BLUE).next_to(qd1_line, DOWN, buff=0.1)
        qs1_label = Text("Qs₁", font_size=24, color=RED).next_to(qs1_line, DOWN, buff=0.1)

        self.play(
            FadeIn(qd1_dot, scale=0.5), Create(qd1_line), Write(qd1_label),
            FadeIn(qs1_dot, scale=0.5), Create(qs1_line), Write(qs1_label)
        )
        self.wait(1)

        # Highlight the surplus quantity
        surplus_arrow = Arrow(
            start=qd1_point + RIGHT * 0.5,
            end=qs1_point - RIGHT * 0.5,
            color=YELLOW,
            stroke_width=4,
            tip_length=0.2
        )
        surplus_label = Text("Surplus", font_size=30, color=YELLOW).next_to(surplus_arrow, UP, buff=0.1)

        self.play(Create(surplus_arrow), Write(surplus_label))
        self.wait(2)

        self.play(
            FadeOut(surplus_arrow),
            FadeOut(surplus_label),
            FadeOut(qd1_dot), FadeOut(qs1_dot),
            FadeOut(qd1_line), FadeOut(qs1_line),
            FadeOut(qd1_label), FadeOut(qs1_label),
            FadeOut(diseq_p_surplus_line_h), FadeOut(diseq_p_surplus_label)
        )
        self.wait(0.5)

        # 5. Disequilibrium: Shortage (Price below equilibrium)
        diseq_p_shortage = 3 # P₂
        diseq_p_shortage_point = axes.coords_to_point(0, diseq_p_shortage)

        diseq_p_shortage_line_h = axes.get_horizontal_line(diseq_p_shortage_point, color=ORANGE, line_arg={"stroke_width": 2})
        diseq_p_shortage_label = Text("P₂", font_size=24, color=ORANGE).next_to(diseq_p_shortage_line_h, LEFT, buff=0.1)

        self.play(Create(diseq_p_shortage_line_h), Write(diseq_p_shortage_label))
        self.wait(0.5)

        # Quantities at P₂: Qd₂ = 5, Qs₂ = 1
        qd2 = 5
        qs2 = 1

        qd2_point = axes.coords_to_point(qd2, diseq_p_shortage)
        qs2_point = axes.coords_to_point(qs2, diseq_p_shortage)

        qd2_dot = Dot(qd2_point, color=BLUE, radius=0.06)
        qs2_dot = Dot(qs2_point, color=RED, radius=0.06)

        qd2_line = axes.get_vertical_line(qd2_point, color=BLUE, line_arg={"stroke_width": 2, "dash_length": 0.1})
        qs2_line = axes.get_vertical_line(qs2_point, color=RED, line_arg={"stroke_width": 2, "dash_length": 0.1})

        qd2_label = Text("Qd₂", font_size=24, color=BLUE).next_to(qd2_line, DOWN, buff=0.1)
        qs2_label = Text("Qs₂", font_size=24, color=RED).next_to(qs2_line, DOWN, buff=0.1)

        self.play(
            FadeIn(qd2_dot, scale=0.5), Create(qd2_line), Write(qd2_label),
            FadeIn(qs2_dot, scale=0.5), Create(qs2_line), Write(qs2_label)
        )
        self.wait(1)

        # Highlight the shortage quantity
        shortage_arrow = Arrow(
            start=qs2_point + RIGHT * 0.5,
            end=qd2_point - RIGHT * 0.5,
            color=ORANGE,
            stroke_width=4,
            tip_length=0.2
        )
        shortage_label = Text("Shortage", font_size=30, color=ORANGE).next_to(shortage_arrow, UP, buff=0.1)

        self.play(Create(shortage_arrow), Write(shortage_label))
        self.wait(2)

        # Final fade out of all elements
        self.play(
            FadeOut(shortage_arrow),
            FadeOut(shortage_label),
            FadeOut(qd2_dot), FadeOut(qs2_dot),
            FadeOut(qd2_line), FadeOut(qs2_line),
            FadeOut(qd2_label), FadeOut(qs2_label),
            FadeOut(diseq_p_shortage_line_h), FadeOut(diseq_p_shortage_label),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(demand_curve),
            FadeOut(supply_curve),
            FadeOut(demand_label),
            FadeOut(supply_label),
            FadeOut(eq_dot),
            FadeOut(eq_q_line),
            FadeOut(eq_p_line),
            FadeOut(eq_q_label),
            FadeOut(eq_p_label)
        )
        self.wait(1)