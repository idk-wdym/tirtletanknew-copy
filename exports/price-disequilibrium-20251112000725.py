from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure camera for 1920x1080 resolution and white background
        # Note: Resolution and FPS are typically set via manim.cfg or command line flags
        # (e.g., manim -pql --resolution 1920x1080 --fps 30 your_script.py GeneratedScene)
        self.camera.background_color = WHITE

        # --- 1. Setup Axes ---
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False, "color": BLACK},
        ).to_edge(DOWN + LEFT, buff=1.0)

        # Axis labels
        quantity_label = Text("Quantity", color=BLACK).scale(0.7).next_to(axes.x_axis, DOWN, buff=0.2)
        price_label = Text("Price", color=BLACK).scale(0.7).rotate(PI / 2).next_to(axes.y_axis, LEFT, buff=0.2)

        self.play(
            Create(axes),
            Write(quantity_label),
            Write(price_label)
        )
        self.wait(0.5)

        # --- 2. Define Supply and Demand Functions ---
        # Demand function: P = 8 - 0.7Q
        demand_func = lambda x: 8 - 0.7 * x
        # Supply function: P = 2 + 0.5Q
        supply_func = lambda x: 2 + 0.5 * x

        demand_curve = axes.plot(demand_func, x_range=[0, 10], color=BLUE, stroke_width=4)
        supply_curve = axes.plot(supply_func, x_range=[0, 10], color=RED, stroke_width=4)

        demand_text = Text("Demand", color=BLUE).scale(0.6).next_to(demand_curve, UP + RIGHT, buff=0.1)
        supply_text = Text("Supply", color=RED).scale(00.6).next_to(supply_curve, UP + LEFT, buff=0.1)

        self.play(
            Create(demand_curve),
            Write(demand_text)
        )
        self.wait(0.5)
        self.play(
            Create(supply_curve),
            Write(supply_text)
        )
        self.wait(1)

        # --- 3. Find and Mark Equilibrium ---
        # Equilibrium: 8 - 0.7Q = 2 + 0.5Q => 6 = 1.2Q => Q_e = 5
        # P_e = 8 - 0.7 * 5 = 4.5
        equilibrium_q = 5
        equilibrium_p = 4.5

        equilibrium_dot = Dot(axes.coords_to_point(equilibrium_q, equilibrium_p), color=GREEN, radius=0.1)
        
        eq_price_line = axes.get_horizontal_line(equilibrium_dot.get_center(), color=GREEN, line_func=Line)
        eq_quantity_line = axes.get_vertical_line(equilibrium_dot.get_center(), color=GREEN, line_func=Line)

        eq_price_label = Text("Pₑ", color=GREEN).scale(0.6).next_to(eq_price_line, LEFT, buff=0.1)
        eq_quantity_label = Text("Qₑ", color=GREEN).scale(0.6).next_to(eq_quantity_line, DOWN, buff=0.1)

        self.play(
            FadeIn(equilibrium_dot, scale=0.5),
            Create(eq_price_line),
            Create(eq_quantity_line),
            Write(eq_price_label),
            Write(eq_quantity_label)
        )
        self.wait(2)

        # --- 4. Introduce Disequilibrium (Surplus) ---
        # Set a price above equilibrium, e.g., P_high = 6
        price_high = 6
        price_high_line = axes.get_horizontal_line(axes.coords_to_point(0, price_high), color=ORANGE, stroke_width=3)
        price_high_label = Text("P_high", color=ORANGE).scale(0.6).next_to(price_high_line, LEFT, buff=0.1)

        self.play(
            Create(price_high_line),
            Write(price_high_label)
        )
        self.wait(1)

        # Quantity demanded at P_high: 6 = 8 - 0.7Q => 0.7Q = 2 => Q_d = 2 / 0.7 ≈ 2.857
        q_demanded_at_phigh = (8 - price_high) / 0.7
        # Quantity supplied at P_high: 6 = 2 + 0.5Q => 0.5Q = 4 => Q_s = 8
        q_supplied_at_phigh = (price_high - 2) / 0.5

        q_d_dot = Dot(axes.coords_to_point(q_demanded_at_phigh, price_high), color=ORANGE, radius=0.08)
        q_s_dot = Dot(axes.coords_to_point(q_supplied_at_phigh, price_high), color=ORANGE, radius=0.08)

        q_d_line = Line(q_d_dot.get_center(), axes.coords_to_point(q_demanded_at_phigh, 0), color=ORANGE, stroke_width=2, dash_length=0.1)
        q_s_line = Line(q_s_dot.get_center(), axes.coords_to_point(q_supplied_at_phigh, 0), color=ORANGE, stroke_width=2, dash_length=0.1)

        q_d_label = Text("Q_d", color=ORANGE).scale(0.5).next_to(q_d_line, DOWN, buff=0.1)
        q_s_label = Text("Q_s", color=ORANGE).scale(0.5).next_to(q_s_line, DOWN, buff=0.1)

        self.play(
            FadeIn(q_d_dot, scale=0.5),
            Create(q_d_line),
            Write(q_d_label)
        )
        self.wait(0.5)
        self.play(
            FadeIn(q_s_dot, scale=0.5),
            Create(q_s_line),
            Write(q_s_label)
        )
        self.wait(1)

        # Highlight the surplus
        surplus_line = Line(q_d_dot.get_center(), q_s_dot.get_center(), color=YELLOW, stroke_width=6)
        surplus_text = Text("Surplus", color=YELLOW).scale(0.7).next_to(surplus_line, UP, buff=0.1)

        self.play(
            Create(surplus_line),
            Write(surplus_text)
        )
        self.wait(2)

        # --- 5. Introduce Disequilibrium (Shortage) ---
        # Set a price below equilibrium, e.g., P_low = 3
        price_low = 3
        price_low_line = axes.get_horizontal_line(axes.coords_to_point(0, price_low), color=PURPLE, stroke_width=3)
        price_low_label = Text("P_low", color=PURPLE).scale(0.6).next_to(price_low_line, LEFT, buff=0.1)

        self.play(
            FadeOut(surplus_line, surplus_text, q_d_dot, q_s_dot, q_d_line, q_s_line, q_d_label, q_s_label, price_high_line, price_high_label),
            Create(price_low_line),
            Write(price_low_label)
        )
        self.wait(1)

        # Quantity demanded at P_low: 3 = 8 - 0.7Q => 0.7Q = 5 => Q_d = 5 / 0.7 ≈ 7.14
        q_demanded_at_plow = (8 - price_low) / 0.7
        # Quantity supplied at P_low: 3 = 2 + 0.5Q => 0.5Q = 1 => Q_s = 2
        q_supplied_at_plow = (price_low - 2) / 0.5

        q_d_dot_low = Dot(axes.coords_to_point(q_demanded_at_plow, price_low), color=PURPLE, radius=0.08)
        q_s_dot_low = Dot(axes.coords_to_point(q_supplied_at_plow, price_low), color=PURPLE, radius=0.08)

        q_d_line_low = Line(q_d_dot_low.get_center(), axes.coords_to_point(q_demanded_at_plow, 0), color=PURPLE, stroke_width=2, dash_length=0.1)
        q_s_line_low = Line(q_s_dot_low.get_center(), axes.coords_to_point(q_supplied_at_plow, 0), color=PURPLE, stroke_width=2, dash_length=0.1)

        q_d_label_low = Text("Q_d", color=PURPLE).scale(0.5).next_to(q_d_line_low, DOWN, buff=0.1)
        q_s_label_low = Text("Q_s", color=PURPLE).scale(0.5).next_to(q_s_line_low, DOWN, buff=0.1)

        self.play(
            FadeIn(q_s_dot_low, scale=0.5),
            Create(q_s_line_low),
            Write(q_s_label_low)
        )
        self.wait(0.5)
        self.play(
            FadeIn(q_d_dot_low, scale=0.5),
            Create(q_d_line_low),
            Write(q_d_label_low)
        )
        self.wait(1)

        # Highlight the shortage
        shortage_line = Line(q_s_dot_low.get_center(), q_d_dot_low.get_center(), color=ORANGE, stroke_width=6)
        shortage_text = Text("Shortage", color=ORANGE).scale(0.7).next_to(shortage_line, DOWN, buff=0.1)

        self.play(
            Create(shortage_line),
            Write(shortage_text)
        )
        self.wait(3)

        self.play(
            FadeOut(
                axes, quantity_label, price_label,
                demand_curve, supply_curve, demand_text, supply_text,
                equilibrium_dot, eq_price_line, eq_quantity_line, eq_price_label, eq_quantity_label,
                price_low_line, price_low_label,
                q_d_dot_low, q_s_dot_low, q_d_line_low, q_s_line_low, q_d_label_low, q_s_label_low,
                shortage_line, shortage_text
            )
        )