from manim import *

# Configure Manim for 1920x1080 resolution, 30fps, and white background
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = WHITE


class GeneratedScene(Scene):
    def construct(self):
        # 1. Create Axes for the graph
        # x_range: [min, max, step]
        # y_range: [min, max, step]
        # x_length and y_length control the physical size of the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": False},
            tips=False  # Do not include arrows at the end of axes
        ).to_edge(DOWN + LEFT, buff=1.0) # Position axes to the bottom-left
        
        # Add labels for the axes
        x_label = Text("Quantity (Q)", font_size=30, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Price (P)", font_size=30, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.2)

        # Group axes and labels for easier animation
        axes_group = VGroup(axes, x_label, y_label)

        # 2. Define and create the Demand Curve
        # Example demand function: P = 10 - Q
        demand_func = lambda x: 10 - x
        demand_graph = axes.get_graph(demand_func, x_range=[0.5, 9.5], color=BLUE, stroke_width=4)
        demand_label = Text("Demand", font_size=30, color=BLUE).next_to(demand_graph, UP + RIGHT, buff=0.2)

        # 3. Define and create the Supply Curve
        # Example supply function: P = Q
        supply_func = lambda x: x
        supply_graph = axes.get_graph(supply_func, x_range=[0.5, 9.5], color=RED, stroke_width=4)
        supply_label = Text("Supply", font_size=30, color=RED).next_to(supply_graph, DOWN + RIGHT, buff=0.2)

        # 4. Find and mark the Equilibrium Point
        # Equilibrium occurs where Demand = Supply: 10 - Q = Q => 2Q = 10 => Q = 5
        # At Q=5, P = 5.
        equilibrium_q = 5
        equilibrium_p = 5
        
        # Get the Manim coordinates for the equilibrium point
        eq_point_coords = axes.coords_to_point(equilibrium_q, equilibrium_p)
        eq_dot = Dot(eq_point_coords, color=BLACK, radius=0.08)
        eq_label = Text("Equilibrium", font_size=25, color=BLACK).next_to(eq_dot, UP + RIGHT, buff=0.1)

        # Draw dashed lines from equilibrium to axes
        h_line = axes.get_h_line(eq_point_coords, color=GRAY, stroke_width=2, stroke_dash_array=[5, 5])
        v_line = axes.get_v_line(eq_point_coords, color=GRAY, stroke_width=2, stroke_dash_array=[5, 5])

        # Add labels for equilibrium price (Pe) and quantity (Qe)
        pe_label = Text("Pe", font_size=25, color=BLACK).next_to(h_line, LEFT, buff=0.1)
        qe_label = Text("Qe", font_size=25, color=BLACK).next_to(v_line, DOWN, buff=0.1)

        # --- Animation Sequence ---
        self.play(Create(axes_group), run_time=2)
        self.wait(0.5)

        self.play(Create(demand_graph), Write(demand_label), run_time=2)
        self.wait(0.5)

        self.play(Create(supply_graph), Write(supply_label), run_time=2)
        self.wait(0.5)

        self.play(
            Create(eq_dot),
            Write(eq_label),
            run_time=1.5
        )
        self.wait(0.5)

        self.play(
            Create(h_line),
            Create(v_line),
            Write(pe_label),
            Write(qe_label),
            run_time=2
        )
        self.wait(2)