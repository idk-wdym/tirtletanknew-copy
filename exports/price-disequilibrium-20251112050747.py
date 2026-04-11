from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure scene resolution and background
        self.camera.background_color = WHITE
        config.frame_width = 16  # 1920 / 120 = 16
        config.frame_height = 9   # 1080 / 120 = 9
        config.frame_rate = 30

        # --- 1. Setup Axes ---
        # Define the axes for Quantity (x-axis) and Price (y-axis)
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 12, 2],
            x_length=7,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": True},
        ).to_edge(DOWN_LEFT).shift(RIGHT*1.5 + UP*1.5)

        # Add labels for the axes
        x_label = axes.get_x_axis_label(Text("Quantity", color=BLACK).scale(0.7))
        y_label = axes.get_y_axis_label(Text("Price", color=BLACK).scale(0.7)).shift(LEFT*0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # --- 2. Define and Draw Demand and Supply Curves ---
        # Demand function: P = 10 - Q
        demand_func = lambda x: 10 - x
        # Supply function: P = 2 + 0.5Q
        supply_func = lambda x: 2 + 0.5 * x

        # Plot the demand curve
        demand_curve = axes.plot(demand_func, x_range=[0, 10], color=BLUE)
        demand_label = axes.get_graph_label(
            demand_curve, label="D", x_val=9, direction=UP + RIGHT, color=BLUE
        ).scale(0.8)

        self.play(Create(demand_curve), Write(demand_label))
        self.wait(0.5)

        # Plot the supply curve
        supply_curve = axes.plot(supply_func, x_range=[0, 10], color=RED)
        supply_label = axes.get_graph_label(
            supply_curve, label="S", x_val=9, direction=UP + RIGHT, color=RED
        ).scale(0.8)

        self.play(Create(supply_curve), Write(supply_label))
        self.wait(1)

        # --- 3. Identify Equilibrium ---
        # Calculate equilibrium point: 10 - Q = 2 + 0.5Q => 8 = 1.5Q => Q_e = 16/3
        q_eq = 16 / 3
        p_eq = demand_func(q_eq) # or supply_func(q_eq)

        # Mark the equilibrium point
        eq_point_coords = axes.coords_to_point(q_eq, p_eq)
        eq_dot = Dot(eq_point_coords, color=GREEN, radius=0.08)

        # Draw dashed lines to the axes for equilibrium price and quantity
        eq_h_line = DashedLine(axes.coords_to_point(0, p_eq), eq_point_coords, color=GREEN)
        eq_v_line = DashedLine(axes.coords_to_point(q_eq, 0), eq_point_coords, color=GREEN)

        # Add labels for equilibrium price and quantity
        p_eq_label = MathTex("P_e", color=GREEN).scale(0.7).next_to(eq_h_line, LEFT, buff=0.1)
        q_eq_label = MathTex("Q_e", color=GREEN).scale(0.7).next_to(eq_v_line, DOWN, buff=0.1)
        equilibrium_text = Text("Equilibrium", color=GREEN).scale(0.6).next_to(eq_dot, UP + RIGHT, buff=0.2)

        self.play(Create(eq_dot), Create(eq_h_line), Create(eq_v_line))
        self.play(Write(p_eq_label), Write(q_eq_label), Write(equilibrium_text))
        self.wait(2)

        # --- 4. Demonstrate Surplus (Price above equilibrium) ---
        # Choose a price above equilibrium
        p_surplus = 7

        # Calculate quantity demanded and supplied at this price
        q_d_surplus = demand_func(p_surplus) # Q = 10 - P => Q = 10 - 7 = 3
        q_s_surplus = (p_surplus - 2) / 0.5 # P = 2 + 0.5Q => 0.5Q = P - 2 => Q = (P - 2) / 0.5 => Q = (7 - 2) / 0.5 = 10

        # Draw a horizontal line at the surplus price
        surplus_price_line = Line(
            axes.coords_to_point(0, p_surplus),
            axes.coords_to_point(q_s_surplus, p_surplus),
            color=ORANGE
        )
        surplus_price_label = MathTex("P_S", color=ORANGE).scale(0.7).next_to(surplus_price_line, LEFT, buff=0.1)

        # Highlight the surplus quantity (Q_s - Q_d)
        surplus_segment = Line(
            axes.coords_to_point(q_d_surplus, p_surplus),
            axes.coords_to_point(q_s_surplus, p_surplus),
            color=ORANGE,
            stroke_width=5
        )
        surplus_text = Text("Surplus", color=ORANGE).scale(0.6).next_to(surplus_segment, UP, buff=0.1)

        self.play(
            FadeOut(equilibrium_text),
            FadeOut(eq_h_line), FadeOut(eq_v_line),
            FadeOut(p_eq_label), FadeOut(q_eq_label),
            FadeOut(eq_dot)
        )
        self.play(Create(surplus_price_line), Write(surplus_price_label))
        self.play(Create(surplus_segment), Write(surplus_text))
        self.wait(2)
        self.play(
            FadeOut(surplus_price_line), FadeOut(surplus_price_label),
            FadeOut(surplus_segment), FadeOut(surplus_text)
        )
        self.wait(0.5)

        # --- 5. Demonstrate Shortage (Price below equilibrium) ---
        # Choose a price below equilibrium
        p_shortage = 2.5

        # Calculate quantity demanded and supplied at this price
        q_d_shortage = demand_func(p_shortage) # Q = 10 - P => Q = 10 - 2.5 = 7.5
        q_s_shortage = (p_shortage - 2) / 0.5 # Q = (2.5 - 2) / 0.5 = 1

        # Draw a horizontal line at the shortage price
        shortage_price_line = Line(
            axes.coords_to_point(0, p_shortage),
            axes.coords_to_point(q_d_shortage, p_shortage),
            color=PURPLE
        )
        shortage_price_label = MathTex("P_H", color=PURPLE).scale(0.7).next_to(shortage_price_line, LEFT, buff=0.1)

        # Highlight the shortage quantity (Q_d - Q_s)
        shortage_segment = Line(
            axes.coords_to_point(q_s_shortage, p_shortage),
            axes.coords_to_point(q_d_shortage, p_shortage),
            color=PURPLE,
            stroke_width=5
        )
        shortage_text = Text("Shortage", color=PURPLE).scale(0.6).next_to(shortage_segment, DOWN, buff=0.1)

        self.play(Create(shortage_price_line), Write(shortage_price_label))
        self.play(Create(shortage_segment), Write(shortage_text))
        self.wait(2)
        self.play(
            FadeOut(shortage_price_line), FadeOut(shortage_price_label),
            FadeOut(shortage_segment), FadeOut(shortage_text)
        )
        self.wait(0.5)

        # Re-show equilibrium for a final view
        self.play(
            Create(eq_dot), Create(eq_h_line), Create(eq_v_line),
            Write(p_eq_label), Write(q_eq_label), Write(equilibrium_text)
        )
        self.wait(2)

        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(demand_curve), FadeOut(demand_label),
            FadeOut(supply_curve), FadeOut(supply_label),
            FadeOut(eq_dot), FadeOut(eq_h_line), FadeOut(eq_v_line),
            FadeOut(p_eq_label), FadeOut(q_eq_label), FadeOut(equilibrium_text)
        )
        self.wait(1)