from manim import *

# Configure Manim for 1920x1080 @ 30fps
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class GeneratedScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # --- 1. Setup Axes for Price and Quantity ---
        axes = Axes(
            x_range=[0, 10, 1],  # Quantity (Q) from 0 to 10
            y_range=[0, 12, 1],  # Price (P) from 0 to 12
            x_length=7,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": True},
            tips=True
        ).to_edge(DOWN + LEFT, buff=1.0)

        x_label = Text("Quantity (Q)", font_size=28, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Price (P)", font_size=28, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.2).rotate(90 * DEGREES)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        self.wait(0.5)

        # --- 2. Define and Draw Supply and Demand Curves ---
        # Demand function: P = -Q + 10
        demand_func = lambda q: -q + 10
        # Supply function: P = Q + 2
        supply_func = lambda q: q + 2

        demand_curve = axes.get_graph(demand_func, x_range=[0, 10], color=BLUE)
        supply_curve = axes.get_graph(supply_func, x_range=[0, 10], color=RED)

        demand_label = Text("Demand (D)", font_size=28, color=BLUE).next_to(demand_curve, UP + RIGHT, buff=0.1).shift(LEFT*0.5)
        supply_label = Text("Supply (S)", font_size=28, color=RED).next_to(supply_curve, UP + LEFT, buff=0.1).shift(RIGHT*0.5)

        self.play(
            Create(demand_curve),
            Write(demand_label)
        )
        self.wait(0.5)
        self.play(
            Create(supply_curve),
            Write(supply_label)
        )
        self.wait(1)

        # --- 3. Find and Mark Equilibrium ---
        eq_q = 4  # Equilibrium Quantity
        eq_p = 6  # Equilibrium Price
        equilibrium_point = axes.coords_to_point(eq_q, eq_p)
        eq_dot = Dot(equilibrium_point, color=GREEN, radius=0.08)

        eq_q_line = DashedLine(equilibrium_point, axes.coords_to_point(eq_q, 0), color=GREEN)
        eq_p_line = DashedLine(equilibrium_point, axes.coords_to_point(0, eq_p), color=GREEN)

        eq_q_label = Text("Qₑ", font_size=28, color=GREEN).next_to(eq_q_line, DOWN, buff=0.1)
        eq_p_label = Text("Pₑ", font_size=28, color=GREEN).next_to(eq_p_line, LEFT, buff=0.1)

        equilibrium_text = Text("Market Equilibrium", font_size=36, color=GREEN).to_edge(UP, buff=0.5)

        self.play(
            Create(eq_dot),
            Create(eq_q_line),
            Create(eq_p_line),
            Write(eq_q_label),
            Write(eq_p_label),
            Write(equilibrium_text)
        )
        self.wait(2)

        self.play(FadeOut(equilibrium_text))
        self.wait(0.5)

        # --- 4. Illustrate Disequilibrium: Surplus (Price above equilibrium) ---
        price_high = 8
        p_high_line = Line(axes.coords_to_point(0, price_high), axes.coords_to_point(10, price_high), color=ORANGE, stroke_width=3)
        p_high_label = Text("P₁ (Above Pₑ)", font_size=28, color=ORANGE).next_to(p_high_line, UP, buff=0.1).shift(RIGHT*2)

        # Calculate quantities demanded (Qd) and supplied (Qs) at P_high
        # From P = -Q + 10 => Q = 10 - P
        qd_high_val = 10 - price_high
        # From P = Q + 2 => Q = P - 2
        qs_high_val = price_high - 2

        qd_high_point = axes.coords_to_point(qd_high_val, price_high)
        qs_high_point = axes.coords_to_point(qs_high_val, price_high)

        qd_high_line_v = DashedLine(qd_high_point, axes.coords_to_point(qd_high_val, 0), color=ORANGE)
        qs_high_line_v = DashedLine(qs_high_point, axes.coords_to_point(qs_high_val, 0), color=ORANGE)

        qd_high_label = Text("Qd", font_size=24, color=ORANGE).next_to(qd_high_line_v, DOWN, buff=0.1)
        qs_high_label = Text("Qs", font_size=24, color=ORANGE).next_to(qs_high_line_v, DOWN, buff=0.1)

        surplus_rect = Rectangle(
            width=axes.x_axis.get_unit_size() * (qs_high_val - qd_high_val),
            height=0.2,
            color=ORANGE,
            fill_opacity=0.6
        ).move_to(axes.coords_to_point((qd_high_val + qs_high_val) / 2, price_high))

        surplus_text = Text("Surplus (Qs > Qd)", font_size=36, color=ORANGE).to_edge(UP, buff=0.5)

        self.play(
            Create(p_high_line),
            Write(p_high_label)
        )
        self.wait(0.5)
        self.play(
            Create(qd_high_line_v),
            Create(qs_high_line_v),
            Write(qd_high_label),
            Write(qs_high_label)
        )
        self.wait(0.5)
        self.play(
            FadeIn(surplus_rect),
            Write(surplus_text)
        )
        self.wait(2)

        self.play(
            FadeOut(p_high_line),
            FadeOut(p_high_label),
            FadeOut(qd_high_line_v),
            FadeOut(qs_high_line_v),
            FadeOut(qd_high_label),
            FadeOut(qs_high_label),
            FadeOut(surplus_rect),
            FadeOut(surplus_text)
        )
        self.wait(1)

        # --- 5. Illustrate Disequilibrium: Shortage (Price below equilibrium) ---
        price_low = 4
        p_low_line = Line(axes.coords_to_point(0, price_low), axes.coords_to_point(10, price_low), color=PURPLE, stroke_width=3)
        p_low_label = Text("P₂ (Below Pₑ)", font_size=28, color=PURPLE).next_to(p_low_line, DOWN, buff=0.1).shift(RIGHT*2)

        # Calculate quantities demanded (Qd) and supplied (Qs) at P_low
        qd_low_val = 10 - price_low
        qs_low_val = price_low - 2

        qd_low_point = axes.coords_to_point(qd_low_val, price_low)
        qs_low_point = axes.coords_to_point(qs_low_val, price_low)

        qd_low_line_v = DashedLine(qd_low_point, axes.coords_to_point(qd_low_val, 0), color=PURPLE)
        qs_low_line_v = DashedLine(qs_low_point, axes.coords_to_point(qs_low_val, 0), color=PURPLE)

        qd_low_label = Text("Qd", font_size=24, color=PURPLE).next_to(qd_low_line_v, DOWN, buff=0.1)
        qs_low_label = Text("Qs", font_size=24, color=PURPLE).next_to(qs_low_line_v, DOWN, buff=0.1)

        shortage_rect = Rectangle(
            width=axes.x_axis.get_unit_size() * (qd_low_val - qs_low_val),
            height=0.2,
            color=PURPLE,
            fill_opacity=0.6
        ).move_to(axes.coords_to_point((qs_low_val + qd_low_val) / 2, price_low))

        shortage_text = Text("Shortage (Qd > Qs)", font_size=36, color=PURPLE).to_edge(UP, buff=0.5)

        self.play(
            Create(p_low_line),
            Write(p_low_label)
        )
        self.wait(0.5)
        self.play(
            Create(qd_low_line_v),
            Create(qs_low_line_v),
            Write(qd_low_label),
            Write(qs_low_label)
        )
        self.wait(0.5)
        self.play(
            FadeIn(shortage_rect),
            Write(shortage_text)
        )
        self.wait(2)

        self.play(
            FadeOut(p_low_line),
            FadeOut(p_low_label),
            FadeOut(qd_low_line_v),
            FadeOut(qs_low_line_v),
            FadeOut(qd_low_label),
            FadeOut(qs_low_label),
            FadeOut(shortage_rect),
            FadeOut(shortage_text)
        )
        self.wait(1)

        # Final title
        final_title = Text("Price Disequilibrium", font_size=48, color=BLACK).to_edge(UP, buff=0.5)
        self.play(Transform(eq_dot, Dot(eq_dot.get_center(), color=GREEN, radius=0.15)))
        self.play(Write(final_title))
        self.wait(3)

        self.play(
            FadeOut(final_title),
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