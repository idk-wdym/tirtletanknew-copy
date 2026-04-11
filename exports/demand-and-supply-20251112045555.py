from manim import *

class GeneratedScene(Scene):
    def setup(self):
        # Configure scene for 1920x1080 @30fps with white background
        self.camera.background_color = WHITE
        config.frame_width = 16
        config.frame_height = 9
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.frame_rate = 30

    def construct(self):
        # 1. Create Axes for Quantity (Q) and Price (P)
        axes = Axes(
            x_range=[0, 10, 1],  # Quantity from 0 to 10, with ticks every 1 unit
            y_range=[0, 12, 1],  # Price from 0 to 12, with ticks every 1 unit
            x_length=7,          # Length of the x-axis
            y_length=6,          # Length of the y-axis
            axis_config={"color": BLACK, "include_numbers": True},
            tips=False           # Do not include arrows at the end of axes
        )
        axes.to_edge(DOWN + LEFT, buff=0.5) # Position the graph to the bottom-left

        # Axis labels using Text
        x_label = Text("Quantity (Q)", font_size=28, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("Price (P)", font_size=28, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)

        # 2. Define Demand and Supply functions
        # Demand function: P = 10 - Q (as Q increases, P decreases)
        def demand_func(q):
            return 10 - q

        # Supply function: P = 2 + 0.5Q (as Q increases, P increases)
        def supply_func(q):
            return 2 + 0.5 * q

        # 3. Create Demand Curve
        demand_curve = axes.get_graph(demand_func, x_range=[0, 10], color=BLUE)
        demand_label = Text("Demand (D)", font_size=28, color=BLUE).next_to(
            demand_curve.get_point_from_function(2), UP + LEFT, buff=0.1
        )

        # 4. Create Supply Curve
        supply_curve = axes.get_graph(supply_func, x_range=[0, 10], color=RED)
        supply_label = Text("Supply (S)", font_size=28, color=RED).next_to(
            supply_curve.get_point_from_function(8), DOWN + RIGHT, buff=0.1
        )

        # 5. Calculate Equilibrium Point (where demand = supply)
        # 10 - Q = 2 + 0.5Q  =>  8 = 1.5Q  =>  Q = 8 / 1.5 = 16/3
        # P = 10 - 16/3 = 14/3
        equilibrium_q = 16/3
        equilibrium_p = 14/3
        equilibrium_point_mobject = axes.coords_to_point(equilibrium_q, equilibrium_p)
        equilibrium_dot = Dot(point=equilibrium_point_mobject, color=PURPLE, radius=0.08)

        # Dashed lines from equilibrium to axes
        q_star_line = DashedLine(
            equilibrium_point_mobject, axes.coords_to_point(equilibrium_q, 0), color=GRAY
        )
        p_star_line = DashedLine(
            equilibrium_point_mobject, axes.coords_to_point(0, equilibrium_p), color=GRAY
        )

        # Labels for equilibrium quantity (Q*) and price (P*)
        q_star_label = Text("Q*", font_size=28, color=PURPLE).next_to(q_star_line, DOWN, buff=0.1)
        p_star_label = Text("P*", font_size=28, color=PURPLE).next_to(p_star_line, LEFT, buff=0.1)

        # 6. Animate the scene
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        self.play(Create(demand_curve), Write(demand_label))
        self.wait(0.5)
        self.play(Create(supply_curve), Write(supply_label))
        self.wait(1)
        self.play(
            FadeIn(equilibrium_dot, scale=0.5),
            Create(q_star_line),
            Create(p_star_line),
            Write(q_star_label),
            Write(p_star_label)
        )
        self.wait(2)