from manim import *

# Configure Manim's global settings for 1920x1080 resolution at 30 FPS
config.frame_width = 16  # Corresponds to 1920 pixels width
config.frame_height = 9  # Corresponds to 1080 pixels height
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = WHITE # Set background to white

class GeneratedScene(Scene):
    def construct(self):
        # --- 1. Setup Axes and Curves ---
        # Define axes for Quantity (x-axis) and Price (y-axis)
        axes = Axes(
            x_range=[0, 10, 1],  # Quantity from 0 to 10, with major ticks every 1 unit
            y_range=[0, 12, 1],  # Price from 0 to 12, with major ticks every 1 unit
            x_length=7,          # Length of the x-axis in Manim units
            y_length=6,          # Length of the y-axis in Manim units
            axis_config={"include_numbers": True, "font_size": 24, "color": BLACK},
            tips=False           # Do not include arrows at the end of axes
        ).to_edge(DOWN + LEFT) # Position axes to leave space for titles at the top

        # Labels for axes
        x_label = axes.get_x_axis_label(Text("Quantity (Q)").scale(0.7).set_color(BLACK), edge=DOWN, direction=DR)
        y_label = axes.get_y_axis_label(Text("Price (P)").scale(0.7).set_color(BLACK), edge=LEFT, direction=UL)
        axes_labels = VGroup(x_label, y_label)

        # Define linear demand and supply functions
        # Demand: P = 10 - Q
        demand_func = lambda q: 10 - q
        # Supply: P = 2 + Q
        supply_func = lambda q: 2 + q

        # Calculate the equilibrium point where demand equals supply (10 - Q = 2 + Q => 2Q = 8 => Q=4, P=6)
        equilibrium_q = 4
        equilibrium_p = 6
        equilibrium_point_coords = (equilibrium_q, equilibrium_p)
        equilibrium_point = axes.coords_to_point(*equilibrium_point_coords)

        # Plot demand and supply curves using the defined functions
        demand_curve = axes.plot(demand_func, x_range=[0, 8], color=BLUE)
        supply_curve = axes.plot(supply_func, x_range=[0, 8], color=RED)

        # Labels for the demand and supply curves
        demand_label = MathTex("D").next_to(demand_curve, DR, buff=0.1).set_color(BLUE)
        supply_label = MathTex("S").next_to(supply_curve, UR, buff=0.1).set_color(RED)

        # --- 2. Introduce Market Equilibrium ---
        title_equilibrium = Text("Market Equilibrium").to_edge(UP).set_color(BLACK)
        self.play(Write(title_equilibrium))
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(demand_curve), Write(demand_label))
        self.play(Create(supply_curve), Write(supply_label))

        # Mark the equilibrium point with a dot and dashed lines to the axes
        eq_dot = Dot(equilibrium_point, color=YELLOW, radius=0.1)
        eq_q_line = DashedLine(equilibrium_point, axes.coords_to_point(equilibrium_q, 0), color=GRAY)
        eq_p_line = DashedLine(equilibrium_point, axes.coords_to_point(0, equilibrium_p), color=GRAY)
        
        # Labels for equilibrium quantity (Q*) and price (P*)
        eq_q_label = MathTex("Q^*").next_to(eq_q_line, DOWN, buff=0.1).set_color(BLACK)
        eq_p_label = MathTex("P^*").next_to(eq_p_line, LEFT, buff=0.1).set_color(BLACK)

        self.play(Create(eq_dot))
        self.play(Create(eq_q_line), Write(eq_q_label), Create(eq_p_line), Write(eq_p_label))
        self.wait(1.5)

        # --- 3. Disequilibrium: Surplus ---
        # Fade out equilibrium labels and introduce the surplus title
        self.play(FadeOut(title_equilibrium, eq_q_label, eq_p_label))
        title_surplus = Text("Price Disequilibrium: Surplus").to_edge(UP).set_color(BLACK)
        self.play(Write(title_surplus))

        # Introduce a price P1 above the equilibrium price
        p1 = 8
        p1_line = Line(axes.coords_to_point(0, p1), axes.coords_to_point(axes.x_range[1], p1), color=PURPLE)
        p1_label = MathTex("P_1").next_to(p1_line, LEFT, buff=0.1).set_color(PURPLE)

        # Calculate quantities demanded and supplied at P1
        qd1 = 10 - p1  # Quantity demanded at P1
        qs1 = p1 - 2   # Quantity supplied at P1

        qd1_point = axes.coords_to_point(qd1, p1)
        qs1_point = axes.coords_to_point(qs1, p1)

        # Draw vertical dashed lines from P1 to the x-axis for Qd1 and Qs1
        qd1_line_v = DashedLine(qd1_point, axes.coords_to_point(qd1, 0), color=GRAY)
        qs1_line_v = DashedLine(qs1_point, axes.coords_to_point(qs1, 0), color=GRAY)

        # Labels for quantities demanded and supplied at P1
        qd1_label = MathTex("Q_{D1}").next_to(qd1_line_v, DOWN, buff=0.1).set_color(BLACK)
        qs1_label = MathTex("Q_{S1}").next_to(qs1_line_v, DOWN, buff=0.1).set_color(BLACK)

        # Highlight the surplus area (Qs1 - Qd1)
        surplus_rect = Rectangle(
            width=axes.x_unit_size * (qs1 - qd1), # Width in Manim units
            height=axes.y_unit_size * (p1 - equilibrium_p), # Height in Manim units
            color=YELLOW,
            fill_opacity=0.3,
            stroke_width=0 # No border for the rectangle
        )
        # Position the rectangle at the center of the surplus area
        surplus_rect.move_to(axes.coords_to_point((qd1 + qs1) / 2, (p1 + equilibrium_p) / 2))
        surplus_text = Text("Surplus", font_size=36).move_to(surplus_rect).set_color(BLACK)

        self.play(Create(p1_line), Write(p1_label))
        self.play(
            Create(qd1_line_v), Write(qd1_label),
            Create(qs1_line_v), Write(qs1_label)
        )
        self.play(FadeIn(surplus_rect, surplus_text))
        self.wait(2.5)

        # --- 4. Disequilibrium: Shortage ---
        # Fade out surplus elements and introduce the shortage title
        self.play(
            FadeOut(p1_line, p1_label, qd1_line_v, qd1_label, qs1_line_v, qs1_label, surplus_rect, surplus_text, title_surplus)
        )
        title_shortage = Text("Price Disequilibrium: Shortage").to_edge(UP).set_color(BLACK)
        self.play(Write(title_shortage))

        # Introduce a price P2 below the equilibrium price
        p2 = 4
        p2_line = Line(axes.coords_to_point(0, p2), axes.coords_to_point(axes.x_range[1], p2), color=ORANGE)
        p2_label = MathTex("P_2").next_to(p2_line, LEFT, buff=0.1).set_color(ORANGE)

        # Calculate quantities demanded and supplied at P2
        qs2 = p2 - 2   # Quantity supplied at P2
        qd2 = 10 - p2  # Quantity demanded at P2

        qs2_point = axes.coords_to_point(qs2, p2)
        qd2_point = axes.coords_to_point(qd2, p2)

        # Draw vertical dashed lines from P2 to the x-axis for Qs2 and Qd2
        qs2_line_v = DashedLine(qs2_point, axes.coords_to_point(qs2, 0), color=GRAY)
        qd2_line_v = DashedLine(qd2_point, axes.coords_to_point(qd2, 0), color=GRAY)

        # Labels for quantities supplied and demanded at P2
        qs2_label = MathTex("Q_{S2}").next_to(qs2_line_v, DOWN, buff=0.1).set_color(BLACK)
        qd2_label = MathTex("Q_{D2}").next_to(qd2_line_v, DOWN, buff=0.1).set_color(BLACK)

        # Highlight the shortage area (Qd2 - Qs2)
        shortage_rect = Rectangle(
            width=axes.x_unit_size * (qd2 - qs2), # Width in Manim units
            height=axes.y_unit_size * (equilibrium_p - p2), # Height in Manim units
            color=YELLOW,
            fill_opacity=0.3,
            stroke_width=0
        )
        # Position the rectangle at the center of the shortage area
        shortage_rect.move_to(axes.coords_to_point((qs2 + qd2) / 2, (p2 + equilibrium_p) / 2))
        shortage_text = Text("Shortage", font_size=36).move_to(shortage_rect).set_color(BLACK)

        self.play(Create(p2_line), Write(p2_label))
        self.play(
            Create(qs2_line_v), Write(qs2_label),
            Create(qd2_line_v), Write(qd2_label)
        )
        self.play(FadeIn(shortage_rect, shortage_text))
        self.wait(2.5)

        # --- 5. Conclusion ---
        # Fade out shortage elements and re-emphasize equilibrium
        self.play(
            FadeOut(p2_line, p2_label, qs2_line_v, qs2_label, qd2_line_v, qd2_label, shortage_rect, shortage_text, title_shortage)
        )
        self.play(FadeIn(eq_q_label, eq_p_label)) # Bring back equilibrium labels
        final_title = Text("Market Dynamics: Towards Equilibrium").to_edge(UP).set_color(BLACK)
        self.play(Write(final_title))
        self.wait(2)
        
        # Fade out all remaining elements to end the scene cleanly
        self.play(
            FadeOut(
                final_title, axes, axes_labels, demand_curve, supply_curve,
                demand_label, supply_label, eq_dot, eq_q_line, eq_p_line,
                eq_q_label, eq_p_label
            )
        )
        self.wait(1)