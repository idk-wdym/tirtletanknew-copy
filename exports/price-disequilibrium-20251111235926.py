from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # --- Configuration ---
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.frame_rate = 30
        self.camera.background_color = WHITE

        # --- 1. Setup Axes ---
        # Define the functions for supply and demand
        # Demand: P = 10 - Q  => Q = 10 - P
        # Supply: P = 2 + Q   => Q = P - 2
        # Equilibrium: Q* = 4, P* = 6

        # Axes for Quantity (Q) and Price (P)
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 12, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": BLACK, "include_numbers": True, "font_size": 24},
            x_axis_config={"numbers_to_include": [2, 4, 6, 8]},
            y_axis_config={"numbers_to_include": [2, 4, 6, 8, 10]},
        ).to_edge(DOWN + LEFT, buff=1.0)
        axes.add_coordinates()

        # Labels for axes
        x_label = axes.get_x_axis_label(Tex("Quantity (Q)", color=BLACK).scale(0.8))
        y_label = axes.get_y_axis_label(Tex("Price (P)", color=BLACK).scale(0.8).rotate(90 * DEGREES))

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # --- 2. Supply and Demand Curves ---
        # Demand function: P = 10 - Q
        demand_func = lambda q: 10 - q
        demand_curve = axes.get_graph(demand_func, x_range=[0, 10], color=BLUE)
        demand_label = MathTex("D", color=BLUE).next_to(demand_curve, UP + RIGHT, buff=0.1)

        # Supply function: P = 2 + Q
        supply_func = lambda q: 2 + q
        supply_curve = axes.get_graph(supply_func, x_range=[0, 8], color=RED) # Limit x_range to avoid going off graph
        supply_label = MathTex("S", color=RED).next_to(supply_curve, UP + LEFT, buff=0.1)

        self.play(Create(demand_curve), Write(demand_label))
        self.play(Create(supply_curve), Write(supply_label))
        self.wait(1)

        # --- 3. Equilibrium ---
        equilibrium_q = 4
        equilibrium_p = 6
        equilibrium_point = axes.coords_to_point(equilibrium_q, equilibrium_p)

        eq_dot = Dot(equilibrium_point, color=GREEN, radius=0.1)
        eq_label = MathTex("E", color=GREEN).next_to(eq_dot, UP + RIGHT, buff=0.1)

        # Dashed lines for equilibrium price and quantity
        eq_q_line = DashedLine(equilibrium_point, axes.coords_to_point(equilibrium_q, 0), color=GRAY)
        eq_p_line = DashedLine(equilibrium_point, axes.coords_to_point(0, equilibrium_p), color=GRAY)

        eq_q_label = MathTex("Q^*", color=BLACK).next_to(eq_q_line, DOWN, buff=0.1)
        eq_p_label = MathTex("P^*", color=BLACK).next_to(eq_p_line, LEFT, buff=0.1)

        self.play(
            Create(eq_q_line),
            Create(eq_p_line),
            FadeIn(eq_q_label),
            FadeIn(eq_p_label),
            Create(eq_dot),
            Write(eq_label)
        )
        self.wait(2)

        # --- Title for the scene ---
        title = Text("Price Disequilibrium", color=BLACK).scale(1.2).to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # --- 4. Disequilibrium - Surplus (Price above equilibrium) ---
        self.play(
            FadeOut(eq_q_line, eq_p_line, eq_q_label, eq_p_label, eq_dot, eq_label),
            FadeOut(title)
        )
        self.wait(0.5)

        # New title for surplus
        surplus_title = Text("Surplus (Price above Equilibrium)", color=BLACK).scale(1.1).to_edge(UP, buff=0.5)
        self.play(Write(surplus_title))

        price_high = 8
        p_high_line = DashedLine(axes.coords_to_point(0, price_high), axes.coords_to_point(10, price_high), color=PURPLE)
        p_high_label = MathTex("P_1", color=PURPLE).next_to(p_high_line, LEFT, buff=0.1)

        self.play(Create(p_high_line), Write(p_high_label))
        self.wait(1)

        # Quantity demanded at P_high
        q_demanded_high = 10 - price_high # Q = 2
        q_demanded_high_point = axes.coords_to_point(q_demanded_high, price_high)
        q_demanded_high_dot = Dot(q_demanded_high_point, color=BLUE, radius=0.08)
        q_demanded_high_label = MathTex("Q_D", color=BLUE).next_to(axes.coords_to_point(q_demanded_high, 0), DOWN, buff=0.1)
        q_demanded_high_line = DashedLine(q_demanded_high_point, axes.coords_to_point(q_demanded_high, 0), color=BLUE)

        # Quantity supplied at P_high
        q_supplied_high = price_high - 2 # Q = 6
        q_supplied_high_point = axes.coords_to_point(q_supplied_high, price_high)
        q_supplied_high_dot = Dot(q_supplied_high_point, color=RED, radius=0.08)
        q_supplied_high_label = MathTex("Q_S", color=RED).next_to(axes.coords_to_point(q_supplied_high, 0), DOWN, buff=0.1)
        q_supplied_high_line = DashedLine(q_supplied_high_point, axes.coords_to_point(q_supplied_high, 0), color=RED)

        self.play(
            Create(q_demanded_high_line), FadeIn(q_demanded_high_dot), FadeIn(q_demanded_high_label),
            Create(q_supplied_high_line), FadeIn(q_supplied_high_dot), FadeIn(q_supplied_high_label)
        )
        self.wait(1)

        # Highlight the surplus area
        surplus_rect = Rectangle(
            width=axes.x_unit_size * (q_supplied_high - q_demanded_high),
            height=axes.y_unit_size * 0.5, # Small height for visual clarity
            color=YELLOW,
            fill_opacity=0.6
        ).move_to(axes.coords_to_point((q_demanded_high + q_supplied_high) / 2, price_high))

        surplus_text = Text("Surplus", color=BLACK).scale(0.8).move_to(surplus_rect.get_center())

        self.play(FadeIn(surplus_rect), Write(surplus_text))
        self.wait(2)

        # --- 5. Disequilibrium - Shortage (Price below equilibrium) ---
        self.play(
            FadeOut(p_high_line, p_high_label, q_demanded_high_line, q_demanded_high_dot, q_demanded_high_label,
                    q_supplied_high_line, q_supplied_high_dot, q_supplied_high_label,
                    surplus_rect, surplus_text, surplus_title)
        )
        self.wait(0.5)

        # New title for shortage
        shortage_title = Text("Shortage (Price below Equilibrium)", color=BLACK).scale(1.1).to_edge(UP, buff=0.5)
        self.play(Write(shortage_title))

        price_low = 4
        p_low_line = DashedLine(axes.coords_to_point(0, price_low), axes.coords_to_point(10, price_low), color=ORANGE)
        p_low_label = MathTex("P_2", color=ORANGE).next_to(p_low_line, LEFT, buff=0.1)

        self.play(Create(p_low_line), Write(p_low_label))
        self.wait(1)

        # Quantity demanded at P_low
        q_demanded_low = 10 - price_low # Q = 6
        q_demanded_low_point = axes.coords_to_point(q_demanded_low, price_low)
        q_demanded_low_dot = Dot(q_demanded_low_point, color=BLUE, radius=0.08)
        q_demanded_low_label = MathTex("Q_D", color=BLUE).next_to(axes.coords_to_point(q_demanded_low, 0), DOWN, buff=0.1)
        q_demanded_low_line = DashedLine(q_demanded_low_point, axes.coords_to_point(q_demanded_low, 0), color=BLUE)

        # Quantity supplied at P_low
        q_supplied_low = price_low - 2 # Q = 2
        q_supplied_low_point = axes.coords_to_point(q_supplied_low, price_low)
        q_supplied_low_dot = Dot(q_supplied_low_point, color=RED, radius=0.08)
        q_supplied_low_label = MathTex("Q_S", color=RED).next_to(axes.coords_to_point(q_supplied_low, 0), DOWN, buff=0.1)
        q_supplied_low_line = DashedLine(q_supplied_low_point, axes.coords_to_point(q_supplied_low, 0), color=RED)

        self.play(
            Create(q_demanded_low_line), FadeIn(q_demanded_low_dot), FadeIn(q_demanded_low_label),
            Create(q_supplied_low_line), FadeIn(q_supplied_low_dot), FadeIn(q_supplied_low_label)
        )
        self.wait(1)

        # Highlight the shortage area
        shortage_rect = Rectangle(
            width=axes.x_unit_size * (q_demanded_low - q_supplied_low),
            height=axes.y_unit_size * 0.5, # Small height for visual clarity
            color=YELLOW,
            fill_opacity=0.6
        ).move_to(axes.coords_to_point((q_supplied_low + q_demanded_low) / 2, price_low))

        shortage_text = Text("Shortage", color=BLACK).scale(0.8).move_to(shortage_rect.get_center())

        self.play(FadeIn(shortage_rect), Write(shortage_text))
        self.wait(2)

        # --- 6. Cleanup and Final State ---
        self.play(
            FadeOut(p_low_line, p_low_label, q_demanded_low_line, q_demanded_low_dot, q_demanded_low_label,
                    q_supplied_low_line, q_supplied_low_dot, q_supplied_low_label,
                    shortage_rect, shortage_text, shortage_title)
        )
        self.wait(0.5)

        # Return to equilibrium state
        final_title = Text("Equilibrium Restored", color=BLACK).scale(1.1).to_edge(UP, buff=0.5)
        self.play(Write(final_title))

        self.play(
            Create(eq_q_line),
            Create(eq_p_line),
            FadeIn(eq_q_label),
            FadeIn(eq_p_label),
            Create(eq_dot),
            Write(eq_label)
        )
        self.wait(3)

        self.play(
            FadeOut(axes, x_label, y_label, demand_curve, demand_label,
                    supply_curve, supply_label, eq_q_line, eq_p_line,
                    eq_q_label, eq_p_label, eq_dot, eq_label, final_title)
        )
        self.wait(1)